#!/usr/bin/env python3
"""Compatibility wrapper for tools/media_pipeline/openai_dual_format_experiment.py."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "media_pipeline" / "openai_dual_format_experiment.py"
sys.path.insert(0, str(SCRIPT.parent))
runpy.run_path(str(SCRIPT), run_name="__main__")
