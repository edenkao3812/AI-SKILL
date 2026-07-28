#!/usr/bin/env python3
"""Generate a readable KANO rigid-demand x ideal-demand quadrant SVG."""

from __future__ import annotations

import csv
import html
import sys
from pathlib import Path


WIDTH = 1100
HEIGHT = 780
LEFT = 95
RIGHT = 360
TOP = 70
BOTTOM = 95
PLOT_W = WIDTH - LEFT - RIGHT
PLOT_H = HEIGHT - TOP - BOTTOM


def x_pos(value: float) -> float:
    return LEFT + max(0.0, min(1.0, value)) * PLOT_W


def y_pos(value: float) -> float:
    return TOP + (1.0 - max(0.0, min(1.0, value))) * PLOT_H


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def load_points(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    required = {"id", "function", "rigid", "ideal", "quadrant", "decision"}
    missing = required.difference(rows[0].keys() if rows else [])
    if missing:
        raise SystemExit(f"Missing CSV columns: {', '.join(sorted(missing))}")
    return rows


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: generate_kano_quadrant_svg.py <input.csv> <output.svg>", file=sys.stderr)
        return 2

    csv_path = Path(sys.argv[1])
    svg_path = Path(sys.argv[2])
    rows = load_points(csv_path)

    colors = {
        "Q1": "#0f766e",
        "Q2": "#7c3aed",
        "Q3": "#64748b",
        "Q4": "#b45309",
    }

    parts: list[str] = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">')
    parts.append('<rect width="100%" height="100%" fill="#ffffff"/>')
    parts.append(f'<rect x="{LEFT}" y="{TOP}" width="{PLOT_W}" height="{PLOT_H}" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>')
    parts.append(f'<line x1="{x_pos(0.5)}" y1="{TOP}" x2="{x_pos(0.5)}" y2="{TOP + PLOT_H}" stroke="#334155" stroke-width="1.2" stroke-dasharray="7 6"/>')
    parts.append(f'<line x1="{LEFT}" y1="{y_pos(0.5)}" x2="{LEFT + PLOT_W}" y2="{y_pos(0.5)}" stroke="#334155" stroke-width="1.2" stroke-dasharray="7 6"/>')

    for tick in [0, 0.25, 0.5, 0.75, 1.0]:
        x = x_pos(tick)
        y = y_pos(tick)
        parts.append(f'<line x1="{x}" y1="{TOP + PLOT_H}" x2="{x}" y2="{TOP + PLOT_H + 7}" stroke="#0f172a"/>')
        parts.append(f'<text x="{x}" y="{TOP + PLOT_H + 28}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#0f172a">{tick:.2f}</text>')
        parts.append(f'<line x1="{LEFT - 7}" y1="{y}" x2="{LEFT}" y2="{y}" stroke="#0f172a"/>')
        parts.append(f'<text x="{LEFT - 14}" y="{y + 5}" text-anchor="end" font-family="Arial, sans-serif" font-size="14" fill="#0f172a">{tick:.2f}</text>')

    parts.append(f'<text x="{LEFT + PLOT_W / 2}" y="35" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#0f172a">KANO 剛性需求 × 理想需求</text>')
    parts.append(f'<text x="{LEFT + PLOT_W / 2}" y="{HEIGHT - 28}" text-anchor="middle" font-family="Arial, sans-serif" font-size="17" fill="#0f172a">剛性需求 = (M + O) / (A + M + O + I)</text>')
    parts.append(f'<text x="26" y="{TOP + PLOT_H / 2}" transform="rotate(-90 26 {TOP + PLOT_H / 2})" text-anchor="middle" font-family="Arial, sans-serif" font-size="17" fill="#0f172a">理想需求 = (A + O) / (A + M + O + I)</text>')

    labels = [
        ("Q1 核心競爭需求", 0.75, 0.92),
        ("Q2 理想／魅力需求", 0.25, 0.92),
        ("Q3 低效需求", 0.25, 0.08),
        ("Q4 基本剛性需求", 0.75, 0.08),
    ]
    for text, xval, yval in labels:
        parts.append(f'<text x="{x_pos(xval)}" y="{y_pos(yval)}" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#334155">{esc(text)}</text>')

    used_offsets: dict[tuple[int, int], int] = {}
    for row in rows:
        rigid = float(row["rigid"])
        ideal = float(row["ideal"])
        key = (round(rigid * 100), round(ideal * 100))
        offset = used_offsets.get(key, 0)
        used_offsets[key] = offset + 1
        px = x_pos(rigid) + (offset % 3) * 12
        py = y_pos(ideal) - (offset // 3) * 12
        quadrant = row["quadrant"].strip().upper()
        color = colors.get(quadrant, "#0f172a")
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="10" fill="{color}" stroke="#ffffff" stroke-width="2"/>')
        parts.append(f'<text x="{px + 14:.1f}" y="{py + 5:.1f}" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="{color}">{esc(row["id"])}</text>')

    legend_x = LEFT + PLOT_W + 35
    legend_y = TOP + 10
    parts.append(f'<text x="{legend_x}" y="{legend_y}" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#0f172a">圖例</text>')
    for i, row in enumerate(rows):
        y = legend_y + 32 + i * 28
        quadrant = row["quadrant"].strip().upper()
        color = colors.get(quadrant, "#0f172a")
        label = f'{row["id"]} {row["function"]} ({row["rigid"]}, {row["ideal"]}, {quadrant}, {row["decision"]})'
        parts.append(f'<circle cx="{legend_x + 8}" cy="{y - 5}" r="6" fill="{color}"/>')
        parts.append(f'<text x="{legend_x + 22}" y="{y}" font-family="Arial, sans-serif" font-size="13" fill="#0f172a">{esc(label)}</text>')

    parts.append("</svg>")
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text("\n".join(parts), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
