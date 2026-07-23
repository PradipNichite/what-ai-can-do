#!/usr/bin/env python3
"""Compatibility wrapper for tools/media_pipeline/upload_tmpfiles.py."""

from __future__ import annotations

import runpy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "media_pipeline" / "upload_tmpfiles.py"
runpy.run_path(str(SCRIPT), run_name="__main__")
