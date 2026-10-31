# Functional validation: upstream cleanup. Run from any directory.
# %% [0] Verify immutable proposal and preserve product blobs
import importlib.util
import json
import os
from pathlib import Path
repo = Path(__file__).resolve().parents[3]
evidence = repo.parent / "local_volume/shared/upstream-remediation-20261031" / repo.name / "validation.json"
proposal = json.loads(evidence.read_text())
spec = importlib.util.spec_from_file_location("publication", repo / ".githooks/clone-hooks/publication.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)
os.chdir(repo)
pub.validate_tree(proposal["proposed_tree"])
actual = {name: (mode, kind, oid) for mode, kind, oid, name in pub.entries(proposal["proposed_tree"])}
for mode, kind, oid, name in pub.entries(proposal["base_main"]):
    if not pub.private(name) and Path(name).name != ".gitignore":
        assert actual[name] == (mode, kind, oid), name
pub.git("diff", "--check", proposal["base_main"], proposal["proposed_tree"])
print("PASS: private metadata absent; product blobs unchanged")
