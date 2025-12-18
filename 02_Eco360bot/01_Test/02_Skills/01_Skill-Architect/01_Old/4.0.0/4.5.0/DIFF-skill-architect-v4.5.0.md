# Diff Report: skill-architect v4.5.0

v4.4.0 → v4.5.0 "Conflict Resolution"

---

## Summary

| Metric | v4.4.0 | v4.5.0 | Delta |
|--------|--------|--------|-------|
| SKILL.md lines | 365 | 377 | +12 |
| Protocol files | 5 | 5 | — |
| Reference files | 12 | 12 | — |
| New features | — | 3 | +3 |

---

## Changes by File

### SKILL.md

```diff
+ ### Conflict Resolution
+ 
+ Priority stack (top wins):
+ 1. Hitchens' → Ask, don't assume
+ 2. Grice's → Intent over literal
+ 3. Einstein's → Sufficient > minimal
+ 4. Hume's → Match problem scale
+ 5. Occam's → Simplify what remains
+ 6. Hanlon's → Stay collaborative
+ 
+ Common: Occam's vs Einstein's → Einstein wins (sufficient first).
```

### reference/cognitive-razors.md

**REPLACED** with v2.0:
- Added Conflict Resolution section
- Added Priority Stack
- Added Decision Tree
- Added Common Conflicts table
- Added Anti-Patterns section

### protocols/P02-plan.md

```diff
+ ### Razor Conflict?
+ 
+ If Occam's says "simpler" but Einstein's says "insufficient":
+ → Einstein wins. Cover requirements first, simplify second.
+ 
+ If unsure about intent AND want to simplify:
+ → Hitchens wins. Ask before cutting.
```

### protocols/P03-build.md

```diff
+ ### Pre-Build Razor Check
+ 
+ Before writing code:
+ - [ ] All Hitchens' questions answered?
+ - [ ] Scale matches (Hume's)?
+ - [ ] Simplest sufficient (Occam's + Einstein's)?
```

---

## NEVER DEGRADE Validation

| Feature | v4.4.0 | v4.5.0 | Status |
|---------|--------|--------|--------|
| 6 cognitive razors | ✓ | ✓ | PRESERVED |
| Protocol chain P01-P04 | ✓ | ✓ | PRESERVED |
| Genes G01-G15 | ✓ | ✓ | PRESERVED |
| Quality Gates L1-L10 | ✓ | ✓ | PRESERVED |
| Validation routing | ✓ | ✓ | PRESERVED |
| All scripts (7) | ✓ | ✓ | PRESERVED |
| Conflict resolution | — | ✓ | NEW |
| Priority stack | — | ✓ | NEW |
| Pre-Build Razor Check | — | ✓ | NEW |

**Result:** ✅ PASS — 6 preserved, 3 added

---

## Files Modified

| File | Action |
|------|--------|
| SKILL.md | EDITED (+12 lines) |
| reference/cognitive-razors.md | REPLACED |
| protocols/P00-router.md | VERSION |
| protocols/P01-init.md | VERSION |
| protocols/P02-plan.md | EDITED (+8 lines) |
| protocols/P03-build.md | EDITED (+6 lines) |
| protocols/P04-deliver.md | VERSION |
| CHANGELOG-skill-architect.md | EDITED |
| MANIFEST.md | EDITED |
| reference/genetic-audit.md | VERSION |

---

*Diff Report | skill-architect v4.5.0*
