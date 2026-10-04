---
name: publish-pantagruel-article
description: Prepare, preview, publish, republish, or verify one Pantagruel Research article through its article branch, local develop preview, explicit approval, and main deployment to GitHub Pages. Use when the user asks to preview a named article, make it live, check its production publication, or explain the publication workflow.
---

# Publicar un artículo de Pantagruel Research

## Explicar el flujo de forma didáctica

When the user asks how publication works, explain before taking action. Do not change branches, open merges, deploy, or publish anything. Adapt the detail to the user's knowledge. Present the workflow in this order:

1. **Desarrollo**: Each article has an issue, an `article/<issue-number>-<short-kebab-name>` branch created from `develop`, and one canonical `docs/YYYY-MM-DD-<slug>/` folder with its Markdown and attachments.
2. **Pre local**: After integrating the branch into `develop`, run tests and the build. Start the preview and provide its exact local URL. Explain that `develop` publishes nothing on the Internet.
3. **Revisión**: The user inspects the article. If corrections are requested, return to the same article branch, repeat integration, and generate a new preview. This invalidates any earlier approval.
4. **Producción**: Integrate `develop` into `main` only after explicit approval of the current preview. GitHub Pages deploys the article. Then verify the exact public URL.
5. **Difusión**: Explain LinkedIn and X as subsequent, optional, independent steps. Follow the global `$pantagruel-research-social-announce` skill and require final confirmation for each network.

Start with a simple summary, such as
`rama del artículo → develop/preview local → aprobación → main/producción`.
Define necessary Git terms. Show useful commands and URLs beside the applicable phase. End with the current state and the user's next decision. An explanation does not authorize execution of the workflow.

## Respetar las fronteras

- Treat `docs/YYYY-MM-DD-<slug>/` as the only editorial source. Do not manually edit or version its projections in `src/content/blog/` or `public/`.
- Require a separate `documental-contribution` issue for each article. Keep its 1:1 relationship with its `article/<issue-number>-<short-kebab-name>` branch, created from `develop` and limited to one article.
- Use `develop` only to build and serve a local preview. Do not deploy a preproduction environment or add services or states.
- Integrate `develop` into `main` only after the user explicitly approves the current preview. General permission to publish does not replace this later approval.
- Stop the workflow at any failure. Report it without claiming that the phase completed.
- Preserve unrelated changes and exclude them from commits, merges, and pushes.

## Preparar e integrar el artículo

1. Identify one specific, unambiguous article. Require the folder and Markdown to share `YYYY-MM-DD-<slug>`. Keep attachments in that folder.
2. Review the state and update remote references. Confirm 1:1 traceability between the issue, branch, and article.
3. Inspect `git diff --name-status downstream/develop...HEAD`. Require every path to belong to one canonical `docs/YYYY-MM-DD-<slug>/` folder. Reject additional article folders or unrelated changes.
4. Validate Markdown and attachments with the repository's current tests and commands. Do not manually reproduce the generator's logic.
5. Integrate the article branch into `develop` with the repository's usual mechanism. Do not publish `main`.

## Servir la preview local

1. Activate the updated `develop` branch. Install dependencies with `npm ci` when necessary.
2. Run the publication tests, `npm run build`, and `git diff --check`. The build must generate the Astro surfaces from `docs/` and leave the projection identical to the canonical source.
3. Resolve the article's actual built path in `dist/blog/<slug>/index.html`. Do not infer it only from the filename, because it can be derived from the title.
4. Start the preview from `develop`:

```bash
npm run preview -- --host 127.0.0.1
```

5. Check for a correct HTTP response and report the exact URL:

```text
http://127.0.0.1:4321/pantagruel-research/blog/<slug>/
```

6. Keep production intact. Request explicit approval of this preview before continuing.

## Corregir tras la preview

1. Return to the same `article/<issue-number>-<short-kebab-name>` branch and integrate the current `develop` into it.
2. Change only the canonical Markdown or its attachments in `docs/`.
3. Integrate the branch into `develop` again. Repeat the build, validations, preview, and report of the exact URL.
4. Treat every earlier approval as expired when the article changes. Request new approval for the new preview.

## Publicar en producción

1. Confirm that explicit approval applies to the content currently validated in `develop`. Record the approved commit.
2. Integrate `develop` into `main` without changing or omitting unrelated content from either branch. Push `main` only if all validations still pass.
3. Wait for the `Deploy to GitHub Pages` workflow associated with the `main` commit. Require successful completion.
4. Resolve and inspect the exact online URL for the same slug:

```text
https://pantagruel-alpha.github.io/pantagruel-research/blog/<slug>/
```

5. Verify a correct HTTP response and confirm that the page matches the approved article. Report commits, workflow result, and final URL.
6. If deployment or verification fails, diagnose and report the failure. Do not declare the article published.

## Mantener separada la difusión

- Do not prepare or publish LinkedIn or X posts as a side effect of this workflow.
- Use `$pantagruel-research-social-announce`. Require final confirmation for each network, always after verifying production.
