---
name: malaysia-tiktok-shop-storyboard
description: Create Malaysian TikTok Shop, Reels, or Shorts product-selling video packages from a product title, 1–3 product images, and an optional reference video. Use for Seedance prompts; three distinct 15-second concepts; six-frame storyboards; reference-video adaptation; strict shot replication or replacement; and generated-video audits. Trigger on requests mentioning 商品图、产品标题、参考视频、TikTok Shop、TikTok 带货、马来西亚、三套不同场景/剧情、15秒动态演化提示词、分镜图、storyboard、首帧图、逐镜复刻、严格替换或成片审计.
---

# Malaysia TikTok Shop Storyboard

Turn product evidence into executable 9:16 video prompts and visual storyboards without inventing product facts.

## Route the request

Choose exactly one route from the user's explicit wording:

1. `CREATIVE_15S_EVOLUTION` — use when the user asks for “三套”, “不同场景”, “演化口播”, “TikTok带货”, “再来一个”, or “换场景”. This is the default route.
2. `STRICT_REFERENCE_ADAPTATION` — use only when the user explicitly asks for “1:1”, “逐镜复刻”, “完全反推”, or “严格替换”. Read [references/strict-reference.md](references/strict-reference.md) only on this route.
3. `GENERATED_VIDEO_AUDIT` — use when the user uploads a generated/final video and asks to identify problems, repair the prompt, or compare it with a reference. Audit observed evidence; do not silently regenerate.

Do not load `references/strict-reference.md` for ordinary creative work or a non-strict audit. If an audit explicitly requests strict 1:1 comparison, route it to `STRICT_REFERENCE_ADAPTATION`.

## Resolve inputs before generation

- Identify the product title, 1–3 product images, reference video, target platform, target duration, and face constraints.
- If one turn contains multiple products, images, or videos, list the exact product → image(s) → video mapping and resolve ambiguity before generation. Never mix assets between products.
- Treat product images as appearance evidence, not automatically as the frame at 0 seconds.
- Treat non-product reference images and reference-video frames as evidence for specific scenes, actions, camera behavior, and plot only. Do not copy or infer a person's face, identity, facial features, skin details, or other personal appearance from them.
- For each supplied video, run `python scripts/inspect_media.py <video-path>`. Use its JSON duration, dimensions, fps, and contact sheet as evidence. Skip this step cleanly when there is no video.
- Read [references/product-dna.md](references/product-dna.md), then record category, silhouette, proportions, colors, materials, lid/handle/port/liner and other key parts, executable actions, and prohibited errors.
- Read [references/banned-claims-and-no-subtitles.md](references/banned-claims-and-no-subtitles.md) for every route.

Use FFmpeg/FFprobe first for video scanning and contact sheets. Use ImageGen for storyboard sheets. Use Pillow only when deterministic shot labels or image compositing are required. PySceneDetect, faster-whisper, and OpenCV are optional enhancements for strict replication or audits; ordinary three-concept work must not depend on them.

## Creative route

Read [references/creative-15s.md](references/creative-15s.md), [references/storyboard-spec.md](references/storyboard-spec.md), and [references/malaysia-malay.md](references/malaysia-malay.md).

1. Design three concepts grounded in the real product structure. Between any two concepts, change at least three of: hook, person, scene, use context, primary proof action, camera path, result, or ending.
2. Default to 15 seconds, 9:16, realistic handheld-phone TikTok style, and Malaysia as the market.
3. Use the complete timeline `0s–2s`, `2s–5s`, `5s–8s`, `8s–11s`, `11s–13s`, `13s–15s`. In every segment specify visible frame, person action, product contact, camera/shot movement, environment/SFX, and the exact spoken line at that moment.
4. Embed spoken lines inside their matching time segments. Never add a separate voiceover-reference block. The spoken line must not announce an effect before it becomes visible.
5. Use natural, informal Malaysian Malay TikTok speech unless the user requests another language.
6. Enforce a three-layer firewall. Layer A is the user-facing video-evolution prompt and contains only the intended finished video: format, verified product state, six timed segments, actions, camera, sound, spoken lines, and continuity. Layer B is the internal storyboard-generation prompt and contains layout, panel labels, framing, identity/privacy, and image-reference rules. Layer C is the internal validation checklist and contains claims, artifact, continuity, and delivery checks. Never copy, paraphrase, summarize, or convert Layer B or Layer C into a negative-prompt paragraph inside Layer A.
7. Use the separate internal storyboard prompt with ImageGen to create one complete six-frame storyboard sheet per concept. Each sheet is a 3-column × 2-row grid whose panels are the first frames of the six timeline shots. Keep shot labels on the sheet border or gutters, outside the depicted video frames. Protect identity through composition—hands-only, below-shoulder framing, back views, or natural occlusion—not by drawing over faces. Never add mosaics, blur, pixelation, solid-color blocks, stickers, or artificial face masks to a storyboard that may be used as a video reference.
8. Deliver each concept directly in chat with the exact label `方案N｜可复制视频提示词`, followed by exactly one copyable `text` code block containing the complete video-evolution prompt, immediately followed by its generated storyboard reference image. Repeat this prompt block → image pair for Concepts 1–3. Do not create or attach a `.md` file. Do not output workflow notes, product-DNA analysis, validation records, internal constraints, the internal storyboard prompt, download sections, file inventories, or duplicate prompt text unless requested.
9. Express required states positively wherever possible: describe what the product, filling, part, hand, or result visibly remains. Mention a negative constraint only when a concrete risk belongs to that exact shot, would materially break the concept, and cannot be controlled clearly with positive state language. Normally use none; never use more than two narrow risk constraints per concept. Keep each one next to the affected segment. Never emit a reusable list of unrelated defects merely because they appear in an internal checklist.
10. Validate the assembled user-facing prompt text through stdin or a temporary internal file with `scripts/validate_delivery.py`; resolve supported warnings, but never deliver the validation file.

Do not output lock cards, line-by-line source-film mappings, internal audit logs, or other strict-mode artifacts in ordinary creative mode. Output only the requested three evolving prompts and three storyboard sheets.

## Strict route

Follow [references/strict-reference.md](references/strict-reference.md) in addition to the shared product-DNA and claims rules. Apply duration and person gates before analyzing shots. Build an evidence library and atomic timeline before producing replacement mappings, first frames, evolving prompts, or an audit. Do not claim 1:1 fidelity where source evidence is missing.

## Generated-video audit route

Inspect both the generated video and reference video with `scripts/inspect_media.py` when present. Compare only observable timing, framing, action order, product geometry, contact, continuity, speech timing, and forbidden overlays/claims. Return: timestamped finding → evidence → likely prompt cause → minimal corrected prompt language. Keep unverified causes labeled as hypotheses.

## Global hard constraints

- Never add in-video subtitles, auto-captions, narration text, titles, prices, discounts, sales claims, promotional stickers, QR codes, floating text, lower thirds, UI, or watermarks.
- Existing text physically printed on the provided product packaging may remain visible; do not add, rewrite, correct, or animate it.
- Never invent price, discount, sales volume, certification, brand relationship, medical or safety effect, heat-retention, leak-proofing, waterproofing, performance specifications, or any unprovided selling point.
- Preserve contact, gravity, occlusion, and action order for liquid, food, tools, lids, buttons, liners, handles, and other parts.
- Inspect product appearance, parts, contact physics, hands, logos, packaging, and scene continuity internally. Convert any relevant finding into a positive visible state in the affected shot. Do not expose the inspection categories as a generic negative list in the delivered video prompt.
- Keep generated storyboard imagery faceless by default through camera composition: use hands, arms, below-shoulder framing, back views, or natural occlusion with the face outside the frame. Never create a censor bar, mosaic, pixelation, blur, solid-color face block, sticker, or artificial mask in a storyboard image or instruct a video model to create one. Do not print face policy, text policy, anti-masking language, or other production-rule checklists inside the delivered video prompt. If the user explicitly permits visible faces, use a newly generated anonymous performer with a natural, unobscured face and do not copy the reference person's identity or appearance.
- Reference imagery/video may supply only concrete setting, action, camera, framing, and plot evidence. Preserve the supplied product's DNA, but do not reproduce any reference person's face, identity, or unneeded personal details.
