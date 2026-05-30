#!/usr/bin/env python3
"""Export a PPTX to PNG previews on Windows with Microsoft PowerPoint."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def export_preview(pptx: Path, output_dir: Path, width: int = 1600, height: int = 900) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    script = f"""
$ErrorActionPreference = 'Stop'
$pptx = '{str(pptx.resolve()).replace("'", "''")}'
$out = '{str(output_dir.resolve()).replace("'", "''")}'
New-Item -ItemType Directory -Force -Path $out | Out-Null
$app = New-Object -ComObject PowerPoint.Application
$presentation = $app.Presentations.Open($pptx, $true, $false, $false)
try {{
  foreach ($slide in $presentation.Slides) {{
    $path = Join-Path $out ('slide_{{0:D2}}.png' -f $slide.SlideIndex)
    $slide.Export($path, 'PNG', {width}, {height}) | Out-Null
  }}
}} finally {{
  $presentation.Close()
  $app.Quit()
}}
"""
    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=900)
    args = parser.parse_args()
    export_preview(args.pptx, args.output_dir, args.width, args.height)


if __name__ == "__main__":
    main()
