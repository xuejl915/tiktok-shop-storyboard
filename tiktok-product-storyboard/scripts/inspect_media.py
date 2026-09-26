#!/usr/bin/env python3
"""Inspect a local video with ffprobe and create a uniform six-frame contact sheet."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def configure_utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def fail(message: str, *, details: str | None = None, code: int = 1) -> int:
    payload: dict[str, Any] = {"error": message}
    if details:
        payload["details"] = details.strip()
    print(json.dumps(payload, ensure_ascii=False), file=sys.stderr)
    return code


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")


def resolve_tool(explicit: Path | None, name: str) -> str | None:
    if explicit is not None:
        candidate = explicit.expanduser().resolve()
        return str(candidate) if candidate.is_file() else None
    return shutil.which(name)


def parse_fps(value: str) -> float:
    try:
        fps = float(Fraction(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid fps value: {value!r}") from exc
    if fps <= 0:
        raise ValueError(f"non-positive fps value: {value!r}")
    return fps


def main() -> int:
    configure_utf8_streams()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path, help="Path to a local video file")
    parser.add_argument(
        "--output",
        type=Path,
        help="Contact-sheet PNG path (default: beside the video as <stem>_contact_sheet.png)",
    )
    parser.add_argument("--frames", type=int, default=6, help="Uniform frames in the contact sheet (default: 6)")
    parser.add_argument("--ffprobe-bin", type=Path, help="Explicit ffprobe executable path")
    parser.add_argument("--ffmpeg-bin", type=Path, help="Explicit ffmpeg executable path")
    args = parser.parse_args()

    video = args.video.expanduser().resolve()
    if not video.is_file():
        return fail("Video file does not exist or is not a file.", details=str(video), code=2)
    if args.frames < 1:
        return fail("--frames must be at least 1.", code=2)

    ffprobe = resolve_tool(args.ffprobe_bin, "ffprobe")
    ffmpeg = resolve_tool(args.ffmpeg_bin, "ffmpeg")
    if not ffprobe or not ffmpeg:
        missing = [name for name, path in (("ffprobe", ffprobe), ("ffmpeg", ffmpeg)) if not path]
        return fail("Required local executable(s) not found on PATH.", details=", ".join(missing), code=3)

    probe_cmd = [
        ffprobe,
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,avg_frame_rate,r_frame_rate:format=duration",
        "-of",
        "json",
        str(video),
    ]
    probed = run(probe_cmd)
    if probed.returncode != 0:
        return fail("ffprobe could not read the video.", details=probed.stderr, code=4)

    try:
        metadata = json.loads(probed.stdout)
        stream = metadata["streams"][0]
        duration = float(metadata["format"]["duration"])
        width = int(stream["width"])
        height = int(stream["height"])
        fps = parse_fps(stream.get("avg_frame_rate") or stream.get("r_frame_rate"))
        if duration <= 0 or width <= 0 or height <= 0:
            raise ValueError("duration and dimensions must be positive")
    except (KeyError, IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return fail("Video metadata is incomplete or invalid.", details=str(exc), code=5)

    output = (args.output or video.with_name(f"{video.stem}_contact_sheet.png")).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    columns = 3 if args.frames >= 3 else args.frames
    rows = (args.frames + columns - 1) // columns
    sample_rate = args.frames / duration
    video_filter = (
        f"fps={sample_rate:.12f},"
        "scale='min(480,iw)':-2,"
        f"tile={columns}x{rows}:nb_frames={args.frames}:padding=8:margin=8:color=white"
    )
    render_cmd = [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(video),
        "-vf",
        video_filter,
        "-frames:v",
        "1",
        str(output),
    ]
    rendered = run(render_cmd)
    if rendered.returncode != 0 or not output.is_file():
        return fail("ffmpeg could not create the contact sheet.", details=rendered.stderr, code=6)

    result = {
        "duration": round(duration, 3),
        "width": width,
        "height": height,
        "fps": round(fps, 3),
        "contact_sheet_path": str(output),
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
