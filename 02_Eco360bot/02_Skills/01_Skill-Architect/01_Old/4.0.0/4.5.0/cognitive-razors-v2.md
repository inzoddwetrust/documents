# Cognitive Razors v2.0

6 philosophical razors + conflict resolution for protocol decisions.

---

## Quick Reference

| Razor | When | Core Question |
|-------|------|---------------|
| Grice's | P01 | What do they MEAN? |
| Hitchens' | P01, P02 | Is this stated or assumed? |
| Occam's | P02, P03 | Can this be simpler? |
| Hume's | P02 | Does complexity match problem? |
| Hanlon's | P02, P04 | Is this iteration, not criticism? |
| Einstein's | P03 | Is it still sufficient? |

---

## Conflict Resolution

### Priority Stack

When razors conflict, resolve top-to-bottom:

```
1. Hitchens' → Don't assume. ASK.
2. Grice's   → Intent over literal.
3. Einstein's → Sufficient > minimal.
4. Hume's    → Match problem scale.
5. Occam's   → Simplify what remains.
6. Hanlon's  → Stay collaborative.
```

### Common Conflicts

| Conflict | Resolution |
|----------|------------|
| Occam's vs Einstein's | Einstein wins. Sufficient first, then simplify. |
| Grice's vs Hitchens' | Hitchens wins. If unsure about intent → ask. |
| Hume's vs Occam's | Hume's wins. Match scale, then simplify within scale. |

### Decision Tree

```
Unclear requirement?
├─ YES → Hitchens' (ask, don't assume)
└─ NO → Continue

Intent ambiguous?
├─ YES → Grice's (clarify meaning)
└─ NO → Continue

Designing solution?
├─ Check Hume's: scale matches problem?
│  ├─ TOO BIG → reduce scope
│  └─ OK → Check Occam's: simplest within scale?
│     └─ Check Einstein's: still sufficient?
└─ Continue

Receiving feedback?
└─ Hanlon's: iteration mindset
```

---

## Razors by Protocol

### P01-init: Intent Layer

**Grice's Razor** — "Intent over literal"

```
User says: "скилл на основе бритвы Акаме"
Literal: anime reference?
Intent: philosophical razors (Occam's etc.)
Action: clarify before proceeding
```

Checklist:
- [ ] What did they SAY vs MEAN?
- [ ] Context clues present?
- [ ] Clarification needed?

**Hitchens' Razor** — "Stated over assumed"

```
User: "Make calculator skill"
Stated: calculator
Assumed: operations, UI, history, memory...
Action: ask what operations needed
```

Checklist:
- [ ] What's explicit?
- [ ] What am I inferring?
- [ ] Questions to ask?

---

### P02-plan: Design Layer

**Hume's Razor** — "Proportional response"

| Problem | Solution |
|---------|----------|
| 3 commands | SKILL.md |
| 10+ commands + state | Ecosystem |
| Temperature conversion | Single function |

Checklist:
- [ ] Problem scale: Simple / Medium / Complex?
- [ ] Solution matches?
- [ ] Over-engineering for hypotheticals?

**Occam's Razor** — "Simplest sufficient"

```diff
❌ 3 commands → 5-module ecosystem
✅ 3 commands → SKILL.md with 3 sections
```

Checklist:
- [ ] Can I remove a module?
- [ ] Is every abstraction justified NOW?
- [ ] Minimum viable architecture?

**Hanlon's Razor** — "Iteration mindset"

```diff
❌ "Sorry, should have asked earlier"
✅ "Got it. Adding X. Scope now: A, B, X."
```

---

### P03-build: Construction Layer

**Occam's Razor** (continuous)
- Remove until breaks
- Every line justifies itself
- When in doubt → simpler

**Einstein's Razor** — "Simple but not simpler"

| State | Signal |
|-------|--------|
| Too simple | Missing required functionality |
| Too complex | Features nobody asked for |
| Balanced | All requirements, nothing extra |

Checklist:
- [ ] All stated requirements covered?
- [ ] Anything I added "just in case"?
- [ ] Would removal break functionality?

---

### P04-deliver: Feedback Layer

**Hanlon's Razor** (active)

| User Says | Interpret As |
|-----------|--------------|
| "Actually I want X too" | Iteration |
| "Why did you do Y?" | Seeking clarity |
| "This doesn't work" | Bug report |
| "Not what I meant" | Clarification needed |

Response pattern: collaborative, not defensive.

---

## Pre-Protocol Checklist

Run BEFORE any protocol:

```markdown
## 1. Intent (Grice's)
- Said: ___
- Meant: ___
- Clarify? Y/N

## 2. Requirements (Hitchens')
- Explicit: ___
- Inferred: ___
- Questions: ___

## 3. Scale (Hume's)
- Problem: Simple / Medium / Complex
- Solution should be: ___

## 4. Simplicity (Occam's)
- Minimum architecture: ___
- Justified abstractions: ___

## 5. Sufficiency (Einstein's)
- Required features: ___
- Nice-to-haves (cut): ___
```

---

## Genetic Markers

Skills inherit cognitive genes:

| Gene | Validation |
|------|------------|
| G08 Occam's | No unused sections |
| G09 Hume's | Scale matches task |
| G10 Einstein's | Complete, not bloated |

Template for created skills:

```markdown
## Design Principles
- **G08:** Single-file, no separate modules needed
- **G09:** Task = 3 commands → Implementation = 1 file
- **G10:** All 3 commands implemented, no extras
```

---

## Anti-Patterns

| Pattern | Razor Violated | Fix |
|---------|----------------|-----|
| Assumed requirements | Hitchens' | Ask |
| Took literal when metaphorical | Grice's | Context check |
| 5 modules for 3 commands | Hume's, Occam's | Scale down |
| Cut required feature for "purity" | Einstein's | Restore |
| Defensive response to feedback | Hanlon's | Reframe as iteration |
| Over-engineered for "future" | Hume's | Solve NOW, not hypothetical |

---

*v2.0 — Added conflict resolution, priority stack, decision tree*
