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

## Complete delivery format

Deliver directly in chat without a `.md` attachment, lock card, internal audit, or exposed storyboard prompt:

1. Exact label `方案1｜可复制视频提示词`, then one `text` code block containing only the complete Seedance video-evolution prompt, then the corresponding generated six-frame reference image.
2. Exact label `方案2｜可复制视频提示词`, then one `text` code block, then its reference image.
3. Exact label `方案3｜可复制视频提示词`, then one `text` code block, then its reference image.

Start the video prompt concisely with: `15秒，9:16，真实手机拍摄TikTok质感。` Then state only the verified product invariants needed for visual consistency and the six timed segments. Do not append any face, masking, subtitle, text, UI, watermark, validation, or workflow instruction. Reference imagery may guide concrete scene, action, camera/framing, and plot, but never a person's identity or facial appearance.
