## Contract

### Context

El contrato declara las skills documental-contribution. La contribución figura en estado Backlog. La responsabilidad está asignada a aprendesc. La trazabilidad conserva las etiquetas skill:documental-contribution y el milestone 001 — Publicación editorial.

Pantagruel Research necesita un ciclo editorial reproducible que mantenga un
único Markdown canónico por artículo, permita revisarlo localmente antes de
publicarlo y reserve la difusión en redes para después de verificar producción.

El flujo acordado es: rama exclusiva del artículo creada desde `develop`, merge
a `develop`, preview local, aprobación, merge de `develop` a `main` y despliegue
online mediante GitHub Pages. LinkedIn y X comparten una skill global con
copy y controles de publicación específicos por red.

La implementación corresponde a la rama
`feature/1-automate-pantagruel-research-publication`. El workflow actual ya
despliega `main`; `npm run build` y `astro preview` se han verificado localmente
en `http://127.0.0.1:4321/pantagruel-research/`.

#### Evidencia y decisiones consolidadas

2026-08-10 11:46 — Issue reactivado y refinado con el ciclo acordado de rama de artículo, pre local en `develop` y producción en `main`.

2026-08-10 11:46 — Corregida la ruta contractual a `context/issues/1-automate-pantagruel-research-publication.md`, adoptado el wrapper de Development Methodology y registrada la rama `feature/1-automate-pantagruel-research-publication`.

2026-08-10 11:52 — Auditoría metodológica aplicada: añadido `Labels`, completados parámetros técnicos y documentales, y alineada la regla de artículos con la trazabilidad `article/<issue-number>-<slug>`.

2026-08-10 12:08 — Implementados sincronización reproducible, preview local, protección de producción, skills independientes para publicación, LinkedIn y X, y correcciones de rutas para adjuntos, metadatos sociales y RSS.

2026-08-10 12:13 — Validación completada con 10 pruebas Node, build Astro de 18 páginas, respuestas HTTP 200 en artículos y activos, validación oficial de las seis skills y comprobación de sincronía entre harnesses.

2026-08-10 12:29 — Verificado el ciclo exacto de CI (`npm ci`, aplicación del parche de sitemap, pruebas y build) y reforzada la cobertura CommonMark y transaccional.

2026-08-10 12:42 — Refinadas las skills de LinkedIn y X: invitación breve y natural, tono académico-profesional, una imagen obligatoria y enlace exacto al artículo dentro del cuerpo de ambas publicaciones.

2026-08-10 12:48 — Reflejado en `AGENTS.md` el cometido de las tres skills y añadido a la skill de publicación un modo explicativo didáctico que no ejecuta acciones.

2026-08-16 — Retiradas `functional-specs` y `technical-specs`; el contrato funcional y técnico existente conserva sus decisiones y criterios de validación.

2026-08-16 — Fusionadas las skills separadas de LinkedIn y X en la skill global `pantagruel-research-social-announce`, conservando copy, previsualización, confirmación, publicación y verificación independientes por red.

#### Material contextual preservado

Los bloques siguientes conservan informes, diseños, decisiones, preguntas y evidencia de la evolución de la contribución sin resumir ni descartar su contenido. Su redacción original no los vuelve vinculantes por sí sola: la proyección activa se limita a `Restrictions`, la orientación no vinculante de `Guide` cuando exista y las condiciones de `Goals`.

#### Technical design

#### Key decisions

1. `docs/` será la única fuente editorial versionada. La colección Astro y los
   adjuntos servidos se generarán antes de cada build.
2. Pre usará `npm run build` seguido de
   `npm run preview -- --host 127.0.0.1`; no habrá deploy remoto ni git hook.
3. La skill de publicación resolverá el slug construido, comunicará la URL
   local exacta y protegerá las fronteras `develop`/`main`.
4. El workflow de producción existente seguirá limitado a `main` y ejecutará
   la misma sincronización mediante el ciclo npm.
5. La primera entrega del issue implementará Development → Pre → Pro. La
   segunda entrega abordará LinkedIn y X mediante una única skill global sobre
   esa base ya validada.

#### Architecture

```text
article/<issue-number>-<slug>
└── docs/YYYY-MM-DD-<slug>/
    ├── YYYY-MM-DD-<slug>.md
    └── adjuntos
             │ merge
             ▼
          develop ── sync → build → preview local → URL exacta
             │
             │ aprobación + merge
             ▼
            main ── sync → build → GitHub Pages → URL online
```

`scripts/sync-articles.mjs` validará las carpetas canónicas, generará de forma
determinista `src/content/blog/` y proyectará adjuntos en `public/`. La ejecución
repetida con la misma entrada producirá el mismo árbol. La skill comparará la
rama del artículo con `develop` y rechazará más de una carpeta canónica o
cambios ajenos. Los errores se propagarán con salida no cero para detener npm o
GitHub Actions.

Las referencias relativas a adjuntos se resolverán durante la proyección sin
alterar el Markdown canónico, mediante el árbol sintáctico CommonMark y sin
reescribir ejemplos de código. La proyección se preparará en árboles temporales,
rechazará destinos simbólicos y sustituirá los árboles generados con rollback.
Los metadatos sociales y RSS incorporarán el `base` de GitHub Pages y
utilizarán la misma ruta de artículo que Astro genera.

La skill `publish-pantagruel-article` tendrá dos fronteras operativas: preview
desde `develop` y producción desde `main` después de confirmación. No duplicará
la lógica de sincronización, sino que invocará el script, el build y la preview.

### Restrictions

Each article branch must contain exactly one article and its attachments.

`develop` must never deploy to the Internet. `main` is the only production branch.

Do not add pre hosting, additional states or new services.

Obtain explicit approval to merge to `main` after the pre review.

External publications require their own final confirmation. Do not trigger them as a side effect of deployment.

Keep existing URLs, articles and unrelated changes.

Keep instructions short, imperative and self-contained. Separate development, local pre, production and external distribution clearly. Do not duplicate the issue contract inside `AGENTS.md`.

### Guide

**Surfaces**: Node/Astro code, npm configuration, editorial workflow, project context and local skills.

**Coding guidelines**: Use a minimal, explicit implementation that follows the repository’s JavaScript/Astro conventions.

**Governing skills**: Use `documental-contribution` for `AGENTS.md` and the skills.

**Target paths**: `AGENTS.md`, `scripts/`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `.gitignore`, `.github/workflows/deploy.yml`, `src/components/BaseHead.astro`, `src/pages/rss.xml.js`, `.agents/skills/`, `.claude/skills/` and `tests/`.

**Purpose / outcomes**: Write each article once. Review it as a local website. Publish it online only after approval.

**Scope / exclusions**: Include the editorial cycle, its automation and distribution skills. Exclude a remote pre environment and actual publication of an article or announcement during implementation.

**Sources**: User decisions of 2026-08-10 and the current structure of `docs/`, Astro and GitHub Pages.

**Objective / scope**: Generate the Astro collection from `docs/`. Serve it locally from `develop`. Reuse the same generation in the `main` build.

**Target paths**: `scripts/sync-articles.mjs`, `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `.gitignore`, `.github/workflows/deploy.yml`, `src/components/BaseHead.astro`, `src/pages/rss.xml.js`, `.agents/skills/publish-pantagruel-article/`, its Claude mirror and `tests/article-publication/`.

**Stack / dependencies**: Use Node.js 20, Astro 4, standard Node APIs, `unified`/`remark-parse` to interpret CommonMark and existing GitHub Actions. Do not add services or runtime dependencies.

**Coding guidelines**: Use a minimal, explicit implementation that follows existing JavaScript/Astro conventions.

**Accepted requirements**: One branch per article, one canonical Markdown, local preview only and production only from `main`.

**Type**: external

**Format**: markdown

**Target path**: `AGENTS.md`, `.agents/skills/publish-pantagruel-article/SKILL.md`, `.claude/skills/publish-pantagruel-article/SKILL.md`, `~/.codex/skills/pantagruel-research-social-announce/SKILL.md`.

#### Table of contents

Project context: Record the durable “one branch, one article” decision and the relationship between `develop` and `main`.

Publication: Include article preparation, local preview, approval, production and verification.

Distribution: Include subsequent limits and dependencies for LinkedIn and X.

### Goals

#### Technical testing

The build, local preview, tests and `git diff --check` must pass.

Run a trial to show that a canonical article appears in pre without changing production. Verify that the same content is ready for the `main` build.

Modified or new skills must pass structural validation.

A branch with one article must be able to merge into `develop`. Its exact local URL must show the article without changing production.

`docs/` must contain the only editorial Markdown. Astro copies must be derived and reproducible.

The content approved in pre must be the content that `main` builds and publishes.

The flow must block branches with more than one article, attachment collisions and differences between the canonical source and its projection.

Keep LinkedIn and X separate from website publication. Within one global skill, keep copy, execution, confirmation and verification independent for each network.

Each announcement must include the exact article link in its body and one relevant image. Keep the text short, natural and academic-professional in tone. Avoid stereotyped or synthetic formulas.

An explanation request must activate the publication skill’s teaching mode. Describe development, local pre, review, production and distribution without executing transitions. Do not treat an explanation request as authorization.

Run Node tests for discovery, names, reproducible copying, collisions and rejection of invalid structures.

Test the article branch diff against `develop`. Accept one canonical folder and reject unrelated changes.

Build the complete existing corpus. Compare the generated paths.

Verify an HTTP 200 response for the expected article in local preview.

Validate skill structure. Check synchronization between `.agents/skills/` and `.claude/skills/`.

Confirm that `.github/workflows/deploy.yml` deploys only `main`.

#### Functional testing

Implement the article branch → `develop` and local preview → `main` and production path.

Keep `docs/` as the only editorial source. Generate the surfaces that Astro needs to build from it.

Report the exact local article URL during pre. Verify the online URL after production.

In a second delivery of the same issue, prepare combined automation to announce verified articles on LinkedIn and X. First validate the web cycle. Keep execution and confirmation independent for each network.

Each article must have its own documentary contribution issue. Create its branch as `article/<issue-number>-<slug>` from `develop`. The branch must add only `docs/YYYY-MM-DD-<slug>/`, with a Markdown of the same name and its attachments. Merge into `develop` when writing is complete.

From `develop`, the publication flow must generate Astro content from `docs/`, build the site, start local preview and report the exact article URL. Make requested changes in the same article branch. Merge again and repeat preview.

After explicit approval, merge `develop` into `main`. The GitHub Pages workflow publishes the site. Verify the online URL. Only then may independent LinkedIn and X announcements be prepared or published.

Stop the path on any validation, build, preview, deployment or verification failure. Report the failure without claiming that the stage is complete.
