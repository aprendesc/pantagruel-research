# Project functional testing: article corpus to published Astro site
# Local implementation: scripts/sync-articles.mjs + `npm run build` (Astro 4) + `npm run preview`
# Required setup: Node 20+ with the installed node_modules (`npm ci` already run); no network, no credentials
# Environment: local only. Nothing is deployed, pushed or announced; docs/ is read, derived folders (src/content/blog, public/articles, dist) are regenerated and git-ignored
# Working directory: repository root; run with `python3 context/tests/article_publication_site_functional_test.py`
# Cell order: [0] -> [1] -> [2] -> [3]
# Observed: the published URL slug is derived from the article title (accents dropped, e.g. `perceptrn`), not from the docs folder slug

# ===== Sync the real article corpus =====
# %% [0] Sync the real article corpus
import html
import re
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# --- Configuration ---
docs_dir = REPO / "docs"
blog_dir = REPO / "src" / "content" / "blog"
assets_dir = REPO / "public" / "articles"
article_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-([a-z0-9]+(?:-[a-z0-9]+)*)$")


def run(*args, cwd=REPO, check=True, timeout=600):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    if check:
        assert result.returncode == 0, result.stdout + result.stderr
    return result


# --- Execution ---
article_slugs = sorted(article_pattern.match(d.name).group(1) for d in docs_dir.iterdir() if d.is_dir() and article_pattern.match(d.name))
tracked_before = run("git", "status", "--porcelain").stdout
first_sync = run("npm", "run", "sync:articles")
second_sync = run("npm", "run", "sync:articles")
tracked_after = run("git", "status", "--porcelain").stdout

# --- Checks ---
assert article_slugs, "el corpus de docs/ no tiene artículos con nombre YYYY-MM-DD-slug"
for slug in article_slugs:
    source = next(d for d in docs_dir.iterdir() if d.name.endswith(slug))
    projected = blog_dir / f"{slug}.md"
    assert projected.is_file(), projected
    assert projected.read_text(encoding="utf-8").startswith("---\ntitle:")
    for attachment in source.iterdir():
        if attachment.suffix != ".md":
            assert (assets_dir / slug / attachment.name).is_file(), attachment.name
assert tracked_before == tracked_after, "la sincronización no debe cambiar archivos versionados"
assert first_sync.returncode == 0 and second_sync.returncode == 0
print(article_slugs)

# ===== Attachment projection and fail-closed validation =====
# %% [1] Attachment projection and fail-closed validation
# --- Configuration ---
scratch_slug = "functional-check"
scratch_folder = f"2026-11-03-{scratch_slug}"
scratch_root = Path(tempfile.mkdtemp(prefix="pantagruel-research-ft-"))
article_dir = scratch_root / "docs" / scratch_folder
article_dir.mkdir(parents=True)
(article_dir / "figure.png").write_bytes(b"\x89PNG\r\n\x1a\n")
article_text = '---\ntitle: "Functional check"\ndescription: "Scratch article"\npubDate: "Nov 03 2026"\n---\n\nSee ![figure](./figure.png) and [external](https://example.com/a.png).\n'
(article_dir / f"{scratch_folder}.md").write_text(article_text, encoding="utf-8")

# --- Execution ---
ok = run("node", str(REPO / "scripts" / "sync-articles.mjs"), "--root", str(scratch_root))
projected_text = (scratch_root / "src" / "content" / "blog" / f"{scratch_slug}.md").read_text(encoding="utf-8")
bad_root = Path(tempfile.mkdtemp(prefix="pantagruel-research-ft-bad-"))
(bad_root / "docs" / "Not-A-Valid-Folder").mkdir(parents=True)
((bad_root / "docs" / "Not-A-Valid-Folder") / "article.md").write_text(article_text, encoding="utf-8")
bad = run("node", str(REPO / "scripts" / "sync-articles.mjs"), "--root", str(bad_root), check=False)

# --- Checks ---
assert ok.returncode == 0, ok.stdout + ok.stderr
assert f"../../articles/{scratch_slug}/figure.png" in projected_text
assert "https://example.com/a.png" in projected_text
assert (scratch_root / "public" / "articles" / scratch_slug / "figure.png").is_file()
assert bad.returncode != 0, "una carpeta de artículo inválida debe fallar"
assert not (bad_root / "src" / "content" / "blog").exists() or not any((bad_root / "src" / "content" / "blog").iterdir())
print(projected_text.splitlines()[-1], "| invalid folder exit code:", bad.returncode)
shutil.rmtree(scratch_root, ignore_errors=True)
shutil.rmtree(bad_root, ignore_errors=True)

# ===== Build the static site =====
# %% [2] Build the static site
# --- Configuration ---
dist_dir = REPO / "dist"
site_base = "pantagruel-research"

# --- Execution ---
shutil.rmtree(dist_dir, ignore_errors=True)
build = run("npm", "run", "build")
index_html = (dist_dir / "index.html").read_text(encoding="utf-8")
rss_xml = (dist_dir / "rss.xml").read_text(encoding="utf-8")
sitemap_files = sorted(p.name for p in dist_dir.glob("sitemap*.xml"))

# --- Checks ---
assert build.returncode == 0 and (dist_dir / "404.html").is_file()
published = {}
for slug in article_slugs:
    title = re.search(r'^title: "(.*)"$', (blog_dir / f"{slug}.md").read_text(encoding="utf-8"), re.M).group(1)
    page = next((d.name for d in (dist_dir / "blog").iterdir() if d.is_dir() and (d / "index.html").is_file() and html.unescape(title) in html.unescape((d / "index.html").read_text(encoding="utf-8"))), None)
    assert page is not None, f"no hay página publicada para el artículo {slug}"
    assert f"/{site_base}/blog/{page}" in rss_xml
    published[slug] = page
assert "<html" in index_html.lower() and site_base in index_html
assert "sitemap-index.xml" in sitemap_files
print(published, sitemap_files)

# ===== Serve and read the built site =====
# %% [3] Serve and read the built site
# --- Configuration ---
preview_port = 43999
base_url = f"http://127.0.0.1:{preview_port}/{site_base}"

# --- Execution ---
preview = subprocess.Popen(["npm", "run", "preview", "--", "--host", "127.0.0.1", "--port", str(preview_port)], cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
try:
    def fetch(path):
        try:
            with urllib.request.urlopen(f"{base_url}{path}", timeout=5) as response:
                return response.status, response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            return error.code, error.read().decode("utf-8")

    deadline = time.time() + 60
    home = None
    while time.time() < deadline and home is None:
        try:
            home = fetch("/")
        except (urllib.error.URLError, ConnectionError):
            time.sleep(0.5)
    pages = {slug: fetch(f"/blog/{page}/") for slug, page in published.items()}
    feed = fetch("/rss.xml")
    missing = fetch("/blog/no-such-article/")
finally:
    preview.terminate()
    preview.wait(timeout=20)

# --- Checks ---
assert home is not None and home[0] == 200
for slug, (status, body) in pages.items():
    assert status == 200 and "<article" in body.lower()
assert feed[0] == 200 and "<rss" in feed[1]
assert missing[0] == 404
print(home[0], {slug: page[0] for slug, page in pages.items()}, feed[0], missing[0])

# ===== Blocked scenarios (not executed) =====
# GitHub Pages deployment, the reviewed upstream release flow and social announcements publish outside this machine: BLOCKED/PENDING, never simulated here.
print("BLOCKED: Pages deployment and upstream release (external, needs reviewed flow); social announcement (external posting, needs explicit authorization)")
