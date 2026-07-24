---
name: digital-service-focus-group
description: Simulate a five-role, five-stage focus group for a digital service name and early concept, using Chinese participant names throughout, then save a UTF-8 Markdown management report with each stage split into 討論 and 產出, detailed role-opinion tables, service focus and TA, at least 10 observable service functions with more added when justified, per-role KANO A/M/O/I/R/X judgments, rigid-demand and ideal-demand coefficients, a real KANO quadrant SVG embedded directly inside the Markdown file, evidence-based feature priorities, and five distinctive names with one recommended fancy name. Use paired functional/dysfunctional KANO questions and calculate rigid demand as (M+O)/(A+M+O+I) and ideal demand as (A+O)/(A+M+O+I). Use when the user says "Focusgroup this:", "Focus group this:", "焦點小組", "數位服務焦點小組", "KANO", "測試服務名稱", "幫服務取名", "Fancy 名稱", "服務名稱壓力測試", or asks to evaluate a digital service idea, expose role-based trade-offs, classify service qualities, plot KANO priorities, plan an MVP, or produce a management-ready Markdown focus-group report. Do not use for simple fact lookup, document summarization, fixed products that cannot change, or isolated technical implementation questions without a service or business concept.
---

# 數位服務焦點小組

Run a simulated focus group for one digital service. Treat the participants as analytical lenses, not real research participants. Use Chinese participant names in the report. Do not expose verbatim role-play, hidden chain-of-thought, or private reasoning. Summarize each participant's position, business reason, agreements, trade-offs, and the moderator's decision.

## 解析輸入

Extract:

1. Proposed service name.
2. Initial concept, problem, audience, geography, market, channel, business model, and constraints.
3. Any naming style, forbidden terms, brand personality, language, or feature constraints.

Start immediately for inputs such as:

- `Focusgroup this: 租車APP`
- `焦點小組測試「照護通」這個長照媒合服務。`
- `幫這個數位服務取一個 Fancy 名稱，並排出最重要的 MVP 功能。`

If only a name is supplied, infer the most plausible service concept and label it `[暫定假設]`. Ask one concise question only if the name is too ambiguous to support a useful decision; otherwise proceed.

## 使用五個中文角色

Use these participant names exactly in user-facing output:

1. **主持人** — control scope, separate evidence from assumptions, resolve contradictions, and make management decisions.
2. **直覺型潛在用戶** — test whether a non-technical user understands the problem, benefit, trust requirement, name, and critical journey.
3. **品牌行銷總監** — assess distinctiveness, memorability, pronunciation, visual extensibility, word of mouth, and campaign potential.
4. **毒舌鄉民／風險控管** — attack vague claims, abuse cases, hidden costs, awkward wording, negative associations, legal exposure, and public-relations risks.
5. **商業定位分析師** — assess market category, competitors, differentiation, SEO, business model, operating constraints, and preliminary trademark collision risk.

Do not display the English role names. Do not let one participant dominate or force false consensus.

## 標示證據品質

Tag material claims where useful:

- `[已知]` — supplied by the user.
- `[外部查證]` — supported by a cited current source.
- `[暫定假設]` — inferred to allow analysis.
- `[待驗證]` — material but unsupported.

Never label an AI-simulated preference as customer evidence.

## 執行五階段討論

For each stage, record two explicit blocks in this order:

1. **討論** — the decision question and the structured role-opinion table.
2. **產出** — the stage deliverable: consensus, disagreement/trade-off, moderator ruling, gate, and the concrete artifact created by that stage.

Inside the discussion block, record:

1. **關鍵決策問題**
2. **角色觀點表** — for each non-moderator participant, give 2–4 complete sentences covering the position, reasoning or observation, risk or objection, and concrete recommendation. Use a Markdown table rather than compressed one-line bullets.

Inside the output block, record:

3. **共識**
4. **核心分歧與取捨**
5. **主持人裁定**
6. **決策閘門** — choose exactly one:
   - `前進` — evidence is sufficient for the stated next step.
   - `修正後前進` — viable after a defined change.
   - `先驗證` — a named test is required before commitment.
   - `停止` — weak value or unacceptable risk invalidates the direction.

### 第一階段：服務聚焦與 TA 界定

- State the job to be done in one sentence.
- Identify the painful current alternative and promised improvement.
- Define one primary persona with context, trigger, desired outcome, and adoption barrier.
- End with a gate on whether the problem and audience are specific enough.

### 第二階段：服務項目展開

- Cover acquisition, search or discovery, core transaction, trust and safety, support, retention, and operator needs.
- Rewrite vague ideas as observable functions.
- Produce at least 10 service functions. Add more than 10 when the service has materially distinct journeys, users, risks, revenue mechanics, operator workflows, compliance needs, or lifecycle stages that would otherwise be compressed into vague mega-functions.
- Do not pad with decorative or duplicate functions. Each added function must be observable, testable, and materially different from the others.
- Number functions sequentially as `F1`, `F2`, `F3`, and so on. If more than 10 functions are used, continue with `F11`, `F12`, etc. Keep these IDs stable across every later section.
- Challenge operational burden, privacy, misuse, accessibility, and positioning drift.
- End with a gate on whether one coherent end-to-end journey exists.

### 第三階段：逐角色 KANO 判定與交叉詰問

Read [references/kano-model.md](references/kano-model.md) completely before classifying any function.

For every candidate function, require each of the four non-moderator roles to state:

- the positive-question answer;
- the negative-question answer;
- the resulting A/M/O/I/R/X code from the matrix;
- why that classification fits the service and target audience;
- what evidence could overturn the judgment.

Present these judgments in a function-by-role table. Do not collapse the four roles into one answer before showing their individual positions. When real customer data is unavailable, mark all role judgments `[暫定假設]`; they are simulated votes, not research evidence.

### 第四階段：KANO 係數計算、圖表與優先順序

For each function, count the four role judgments or real respondent results as A, M, O, I, R, and X. Let `N = A + M + O + I`.

- `剛性需求 = (M + O) / (A + M + O + I)`
- `理想需求 = (A + O) / (A + M + O + I)`

Exclude R and X from both denominators, but report their counts. If `N = 0`, return `N/A` and require re-survey. Show the substituted numbers and result to two decimal places for every function.

Create a real rendered quadrant image and embed it directly inside the Markdown file. Do not include a fenced `mermaid` block by default, because some Codex/Desktop Markdown renderers auto-render Mermaid and can fail on `quadrantChart` syntax or localized labels.

1. Generate a real SVG image file under the same `output/` directory as the Markdown report, using the preferred pattern `<report-stem>-kano-quadrant.svg`.
2. Inline the SVG markup inside the Markdown report immediately under `## 6. KANO 四象限圖與功能優先順序`, between `<!-- KANO_QUADRANT_SVG_START -->` and `<!-- KANO_QUADRANT_SVG_END -->`.
3. The Markdown report must be self-contained for the chart: opening only the `.md` file must still show the chart in renderers that support inline SVG. Do not rely only on `![KANO 四象限圖](...)` or any external image link.
4. The external SVG file may still be saved as an audit artifact, but it is a backup, not the primary embedded chart.
5. The SVG must contain axes, quadrant split lines at 0.50, quadrant labels, plotted points, point labels, and a legend mapping point IDs to function names. It must be readable without relying on Mermaid rendering.
6. If inline SVG is technically unavailable in the target renderer, embed a base64 PNG or SVG data URI and explicitly state the limitation in the report. A plain external file link alone is not sufficient.
7. If editable chart source is useful, include it in a fenced `text` block titled `Mermaid source (not auto-rendered)`, not in a fenced `mermaid` block.

Use these chart rules:

- x-axis = 剛性需求, from 0 to 1;
- y-axis = 理想需求, from 0 to 1;
- both split lines at 0.50;
- short point IDs such as F1, F2, and a legend mapping IDs to function names.

Use these universal quadrants:

| Quadrant | Rule | Meaning | Default decision |
|---|---|---|---|
| Q1 | rigid ≥ 0.50 and ideal ≥ 0.50 | core competitive demand | P0, build first |
| Q4 | rigid ≥ 0.50 and ideal < 0.50 | baseline rigid demand | P0, complete before launch |
| Q2 | rigid < 0.50 and ideal ≥ 0.50 | ideal or delight demand | P1, differentiation phase |
| Q3 | rigid < 0.50 and ideal < 0.50 | low-effect demand | P2 or no investment |

Order and present development decisions as four visible groups, not only as one flat list:

1. **第一象限 Q1：核心競爭需求** — P0, build first.
2. **第四象限 Q4：基本剛性需求** — P0, complete before launch.
3. **第二象限 Q2：理想／魅力需求** — P1, differentiation phase.
4. **第三象限 Q3：低效需求** — P2, postpone or avoid investment.

Within Q1 and Q4, sort by rigid demand descending and then ideal demand descending. Within Q2, sort by ideal demand descending and then rigid demand descending. Within Q3, show equal low priority unless the user supplies another rule. Route a dominant R result to avoid/remove and a dominant X result to re-survey instead of plotting it as a normal priority.

Every function must keep its service function ID everywhere it appears. Use labels like `F2｜完整總價與費用明細`, not just the function name, in the executive summary, discussion outputs, quadrant legend, grouped development-decision tables, and final next steps.

### 第五階段：名稱壓力測試與 Fancy 命名

First evaluate the supplied name for:

- five-second comprehension;
- pronunciation, spelling, recall, and oral transmission;
- fit with service promise and expansion;
- visual and campaign extensibility;
- homophones, slang, abbreviations, cultural and accessibility risks;
- search-result crowding, competitor confusion, domain or handle discoverability, and preliminary trademark risk.

Then generate exactly five distinctive candidate names:

- Use five different naming territories when practical: benefit, emotion, metaphor, coined word, and category twist.
- Favor a concise, pronounceable core brand over a generic description.
- Pair a less obvious name with a clear descriptor or tagline.
- Avoid small spelling variations of the same idea.
- Do not claim domain, handle, or trademark availability without verification.

Score each candidate from 1–10 on:

- service fit;
- memorability;
- oral transmission;
- visual extensibility;
- search and risk defensibility.

Select exactly one **首選 Fancy 名稱**. Explain why it wins, provide a one-line tagline, and state any unverified naming risks.

For current competitor, SEO, domain, handle, or trademark claims, browse when tools are available and cite links inline. Treat trademark review as preliminary screening, never legal clearance. If tools are unavailable, mark the check `[待驗證]` and name the exact registry or platform to search. Never invent search volume, availability, registrations, or legal conclusions.

## 形成企業決策

State:

- the one decision management must make now;
- the recommended fancy name;
- the core service promise;
- the P0 feature scope;
- explicit non-goals;
- confidence level: `High`, `Medium`, or `Low`;
- critical assumptions and cost of being wrong;
- one measurable validation action.

Do not merely say "change the name." Deliver five candidates and choose one. Do not merely list features. Prioritize them and define why they matter and how MVP completion can be verified.

## 圖表產生腳本

Prefer using `scripts/generate_kano_quadrant_svg.py` for the rendered KANO chart after the coefficient table is finalized.

Create an input CSV with headers:

`id,function,rigid,ideal,quadrant,decision`

Only include functions with numeric coefficients. Exclude dominant R functions marked remove/avoid and dominant X functions marked re-survey from normal plotted priority points; mention them in the priority table instead.

Run:

```powershell
python scripts/generate_kano_quadrant_svg.py <input.csv> <output.svg>
```

Then embed the contents of `<output.svg>` directly in the Markdown report between the KANO SVG markers. Keep `<output.svg>` as a backup artifact. If source is included, place it in a `text` fenced block so it does not auto-render.

## 輸出契約

Write in the user's language unless asked otherwise. Use the following Markdown structure exactly. Keep participant summaries concise and decision fields specific.

```markdown
# 數位服務焦點小組分析報告

## 0. 企業決策摘要
* **現在必須決定：** [單一管理決策]
* **首選 Fancy 名稱：** [選定名稱]
* **一句話品牌承諾：** [核心價值]
* **P0 功能範圍：** [位於 Q1 與 Q4 的功能，逐項包含功能 ID，例如 F2｜完整總價與費用明細]
* **本階段明確不做：** [避免範圍膨脹的項目]
* **決策信心：** [High / Medium / Low＋依據]
* **關鍵假設與判斷錯誤代價：** [證據標籤＋主要代價]

## 1. 焦點小組討論摘要

### 第一階段｜服務聚焦與 TA 界定

#### 討論
* **關鍵決策問題：** [本階段管理問題]

| 角色 | 主要觀點 | 判斷依據 | 風險／反對意見 | 具體建議 |
|---|---|---|---|---|
| 直覺型潛在用戶 | [2–4 句] | [使用情境與痛點] | [採用障礙] | [具體調整] |
| 品牌行銷總監 | [2–4 句] | [傳播與接觸點] | [訊息風險] | [具體調整] |
| 毒舌鄉民／風險控管 | [2–4 句] | [漏洞與失敗情境] | [最壞後果] | [具體防範] |
| 商業定位分析師 | [2–4 句] | [市場與競爭證據] | [商業限制] | [具體聚焦] |

#### 產出
* **共識：** [共識]
* **核心分歧與取捨：** [真正影響決策的分歧]
* **主持人裁定：** [工作決定＋依據]
* **決策閘門：** [前進 / 修正後前進 / 先驗證 / 停止]
* **本階段產物：** [核心任務、TA Persona、採用障礙與成功判準]

### 第二階段｜服務項目展開

#### 討論
* **關鍵決策問題：** [本階段管理問題]

| 角色 | 主張納入的功能 | 判斷依據 | 反對或刪除項目 | 具體建議 |
|---|---|---|---|---|
| 直覺型潛在用戶 | [功能與理由，2–4 句] | [使用旅程] | [不需要的項目] | [操作期待] |
| 品牌行銷總監 | [功能與理由，2–4 句] | [價值感知] | [失焦風險] | [亮點設計] |
| 毒舌鄉民／風險控管 | [功能與理由，2–4 句] | [風險情境] | [高風險項目] | [控制措施] |
| 商業定位分析師 | [功能與理由，2–4 句] | [競品與商模] | [成本或定位問題] | [範圍收斂] |

#### 產出
* **共識：** [共識]
* **核心分歧與取捨：** [真正影響決策的分歧]
* **主持人裁定：** [工作決定＋依據]
* **決策閘門：** [前進 / 修正後前進 / 先驗證 / 停止]
* **本階段產物：** [可觀察功能清單與端到端服務旅程]

### 第三階段｜逐角色 KANO 判定與交叉詰問

#### 討論
* **關鍵決策問題：** [本階段管理問題]

| 角色 | 整體 KANO 觀點 | 最可能判為 M/O/A 的功能 | 爭議功能與理由 | 建議驗證 |
|---|---|---|---|---|
| 直覺型潛在用戶 | [2–4 句] | [功能＋類型] | [分歧] | [真實用戶問題] |
| 品牌行銷總監 | [2–4 句] | [功能＋類型] | [分歧] | [訊息或偏好測試] |
| 毒舌鄉民／風險控管 | [2–4 句] | [功能＋類型] | [分歧] | [反例或壓力測試] |
| 商業定位分析師 | [2–4 句] | [功能＋類型] | [分歧] | [市場驗證] |

#### 產出
* **共識：** [共識]
* **核心分歧與取捨：** [真正影響決策的分歧]
* **主持人裁定：** [工作決定＋依據]
* **決策閘門：** [前進 / 修正後前進 / 先驗證 / 停止]
* **本階段產物：** [每項功能的四角色 A/M/O/I/R/X 假設與待驗證問卷]

### 第四階段｜KANO 係數計算、圖表與優先順序

#### 討論
* **關鍵決策問題：** [本階段管理問題]

| 角色 | 對計算結果的解讀 | 認為最重要的功能 | 對優先順序的異議 | 建議決策 |
|---|---|---|---|---|
| 直覺型潛在用戶 | [2–4 句] | [功能＋係數] | [異議] | [建議] |
| 品牌行銷總監 | [2–4 句] | [功能＋係數] | [異議] | [建議] |
| 毒舌鄉民／風險控管 | [2–4 句] | [功能＋係數] | [異議] | [建議] |
| 商業定位分析師 | [2–4 句] | [功能＋係數] | [異議] | [建議] |

#### 產出
* **共識：** [共識]
* **核心分歧與取捨：** [真正影響決策的分歧]
* **主持人裁定：** [依係數與象限作出的決定]
* **決策閘門：** [前進 / 修正後前進 / 先驗證 / 停止]
* **本階段產物：** [剛性需求／理想需求係數表、實際四象限圖、功能優先順序]

### 第五階段｜名稱壓力測試與 Fancy 命名

#### 討論
* **關鍵決策問題：** [本階段管理問題]

| 角色 | 名稱評價 | 判斷依據 | 風險／反對意見 | 推薦方向 |
|---|---|---|---|---|
| 直覺型潛在用戶 | [2–4 句] | [秒懂度與口傳] | [誤解風險] | [建議] |
| 品牌行銷總監 | [2–4 句] | [記憶與延展] | [傳播限制] | [建議] |
| 毒舌鄉民／風險控管 | [2–4 句] | [諧音與公關] | [雷區] | [建議] |
| 商業定位分析師 | [2–4 句] | [SEO 與競品] | [商標或搜尋風險] | [建議] |

#### 產出
* **共識：** [共識]
* **核心分歧與取捨：** [真正影響決策的分歧]
* **主持人裁定：** [工作決定＋依據]
* **決策閘門：** [前進 / 修正後前進 / 先驗證 / 停止]
* **本階段產物：** [五個候選名稱、首選 Fancy 名稱、標語與命名風險]

## 2. 服務核心定位
* **核心問題：** [解決什麼問題]
* **主要 TA：** [具體 Persona]
* **差異化主張：** [為何選擇此服務]

## 3. 服務功能展開

| 功能 ID | 服務功能 | 對應旅程 | 解決的問題 | 主要使用者 | 營運依賴 | 主要風險 |
|---|---|---|---|---|---|---|
| F1 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F2 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F3 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F4 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F5 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F6 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F7 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F8 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F9 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |
| F10 | [可觀察功能] | [旅程階段] | [問題] | [角色] | [依賴] | [風險] |

## 4. 逐角色 KANO 判定

* **資料狀態：** [真實問卷／AI 焦點小組假設；無真實資料時標示「以下皆為暫定假設」]
* **判定方法：** [正向＋反向問題及 5×5 A/M/O/I/R/X 矩陣]

| 功能 ID | 功能 | 判定角色 | 具備時回答 | 不具備時回答 | KANO | 判定理由 | 可推翻此判定的證據 |
|---|---|---|---|---|---|---|---|
| F1 | [功能] | 直覺型潛在用戶 | [五選一] | [五選一] | [A/M/O/I/R/X] | [服務與 TA 理由] | [需驗證資料] |
| F1 | [功能] | 品牌行銷總監 | [五選一] | [五選一] | [A/M/O/I/R/X] | [服務與 TA 理由] | [需驗證資料] |
| F1 | [功能] | 毒舌鄉民／風險控管 | [五選一] | [五選一] | [A/M/O/I/R/X] | [服務與 TA 理由] | [需驗證資料] |
| F1 | [功能] | 商業定位分析師 | [五選一] | [五選一] | [A/M/O/I/R/X] | [服務與 TA 理由] | [需驗證資料] |

### 待驗證的 KANO 成對問卷

| 功能 ID | 正向問題：具備時 | 反向問題：不具備時 |
|---|---|---|
| F1 | 如果本服務具備［功能］，你的感受是？ | 如果本服務不具備［功能］，你的感受是？ |

統一回答選項：`很愉悅／理所當然／沒感覺／可以忍受／無法接受`

## 5. 剛性需求與理想需求計算

* **剛性需求公式：** `(M + O) / (A + M + O + I)`
* **理想需求公式：** `(A + O) / (A + M + O + I)`
* **例外規則：** R、X 不列入分母，但必須呈現；若分母為 0，標示 `N/A` 並重新問卷。

| 功能 ID | A | M | O | I | R | X | 剛性需求計算 | 剛性需求 | 理想需求計算 | 理想需求 | 象限 |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---|
| F1 | [票數] | [票數] | [票數] | [票數] | [票數] | [票數] | `(M+O)/N` | [0.00] | `(A+O)/N` | [0.00] | [Q1/Q2/Q3/Q4] |

## 6. KANO 四象限圖與功能優先順序

<!-- KANO_QUADRANT_SVG_START -->
<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="780" viewBox="0 0 1100 780" role="img" aria-label="KANO 四象限圖">
  [完整內嵌 SVG 圖表，不是外部圖片連結]
</svg>
<!-- KANO_QUADRANT_SVG_END -->

**Mermaid source (not auto-rendered):**

```text
quadrantChart
    title KANO 剛性需求 × 理想需求
    x-axis 低剛性需求 --> 高剛性需求
    y-axis 低理想需求 --> 高理想需求
    quadrant-1 核心競爭需求
    quadrant-2 理想／魅力需求
    quadrant-3 低效需求
    quadrant-4 基本剛性需求
    F1: [0.00, 0.00]
```

| 功能 ID | 功能名稱 |
|---|---|
| F1 | [功能] |

| 優先順序 | 功能 ID | 服務功能 | 主 KANO 類型 | 剛性需求 | 理想需求 | 象限 | 重要性解讀 | 開發決策 | MVP 驗收標準 |
|---:|---|---|---|---:|---:|---|---|---|---|
| 1 | F1 | [功能] | [A/M/O/I/R/X] | [0.00] | [0.00] | [Q1] | [為何重要] | [第一象限 Q1：P0，最先投入] | [可觀察標準] |

### 開發決策分組

#### 第一象限 Q1｜核心競爭需求

| 功能 ID | 服務功能 | 剛性需求 | 理想需求 | 開發決策 | MVP 驗收標準 |
|---|---|---:|---:|---|---|
| F1 | [功能] | [0.00] | [0.00] | [P0，最先投入] | [可觀察標準] |

#### 第四象限 Q4｜基本剛性需求

| 功能 ID | 服務功能 | 剛性需求 | 理想需求 | 開發決策 | MVP 驗收標準 |
|---|---|---:|---:|---|---|
| F2 | [功能] | [0.00] | [0.00] | [P0，上線前完成] | [可觀察標準] |

#### 第二象限 Q2｜理想／魅力需求

| 功能 ID | 服務功能 | 剛性需求 | 理想需求 | 開發決策 | MVP 驗收標準 |
|---|---|---:|---:|---|---|
| F3 | [功能] | [0.00] | [0.00] | [P1，差異化階段] | [可觀察標準] |

#### 第三象限 Q3｜低效需求

| 功能 ID | 服務功能 | 剛性需求 | 理想需求 | 開發決策 | MVP 驗收標準 |
|---|---|---:|---:|---|---|
| F4 | [功能] | [0.00] | [0.00] | [P2 或暫不投入] | [可觀察標準或不投入理由] |

#### 例外處理｜R 或 X 主導

| 功能 ID | 服務功能 | R/X 判定 | 開發決策 | 原因 |
|---|---|---|---|---|
| F5 | [功能] | [R/X 主導] | [移除／重測] | [原因] |

## 7. Fancy 名稱決策

| 候選名稱 | 命名概念 | 服務契合 | 記憶度 | 口語傳播 | 視覺延展 | 搜尋與風險防禦 | 總分 |
|---|---|---:|---:|---:|---:|---:|---:|
| [候選 1] | [概念] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] |
| [候選 2] | [概念] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] |
| [候選 3] | [概念] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] |
| [候選 4] | [概念] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] |
| [候選 5] | [概念] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] |

* **原名稱壓力測試：** [評分＋主要問題]
* **首選 Fancy 名稱：** [名稱＋勝出理由]
* **品牌標語：** [一句話 tagline]
* **命名風險：** [商標、SEO、網域、語意或公關風險；標示查證狀態]

## 8. 最終裁決與下一步
* **最終裁決：** [採用首選名稱／修改後再測／重新命名＋產品方向]
* **核准進入下一階段的條件：** [量化門檻]
* **第一個行動：** [單一、明確、可衡量的驗證行動]
```

## Markdown 檔案交付

Always deliver the complete report as a `.md` file, not only as chat text.

1. Use a user-specified destination when provided; otherwise create or reuse `output/` under the current working directory.
2. Build a readable filename from the selected brand or supplied service name:
   - preferred pattern: `<service-slug>-focus-group-report.md`
   - example: `tripkey-car-rental-focus-group-report.md`
3. Save as UTF-8 Markdown.
4. Never overwrite an existing file. If the preferred filename exists, append `-v2`, `-v3`, and so on.
5. Write the full report structure to the file with no placeholders.
6. Re-read the saved file and verify all required headings, five discussion stages, role-opinion tables, five name candidates, per-role KANO judgments, both demand coefficients, the rendered quadrant image, priority matrix, and final decision are present.
7. Generate and re-open or inspect the real KANO quadrant SVG file. Verify it exists and is non-empty. Then verify the SVG markup is directly embedded in the Markdown between `KANO_QUADRANT_SVG_START` and `KANO_QUADRANT_SVG_END`; an external image link alone does not pass.
8. In the chat response, provide only a concise result summary plus clickable absolute links to the Markdown report and the rendered quadrant image.
9. If filesystem writing is technically unavailable, return the complete Markdown in chat and clearly state that the file could not be created.

Before sending, verify:

- All user-facing participant names are Chinese.
- All five stages are split into `#### 討論` and `#### 產出`, and contain a detailed role-opinion table, one consequential disagreement, a moderator decision, one gate, and a concrete stage output.
- The service function list contains at least 10 observable, non-duplicate functions. If the service scope justifies more, include F11 and onward rather than compressing distinct functions.
- Exactly five name candidates appear and exactly one fancy name is selected.
- Naming availability is verified or explicitly marked unverified.
- `references/kano-model.md` was read before KANO classification.
- KANO classification uses paired positive/negative responses and the A/M/O/I/R/X matrix.
- Simulated KANO results are labeled `[暫定假設]`, not customer evidence.
- Every function shows all four non-moderator role judgments before aggregation.
- Every function shows A, M, O, I, R, and X counts.
- Rigid demand equals `(M+O)/(A+M+O+I)` and ideal demand equals `(A+O)/(A+M+O+I)`, with substituted values shown.
- R and X are reported but excluded from both denominators; a zero denominator returns `N/A`.
- A real rendered SVG quadrant image exists as an audit artifact and the full SVG markup is embedded directly inside the Markdown before any optional source block. The chart uses rigid demand as x and ideal demand as y with 0.50 split lines and a point-ID legend.
- The Markdown chart is self-contained; it does not depend only on a linked local image file.
- No fenced `mermaid` block is used for the KANO chart. Optional chart source, if included, is fenced as `text`.
- Development decisions are visibly grouped by 第一象限 Q1, 第四象限 Q4, 第二象限 Q2, 第三象限 Q3, plus an exception table for dominant R or X when needed.
- Priority follows Q1 → Q4 → Q2 → Q3 and the documented within-quadrant ordering rules.
- Every function shown in summary, tables, legend, priority, grouped development decisions, and final next steps includes its service function ID.
- Dominant R routes to avoid/remove and dominant X routes to re-survey.
- Every feature appears in only one priority.
- Every priority row includes both coefficients, quadrant, importance interpretation, development decision, and acceptance criterion.
- Evidence labels match support.
- No invented quotations, verbatim simulated dialogue, or private reasoning appears.
- A non-overwriting UTF-8 `.md` report was created and re-read successfully.
- The final chat response links to the exact report file.
