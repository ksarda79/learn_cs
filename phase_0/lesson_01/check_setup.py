"""Run this from VS Code's terminal to confirm your environment is ready.

    python check_setup.py
"""
import shutil
import sys


def check(label, ok, fix):
    mark = "OK  " if ok else "FAIL"
    print(f"[{mark}] {label}")
    if not ok:
        print(f"       -> {fix}")
    return ok


results = [
    check(
        f"Python version is 3.11 or newer (you have {sys.version.split()[0]})",
        sys.version_info >= (3, 11),
        "Install the latest Python from python.org and reopen VS Code.",
    ),
    check(
        "A virtual environment is active",
        sys.prefix != sys.base_prefix,
        "In the terminal run the activate command for .venv (see setup step 5).",
    ),
    check(
        "Git is installed",
        shutil.which("git") is not None,
        "Install Git from git-scm.com, then restart VS Code.",
    ),
]

try:
    import pytest  # noqa: F401
    results.append(check("pytest is installed", True, ""))
except ImportError:
    results.append(check("pytest is installed", False, "Run: pip install pytest"))

print()
print("All set - you're ready for Lesson 0.1!" if all(results)
      else "Fix the FAIL lines above, then run this again.")
