# release/6-remove-development-metadata · [Issue #6](https://github.com/aprendesc/pantagruel-research/issues/6) · [PR #9](https://github.com/pantagruel-alpha/pantagruel-research/pull/9)

## Context (delta_time: 04/11/2026 14:10)

### Descripción

Retiró metadatos privados publicados en upstream conservando los blobs de aplicación y artículos. El cierre histórico registra PR #9 integrado el 31/10/2026; este contrato no prescribe repetir la operación. La homologación solo mantiene trazabilidad y validación privada.

### Specialized skills

No se requiere una skill especializada adicional para este registro de gobernanza.

---
## Diff (delta_time: 04/11/2026 14:10)

```text
Comparación histórica no recalculada: cierre registrado en 55f80538749c9ce62b82ab91ce6f55bf28136990.
```

---
## Test Profiling (delta_time: 04/11/2026 14:10)

**Script de test funcional:** `context/issues/6-retirar-metadatos-privados-del-upstream/upstream_cleanup_functional_test.py`.

### Árbol de abstracción

```text
A0 Celda
└── A1 Validación funcional
    └── A2 Aplicación y recursos
```

### context/issues/6-retirar-metadatos-privados-del-upstream/upstream_cleanup_functional_test.py :: Verify immutable cleanup and preserve product blobs

```text
LOW · A1
Celda de entrada: # %% [0] Verify immutable cleanup and preserve product blobs
Descripción: Verify immutable cleanup and preserve product blobs; comprueba el mecanismo local sin publicar ni operar servicios externos.
── Configuración ─────────────────────────────
└── upstream_cleanup_functional_test.py
    └── target = 55f80538749c9ce62b82ab91ce6f55bf28136990

── Diagrama ──────────────────────────────────
┌───────────────────────────────────────────────────┐
│ (1) publication.validate_tree(target (a)) -> None │ ───▶ [ (2) assert actual_product == before_product ]
└───────────────────────────────────────────────────┘
R ← objetos Git; .githooks/clone-hooks/publication.py

── Visor de variables y validaciones ──────────
(a) target · target = "55f80538749c9ce62b82ab91ce6f55bf28136990"
[OK] (2) assert actual_product == before_product
```

---
## Persistence (delta_time: 04/11/2026 14:10)

```text
Local
└── context/issues/6-retirar-metadatos-privados-del-upstream/
│   └── upstream_cleanup_functional_test.py
Git
└── 55f80538749c9ce62b82ab91ce6f55bf28136990 · integración registrada
```

---
## Execution plan (delta_time: 04/11/2026 14:10)

### Secuencia de ejecución

Registro de trabajo histórico completado; no orden de volver a publicar.

1. [OK] **Etapa 1 — Verificar exposición y preservar trabajo:** comprobación histórica de referencias y recuperación.
2. [OK] **Etapa 2 — Preparar y validar limpieza:** eliminación de metadatos privados manteniendo blobs públicos.
3. [OK] **Etapa 3 — Publicar y cerrar:** integración y sincronización registradas el 31/10/2026.

### Etapa 1 — Verificar exposición y preservar trabajo

- **Detalles y especificaciones:** preservar código público, historia Git, ramas no integradas y contenido editorial. La celda 0 contrasta el árbol inmutable de propuesta con su base y valida ausencia de metadatos privados.
- **Registro de desarrollo:** ver evidencia histórica consolidada abajo; ninguna nueva operación remota durante la migración.

### Etapa 2 — Preparar y validar limpieza

- **Detalles y especificaciones:** preservar código público, historia Git, ramas no integradas y contenido editorial. La celda 0 contrasta el árbol inmutable de propuesta con su base y valida ausencia de metadatos privados.
- **Registro de desarrollo:** ver evidencia histórica consolidada abajo; ninguna nueva operación remota durante la migración.

### Etapa 3 — Publicar y cerrar

- **Detalles y especificaciones:** preservar código público, historia Git, ramas no integradas y contenido editorial. La celda 0 contrasta el árbol inmutable de propuesta con su base y valida ausencia de metadatos privados.
- **Registro de desarrollo:** ver evidencia histórica consolidada abajo; ninguna nueva operación remota durante la migración.

- **Evidencia histórica conservada:**

- **1. Verify remote exposure and preserve integrated historical work:**

Fetched upstream and verified main exposure. Removed only integrated remote branches with SHA leases and a recovery bundle. Retained the unique V2 issue-74 commit. Both upstream develop trees are free of private metadata.

---

- **2. Prepare and validate a minimal upstream main cleanup contribution:**

Prepared patch and immutable proposed-tree evidence under local-volume/shared/upstream-remediation-20261031/pantagruel-research/. All product blobs must remain identical to upstream main. The pre-push chain must allow deletion of previously exposed metadata while rejecting its introduction. Validate the proposal with upstream_cleanup_functional_test.py.

---

- **3. Review publication and restore synchronized downstream standby:**

Publish a numbered cleanup branch and PR. Preserve main history; do not bundle unrelated develop product changes into upstream. Verify final refs, PR state, and local clean develop. Downstream synchronization is explicitly authorized. No rewriting historical commits.

Publication branch passed the full installed hook chain. Upstream PR: https://github.com/pantagruel-alpha/pantagruel-research/pull/8. The PR is open for review; no upstream merge or deployment has been performed.

- **Completion — 2026-10-31:**

User authorized repair of all confirmed violations. Upstream PR https://github.com/pantagruel-alpha/pantagruel-research/pull/9 merged as `55f80538749c9ce62b82ab91ce6f55bf28136990` after required validation. V2 passed all seven repository tests; Research passed Personal policy and Integration. CI contract checks were updated to accept metadata-free publication. Main snapshots contain no private methodology paths. Application and article blobs were preserved; only validation/CI files were added to the previously approved cleanup delta. The unique issue-74 commit is retained in downstream/archive/74-trade-source-checkpoint and a recovery bundle. All 32 obsolete upstream work branches are removed. Final downstream synchronization is recorded in the closeout PR and external standby evidence.


---
## Results and reporting (delta_time: 04/11/2026 14:10)

El histórico registra la integración de la limpieza privada en upstream y la conservación de los blobs públicos. La migración no repitió publicación ni merge. La validación actual usa el commit inmutable integrado y su primer padre: 69 blobs públicos conservados, 0 rutas privadas y `git diff --check` correcto. El antiguo JSON local ya no estaba disponible; se sustituyó esa dependencia por los propios objetos Git, sin reescribir el histórico ni contactar remotos.
