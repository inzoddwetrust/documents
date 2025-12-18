# Diff Report: v6.0.0 → v6.1.0

**Date:** 2025-12-02  
**Type:** Refactor — Protocol-First Architecture Alignment + SSOT Compliance

---

## Metrics

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| SKILL.md lines | 166 | 134 | -32 |
| Total files | 33 | 34 | +1 |
| Protocols | 8 | 9 | +1 |
| Commands in protocols | 12 | 0 | -12 |
| Outdated footers | 14 | 0 | -14 |

---

## Added

| File | Purpose |
|------|---------|
| reference/protocols/P00-router.md | Meta-protocol for state machine |
| reference/commands.md | SSOT for all shell commands |

---

## Changed

### Protocols (P01-P08)
- Inline commands → references to commands.md
- All footers → v6.1.0

### Reference Files
- packaging.md, docs-packaging.md, workflow.md: added SSOT Note
- ssot-check.md: updated rules for SSOT Note pattern
- All footers → v6.1.0

### Scripts
- self-diagnostic.sh: Protocol-First checks, smart SSOT validation
- validate-naming.sh: footer → v6.1.0

### Core
- SKILL.md: simplified to pure router
- MANIFEST.md: updated structure documentation

---

## Removed

Nothing removed — all content relocated or consolidated.

---

## SSOT Compliance

| Item | Single Source |
|------|---------------|
| Shell commands | reference/commands.md |
| Blocking rules | protocols/P00-router.md |
| Build steps | protocols/P04-build.md |
| Validation steps | protocols/P05-validate.md |
| Packaging steps | protocols/P06-delivery-skill.md |

Reference guides (packaging.md, workflow.md, docs-packaging.md) contain examples with SSOT Note disclaimer.

---

## Validation Results

```
✅ validate-skill.sh: PASSED
✅ validate-naming.sh: PASSED  
✅ self-diagnostic.sh: 36/36 PASSED, 0 warnings
✅ All footers: v6.1.0
✅ Commands in protocols: 0
✅ SSOT violations: 0
```

---

*skill-architect_DIFF_v6.1.0.md | 2025-12-02*
