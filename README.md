# Malaysia TikTok Shop Storyboard

A Codex Skill for turning product evidence into production-ready Malaysian TikTok Shop video concepts, Seedance prompts, and six-shot storyboard sheets.

一个面向马来西亚 TikTok Shop 商品短视频的 Codex Skill。根据商品标题、1–3 张商品图和可选参考视频，生成可执行的 15 秒视频方案、马来语口播、Seedance 动态提示词与六格分镜图。

## What it does / 功能

- Creates three genuinely different 15-second product-video concepts.
- Uses natural, informal Malaysian Malay speech by default.
- Produces a complete six-part timeline and a 3×2 storyboard sheet for each concept.
- Preserves product shape, color, parts, packaging, scale, and physical interactions.
- Supports strict reference-video adaptation when the user explicitly requests shot-by-shot replication.
- Audits generated videos and returns timestamped prompt corrections.
- Protects performer identity through hands-only, below-shoulder, back-view, or naturally occluded composition—never through mosaics, blur, censor blocks, stickers, or artificial face masks that could leak into generated video.
- Rejects invented prices, discounts, certifications, performance claims, subtitles, UI, and watermarks.

## Install with Codex / 使用 Codex 安装

Copy the following prompt into Codex:

```text
请使用内置的 $skill-installer 安装下面这个 GitHub Skill：

https://github.com/xuejl915/tiktok-shop-storyboard/tree/main/malaysia-tiktok-shop-storyboard

仓库是 xuejl915/tiktok-shop-storyboard，Skill 路径是 malaysia-tiktok-shop-storyboard。
请安装完整目录，包括 SKILL.md、agents、references 和 scripts，不能只下载 SKILL.md。
安装到默认的 $CODEX_HOME/skills 目录。如果已经存在同名 Skill，不要直接覆盖，先告诉我。
安装完成后报告实际安装路径，并提醒我从下一条消息开始使用 $malaysia-tiktok-shop-storyboard。
```

English installation prompt:

```text
Use the built-in $skill-installer to install this GitHub Skill:

https://github.com/xuejl915/tiktok-shop-storyboard/tree/main/malaysia-tiktok-shop-storyboard

Install the complete malaysia-tiktok-shop-storyboard directory, including SKILL.md, agents, references, and scripts, into the default $CODEX_HOME/skills directory. Do not overwrite an existing skill without asking me first. After installation, report the installed path and remind me that the skill will be available as $malaysia-tiktok-shop-storyboard on my next message.
```

Start a new chat or send a new message after installation so Codex can discover the Skill.

## Manual installation / 手动安装

Download or clone this repository, then copy the complete folder:

```text
malaysia-tiktok-shop-storyboard/
```

to one of the following locations:

```text
Windows:  C:\Users\<username>\.codex\skills\malaysia-tiktok-shop-storyboard
macOS:    ~/.codex/skills/malaysia-tiktok-shop-storyboard
Linux:    ~/.codex/skills/malaysia-tiktok-shop-storyboard
```

Do not copy only `SKILL.md`; the workflow also uses files under `agents/`, `references/`, and `scripts/`.

## Requirements / 运行要求

- Codex with Skill support.
- Image generation capability for storyboard sheets.
- Python 3 for the included validation and media-inspection scripts.
- FFmpeg and FFprobe when analyzing reference or generated videos.
- Optional for advanced audits: PySceneDetect, faster-whisper, or OpenCV.

The two bundled Python scripts otherwise use only the Python standard library.

## Inputs / 输入资料

Provide:

1. Product title or a short factual description.
2. One to three clear product images.
3. Optional reference video.
4. Optional target language, duration, platform, or strict-replication requirement.

The Skill treats product images as the source of truth and does not invent unprovided specifications or sales claims.

## Quick start / 快速开始

### Three creative concepts

```text
使用 $malaysia-tiktok-shop-storyboard，根据这个商品标题和我上传的商品图，生成三套不同场景、不同剧情的 15 秒马来西亚 TikTok Shop 带货方案。每套包含 Seedance 动态演化提示词和 3×2 六格分镜图。
```

### Strict reference adaptation

```text
使用 $malaysia-tiktok-shop-storyboard，严格逐镜分析我上传的参考视频，并用我的商品替换参考商品。先检查时长、镜头边界、动作顺序和证据缺口；没有证据的部分不要声称做到 1:1。
```

### Generated-video audit

```text
使用 $malaysia-tiktok-shop-storyboard 审计这个生成视频。按时间戳列出画面偏差、证据、可能的提示词原因，以及最小修改后的提示词。
```

## Output / 默认输出

For ordinary creative requests, the Skill returns results in this order:

1. Concept 1 Seedance prompt
2. Concept 1 six-frame storyboard
3. Concept 2 Seedance prompt
4. Concept 2 six-frame storyboard
5. Concept 3 Seedance prompt
6. Concept 3 six-frame storyboard

Each 15-second concept uses the timeline `0–2s`, `2–5s`, `5–8s`, `8–11s`, `11–13s`, and `13–15s`.

## Repository structure / 目录结构

```text
malaysia-tiktok-shop-storyboard/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── banned-claims-and-no-subtitles.md
│   ├── creative-15s.md
│   ├── malaysia-malay.md
│   ├── product-dna.md
│   ├── storyboard-spec.md
│   └── strict-reference.md
└── scripts/
    ├── inspect_media.py
    └── validate_delivery.py
```

## Rename notice / 更名说明

The Skill was previously named `tiktok-product-storyboard`. New installations should use:

```text
$malaysia-tiktok-shop-storyboard
```

If the old Skill is already installed, remove or archive the old folder only after confirming that the new Skill works. Keeping both installed may cause ambiguous activation.

## Updating / 更新

The installer does not overwrite an existing Skill directory automatically. Before updating, preserve any local changes, then replace the installed directory with the latest complete folder from this repository.

## Disclaimer

Users are responsible for verifying product claims, platform rules, music and media rights, and advertising compliance before publishing generated content.
