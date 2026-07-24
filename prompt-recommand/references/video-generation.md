# Video generation prompt blueprint

Use this reference for every video-prompt session. Build for observable motion and timing, not a pile of cinematic adjectives.

## 1. Classify the generation mode

- **Text-to-video**: Create all visuals and motion from a written brief.
- **Image-to-video**: Animate a supplied image while preserving selected traits and composition.
- **Multi-shot video**: Create separate shots or clips, then edit them into one sequence. Prefer this for ads, narratives, dialogue, or videos longer than a single coherent action.

Name the primary format: social ad, product demo, cinematic story, explainer, UGC/talking head, music or mood clip, motion graphic, or seamless loop.

## 2. Collect the brief progressively

Ask only for missing fields, one question per turn, in this order:

1. **Purpose and platform**: attention, explanation, conversion, mood, or storytelling; Reels, TikTok, Shorts, website, presentation, or display.
2. **Duration and format**: total seconds, aspect ratio, resolution if known, and whether it must loop.
3. **Subject and action**: who or what appears, the single most important visible action, and the start/end state.
4. **Story and message**: hook, development, final beat, CTA, exact on-screen copy, dialogue, or voice-over.
5. **Shot design**: shot count, framing, camera position, lens feel, movement, transitions, and pacing.
6. **Visual language**: realism, art direction, setting, lighting, palette, weather, texture, and mood.
7. **Audio**: ambient sound, effects, music energy, dialogue, voice character, or silent delivery.
8. **Continuity and constraints**: identity, product, wardrobe, props, environment, screen direction, facts, brand rules, and unwanted artifacts.
9. **Target tool**: named generator, supported clip length, reference inputs, and whether shots must be prompted separately.

For image-to-video, ask for the source image before motion design if it is not attached. Confirm `must preserve`, `may animate`, and `must remain static`.

## 3. Choose a duration structure

Use these as starting patterns, then adapt to the story:

| Duration | Recommended structure | Typical shot count |
| --- | --- | --- |
| 3-5 sec | One subject, one action, one camera move, loop or reveal | 1 |
| 6-10 sec | Setup → action/reveal → final state | 1-3 |
| 15 sec | 0-3 hook → 3-10 proof/story → 10-13 payoff → 13-15 CTA | 3-5 |
| 30 sec | 0-3 hook → 3-10 problem → 10-22 solution/proof → 22-27 payoff → 27-30 CTA | 5-8 |

Do not force a cut every few seconds when one continuous shot communicates the idea more clearly. If the generator only supports short clips, split the timeline into independently generatable shots and include edit notes.

## 4. Write the script

Create a compact beat sheet before writing prompts:

- **Hook**: the first visible change, tension, question, or surprising image.
- **Development**: the action, demonstration, transformation, or emotional turn.
- **Payoff**: the result, proof, reveal, or memorable final image.
- **CTA/final beat**: the precise next action or a clean loop back to the opening.

For voice-over or dialogue, estimate spoken length conservatively. Use roughly 3-4 Traditional Chinese characters per second for comfortable narration, then shorten further when visuals need breathing room. Keep generated on-screen text minimal and recommend post-production for long or brand-critical typography.

## 5. Design the storyboard

Return a table with these fields:

| Time | Visual and action | Framing | Camera movement | Audio/text | Transition |
| --- | --- | --- | --- | --- | --- |
| 00:00-00:03 | State the visible action and start/end state | Shot size and angle | One motivated move | VO, SFX, music, exact copy | Cut, dissolve, match cut, whip, or continuous |

Each row must fit inside the assigned time. Make the subject action countable and observable. State who moves, where they move, and what changes by the end of the shot.

## 6. Choose camera movement deliberately

- **Locked-off/static**: clarity, tension, graphic composition, product proof.
- **Pan/tilt**: reveal adjacent or vertical information while staying in place.
- **Dolly in/push-in**: increase attention or intimacy.
- **Dolly out/pull-back**: reveal context or create emotional distance.
- **Truck/track**: follow lateral motion and maintain subject relationship.
- **Orbit/arc**: reveal form or environment around a stable subject; use sparingly.
- **Crane/jib/pedestal**: change height to reveal scale or hierarchy.
- **Handheld**: immediacy or UGC energy; specify restrained or energetic shake.
- **Rack focus**: redirect attention between two established depth planes.
- **POV/body-mounted**: subjective experience; define whose viewpoint it is.

Avoid contradictory instructions such as static tripod plus sweeping handheld, or simultaneous pan, orbit, zoom, and crane in a three-second shot. Describe the starting frame, movement path, speed, and ending frame.

## 7. Master prompt template

```text
任務：生成一支【總秒數】的【影片類型】，用於【平台／情境】。
輸出：【比例、解析度（若需要）、幀率（若工具支援）】；【是否循環】。

核心概念：
- 主角：【人物／產品／物件】
- 開始狀態：【第一幀可見內容】
- 核心動作：【單一主要動作或轉變】
- 結束狀態：【最後一幀可見內容】
- 觀眾應感受到：【情緒或訊息】

時間與鏡頭：
- 00:00-00:03：【景別與角度】；【主體動作】；攝影機【起點、移動方式、速度、終點】。
- 00:03-00:08：【下一個鏡頭或連續動作】。
- 00:08-00:15：【收尾、產品畫面或 CTA】。

視覺與聲音：
- 場景與光線：【地點、時間、光線方向與變化】
- 色彩與材質：【可觀察的視覺特徵】
- 節奏與轉場：【剪輯速度、轉場方式】
- 聲音：【環境音、音效、音樂能量、旁白／對白】
- 畫面文字：【逐字文案；繁體中文；出現時間】

一致性：
- 必須保留：【人物、產品、服裝、場景、品牌等】
- 可以變化：【表情、姿勢、光線、背景動態等】
- 必須避免：【變形、閃爍、漂移、額外肢體、錯字、不合理物理等】
```

Delete irrelevant sections. For separate generation, create one prompt per shot and repeat only the continuity locks needed to match adjacent shots.

## 8. Image-to-video template

```text
以提供的參考圖為第一幀，生成【秒數】秒影片。

必須保留：
- 【人物身分、五官、髮型、服裝、產品外型、標籤、構圖、背景結構】

允許動態：
- 主體：【微表情、手部、步伐、產品動作】
- 環境：【頭髮、衣料、蒸氣、光影、植物、粒子】
- 攝影機：【起始景別、移動路徑、速度、結束景別】

保持靜止：
- 【不得移動或變形的標誌、文字、建築線條、產品比例】

時間：
- 00:00-00:02：【起始與微動】
- 00:02-00:05：【主要動作】
- 00:05-00:06：【穩定收尾或無縫循環】

避免：身分漂移、臉部重繪、額外手指或肢體、產品標籤變字、背景融化、邊緣閃爍、瞬間速度變化、無因果的物件移動。
```

## 9. Reliability checks

- Confirm that shot durations add up to the requested total.
- Give each short shot one dominant action and one motivated camera move.
- State start and end frames so motion has a direction.
- Lock recurring traits across shots: face, hair, wardrobe, product geometry, props, palette, time of day, and environment.
- Preserve screen direction across cuts unless crossing the axis is intentional.
- Avoid relying on generated typography for long copy, small legal text, prices, or exact logos.
- Separate generation prompts from editing instructions when the tool creates clips rather than a finished timeline.
- Name physical causes for secondary motion: wind moves fabric, footsteps disturb dust, steam rises from heat.
- Avoid impossible simultaneous actions, unexplained object appearances, floating props, temporal jumps, flicker, morphing, and texture crawl.
- If the target generator's current limits matter, verify them before promising resolution, clip length, audio, reference-image, or multi-shot capabilities.

## 10. Final self-check

Before delivering, verify: What is being made? Where will it appear? How long is it? What happens in each time range? What does the camera do? What are the opening and closing frames? What is heard or read? What must stay consistent? What must not happen? Does the full timeline add up exactly?
