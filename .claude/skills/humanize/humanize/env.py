"""Where things are, found without depending on git or on the caller's PATH."""
import shutil
from pathlib import Path


def find_root(start=None):
    """The repository root: the nearest folder at or above `start` that holds a humanize installation
    (.humanize/manifest.json) or a git checkout (.git, a folder or, in worktrees, a file). None if there is neither."""
    here = Path(start or Path.cwd()).resolve()
    for folder in (here, *here.parents):
        if (folder / ".humanize" / "manifest.json").is_file() or (folder / ".git").exists():
            return folder
    return None


def has_git(root):
    """git is installed and `root` is a git checkout."""
    return bool(shutil.which("git")) and (Path(root) / ".git").exists()
