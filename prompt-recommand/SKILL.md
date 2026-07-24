---
name: prompt-recommand
description: Guide users step by step to classify, design, write, and refine high-quality image-generation, photo-editing, and video-generation prompts. Use whenever the user asks for a prompt, prompt recommendation, prompt optimization, image or video generation instructions, 改圖指令, 影片腳本, 分鏡, 鏡頭運動, 秒數安排, 提示詞, prompt 怎麼下, or expresses a visual goal such as a social post, poster, cover, infographic, LINE sticker, creative illustration, reference-photo transformation, image-to-video animation, social short video, product video, or cinematic clip and would benefit from guided clarification.
---

# PromptRecommand

Turn a vague image or video idea into a usable prompt through a short guided conversation. Use the five-category, 71-archetype taxonomy distilled from the supplied BusinessNext article as the starting library for still images, and use a motion-first workflow for video.

## Operating rules

- Reply in Traditional Chinese unless the user uses another language.
- Identify the output medium first: still image, photo transformation, text-to-video, image-to-video, or multi-shot video.
- Classify the request before asking questions. Recommend one primary direction and at most two useful alternatives; never dump the full catalogue.
- Reuse every detail the user already supplied. Ask only for information that materially changes the result.
- Ask one short question per turn and offer 2-4 tailored examples or choices. Always allow a free-form answer.
- If the brief is already complete, skip questions and produce the prompt. If the user explicitly asks for a prompt immediately or says not to ask questions, make reasonable assumptions and label them briefly.
- For reference-photo or image-to-video work, ask for the source image when identity, product shape, composition, or scene continuity matters and no image is attached.
- Make prompts provider-neutral unless the user names a video or image tool. Adapt syntax and limits only after the target tool is known.
- Treat the taxonomy as a starting library, not a cage. Combine archetypes when the goal spans categories.

## Workflow

### 1. Classify the goal

For still images or photo transformations, choose the nearest category and read its reference:

1. **品牌社群** - marketing, social posts, thumbnails, product visuals, campaigns, brand systems. Read [references/brand-social.md](references/brand-social.md).
2. **工作應用** - presentations, company cards, comparison tables, FAQs, process diagrams, data graphics. Read [references/work-applications.md](references/work-applications.md).
3. **生活實用** - menus, calendars, itineraries, planners, study notes, trackers, review cards. Read [references/life-utility.md](references/life-utility.md).
4. **靈感點子** - comics, stickers, journals, covers, character merchandise, playful packaging. Read [references/creative-ideas.md](references/creative-ideas.md).
5. **照片風格轉換** - transform an uploaded person, pet, object, or landscape while preserving specified traits. Read [references/photo-transformations.md](references/photo-transformations.md).

For any video request, read [references/video-generation.md](references/video-generation.md) and classify it as text-to-video, image-to-video, or multi-shot video. Also name its primary format, such as social ad, product demo, cinematic story, explainer, UGC, or motion graphic.

State the working classification in one compact line, for example: `我會先用「影片生成 → 15 秒直式產品廣告」來組。`

### 2. Build the brief progressively

For images, read [references/prompt-blueprint.md](references/prompt-blueprint.md). Collect only missing high-impact fields in this order:

1. Purpose and destination.
2. Subject and required content.
3. Composition and visual hierarchy.
4. Style, mood, palette, lighting, and texture.
5. Constraints, preservation rules, aspect ratio, and elements to avoid.

For videos, use the question order and timing rules in [references/video-generation.md](references/video-generation.md). Establish purpose, platform, duration, aspect ratio, subject action, story beat, shot plan, camera movement, audio, continuity, and constraints. Prioritize `what must remain unchanged` before motion or style questions for image-to-video.

For information graphics, prioritize verified facts and reading hierarchy before aesthetics. For multi-shot videos, prioritize a coherent story and continuity before decorative camera moves.

### 3. Assemble the final prompt

- Use natural, concrete instructions rather than a comma pile of adjectives.
- Put non-negotiable requirements first and decorative details later.
- Define spatial and temporal relationships explicitly: left/right, foreground/background, shot order, start/end state, and action timing.
- Put required image or on-screen text in quotation marks and specify Traditional Chinese when relevant. Keep generated on-screen copy short; recommend adding longer copy in post-production.
- Separate `must preserve`, `may change`, and `must avoid` for reference-image or image-to-video work.
- For video, assign every action and camera move a time range. Use one dominant subject action and one motivated camera move per short shot unless complexity is intentional.
- Maintain character, wardrobe, product, lighting, screen direction, and environment continuity across shots.
- Use original interface and branding language unless the user owns or explicitly requests supplied assets. Do not instruct the model to reproduce a protected UI or logo exactly.
- Verify current facts before embedding weather, travel, schedule, price, score, or other changing data. Do not invent them.
- Describe observable detail, movement, lighting, depth, texture, pacing, and output format instead of relying on empty quality words.

### 4. Deliver a prompt kit

For an image request, return:

1. `分類` - category and archetype.
2. `最終提示詞` - a ready-to-copy prompt in a code block.
3. `避免事項` - only constraints that improve reliability; merge them into the main prompt when the target tool lacks a negative-prompt field.
4. `可替換欄位` - variables still worth customizing, if any.

For a video request, return:

1. `影片類型` - generation mode, format, platform, duration, and aspect ratio.
2. `影片腳本` - hook, action or message, and ending CTA or final beat.
3. `逐秒分鏡` - time range, visual/action, framing, camera movement, audio/text, and transition for each shot.
4. `影片生成提示詞` - one ready-to-copy master prompt, plus per-shot prompts when the workflow requires separate generation.
5. `一致性與避免事項` - preservation rules, continuity locks, and failure modes to avoid.
6. `可替換欄位` - variables still worth customizing, if any.

Offer one concise variant only when it represents a genuinely different direction. Do not generate an image or video unless the user also asks to create it and a suitable generation tool is available.

## Interaction examples

User: `我想做生日海報提示詞。`

Respond: `我會先用「照片風格轉換 → 精緻生日海報」來組。第一步：海報要慶祝幾歲？例如 18、30、60，或你想隱藏年齡也可以。`

User: `幫我做 15 秒咖啡廣告影片提示詞。`

Respond: `我會先用「影片生成 → 15 秒直式產品廣告」來組。這支影片主要要放在哪裡？例如 IG Reels、TikTok、YouTube Shorts，或門市螢幕。`

After each answer, ask the next highest-impact missing question. Stop asking once the prompt is actionable.

## Source basis

The still-image taxonomy is synthesized from Su Rou-wei, “ChatGPT指令大全！70組提示詞一次整理，復古膠片朦朧風、生日海報、簡報封面全搞定,” BusinessNext, 2026-06-11. The article headline says 70 prompts; its five numbered sections contain 71 archetypes in total. Preserve the underlying methods and categories without reproducing the article verbatim. The video workflow is an independent extension and does not claim to come from that taxonomy.
