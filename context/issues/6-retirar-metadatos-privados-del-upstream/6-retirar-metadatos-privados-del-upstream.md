# Repair upstream publication metadata

## Execution plan

- [x] 1. Verify remote exposure and preserve integrated historical work.
- [ ] 2. Prepare and validate a minimal upstream main cleanup contribution.
- [ ] 3. Review publication and restore synchronized downstream standby.

## Context

Issue: https://github.com/aprendesc/pantagruel-research/issues/6 — aprendesc/pantagruel-research#6.
The user authorized removal of obsolete integrated branches and cleanup of personal upstream metadata. Downstream retains context and hooks; shared upstream excludes them and their ignore traces. Preserve application/article blobs, pending work and Git history. Standby is clean develop synchronized with downstream; downstream main must also synchronize.

### Applicable skills

- [development-methodology](/Users/alejandroprendes/.codex/skills/development-methodology/SKILL.md): lifecycle and publication boundaries.
- [standard-contribution-contract](/Users/alejandroprendes/.codex/skills/standard-contribution-contract/SKILL.md): this contract.
- [planning-mode](/Users/alejandroprendes/.codex/skills/planning-mode/SKILL.md): functional plan blocks.
- [decision-and-context-mode](/Users/alejandroprendes/.codex/skills/decision-and-context-mode/SKILL.md): publication scope.
- [functional-testing-guidelines](/Users/alejandroprendes/.codex/skills/functional-testing-guidelines/SKILL.md): validation script.

### 1. Verify remote exposure and preserve integrated historical work

Fetched upstream and verified main exposure. Removed only integrated remote branches with SHA leases and a recovery bundle. Retained the unique V2 issue-74 commit. Both upstream develop trees are free of private metadata.

---

### 2. Prepare and validate a minimal upstream main cleanup contribution

Prepared patch and immutable proposed-tree evidence under local_volume/shared/upstream-remediation-20261031/pantagruel-research/. All product blobs must remain identical to upstream main. The pre-push chain must allow deletion of previously exposed metadata while rejecting its introduction. Validate the proposal with validate-upstream-cleanup.py.

---

### 3. Review publication and restore synchronized downstream standby

Publish a numbered cleanup branch and PR. Preserve main history; do not bundle unrelated develop product changes into upstream. Verify final refs, PR state, and local clean develop. Downstream synchronization is explicitly authorized. No rewriting historical commits.
