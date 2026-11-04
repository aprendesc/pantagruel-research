# feature/1-automate-pantagruel-research-publication · [Issue #1](https://github.com/aprendesc/pantagruel-research/issues/1) · PR pendiente

## Context (delta_time: 04/11/2026 16:51)

### Descripción

Automatiza el ciclo editorial de Pantagruel Research con Node/Astro: un Markdown canónico por artículo, proyección reproducible del sitio y revisión local antes de publicar. Las entregas de agosto de 2026 implementaron sincronización, adjuntos, preview y herramientas de publicación; LinkedIn y X mantienen confirmaciones independientes. La validación local registrada el 04/11/2026 no acredita despliegue ni anuncios. La presente migración reorganiza el contrato sin reabrir su ejecución.

El responsable histórico es `aprendesc`. El registro antiguo indicaba Backlog, hito `001 — Publicación editorial` y etiqueta `skill:documental-contribution`; esos datos son trazabilidad histórica, no estado actual de GitHub ni metodología vigente. El entregable es código y herramientas, aunque opere sobre artículos.

### Specialized skills

- [publish-pantagruel-article](../../../.agents/skills/publish-pantagruel-article/SKILL.md): revisión local y publicación editorial con sus autorizaciones.
- [pantagruel-research-social-announce](../../../.agents/skills/pantagruel-research-social-announce/SKILL.md): anuncios independientes por red.

---
## Diff (delta_time: 04/11/2026 14:10)

```text
Comparación histórica pendiente: no hay rama de tarea local conservada; develop no equivale al diff de la contribución.
```

---
## Test Profiling (delta_time: 04/11/2026 16:51)

**Evidencia conservada:** resultados registrados el 04/11/2026 a las 14:10. Esta migración de formato no vuelve a ejecutar las celdas.

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
## Persistence (delta_time: 04/11/2026 16:51)

```text
Local · raíz del repositorio
├── context/issues/1-automate-pantagruel-research-publication/
│   ├── 1-automate-pantagruel-research-publication.md  contrato coding
│   ├── migration-source.md                          original exacto anterior a esta migración
│   └── article_publication_functional_test.py        celdas [0]–[3] de issue
├── context/tests/article_publication_site_functional_test.py  validador global reutilizado
├── docs/YYYY-MM-DD-<slug>/                          fuente editorial versionada; patrón
│   ├── YYYY-MM-DD-<slug>.md                         Markdown canónico
│   └── attachments                                 recursos del artículo; nombres variables
├── src/content/blog/                               proyección generada
├── public/articles/                                recursos generados
└── dist/                                           build local derivado
GitHub Pages · publicación externa; no ejecutada por esta migración
```

---
## Execution plan (delta_time: 04/11/2026 16:51)

### Secuencia de ejecución

Se conserva la secuencia y los estados del contrato previo. La autonomía HIGH allí declarada correspondía a su migración anterior; esta reorganización del contrato no autoriza ejecución, publicación ni anuncios.

1. [OK] **Etapa 1 — Revalidar el ciclo local:** sincronización, adjuntos, build y lectura HTTP mediante las celdas 0–3; resultado registrado el 04/11/2026 a las 14:10.
2. [GATE] **Etapa 2 — Publicación y anuncios:** decisión humana antes de merge a `main`, despliegue y cada anuncio externo.

### Etapa 1 — Revalidar el ciclo local

- **Detalles y especificaciones:** requisitos de implementación conservados como historia de la contribución; el estado [OK] corresponde a las cuatro celdas locales, no a la publicación externa.

#### Fuente, arquitectura y límites acordados

`docs/` es la única fuente editorial versionada. Cada rama `article/<issue-number>-<slug>` contiene un artículo y adjuntos, parte de `develop` y se integra en `develop` para revisión local. La primera entrega debe implementar Development → Pre → Pro; la segunda, la distribución por LinkedIn y X mediante una única skill global, basada en el ciclo web validado.

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

Pre debe ejecutar `npm run build` seguido de `npm run preview -- --host 127.0.0.1`, resolver el slug compilado y comunicar su URL exacta. No debe desplegar remotamente ni usar un Git hook. La sincronización pertenece al ciclo npm y se reutiliza en el build de `main`.

- **Article branch**: Each article branch must contain exactly one article and its attachments.
- **Hosting and services**: Do not add pre hosting, additional states, or new services.
- **Compatibility**: Keep existing URLs, articles, and unrelated changes.
- **Instructions**: Keep instructions short, imperative, and self-contained. Separate development, local pre, production, and external distribution. Do not duplicate this issue contract in `AGENTS.md`.

#### Superficies y construcción

- **Ámbito:** código Node/Astro, configuración npm, flujo editorial, contexto y skills de publicación. Excluye un entorno pre remoto y publicar artículos o anuncios durante la implementación.
- **Stack acordado:** Node.js 20, Astro 4, APIs estándar de Node, `unified`/`remark-parse` para CommonMark y GitHub Actions existente; sin servicios ni dependencias de runtime nuevos.
- **Estilo:** implementación mínima y explícita, siguiendo las convenciones JavaScript/Astro del repositorio.
- **Rutas históricas:** `AGENTS.md`, `scripts/sync-articles.mjs`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `.gitignore`, `.github/workflows/deploy.yml`, `src/components/BaseHead.astro`, `src/pages/rss.xml.js`, `.agents/skills/`, `.claude/skills/` y `tests/article-publication/`. Son superficies registradas, no permiso para editarlas en esta migración.
- **Documentación de entrega:** Markdown externo en `AGENTS.md` y las skills locales de publicación, su espejo Claude y la skill global de anuncios. Debe explicar contexto estable de un artículo por rama, desarrollo, pre local, aprobación, producción y verificación, y finalmente distribución. No duplicar el contrato en `AGENTS.md`.
- **Fuentes del acuerdo:** decisiones del usuario del 10/08/2026 y estructura del corpus, Astro y GitHub Pages.

#### Validación y aceptación local conservadas

- **Build and preview**: The build, local preview, tests, and `git diff --check` must pass. Record the results.
- **Pre and production isolation**: Run a trial to show that a canonical article appears in pre without changing production. Verify that the same content is ready for the `main` build.
- **Skill structure**: Modified or new skills must pass structural validation. Record the results.
- **Article branch flow**: A branch with one article must be able to merge into `develop`. Its exact local URL must show the article without changing production.
- **Canonical source**: `docs/` must contain the only editorial Markdown. Astro copies must be derived and reproducible.
- **Invalid input handling**: The flow must block branches with more than one article, attachment collisions, and differences between the canonical source and its projection.
- **Teaching mode**: An explanation request must activate the publication skill's teaching mode. Describe development, local pre, review, production, and distribution without executing transitions. Do not treat an explanation request as authorization.
- **Node tests**: Test discovery, names, reproducible copying, collisions, and rejection of invalid structures.
- **Branch diff**: Test the article branch diff against `develop`. Accept one canonical folder and reject unrelated changes.
- **Full corpus**: Build the complete existing corpus and compare the generated paths.
- **HTTP response**: Verify an HTTP 200 response for the expected article in local preview.
- **Skill synchronization**: Validate skill structure and check synchronization between `.agents/skills/` and `.claude/skills/`.
- **Recorded checks**: Identify checks that passed, failed, and are pending.

- **Single editorial source**: Keep `docs/` as the only editorial source. Generate the surfaces that Astro needs to build from it.
- **Local article URL**: Report the exact local article URL during pre. Verify the online URL after production.
- **Article branch setup**: Give each article its own documentary contribution issue. Create its branch as `article/<issue-number>-<slug>` from `develop`. The branch must add only `docs/YYYY-MM-DD-<slug>/`, with a Markdown file of the same name and its attachments. Merge into `develop` when writing is complete.
- **Local preview cycle**: From `develop`, generate Astro content from `docs/`, build the site, start local preview, and report the exact article URL. Make requested changes in the same article branch. Merge again and repeat the preview.
- **Failure handling**: Stop the flow on any validation, build, preview, deployment, or verification failure. Report the failure. Do not claim that the stage is complete.

- **Vinculación con el script de issue:** `[0]` sincroniza el corpus; `[1]` comprueba adjuntos y rechazo de entrada inválida; `[2]` construye el sitio; `[3]` sirve y lee las rutas HTTP. Reutilizan las celdas reales del validador global, sin simulación ni publicación. Otros criterios históricos no quedan automáticamente cubiertos por estas cuatro celdas.

#### Registro de desarrollo

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

- **04/11/2026 14:10 · migración anterior:** asociación explícita del script de issue y ejecución local registrada: 2 artículos sincronizados, carpeta inválida rechazada (exit 1), build correcto, páginas/feed HTTP 200 y ruta inexistente HTTP 404. Los resultados de agosto siguen siendo históricos.
- **04/11/2026 16:51 · reclasificación actual:** original exacto conservado en `migration-source.md`; requisitos redistribuidos por su función. Sin nueva implementación ni ejecución.

### Etapa 2 — Publicación y anuncios

- **GATE:** aprobación explícita antes de merge a `main`, despliegue y cada anuncio externo. El gate sigue pendiente; ningún registro local lo resuelve.
- **Detalles y especificaciones:** conservar el flujo acordado de producción y distribución, condicionado al ciclo local validado.

- **Production branch**: `develop` must never deploy to the Internet. `main` is the only production branch.
- **Approval**: Obtain explicit approval before merging to `main` after the pre review.
- **External publication**: Obtain a separate final confirmation for external publications. Do not trigger them as a side effect of deployment.

- **Content identity**: The content approved in pre must be the content that `main` builds and publishes.
- **Separate distribution**: Keep LinkedIn and X separate from website publication. In one global skill, keep copy, execution, confirmation, and verification independent for each network.
- **Announcement content**: Each announcement must include the exact article link in its body and one relevant image. Keep the text short and natural, with an academic-professional tone. Avoid stereotyped or synthetic formulas.
- **Production workflow**: Confirm that `.github/workflows/deploy.yml` deploys only `main`.

- **End-to-end publication**: Implement and verify the article branch → `develop` and local preview → `main` and production path.
- **Social distribution delivery**: In a second delivery of this issue, prepare combined automation to announce verified articles on LinkedIn and X. First validate the website cycle. Keep execution and confirmation independent for each network.
- **Production and distribution**: After explicit approval, merge `develop` into `main`. The GitHub Pages workflow publishes the site. Verify the online URL. Only then may separate LinkedIn and X announcements be prepared or published.

- **Registro de desarrollo:** sin nueva publicación. Los comandos `npm run build` y `astro preview` constaban verificados localmente en `http://127.0.0.1:4321/pantagruel-research/`; esa dirección histórica no demuestra un servicio activo ahora. La configuración histórica de producción limitada a `main` no constituye evidencia de un despliegue realizado.

---
## Results and reporting (delta_time: 04/11/2026 16:51)

El código de automatización editorial y sus requisitos quedan organizados como contrato coding. Se conservan las cuatro celdas superadas el 04/11/2026 a las 14:10 y la evidencia de agosto. Esta reclasificación no ejecutó pruebas, despliegues ni anuncios.

- **Limitación:** la validación local no acredita producción ni distribución social; el gate de la etapa 2 sigue pendiente.
- **Trazabilidad:** el original exacto previo a esta transformación se conserva en [migration-source.md](migration-source.md). La antigua etiqueta documental describe su procedencia, mientras que el tipo actual sigue el código implementado.
