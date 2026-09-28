# Six-Frame Storyboard Specification

Generate one complete sheet for each concept with ImageGen.

This specification applies only to the internal ImageGen prompt. Never paste these layout, labeling, identity, or reference-board instructions into the user-facing video-evolution prompt. The final response shows the resulting image, not this internal prompt.

## Layout

- Exactly 6 panels in a 3-column × 2-row grid.
- Reading order: top-left to top-right, then bottom-left to bottom-right.
- Panels correspond to the first frames at `0s`, `2s`, `5s`, `8s`, `11s`, and `13s` for Shots 1–6.
- Keep equal panel sizes and clear gutters. Do not create extra thumbnails, inset close-ups, cover art, or a title panel.
- Put `Shot 1`–`Shot 6` labels only on the outer border or gutters. Labels are production annotations outside each video frame and must not appear in the depicted scene.

## Continuity

- Use the same approved anonymous performer/body framing throughout a concept unless its timeline explicitly introduces another person.
- Protect identity through composition: hands-only, below-shoulder framing, back views, or natural occlusion with the face outside the frame. Never repair a visible face by drawing over it; reframe or regenerate the panel instead.
- Storyboards that may become video references must contain no mosaics, pixelation, face blur, censor bars, solid-color face blocks, stickers, or artificial masks because video models can reproduce them. If the user explicitly permits visible faces, use a newly generated anonymous performer with a natural unobscured face, never the reference person's identity or facial appearance.
- Keep the supplied product's silhouette, proportions, color, parts, logo placement, packaging text, and scale stable.
- Maintain the same environment geography, surface, light direction, props, wardrobe, hand state, and product state across adjacent shots unless the scripted action changes them.
- Respect face restrictions in every panel, including reflections and background people.
- The panel must depict the start state of its shot, not a collage of the whole action.

## ImageGen prompt contents

Include: 3×2 grid; exact panel-to-shot mapping; product-DNA invariants; setting; first-frame composition and action state for all six panels; consistent realistic phone-video look; identity-safe composition with faces outside the frame by default; **no mosaic, pixelation, face blur, censor bar, solid-color face block, sticker, or artificial mask**; reference people used only for pose/action/framing, never identity or facial appearance; border-only labels; no in-frame text, caption, price, sticker, QR code, UI, lower third, or watermark; unchanged original packaging text only.

If ImageGen cannot guarantee precise labels, generate clean panels without in-frame labels and use Pillow only to add deterministic `Shot 1`–`Shot 6` text to gutters afterward.
