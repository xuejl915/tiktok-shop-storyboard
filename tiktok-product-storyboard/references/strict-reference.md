# Strict Reference Adaptation

Read this file only for `STRICT_REFERENCE_ADAPTATION`: the user explicitly requests 1:1, shot-by-shot replication, complete reverse engineering, or strict replacement.

## 1. Duration gate

- Inspect the source with `scripts/inspect_media.py` before writing.
- Record exact source duration, aspect ratio, resolution, fps, and contact sheet.
- If the requested output duration differs from the source, stop calling the result “1:1”. Ask which has priority: identical timing or target duration.
- For variable-frame-rate or timing-critical footage, use frame timestamps rather than assuming constant fps.

## 2. Person gate

- Inventory every person, partial person, hand, reflection, shadow, and background face.
- Resolve whether the user authorizes a replacement performer, wants the source person preserved as a structural reference only, or requires faceless framing.
- “无脸/不要人脸/无参考人物” excludes full faces, partial faces, reflections, screens, posters, and background faces.

## 3. Source evidence library

Build evidence before adapting:

- video metadata and uniform contact sheet;
- shot boundaries and transition type;
- source-frame samples at action starts, contact moments, peaks, and ends;
- verbatim audible speech with timestamp and uncertainty flags;
- product state, hand state, prop state, background, light, camera height, lens feel, and movement per shot.

FFmpeg/FFprobe are required local foundations. PySceneDetect may propose cut boundaries; faster-whisper may draft speech timestamps; OpenCV may support frame comparison, motion, or geometry checks. These are optional enhancements and never substitutes for checking source frames.

## 4. Atomic timeline

Split the source at every change in shot, action phase, contact state, speaker line, camera behavior, or product state. For each atomic interval record:

`start–end | source frame evidence | subject/action | product/contact state | camera | environment/SFX | exact speech | transition | confidence`

Do not compress two sequential physical actions into one prompt phrase. Unknown evidence remains unknown.

## 5. First frames and dynamic evolution

- Define a reproducible first frame for every shot: composition, subject pose, product orientation, hand position, props, background, camera height, and lighting.
- Follow it with the within-shot evolution: action trajectory, camera trajectory, focus/exposure behavior, contact changes, and exact endpoint.
- A product image is appearance evidence; it becomes a first frame only if the user explicitly asks for that composition.

## 6. Replacement mapping

Create an explicit source → replacement map only in strict mode:

- source product → supplied product DNA;
- source performer → permitted performer/framing;
- source setting/prop → retained or intentionally replaced equivalent;
- source claim/dialogue → evidence-safe rewritten line;
- source shot duration, action, camera path, and transition → target counterpart.

Keep timing and function fixed unless the user authorizes a deviation. Never preserve an unsupported claim merely because it appears in the reference.

## 7. Strict deliverables

Include:

1. gates and unresolved conflicts;
2. source evidence table;
3. atomic timeline;
4. replacement map;
5. shot first-frame specifications;
6. time-evolving Seedance prompt;
7. storyboard sheet(s) requested by the user;
8. audit checklist keyed to timestamps.

Label assumptions and confidence. “1:1” refers to evidenced timing, composition, action, and camera behavior—not unauthorized identity cloning, unsupported claims, or corrupted product geometry.

## 8. Finished-video audit

Compare generated output and source on aligned timestamps:

- duration, shot order, boundary timing, and transition;
- camera position, framing, lens feel, movement, and focus;
- performer pose, gaze/face restriction, gesture, and hand contact;
- product silhouette, scale, orientation, parts, branding stability, and working-surface use;
- physical action sequence, gravity, occlusion, and result timing;
- speech content and whether it lags/leads visible proof;
- unwanted captions, overlays, UI, watermark, fabricated claims, and visual artifacts.

Report `timestamp → observed deviation → source evidence → severity → minimal prompt correction`. Separate source-evidenced failures from aesthetic suggestions.

