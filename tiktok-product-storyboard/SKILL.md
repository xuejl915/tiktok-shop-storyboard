---
name: tiktok-product-storyboard
description: Create Malaysian TikTok, Reels, or Shorts product-selling video packages from a product title, 1–3 product images, and an optional reference video. Use for Seedance prompts; three 15-second evolving concepts with different scenes, plots, and people; six-frame storyboards or first-frame sheets; reference-video reverse engineering; strict 1:1 shot replication or replacement; and generated-video audits. Trigger on requests mentioning 商品图、产品标题、参考视频、TikTok 带货、三套不同场景/剧情/人物、15秒动态演化提示词、分镜图、Storyboards、首帧图、严格1:1、逐镜复刻、完全反推、严格替换或成片审计.
---

# TikTok Product Storyboard

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
6. Use ImageGen to create one complete six-frame storyboard sheet per concept. Each sheet is a 3-column × 2-row grid whose panels are the first frames of the six timeline shots. Keep shot labels on the sheet border or gutters, outside the depicted video frames.
7. Deliver in this exact order: Concept 1 prompt → Concept 1 storyboard → Concept 2 prompt → Concept 2 storyboard → Concept 3 prompt → Concept 3 storyboard.
8. Run `python scripts/validate_delivery.py <delivery-file>` before final delivery and resolve warnings supported by evidence.

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
- Prevent recoloring, rescaling, melting, floating, disappearing parts, extra handles, reversed orientation, fused fingers, intersections, jumping logos, garbled packaging text, and scene drift.
- If the user says “无脸”, “不要人脸”, or “无参考人物”, show no full face, partial face, reflected face, or background face. Use only hands, arms, below-shoulder framing, or a back view.

