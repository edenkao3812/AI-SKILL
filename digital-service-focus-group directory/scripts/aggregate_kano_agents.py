#!/usr/bin/env python3
"""Validate four isolated role submissions and aggregate exploratory Kano scores."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path


ROLES = (
    "直覺型潛在用戶",
    "品牌行銷總監",
    "毒舌鄉民／風險控管",
    "商業定位分析師",
)
ANSWERS = ("很愉悅", "理所當然", "沒感覺", "可以忍受", "無法接受")
CODES = "AMOIRX"
NAME_SCORES = ("fit", "memory", "oral", "visual", "search_risk")
MATRIX = (
    ("X", "A", "A", "A", "O"),
    ("R", "I", "I", "I", "M"),
    ("R", "I", "I", "I", "M"),
    ("R", "I", "I", "I", "M"),
    ("R", "R", "R", "R", "X"),
)


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def read_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read JSON {path}: {exc}") from exc
    require(isinstance(data, dict), f"{path}: top level must be an object")
    return data


def validate_view(view: object, location: str) -> None:
    require(isinstance(view, dict), f"{location}: view must be an object")
    for key in ("position", "basis", "risk", "recommendation"):
        require(nonempty(view.get(key)), f"{location}: missing {key}")


def validate_score_map(scores: object, keys: tuple[str, ...] | str, location: str) -> None:
    require(isinstance(scores, dict), f"{location}: scores must be an object")
    require(set(scores) == set(keys), f"{location}: score keys must be {','.join(keys)}")
    for key in keys:
        val = scores[key]
        require(type(val) is int and 1 <= val <= 10, f"{location}: {key} must be an integer from 1 to 10")


def validate_manifest(manifest: dict) -> tuple[list[dict], list[str]]:
    require(nonempty(manifest.get("version")), "manifest: version is required")
    functions = manifest.get("functions")
    names = manifest.get("names")
    require(isinstance(functions, list) and len(functions) >= 10, "manifest: at least 10 functions required")
    for idx, item in enumerate(functions, 1):
        require(isinstance(item, dict), f"manifest: function {idx} must be an object")
        require(item.get("id") == f"F{idx}", f"manifest: expected function ID F{idx}")
        require(nonempty(item.get("name")), f"manifest: F{idx} needs a name")
    require(len({f["name"] for f in functions}) == len(functions), "manifest: duplicate function names")
    require(isinstance(names, list) and len(names) == 5, "manifest: exactly five names required")
    require(all(nonempty(n) for n in names) and len(set(names)) == 5, "manifest: names must be distinct, nonempty strings")
    return functions, names


def validate_round_a(data: dict, path: Path) -> None:
    loc = str(path)
    require(data.get("schema_version") == "1.0" and data.get("round") == "A", f"{loc}: wrong schema/round")
    require(data.get("role") in ROLES, f"{loc}: unexpected role")
    require(nonempty(data.get("task_id")), f"{loc}: actual task_id required")
    for stage in ("stage1_view", "stage2_view"):
        validate_view(data.get(stage), f"{loc}/{stage}")
    proposals = data.get("feature_proposals")
    require(isinstance(proposals, list) and proposals, f"{loc}: feature_proposals must be nonempty")
    for idx, proposal in enumerate(proposals, 1):
        require(isinstance(proposal, dict), f"{loc}: proposal {idx} must be an object")
        for key in ("name", "journey", "reason", "risk"):
            require(nonempty(proposal.get(key)), f"{loc}: proposal {idx} missing {key}")
    directions = data.get("naming_directions")
    require(isinstance(directions, list) and directions and all(nonempty(v) for v in directions), f"{loc}: naming_directions required")


def validate_round_b(data: dict, path: Path, functions: list[dict], names: list[str]) -> None:
    loc = str(path)
    require(data.get("schema_version") == "1.0" and data.get("round") == "B", f"{loc}: wrong schema/round")
    require(data.get("role") in ROLES, f"{loc}: unexpected role")
    require(nonempty(data.get("task_id")), f"{loc}: actual task_id required")
    for stage in ("stage3_view", "stage4_view", "stage5_view"):
        validate_view(data.get(stage), f"{loc}/{stage}")
    rows = data.get("functions")
    require(isinstance(rows, list) and len(rows) == len(functions), f"{loc}: function count differs from manifest")
    expected_ids = {f["id"] for f in functions}
    require({r.get("id") for r in rows if isinstance(r, dict)} == expected_ids, f"{loc}: function IDs differ from manifest")
    for row in rows:
        fid = row["id"]
        require(row.get("positive") in ANSWERS and row.get("negative") in ANSWERS, f"{loc}/{fid}: invalid paired answer")
        code = MATRIX[ANSWERS.index(row["positive"])][ANSWERS.index(row["negative"])]
        require(row.get("primary") == code, f"{loc}/{fid}: primary {row.get('primary')} does not match matrix {code}")
        validate_score_map(row.get("scores"), CODES, f"{loc}/{fid}")
        require(nonempty(row.get("rationale")) and nonempty(row.get("overturn")), f"{loc}/{fid}: rationale and overturn required")
    name_rows = data.get("names")
    require(isinstance(name_rows, list) and len(name_rows) == 5, f"{loc}: exactly five name scores required")
    require({r.get("name") for r in name_rows if isinstance(r, dict)} == set(names), f"{loc}: names differ from manifest")
    for row in name_rows:
        label = row["name"]
        validate_score_map(row.get("scores"), NAME_SCORES, f"{loc}/{label}")
        require(nonempty(row.get("rationale")) and nonempty(row.get("risk")), f"{loc}/{label}: rationale and risk required")


def aggregate(functions: list[dict], names: list[str], a_by_role: dict, b_by_role: dict, version: str) -> dict:
    items = []
    chart = []
    for feature in functions:
        fid = feature["id"]
        rows = [next(r for r in b_by_role[role]["functions"] if r["id"] == fid) for role in ROLES]
        totals = {code: sum(row["scores"][code] for row in rows) for code in CODES}
        counts = dict(Counter(row["primary"] for row in rows))
        counts = {code: counts.get(code, 0) for code in CODES}
        denominator = sum(totals[code] for code in "AMOI")
        rigid = (totals["M"] + totals["O"]) / denominator if denominator else None
        ideal = (totals["A"] + totals["O"]) / denominator if denominator else None
        high = max(totals.values())
        review_flags = []
        if high and totals["R"] >= 0.9 * high:
            review_flags.append("R_near_or_dominant")
        if high and totals["X"] >= 0.9 * high:
            review_flags.append("X_near_or_dominant")
        if totals["X"] == high and totals["R"] == high:
            quadrant = "R_X_REVIEW"
        elif totals["X"] == high:
            quadrant = "X_REVIEW"
        elif totals["R"] == high:
            quadrant = "R_REVIEW"
        elif denominator == 0:
            quadrant = "X_REVIEW"
        elif rigid >= .5 and ideal >= .5:
            quadrant = "Q1"
        elif rigid >= .5:
            quadrant = "Q4"
        elif ideal >= .5:
            quadrant = "Q2"
        else:
            quadrant = "Q3"
        item = dict(id=fid, function=feature["name"], scores=totals, primary_counts=counts,
                    denominator=denominator, rigid=round(rigid, 4) if rigid is not None else None,
                    ideal=round(ideal, 4) if ideal is not None else None, quadrant=quadrant,
                    review_flags=review_flags,
                    r_share_of_high=round(totals["R"] / high, 4) if high else None,
                    x_share_of_high=round(totals["X"] / high, 4) if high else None)
        items.append(item)
        if quadrant in ("Q1", "Q4", "Q2", "Q3"):
            chart.append(dict(id=fid, function=feature["name"], rigid=f"{rigid:.2f}",
                              ideal=f"{ideal:.2f}", quadrant=quadrant,
                              decision={"Q1": "P0", "Q4": "P0", "Q2": "P1", "Q3": "P2"}[quadrant]))

    name_items = []
    for name in names:
        score_rows = [next(r for r in b_by_role[role]["names"] if r["name"] == name)["scores"] for role in ROLES]
        means = {key: round(sum(row[key] for row in score_rows) / 4, 1) for key in NAME_SCORES}
        name_items.append(dict(name=name, mean_scores=means, total=round(sum(means.values()), 1),
                               per_role={role: score_rows[i] for i, role in enumerate(ROLES)}))

    return dict(source_type="four_independent_ai_agent_simulation_not_customer_data",
                manifest_version=version,
                agents=[dict(role=role, task_id=a_by_role[role]["task_id"]) for role in ROLES],
                functions=items, names=name_items, chart_rows=chart,
                methodology="Exploratory score-weighted Kano heuristic; formal respondent surveys use category counts separately.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--round-a", type=Path, nargs=4, required=True)
    parser.add_argument("--round-b", type=Path, nargs=4, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = read_json(args.manifest)
        functions, names = validate_manifest(manifest)
        a_by_role = {}
        b_by_role = {}
        for path in args.round_a:
            data = read_json(path)
            validate_round_a(data, path)
            role = data["role"]
            require(role not in a_by_role, f"duplicate Round A role: {role}")
            a_by_role[role] = data
        for path in args.round_b:
            data = read_json(path)
            validate_round_b(data, path, functions, names)
            role = data["role"]
            require(role not in b_by_role, f"duplicate Round B role: {role}")
            b_by_role[role] = data
        require(set(a_by_role) == set(ROLES) and set(b_by_role) == set(ROLES), "all four distinct roles required in both rounds")
        task_ids = []
        for role in ROLES:
            require(a_by_role[role]["task_id"] == b_by_role[role]["task_id"], f"{role}: task_id changed across rounds")
            task_ids.append(a_by_role[role]["task_id"])
        require(len(set(task_ids)) == 4, "four distinct agent task IDs required")
        result = aggregate(functions, names, a_by_role, b_by_role, manifest["version"])
        args.out.mkdir(parents=True, exist_ok=True)
        json_path = args.out / "kano-agent-summary.json"
        csv_path = args.out / "kano-chart-input.csv"
        require(not json_path.exists() and not csv_path.exists(), "output files already exist; use a fresh --out directory")
        json_path.write_text(json.dumps({k: v for k, v in result.items() if k != "chart_rows"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=("id", "function", "rigid", "ideal", "quadrant", "decision"))
            writer.writeheader()
            writer.writerows(result["chart_rows"])
        print(json_path)
        print(csv_path)
        return 0
    except ValidationError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
