"""Issue #1: run the real shared local publication scenarios; no external publication."""
import re
from pathlib import Path

GLOBAL_SCRIPT = Path(__file__).resolve().parents[2] / "tests/article_publication_site_functional_test.py"
source = GLOBAL_SCRIPT.read_text(encoding="utf-8")
markers = list(re.finditer(r"^# %% \[([^\]]+)\].*$", source, re.M))
cells = {m.group(1): source[m.end():markers[i + 1].start() if i + 1 < len(markers) else len(source)] for i, m in enumerate(markers)}
state = {"__file__": str(GLOBAL_SCRIPT), "__name__": "__main__"}


def run_cell(cell_id):
    exec(compile(cells[cell_id], str(GLOBAL_SCRIPT), "exec"), state)
    return state


# ===== Sync the real article corpus =====
# %% [0] Sync the real article corpus
# --- Configuration ---
cell_id = "0"
# --- Execution ---
state = run_cell(cell_id)
# --- Checks ---
assert state["article_slugs"]

# ===== Attachment projection and fail-closed validation =====
# %% [1] Attachment projection and fail-closed validation
# --- Configuration ---
cell_id = "1"
# --- Execution ---
state = run_cell(cell_id)
# --- Checks ---
assert state["ok"].returncode == 0 and state["bad"].returncode != 0

# ===== Build the static site =====
# %% [2] Build the static site
# --- Configuration ---
cell_id = "2"
# --- Execution ---
state = run_cell(cell_id)
# --- Checks ---
assert state["build"].returncode == 0 and state["published"]

# ===== Serve and read the built site =====
# %% [3] Serve and read the built site
# --- Configuration ---
cell_id = "3"
# --- Execution ---
state = run_cell(cell_id)
# --- Checks ---
assert state["home"][0] == 200 and state["feed"][0] == 200 and state["missing"][0] == 404
