#!/usr/bin/env python3
"""Entry point: python tools/editor/editor.py <command> ... (see `--help`)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from titan_editor.cli import main  # noqa: E402

rc = main()
sys.exit(rc if isinstance(rc, int) else 0)  # commands may return data objects; only ints are exit codes
