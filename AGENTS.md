# Context

## **Purpose**

Pantagruel Research is the editorial space and technical blog of Pantagruel Alpha.
It contains extensive work on quantitative finance, machine learning, and data science.
The product combines a maintainable editorial corpus with an Astro application published through GitHub Pages at
<https://pantagruel-alpha.github.io/pantagruel-research>.

## **Corpus and derived application**

[`docs/`](docs/) is the workshop and canonical source for articles.
Each article resides in `docs/YYYY-MM-DD-<slug>/`, with a Markdown file of the same name and its attachments.
[`scripts/sync-articles.mjs`](scripts/sync-articles.mjs) generates the [Astro](src/) application collection and isolated attachments under `public/articles/` from this corpus.
Both surfaces are derived.
Do not edit or version them manually.
Commands and dependencies reside in [`package.json`](package.json).

The [GitHub Pages workflow](.github/workflows/deploy.yml) runs the tests and deploys only `main`.

## **Editorial workflow and branches**

- **Downstream.** `downstream` is `aprendesc/pantagruel-research`, the development repository. Integrate ordinary work into `downstream/develop`.
- **Upstream.** `upstream` is `pantagruel-alpha/pantagruel-research`, the shared destination. Publish there only at the user's explicit request.

Apply the 1:1 editorial relationship: one issue, one branch, one article.
Define each article as its own documentary contribution.
Develop it from `develop` in `article/<issue-number>-<slug>`.
Use one canonical folder under `docs/`.
`develop` is the local preproduction surface, and `main` is the only branch for online publication.
After the local preview has been reviewed and approved, move to `main`.

## **Editorial criteria**

Unless another language is requested, prioritize rigorous, traceable, readable analysis in Spanish.
Treat article creation and curation as documentary contributions.
Treat changes to the blog interface and experience as frontend work.
Existing articles and their images are editorial corpus, not retroactive task contracts.

## **Planning and contracts**

The [Notion Panel](https://app.notion.com/p/5f9adc0336964ffe95abcf27631569d9) is the canonical inventory, with `Pantagruel Research` as the project for this product.
It is independent of entries classified as `Pantagruel`.
For this repository, do not consult those entries about backlog, active tasks, or equivalent concepts.
If the user explicitly requests a cross-project query, permit this exception.
This project's tasks are issues in `pantagruel-alpha/pantagruel-research`.
Their self-contained contracts reside in `context/issues/<issue-number>-<issue-title-kebab-case>.md`, with a 1:1 correspondence to issues in this repository.

This document preserves editorial direction, decisions, and project memory without duplicating the board.

## **Local skills**

The versioned local [publication](.agents/skills/publish-pantagruel-article/SKILL.md) skill explains and executes this sequence:
article branch → `develop` → local preview → approval → `main` → verification on GitHub Pages.
When the user asks how to publish, explain the process clearly and in order.
Clearly distinguish development, local preproduction, and production.
Show the applicable URLs.
If the user requested only an explanation, do not execute publication.

The local [social announcements](.agents/skills/pantagruel-research-social-announce/SKILL.md) skill prepares or publishes on LinkedIn, X, or both networks.
Verify production first.
Write short, natural invitations with an academic-professional tone.
Include the exact article link and one relevant image with alternative text in each announcement.
Obtain separate final confirmation for each network before each external publication.
