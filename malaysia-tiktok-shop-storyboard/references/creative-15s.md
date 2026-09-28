# Creative 15-Second Evolution

Use this reference only for `CREATIVE_15S_EVOLUTION`.

## Timeline template

Every concept is a single continuously evolving 15-second video, not six unrelated stills. Use all six segments:

| Time | Narrative job | Required content |
|---|---|---|
| 0s–2s | Visual hook | Visible frame; immediate human action; first product contact if present; framing/movement; environment/SFX; exact spoken line |
| 2s–5s | Problem or context | Same six fields; preserve location and hand/object continuity |
| 5s–8s | Product introduction | Same six fields; expose only real, visible product structure |
| 8s–11s | Primary proof action | Same six fields; show the action and its result in physical order |
| 11s–13s | Result/reaction | Same six fields; speech may describe only what is already visible |
| 13s–15s | Natural close | Same six fields; end with a physical product/result shot, not text or UI |

Write the accurate spoken line inside its segment. Do not add a detached voiceover section.

## Three-concept differentiation

Create three genuinely different executions. Between every pair, change at least three dimensions:

- hook mechanism;
- anonymous performer body framing;
- location and production texture;
- use context/problem;
- primary proof action;
- camera route or shot grammar;
- visible result;
- ending beat.

Changing only props, wardrobe color, or a synonym in the dialogue does not count. Do not repeat the same Malay opening or CTA across all three.

## Physical continuity

- Establish the product's position before hands interact with it.
- Show grasp → lift/turn/open/press/pour → release/result in order.
- Liquids and loose food obey gravity and container capacity; no contents appear before being added.
- A lid, liner, tool, button, cable, handle, or port remains present, attached, or placed where the previous shot left it.
- Respect hand occlusion, working surfaces, hinges, opening direction, and the product's actual scale.
- Keep product color, geometry, branding, and packaging text stable across all shots.
- Give fast actions enough screen time to read; do not hide the proof behind a cut.

## Separate prompt construction

Build two artifacts per concept:

1. **User-facing video-evolution prompt** — one complete plain-text Seedance prompt containing only the 15-second 9:16 format, verified product invariants, six timed segments, visible content, product operation, camera movement, scene sound, matching Malay speech, and physical continuity. It must stand alone when copied. Do not include grid instructions, panel labels, storyboard terminology, first-frame-sheet instructions, ImageGen directions, workflow notes, product-DNA analysis, validation records, file lists, or any face/text/masking production-policy language.
2. **Internal storyboard prompt** — the ImageGen-only instructions needed to render the six first frames. Keep it internal and follow `references/storyboard-spec.md`. Never paste it into the video prompt or final text copy block.

Performer privacy and text-handling decisions belong to the internal storyboard prompt and validation process. Do not add a global or per-shot paragraph about avoiding faces, keeping heads out of frame, masking, mosaics, blur, blocks, stickers, captions, text changes, UI, or watermarks to the user-facing video prompt.

## Positive state locks and risk-filtered constraints

Build the video prompt from intended visible states, not from a catalogue of possible failures.

- Prefer a positive state lock: `掰开后馅料始终保持参考图中统一的开心果绿色、稠密顺滑形态。`
- Do not seed unwanted alternatives by writing `不要白丝、不要芝士丝、不要奶油` or similar lists.
- Keep continuity positive where possible: `前后镜头保持同一颗曲奇。`
- A narrow negative constraint is allowed only when the risk is specific to the current shot, its occurrence would break the proof, and positive wording alone is insufficient. Example: `0s–5s 曲奇保持完整，掰开前不得提前露馅。`
- Use zero negative constraints by default and at most two per concept. Put each constraint in the affected time segment, not in a global negative-prompt block.
- Never import generic internal-check terms such as prices, discounts, QR codes, UI, missing parts, reversed motion, floating objects, cream, cheese, or censor artifacts unless the exact shot genuinely contains that evidenced risk. Even then, first rewrite the requirement as the desired visible state.

Before delivery, apply this gate to every sentence: if it describes the 3×2 sheet, Shot labels, ImageGen, face/privacy handling, packaging-text policy, validation, or a hypothetical defect rather than the intended finished video, remove it from the video prompt and keep it only in its proper internal layer.

## Complete delivery format

Deliver directly in chat without a `.md` attachment, lock card, internal audit, or exposed storyboard prompt:

1. Exact label `方案1｜可复制视频提示词`, then one `text` code block containing only the complete Seedance video-evolution prompt, then the corresponding generated six-frame reference image.
2. Exact label `方案2｜可复制视频提示词`, then one `text` code block, then its reference image.
3. Exact label `方案3｜可复制视频提示词`, then one `text` code block, then its reference image.

Start the video prompt concisely with: `15秒，9:16，真实手机拍摄TikTok质感。` Then state only the verified product invariants needed for visual consistency and the six timed segments. Do not append any face, masking, subtitle, text, UI, watermark, validation, or workflow instruction. Reference imagery may guide concrete scene, action, camera/framing, and plot, but never a person's identity or facial appearance.
