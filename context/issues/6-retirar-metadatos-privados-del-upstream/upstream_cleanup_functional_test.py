"""Validate the recorded cleanup against immutable Git objects; never fetch or publish."""
# ===== Verify immutable cleanup and preserve product blobs =====
# %% [0] Verify immutable cleanup and preserve product blobs
# --- Configuration ---
import importlib.util
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
repo = Path(__file__).resolve().parents[3]
target = "55f80538749c9ce62b82ab91ce6f55bf28136990"
base = target + "^1"

# --- Execution ---
spec = importlib.util.spec_from_file_location("publication", repo / ".githooks/clone-hooks/publication.py")
publication = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publication)
os.chdir(repo)
publication.validate_tree(target)
actual = {name: (mode, kind, oid) for mode, kind, oid, name in publication.entries(target)}
before = {name: (mode, kind, oid) for mode, kind, oid, name in publication.entries(base)}


def product(name):
    # These CI changes were explicitly recorded in the historical cleanup closeout.
    return not publication.private(name) and name != ".gitignore" and not name.startswith(".github/") and name != "tests/article-publication/ci-workflow.test.mjs"


# --- Checks ---
actual_product = {name: blob for name, blob in actual.items() if product(name)}
before_product = {name: blob for name, blob in before.items() if product(name)}
assert actual_product == before_product, "application/article blobs changed"
publication.git("diff", "--check", base, target)
print({"target": target, "product_blobs": sum(product(name) for name in actual), "private_paths": sum(publication.private(name) for name in actual)})
