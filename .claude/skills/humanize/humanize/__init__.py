"""humanize: deterministic pre/post assessment for line-editing AI-drafted prose.

The tool never calls a language model. A chat agent does the rewriting; this
package decides what to fix (check, brief) and verifies the result (gate).
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
VERSIONS = json.loads((DATA / "versions.json").read_text())
__version__ = VERSIONS["package"]
