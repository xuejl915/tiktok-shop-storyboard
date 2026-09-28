# Banned Claims and No-Subtitles Rules

Apply this reference to every route.

## No-screen-text rule

Do not add any video-layer text:

- subtitles, burned-in captions, auto-captions, karaoke words, or narration text;
- titles, feature callouts, prices, discounts, sales volume, promotion stickers, countdowns, or CTA text;
- QR codes, floating words, lower thirds, UI, app chrome, or watermarks.

Original text physically printed on supplied product packaging may remain visible. Do not add, rewrite, translate, correct, sharpen into different words, or animate it. A Shot label may appear only outside the video panels in a storyboard gutter/border.

## Never fabricate

Unless the user provides verifiable evidence and explicitly asks to use it, do not state or imply:

- price, discount, sale, stock scarcity, sales count, ranking, or popularity;
- certification, award, official endorsement, brand relationship, authenticity, or origin;
- medical, therapeutic, health, hygiene, safety, child-safety, or risk-prevention effects;
- heat/cold retention, leak-proofing, waterproofing, fire resistance, durability, load capacity, battery life, speed, power, dimensions, material composition, or other performance specifications;
- comparison superiority, guarantee, permanence, or universal results;
- any feature or benefit not visible in the provided assets or stated by the user.

Show an evidenced action instead of upgrading it into a broader claim. Speech cannot announce a benefit before the relevant result is visible.

## Internal video checks

Inspect the draft internally in four categories: unsupported claims, unwanted overlays, product/part continuity, and contact/action continuity. These are audit categories, not prompt copy. Do not paste or paraphrase their names, examples, or failure vocabulary into the user-facing video prompt.

When a check finds a relevant risk:

1. Rewrite it first as the intended visible state at the affected moment.
2. Keep the wording concrete and product-specific.
3. Use a negative constraint only if that exact shot still has a high-probability failure that would break the concept.
4. Keep such a constraint beside that shot; never accumulate a global negative-prompt list.

For example, preserve a pistachio filling with `馅料始终保持参考图中的统一开心果绿色形态`, not a list mentioning white strands, cheese, cream, or other unwanted alternatives. Internal checks must not introduce new visual concepts into the generation prompt.

## Storyboard-only performer privacy

Apply the following when building the internal storyboard prompt. Do not copy this paragraph, its censor-artifact vocabulary, or any storyboard-production instruction into the user-facing video-evolution prompt:

`Protect identity through composition, not face covering. By default use hands-only, below-shoulder framing, back views, or natural occlusion so faces remain outside the frame. Do not add mosaics, pixelation, face blur, censor bars, solid-color blocks, stickers, or artificial masks to storyboard references. If visible faces are explicitly permitted, use a newly generated anonymous performer with a natural unobscured face; never copy a reference person's identity or facial appearance. Reference people may guide only pose, scene, action, framing, and plot.`

For the delivered video prompt, simply describe the intended performer, action, and camera framing. Do not mention face avoidance, masking, mosaics, blur, censoring, face blocks, text handling, captions, watermarks, UI removal, or the storyboard privacy process. Keep those decisions internal to storyboard generation and final validation.
