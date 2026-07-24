# Prompt blueprint

Use this reference for every guided prompt session.

## Core slots

| Slot | Capture | Useful question |
| --- | --- | --- |
| Goal | Intended outcome and platform | 這張圖最重要是吸睛、說明資訊、促成行動，還是紀念收藏？ |
| Subject | People, products, objects, setting | 主角是誰／什麼？有哪些一定要出現的元素？ |
| Content | Facts, labels, exact copy | 圖上必須放哪些文字或數字？請給我正確原文。 |
| Composition | Ratio, framing, hierarchy, placement | 要直式、橫式還是方形？主視覺與留白怎麼分配？ |
| Style | Medium, era, visual references, realism | 想走寫實攝影、編輯設計、手繪、3D 公仔，還是其他方向？ |
| Mood | Emotional tone and story | 希望觀眾第一眼感到療癒、專業、熱血、神秘，還是幽默？ |
| Palette/light | Colors, contrast, lighting | 有品牌色或指定光線嗎？ |
| Preserve | Identity, pose, product shape, scene | 參考圖中哪些細節絕對不能改？ |
| Avoid | Clutter, illegible text, artifacts, unwanted styles | 有哪些元素、色彩或效果一定不要？ |
| Output | Dimensions, format, variant count | 使用哪個生成工具與尺寸？需不需要多版？ |

## Question order by task

### New image

Ask: goal/platform → subject/content → composition/text → style/mood → technical constraints.

### Reference-photo transformation

Ask: confirm image → preserve list → transformation concept → new scene/composition → ratio/text → exclusions.

### Information graphic

Ask: verified source facts → audience and takeaway → hierarchy/sections → brand system → ratio and delivery surface.

### Series or template

Ask: system-wide constants → item list → variable fields → layout rules → output count and naming.

## Assembly template

```text
任務：建立一張【用途／成品類型】，用於【平台／情境】。

主體與內容：
- 主角：【人物／產品／物件】
- 必須出現：【必要元素】
- 圖中文字：【逐字文案；指定繁體中文】

構圖：
- 比例與尺寸：【比例／像素】
- 主視覺：【位置、景別、姿勢、焦點】
- 前景／中景／背景：【空間關係】
- 資訊層級與留白：【閱讀順序】

視覺語言：
- 風格：【媒材／年代／設計語彙】
- 色彩：【主色、輔色、對比】
- 光線與材質：【可觀察的效果】
- 氛圍：【情緒與故事感】

參考圖規則：
- 必須保留：【五官、髮型、產品外型等】
- 可以改變：【服裝、場景、姿勢等】

避免：
- 【不需要的元素、錯字、裁切、變形、雜亂等】
```

Delete irrelevant sections. Put the highest-priority constraints near the top and repeat only when failure would ruin the output.

## Reliability checks

- Make every required entity countable: number of panels, expressions, cards, products, or people.
- For multi-panel images, define each panel separately and lock character continuity.
- For image text, keep copy short, quote it exactly, and request clean editable-looking text zones when later editing is likely.
- For faces, state identity preservation explicitly; avoid contradictory requests to both preserve pose and create a different action.
- For products, preserve silhouette, label geometry, logo placement, material, and color before changing the environment.
- For social platforms, choose ratio intentionally: 1:1 square, 4:5 feed portrait, 9:16 story/wallpaper, 16:9 thumbnail/video.
- For brand series, define constants (grid, type hierarchy, palette, icon family) separately from variables (title, date, offer, image).
- For current data, verify first and cite or record the timestamp in the working brief.

## Final self-check

Before delivering, ensure the prompt answers: What is being made? For whom and where? What must appear? What is the focal point? What should it look and feel like? What must remain unchanged? What must not happen? What exact output is required?
