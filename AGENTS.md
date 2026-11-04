# Pantagruel Research

## Purpose and context

This repository is the editorial space and technical blog of Pantagruel Alpha. Its corpus covers quantitative finance, trading, Machine Learning and data science. An Astro application derives the published site from the article sources.

## Key definitions

- **Article corpus:** authored Markdown and attachments, independent of the rendered website.
- **Derived application:** the generated Astro collection and public assets.
- **Editorial contribution:** an article and its scoped issue; interface changes are software contributions.

## Repository overview

- [docs](docs/): article folders named `YYYY-MM-DD-<slug>` with their resources.
- [scripts/sync-articles.mjs](scripts/sync-articles.mjs): source-to-site conversion.
- [src](src/) and `public/articles/`: derived application surfaces.
- [package.json](package.json): development and validation commands.
- [.github/workflows/ci.yml](.github/workflows/ci.yml): actual CI and publication configuration.
- [Publication skill](.agents/skills/publish-pantagruel-article/SKILL.md) and [social announcements](.agents/skills/pantagruel-research-social-announce/SKILL.md): editorial delivery references.
- [Pantagruel V2](../pantagruel-v2/AGENTS.md): the separate trading application.

## Planning and stakeholders

[Planning panel](https://github.com/users/aprendesc/projects/13)

- `aprendesc`: editorial author and maintainer.
- Xavi: Pantagruel business collaborator and trader.

## Methodologies and references

[`development-methodology`](/Users/alejandroprendes/.codex/skills/development-methodology/SKILL.md).
For code issues, use [coding-contract-guidelines](/Users/alejandroprendes/.codex/skills/coding-contract-guidelines/SKILL.md) and [functional-testing-guidelines](/Users/alejandroprendes/.codex/skills/functional-testing-guidelines/SKILL.md). Keep the contract and issue validation script together in `context/issues/<issue>/`; each stable cell implements a registered validation mechanism tracked in Test Profiling. Global scenarios remain in `context/tests/`. Use [documental-contract-guidelines](/Users/alejandroprendes/.codex/skills/documental-contract-guidelines/SKILL.md) for documentary deliverables and [general-contract-guidelines](/Users/alejandroprendes/.codex/skills/general-contract-guidelines/SKILL.md) for organizational and review tasks. Documentary articles retain their authoring and publication rules. Classify by the actual deliverable, not by the presence of a validation script. Use the local publication and announcement skills. Write articles in Spanish unless another language is requested. Preserve evidence, readable analysis and the original article corpus.

Downstream: `aprendesc/pantagruel-research`; upstream: `pantagruel-alpha/pantagruel-research`. Ordinary development uses downstream `develop`; site publication follows the reviewed upstream release flow. Generated content is not the authoring source. A historical site URL does not prove the current release is deployed.

Local clone safeguards and configuration: [.githooks/CLONE.md](.githooks/CLONE.md).
