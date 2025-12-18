# Patch: Session Indicator v1.0

**Target:** skill-architect v8.7.0 → v8.8.0  
**Type:** Feature replacement  
**Priority:** High  
**Reason:** Token counter was unreliable (Claude cannot access real token count)

---

## Summary

Replace fake token counter with honest session state indicator.

**Before:**
```
🟢 ~165k | ~3k 🟡
```

**After:**
```
🟢 fresh
```

---

## Changes

### 1. SKILL.md

**Location:** Line 66-72 (Context Anchor section)

**Old:**
```markdown
## ⚠️ Context Anchor

End EVERY response:
```
⚙️ skill-architect v8.7.0 · [protocol] · [status]
🟢 [remaining] | ~[cost] 🟡
```
```

**New:**
```markdown
## ⚠️ Context Anchor

End EVERY response:
```
⚙️ skill-architect v[X.Y.Z] · [protocol] · [status]
[session-indicator]
```

Session indicator format — see reference/session-indicator.md
```

---

### 2. NEW FILE: reference/session-indicator.md

**Action:** Create new file

```markdown
# Session Indicator

Honest session state tracking. Replaces unreliable token counter.

---

## Format

Single line, one of three states:

| State | Display | Meaning |
|-------|---------|---------|
| Fresh | 🟢 fresh | Free to work, context clean |
| Mid | 🟡 mid | Normal, keep focus |
| Long | 🔴 long | Risk of context loss, stay narrow |

---

## Detection Rules

### 🟢 fresh

ALL conditions met:
- < 10 user messages in session
- No files > 500 lines loaded
- < 5 tool calls total
- No large artifacts generated

### 🟡 mid

ANY condition met:
- 10-30 user messages
- 1-2 large files (> 500 lines)
- 5-15 tool calls
- 1-2 large artifacts generated

### 🔴 long

ANY condition met:
- > 30 user messages
- > 2 large files loaded
- > 15 tool calls
- > 2 large artifacts
- Multiple complex code generations

---

## Aggravating Factors

These push indicator ONE level higher:

- File > 1000 lines loaded
- Multiple skill files read in session
- Heavy debugging/iteration cycles
- User uploaded images (high token cost)
- Cyrillic-heavy conversation (higher token/char ratio)

---

## Behavior by State

| State | Claude Action |
|-------|---------------|
| 🟢 fresh | Work freely |
| 🟡 mid | Keep responses focused, avoid tangents |
| 🔴 long | Suggest narrowing focus or new chat if appropriate |

---

## Context Anchor Format

```
⚙️ [skill-name] v[X.Y.Z] · [protocol] · [status]
[indicator] [state]
```

**Examples:**
```
⚙️ skill-architect v8.8.0 · P01-init · active
🟢 fresh

⚙️ skill-architect v8.8.0 · P03-build · creating
🟡 mid

⚙️ skill-architect v8.8.0 · P06-audit · complete
🔴 long
```

---

## Integration in Other Skills

When embedding in new skills, add to SKILL.md:

```markdown
## Context Anchor

End EVERY response:
```
⚙️ [skill-name] v[X.Y.Z] · [status]
[session-indicator]
```

Indicator: 🟢 fresh | 🟡 mid | 🔴 long
Based on message count, file load, tool usage.
```

---

## Why Not Token Counter?

Claude cannot reliably access:
- Exact token count of context
- Context window limit for current model
- Real remaining capacity

Previous approach produced inconsistent outputs:
- "full context" (meaningless)
- "done" (wrong field)
- Dollar amounts (irrelevant metric)
- Random numbers (hallucination)

Session indicator uses observable facts only.

---

*session-indicator.md v1.0.0 | skill-architect v8.8.0*
```

---

### 3. reference/context-management.md

**Location:** Lines 7-14 (Token Counter section)

**Old:**
```markdown
## Token Counter

| Remaining | Format | Action |
|-----------|--------|--------|
| >100k | 🟢 ~Xk \| ~Yk 🟡 | Healthy |
| 50-100k | 🟡 ~Xk \| ~Yk 🔴 | Consider compaction |
| <50k | 🔴 ~Xk \| ~Yk ⚫ | Mandatory compaction |
```

**New:**
```markdown
## Session Indicator

| State | Display | Action |
|-------|---------|--------|
| Fresh | 🟢 fresh | Work freely |
| Mid | 🟡 mid | Keep focus, avoid tangents |
| Long | 🔴 long | Narrow scope or suggest new chat |

Full spec: reference/session-indicator.md
```

---

**Location:** Lines 46-52 (Context Anchor section)

**Old:**
```markdown
## Context Anchor

Every response ends with:
```
⚙️ [skill] · [protocol] · [status]
🟢 ~Xk | ~Yk 🟡
```
```

**New:**
```markdown
## Context Anchor

Every response ends with:
```
⚙️ [skill] v[X.Y.Z] · [protocol] · [status]
🟢 fresh
```

See: reference/session-indicator.md
```

---

### 4. reference/protocols/*.md

**Action:** Update Context Anchor examples in all protocol files

**Pattern to find:**
```
🟢 ~Xk | ~Yk 🟡
```

**Replace with:**
```
🟢 fresh
```

**Files to check:**
- P00-router.md
- P01-init.md (if exists)
- P02-plan.md (if exists)
- P03-build.md (if exists)
- P04-deliver.md (if exists)
- P05-simulation.md (if exists)
- P06-audit.md (if exists)

---

### 5. Version Bump

**SKILL.md line 3:**
```markdown
description: "v8.8.0 | Lean protocol-driven skill creation..."
```

**SKILL.md line 6:**
```markdown
# Skill Architect v8.8.0
```

**SKILL.md last line:**
```markdown
*v8.8.0 "Honest Indicator" — session state tracking*
```

---

## CHANGELOG Entry

```markdown
## [8.8.0] - 2024-XX-XX

### Changed
- Replaced token counter with session indicator
- Token counter was unreliable (Claude cannot access real token count)

### Added
- reference/session-indicator.md — full spec for session state tracking
- Three states: 🟢 fresh | 🟡 mid | 🔴 long
- Detection based on observable facts: message count, file load, tool usage

### Fixed
- Context Anchor now shows consistent, honest information
- No more hallucinated token counts or dollar amounts
```

---

## Validation

After applying patch, run:

```bash
./scripts/validate-skill.sh /path/to/skill-architect
```

Check:
- [ ] SKILL.md < 300 lines
- [ ] All references to old token format removed
- [ ] session-indicator.md exists and valid
- [ ] Context Anchor format consistent across all files

---

## Related Skills to Update

Apply same pattern to:
- `clean-protocol` — uses same token counter
- Any future skills using Context Anchor

---

*patch-session-indicator-v1.0.md | Created for skill-architect v8.7.0 → v8.8.0*
