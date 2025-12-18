# Diff: v8.6.0 → v8.7.0

**Skill:** skill-architect  
**Date:** 2025-12-12

---

## Metrics

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| SKILL.md lines | 167 | 104 | **-38%** |
| Protocol files | 10 | 7 | **-30%** |
| Flow steps | 8 | 5 | **-38%** |
| Blocking points | 4 | 2 | **-50%** |

---

## Restructured

| Old Protocols | New Protocol |
|---------------|--------------|
| P01-activation + P02-config | **P01-init** |
| P03-planning | **P02-plan** |
| P04-build + P05-validate | **P03-build** |
| P06-delivery + P07-closure | **P04-deliver** |
| P08-simulation | **P05-simulation** |
| P09-full-audit | **P06-audit** |

---

## Added

| File | Lines | Purpose |
|------|-------|---------|
| P01-init.md | 65 | Merged activation + config |
| P02-plan.md | 70 | Renamed planning |
| P03-build.md | 75 | Merged build + validate |
| P04-deliver.md | 85 | Merged delivery + closure |
| P05-simulation.md | 60 | Renamed simulation |
| P06-audit.md | 55 | Renamed audit |

---

## Removed

| File | Reason |
|------|--------|
| P01-activation.md | → P01-init |
| P02-config.md | → P01-init |
| P03-planning.md | → P02-plan |
| P04-build.md | → P03-build |
| P05-validate.md | → P03-build |
| P06-delivery-skill.md | → P04-deliver |
| P07-closure.md | → P04-deliver |
| P08-simulation.md | → P05-simulation |
| P09-full-audit.md | → P06-audit |

⚠️ **NEVER DEGRADE:** PASSED — functionality merged, not removed

---

## Preserved

- All scripts (validate-*.sh, generate-docs.sh)
- All reference files
- NEVER DEGRADE enforcement
- Docs system
- Quality checklist

---

## Validation

```
✅ SKILL.md: 104 lines (< 300)
✅ SKILL.md: English
✅ Protocols: 7 files (P00-P06)
✅ Flow: P01 → P02 ⛔ → P03 → P04 ⛔ → P05
```

---

*DIFF-skill-architect-v8.7.0.md | skill-architect v8.7.0*
