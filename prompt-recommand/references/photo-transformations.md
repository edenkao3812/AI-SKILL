# 照片風格轉換類

Use when an uploaded person, pet, object, or landscape is the source. Ask what must remain unchanged before choosing the transformation. Default preservation fields: face shape, facial features, hairstyle, skin tone, expression, body proportions, clothing, pose, product geometry, and original scene relationships.

| ID | Archetype | Required slots | Recipe anchor |
| --- | --- | --- | --- |
| P1 | 衝破手機螢幕 | person/reference, original account label, action, UI content, 4:5 | Person walks out of an original photo-sharing interface with foreshortened step, glass/digital fragments, cinematic depth. |
| P2 | 個人形象潑墨插圖 | portrait, preserve list, pose, palette | Japanese hand-drawn portrait combining loose ink, watercolor wash, sketch lines, simple white background and small doodles. |
| P3 | 角色設定海報 | portrait, profile fields, mini-scenes, visual tone | Semi-realistic illustrated character profile with hero portrait, daily/work variants, notes, arrows, and structured personal traits. |
| P4 | 穿搭建議分析 | full-body photo, face/skin/body traits, contexts, preferences | Personalized styling board based on the actual subject; explain top, bottom, proportion, palette, accessories, and why each suits them. |
| P5 | 復古電子寵物像素風 | photo, subject relationship, four-color palette, UI labels | Full-frame early-LCD 8-bit scene with limited pastel colors, pixels, status icons, date/time; no device casing or buttons. |
| P6 | Q版 3D 小人風 | photo, preserved pose, mini-count/actions, placement, title | Keep the main photo subject fixed; surround them with 3-7 active mini selves, natural shadows, sticker edge, small Korean-feel title and doodles. |
| P7 | 電影海報風 | photo, genre, title/tagline, emotional tone | Intensify narrative focal point, light contrast, atmosphere, and cinematic typography according to the source mood. |
| P8 | 大尺寸與迷你版人物 | portrait, mini actions, room props, emotional theme | Same person at normal and 1/6-1/8 scale interacting in a warm miniature dream scene; identity and wardrobe remain consistent. |
| P9 | 日本極道千金／少爺風 | portrait, gender presentation, wardrobe, city/rain setting | Preserve identity in a moody crime-film scene with luxury car, bodyguard, wet neon street, black/gold low-saturation lighting. |
| P10 | Y2K 四格大頭貼 | portrait, four expressions, accessories, tiny copy | 2x2 fisheye elevator selfies with distinct expressions, CCD softness, stickers, flash artifacts, and consistent identity. |
| P11 | 蠟筆手繪風 | photo, essential objects, new palette, doodles | Simplify into a childlike drawing on white paper with irregular crayon strokes, bright pastel palette, innocent decorative motifs. |
| P12 | 小畫家隨興畫風 | photo, preserve palette, absurdity level | Intentionally clumsy mouse-drawn remake with crooked lines, broken proportions, low-resolution pixels, yet recognizable subject. |
| P13 | 大頭照手機桌布 | portrait, four expressions, phone model, 9:16 | Korean cream minimal wallpaper: 65-70% top whitespace, low Dock-like rounded panel, four evenly spaced floating heads above it. |
| P14 | 風景浮雕徽章 | landscape, landmark label, simplification, background | Convert the main scenery into a centered enamel travel magnet with pastel fills, polished gold border, shallow relief and collectible finish. |
| P15 | 手作紙雕風 | photo, subject simplification, layer count, palette | Layered laser-cut paper diorama with rounded shapes, clean cut edges, gentle shadows, handmade depth and warm Japanese craft feel. |
| P16 | 地球小行星風 | photo, location, travel notes, doodles | Place the subject at the center of a Tiny Planet 360-degree fisheye world with bright natural light, postcard labels and travel energy. |
| P17 | 電玩遊戲像素風 | full-body photo, outfit details, background rule | Soft small-pixel dress-up avatar, faithful face/hair/outfit cues, slightly blurred low-resolution edge, usually plain white background. |
| P18 | 塔羅牌風 | photo, card name/number, symbols, palette | Vintage European tarot layout with gold border, celestial/floral symbols, paper texture, mystical hand-drawn fantasy atmosphere. |
| P19 | F1 賽車現場照 | portrait, team, name/title, scene, 16:9 | Realistic paddock/strategy-console documentary moment, team-color headset/jacket, telemetry background, original ranking HUD and lower third. |
| P20 | NBA 球賽現場照 | portrait, supported team, opponent, score context, 16:9 | Natural courtside spectator broadcast capture with arena compression, long-lens depth and an original professional scoreboard UI. |
| P21 | 職棒現場照 | portrait, CPBL team, opponent, score/inning, 16:9 | Night-game spectator shot with cheering props, Taiwanese stadium light, verified Traditional-Chinese broadcast information and original UI. |
| P22 | 偶像打歌現場照 | portrait, stage name, K-pop/J-pop direction, song/comeback, 16:9 | Official-fancam feel with stage outfit, headset mic, LED/laser lighting, audience lights and original clean program graphics. |
| P23 | 手繪塗鴉分身 | portrait, poses, expressions, outfits | Unruled white sketchbook page packed with overlapping full-body studies, Q versions, face/hand details, arrows and notes, all the same person. |
| P24 | 優雅老年風 | portrait, years aged, mature wardrobe, setting | Natural believable aging while preserving identity; stylish mature clothing, period street/cafe, dusk film light and experienced confidence. |
| P25 | 人物臉貼玻璃 | portrait, expressions, edge positions, 9:16 | Playful wallpaper where face and palms press against the screen glass from different edges, with believable soft compression and small doodles. |
| P26 | 復古膠片朦朧風 | portrait, location, flowers/props, motion direction | Low-saturation film grain, backlight, defocus, motion smear and double exposure creating a sweet, distant, story-rich cinematic still. |
| P27 | Q版人物躍出手機 | portrait, outfit, jump pose, setting | Detailed chibi character leaps over a fully visible giant phone whose screen captures the same airborne moment; strong scale and social-share impact. |
| P28 | 精緻生日海報 | portrait, age, exact wording, wardrobe, 3:4 | Premium cream paper wall with a large carved age number, balloons/flowers inside, subject emerging through the number, warm studio light and minimal cover typography. |

## Transformation guardrails

- State identity continuity separately from style. `保留辨識度` is not enough; list the features.
- If a new pose is required, do not also demand the original pose remain unchanged.
- For P3 and P4, distinguish visual transformation from inferred personality or styling analysis; frame uncertain interpretations as suggestions.
- For P19-P22, use verified names, teams, scores, dates, and event context. Ask whether the UI should be fictionalized when current data is unavailable.
- For P1, P9, P19-P22, and P27, use original interface/brand treatments unless authorized assets are supplied.
- For P10 and other panel layouts, define each panel and keep one subject identity across all panels.
- For P13, P25, and P28, reserve exact safe areas for the phone clock, app icons, or headline copy.
- Do not use living-artist or studio names as a shortcut. Translate references into observable visual traits.
