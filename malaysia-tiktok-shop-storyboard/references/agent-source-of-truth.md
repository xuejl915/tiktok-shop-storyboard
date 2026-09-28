# Agent Source of Truth

This file is the compact execution contract for any primary agent, sub-agent, or handoff agent working on the ordinary creative route. Read it before writing prompts or storyboards. If another instruction packet conflicts with this contract, stop and reconcile the conflict instead of blending both rule sets.

## Scope and evidence

- Default output: three genuinely different Malaysian TikTok Shop concepts, each 15 seconds and 9:16, unless the user explicitly requests another count, duration, market, or language.
- Use supplied product images and user-provided facts as the product evidence boundary. Do not invent price, discount, certification, performance, medical/safety effect, popularity, specifications, or invisible functionality.
- A reference video supplies observable scene, action, camera, pacing, sound, and plot evidence only. Product images are appearance evidence and are not automatically the frame at second 0.
- Strict shot replication applies only when the user explicitly requests 1:1, shot-by-shot recreation, complete reverse engineering, or strict replacement.

## Three-layer firewall

Keep these layers separate throughout planning, generation, handoff, and delivery:

### Layer A — Copyable video prompt

This is the only text delivered inside the user's copy block. It contains only:

- `15秒，9:16` and the intended realistic video style;
- verified product appearance/state needed for continuity;
- the six intervals `0s–2s`, `2s–5s`, `5s–8s`, `8s–11s`, `11s–13s`, and `13s–15s`;
- visible scene and action, product contact/operation, camera movement, scene sound, and the exact matching spoken line in every interval;
- concrete physical continuity between shots.

Layer A must not contain storyboard layout, panel labels, ImageGen directions, face/privacy policy, masking vocabulary, packaging-text policy, validation notes, workflow explanations, internal checklists, or file instructions.

### Layer B — Internal storyboard prompt

This layer exists only to generate the corresponding six-frame reference image. It may contain the 3×2 layout, Shot 1–6 gutter labels, first-frame mapping, product-first composition, identity-safe framing, and image/reference rules from `storyboard-spec.md`.

Never paste or paraphrase Layer B into Layer A. Terms such as `3×2`, `六格分镜`, `Shot 1–6`, `ImageGen`, face avoidance, reflected/background faces, mosaics, blur, solid-color blocks, stickers, or masks must not appear in the copyable video prompt.

### Layer C — Internal validation

This layer checks evidence, claims, overlays, product continuity, contact physics, timeline coverage, and final delivery structure. It is never user-facing prompt material.

Do not turn Layer C into a generic negative prompt. Prices, discounts, QR codes, UI, missing parts, reverse motion, floating objects, cream, cheese, censor artifacts, and other hypothetical failures must not be listed merely because an internal check knows about them.

## Prompt-writing rule

- Describe the intended visible state positively. Example: `掰开后馅料始终保持参考图中统一的开心果绿色、稠密顺滑形态。`
- Do not seed unwanted alternatives with lists such as `不要白丝、不要芝士丝、不要奶油`.
- Keep continuity positive when possible: `前后镜头保持同一颗曲奇。`
- Use a negative constraint only when the risk is concrete to the exact shot, would break the concept, and positive wording is insufficient. Example: `0s–5s 曲奇保持完整，掰开前不得提前露馅。`
- Default to zero negative constraints and allow at most two narrow, shot-local constraints per concept. Never append a global negative-prompt paragraph.

## Storyboard rule

- Generate one complete six-frame sheet per concept, corresponding to the first frames at 0s, 2s, 5s, 8s, 11s, and 13s.
- Prioritize the product, setup/operation, and result. Include a person only when needed to explain the action.
- Protect identity through composition such as hands-only, below-shoulder, back view, or natural occlusion. Never draw censor artifacts over a face; reframe or regenerate instead.
- Keep Shot labels in gutters or borders, outside the depicted video frames.
- Keep product silhouette, proportions, colors, parts, scale, environment geography, and adjacent-shot state consistent.

## Final delivery contract

For each concept, deliver exactly this pair in chat:

```text
方案N｜可复制视频提示词
[one copyable plain-text video prompt]
```

Immediately follow it with that concept's generated six-frame storyboard image, then continue to the next concept.

Do not deliver a `.md` summary, workflow explanation, product-DNA analysis, validation record, internal constraint list, internal storyboard prompt, download section, or redundant file inventory unless the user explicitly requests it.

Before delivery, run `scripts/validate_delivery.py` against Layer A only. A valid result must have six continuous intervals and no storyboard leakage, production/policy meta-instructions, face-censor instructions, generic negative list, or unsupported promotional terms.

## Handoff requirement

When work is delegated, every downstream packet must include or directly point to this file and must identify which layer the agent is producing. An agent assigned Layer B or Layer C must never author or rewrite Layer A. The integrating agent owns the final separation check and rejects any response that mixes layers.
