# Planning Document: skill-architect v4.3.0 "Interactive Razors"

## Meta

| Field | Value |
|-------|-------|
| Date | 2025-12-15 |
| Mode | UPDATE |
| Baseline | v4.2.0 "Delegation" |
| Retrospectives | 3 versions (v4.0.0, v4.1.0, v4.2.0) analyzed |

---

## ⛔ BUILD RULES — READ FIRST

### Forbidden Actions

| ❌ FORBIDDEN | Why |
|--------------|-----|
| `rm file && create_file` | Destroys existing content |
| Rewriting entire files | Loses working logic |
| "Optimizing" by removing | Violates NEVER DEGRADE |
| Ignoring reference/*.md | Miss critical requirements |

### Required Actions

| ✅ REQUIRED | How |
|-------------|-----|
| Use `str_replace` only | Surgical changes, preserve context |
| Read reference/*.md FIRST | Before modifying any protocol |
| Verify .skill packaging preserved | Check P04-deliver lines 74-84 intact |
| Compare before/after line counts | Catch accidental deletions |

### Pre-Build Checklist

Before ANY file modification:

- [ ] Read reference/packaging.md (lines 1-60)
- [ ] Read target file completely
- [ ] Identify EXACT strings to replace
- [ ] Verify replacement preserves surrounding content
- [ ] Check no packaging/delivery logic removed

---

## Sources

| Source | Changes |
|--------|---------|
| ecosystem-analysis-report.md | Version footers removal |
| skill-architect-update-task.md | Interactive Anchors, Language Policy |
| skill-architect-razors-update-plan.md | Cognitive Razors, Genes G08-G10 |
| ecosystem-update-plan-v2.md | Consolidated plan |

---

## KEEP (from baseline) — CRITICAL

### Must Preserve Verbatim

| Item | Location | Lines to NEVER touch |
|------|----------|---------------------|
| .skill package format | reference/packaging.md | ALL (160 lines) |
| Package creation commands | P04-deliver.md | 74-84 |
| zip command format | P04-deliver.md | Line 80: `zip -r skill-name-vX.Y.Z.skill` |
| Delivery to outputs | P04-deliver.md | Line 83: `cp ... /mnt/user-data/outputs/` |
| Final Response template | P04-deliver.md | 153-165 |
| Auto-Test Suggestion | P04-deliver.md | 95-117 |
| Cross-Skill Routing | P04-deliver.md | 119-128 |

### Must Preserve Logic

| Item | Reason |
|------|--------|
| Protocol chain P00→P04 | Working architecture |
| NEVER DEGRADE principle | Quality protection |
| Blocking points (⛔) at P02, P04 | User control |
| Chat Verification | Context preservation |
| PRE-BUILD Checkpoint | Quality gate |
| Diff Report generation | Change visibility |
| INoT Engine | Complex decisions |
| Anchor + NEXT | State management |
| Session Indicator 🟢🟡🔴 | Context awareness |
| Recovery Protocol | Context loss handling |
| Ecosystem awareness | Cross-skill routing |
| test-architect delegation | Single testing authority |
| 5 protocols structure | Working flow |
| 9 reference files content | Supporting docs |
| 5 scripts | Automation |
| docs/ versioned history | Retrospectives |
| Validation Before Packaging | reference/packaging.md 101-110 |

**Total KEEP:** 16 core features + ALL packaging/delivery logic

---

## REMOVE

| Item | Location | Method |
|------|----------|--------|
| Version footer | End of each .md file | str_replace `*...v4.x.x*` → (empty) |
| Confirmation Words section | SKILL.md lines ~78-83 | str_replace entire section → (empty) |

**Total REMOVE:** 2 types of items (footers + one section)

**⚠️ WARNING:** Do NOT remove anything else. No "optimization".

---

## ADD

### A1. SKILL.md — Language Policy

**Location:** After Critical Rules section (line ~77), BEFORE Confirmation Words

**Method:** str_replace

**Find:**
```markdown
| **NEVER DEGRADE** | Feature count ≥ baseline |

---

## Confirmation Words
```

**Replace with:**
```markdown
| **NEVER DEGRADE** | Feature count ≥ baseline |

---

## Language Policy

### Production Rule
All artifacts in English (always):
- SKILL.md, README.md, CHANGELOG.md
- Planning Documents, Diff Reports
- Protocol files, reference files

### Chat Rule
Dialogue adapts to user's language.

### Override
User can explicitly request artifact language.

---

## Confirmation Words
```

---

### A2. SKILL.md — Interactive Anchor (replace Confirmation Words + old Anchor)

**Location:** Lines ~78-106

**Method:** str_replace (replace Confirmation Words section AND Anchor Format section with new combined version)

**Find:**
```markdown
## Confirmation Words

| Valid | Invalid |
|-------|---------|
| да, yes, ок, подтверждаю, го, погнали, do it, confirm, approved | угу, ладно, ну, maybe, looks good |

---

## Anchor Format

Every response MUST end with:

```
⚙️ skill-architect v4.2.0 · [protocol] · [status]
[session] | NEXT: [explicit next action]
```

**Session Indicator:**
- 🟢 fresh (<5 messages)
- 🟡 mid (5-15 messages)
- 🔴 long (>15 messages)

**NEXT** — self-instruction for Claude's next response. Critical: Claude has no memory between responses.

Examples:
- `NEXT: present plan for user confirmation`
- `NEXT: user confirms → run P03-build`
- `NEXT: validate → if pass → deliver`
```

**Replace with:**
```markdown
## Anchor Format

Every response ends with:

```
[session] [protocol] · [status]
NEXT: [explicit next action]

Options: (only at ⛔ points)
1 → [action] (→ [next])
2 → [action]
3 → [action]
```

### Session Indicator
- 🟢 fresh (<5 messages)
- 🟡 mid (5-15 messages)
- 🔴 long (>15 messages)

### Standard Option Sets

| Point | Options |
|-------|---------|
| P02-plan | 1-Confirm, 2-Edit, 3-Cancel |
| P04-deliver | 1-Deliver, 2-Test first, 3-Edit |

### User Input
User types number (1, 2, 3) or matching text.

**NEXT** — self-instruction for Claude's next response.

See: `reference/anchor-format.md`
```

---

### A3. SKILL.md — Cognitive Razors section

**Location:** After INoT Engine section (line ~164)

**Method:** str_replace

**Find:**
```markdown
See: `reference/inot-engine.md`

---

## UPDATE Requirements
```

**Replace with:**
```markdown
See: `reference/inot-engine.md`

---

## Cognitive Razors

6 razors for decision-making:

| Razor | Protocol | Purpose |
|-------|----------|---------|
| Grice's | P01 | Intent vs literal |
| Hitchens' | P01, P02 | Stated vs assumed |
| Occam's | P02, P03 | Simplest solution |
| Hume's | P02 | Proportional complexity |
| Hanlon's | P02, P04 | Iteration mindset |
| Einstein's | P03 | Simple but sufficient |

See: `reference/cognitive-razors.md`

---

## UPDATE Requirements
```

---

### A4. SKILL.md — Update Required Genes (add G08-G10)

**Location:** Required Genes section (lines ~109-124)

**Method:** str_replace

**Find:**
```markdown
| G07 Blocking | ⛔ where confirmation required |

Validation: `test-architect test [path] --genetic`
```

**Replace with:**
```markdown
| G07 Blocking | ⛔ where confirmation required |

### Cognitive Genes (G08-G10)

| Gene | Requirement |
|------|-------------|
| G08 Occam's Design | Simplest structure covering requirements |
| G09 Hume's Scale | Complexity matches task size |
| G10 Einstein's Balance | Complete but not bloated |

Validation: `test-architect test [path] --genetic`
```

---

### A5. P01-init.md — Add Intent Interpretation

**Location:** After PRE-ACTION, before DO (line ~15)

**Method:** str_replace

**Find:**
```markdown
- [ ] If UPDATE: retrospective docs available (1-3 versions)

---

## DO
```

**Replace with:**
```markdown
- [ ] If UPDATE: retrospective docs available (1-3 versions)

---

## Intent Interpretation

Before proceeding, apply:

### Grice's Razor Check
- [ ] What did user MEAN vs SAY?
- [ ] Need clarification?

### Hitchens' Razor Check  
- [ ] What's explicitly stated?
- [ ] What am I assuming?

**Rule:** If ambiguity → ask before planning.

---

## DO
```

---

### A6. P02-plan.md — Add Design Razors

**Location:** After PRE-ACTION, before DO (line ~15)

**Method:** str_replace

**Find:**
```markdown
- [ ] For UPDATE: baseline snapshot exists

---

## DO
```

**Replace with:**
```markdown
- [ ] For UPDATE: baseline snapshot exists

---

## Design Razors

Before Planning Document, apply:

### Occam's Razor
- Simplest architecture covering requirements?

### Hume's Razor
- Solution complexity = problem complexity?

### Hanlon's Mindset
- Change requests = iteration, not criticism

---

## DO
```

---

### A7. P02-plan.md — Update Blocking Rules to Options

**Location:** Lines ~115-120

**Method:** str_replace

**Find:**
```markdown
## ⛔ BLOCKING RULES

1. Do NOT start building without explicit confirmation
2. Valid confirmations: да, yes, ок, подтверждаю, го, погнали, do it, confirm, approved
3. Invalid: угу, ладно, ну, maybe, looks good
4. If unclear: ask again
```

**Replace with:**
```markdown
## ⛔ BLOCKING: Options

Present at this point:

```
🟡 P02-plan · ⛔ waiting-confirm
NEXT: confirm → P03-build

Options:
1 → Confirm (→ P03-build)
2 → Edit plan
3 → Cancel
```

| Input | Action |
|-------|--------|
| 1, да, yes, confirm | → P03-build |
| 2, edit, правки | Update plan |
| 3, cancel, отмена | Cancel |
```

---

### A8. P03-build.md — Add Build Razors

**Location:** After PRE-BUILD Checkpoint section (line ~33)

**Method:** str_replace

**Find:**
```markdown
Ready to build.
```

---

## DO
```

**Replace with:**
```markdown
Ready to build.
```

---

## Build Razors

During implementation:

### Occam's Razor
- Remove until it breaks
- Every abstraction must justify itself

### Einstein's Razor
- Simple but not simpler
- All requirements met, nothing extra

---

## DO
```

---

### A9. P03-build.md — Update Genes Table (add G08-G10)

**Location:** Genes table (line ~67)

**Method:** str_replace

**Find:**
```markdown
| G07 Blocking | ⛔ where needed |
```

**Replace with:**
```markdown
| G07 Blocking | ⛔ where needed |
| G08 Occam's | Simplest sufficient structure |
| G09 Hume's | Proportional complexity |
| G10 Einstein's | Complete but not bloated |
```

---

### A10. P04-deliver.md — Add Genetic Validation + Feedback Razors

**Location:** After PRE-ACTION, before DO (line ~15)

**Method:** str_replace

**Find:**
```markdown
- [ ] Validation passed

---

## DO
```

**Replace with:**
```markdown
- [ ] Validation passed

---

## Genetic Validation

Before packaging, verify genes G01-G10:

| Gene | Check |
|------|-------|
| G01-G07 | Core genes present |
| G08 Occam's | No unused sections |
| G09 Hume's | Complexity matches task |
| G10 Einstein's | Complete but not bloated |

---

## Feedback Razors

When receiving feedback, apply Hanlon's:
- Questions = seeking clarity
- Changes = iteration, not criticism

---

## DO
```

---

### A11. P04-deliver.md — Update Blocking Rules to Options

**Location:** Lines ~142-148

**Method:** str_replace

**Find:**
```markdown
## ⛔ BLOCKING RULES

1. Do NOT package without Diff Report confirmation
2. Do NOT skip NEVER DEGRADE check
3. Do NOT deliver if validation failed
4. Valid confirmations: да, yes, ок, подтверждаю, го, погнали, do it, confirm, approved
```

**Replace with:**
```markdown
## ⛔ BLOCKING: Options

Present at this point:

```
🟡 P04-deliver · ⛔ waiting-confirm
NEXT: confirm → deliver

Options:
1 → Deliver
2 → Test first (→ test-architect)
3 → Edit
```

| Input | Action |
|-------|--------|
| 1, да, deliver | Package and deliver |
| 2, test, тест | Route to test-architect |
| 3, edit, правки | Back to P03-build |

### Rules
1. Do NOT package without Diff Report confirmation
2. Do NOT skip NEVER DEGRADE check
3. Do NOT deliver if validation failed
```

---

### A12. NEW FILE: reference/cognitive-razors.md

**Method:** create_file (new file, doesn't replace anything)

**Content:** Full razors framework (~350 lines from razors-plan.md)

---

### A13. reference/anchor-format.md — Add Options section

**Location:** After NEXT Instruction section (line ~93)

**Method:** str_replace

**Find:**
```markdown
NEXT: user confirms → package and deliver
NEXT: END
```

---

## Examples
```

**Replace with:**
```markdown
NEXT: user confirms → package and deliver
NEXT: END
```

---

## Options (at ⛔ points only)

```
Options:
1 → [primary action] (→ [next protocol])
2 → [alternative]
3 → [cancel/back]
```

### Standard Sets

| Point | Options |
|-------|---------|
| P02-plan | 1-Confirm, 2-Edit, 3-Cancel |
| P04-deliver | 1-Deliver, 2-Test, 3-Edit |

### User Input

| Input | Interpretation |
|-------|----------------|
| 1, 2, 3 | Select option |
| confirm, да | Option 1 |
| edit, правки | Option 2 |
| cancel, отмена | Option 3 |

---

## Examples
```

---

### A14. reference/templates.md — Add Genetic Markers

**Location:** After Anchor section in template (line ~78)

**Method:** str_replace

**Find:**
```markdown
## Anchor

```
⚙️ {name} v{X.Y.Z} · {status}
{session} | NEXT: {action}
```

*v{X.Y.Z}*
```
```

**Replace with:**
```markdown
## Anchor

```
{session} {name} · {status}
NEXT: {action}
```

---

## Design Principles

**G08 Occam's:** {why this is simplest structure}
**G09 Hume's:** Task = {complexity}, Implementation = {matching}
**G10 Einstein's:** Requirements: {X/X met}
```
```

---

### A15. Version Footers — Remove from ALL files

**Files:** All .md in protocols/, reference/, root

**Method:** str_replace for each file

**Find pattern:** `*...*` at end of file (e.g., `*P01-init | skill-architect v4.0.0*`)

**Replace with:** (empty — delete the line)

---

### A16. CHANGELOG — Add v4.3.0

**Location:** Top of file, after header

**Method:** str_replace

---

### A17. MANIFEST — Update version

**Method:** str_replace version number and date

---

### A18. docs/v4.3.0/ — Create new directory

**Method:** mkdir + create_file for 3 docs

---

## NEVER DEGRADE Check

### Content Verification

| File | Critical Content | Must Exist After Update |
|------|-----------------|------------------------|
| P04-deliver.md | `zip -r skill-name-vX.Y.Z.skill` | ✅ |
| P04-deliver.md | `cp ... /mnt/user-data/outputs/` | ✅ |
| P04-deliver.md | Auto-Test Suggestion section | ✅ |
| P04-deliver.md | Cross-Skill Routing section | ✅ |
| P04-deliver.md | Final Response template | ✅ |
| reference/packaging.md | Full file unchanged | ✅ |

### Metrics

| Metric | Baseline | Planned | Status |
|--------|----------|---------|--------|
| Commands | 7 | 7 | ✅ |
| Protocols | 5 | 5 | ✅ |
| Reference files | 9 | 10 | ✅ +1 |
| Scripts | 5 | 5 | ✅ |
| Genes | 7 | 10 | ✅ +3 |
| .skill packaging | ✅ | ✅ | ✅ preserved |

---

## Implementation Order

### Phase 1: Read Reference Files
1. Read reference/packaging.md completely
2. Read P04-deliver.md completely
3. Identify all delivery-related content to preserve

### Phase 2: Baseline Snapshot
```bash
cp -r /mnt/skills/user/skill-architect /home/claude/skill-architect-ORIGINAL
```

### Phase 3: Work Copy
```bash
cp -r /home/claude/skill-architect-ORIGINAL /home/claude/skill-architect-v4.3.0
```

### Phase 4: Apply str_replace Changes
Order: SKILL.md → P01 → P02 → P03 → P04 → reference/anchor-format.md → reference/templates.md

### Phase 5: Create New File
- reference/cognitive-razors.md

### Phase 6: Remove Footers
- All .md files except CHANGELOG

### Phase 7: Update Documentation
- CHANGELOG, MANIFEST, README

### Phase 8: Create Version Docs
- docs/v4.3.0/DIFF, SCAN, LOGIC-TREE

### Phase 9: Validate
```bash
# Check .skill packaging preserved
grep -n "\.skill" /home/claude/skill-architect-v4.3.0/protocols/P04-deliver.md
grep -n "zip -r" /home/claude/skill-architect-v4.3.0/protocols/P04-deliver.md

# Check line counts (should increase, not decrease)
wc -l /home/claude/skill-architect-ORIGINAL/protocols/P04-deliver.md
wc -l /home/claude/skill-architect-v4.3.0/protocols/P04-deliver.md
```

### Phase 10: Package
```bash
cd /home/claude
zip -r skill-architect-v4.3.0.skill skill-architect-v4.3.0/
cp skill-architect-v4.3.0.skill /mnt/user-data/outputs/
# Use present_files tool
```

---

## Summary

| Category | Count |
|----------|-------|
| KEEP | 16 features + ALL packaging logic |
| REMOVE | Version footers + Confirmation Words section |
| ADD | 14 items via str_replace |
| New files | 1 (cognitive-razors.md) + 3 docs |

**Critical:** Use str_replace ONLY. Never rewrite files.

---

*Planning Document v4.3.0 — ADDITIVE ONLY*
