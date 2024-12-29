from __future__ import annotations

from pathlib import Path

# Is set during `onbuild` if `pip install hrid` is used
__version__ = ""

if not __version__:
    try:
        import versioningit
    except ImportError:  # pragma: no cover
        import importlib.metadata

        __version__ = importlib.metadata.version("ynab-analysis")
    else:
        PROJECT_DIR = Path(__file__).parents[2]
        __version__ = versioningit.get_version(project_dir=PROJECT_DIR)
