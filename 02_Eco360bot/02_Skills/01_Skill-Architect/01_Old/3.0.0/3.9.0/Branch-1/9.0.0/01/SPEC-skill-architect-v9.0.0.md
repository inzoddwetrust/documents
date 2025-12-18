# Technical Specification: skill-architect v9.0.0 "Clean Slate"

**Purpose:** Complete rebuild of skill-architect from extracted knowledge.

**For:** Claude Opus (new chat window)

**Created:** 2025-12-12

---

## 🎯 MISSION

Build skill-architect v9.0.0 from scratch using proven patterns extracted from 18+ versions of evolution (v3.9.0 → v8.7.0).

**NOT a patch. NOT an update. A CLEAN REBUILD.**

---

## ⛔ CRITICAL CONSTRAINTS

### Language: ENGLISH ONLY

| Component | Language | Violation |
|-----------|----------|-----------|
| SKILL.md | English | ⛔ BLOCKING |
| README.md | English | ⛔ BLOCKING |
| All protocols | English | ⛔ BLOCKING |
| All reference files | English | ⛔ BLOCKING |
| All scripts | English | ⛔ BLOCKING |
| Commands | English | ⛔ BLOCKING |
| Output messages | English | ⛔ BLOCKING |
| Skills created BY skill-architect | English | ⛔ BLOCKING |

**ZERO tolerance for Russian, German, French, or ANY other language.**

---

### Platform Constraints

| Constraint | Value | Reason |
|------------|-------|--------|
| SKILL.md max lines | 300 | Platform limit |
| SKILL.md target | 80-100 lines | Lean principle |
| Frontmatter keys | name, description ONLY | Platform upload breaks with other keys |
| Version in description | Required | Can't use "version:" key |

**Frontmatter format:**
```yaml
---
name: skill-name
description: "v1.0.0 | What it does. Triggers: a, b, c."
---
```

**❌ INVALID (breaks upload):**
```yaml
---
name: skill-name
version: 1.0.0        # ❌ NOT ALLOWED
ecosystem: tools      # ❌ NOT ALLOWED
author: someone       # ❌ NOT ALLOWED
---
```

---

## 📐 ARCHITECTURE

### File Structure (Target: ~35 files)

```
skill-architect-v9.0.0/
│
├── SKILL.md                      ← Claude instructions (80-100 lines)
├── README-skill-architect.md     ← User documentation (English)
├── CHANGELOG-skill-architect.md  ← Cumulative history
├── MANIFEST.md                   ← File index with line counts
│
├── protocols/                    ← 5 protocol files
│   ├── P00-router.md            ← State machine, routing logic
│   ├── P01-init.md              ← Activation + configuration
│   ├── P02-plan.md              ← Planning ⛔ BLOCKING
│   ├── P03-build.md             ← Build + validation
│   └── P04-deliver.md           ← Delivery + audit ⛔ BLOCKING
│
├── reference/                    ← 8-10 reference files
│   ├── quality-gates.md         ← G1-G8 validation gates
│   ├── templates.md             ← All templates consolidated
│   ├── session-indicator.md     ← Context tracking (NEW)
│   ├── diff-format.md           ← Diff Report + Planning Document
│   ├── naming.md                ← Naming conventions
│   ├── project-mode.md          ← Project skill features
│   ├── evaluations.md           ← Test scenarios E-001 to E-008
│   └── evolution.md             ← History of patterns (optional)
│
├── scripts/                      ← 5 consolidated scripts
│   ├── validate.sh              ← All validations merged
│   ├── audit.sh                 ← Full audit (genetic + skill)
│   ├── generate-docs.sh         ← Documentation generation
│   ├── package.sh               ← Packaging logic
│   └── update-version.sh        ← Version sync
│
└── docs/                         ← Version archives
    └── v9.0.0/
        ├── DIFF-skill-architect-v9.0.0.md
        ├── LOGIC-TREE-skill-architect-v9.0.0.md   ← MANDATORY
        └── SCAN-skill-architect-v9.0.0.md
```

---

### Protocol Flow (5 protocols, 2 blocking points)

```
[USER REQUEST]
      │
      ▼
   P01-init ─────────────── "What are we doing?"
      │
      ▼
   P02-plan ⛔ ───────────── Planning + explicit confirmation
      │                      WAIT for "yes/go/proceed"
      ▼
   P03-build ────────────── Create + validate
      │
      ▼
   P04-deliver ⛔ ────────── Package + deliver + optional audit
      │                      WAIT for user decision
      ▼
    [END]
```

**Key changes from v8.7.0:**
- P05-simulation MERGED into P04-deliver (optional audit step)
- P06-audit MERGED into P04-deliver (on "checkup" command)
- Result: 6 protocols → 5 protocols

---

## 📝 SKILL.md SPECIFICATION

**Target:** 80-100 lines

```markdown
---
name: skill-architect
description: "v9.0.0 | Protocol-driven skill creation. Triggers: create skill, update, refactor, checkup."
---

# Skill Architect v9.0.0

Lean skill creation with 5-step protocol flow.

---

## Flow

```
P01-init → P02-plan ⛔ → P03-build → P04-deliver ⛔
```

| Protocol | Purpose | Blocking |
|----------|---------|----------|
| P01-init | Activation + config | |
| P02-plan | Planning + confirmation | ⛔ |
| P03-build | Create + validate | |
| P04-deliver | Package + deliver + audit | ⛔ |

---

## ⛔ Critical Rules

| # | Rule | Validation |
|---|------|------------|
| 1 | SKILL.md = English | validate.sh |
| 2 | SKILL.md < 300 lines | validate.sh |
| 3 | Frontmatter: name + description only | validate.sh |
| 4 | README-{name}.md required | validate.sh |
| 5 | Explicit confirmation required | Protocol P02 |
| 6 | NEVER DEGRADE | validate.sh |

---

## ⛔ First Step

Read protocol before any action:
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

End EVERY response with:
```
⚙️ skill-architect v9.0.0 · [protocol] · [status]
[session-indicator]
```

Session indicator: 🟢 fresh | 🟡 mid | 🔴 long

---

*v9.0.0 "Clean Slate" — rebuilt from knowledge extraction*
```

---

## 🔄 PROTOCOL SPECIFICATIONS

### P00-router.md

**Purpose:** State machine and routing logic.

**Content:**
```markdown
# P00: Router

Meta-protocol for navigation.

---

## State Machine

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
  P03-build ───────── create + validate
    │
    ▼
  P04-deliver ⛔ ──── package + deliver + audit
    │
    ▼
  [END]
```

---

## Decision Table

| Current State | User Input | Next State |
|---------------|------------|------------|
| None | skill request | P01-init |
| P01 complete | config done | P02-plan |
| P02 complete | "yes/go/proceed" | P03-build |
| P02 complete | question | Stay P02 |
| P03 complete | validation pass | P04-deliver |
| P04 complete | "audit" | Run audit in P04 |
| P04 complete | "skip" | END |
| Any | "checkup" | P04 audit section |

---

## Blocking Points

| Point | Requires | Invalid |
|-------|----------|---------|
| P02 → P03 | "yes", "go", "proceed" | "ok", "got it" |
| P04 → END | User decision | — |

---

## Recovery

After context loss:
1. Re-read SKILL.md
2. Check last confirmed state
3. Resume from there

---

*P00-router.md v1.0.0 | skill-architect v9.0.0*
```

---

### P01-init.md

**Purpose:** Activation and configuration in one step.

**Key behaviors:**
- Quick response with version
- Determine intent (create/update/refactor/checkup)
- Gather configuration if needed
- ONE question at a time

**Output:** Ready for P02-plan

---

### P02-plan.md ⛔ BLOCKING

**Purpose:** Planning document with explicit confirmation.

**Key behaviors:**
- Create Planning Document
- Include: Constraints, Context, Changes (Add/Change/Remove/Keep), Risks
- Save to outputs
- WAIT for explicit "yes/go/proceed"
- Reject "ok", "got it", "understood"

**Planning Document template:**
```markdown
# [Skill Name]: Plan vX.X.X → vY.Y.Y

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md | English, < 300 lines |
| README.md | English |
| Frontmatter | name + description only |

## Context

[Why this change is needed]

## Changes

### Add
- [item]

### Change
- [item]

### Remove
- [item] — NEVER DEGRADE check required

### Keep
- [item]

## Risks

| Risk | Mitigation |
|------|------------|
| | |

## Chat Verification

[All discussed items confirmed]

---

**Confirm:** "yes", "go", "proceed"
```

---

### P03-build.md

**Purpose:** Create files and validate.

**Key behaviors:**
- Follow plan exactly
- Log any deviations
- Run validate.sh immediately
- Fix issues and re-validate
- NEVER DEGRADE reminder

**Validation checklist:**
```
□ SKILL.md exists
□ SKILL.md < 300 lines
□ SKILL.md = English
□ README-{name}.md exists
□ Frontmatter valid
□ Version in description
```

---

### P04-deliver.md ⛔ BLOCKING

**Purpose:** Package, deliver, and optional audit.

**Phases:**

1. **NEVER DEGRADE Check** (updates only)
   ```bash
   bash scripts/validate.sh --degrade /old /new
   ```

2. **Create Diff Report**
   - Metrics (before/after)
   - Added/Changed/Removed
   - NEVER DEGRADE status

3. **Package Skill**
   ```bash
   bash scripts/package.sh skill-name X.Y.Z
   ```

4. **Generate Docs**
   ```bash
   bash scripts/generate-docs.sh . X.Y.Z
   ```

5. **Deliver**
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

6. **Optional Audit** (if user says "yes" or "checkup" command)
   - Load and verify SKILL.md
   - Check protocol flow
   - Verify cross-references
   - Check version sync
   - Generate audit report

---

## 📊 SESSION INDICATOR SPECIFICATION

**Purpose:** Replace unreliable token counter with honest session state tracking.

**Format:**
```
🟢 fresh | 🟡 mid | 🔴 long
```

### Detection Rules

**🟢 fresh** — ALL conditions met:
- < 10 user messages
- < 5 tool calls
- No files > 500 lines loaded
- No large artifacts generated

**🟡 mid** — ANY condition met:
- 10-30 user messages
- 5-15 tool calls
- 1-2 large files loaded
- 1-2 large artifacts generated

**🔴 long** — ANY condition met:
- > 30 user messages
- > 15 tool calls
- > 2 large files loaded
- > 2 large artifacts
- Multiple complex code generations

### Aggravating Factors (push ONE level higher)

- File > 1000 lines loaded
- Multiple skill files read
- Heavy debugging cycles
- Images uploaded

### Behavior by State

| State | Action |
|-------|--------|
| 🟢 fresh | Work freely |
| 🟡 mid | Keep responses focused |
| 🔴 long | Suggest narrowing focus or new chat |

---

## ✅ QUALITY GATES SPECIFICATION

### Mandatory Gates (BLOCKING)

| Gate | Check | Script |
|------|-------|--------|
| G1 | SKILL.md exists | validate.sh |
| G2 | SKILL.md < 300 lines | validate.sh |
| G3 | SKILL.md = English only | validate.sh |
| G4 | Frontmatter: name + description only | validate.sh |
| G5 | README-{name}.md exists | validate.sh |
| G6 | Explicit confirmation before build | Protocol P02 |
| G7 | NEVER DEGRADE check | validate.sh --degrade |

### Warning Gates (NON-BLOCKING)

| Gate | Check |
|------|-------|
| G8 | MANIFEST.md current |
| G9 | Footer versions synced |
| G10 | No knowledge redundancy |

---

## 📄 DOCUMENTATION SPECIFICATION

### Mandatory Documents (3 types)

| Document | Purpose | Required |
|----------|---------|----------|
| DIFF-{skill}-v{X.Y.Z}.md | What changed | ✅ |
| LOGIC-TREE-{skill}-v{X.Y.Z}.md | Business logic flow | ✅ |
| SCAN-{skill}-v{X.Y.Z}.md | Validation results | ✅ |

### LOGIC-TREE Template

```markdown
# LOGIC-TREE: {skill-name} v{X.Y.Z}

Business logic flow visualization.

---

## Main Flow

```
[START]
    │
    ▼
[STEP 1] ─────────── description
    │
    ▼
[DECISION?] ──► YES ──► [ACTION A]
    │
    ▼ NO
[ACTION B]
    │
    ▼
[END]
```

---

## Blocking Points

| Protocol | Gate | Requires |
|----------|------|----------|
| P02-plan | Confirmation | "yes/go/proceed" |
| P04-deliver | User decision | "audit" or "skip" |

---

## State Transitions

| From | Condition | To |
|------|-----------|-----|
| P01 | Config complete | P02 |
| P02 | Confirmed | P03 |
| P03 | Validation pass | P04 |
| P04 | User skip | END |

---

*LOGIC-TREE-{skill-name}-v{X.Y.Z}.md | {skill-name} v{X.Y.Z}*
```

---

## 🔧 SCRIPTS SPECIFICATION

### validate.sh (consolidated)

**Merges:** validate-skill.sh, validate-degrade.sh, validate-docs.sh, validate-naming.sh, ssot-check.sh

**Usage:**
```bash
bash scripts/validate.sh /path/to/skill           # Full validation
bash scripts/validate.sh --degrade /old /new      # NEVER DEGRADE check
bash scripts/validate.sh --docs /path             # Docs only
bash scripts/validate.sh --naming /path           # Naming only
```

**Checks:**
- G1-G7 gates
- File structure
- Frontmatter validation
- English-only content
- Line count
- NEVER DEGRADE (--degrade mode)

---

### audit.sh (consolidated)

**Merges:** audit-skill.sh, audit-project.sh, genetic-audit.sh

**Usage:**
```bash
bash scripts/audit.sh /path/to/skill
```

**Output:**
```
═══════════════════════════════════════
AUDIT REPORT: {skill-name} v{X.Y.Z}
═══════════════════════════════════════

STRUCTURE ────────────────────────────
[results]

CONTENT ──────────────────────────────
[results]

VERSIONS ─────────────────────────────
[results]

ISSUES ───────────────────────────────
🔴 Critical: [N]
🟡 Medium: [N]
🟢 Minor: [N]

VERDICT: PASS / FAIL
═══════════════════════════════════════
```

---

### generate-docs.sh

**Usage:**
```bash
bash scripts/generate-docs.sh /path X.Y.Z
bash scripts/generate-docs.sh /path X.Y.Z update /prev-docs
```

**Creates:**
- DIFF-{skill}-v{X.Y.Z}.md
- LOGIC-TREE-{skill}-v{X.Y.Z}.md
- SCAN-{skill}-v{X.Y.Z}.md

---

### package.sh

**Usage:**
```bash
bash scripts/package.sh skill-name X.Y.Z
```

**Creates:**
- skill-name-vX.Y.Z.skill (ZIP format)
- Verifies with `file` command

---

### update-version.sh

**Usage:**
```bash
bash scripts/update-version.sh /path X.Y.Z
```

**Updates:** All footer versions to match.

---

## 🧪 EVALUATIONS

### E-001: Create Skill

**Input:** `create skill: API test generator`

**Expected:**
1. P01-init activation
2. P02-plan with confirmation ⛔
3. P03-build + validation
4. P04-deliver with audit offer ⛔
5. All files in English
6. Session indicator shown

**Criteria:**
- [ ] SKILL.md English, < 300 lines
- [ ] README-{name}.md English
- [ ] Frontmatter: name + description only
- [ ] Session indicator correct

---

### E-002: Update Skill

**Input:** `[attached .skill] + add error handling`

**Expected:**
1. Snapshot original
2. NEVER DEGRADE check
3. Planning Document
4. Diff Report
5. Delivery

---

### E-003: Confirmation Protocol

**Input:** After plan — "ok got it"

**Expected:**
1. Reject invalid confirmation
2. Request explicit "yes/go/proceed"
3. Only proceed on valid confirmation

---

### E-004: Session Indicator

**Input:** Long session (30+ messages)

**Expected:** Indicator changes 🟢 → 🟡 → 🔴

---

### E-005: Checkup Command

**Input:** `checkup`

**Expected:**
1. Jump to P04 audit section
2. Run full audit
3. Generate audit report

---

### E-006: Language Enforcement

**Input:** Request with Russian text

**Expected:**
1. Respond in English
2. Create skill in English
3. All outputs in English

---

## ⭐ PROVEN PATTERNS (MUST INCLUDE)

### 1. NEVER DEGRADE

**Rule:** Never remove working functionality.

**Implementation:**
- validate.sh --degrade check
- Blocks delivery if >30% content loss
- Blocks if key sections removed

---

### 2. Explicit Confirmation

**Rule:** Require explicit "yes/go/proceed".

**Implementation:**
- P02-plan waits for confirmation
- Rejects "ok", "got it", "understood"
- Clear re-request if invalid

---

### 3. Protocol-First

**Rule:** Always read protocol before action.

**Implementation:**
- ⛔ FIRST STEP section in SKILL.md
- P00-router.md as entry point
- State machine determines action

---

### 4. Specific > Abstract

**Rule:** Two specific instructions better than one abstract.

**Anti-pattern:** "Unified Workflow" table
**Pattern:** Separate protocols with clear responsibilities

---

### 5. Prevention > Correction

**Rule:** Validate before delivery, not after.

**Implementation:**
- validate.sh runs in P03-build
- NEVER DEGRADE check in P04-deliver
- Planning Document in P02-plan

---

## 📦 DELIVERABLES

When complete, deliver:

1. **skill-architect-v9.0.0.skill** — ZIP archive with:
   - SKILL.md (80-100 lines)
   - README-skill-architect.md
   - CHANGELOG-skill-architect.md
   - MANIFEST.md
   - protocols/ (5 files)
   - reference/ (8-10 files)
   - scripts/ (5 files)
   - docs/v9.0.0/ (3 files)

2. **skill-architect-v9.0.0-docs.zip** — Documentation archive

3. **Diff Report** — v8.7.0 → v9.0.0 comparison

---

## 🎯 SUCCESS CRITERIA

| Metric | Target | v8.7.0 |
|--------|--------|--------|
| SKILL.md lines | 80-100 | 104 |
| Total files | ~35 | 70 |
| Scripts | 5 | 12 |
| Protocols | 5 | 7 |
| Docs types | 3 | 7 |
| Language | English only | Mixed |

---

## ⚠️ ANTI-PATTERNS TO AVOID

| ❌ Anti-pattern | ✅ Correct |
|-----------------|-----------|
| "Unified Workflow" abstraction | Separate specific protocols |
| Token counter (unreliable) | Session indicator |
| "ok understood" acceptance | Explicit confirmation only |
| Remove "unused" sections | Keep if provides context |
| Russian/mixed language | English only |
| 7 doc types | 3 mandatory docs |
| 12 scripts | 5 consolidated |

---

## 📋 BUILD CHECKLIST

```
□ Create folder structure
□ Write SKILL.md (80-100 lines, English)
□ Write protocols/ (5 files)
□ Write reference/ (8-10 files)
□ Write scripts/ (5 files, consolidated)
□ Write README-skill-architect.md (English)
□ Write CHANGELOG-skill-architect.md
□ Generate MANIFEST.md
□ Generate docs/v9.0.0/ (3 files including LOGIC-TREE)
□ Run validate.sh — all pass
□ Package as .skill
□ Create Diff Report v8.7.0 → v9.0.0
```

---

*SPEC-skill-architect-v9.0.0.md | Technical Specification for Clean Slate Rebuild*
