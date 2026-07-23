#!/usr/bin/env python3
"""Compatibility wrapper for tools/media_pipeline/verify_visual_qa_verdicts.py."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "media_pipeline" / "verify_visual_qa_verdicts.py"
sys.path.insert(0, str(SCRIPT.parent))
runpy.run_path(str(SCRIPT), run_name="__main__")
