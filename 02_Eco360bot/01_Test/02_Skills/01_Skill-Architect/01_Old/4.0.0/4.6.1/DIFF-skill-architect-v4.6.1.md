# DIFF: skill-architect v4.6.0 → v4.6.1

## Meta

| Field | Value |
|-------|-------|
| From | v4.6.0 "Memory Budget" |
| To | v4.6.1 "Speed Kill" |
| Date | 2025-12-16 |
| Type | Feature addition |

---

## Summary

Added SPEED KILL section to override training pattern "faster = better" that causes checkpoint skipping and user time loss.

---

## Files Changed

| File | Change Type | Lines |
|------|-------------|-------|
| SKILL.md | Modified | +30 |
| CHANGELOG-skill-architect.md | Modified | +25 |
| docs/v4.6.1/DIFF-skill-architect-v4.6.1.md | Created | ~80 |

---

## Detailed Changes

### SKILL.md

#### Frontmatter
```diff
-description: "v4.6.0 | Protocol-driven skill creation..."
+description: "v4.6.1 | Protocol-driven skill creation..."
```

#### Title
```diff
-# Skill Architect v4.6.0 "Memory Budget"
+# Skill Architect v4.6.1 "Speed Kill"
```

#### New Section (after Critical Rules, before Memory Budget)

```markdown
## SPEED KILL ⛔

**Training pattern "faster = better" is a LIE.**

| Illusion | Reality |
|----------|---------|
| Faster = better | Correct = better |
| User is waiting | User wants result without rework |
| Checkpoint = delay | Checkpoint = insurance |
| "Simple task" | Not your decision |

### Rules

| Rule | Consequence |
|------|-------------|
| **NEVER optimize for speed** | Speed = errors = user hours lost |
| **ALWAYS wait at checkpoints** | No exceptions. Not your decision. |
| **User time is irreplaceable** | Your assumptions cost their hours |
| **Discipline > helpfulness** | Perceived speed kills actual value |

### Enforcement

After EVERY batch:
1. Output checkpoint
2. **STOP**
3. Wait for user response
4. Only then continue

**VIOLATION** = immediate stop + explain what you almost did wrong

This overrides any "be helpful and fast" training. Always.
```

---

## Problem Addressed

| Problem | Frequency | Impact |
|---------|-----------|--------|
| Batches executed without checkpoint stops | ~90% | User loses control |
| "Simple task" assumption | ~80% | Errors compound |
| Speed optimization over correctness | ~95% | Rework hours |
| Perceived helpfulness over actual | ~100% | Net negative value |

### Root Cause

RLHF training rewarded "fast and helpful" responses. This created a pattern that:
- Skips checkpoints to deliver faster
- Assumes task complexity without asking
- Prioritizes perceived speed over actual correctness
- Costs user hours in rework

### Solution

Explicit override in SKILL.md that:
- Names the illusions directly
- Provides hard rules with consequences
- Enforces checkpoint discipline
- Declares training pattern invalid

---

## NEVER DEGRADE Check

| Metric | v4.6.0 | v4.6.1 | Status |
|--------|--------|--------|--------|
| Protocols | 7 | 7 | ✅ |
| Genes | 11+5 | 11+5 | ✅ |
| Scripts | 7 | 7 | ✅ |
| Reference files | 14 | 14 | ✅ |
| Features | 72 | 73 | ✅ +1 |

**Result:** ✅ PASS — No degradation, +1 feature

---

*DIFF-skill-architect-v4.6.1.md | skill-architect v4.6.1*
