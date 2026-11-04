# release/6-remove-development-metadata · [Issue #6](https://github.com/aprendesc/pantagruel-research/issues/6) · [PR #9](https://github.com/pantagruel-alpha/pantagruel-research/pull/9)

## Descripción

Retirada histórica de metadatos privados de upstream y revisión de su cierre, conservando código público, artículos, historia Git y trabajo no integrado. La PR #9 quedó integrada el 31/10/2026 en `55f80538749c9ce62b82ab91ce6f55bf28136990`. Es un contrato general de gobernanza y revisión: su entregable fue la limpieza y su evidencia, sin implementación de producto ni redacción de un corpus.

La presente migración conserva los tres pasos completados, sus decisiones y validaciones registradas. No prescribe repetir la limpieza, publicar, borrar ramas ni sincronizar remotos.

---
## Diff

DU/IU (🔴 / 🔴) · IU/ID (🔴 / 🔴) · DU/DD (🔵 0 / 🟢 8) · DD/ID (🔴 / 🔴)
DU = pantagruel-alpha/pantagruel-research:develop (pendiente)\
IU = pantagruel-alpha/pantagruel-research:🔴 (pendiente)\
ID = aprendesc/pantagruel-research:🔴 (aprendesc)\
DD = aprendesc/pantagruel-research:develop (aprendesc)

**Cómputo:** DU/DD e IU/ID excluyen archivos privados y trazas privadas de `.gitignore` según el filtro canónico de publicación; DD/ID y DU/IU incluyen el árbol completo. Cada par cuenta cambios desde su ancestro común hacia la rama izquierda / derecha.

```text
Comparación histórica no recalculada: cierre registrado en 55f80538749c9ce62b82ab91ce6f55bf28136990.
Base de la validación histórica: primer padre de ese commit.
```

---
## Persistencia

```text
Local · raíz del repositorio
└── context/issues/6-retirar-metadatos-privados-del-upstream/
    ├── 6-retirar-metadatos-privados-del-upstream.md  contrato general y seguimiento
    ├── migration-source.md                         original exacto previo a esta transformación
    └── upstream_cleanup_functional_test.py         comprobación privada conservada; no ejecutada ahora
Git · objeto de integración registrado
└── 55f80538749c9ce62b82ab91ce6f55bf28136990
Evidencia externa histórica · local-volume/shared/upstream-remediation-20261031/pantagruel-research/
└── validation.json                                 no disponible en la validación del 04/11/2026
Recuperación histórica
├── downstream/archive/74-trade-source-checkpoint    referencia V2, no de Research
└── recovery bundle                                 ubicación no precisada en el registro
```

La comprobación privada usa `.githooks/clone-hooks/publication.py` y objetos Git; que exista un script no convierte esta revisión en una contribución de código. No se ha vuelto a comprobar la disponibilidad del volumen ni las referencias remotas durante esta migración.

---
## Plan

Registro de trabajo histórico completado, con la misma secuencia y estados; no orden de ejecución nueva.

1. [OK] **Verificar exposición y preservar trabajo integrado:** conservar código público, historia Git, ramas no integradas y corpus editorial; comprobar referencias y recuperación.

Fetched upstream and verified main exposure. Removed only integrated remote branches with SHA leases and a recovery bundle. Retained the unique V2 issue-74 commit. Both upstream develop trees are free of private metadata.

2. [OK] **Preparar y validar una limpieza mínima de upstream main:** retirar metadatos privados sin modificar blobs de producto, con evidencia inmutable y controles de publicación.

Prepared patch and immutable proposed-tree evidence under local-volume/shared/upstream-remediation-20261031/pantagruel-research/. All product blobs must remain identical to upstream main. The pre-push chain must allow deletion of previously exposed metadata while rejecting its introduction. Validate the proposal with upstream_cleanup_functional_test.py.

3. [OK] **Revisar publicación y restaurar downstream sincronizado:** publicar la contribución numerada autorizada, revisar PR/refs y conservar `develop` limpio, sin reescribir commits ni mezclar producto ajeno.

Publish a numbered cleanup branch and PR. Preserve main history; do not bundle unrelated develop product changes into upstream. Verify final refs, PR state, and local clean develop. Downstream synchronization is explicitly authorized. No rewriting historical commits.

Publication branch passed the full installed hook chain. Upstream PR: https://github.com/pantagruel-alpha/pantagruel-research/pull/8. The PR is open for review; no upstream merge or deployment has been performed.

El estado de PR #8 «open for review» del registro anterior a la integración se conserva como evento histórico; no describe el cierre final ni un estado GitHub comprobado hoy.

---
## Seguimiento

### Cierre registrado — 31/10/2026

User authorized repair of all confirmed violations. Upstream PR https://github.com/pantagruel-alpha/pantagruel-research/pull/9 merged as `55f80538749c9ce62b82ab91ce6f55bf28136990` after required validation. V2 passed all seven repository tests; Research passed Personal policy and Integration. CI contract checks were updated to accept metadata-free publication. Main snapshots contain no private methodology paths. Application and article blobs were preserved; only validation/CI files were added to the previously approved cleanup delta. The unique issue-74 commit is retained in downstream/archive/74-trade-source-checkpoint and a recovery bundle. All 32 obsolete upstream work branches are removed. Final downstream synchronization is recorded in the closeout PR and external standby evidence.

### Validación privada registrada — 04/11/2026 14:10

El contrato previo registra una comprobación contra el commit integrado y su primer padre: **69 blobs de producto conservados**, **0 rutas privadas** y `git diff --check` correcto. El JSON local antiguo ya no estaba disponible; se reemplazó esa dependencia por los propios objetos Git, sin reescribir historia ni contactar remotos.

Mecanismo conservado en `upstream_cleanup_functional_test.py`, celda `# %% [0] Verify immutable cleanup and preserve product blobs`: `publication.validate_tree(target)` comprueba el árbol; `actual_product == before_product` contrasta los blobs. El script excluye de esa comparación las rutas privadas y los cambios de CI explícitamente registrados (`.gitignore`, `.github/`, `tests/article-publication/ci-workflow.test.mjs`). El dato de 69 blobs corresponde a ese alcance de comparación.

### Migración de tipo — 04/11/2026 16:51

Reclasificado a general por su entregable de gobernanza. Se conservan especificaciones, estados y evidencia; el original exacto anterior se encuentra en [migration-source.md](migration-source.md). Se eliminó la estructura obligatoria de profiling de código, manteniendo la comprobación útil como evidencia auxiliar. Sin ejecución de pruebas ni operaciones externas durante esta migración.
