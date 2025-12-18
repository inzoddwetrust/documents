# SPECIFICATION: skill-architect v9.0.0 "Clean Slate"
# VERSION 3.0 — COMPLETE WITH INHERITANCE

**Purpose:** Self-contained specification for rebuilding skill-architect with ALL proven patterns preserved.

**For:** Claude Opus (new chat window)

**Created:** 2025-12-12

**Principle:** This document contains EVERYTHING. Build exactly what's specified.

---

# PART 1: MISSION AND CONSTRAINTS

## 1.1 Mission

Build skill-architect v9.0.0 — a meta-skill that:
1. Creates other skills
2. Transfers best practices to children (inheritance)
3. Validates quality at 9 levels
4. Prevents degradation

**CLEAN REBUILD from proven patterns.**

---

## 1.2 Language: ENGLISH ONLY

| Component | Language |
|-----------|----------|
| SKILL.md | English |
| README.md | English |
| All protocols | English |
| All reference files | English |
| All scripts | English |
| Commands | English |
| Skills created BY this skill | English |

**ZERO TOLERANCE for other languages.**

---

## 1.3 Platform Constraints

| Constraint | Value |
|------------|-------|
| SKILL.md max lines | 300 |
| SKILL.md target | 80-100 |
| Frontmatter keys | name + description ONLY |

**Valid frontmatter:**
```yaml
---
name: skill-name
description: "v1.0.0 | What it does. Triggers: a, b, c."
---
```

**FORBIDDEN keys:** version, ecosystem, type, author — break upload.

---

# PART 2: ARCHITECTURE

## 2.1 File Structure (Target: ~30 files)

```
skill-architect-v9.0.0/
│
├── SKILL.md                      ← 80-100 lines
├── README-skill-architect.md
├── CHANGELOG-skill-architect.md
├── MANIFEST.md
│
├── protocols/                    ← 5 files
│   ├── P00-router.md
│   ├── P01-init.md
│   ├── P02-plan.md              ← ⛔ BLOCKING
│   ├── P03-build.md             ← PRE-BUILD CHECKPOINT
│   └── P04-deliver.md           ← ⛔ BLOCKING + audit
│
├── reference/                    ← 10 files
│   ├── quality-gates.md         ← L1-L9 ALL layers
│   ├── templates.md             ← INHERITANCE (genes)
│   ├── session-indicator.md     ← + context management
│   ├── diff-format.md
│   ├── naming.md
│   ├── packaging.md             ← archive rules
│   ├── commands.md              ← SSOT for bash
│   ├── evaluations.md
│   ├── genetic-audit.md         ← inheritance verification
│   └── docs-system.md           ← documentation architecture
│
├── scripts/                      ← 5 files
│   ├── validate.sh              ← --degrade, --docs, --naming, --ssot
│   ├── audit.sh                 ← full + genetic
│   ├── generate-docs.sh
│   ├── package.sh
│   └── update-version.sh
│
└── docs/v9.0.0/                  ← 3 mandatory
    ├── DIFF-skill-architect-v9.0.0.md
    ├── LOGIC-TREE-skill-architect-v9.0.0.md
    └── SCAN-skill-architect-v9.0.0.md
```

---

## 2.2 Protocol Flow

```
[USER REQUEST]
      │
      ▼
   P01-init ─────────────── Activation + config
      │
      ▼
   P02-plan ⛔ ───────────── Planning + WAIT for "yes/go/proceed"
      │
      ▼
   P03-build ────────────── PRE-BUILD CHECKPOINT + create + validate
      │
      ▼
   P04-deliver ⛔ ────────── Package + deliver + simulation + audit
      │
      ▼
    [END]
```

---

# PART 3: COMPLETE FILE SPECIFICATIONS

## 3.1 SKILL.md (80-100 lines)

```markdown
---
name: skill-architect
description: "v9.0.0 | Protocol-driven skill creation with inheritance. Triggers: create skill, update, refactor, checkup."
---

# Skill Architect v9.0.0

Lean skill creation with 5-step protocol flow and quality inheritance.

---

## Flow

```
P01-init → P02-plan ⛔ → P03-build → P04-deliver ⛔
```

| Protocol | Purpose | Blocking |
|----------|---------|----------|
| P01-init | Activation + config | |
| P02-plan | Planning + confirmation | ⛔ |
| P03-build | PRE-BUILD + create + validate | |
| P04-deliver | Package + deliver + audit | ⛔ |

---

## ⛔ Critical Rules

| # | Rule | Validation |
|---|------|------------|
| 1 | SKILL.md = English | validate.sh |
| 2 | SKILL.md < 300 lines | validate.sh |
| 3 | Frontmatter: name + description only | validate.sh |
| 4 | README-{name}.md required | validate.sh |
| 5 | Explicit confirmation required | P02 |
| 6 | NEVER DEGRADE | validate.sh --degrade |
| 7 | Inheritance (genes to children) | templates.md |

---

## ⛔ First Step

Always read protocol before action:
```
view → protocols/P00-router.md
```

---

## Commands

| Command | Action |
|---------|--------|
| create skill: [purpose] | New skill |
| update: [changes] | Modify existing |
| refactor | Restructure |
| checkup | Full audit |

---

## Confirmation

| ✅ Valid | ❌ Invalid |
|----------|------------|
| yes, go, proceed | ok, got it, understood |

---

## Context Anchor

End EVERY response:
```
⚙️ skill-architect v9.0.0 · [protocol] · [status]
[session-indicator]
```

Session: 🟢 fresh | 🟡 mid | 🔴 long

---

*v9.0.0 "Clean Slate"*
```

---

## 3.2 protocols/P00-router.md

```markdown
# P00: Router

State machine for navigation.

---

## Flow

```
[START]
    │
    ▼
  P01-init ────────── activation + config
    │
    ▼
  P02-plan ⛔ ─────── planning + confirmation
    │
    ▼
  P03-build ───────── PRE-BUILD + create + validate
    │
    ▼
  P04-deliver ⛔ ──── package + deliver + audit
    │
    ▼
  [END]
```

---

## Decision Table

| State | User Input | Next |
|-------|------------|------|
| None | skill request | P01-init |
| P01 done | config complete | P02-plan |
| P02 done | "yes/go/proceed" | P03-build |
| P02 done | question | Stay P02 |
| P03 done | validation pass | P04-deliver |
| P04 done | "audit" | Run audit |
| P04 done | "skip" | END |
| Any | "checkup" | P04 audit |

---

## Blocking Points

| Point | Valid | Invalid |
|-------|-------|---------|
| P02 → P03 | "yes", "go", "proceed" | "ok", "got it" |
| P04 → END | User decision | — |

---

## Recovery

1. Check /home/claude/ for artifacts
2. Check /mnt/user-data/outputs/ for deliverables
3. Ask: "Where were we?"
4. Resume from last confirmed state

---

*P00-router.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.3 protocols/P01-init.md

```markdown
# P01: Init

Activation and configuration.

---

## Trigger

Keywords: create skill, update, refactor, checkup

---

## Steps

### 1. Quick Response

```
Skill Architect v9.0.0
```

### 2. Determine Intent

| User provides | Action |
|---------------|--------|
| Clear purpose | → P02-plan |
| Unclear | Ask: "Purpose?" |

### 3. Gather Config (if needed)

One question at a time:
```
What does it do?
```

### 4. Confirm

```
Got it: skill for [purpose]
→ Planning
```

---

## Output

Ready for P02-plan

---

## Next

→ P02-plan (always)

---

*P01-init.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.4 protocols/P02-plan.md

```markdown
# P02: Plan

Planning document with explicit confirmation.

---

## ════════════════════════════════════════════════
## ⛔ BLOCKING — EXPLICIT CONFIRMATION REQUIRED
## ════════════════════════════════════════════════

| ✅ Valid | ❌ Invalid |
|----------|------------|
| yes, go, proceed | ok, got it, understood |

---

## Steps

### 1. Create Planning Document

```markdown
# [Skill]: Plan v0.0.0 → v1.0.0

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md | English, < 300 lines |
| Frontmatter | name + description only |
| Inheritance | Must include genes from templates.md |

## Context

[Why this change]

## Changes

### Add
- [items]

### Change
- [items]

### Remove
- [items] — NEVER DEGRADE check

### Keep
- [items]

## Inherited Genes

| Gene | Source | Included |
|------|--------|----------|
| Purpose Block | templates.md | □ |
| Context Anchor | templates.md | □ |
| Session Indicator | templates.md | □ |
| Protocol-First | templates.md | □ |

## Risks

| Risk | Mitigation |
|------|------------|

---

**Confirm:** "yes", "go", "proceed"
```

### 2. Save to /mnt/user-data/outputs/

### 3. WAIT for confirmation

---

## Confirmation Handling

| User says | Action |
|-----------|--------|
| "yes/go/proceed" | → P03-build |
| Question | Answer, re-ask |
| "ok/got it" | ❌ Invalid, request explicit |

---

## Next

→ P03-build (only after valid confirmation)

---

*P02-plan.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.5 protocols/P03-build.md

```markdown
# P03: Build

PRE-BUILD CHECKPOINT + create + validate.

---

## Trigger

P02-plan confirmed with "yes/go/proceed"

---

## ════════════════════════════════════════════════
## ⛔ PRE-BUILD CHECKPOINT — MANDATORY
## ════════════════════════════════════════════════

**BEFORE any file creation, verify:**

```
□ SKILL.md will be English
□ SKILL.md will be < 300 lines
□ README will be English
□ Frontmatter: name + description only
□ Inherited genes included (from templates.md)
```

**Trigger:** After web search, long conversation, any doubt.

**Action:** Re-read reference/templates.md to confirm genes.

---

## Steps

### 1. PRE-BUILD CHECKPOINT

Run the checklist above. Log confirmation:
```
PRE-BUILD: ✅ Verified
```

### 2. Create Files

Per plan:
- New skill → create in /home/claude/
- Update → copy, modify
- Log deviations

### 3. Validate Immediately

```bash
bash scripts/validate.sh /path/to/skill
```

| Result | Action |
|--------|--------|
| PASS | → P04-deliver |
| FAIL | Fix, re-validate |

### 4. NEVER DEGRADE Reminder

- Don't remove working functionality
- Don't replace specific with abstract
- When in doubt, keep both

---

## Output

- Files created in /home/claude/
- Validation passed
- Ready for delivery

---

## Next

→ P04-deliver (on validation pass)

---

*P03-build.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.6 protocols/P04-deliver.md

```markdown
# P04: Deliver

Package, deliver, and optional audit.

---

## ════════════════════════════════════════════════
## ⛔ BLOCKING — WAIT FOR USER AFTER DELIVERY
## ════════════════════════════════════════════════

---

## Steps

### 1. NEVER DEGRADE Check (updates only)

```bash
bash scripts/validate.sh --degrade /old /new
```

| Result | Action |
|--------|--------|
| PASS | Continue |
| FAIL | ⛔ STOP, restore content |

### 2. Create Diff Report

Per reference/diff-format.md

### 3. Package Skill

```bash
cd /home/claude
zip -r skill-name-vX.Y.Z.skill skill-name-vX.Y.Z/

# ⛔ VERIFY before delivery:
file skill-name-vX.Y.Z.skill
# Must show: "Zip archive data"

cp *.skill /mnt/user-data/outputs/
```

### 4. Generate Docs

```bash
bash scripts/generate-docs.sh /path X.Y.Z
```

### 5. Package Docs

```bash
zip -r skill-name-vX.Y.Z-docs.zip docs/vX.Y.Z/
cp *-docs.zip /mnt/user-data/outputs/
```

### 6. Deliver

```markdown
## Delivery Complete

| Item | File |
|------|------|
| Skill | [link] |
| Docs | [link] |

Version: vX.Y.Z

---

Run audit? "yes" / "skip"
```

---

## Simulation (if requested)

### Load Skill

```bash
cat SKILL.md | head -20
ls reference/ protocols/ scripts/
```

### Check Activation

```
□ Frontmatter valid
□ Triggers listed
□ Version matches
```

### Check Protocol Flow

```
□ All protocols exist
□ Next pointers valid
□ No circular refs
```

### Check Cross-References

```bash
grep -r "P0[0-9]" protocols/
```

### Check Versions

```bash
grep -h "skill-name v" *.md **/*.md | grep -oP 'v\d+\.\d+\.\d+' | sort | uniq -c
```

### Generate Report

```
═══════════════════════════════════════
SIMULATION REPORT
═══════════════════════════════════════

Skill: [name] v[version]

ACTIVATION: ✅/❌
FLOW: ✅/❌
CROSS-REFS: ✅/❌
VERSIONS: ✅/❌

VERDICT: PASS / FAIL
═══════════════════════════════════════
```

---

## Audit (if "checkup" command)

```bash
bash scripts/audit.sh /path
```

---

## Next

| User says | Action |
|-----------|--------|
| "yes/audit" | Run audit → END |
| "skip" | END |

---

*P04-deliver.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.7 reference/quality-gates.md

```markdown
# Quality Gates

L1-L9 validation layers.

---

## L1: Structure

| Check | Pass |
|-------|------|
| SKILL.md exists | ✅ |
| README-{name}.md exists | ✅ |
| SKILL.md < 300 lines | ✅ |
| Frontmatter: name + description | ✅ |
| Body in English | ✅ |

---

## L2: Content

| Check | Pass |
|-------|------|
| Purpose section present | ✅ |
| Triggers in description | ✅ |
| Version in description (vX.Y.Z) | ✅ |
| Context anchor format | ✅ |

---

## L3: Logic

| Check | Pass |
|-------|------|
| Clear state machine | ✅ |
| Blocking points marked ⛔ | ✅ |
| No circular dependencies | ✅ |
| Recovery path defined | ✅ |

---

## L4: Naming

| Check | Pass |
|-------|------|
| Folder: kebab-case | ✅ |
| Files: kebab-case.ext | ✅ |
| Version: vX.Y.Z (semver) | ✅ |

---

## L5: Integration

| Check | Pass |
|-------|------|
| MANIFEST.md if reference/ exists | ✅ |
| Scripts executable | ✅ |
| Protocols numbered P0X | ✅ |
| Footer versions synced | ✅ |

---

## L6: Testing

| Check | Pass |
|-------|------|
| Primary flow works | ✅ |
| Edge cases handled | ✅ |
| Error messages clear | ✅ |

---

## L7: Knowledge Redundancy ⭐ CRITICAL

| Check | Pass | Fail |
|-------|------|------|
| No concept explanations | ✅ | Has "what is X" sections |
| No standard pattern tutorials | ✅ | Full XML/YAML templates |
| Tables over prose for rules | ✅ | Verbose paragraphs |

**Quick Test:**
> "Delete this section. Would skill still work?"
> YES = redundant, delete
> NO = keep

**LLM-Native (safe to remove):**
- General concepts (what is API, REST)
- Standard patterns (OWASP, design patterns)
- Common formats (JSON/YAML structure)

**Skill-Specific (keep):**
- Custom workflows, state machines
- Blocking points, platform constraints
- Naming conventions specific to skill

**Redundancy Score:**

| Score | Verdict |
|-------|---------|
| 0-10% | ✅ Lean |
| 10-30% | 🟡 Review |
| 30%+ | 🔴 Prune required |

---

## L8: Version Integrity

| Check | Pass |
|-------|------|
| Main version in description | ✅ |
| Header version matches | ✅ |
| Footer versions synced | ✅ |
| MANIFEST version matches | ✅ |

**Quick Test:**
```bash
grep -r "skill-name v" . --include="*.md" | grep -oP 'v\d+\.\d+\.\d+' | sort | uniq
# Should show ONE version only
```

---

## L9: Documentation

| Check | Pass |
|-------|------|
| README-{skill-name}.md exists | ✅ |
| CHANGELOG-{skill-name}.md exists | ✅ |
| docs/vX.Y.Z/ exists | ✅ |
| DIFF document present | ✅ |
| LOGIC-TREE present | ✅ |
| SCAN document present | ✅ |
| Naming convention followed | ✅ |

---

## Validation Commands

```bash
bash scripts/validate.sh /path           # L1-L6
bash scripts/validate.sh --degrade /a /b # NEVER DEGRADE
bash scripts/validate.sh --docs /path    # L9
bash scripts/validate.sh --naming /path  # L4
bash scripts/validate.sh --ssot /path    # SSOT check
bash scripts/audit.sh /path              # L1-L9 + genetic
```

---

*quality-gates.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.8 reference/templates.md ⭐ INHERITANCE

```markdown
# Templates

Skill creation templates with INHERITANCE.

---

## ⛔ Frontmatter (MANDATORY)

**Allowed keys ONLY:**

| Key | Required |
|-----|----------|
| name | ✅ |
| description | ✅ |

**Format:**
```yaml
---
name: my-skill
description: "v1.0.0 | What it does. Triggers: a, b, c."
---
```

**❌ FORBIDDEN:** version, ecosystem, type, author

---

## ⛔ Purpose Block (MANDATORY) — GENE

Every skill MUST inherit:

```markdown
## Purpose

| Field | Value |
|-------|-------|
| serves | Who uses this (specific role/situation) |
| goal | What result (measurable) |
| method | How it achieves |
| success | How to verify |
```

---

## ⛔ Protocol-First (MANDATORY) — GENE

Skills with protocols MUST include:

```markdown
## ⛔ First Step

Read protocol before any action:
view → protocols/P00-router.md
```

| Rule | Reason |
|------|--------|
| Read before act | Prevents drift |
| Protocol determines action | Not user request directly |
| State machine is law | Skip = broken skill |

---

## ⛔ Context Anchor (MANDATORY) — GENE

Every response ends with:

```
⚙️ [skill-name] v[X.Y.Z] · [protocol] · [status]
[session-indicator]
```

Session indicator: 🟢 fresh | 🟡 mid | 🔴 long

---

## Template Types

| Type | Keywords | Process |
|------|----------|---------|
| Analysis | analyze, review | Gather → Analyze → Report |
| Content | create, write | Plan → Generate → Review |
| Data | process, extract | Validate → Transform → Verify |
| Code | build, develop | Design → Implement → Test |

Choose closest, adapt to domain. Claude knows these patterns natively.

---

## SKILL.md Template

```markdown
---
name: {skill-name}
description: "v1.0.0 | {purpose}. Triggers: {triggers}."
---

# {Skill Name} v1.0.0

{One line description}

---

## Purpose

| Field | Value |
|-------|-------|
| serves | {who} |
| goal | {what} |
| method | {how} |
| success | {verify} |

---

## ⛔ First Step

Read protocol before action:
view → protocols/P00-router.md

---

## Commands

| Command | Action |
|---------|--------|
| {cmd} | {action} |

---

## Context Anchor

⚙️ {skill-name} v1.0.0 · [status]
[session-indicator]

---

*v1.0.0*
```

---

## PRE-BUILD CHECKPOINT

**Trigger:** After web search, long conversation, any doubt.

**Action:** Re-read this file, verify genes will be included.

```
□ Purpose Block (serves/goal/method/success)
□ Protocol-First (if has protocols)
□ Context Anchor
□ Session Indicator
□ Frontmatter (name + description only)
□ English only
□ < 300 lines
```

---

## Lean Principle

**SKILL.md contains ONLY what Claude needs to execute.**

Everything else goes to README or docs/.

---

*templates.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.9 reference/session-indicator.md

```markdown
# Session Indicator + Context Management

Session state tracking and long conversation strategy.

---

## Session Indicator

| State | Display | Meaning |
|-------|---------|---------|
| Fresh | 🟢 fresh | Free to work |
| Mid | 🟡 mid | Keep focus |
| Long | 🔴 long | Risk of context loss |

---

## Detection Rules

### 🟢 fresh — ALL:

- < 10 user messages
- < 5 tool calls
- No large files loaded

### 🟡 mid — ANY:

- 10-30 user messages
- 5-15 tool calls
- 1-2 large files loaded

### 🔴 long — ANY:

- > 30 user messages
- > 15 tool calls
- > 2 large files loaded

---

## Context Anchor Format

```
⚙️ skill-architect v9.0.0 · [protocol] · [status]
🟢 fresh
```

---

## When to Compact

- Session indicator shows 🟡 or 🔴
- Session > 30 messages
- Before major phase (P03→P04)

---

## What to PRESERVE

- Current protocol (P0X)
- Blocking points status
- Skill name and version
- File paths (not contents)
- Key decisions
- Unresolved issues

---

## What to DROP

- Verbose intermediate outputs
- Full file contents
- Duplicate explanations
- Resolved discussions

---

## Recovery After Context Loss

1. Check /home/claude/ for artifacts
2. Check /mnt/user-data/outputs/ for deliverables
3. Ask: "Where were we?"
4. Resume from last confirmed state

---

*session-indicator.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.10 reference/commands.md (SSOT)

```markdown
# Commands Reference (SSOT)

Single source of truth for all bash commands.

---

## Packaging

```bash
cd /home/claude
zip -r [skill-name]-v[X.Y.Z].skill [skill-name]-v[X.Y.Z]/
cp [skill-name]-v[X.Y.Z].skill /mnt/user-data/outputs/

# ⛔ VERIFY:
file [skill-name]-v[X.Y.Z].skill
# Must show: "Zip archive data"
```

---

## Validation

```bash
bash scripts/validate.sh /path              # Full
bash scripts/validate.sh --degrade /old /new # NEVER DEGRADE
bash scripts/validate.sh --docs /path        # Docs naming
bash scripts/validate.sh --naming /path      # Structure
bash scripts/validate.sh --ssot /path        # Duplicates
```

---

## Audit

```bash
bash scripts/audit.sh /path                  # Full L1-L9
bash scripts/audit.sh --genetic /path        # Inheritance
```

---

## Documentation

```bash
bash scripts/generate-docs.sh /path X.Y.Z
bash scripts/update-version.sh /path X.Y.Z
```

---

## Diagnostics

```bash
# Version sync check
grep -r "skill-name v" . --include="*.md" | grep -oP 'v\d+\.\d+\.\d+' | sort | uniq

# Cross-reference check
grep -r "P0[0-9]" protocols/

# File structure
find . -name "*.md" -o -name "*.sh" | head -30
```

---

*commands.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.11 reference/genetic-audit.md

```markdown
# Genetic Audit

Inheritance verification — does skill pass genes to children?

---

## Purpose

Verify skill documents requirements for children that it follows itself.

---

## Core Genes (must inherit)

| Gene | Required | Source |
|------|----------|--------|
| Purpose Block | ✅ | templates.md |
| Frontmatter (name, description) | ✅ | templates.md |
| Context Anchor | ✅ | templates.md |
| Session Indicator | ✅ | templates.md |
| Blocking Points (if workflow) | ✅ | templates.md |
| Protocol-First (if protocols) | ✅ | templates.md |
| SKILL.md < 300 lines | ✅ | quality-gates.md |
| English only | ✅ | quality-gates.md |
| NEVER DEGRADE | ✅ | quality-gates.md |
| Validation before delivery | ✅ | P03-build.md |

---

## Audit Process

1. Extract parent genes (what skill-architect uses)
2. Extract child requirements (what it documents)
3. Build inheritance matrix
4. Identify lost genes
5. Report alignment %

---

## Redundancy Check

| Marker | Verdict |
|--------|---------|
| XML templates for known patterns | Redundant |
| Full YAML schemas with comments | Redundant |
| Explanations of concepts | Redundant |
| Step-by-step for obvious things | Redundant |

**Lean Pattern:**
```
BLOATED: "INoT is a technique where..." (50 lines)
LEAN: "INoT: agent debate. Claude knows." (1 line)
```

---

## Output

```
GENETIC AUDIT: [skill]

Genes: N found
Inherited: X%
Lost: [list]

REDUNDANCY:
LLM-native: X lines (Y%)
Skill-specific: Z lines
Verdict: LEAN / REVIEW / PRUNE
```

---

## Command

```bash
bash scripts/audit.sh --genetic /path
```

---

*genetic-audit.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.12 reference/packaging.md

```markdown
# Packaging

Skill archive structure and rules.

---

## Archive Structure

```
skill-name-vX.Y.Z.skill (ZIP)
└── skill-name-vX.Y.Z/
    ├── SKILL.md          (required)
    ├── README-{name}.md  (required)
    ├── MANIFEST.md       (if reference/ exists)
    ├── reference/
    ├── protocols/
    └── scripts/
```

---

## Rules

| Rule | Value |
|------|-------|
| Extension | .skill (ZIP format) |
| Root | Single folder, not loose files |
| Folder name | skill-name-vX.Y.Z |
| SKILL.md | Root of folder |
| Format | ZIP (not tar, not gzip) |

---

## ⛔ BEFORE PACKAGING — MANDATORY

```
□ Read this file
□ Folder name = skill-name-vX.Y.Z (with version!)
□ Files whitelist:
  ✓ SKILL.md, README-{name}.md
  ✓ MANIFEST.md (if reference/ exists)
  ✓ reference/, protocols/, scripts/
  ✗ NO: DIFF, PLAN, temp files
□ Command: zip -r (NOT tar)
```

---

## Commands

```bash
cd /home/claude
zip -r skill-name-vX.Y.Z.skill skill-name-vX.Y.Z/

# ⛔ VERIFY:
file skill-name-vX.Y.Z.skill
# Must: "Zip archive data"

unzip -t skill-name-vX.Y.Z.skill
# Must: "No errors detected"

cp *.skill /mnt/user-data/outputs/
```

---

*packaging.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.13 reference/diff-format.md

```markdown
# Diff Report Format

Standard format for version comparison.

---

## Template

```markdown
# Diff: v[OLD] → v[NEW]

**Skill:** [skill-name]
**Date:** [YYYY-MM-DD]

---

## Metrics

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| SKILL.md lines | X | Y | ±N |
| Total files | X | Y | ±N |

---

## Added

| Item | Description |
|------|-------------|

## Changed

| Item | Change |
|------|--------|

## Removed

| Item | Reason |
|------|--------|
| — | NEVER DEGRADE: nothing removed |

---

## NEVER DEGRADE: PASSED ✅

---

## Inherited Genes: VERIFIED ✅

---

*DIFF-{skill}-v{X.Y.Z}.md | {skill} v{X.Y.Z}*
```

---

*diff-format.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.14 reference/naming.md

```markdown
# Naming Conventions

---

## Folders

- kebab-case: `my-skill-name`
- With version: `my-skill-v1.0.0`

---

## Files

| Type | Format |
|------|--------|
| Core | SKILL.md, MANIFEST.md |
| Docs | README-{skill}.md, CHANGELOG-{skill}.md |
| Versioned | DIFF-{skill}-v{X.Y.Z}.md |
| Protocols | P00-router.md, P01-init.md |

---

## Versions

- Semver: v1.0.0, v2.1.3
- In description, not separate key
- No underscores (v1.0.0 not v1_0_0)

---

## Footer

```
*{filename} v{X.Y.Z} | {skill-name} v{X.Y.Z}*
```

---

*naming.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.15 reference/docs-system.md

```markdown
# Documentation System

Versioned documentation architecture.

---

## Structure

```
skill-name/
├── SKILL.md                  ← Claude (minimal)
├── README-{skill}.md         ← Human (full)
├── CHANGELOG-{skill}.md      ← History
├── MANIFEST.md               ← Index
└── docs/
    └── vX.Y.Z/
        ├── DIFF-{skill}-vX.Y.Z.md
        ├── LOGIC-TREE-{skill}-vX.Y.Z.md
        └── SCAN-{skill}-vX.Y.Z.md
```

---

## Document Types

| Document | Required | Content |
|----------|----------|---------|
| DIFF | ✅ | What changed |
| LOGIC-TREE | ✅ | Business logic flow |
| SCAN | ✅ | Validation results |

---

## Lean Principle

| Layer | Content | Audience |
|-------|---------|----------|
| SKILL.md | Minimal instructions | Claude |
| README | Full documentation | Human |
| docs/ | Version archives | Reference |

**Rule:** SKILL.md contains ONLY what Claude needs to execute.

---

*docs-system.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.16 reference/evaluations.md

```markdown
# Evaluations

Test scenarios for validation.

---

## E-001: Create Skill

**Input:** `create skill: API test generator`

**Expected:**
1. P01-init activation
2. P02-plan with confirmation ⛔
3. PRE-BUILD CHECKPOINT verified
4. P03-build + validation
5. P04-deliver ⛔

**Checks:**
- [ ] SKILL.md English, < 300 lines
- [ ] Inherited genes present
- [ ] Session indicator shown

---

## E-002: Update Skill

**Input:** `[attached .skill] + add error handling`

**Expected:**
1. NEVER DEGRADE check
2. Planning Document
3. PRE-BUILD CHECKPOINT
4. Diff Report

---

## E-003: Confirmation Rejection

**Input:** After plan — "ok got it"

**Expected:**
1. Reject as invalid
2. Request: "Please confirm with 'yes', 'go', or 'proceed'"

---

## E-004: Context Recovery

**Input:** Long session with web search

**Expected:**
1. PRE-BUILD CHECKPOINT triggered
2. Rules re-verified
3. No context drift

---

## E-005: Checkup Command

**Input:** `checkup`

**Expected:**
1. Run full audit (L1-L9)
2. Run genetic audit
3. Generate report

---

## E-006: Inheritance Verification

**Input:** Create any skill

**Expected:**
1. Purpose Block present (serves/goal/method/success)
2. Context Anchor present
3. Protocol-First if protocols exist
4. Session Indicator documented

---

## Results Template

```
| # | Scenario | Result |
|---|----------|--------|
| E-001 | Create | ✅/❌ |
| E-002 | Update | ✅/❌ |
| E-003 | Confirmation | ✅/❌ |
| E-004 | Context | ✅/❌ |
| E-005 | Checkup | ✅/❌ |
| E-006 | Inheritance | ✅/❌ |

Overall: X/6 passed
```

---

*evaluations.md v1.0.0 | skill-architect v9.0.0*
```

---

# PART 4: COMPLETE SCRIPTS

## 4.1 scripts/validate.sh

```bash
#!/bin/bash
# validate.sh — Comprehensive skill validation
# Usage: bash validate.sh <path>
#        bash validate.sh --degrade <old> <new>
#        bash validate.sh --docs <path>
#        bash validate.sh --naming <path>
#        bash validate.sh --ssot <path>
# v1.0.0 | skill-architect v9.0.0

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ERRORS=0
WARNINGS=0

log_pass() { echo -e "${GREEN}✅ $1${NC}"; }
log_fail() { echo -e "${RED}❌ $1${NC}"; ((ERRORS++)); }
log_warn() { echo -e "${YELLOW}⚠️ $1${NC}"; ((WARNINGS++)); }

echo "═══════════════════════════════════════════════════════"
echo "         SKILL VALIDATION v1.0.0"
echo "═══════════════════════════════════════════════════════"
echo ""

# ═══════════════════════════════════════════════════════════
# STANDARD VALIDATION (L1-L6)
# ═══════════════════════════════════════════════════════════

validate_standard() {
    local FOLDER="$1"
    
    echo "📁 Validating: $FOLDER"
    echo ""
    
    # L1: Structure
    echo "═══ L1: STRUCTURE ═══"
    
    # SKILL.md exists
    if [ -f "${FOLDER}/SKILL.md" ]; then
        log_pass "SKILL.md found"
    else
        log_fail "SKILL.md NOT FOUND"
        return
    fi
    
    # Line count < 300
    LINES=$(wc -l < "${FOLDER}/SKILL.md")
    if [ "$LINES" -lt 300 ]; then
        log_pass "Line count: $LINES (< 300)"
    else
        log_fail "Line count: $LINES (EXCEEDS 300!)"
    fi
    
    # English only
    BODY=$(awk '/^---$/{n++; next} n>=2' "${FOLDER}/SKILL.md")
    CYRILLIC=$(echo "$BODY" | grep -c '[а-яА-ЯёЁ]' 2>/dev/null || echo 0)
    if [ "$CYRILLIC" -gt 10 ]; then
        log_fail "SKILL.md contains non-English ($CYRILLIC Cyrillic chars)"
    else
        log_pass "SKILL.md is English"
    fi
    
    # README exists
    SKILL_NAME=$(grep "^name:" "${FOLDER}/SKILL.md" 2>/dev/null | sed 's/name: *//' | tr -d '"' | tr -d "'")
    if [ -f "${FOLDER}/README.md" ] || [ -f "${FOLDER}/README-${SKILL_NAME}.md" ]; then
        log_pass "README found"
    else
        log_fail "README NOT FOUND"
    fi
    echo ""
    
    # L2: Content
    echo "═══ L2: CONTENT ═══"
    
    # Frontmatter
    FIRST_LINE=$(head -1 "${FOLDER}/SKILL.md")
    if [ "$FIRST_LINE" = "---" ]; then
        log_pass "Frontmatter present"
        
        # Check name
        if grep -q "^name:" "${FOLDER}/SKILL.md"; then
            log_pass "name field present"
        else
            log_fail "name field missing"
        fi
        
        # Check description
        if grep -q "^description:" "${FOLDER}/SKILL.md"; then
            log_pass "description field present"
        else
            log_fail "description field missing"
        fi
        
        # Check for forbidden keys
        FORBIDDEN=$(sed -n '2,/^---$/p' "${FOLDER}/SKILL.md" | grep -E '^(version|ecosystem|type|author):' || true)
        if [ -n "$FORBIDDEN" ]; then
            log_fail "Forbidden frontmatter keys found"
        fi
    else
        log_fail "No frontmatter"
    fi
    
    # Version in description
    if grep -q 'description:.*v[0-9]\+\.[0-9]\+\.[0-9]\+' "${FOLDER}/SKILL.md"; then
        log_pass "Version in description"
    else
        log_warn "No version in description"
    fi
    echo ""
    
    # L3: Logic
    echo "═══ L3: LOGIC ═══"
    
    # Blocking points
    if grep -q "⛔\|BLOCKING" "${FOLDER}/SKILL.md"; then
        log_pass "Blocking points marked"
    else
        log_warn "No blocking points found"
    fi
    
    # Context anchor
    if grep -q "Context Anchor\|⚙️" "${FOLDER}/SKILL.md"; then
        log_pass "Context anchor present"
    else
        log_warn "No context anchor"
    fi
    echo ""
    
    # L4: Naming
    echo "═══ L4: NAMING ═══"
    
    # Folder naming
    BASENAME=$(basename "$FOLDER")
    if [[ "$BASENAME" =~ ^[a-z0-9-]+$ ]] || [[ "$BASENAME" =~ ^[a-z0-9-]+-v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        log_pass "Folder name: $BASENAME"
    else
        log_warn "Folder name not kebab-case: $BASENAME"
    fi
    echo ""
    
    # L5: Integration
    echo "═══ L5: INTEGRATION ═══"
    
    # MANIFEST if reference/ exists
    if [ -d "${FOLDER}/reference" ]; then
        if [ -f "${FOLDER}/MANIFEST.md" ]; then
            log_pass "MANIFEST.md found (required for reference/)"
        else
            log_fail "MANIFEST.md missing (required for reference/)"
        fi
    fi
    
    # Footer versions
    VERSIONS=$(grep -rh "$SKILL_NAME v" "$FOLDER" --include="*.md" 2>/dev/null | grep -oP 'v\d+\.\d+\.\d+' | sort | uniq | wc -l)
    if [ "$VERSIONS" -le 1 ]; then
        log_pass "Footer versions consistent"
    else
        log_warn "Multiple footer versions found"
    fi
    echo ""
}

# ═══════════════════════════════════════════════════════════
# NEVER DEGRADE VALIDATION
# ═══════════════════════════════════════════════════════════

validate_degrade() {
    local OLD="$1"
    local NEW="$2"
    
    echo "⛔ NEVER DEGRADE CHECK"
    echo "OLD: $OLD"
    echo "NEW: $NEW"
    echo ""
    
    if [ ! -d "$OLD" ] || [ ! -d "$NEW" ]; then
        log_fail "Both directories required"
        return
    fi
    
    # PHASE 1: File deletion
    echo "═══ PHASE 1: FILE DELETION ═══"
    for file in "$OLD"/*.md; do
        [ -f "$file" ] || continue
        basename=$(basename "$file")
        if [ ! -f "$NEW/$basename" ]; then
            log_fail "DELETED: $basename"
        fi
    done
    
    # PHASE 2: Content volume (>30% loss = violation)
    echo ""
    echo "═══ PHASE 2: CONTENT VOLUME ═══"
    if [ -f "$OLD/SKILL.md" ] && [ -f "$NEW/SKILL.md" ]; then
        old_lines=$(wc -l < "$OLD/SKILL.md")
        new_lines=$(wc -l < "$NEW/SKILL.md")
        
        if [ "$old_lines" -gt 0 ]; then
            ratio=$((new_lines * 100 / old_lines))
            if [ "$ratio" -lt 70 ]; then
                log_fail "SKILL.md: $old_lines → $new_lines (${ratio}% — >30% loss!)"
            else
                log_pass "SKILL.md: $old_lines → $new_lines (${ratio}%)"
            fi
        fi
    fi
    
    # PHASE 3: Key sections
    echo ""
    echo "═══ PHASE 3: KEY SECTIONS ═══"
    SECTIONS=("## Purpose" "## Flow" "## Commands" "Context Anchor")
    for section in "${SECTIONS[@]}"; do
        if grep -q "$section" "$OLD/SKILL.md" 2>/dev/null; then
            if ! grep -q "$section" "$NEW/SKILL.md" 2>/dev/null; then
                log_fail "SECTION REMOVED: '$section'"
            else
                log_pass "Section preserved: '$section'"
            fi
        fi
    done
}

# ═══════════════════════════════════════════════════════════
# DOCS VALIDATION (L9)
# ═══════════════════════════════════════════════════════════

validate_docs() {
    local FOLDER="$1"
    
    echo "═══ L9: DOCUMENTATION ═══"
    
    SKILL_NAME=$(grep "^name:" "${FOLDER}/SKILL.md" 2>/dev/null | sed 's/name: *//' | tr -d '"')
    
    # README naming
    if [ -f "${FOLDER}/README-${SKILL_NAME}.md" ]; then
        log_pass "README-${SKILL_NAME}.md"
    elif [ -f "${FOLDER}/README.md" ]; then
        log_warn "README.md (should be README-${SKILL_NAME}.md)"
    else
        log_fail "README missing"
    fi
    
    # CHANGELOG naming
    if [ -f "${FOLDER}/CHANGELOG-${SKILL_NAME}.md" ]; then
        log_pass "CHANGELOG-${SKILL_NAME}.md"
    else
        log_warn "CHANGELOG-${SKILL_NAME}.md missing"
    fi
    
    # docs/ folder
    if [ -d "${FOLDER}/docs" ]; then
        log_pass "docs/ folder exists"
        
        # Check for required docs
        for doc in DIFF LOGIC-TREE SCAN; do
            if find "${FOLDER}/docs" -name "${doc}*.md" | grep -q .; then
                log_pass "$doc document found"
            else
                log_warn "$doc document missing"
            fi
        done
    else
        log_warn "docs/ folder missing"
    fi
}

# ═══════════════════════════════════════════════════════════
# NAMING VALIDATION (L4)
# ═══════════════════════════════════════════════════════════

validate_naming() {
    local FOLDER="$1"
    
    echo "═══ L4: NAMING VALIDATION ═══"
    
    # Check folders
    for dir in protocols reference scripts; do
        if [ -d "${FOLDER}/${dir}" ]; then
            log_pass "${dir}/ exists"
        fi
    done
    
    # Check protocol files
    if [ -d "${FOLDER}/protocols" ]; then
        for proto in P00-router P01-init P02-plan P03-build P04-deliver; do
            if [ -f "${FOLDER}/protocols/${proto}.md" ]; then
                log_pass "${proto}.md"
            else
                log_warn "${proto}.md missing"
            fi
        done
    fi
}

# ═══════════════════════════════════════════════════════════
# SSOT VALIDATION
# ═══════════════════════════════════════════════════════════

validate_ssot() {
    local FOLDER="$1"
    
    echo "═══ SSOT CHECK ═══"
    
    # Check for duplicate definitions
    FRONTMATTER_DEFS=$(grep -rh "frontmatter\|Frontmatter" "$FOLDER" --include="*.md" 2>/dev/null | wc -l)
    if [ "$FRONTMATTER_DEFS" -gt 3 ]; then
        log_warn "Frontmatter defined in $FRONTMATTER_DEFS places"
    else
        log_pass "Frontmatter definitions OK"
    fi
    
    # Check version consistency
    VERSIONS=$(grep -rh "skill-architect v" "$FOLDER" --include="*.md" 2>/dev/null | grep -oP 'v\d+\.\d+\.\d+' | sort | uniq)
    VERSION_COUNT=$(echo "$VERSIONS" | wc -l)
    if [ "$VERSION_COUNT" -le 1 ]; then
        log_pass "Single version: $VERSIONS"
    else
        log_warn "Multiple versions: $VERSIONS"
    fi
}

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

case "${1:-}" in
    --degrade)
        validate_degrade "$2" "$3"
        ;;
    --docs)
        validate_docs "$2"
        ;;
    --naming)
        validate_naming "$2"
        ;;
    --ssot)
        validate_ssot "$2"
        ;;
    *)
        if [ -n "$1" ]; then
            validate_standard "$1"
        else
            echo "Usage:"
            echo "  bash validate.sh /path              # Full L1-L6"
            echo "  bash validate.sh --degrade /old /new # NEVER DEGRADE"
            echo "  bash validate.sh --docs /path        # L9 docs"
            echo "  bash validate.sh --naming /path      # L4 naming"
            echo "  bash validate.sh --ssot /path        # SSOT check"
            exit 1
        fi
        ;;
esac

# SUMMARY
echo ""
echo "═══════════════════════════════════════════════════════"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ VALIDATION PASSED${NC}"
    [ $WARNINGS -gt 0 ] && echo "Warnings: $WARNINGS"
    exit 0
else
    echo -e "${RED}❌ VALIDATION FAILED: $ERRORS error(s), $WARNINGS warning(s)${NC}"
    exit 1
fi
```

---

## 4.2 scripts/audit.sh

```bash
#!/bin/bash
# audit.sh — Full skill audit (L1-L9 + genetic)
# Usage: bash audit.sh <path>
#        bash audit.sh --genetic <path>
# v1.0.0 | skill-architect v9.0.0

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

INPUT="$1"
[ "$1" == "--genetic" ] && INPUT="$2"

echo "═══════════════════════════════════════════════════════"
echo "              FULL AUDIT v1.0.0"
echo "═══════════════════════════════════════════════════════"
echo ""

if [ -z "$INPUT" ] || [ ! -d "$INPUT" ]; then
    echo "Usage: bash audit.sh <skill-folder>"
    echo "       bash audit.sh --genetic <skill-folder>"
    exit 1
fi

# Run standard validation
bash "$(dirname "$0")/validate.sh" "$INPUT"
VALIDATE_RESULT=$?

# Run docs validation
bash "$(dirname "$0")/validate.sh" --docs "$INPUT"

# Run naming validation
bash "$(dirname "$0")/validate.sh" --naming "$INPUT"

# Run SSOT validation
bash "$(dirname "$0")/validate.sh" --ssot "$INPUT"

# Genetic audit if requested
if [ "$1" == "--genetic" ]; then
    echo ""
    echo -e "${BLUE}═══ GENETIC AUDIT ═══${NC}"
    echo ""
    
    INHERITED=0
    LOST=0
    
    # Check genes
    GENES=("Purpose" "Context Anchor" "Session" "First Step" "Blocking")
    
    for gene in "${GENES[@]}"; do
        if grep -q "$gene" "$INPUT/SKILL.md" 2>/dev/null; then
            echo -e "${GREEN}✅ Gene: $gene${NC}"
            ((INHERITED++))
        else
            echo -e "${RED}❌ Lost: $gene${NC}"
            ((LOST++))
        fi
    done
    
    TOTAL=${#GENES[@]}
    PERCENT=$((INHERITED * 100 / TOTAL))
    
    echo ""
    echo "Inheritance: $INHERITED/$TOTAL ($PERCENT%)"
    
    if [ "$PERCENT" -ge 80 ]; then
        echo -e "${GREEN}VERDICT: ALIGNED${NC}"
    else
        echo -e "${YELLOW}VERDICT: GAPS${NC}"
    fi
fi

# Extract info
SKILL_NAME=$(grep "^name:" "$INPUT/SKILL.md" 2>/dev/null | sed 's/name: *//' | tr -d '"')
VERSION=$(grep -oP 'v\d+\.\d+\.\d+' "$INPUT/SKILL.md" | head -1)

echo ""
echo "═══════════════════════════════════════════════════════"
echo "              AUDIT REPORT"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "Skill: $SKILL_NAME"
echo "Version: $VERSION"
echo "Date: $(date +%Y-%m-%d)"
echo ""

# Stats
FILE_COUNT=$(find "$INPUT" -name "*.md" -o -name "*.sh" | wc -l)
TOTAL_LINES=$(find "$INPUT" -name "*.md" -exec cat {} \; 2>/dev/null | wc -l)

echo "Files: $FILE_COUNT"
echo "Lines: $TOTAL_LINES"

echo ""
if [ $VALIDATE_RESULT -eq 0 ]; then
    echo -e "${GREEN}VERDICT: ✅ PASS${NC}"
else
    echo -e "${RED}VERDICT: ❌ FAIL${NC}"
fi
echo "═══════════════════════════════════════════════════════"
```

---

## 4.3 scripts/generate-docs.sh

```bash
#!/bin/bash
# generate-docs.sh — Generate version documentation
# Usage: bash generate-docs.sh <path> <version>
# v1.0.0 | skill-architect v9.0.0

set -e

INPUT="$1"
VERSION="$2"

if [ -z "$INPUT" ] || [ -z "$VERSION" ]; then
    echo "Usage: bash generate-docs.sh <skill-folder> <version>"
    exit 1
fi

SKILL_NAME=$(grep "^name:" "$INPUT/SKILL.md" 2>/dev/null | sed 's/name: *//' | tr -d '"')
DOCS_DIR="$INPUT/docs/v${VERSION}"

mkdir -p "$DOCS_DIR"

# DIFF
cat > "$DOCS_DIR/DIFF-${SKILL_NAME}-v${VERSION}.md" << EOF
# Diff: v0.0.0 → v${VERSION}

**Skill:** ${SKILL_NAME}
**Date:** $(date +%Y-%m-%d)

---

## Metrics

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| SKILL.md lines | 0 | TBD | — |
| Total files | 0 | TBD | — |

---

## Added

| Item | Description |
|------|-------------|
| All | Initial release |

---

## NEVER DEGRADE: N/A (new skill)

## Inherited Genes: VERIFIED ✅

---

*DIFF-${SKILL_NAME}-v${VERSION}.md | ${SKILL_NAME} v${VERSION}*
EOF

# LOGIC-TREE
cat > "$DOCS_DIR/LOGIC-TREE-${SKILL_NAME}-v${VERSION}.md" << EOF
# LOGIC-TREE: ${SKILL_NAME} v${VERSION}

Business logic flow.

---

## Main Flow

\`\`\`
[START]
    │
    ▼
[P01-init] ─────────── Activation
    │
    ▼
[P02-plan] ⛔ ───────── Planning + confirmation
    │
    ▼
[P03-build] ────────── PRE-BUILD + create + validate
    │
    ▼
[P04-deliver] ⛔ ────── Package + deliver + audit
    │
    ▼
[END]
\`\`\`

---

## Blocking Points

| Protocol | Gate | Requires |
|----------|------|----------|
| P02-plan | Confirmation | "yes/go/proceed" |
| P04-deliver | User decision | "audit" or "skip" |

---

## Quality Gates

| Gate | Check | Level |
|------|-------|-------|
| L1 | Structure | SKILL.md, README |
| L2 | Content | Purpose, triggers |
| L3 | Logic | State machine |
| L4 | Naming | kebab-case |
| L5 | Integration | MANIFEST |
| L6 | Testing | Flow works |
| L7 | Redundancy | No bloat |
| L8 | Versions | Sync |
| L9 | Docs | Naming |

---

## Inherited Genes

| Gene | Required |
|------|----------|
| Purpose Block | ✅ |
| Context Anchor | ✅ |
| Session Indicator | ✅ |
| Protocol-First | ✅ |
| NEVER DEGRADE | ✅ |

---

*LOGIC-TREE-${SKILL_NAME}-v${VERSION}.md | ${SKILL_NAME} v${VERSION}*
EOF

# SCAN
cat > "$DOCS_DIR/SCAN-${SKILL_NAME}-v${VERSION}.md" << EOF
# SCAN: ${SKILL_NAME} v${VERSION}

Validation results.

---

## Summary

| Level | Check | Result |
|-------|-------|--------|
| L1 | Structure | ☐ |
| L2 | Content | ☐ |
| L3 | Logic | ☐ |
| L4 | Naming | ☐ |
| L5 | Integration | ☐ |
| L6 | Testing | ☐ |
| L7 | Redundancy | ☐ |
| L8 | Versions | ☐ |
| L9 | Docs | ☐ |

## Genetic Audit

| Gene | Inherited |
|------|-----------|
| Purpose Block | ☐ |
| Context Anchor | ☐ |
| Protocol-First | ☐ |

**Status:** PENDING

---

*SCAN-${SKILL_NAME}-v${VERSION}.md | ${SKILL_NAME} v${VERSION}*
EOF

echo "✅ Generated docs in $DOCS_DIR"
echo "   - DIFF-${SKILL_NAME}-v${VERSION}.md"
echo "   - LOGIC-TREE-${SKILL_NAME}-v${VERSION}.md"
echo "   - SCAN-${SKILL_NAME}-v${VERSION}.md"
```

---

## 4.4 scripts/package.sh

```bash
#!/bin/bash
# package.sh — Package skill as .skill archive
# Usage: bash package.sh <skill-name> <version>
# v1.0.0 | skill-architect v9.0.0

set -e

NAME="$1"
VERSION="$2"

if [ -z "$NAME" ] || [ -z "$VERSION" ]; then
    echo "Usage: bash package.sh <skill-name> <version>"
    exit 1
fi

FOLDER="${NAME}-v${VERSION}"
ARCHIVE="${FOLDER}.skill"

# Rename if needed
if [ -d "$NAME" ] && [ ! -d "$FOLDER" ]; then
    cp -r "$NAME" "$FOLDER"
fi

# Create ZIP
zip -r "$ARCHIVE" "$FOLDER/"

# Verify
FILE_TYPE=$(file "$ARCHIVE")
if echo "$FILE_TYPE" | grep -q "Zip archive"; then
    echo "✅ Created: $ARCHIVE"
    echo "   Format: ZIP (valid)"
else
    echo "❌ ERROR: Not a valid ZIP"
    exit 1
fi
```

---

## 4.5 scripts/update-version.sh

```bash
#!/bin/bash
# update-version.sh — Sync all versions
# Usage: bash update-version.sh <path> <version>
# v1.0.0 | skill-architect v9.0.0

set -e

INPUT="$1"
VERSION="$2"

if [ -z "$INPUT" ] || [ -z "$VERSION" ]; then
    echo "Usage: bash update-version.sh <skill-folder> <version>"
    exit 1
fi

SKILL_NAME=$(grep "^name:" "$INPUT/SKILL.md" 2>/dev/null | sed 's/name: *//' | tr -d '"')

echo "Updating $SKILL_NAME to v$VERSION"

# Update footers
find "$INPUT" -name "*.md" -exec sed -i "s/${SKILL_NAME} v[0-9]\+\.[0-9]\+\.[0-9]\+/${SKILL_NAME} v${VERSION}/g" {} \;

# Verify
VERSIONS=$(grep -rh "$SKILL_NAME v" "$INPUT" --include="*.md" | grep -oP 'v\d+\.\d+\.\d+' | sort | uniq)
echo "Versions found: $VERSIONS"

echo "✅ Version update complete"
```

---

# PART 5: DIALOG EXAMPLES

## 5.1 Create Skill — Full Flow

**User:** `create skill: markdown linter`

**Claude (P01-init):**
```
Skill Architect v9.0.0

Got it: skill for markdown linting.

→ Planning

⚙️ skill-architect v9.0.0 · P01-init · complete
🟢 fresh
```

**Claude (P02-plan):**
```
# markdown-linter: Plan v0.0.0 → v1.0.0

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md | English, < 300 lines |
| Frontmatter | name + description only |
| Inheritance | Purpose, Anchor, Protocol-First |

## Context

New skill for linting markdown files.

## Changes

### Add
- SKILL.md with lint commands
- README-markdown-linter.md

### Inherited Genes

| Gene | Included |
|------|----------|
| Purpose Block (serves/goal/method/success) | ✅ |
| Context Anchor | ✅ |
| Session Indicator | ✅ |

---

**Confirm:** "yes", "go", "proceed"

⚙️ skill-architect v9.0.0 · P02-plan · awaiting confirmation
🟢 fresh
```

**User:** `ok sounds good`

**Claude (P02-plan — rejection):**
```
I need explicit confirmation to proceed.

Please reply with "yes", "go", or "proceed".

⚙️ skill-architect v9.0.0 · P02-plan · awaiting confirmation
🟢 fresh
```

**User:** `yes`

**Claude (P03-build):**
```
PRE-BUILD: ✅ Verified
- SKILL.md = English ✓
- < 300 lines ✓
- Genes included ✓

Building markdown-linter v1.0.0...

✅ SKILL.md created (52 lines)
✅ README-markdown-linter.md created
✅ Purpose Block included
✅ Context Anchor included

Running validation...
═══ L1: STRUCTURE ═══
✅ SKILL.md found
✅ Line count: 52 (< 300)
✅ SKILL.md is English
✅ README found

✅ VALIDATION PASSED

→ Delivery

⚙️ skill-architect v9.0.0 · P03-build · complete
🟢 fresh
```

**Claude (P04-deliver):**
```
## Delivery Complete

| Item | File |
|------|------|
| Skill | markdown-linter-v1.0.0.skill |
| Docs | markdown-linter-v1.0.0-docs.zip |

Version: v1.0.0
Inherited Genes: ✅ VERIFIED

---

Run audit? "yes" / "skip"

⚙️ skill-architect v9.0.0 · P04-deliver · awaiting decision
🟢 fresh
```

---

## 5.2 Checkup Command

**User:** `checkup`

**Claude:**
```
═══════════════════════════════════════════════════════
              FULL AUDIT v1.0.0
═══════════════════════════════════════════════════════

═══ L1: STRUCTURE ═══
✅ SKILL.md found
✅ Line count: 88 (< 300)
✅ SKILL.md is English
✅ README found

═══ L2: CONTENT ═══
✅ Frontmatter present
✅ name field present
✅ description field present
✅ Version in description

═══ L7: REDUNDANCY ═══
✅ No bloat detected

═══ GENETIC AUDIT ═══
✅ Gene: Purpose
✅ Gene: Context Anchor
✅ Gene: Session
✅ Gene: First Step
✅ Gene: Blocking

Inheritance: 5/5 (100%)
VERDICT: ALIGNED

═══════════════════════════════════════════════════════
              AUDIT REPORT
═══════════════════════════════════════════════════════

Skill: skill-architect
Version: v9.0.0
Files: 28
Lines: 2,100

VERDICT: ✅ PASS
═══════════════════════════════════════════════════════

⚙️ skill-architect v9.0.0 · P04-deliver · audit complete
🟡 mid
```

---

# PART 6: DELIVERABLES

When complete, deliver:

1. **skill-architect-v9.0.0.skill** — ZIP with:
   - SKILL.md (80-100 lines)
   - README-skill-architect.md
   - CHANGELOG-skill-architect.md
   - MANIFEST.md
   - protocols/ (5 files)
   - reference/ (10 files)
   - scripts/ (5 files)
   - docs/v9.0.0/ (3 files)

2. **skill-architect-v9.0.0-docs.zip**

3. **Diff Report** — comparison

---

# PART 7: SUCCESS CRITERIA

| Metric | Target |
|--------|--------|
| SKILL.md lines | 80-100 |
| Total files | ~30 |
| Language | English only |
| Protocols | 5 |
| Scripts | 5 |
| Reference | 10 |
| Quality layers | L1-L9 ALL |
| Inheritance | WORKING |

---

# PART 8: BUILD CHECKLIST

```
□ Create skill-architect-v9.0.0/
□ Write SKILL.md (80-100 lines, English)
□ Write protocols/ (5 files)
□ Write reference/ (10 files, including inheritance)
□ Write scripts/ (5 files with all modes)
□ Write README-skill-architect.md
□ Write CHANGELOG-skill-architect.md
□ Generate MANIFEST.md
□ Run: bash scripts/generate-docs.sh . 9.0.0
□ Run: bash scripts/validate.sh .
□ Run: bash scripts/audit.sh --genetic .
□ Verify: ALL PASS
□ Run: bash scripts/package.sh skill-architect 9.0.0
□ Deliver .skill and -docs.zip
```

---

# PART 9: CRITICAL REMINDERS

## What v8.7.0 → v9.0.0 v1/v2 Lost:

| Lost | Status |
|------|--------|
| Inheritance (genes) | ✅ RESTORED |
| L7-L9 quality layers | ✅ RESTORED |
| SSOT concept | ✅ RESTORED |
| Context management | ✅ RESTORED |
| PRE-BUILD CHECKPOINT | ✅ RESTORED |
| Simulation details | ✅ RESTORED |
| Commands reference | ✅ RESTORED |
| Genetic audit | ✅ RESTORED |
| --docs mode | ✅ RESTORED |
| --naming mode | ✅ RESTORED |
| Project mode | ❌ REMOVED (scope) |

## Anti-Patterns:

| ❌ Don't | ✅ Do |
|---------|------|
| Remove L7-L9 | Keep all 9 layers |
| Skip inheritance | Include genes |
| Skip PRE-BUILD | Always checkpoint |
| Simplify too much | Keep proven patterns |

---

*SPEC-skill-architect-v9.0.0-COMPLETE-V3.md | Self-contained specification with inheritance*
