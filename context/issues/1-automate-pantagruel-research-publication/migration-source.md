# feature/1-automate-pantagruel-research-publication · [Issue #1](https://github.com/aprendesc/pantagruel-research/issues/1) · PR pendiente

## Context (delta_time: 04/11/2026 14:10)

### Descripción

Automatiza el ciclo editorial de Pantagruel Research: una fuente Markdown por artículo, generación reproducible del sitio y revisión local antes de publicar. Es una contribución de código y herramientas de publicación, aunque su registro antiguo la etiquetaba documental. El histórico registra entregas de agosto de 2026; la migración no reabre despliegues ni anuncios.

### Specialized skills

- [publish-pantagruel-article](../../../.agents/skills/publish-pantagruel-article/SKILL.md): publicación editorial y revisión local.
- [pantagruel-research-social-announce](../../../.agents/skills/pantagruel-research-social-announce/SKILL.md): anuncios con autorización independiente.

---
## Diff (delta_time: 04/11/2026 14:10)

```text
Comparación histórica pendiente: no hay rama de tarea local conservada; develop no equivale al diff de la contribución.
```

---
## Test Profiling (delta_time: 04/11/2026 14:10)

**Script de test funcional:** `context/issues/1-automate-pantagruel-research-publication/article_publication_functional_test.py`.

### Árbol de abstracción

```text
A0 Celda
└── A1 Validación funcional
    └── A2 Aplicación y recursos
```

### context/issues/1-automate-pantagruel-research-publication/article_publication_functional_test.py :: Sync the real article corpus

```text
LOW · A1
Celda de entrada: # %% [0] Sync the real article corpus
Descripción: Sync the real article corpus; comprueba el mecanismo local sin publicar ni operar servicios externos.
── Configuración ─────────────────────────────
└── article_publication_functional_test.py
    └── cell_id = "0"

── Diagrama ──────────────────────────────────
┌────────────────────────────────────────────────────────────────────┐
│ (1) article_publication_functional_test.run_cell("0") -> state (a) │ ───▶ [ (2) assert state["article_slugs"] ]
└────────────────────────────────────────────────────────────────────┘
R ← docs/
W → src/content/blog/; public/articles/

── Visor de variables y validaciones ──────────
(a) state · len(state["article_slugs"]) = 2
[OK] (2) assert state["article_slugs"]
```

### context/issues/1-automate-pantagruel-research-publication/article_publication_functional_test.py :: Attachment projection and fail-closed validation

```text
LOW · A1
Celda de entrada: # %% [1] Attachment projection and fail-closed validation
Descripción: Attachment projection and fail-closed validation; comprueba el mecanismo local sin publicar ni operar servicios externos.
── Configuración ─────────────────────────────
└── article_publication_functional_test.py
    └── cell_id = "1"

── Diagrama ──────────────────────────────────
┌────────────────────────────────────────────────────────────────────┐
│ (1) article_publication_functional_test.run_cell("1") -> state (a) │ ───▶ [ (2) assert ok.returncode == 0 and bad.returncode != 0 ]
└────────────────────────────────────────────────────────────────────┘
R ← scripts/sync-articles.mjs
W → directorios temporales del escenario

── Visor de variables y validaciones ──────────
(a) state · state["bad"].returncode = 1
[OK] (2) assert ok.returncode == 0 and bad.returncode != 0
```

### context/issues/1-automate-pantagruel-research-publication/article_publication_functional_test.py :: Build the static site

```text
LOW · A1
Celda de entrada: # %% [2] Build the static site
Descripción: Build the static site; comprueba el mecanismo local sin publicar ni operar servicios externos.
── Configuración ─────────────────────────────
└── article_publication_functional_test.py
    └── cell_id = "2"

── Diagrama ──────────────────────────────────
┌────────────────────────────────────────────────────────────────────┐
│ (1) article_publication_functional_test.run_cell("2") -> state (a) │ ───▶ [ (2) assert build.returncode == 0 and published ]
└────────────────────────────────────────────────────────────────────┘
R ← corpus y configuración Astro
W → dist/

── Visor de variables y validaciones ──────────
(a) state · len(state["published"]) = 2
[OK] (2) assert build.returncode == 0 and published
```

### context/issues/1-automate-pantagruel-research-publication/article_publication_functional_test.py :: Serve and read the built site

```text
LOW · A1
Celda de entrada: # %% [3] Serve and read the built site
Descripción: Serve and read the built site; comprueba el mecanismo local sin publicar ni operar servicios externos.
── Configuración ─────────────────────────────
└── article_publication_functional_test.py
    └── cell_id = "3"

── Diagrama ──────────────────────────────────
┌────────────────────────────────────────────────────────────────────┐
│ (1) article_publication_functional_test.run_cell("3") -> state (a) │ ───▶ [ (2) assert home[0] == 200 and feed[0] == 200 and missing[0] == 404 ]
└────────────────────────────────────────────────────────────────────┘
R ← dist/
C → http://127.0.0.1:43999/pantagruel-research/

── Visor de variables y validaciones ──────────
(a) state · state["home"][0] = 200
[OK] (2) assert home[0] == 200 and feed[0] == 200 and missing[0] == 404
```

---
## Persistence (delta_time: 04/11/2026 14:10)

```text
Local · raíz del repositorio
├── docs/                         fuente editorial versionada
├── src/content/blog/             proyección generada
├── public/articles/              recursos generados
└── dist/                         build local derivado
GitHub Pages · publicación externa no ejecutada por esta migración
```

---
## Execution plan (delta_time: 04/11/2026 14:10)

### Secuencia de ejecución

**Autonomía de la migración:** HIGH; no amplía la autorización histórica de publicación.

1. [OK] **Etapa 1 — Revalidar el ciclo local:** sincronización, adjuntos, build y lectura HTTP mediante las celdas 0–3.
2. [GATE] **Etapa 2 — Publicación y anuncios:** únicamente tras decisión humana, fuera de esta migración privada.

### Etapa 1 — Revalidar el ciclo local

- **Detalles y especificaciones:** las celdas 0–3 del script de issue reutilizan las celdas reales del validador global. No se sustituyen por simulaciones ni se publica externamente. Se conserva a continuación la especificación y evidencia histórica completa.

- **Context:**

- **Historical contribution record:**

- **Skills**: This contract declares the `coding-contract-guidelines` skills.
- **Historical status:** The source listed Backlog; the implementation reports below do not establish current GitHub status.
- **Owner**: `aprendesc` is responsible for the contribution.
- **Historical traceability:** The source used the now-deprecated label `skill:documental-contribution` and milestone `001 — Publicación editorial`; this is provenance, not an instruction to invoke that removed methodology.

- **Editorial cycle:**

Pantagruel Research needs a repeatable editorial cycle. The cycle must keep one canonical Markdown file for each article, allow local review before publication, and allow social distribution only after production has been verified.

The agreed flow is: create a branch for one article from `develop`; merge it into `develop`; run a local preview; obtain approval; merge `develop` into `main`; and deploy through GitHub Pages. LinkedIn and X use one global skill. The skill must keep copy and publication checks specific to each network.

The implementation branch is `feature/1-automate-pantagruel-research-publication`. The current workflow already deploys `main`. The commands `npm run build` and `astro preview` have been verified locally at `http://127.0.0.1:4321/pantagruel-research/`.

- **Consolidated evidence and decisions:**

- **2026-08-10 11:46**: The issue was reactivated and refined with the agreed article-branch cycle, local pre in `develop`, and production in `main`.
- **2026-08-10 11:46**: The contract path was corrected to `context/issues/1-automate-pantagruel-research-publication/1-automate-pantagruel-research-publication.md`. The Development Methodology wrapper was adopted, and the branch `feature/1-automate-pantagruel-research-publication` was recorded.
- **2026-08-10 11:52**: A methodology audit added `Labels`, completed the technical and documentary parameters, and aligned the article-branch rule with the traceability format `article/<issue-number>-<slug>`.
- **2026-08-10 12:08**: Reproducible synchronization, local preview, production protection, separate publication skills for LinkedIn and X, and path fixes for attachments, social metadata, and RSS were implemented.
- **2026-08-10 12:13**: Validation passed: 10 Node tests, an Astro build of 18 pages, HTTP 200 responses for articles and assets, official validation of all six skills, and a synchronization check between harnesses.
- **2026-08-10 12:29**: The exact CI cycle (`npm ci`, apply the sitemap patch, run tests, and build) was verified. CommonMark and transactional coverage were strengthened.
- **2026-08-10 12:42**: LinkedIn and X skills were refined. Each post must use a brief, natural invitation, an academic-professional tone, one required image, and the exact article link in its body.
- **2026-08-10 12:48**: `AGENTS.md` was updated to describe the three skills. A teaching mode that takes no action was added to the publication skill.
- **2026-08-16**: `functional-specs` and `technical-specs` were removed. The existing functional and technical contract retains their decisions and validation criteria.
- **2026-08-16**: The separate LinkedIn and X skills were merged into the global skill `pantagruel-research-social-announce`. The skill retains separate copy, preview, confirmation, publication, and verification for each network.

- **Preserved source material:**

The sections below retain reports, designs, decisions, questions, and evidence from the contribution history. They do not become binding requirements only because they appear here. Historical source below preserves the original requirements and evidence; pending execution is governed by this stage specification.

- **Technical design:**

- **Key decisions:**

1. `docs/` is the only versioned editorial source. Generate the Astro collection and served attachments before each build.
2. Pre must run `npm run build` followed by `npm run preview -- --host 127.0.0.1`. Do not deploy remotely or use a Git hook.
3. The publication skill must resolve the built slug, report the exact local URL, and protect the `develop`/`main` boundary.
4. Keep the existing production workflow limited to `main`. Run the same synchronization through the npm cycle.
5. The first delivery of this issue must implement Development → Pre → Pro. The second delivery must address LinkedIn and X through one global skill, based on the validated website cycle.

- **Architecture:**

```text
article/<issue-number>-<slug>
└── docs/YYYY-MM-DD-<slug>/
    ├── YYYY-MM-DD-<slug>.md
    └── attachments
             │ merge
             ▼
          develop ── sync → build → local preview → exact URL
             │
             │ approval + merge
             ▼
            main ── sync → build → GitHub Pages → online URL
```

`scripts/sync-articles.mjs` must validate canonical folders, generate `src/content/blog/` deterministically, and project attachments into `public/`. Repeating the command with the same input must produce the same tree. The skill must compare the article branch with `develop` and reject more than one canonical folder or unrelated changes. Errors must return a non-zero exit code so npm or GitHub Actions stops.

Resolve relative attachment references during projection without changing canonical Markdown. Use the CommonMark syntax tree and do not rewrite code examples. Prepare the projection in temporary trees, reject symbolic-link destinations, and replace generated trees with rollback. Social metadata and RSS must include the GitHub Pages `base` and use the same article path that Astro generates.

The skill `publish-pantagruel-article` must have two operational boundaries: preview from `develop`, and production from `main` after confirmation. It must not duplicate synchronization logic. It must call the script, build, and preview.

- **Restrictions:**

- **Article branch**: Each article branch must contain exactly one article and its attachments.
- **Production branch**: `develop` must never deploy to the Internet. `main` is the only production branch.
- **Hosting and services**: Do not add pre hosting, additional states, or new services.
- **Approval**: Obtain explicit approval before merging to `main` after the pre review.
- **External publication**: Obtain a separate final confirmation for external publications. Do not trigger them as a side effect of deployment.
- **Compatibility**: Keep existing URLs, articles, and unrelated changes.
- **Instructions**: Keep instructions short, imperative, and self-contained. Separate development, local pre, production, and external distribution. Do not duplicate this issue contract in `AGENTS.md`.

- **Guide:**

- **Surfaces**: Node/Astro code, npm configuration, editorial workflow, project context, and local skills.
- **Coding guidelines**: Use a minimal, explicit implementation that follows repository JavaScript/Astro conventions.
- **Governing skill**: Use `coding-contract-guidelines` for `AGENTS.md` and the skills.
- **Target paths**: `AGENTS.md`, `scripts/`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `.gitignore`, `.github/workflows/deploy.yml`, `src/components/BaseHead.astro`, `src/pages/rss.xml.js`, `.agents/skills/`, `.claude/skills/`, and `tests/`.
- **Purpose and outcomes**: Write each article once. Review it as a local website. Publish it online only after approval.
- **Scope and exclusions**: Include the editorial cycle, its automation, and distribution skills. Exclude a remote pre environment and actual publication of an article or announcement during implementation.
- **Sources**: User decisions from 2026-08-10 and the current structure of `docs/`, Astro, and GitHub Pages.
- **Objective and scope**: Generate the Astro collection from `docs/`. Serve it locally from `develop`. Reuse the same generation in the `main` build.
- **Target paths**: `scripts/sync-articles.mjs`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `.gitignore`, `.github/workflows/deploy.yml`, `src/components/BaseHead.astro`, `src/pages/rss.xml.js`, `.agents/skills/publish-pantagruel-article/`, its Claude mirror, and `tests/article-publication/`.
- **Stack and dependencies**: Use Node.js 20, Astro 4, standard Node APIs, `unified`/`remark-parse` to interpret CommonMark, and existing GitHub Actions. Do not add services or runtime dependencies.
- **Coding guidelines**: Use a minimal, explicit implementation that follows existing JavaScript/Astro conventions.
- **Accepted requirements**: One branch per article, one canonical Markdown file, local preview only, and production only from `main`.
- **Type**: `external`.
- **Format**: `markdown`.
- **Target path**: `AGENTS.md`, `.agents/skills/publish-pantagruel-article/SKILL.md`, `.claude/skills/publish-pantagruel-article/SKILL.md`, and `~/.codex/skills/pantagruel-research-social-announce/SKILL.md`.

- **Table of contents:**

- **Project context**: Record the durable “one branch, one article” decision and the relationship between `develop` and `main`.
- **Publication**: Include article preparation, local preview, approval, production, and verification.
- **Distribution**: Include subsequent limits and dependencies for LinkedIn and X.

- **Specifications:**

- **Build and preview**: The build, local preview, tests, and `git diff --check` must pass. Record the results.
- **Pre and production isolation**: Run a trial to show that a canonical article appears in pre without changing production. Verify that the same content is ready for the `main` build.
- **Skill structure**: Modified or new skills must pass structural validation. Record the results.
- **Article branch flow**: A branch with one article must be able to merge into `develop`. Its exact local URL must show the article without changing production.
- **Canonical source**: `docs/` must contain the only editorial Markdown. Astro copies must be derived and reproducible.
- **Content identity**: The content approved in pre must be the content that `main` builds and publishes.
- **Invalid input handling**: The flow must block branches with more than one article, attachment collisions, and differences between the canonical source and its projection.
- **Separate distribution**: Keep LinkedIn and X separate from website publication. In one global skill, keep copy, execution, confirmation, and verification independent for each network.
- **Announcement content**: Each announcement must include the exact article link in its body and one relevant image. Keep the text short and natural, with an academic-professional tone. Avoid stereotyped or synthetic formulas.
- **Teaching mode**: An explanation request must activate the publication skill's teaching mode. Describe development, local pre, review, production, and distribution without executing transitions. Do not treat an explanation request as authorization.
- **Node tests**: Test discovery, names, reproducible copying, collisions, and rejection of invalid structures.
- **Branch diff**: Test the article branch diff against `develop`. Accept one canonical folder and reject unrelated changes.
- **Full corpus**: Build the complete existing corpus and compare the generated paths.
- **HTTP response**: Verify an HTTP 200 response for the expected article in local preview.
- **Skill synchronization**: Validate skill structure and check synchronization between `.agents/skills/` and `.claude/skills/`.
- **Production workflow**: Confirm that `.github/workflows/deploy.yml` deploys only `main`.
- **Recorded checks**: Identify checks that passed, failed, and are pending.

- **Acceptance criteria and testing:**

- **Functional:**

- **End-to-end publication**: Implement and verify the article branch → `develop` and local preview → `main` and production path.
- **Single editorial source**: Keep `docs/` as the only editorial source. Generate the surfaces that Astro needs to build from it.
- **Local article URL**: Report the exact local article URL during pre. Verify the online URL after production.
- **Social distribution delivery**: In a second delivery of this issue, prepare combined automation to announce verified articles on LinkedIn and X. First validate the website cycle. Keep execution and confirmation independent for each network.
- **Article branch setup**: Give each article its own documentary contribution issue. Create its branch as `article/<issue-number>-<slug>` from `develop`. The branch must add only `docs/YYYY-MM-DD-<slug>/`, with a Markdown file of the same name and its attachments. Merge into `develop` when writing is complete.
- **Local preview cycle**: From `develop`, generate Astro content from `docs/`, build the site, start local preview, and report the exact article URL. Make requested changes in the same article branch. Merge again and repeat the preview.
- **Production and distribution**: After explicit approval, merge `develop` into `main`. The GitHub Pages workflow publishes the site. Verify the online URL. Only then may separate LinkedIn and X announcements be prepared or published.
- **Failure handling**: Stop the flow on any validation, build, preview, deployment, or verification failure. Report the failure. Do not claim that the stage is complete.



- **Registro de desarrollo:** migración del contrato y asociación explícita del script de issue; validación actual superada en las cuatro celdas: 2 artículos sincronizados, carpeta inválida rechazada (exit 1), build correcto, páginas/feed HTTP 200 y ruta inexistente HTTP 404. Los resultados de agosto siguen siendo históricos.

### Etapa 2 — Publicación y anuncios

- **GATE:** aprobación explícita antes de merge a main, despliegue y cada anuncio externo.
- **Detalles y especificaciones:** conservar el flujo editorial y las autorizaciones registradas arriba; no ejecutar esta etapa como efecto de la homologación.
- **Registro de desarrollo:** sin nueva publicación.

---
## Results and reporting (delta_time: 04/11/2026 14:10)

Contrato histórico de automatización editorial homologado; los requisitos y reportes anteriores se conservan. El script de issue valida mecanismos locales reales reutilizando el global; cuatro celdas superadas el 04/11/2026 sobre el código local. Ningún despliegue ni anuncio se realizó.
