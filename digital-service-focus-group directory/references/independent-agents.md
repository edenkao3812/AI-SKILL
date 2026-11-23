# 獨立 AI 角色任務契約

這份契約只用於 `digital-service-focus-group` 的四個非主持角色。`主持人` 是協調與裁決者，不是第五份受訪者資料。四份輸出都是 AI 假設，不能稱為真實焦點小組或顧客證據。

## 隔離與兩輪流程

1. 主持人準備一份相同的服務簡介：使用者原文、已知條件、暫定假設、地域與目標客群假設、限制與待驗證事項。不要加入預設 KANO 結論或候選名稱勝出者。
2. 為 `直覺型潛在用戶`、`品牌行銷總監`、`毒舌鄉民／風險控管`、`商業定位分析師` 各開一個**獨立 agent 任務**。若工具支援，使用空白／不繼承對話的上下文（例如 `fork_turns="none"`）。各任務只收到相同簡介及自己的角色描述。不同時間執行也可以，但不能把先完成的角色答案送給後一個角色。
3. **Round A：** 每位 agent 獨立提交服務焦點、主要 TA、風險、可觀察功能提案及命名方向。主持人等四份都完成，才綜合定出固定的服務定位、至少 10 個功能（含穩定 `F` 編號）和五個待評名稱。主持人可判斷取捨，但不可把自己的意見偽裝為某角色提案。
4. **Round B：** 同四個 agent 各自收到完全相同的固定定位、功能清單、五個候選名稱、[KANO 參考矩陣](kano-model.md)和輸出格式，以及自己的原角色任務。可以讓 agent 看自己的 Round A 回答；不得讓它看其他 agent 的任何提交。每位 agent 分別判定所有功能並評五個名稱。
5. 主持人收到四份 Round B 後才交叉比較、驗證、計算、畫圖與裁決。若某份格式或矩陣對不上，請**原 agent**只修正該份，保留原件與修正版，且不得附上其他角色答案。

對話中若有討論、修改功能或名稱，Round B 的共同清單必須版本化。只要共同清單改變，就重新發給**全部四個 agent**，不能只更新部分角色。

## 相同資訊與不同資訊

相同資訊：服務簡介、功能 ID／定義、五個候選名稱、KANO 五個回答選項與 5×5 矩陣、六類 1–10 評分定義、輸出欄位。

不同資訊：僅各自的角色觀察角度。每個 agent 必須能提出與其他角色不同甚至相反的看法；不要要求一致意見。

不得提供：另一角色的回答、主持人的偏好、預期象限、預算或配額式分數、已寫好的報告段落。不要使用固定分數模板代替 agent 的獨立判斷。

## Round A JSON

每個 agent 回傳一個 JSON 物件。`task_id` 由主持人根據實際執行環境補入或核對，不得虛構。

```json
{
  "schema_version": "1.0",
  "round": "A",
  "role": "直覺型潛在用戶",
  "task_id": "actual-agent-task-id",
  "stage1_view": {"position": "完整句子", "basis": "依據或假設", "risk": "風險", "recommendation": "具體建議"},
  "stage2_view": {"position": "完整句子", "basis": "依據或假設", "risk": "風險", "recommendation": "具體建議"},
  "feature_proposals": [
    {"name": "可觀察的服務功能", "journey": "服務旅程階段", "reason": "為何需要", "risk": "主要代價或風險"}
  ],
  "naming_directions": ["命名方向及理由"]
}
```

`feature_proposals` 不需剛好 10 項；主持人要把四份提案整合成至少 10 項有意義且不重複的功能。每個欄位應是可供報告摘要的最終判斷，不要回傳隱藏推理或逐字角色扮演。

## Round B JSON

同一 agent 在後續任務中回傳第二個 JSON 物件，`role` 與 `task_id` 應與 Round A 相同。`functions` 必須覆蓋固定清單中所有功能且恰好各一次；`names` 必須覆蓋五個固定候選名稱且恰好各一次。

```json
{
  "schema_version": "1.0",
  "round": "B",
  "role": "直覺型潛在用戶",
  "task_id": "actual-agent-task-id",
  "stage3_view": {"position": "完整句子", "basis": "依據或假設", "risk": "爭議", "recommendation": "建議驗證"},
  "stage4_view": {"position": "對優先順序的預判", "basis": "重要功能及理由", "risk": "異議", "recommendation": "建議決策"},
  "stage5_view": {"position": "名稱判斷", "basis": "語意或傳播依據", "risk": "命名風險", "recommendation": "推薦方向"},
  "functions": [
    {
      "id": "F1",
      "positive": "很愉悅",
      "negative": "無法接受",
      "primary": "O",
      "scores": {"A": 3, "M": 4, "O": 9, "I": 2, "R": 1, "X": 1},
      "rationale": "此角色對功能和缺席的判斷及六類分數理由",
      "overturn": "什麼真實資料會推翻判斷"
    }
  ],
  "names": [
    {
      "name": "候選名稱",
      "scores": {"fit": 8, "memory": 7, "oral": 8, "visual": 7, "search_risk": 5},
      "rationale": "名稱與服務承諾的契合理由",
      "risk": "未查證的風險"
    }
  ]
}
```

回答選項固定為 `很愉悅／理所當然／沒感覺／可以忍受／無法接受`。`primary` 只能依正向與反向回答在矩陣的交點產生，不得由六類分數倒推。六類分數均為 1–10 整數；主碼和分數可以呈現混合效果，並須給出可理解的理由。名稱各面向分數也是 1–10 整數。

Round B 不應看全體計算結果後才寫 `stage4_view`；該欄是角色對重要性的**預判**，實際係數由主持人在四份提交後計算。搜尋、競品、商標、網域或社群帳號的現況須另行查證並註明來源；agent 的名稱風險分數不證明可用性。

主持人另存一份固定清單 `manifest.json`，作為四份 Round B 的共同核對基準：

```json
{
  "version": "1",
  "functions": [{"id": "F1", "name": "可觀察功能名稱"}],
  "names": ["候選名稱一", "候選名稱二", "候選名稱三", "候選名稱四", "候選名稱五"]
}
```

範例只顯示一項功能；正式 `manifest.json` 至少含 10 個依序編號的功能。更動清單時建立新版本，將新版本完整送給四個 agent，保留舊版本供稽核。

## 驗證與來源記錄

將八份原始 JSON 以不覆寫的檔名保存，並記下共同簡介與固定清單版本。使用：

```text
python scripts/aggregate_kano_agents.py --manifest manifest.json --round-a a1.json a2.json a3.json a4.json --round-b b1.json b2.json b3.json b4.json --out WORK_DIR
```

腳本會檢查角色、任務識別碼、Round A/B 對應、固定功能與候選名稱覆蓋、KANO 矩陣、分數範圍，輸出 `kano-agent-summary.json` 與 `kano-chart-input.csv`。若 R 或 X 分數達最高類別分數的 90%，會標記為待人工審查；這是提醒門檻，不會替主持人作決策。主持人須依理由決定是否移除或重測，並在最後繪圖前調整 CSV。成本依賴與商業裁決也由主持人負責。

報告需列出四個角色各自的任務識別碼、Round A/B 提交檔、資料性質與分析界線。角色表只能摘要其提交內容；不可憑空補出角色意見。個別 agent 的獨立執行降低共同上下文污染，但同源模型仍可能有共同偏差；不能代替真實用戶訪談與問卷。
