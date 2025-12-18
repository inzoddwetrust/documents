# Diff: v8.5.0 → v8.6.0

**Skill:** skill-architect  
**Date:** 2025-12-12

---

## Metrics

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| SKILL.md lines | 169 | 167 | -2 |
| Total files | ~35 | ~36 | +1 |
| Scripts | 11 | 12 | +1 |
| Protocols | 10 | 10 | 0 |

---

## Added

| File/Section | Lines | Purpose |
|--------------|-------|---------|
| `scripts/validate-degrade.sh` | 156 | **NEW** — Automated NEVER DEGRADE enforcement |
| P06 `⛔ NEVER DEGRADE Check` section | 15 | BLOCKING check before packaging |
| P07 `⛔ NEVER DEGRADE Check — Docs` section | 10 | BLOCKING check for docs |
| P08 `Create PATCH Document` step | 45 | Create PATCH when issues found |
| generate-docs.sh `update` mode | 40 | Require prev docs for updates |

---

## Changed

| File | Change | Reason |
|------|--------|--------|
| SKILL.md | Version 8.5.0 → 8.6.0 | Release |
| SKILL.md | Rules 9-10 enforcement → validate-degrade.sh | Automated check |
| SKILL.md | Context Anchor simplified | Remove 📋 line (redundant) |
| P04-build.md | NEVER DEGRADE → reminder only | Check moved to P06/P07 |
| P06-delivery-skill.md | Added BLOCKING check | Automated enforcement |
| P07-closure.md | Added docs check | Prevent template overwrite |
| P08-simulation.md | Added PATCH creation | Document issues for next release |
| generate-docs.sh | v1.0.0 → v2.0.0 | Added update mode |
| All protocols | Footer v8.4.0 → v8.6.0 | Version sync |

---

## Removed

| What | Lines | Reason |
|------|-------|--------|
| SKILL.md 📋 line in Context Anchor | 1 | Redundant (per user request) |
| P04 detailed NEVER DEGRADE checklist | 10 | Moved to P06 as automated check |

⚠️ **NEVER DEGRADE check:** PASSED — functionality moved, not removed

---

## Preserved

- All 10 protocols (structure intact)
- All existing scripts (no deletions)
- Core workflow P00→P09
- All reference files
- docs/v8.5.0/ (history)

---

## Deviation from Plan

- None

---

## Validation

```
✅ SKILL.md: 167 lines (< 300)
✅ SKILL.md: English (except examples)
✅ All footers: v8.6.0
✅ New script: validate-degrade.sh
✅ NEVER DEGRADE: functionality preserved
```

---

*DIFF-skill-architect-v8.6.0.md | skill-architect v8.6.0*
