#!/usr/bin/env python3
"""Validate creative timelines, layer separation, and prompt quality."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


INTERVAL_RE = re.compile(
    r"(?<!\d)(\d+(?:\.\d+)?)\s*(?:s|秒)?\s*[\-–—~～至到]\s*(\d+(?:\.\d+)?)\s*(?:s|秒)?",
    re.IGNORECASE,
)
HEADING_RE = re.compile(
    r"(?im)^[ \t]{0,3}(?:#{1,6}[ \t]*)?(?:方案|概念|concept|option)[ \t]*[-_:#：]*[ \t]*([123](?!\d)|one\b|two\b|three\b).*$"
)
NEGATION_RE = re.compile(
    r"无|禁止|不得|不要|不显示|不添加|严禁|避免|移除|no\b|without\b|never\b|"
    r"do\s+not\b|don't\b|must\s+not\b|forbid",
    re.IGNORECASE,
)
BANNED_TERMS = [
    "字幕", "caption", "auto-caption", "auto caption", "价格", "price", "discount", "sale",
    "折扣", "销量", "促销贴纸", "二维码", "qr code", "watermark", "水印", "guaranteed", "certified",
]
CENSOR_ARTIFACT_TERMS = [
    "打码", "马赛克", "像素化", "模糊脸", "脸部模糊", "纯色遮挡", "遮挡块", "面部遮罩",
    "face mask", "masked face", "mosaic", "pixelation", "pixelated face", "blurred face",
    "censor bar", "censor block", "solid-color face block",
]
FORBIDDEN_VIDEO_META_TERMS = [
    "字幕", "屏幕文字", "新增文字", "改写任何文字", "文字处理", "水印", "促销UI", "界面元素",
    "打码", "马赛克", "像素化", "模糊脸", "脸部模糊", "纯色遮挡", "遮挡块", "面部遮罩",
    "避脸", "头部与脸部", "身份特征", "subtitles", "captions", "on-screen text", "watermark",
    "face mask", "masked face", "mosaic", "pixelation", "blurred face", "censor bar", "censor block",
    "do not add text", "no text",
]
STORYBOARD_LEAK_TERMS = [
    "3×2", "3x2", "六格分镜", "分镜图", "分镜生成", "storyboard", "first-frame sheet",
    "首帧图", "参考图生成规范", "imagegen", "shot 1", "shot 2", "shot 3", "shot 4",
    "shot 5", "shot 6", "反射脸", "背景脸", "纯色遮脸块",
]
GENERIC_FAILURE_TERMS = [
    "价格", "折扣", "二维码", "ui", "缺件", "多余部件", "反向", "漂浮", "融化",
    "白丝", "芝士", "奶油", "水印", "字幕", "打码", "马赛克", "像素化", "模糊脸",
    "遮挡块", "贴纸", "price", "discount", "qr code", "missing part", "extra part",
    "reversed", "floating", "cream", "cheese", "watermark", "caption", "mosaic",
]
CLAUSE_BOUNDARY_RE = re.compile(r"[。！？；;.!?]")


def configure_utf8_streams() -> None:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def split_scripts(text: str) -> list[tuple[str, str]]:
    matches = list(HEADING_RE.finditer(text))
    if not matches:
        return [("delivery", text)]
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(0).strip(" #\t"), text[match.start() : end]))
    return blocks


def intervals_for(text: str) -> list[tuple[float, float]]:
    intervals = [(float(start), float(end)) for start, end in INTERVAL_RE.findall(text)]
    unique = set(intervals)
    if len(unique) > 6 and (0.0, 15.0) in unique:
        intervals = [interval for interval in intervals if interval != (0.0, 15.0)]
    return intervals


def timeline_warnings(intervals: list[tuple[float, float]]) -> list[str]:
    warnings: list[str] = []
    unique = sorted(set(intervals))
    if len(unique) < 6:
        warnings.append(f"Found {len(unique)} distinct time segments; at least 6 are required.")
    if not unique:
        warnings.append("No recognizable time segments were found.")
        return warnings
    if abs(unique[0][0]) > 0.01:
        warnings.append(f"Timeline starts at {unique[0][0]:g}s instead of 0s.")
    cursor = 0.0
    for start, end in unique:
        if end <= start:
            warnings.append(f"Invalid segment {start:g}s–{end:g}s.")
            continue
        if start > cursor + 0.01:
            warnings.append(f"Timeline gap from {cursor:g}s to {start:g}s.")
        elif start < cursor - 0.01:
            warnings.append(f"Timeline overlap at {start:g}s–{min(cursor, end):g}s.")
        cursor = max(cursor, end)
    if cursor < 14.99:
        warnings.append(f"Timeline ends at {cursor:g}s instead of 15s.")
    elif cursor > 15.01:
        warnings.append(f"Timeline extends to {cursor:g}s beyond 15s.")
    return warnings


def banned_hits(text: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        lowered = line.casefold()
        found = sorted({term for term in BANNED_TERMS if term.casefold() in lowered})
        if found and not NEGATION_RE.search(line):
            hits.append({"line": line_number, "terms": found, "excerpt": line.strip()[:180]})
    return hits


def censor_artifact_hits(text: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        lowered = line.casefold()
        found: set[str] = set()
        for term in CENSOR_ARTIFACT_TERMS:
            normalized_term = term.casefold()
            start = 0
            while True:
                index = lowered.find(normalized_term, start)
                if index < 0:
                    break
                clause_prefix = CLAUSE_BOUNDARY_RE.split(line[:index])[-1]
                if not NEGATION_RE.search(clause_prefix):
                    found.add(term)
                start = index + len(normalized_term)
        if found:
            hits.append({"line": line_number, "terms": sorted(found), "excerpt": line.strip()[:180]})
    return hits


def forbidden_video_meta_hits(text: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        lowered = line.casefold()
        found = sorted({term for term in FORBIDDEN_VIDEO_META_TERMS if term.casefold() in lowered})
        if found:
            hits.append({"line": line_number, "terms": found, "excerpt": line.strip()[:180]})
    return hits


def storyboard_leak_hits(text: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        lowered = line.casefold()
        found = sorted({term for term in STORYBOARD_LEAK_TERMS if term.casefold() in lowered})
        if found:
            hits.append({"line": line_number, "terms": found, "excerpt": line.strip()[:180]})
    return hits


def dense_negative_constraint_hits(text: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for clause in filter(None, (part.strip() for part in CLAUSE_BOUNDARY_RE.split(line))):
            lowered = clause.casefold()
            found = sorted({term for term in GENERIC_FAILURE_TERMS if term.casefold() in lowered})
            negations = len(NEGATION_RE.findall(clause))
            list_items = len(re.split(r"[、,，]", clause))
            if len(found) >= 3 or negations >= 3 or (found and negations and list_items >= 4):
                hits.append({
                    "line": line_number,
                    "terms": found,
                    "negation_count": negations,
                    "excerpt": clause[:180],
                })
    return hits


def main() -> int:
    configure_utf8_streams()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("delivery", nargs="?", help="UTF-8 user-facing prompt text file; omit or use - for stdin")
    args = parser.parse_args()
    try:
        if not args.delivery or args.delivery == "-":
            text = sys.stdin.read()
            source = "stdin"
        else:
            path = Path(args.delivery).expanduser().resolve()
            text = path.read_text(encoding="utf-8")
            source = str(path)
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"status": "警告", "status_code": "WARNING", "error": str(exc)}, ensure_ascii=False))
        return 2

    scripts: list[dict[str, Any]] = []
    for name, block in split_scripts(text):
        intervals = intervals_for(block)
        warnings = timeline_warnings(intervals)
        scripts.append({
            "name": name,
            "status": "通过" if not warnings else "警告",
            "status_code": "PASS" if not warnings else "WARNING",
            "segment_count": len(set(intervals)),
            "intervals": intervals,
            "warnings": warnings,
        })

    global_warnings: list[str] = []
    hits = banned_hits(text)
    if hits:
        global_warnings.append("Potentially prohibited terms appear outside an explicit negative constraint.")
    censor_hits = censor_artifact_hits(text)
    if censor_hits:
        global_warnings.append("A face-censor artifact may be requested instead of explicitly prohibited.")
    meta_hits = forbidden_video_meta_hits(text)
    if meta_hits:
        global_warnings.append("Production or policy meta-instructions appear in the user-facing video prompt.")
    storyboard_hits = storyboard_leak_hits(text)
    if storyboard_hits:
        global_warnings.append("Storyboard-generation instructions appear in the user-facing video prompt.")
    dense_negative_hits = dense_negative_constraint_hits(text)
    if dense_negative_hits:
        global_warnings.append("A dense or generic negative-constraint list appears in the video prompt; use positive shot-specific state language instead.")
    passed = not global_warnings and all(item["status_code"] == "PASS" for item in scripts)
    result = {
        "status": "通过" if passed else "警告",
        "status_code": "PASS" if passed else "WARNING",
        "source": source,
        "scripts": scripts,
        "global_warnings": global_warnings,
        "banned_term_hits": hits,
        "censor_artifact_hits": censor_hits,
        "forbidden_video_meta_hits": meta_hits,
        "storyboard_leak_hits": storyboard_hits,
        "dense_negative_constraint_hits": dense_negative_hits,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
