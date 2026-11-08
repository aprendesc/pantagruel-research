# 2 - Remove legacy integration control

## Context

The user explicitly requires removing the obsolete repository integration control and its workflow dependencies. Integration is governed by the current APC Harness methodology. Preserve application CI jobs, their existing activation conditions, local canonical hooks and unrelated project work. Publish and integrate this cleanup into downstream/develop. This is local maintenance task 2; no GitHub issue is claimed.

## Preferences and memories

- **BD:** `downstream/develop`
- **BU:** `upstream/develop`
- **ID:** `downstream/chore/2-remove-legacy-ci`
- **IU:** `upstream/chore/2-remove-legacy-ci-upstream`
- **Authority:** Remove the legacy integration package, stale documentation and obsolete special cases; keep current canonical controls active.
- **CI/CD:** GL4 Personal CI/CD Guidelines; the methodology remains applicable.
- **Functional status:** PENDING; do not claim broad test coverage.
- **Depth:** ADAPTIVE; scoped removal and verification of workflow dependency integrity.

## Validation

Verify that the retired package has no active references, remaining workflow jobs and conditions are preserved, dependencies resolve, and installed canonical hooks still verify. No general test redesign is included.
