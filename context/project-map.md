# Project Map

```text
Repositorios
├── Upstream: pantagruel-alpha/pantagruel-research
│   └── develop                         [no consultado: solo se opera contra downstream]
└── Downstream: aprendesc/pantagruel-research
    ├── develop                         [A: rama de trabajo · HEAD local = downstream/develop]
    └── (sin rama de issue activa)      [B: no aplicable]
```

Evidencia de ejecución: 3/11/2026, macOS, Node 25.8.1, Astro 4, sin red ni despliegue.

## Contexto

Pantagruel Research es el espacio editorial y el blog técnico de Pantagruel Alpha: artículos sobre finanzas cuantitativas, trading, aprendizaje automático y ciencia de datos. El autor escribe cada artículo como una carpeta de Markdown con sus imágenes; esa carpeta es la fuente de verdad. A partir de ella, una pequeña aplicación Astro genera el sitio web.

Se parece a una imprenta con dos pasos. Primero, el **sincronizador** copia cada artículo a la sala de composición (colección de contenido y activos públicos) y corrige los enlaces a sus imágenes. Después, **Astro** compone las páginas: portada, listado del blog, una página por artículo, el feed RSS y el mapa del sitio. Lo compuesto no es fuente: se puede borrar y regenerar. Publicar en Internet, en cambio, no es automático: pasa por una revisión y un despliegue que esta máquina no ejecuta.

Hoy el corpus contiene dos artículos (una bienvenida y un artículo de prueba sobre el perceptrón de Rosenblatt). No hay producción ni publicación activada, ni una issue abierta que defina el siguiente paso editorial.

---

## Diff

Downstream `aprendesc/pantagruel-research` · `develop` → rama de issue: **no aplicable**.

No hay issue ni PR abiertas en el repositorio downstream y la tarea editorial vigente no tiene issue ni rama, así que no se inventa una comparación. Cuando exista una rama de issue, el delta comparará downstream `develop` contra ella.

## Mapa global

Los **entrypoints existentes** se muestran completos. Cada fila es un comando independiente.

```text
LVL LOW · IMPLEMENTADO (filas 1–3 verificadas por ejecución el 3/11/2026; filas 4–5 no ejecutadas)
Script: npm run <sync:articles|build|preview|dev|test> · node scripts/sync-articles.mjs [--root]
Pruebas: context/tests/article_publication_site_functional_test.py
Configuración por componente
├── scripts/sync-articles.mjs · syncArticles
│   └── --root = directorio raíz (por defecto, el directorio actual) · ARTICLE_DIRECTORY = YYYY-MM-DD-<slug>
├── astro.config.mjs
│   ├── site = https://pantagruel-alpha.github.io
│   ├── base = /pantagruel-research
│   └── integrations = [mdx, sitemap, tailwind]
├── src/content/config.ts · blogSchema
│   └── title, description, pubDate (obligatorios) · heroImage, badge, tags, updatedDate (opcionales)
└── src/config.ts
    └── GENERATE_SLUG_FROM_TITLE = true

1 Sincronizar artículos · npm run sync:articles
+--------------------+     +-------------------------+     +----------------------------+
| (1) Leer carpetas  | --> | (2) Proyectar enlaces   | --> | (3) Reemplazar derivados   |
|   docs/YYYY-…-slug |     |   de adjuntos           |     |   de forma atómica         |
+--------------------+     +-------------------------+     +----------------------------+

1 <- disco: docs/<carpeta>/*.md y adjuntos
3 -> disco: src/content/blog/<slug>.md, public/articles/<slug>/*

2 Construir el sitio · npm run build
+--------------------+     +--------------------+     +-------------------------+
| (1) prebuild:      | --> | (2) Componer       | --> | (3) Escribir dist/      |
|   sincronizar      |     |   páginas, RSS     |     |   y sitemap             |
+--------------------+     |   y mapa del sitio |     +-------------------------+
                           +--------------------+

1 <- disco: docs/
2 <- disco: src/content/blog, src/pages, src/layouts, public/
3 -> disco: dist/

3 Servir el sitio construido · npm run preview
+--------------------+     +------------------------+
| (1) Leer dist/     | --> | (2) Responder HTTP     |
|                    |     |   bajo /pantagruel-    |
+--------------------+     |   research             |
                           +------------------------+

1 <- disco: dist/
2 <- red: GET /pantagruel-research/, /blog/<slug>/, /rss.xml

4 Servidor de desarrollo · npm run dev | start  (no ejecutado)
+---------------------+     +--------------------+
| (1) Observar fuentes| --> | (2) Recargar en    |
|   src/ y public/    |     |   caliente         |
+---------------------+     +--------------------+

1 <- disco: src/, public/, src/content/blog
2 <- red: navegador local

5 Publicación y release  (no ejecutada: BLOQUEADO / PENDIENTE)
+-------------------+     +--------------------+     +----------------------+     +---------------------+
| (1) Contrato      | --> | (2) CI: tests,     | --> | (3) Preparar         | --> | (4) Despliegue en   |
|   de publicación  |     |   build y artefacto|     |   upstream/release   |     |   GitHub Pages      |
+-------------------+     +--------------------+     +----------------------+     +---------------------+

2 <- red: GitHub Actions (en downstream los jobs quality/deploy/release están desactivados; policy activo)
3 -> disco: rama de publicación local (scripts/promote-to-upstream, .github/personal-ci/prepare-*.py)
4 -> red: GitHub Pages (upstream, tras revisión)
```

Entrypoints cubiertos por esta tabla: `npm run sync:articles|prebuild|build|preview|dev|start|test|astro|postinstall`, `node scripts/sync-articles.mjs`, `scripts/promote-to-upstream`, `.github/personal-ci/{gate,local-guard,install-hooks,prepare-release,prepare-upstream}.py` y `.github/workflows/ci.yml`. Los procedimientos editoriales `.agents/skills/publish-pantagruel-article` y `pantagruel-research-social-announce` son guías de agente, no ejecutables: la segunda publica en redes externas y queda bloqueada sin autorización expresa. `npm test` ejecuta las pruebas clásicas de `tests/article-publication/` (contrato de proyección y del workflow); no sustituyen a las pruebas funcionales.

Las líneas bajo cada diagrama usan el número de la caja: `n ->` es una salida y `n <-` una entrada; `disco` y `red` identifican el intercambio.

## Mecánicas principales

La sincronización alimenta la construcción y la construcción alimenta el servicio. La prueba funcional recorre las filas 1–3 con los dos artículos reales y con un artículo de prueba en un directorio temporal.

### 1. Sincronización de artículos · `syncArticles`

Lee cada carpeta `YYYY-MM-DD-<slug>` de `docs/`, valida su nombre y su cadena de directorios, y reescribe los enlaces a adjuntos locales (`./figura.png`) hacia `../../articles/<slug>/figura.png` sin tocar enlaces externos ni anclas. Prepara las proyecciones y las coloca de una vez, de modo que un error no deja el sitio a medias: una carpeta inválida termina con código 1 y no escribe nada. Ejecutarla dos veces da el mismo resultado.

```text
LVL LOW · IMPLEMENTADO
Entrada: syncArticles (scripts/sync-articles.mjs) · npm run sync:articles · --root <dir>
Prueba: context/tests/article_publication_site_functional_test.py [0] y [1]
Configuración
└── syncArticles
    ├── rootDirectory = process.cwd() | --root
    └── ARTICLE_DIRECTORY = ^\d{4}-\d{2}-\d{2}-<slug>$

+-------------------+     +------------------------+     +---------------------+     +-------------------------+
| (1) Listar        | --> | (2) Validar nombre y   | --> | (3) Proyectar       | --> | (4) Reemplazar          |
|   docs/           |     |   cadena de directorio |     |   enlaces adjuntos  |     |   src/content/blog y    |
+-------------------+     +------------------------+     +---------------------+     |   public/articles       |
                                                                                      +-------------------------+

1 <- disco: docs/<carpeta>/
2 <- disco: metadatos de archivos y directorios
4 -> disco: src/content/blog/<slug>.md, public/articles/<slug>/<adjuntos>
```

---

### 2. Construcción del sitio · `npm run build`

`prebuild` sincroniza; después Astro valida el frontmatter contra `blogSchema` y genera `dist/`: portada, listado y paginación del blog, una página por artículo, etiquetas, tienda, `rss.xml`, `sitemap-index.xml` y `404.html`, todo bajo la base `/pantagruel-research`. El nombre de cada página se deriva del **título** (`GENERATE_SLUG_FROM_TITLE = true`), con las letras acentuadas eliminadas: el artículo del perceptrón se publica como `el-perceptrn-de-rosenblatt-…`, no como su carpeta. Es una observación, no una corrección.

```text
LVL LOW · IMPLEMENTADO
Entrada: npm run build (prebuild → astro build)
Prueba: context/tests/article_publication_site_functional_test.py [2]
Configuración
├── astro.config.mjs
│   ├── site = https://pantagruel-alpha.github.io
│   └── base = /pantagruel-research
└── src/content/config.ts · blogSchema
    └── title · description · pubDate · tags (únicas)

+-------------------+     +------------------------+     +-------------------------+
| (1) Sincronizar   | --> | (2) Validar contenido  | --> | (3) Generar páginas,    |
|   artículos       |     |   con blogSchema       |     |   RSS, sitemap y 404    |
+-------------------+     +------------------------+     +-------------------------+

1 <- disco: docs/
2 <- disco: src/content/blog/*.md
3 -> disco: dist/index.html, dist/blog/<slug-del-título>/index.html, dist/rss.xml, dist/sitemap-*.xml, dist/404.html, dist/articles/<slug>/*
```

---

### 3. Servicio del sitio construido · `npm run preview`

Sirve `dist/` bajo la base configurada. La prueba lee la portada, cada artículo (200), el feed RSS (200) y comprueba que una ruta inexistente responde 404.

```text
LVL LOW · IMPLEMENTADO
Entrada: npm run preview -- --host 127.0.0.1 --port <puerto>
Prueba: context/tests/article_publication_site_functional_test.py [3]
Configuración
└── astro preview
    ├── --host = 127.0.0.1
    └── --port = 43999 (prueba)

+-------------------+     +-------------------------+     +-------------------------+
| (1) Servir dist/  | --> | (2) Responder páginas   | --> | (3) 404 para rutas      |
|   bajo la base    |     |   y feed                |     |   inexistentes          |
+-------------------+     +-------------------------+     +-------------------------+

1 <- disco: dist/
2 <- red: GET /pantagruel-research/, /blog/<slug>/, /rss.xml
3 <- red: GET /pantagruel-research/blog/no-such-article/
```

---

### 4. Publicación y release (bloqueada)

Fuera de esta máquina: la CI de GitHub (en el downstream solo está activo el chequeo de política), la preparación de una rama pública sin historia privada (`scripts/promote-to-upstream`, `prepare-upstream.py`, `prepare-release.py`) y el despliegue en GitHub Pages desde `main` tras revisión. No se ejecutan sin una orden explícita y un flujo revisado, y no se simulan. Tampoco se ejecuta el anuncio en redes sociales.

```text
LVL LOW · IMPLEMENTADO COMO CONFIGURACIÓN (no ejecutado: BLOQUEADO / PENDIENTE)
Entrada: .github/workflows/ci.yml · scripts/promote-to-upstream · .github/personal-ci/prepare-release.py
Prueba: ninguna (requiere GitHub y revisión humana)

+-------------------+     +---------------------+     +----------------------+     +--------------------+
| (1) Preparar rama | --> | (2) Revisar y pasar | --> | (3) CI: tests, build | --> | (4) Pages          |
|   limpia          |     |   política          |     |   y artefacto        |     |   (upstream)       |
+-------------------+     +---------------------+     +----------------------+     +--------------------+

1 -> disco: rama de publicación local
3 <- red: GitHub Actions
4 -> red: GitHub Pages
```

---

## Storage

Estructura verificada en el repositorio y tras la ejecución del 3/11/2026. Solo se gestiona disco local; no hay almacenamiento en Databricks.

```text
Storage
└── Local · repositorio/
    ├── docs/                                       Fuente editorial (versionada).
    │   └── YYYY-MM-DD-<slug>/
    │       ├── YYYY-MM-DD-<slug>.md                Artículo con frontmatter.
    │       └── post_img.webp (y otros adjuntos)    Imágenes del artículo.
    ├── src/                                        Aplicación Astro (versionada).
    │   ├── pages/ · layouts/ · components/ · lib/  Rutas, plantillas y utilidades.
    │   ├── content/config.ts                       Esquema de contenido.
    │   └── content/blog/<slug>.md                  Proyección derivada (git-ignorada).
    ├── public/                                     Activos estáticos (versionados).
    │   └── articles/<slug>/*                       Adjuntos proyectados (git-ignorados).
    ├── dist/                                       Sitio construido (git-ignorado).
    ├── scripts/ · .github/ · .agents/skills/       Sincronizador, CI y guías editoriales.
    ├── tests/article-publication/                  Pruebas clásicas del contrato de publicación.
    ├── context/                                    issues/, sessions/, tests/ y este mapa.
    └── node_modules/ · .astro/                     Dependencias y caché (git-ignoradas).
```

`syncArticles` lee `docs/` y escribe `src/content/blog/` y `public/articles/`; `astro build` lee esas rutas y escribe `dist/`.
