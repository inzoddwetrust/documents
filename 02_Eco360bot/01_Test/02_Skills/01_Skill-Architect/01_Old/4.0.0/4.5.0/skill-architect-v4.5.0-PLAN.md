# Planning Document: skill-architect v4.5.0

## Meta

| Field | Value |
|-------|-------|
| Target | skill-architect |
| Version | v4.4.0 → v4.5.0 |
| Mode | UPDATE |
| Codename | "Conflict Resolution" |

---

## Objective

Integrate cognitive-razors v2.0 with priority stack for razor conflict resolution.

---

## Changes

### 1. SKILL.md

**Location:** After "Cognitive Razors" table (line ~136)

**Add:**

```markdown
### Conflict Resolution

Priority stack (top wins):
1. Hitchens' → Ask, don't assume
2. Grice's → Intent over literal
3. Einstein's → Sufficient > minimal
4. Hume's → Match problem scale
5. Occam's → Simplify what remains
6. Hanlon's → Stay collaborative

Common: Occam's vs Einstein's → Einstein wins (sufficient first).
```

---

### 2. reference/cognitive-razors.md

**Action:** REPLACE entire file with cognitive-razors-v2.md

**Source:** /home/claude/cognitive-razors-v2.md

---

### 3. protocols/P02-plan.md

**Location:** After "Design Razors" section

**Add:**

```markdown
### Razor Conflict?

If Occam's says "simpler" but Einstein's says "insufficient":
→ Einstein wins. Cover requirements first, simplify second.

If unsure about intent AND want to simplify:
→ Hitchens wins. Ask before cutting.
```

---

### 4. protocols/P03-build.md

**Location:** After "PRE-ACTION" section

**Add:**

```markdown
### Pre-Build Razor Check

Before writing code:
- [ ] All Hitchens' questions answered?
- [ ] Scale matches (Hume's)?
- [ ] Simplest sufficient (Occam's + Einstein's)?
```

---

### 5. CHANGELOG-skill-architect.md

**Location:** Top of changelog

**Add:**

```markdown
## v4.5.0 "Conflict Resolution"

- Added razor conflict resolution with priority stack
- Updated reference/cognitive-razors.md to v2.0
- Added decision tree for razor conflicts
- Added Pre-Build Razor Check to P03-build.md
- SKILL.md: +Conflict Resolution section
```

---

## Not Changing

| Component | Reason |
|-----------|--------|
| Protocol flow (P01→P04) | Working as intended |
| Genetic markers G08-G10 | Already cover razors |
| Anchor format | Stable |
| Quality Gates L1-L10 | Complete |
| Scripts | No changes needed |
| INoT Engine | Unrelated |

---

## NEVER DEGRADE Validation

| Feature | v4.4.0 | v4.5.0 | Status |
|---------|--------|--------|--------|
| 6 cognitive razors | ✓ | ✓ | PRESERVED |
| Protocol chain P01-P04 | ✓ | ✓ | PRESERVED |
| Genes G01-G15 | ✓ | ✓ | PRESERVED |
| Quality Gates L1-L10 | ✓ | ✓ | PRESERVED |
| Validation routing | ✓ | ✓ | PRESERVED |
| Ecosystem paths | ✓ | ✓ | PRESERVED |
| **Conflict resolution** | — | ✓ | NEW |
| **Priority stack** | — | ✓ | NEW |
| **Pre-Build Razor Check** | — | ✓ | NEW |

**Result:** 6 features preserved, 3 features added. ✅ PASS

---

## Execution Order

1. Copy baseline (done)
2. Edit SKILL.md
3. Replace reference/cognitive-razors.md
4. Edit protocols/P02-plan.md
5. Edit protocols/P03-build.md
6. Edit CHANGELOG-skill-architect.md
7. Run validation
8. Package

---

*Planning Document | skill-architect v4.5.0*
