#!/usr/bin/env python3
"""Compatibility wrapper for tools/media_pipeline/render_local_video_edit.py."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "media_pipeline" / "render_local_video_edit.py"
sys.path.insert(0, str(SCRIPT.parent))
runpy.run_path(str(SCRIPT), run_name="__main__")
