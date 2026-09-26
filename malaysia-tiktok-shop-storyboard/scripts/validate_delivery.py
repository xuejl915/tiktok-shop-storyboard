#!/usr/bin/env python3
"""Validate creative-delivery timelines and global no-overlay constraints."""

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
NO_OVERLAY_RE = re.compile(
    r"无(?:屏幕|视频内|新增)?字幕|不要字幕|禁止.*字幕|不得.*字幕|不显示.*字幕|"
    r"no\s+(?:on[- ]screen\s+)?(?:subtitles?|captions?)|without\s+(?:subtitles?|captions?)|"
    r"do\s+not\s+(?:add|show|use).*(?:subtitles?|captions?)",
    re.IGNORECASE,
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


def configure_utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
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


def main() -> int:
    configure_utf8_streams()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("delivery", nargs="?", help="UTF-8 delivery text/Markdown file; omit or use - for stdin")
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
        if not NO_OVERLAY_RE.search(block):
            warnings.append("Missing an explicit no-on-screen-subtitles constraint in this script.")
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
    passed = not global_warnings and all(item["status_code"] == "PASS" for item in scripts)
    result = {
        "status": "通过" if passed else "警告",
        "status_code": "PASS" if passed else "WARNING",
        "source": source,
        "scripts": scripts,
        "global_warnings": global_warnings,
        "banned_term_hits": hits,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
