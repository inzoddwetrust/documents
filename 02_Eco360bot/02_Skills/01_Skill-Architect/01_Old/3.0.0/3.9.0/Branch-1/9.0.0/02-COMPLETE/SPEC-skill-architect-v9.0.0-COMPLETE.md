# SPECIFICATION: skill-architect v9.0.0 "Clean Slate"

**Purpose:** Complete, self-contained specification for rebuilding skill-architect from scratch.

**For:** Claude Opus (new chat window)

**Created:** 2025-12-12

**Principle:** This document contains EVERYTHING needed to build v9.0. No external references required.

---

# PART 1: MISSION AND CONSTRAINTS

## 1.1 Mission

Build skill-architect v9.0.0 — a meta-skill for creating other skills — using proven patterns extracted from 18+ versions of evolution.

**This is a CLEAN REBUILD, not a patch.**

---

## 1.2 Language Constraint: ENGLISH ONLY

| Component | Language | Violation |
|-----------|----------|-----------|
| SKILL.md | English | ⛔ BLOCKING |
| README.md | English | ⛔ BLOCKING |
| All protocols | English | ⛔ BLOCKING |
| All reference files | English | ⛔ BLOCKING |
| All scripts | English | ⛔ BLOCKING |
| All commands | English | ⛔ BLOCKING |
| All output messages | English | ⛔ BLOCKING |
| Skills created BY this skill | English | ⛔ BLOCKING |

**ZERO TOLERANCE for Russian, German, French, or ANY other language.**

---

## 1.3 Platform Constraints

| Constraint | Value | Reason |
|------------|-------|--------|
| SKILL.md max lines | 300 | Platform limit |
| SKILL.md target | 80-100 | Lean principle |
| Frontmatter keys | name, description ONLY | Other keys break upload |

**Valid frontmatter:**
```yaml
---
name: skill-name
description: "v1.0.0 | What it does. Triggers: a, b, c."
---
```

**Invalid frontmatter (BREAKS UPLOAD):**
```yaml
---
name: skill-name
version: 1.0.0        # ❌ FORBIDDEN
ecosystem: tools      # ❌ FORBIDDEN  
author: someone       # ❌ FORBIDDEN
type: tool            # ❌ FORBIDDEN
---
```

---

# PART 2: ARCHITECTURE

## 2.1 File Structure (Target: ~30 files)

```
skill-architect-v9.0.0/
│
├── SKILL.md                      ← 80-100 lines, English
├── README-skill-architect.md     ← User documentation, English
├── CHANGELOG-skill-architect.md  ← History
├── MANIFEST.md                   ← File index
│
├── protocols/                    ← 5 files
│   ├── P00-router.md
│   ├── P01-init.md
│   ├── P02-plan.md              ← ⛔ BLOCKING
│   ├── P03-build.md
│   └── P04-deliver.md           ← ⛔ BLOCKING
│
├── reference/                    ← 6 files
│   ├── quality-gates.md
│   ├── templates.md
│   ├── session-indicator.md
│   ├── diff-format.md
│   ├── naming.md
│   └── evaluations.md
│
├── scripts/                      ← 4 files
│   ├── validate.sh
│   ├── audit.sh
│   ├── generate-docs.sh
│   └── package.sh
│
└── docs/
    └── v9.0.0/
        ├── DIFF-skill-architect-v9.0.0.md
        ├── LOGIC-TREE-skill-architect-v9.0.0.md  ← MANDATORY
        └── SCAN-skill-architect-v9.0.0.md
```

---

## 2.2 Protocol Flow

```
[USER REQUEST]
      │
      ▼
   P01-init ─────────────── Activation + configuration
      │
      ▼
   P02-plan ⛔ ───────────── Planning + WAIT for "yes/go/proceed"
      │
      ▼
   P03-build ────────────── Create + validate
      │
      ▼
   P04-deliver ⛔ ────────── Package + deliver + optional audit
      │
      ▼
    [END]
```

**Blocking points:**
1. **P02 → P03**: Requires explicit "yes", "go", or "proceed"
2. **P04 → END**: User decides "audit" or "skip"

---

# PART 3: COMPLETE FILE SPECIFICATIONS

## 3.1 SKILL.md (80-100 lines)

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

| # | Rule | Check |
|---|------|-------|
| 1 | SKILL.md = English | validate.sh |
| 2 | SKILL.md < 300 lines | validate.sh |
| 3 | Frontmatter: name + description only | validate.sh |
| 4 | README-{name}.md required | validate.sh |
| 5 | Explicit confirmation required | P02 |
| 6 | NEVER DEGRADE | validate.sh |

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

State machine for skill-architect navigation.

---

## Flow Diagram

```
[START]
    │
    ▼
  P01-init ────────── "What are we doing?"
    │
    ▼
  P02-plan ⛔ ─────── Planning + confirmation
    │
    ▼
  P03-build ───────── Create + validate
    │
    ▼
  P04-deliver ⛔ ──── Package + deliver + audit
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
| P04 → END | Any user decision | — |

---

## Recovery

After context loss:
1. Re-read SKILL.md
2. Check last state
3. Resume

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

### 1. Respond with version

```
Skill Architect v9.0.0
```

### 2. Determine intent

| User provides | Action |
|---------------|--------|
| Clear purpose | → P02-plan |
| Unclear | Ask: "Purpose?" |

### 3. Gather config (if needed)

One question at a time:
```
Mode? (skill)
What does it do?
```

### 4. Confirm

```
Got it: [skill] for [purpose]
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

**Cannot proceed without "yes", "go", or "proceed"**

| ✅ Valid | ❌ Invalid |
|----------|------------|
| yes, go, proceed | ok, got it, understood |

---

## Steps

### 1. Create Planning Document

```markdown
# [Skill Name]: Plan v0.0.0 → v1.0.0

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md | English, < 300 lines |
| Frontmatter | name + description only |

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

## Risks

| Risk | Mitigation |
|------|------------|

---

**Confirm:** "yes", "go", "proceed"
```

### 2. Save to outputs

### 3. WAIT for confirmation

---

## Confirmation Handling

| User says | Action |
|-----------|--------|
| "yes/go/proceed" | → P03-build |
| Question | Answer, re-ask |
| "ok/got it" | ❌ Invalid, re-ask |

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

Create files and validate.

---

## Trigger

P02-plan confirmed with "yes/go/proceed"

---

## Prerequisites Check

```
□ Plan confirmed (explicit yes)
□ SKILL.md will be English
□ SKILL.md will be < 300 lines
□ README will be English
```

---

## Steps

### 1. Create files

Per plan:
- New skill → create in /home/claude/
- Update → copy, modify
- Log deviations

### 2. Validate immediately

```bash
bash scripts/validate.sh /path/to/skill
```

### 3. Handle results

| Result | Action |
|--------|--------|
| PASS | → P04-deliver |
| FAIL | Fix, re-validate |

---

## NEVER DEGRADE Reminder

- Don't remove working functionality
- Don't replace specific with abstract
- When in doubt, keep both

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

### 3. Package

```bash
bash scripts/package.sh skill-name X.Y.Z
```

### 4. Generate docs

```bash
bash scripts/generate-docs.sh /path X.Y.Z
```

### 5. Deliver

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

### 6. Optional Audit

If user says "yes" or "checkup" command:
- Run full validation
- Check cross-references
- Generate audit report

---

## Next

| User says | Action |
|-----------|--------|
| "yes/audit" | Run audit, then END |
| "skip" | END |

---

*P04-deliver.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.7 reference/quality-gates.md

```markdown
# Quality Gates

Validation layers for skills.

---

## Mandatory Gates (BLOCKING)

| Gate | Check | How |
|------|-------|-----|
| G1 | SKILL.md exists | validate.sh |
| G2 | SKILL.md < 300 lines | validate.sh |
| G3 | SKILL.md = English only | validate.sh |
| G4 | Frontmatter: name + description only | validate.sh |
| G5 | README-{name}.md exists | validate.sh |
| G6 | Explicit confirmation before build | P02 protocol |
| G7 | NEVER DEGRADE check | validate.sh --degrade |

---

## Warning Gates

| Gate | Check |
|------|-------|
| G8 | MANIFEST.md current |
| G9 | Footer versions synced |

---

## Validation Command

```bash
bash scripts/validate.sh /path/to/skill
bash scripts/validate.sh --degrade /old /new
```

---

*quality-gates.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.8 reference/session-indicator.md

```markdown
# Session Indicator

Honest session state tracking.

---

## Format

Single emoji + state:

| State | Display | Meaning |
|-------|---------|---------|
| Fresh | 🟢 fresh | Free to work |
| Mid | 🟡 mid | Keep focus |
| Long | 🔴 long | Risk of context loss |

---

## Detection Rules

### 🟢 fresh — ALL conditions:

- < 10 user messages
- < 5 tool calls
- No large files loaded

### 🟡 mid — ANY condition:

- 10-30 user messages
- 5-15 tool calls
- 1-2 large files loaded

### 🔴 long — ANY condition:

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

*session-indicator.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.9 reference/templates.md

```markdown
# Templates

Skill creation templates.

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

**❌ FORBIDDEN keys:**
- version
- ecosystem
- type
- author
- Any other key

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
| Goal | {what it achieves} |
| Method | {how} |

---

## Commands

| Command | Action |
|---------|--------|
| {cmd} | {action} |

---

## Context Anchor

```
⚙️ {skill-name} v1.0.0 · [status]
[session-indicator]
```

---

*v1.0.0*
```

---

## Footer Convention

```
*{filename} v{X.Y.Z} | {skill-name} v{X.Y.Z}*
```

---

*templates.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.10 reference/diff-format.md

```markdown
# Diff Report Format

Change documentation.

---

## Template

```markdown
# Diff: v{OLD} → v{NEW}

**Skill:** {name}
**Date:** {date}

---

## Metrics

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| SKILL.md lines | X | Y | ±Z% |
| Total files | X | Y | ±Z |

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

*DIFF-{skill}-v{X.Y.Z}.md | {skill} v{X.Y.Z}*
```

---

*diff-format.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.11 reference/naming.md

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

---

## Versions

- Semver: v1.0.0, v2.1.3
- In description, not separate key

---

*naming.md v1.0.0 | skill-architect v9.0.0*
```

---

## 3.12 reference/evaluations.md

```markdown
# Evaluations

Test scenarios for validation.

---

## E-001: Create Skill

**Input:** `create skill: API test generator`

**Expected flow:**
1. P01-init activation
2. P02-plan with confirmation ⛔
3. P03-build + validation
4. P04-deliver with audit offer ⛔

**Checks:**
- [ ] SKILL.md English, < 300 lines
- [ ] README English
- [ ] Frontmatter valid
- [ ] Session indicator shown

---

## E-002: Update Skill

**Input:** `[attached .skill] + add error handling`

**Expected:**
1. NEVER DEGRADE check
2. Planning Document
3. Diff Report

---

## E-003: Confirmation Rejection

**Input:** After plan — "ok got it"

**Expected:**
1. Reject as invalid
2. Request: "Please confirm with 'yes', 'go', or 'proceed'"
3. Wait for valid confirmation

---

## E-004: Checkup Command

**Input:** `checkup`

**Expected:**
1. Run full audit
2. Generate report

---

*evaluations.md v1.0.0 | skill-architect v9.0.0*
```

---

# PART 4: COMPLETE SCRIPTS

## 4.1 scripts/validate.sh

```bash
#!/bin/bash
# validate.sh — Skill validation
# Usage: bash validate.sh <path>
#        bash validate.sh --degrade <old> <new>
# v1.0.0 | skill-architect v9.0.0

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

MODE="standard"
if [ "$1" == "--degrade" ]; then
    MODE="degrade"
    OLD="$2"
    NEW="$3"
else
    INPUT="$1"
fi

ERRORS=0
WARNINGS=0

echo "═══════════════════════════════════════════════════════"
echo "         SKILL VALIDATION v1.0.0"
echo "═══════════════════════════════════════════════════════"
echo ""

# ═══════════════════════════════════════════════════════════
# STANDARD VALIDATION
# ═══════════════════════════════════════════════════════════

validate_standard() {
    local FOLDER="$1"
    
    echo "📁 Validating: $FOLDER"
    echo ""
    
    # G1: SKILL.md exists
    if [ -f "${FOLDER}/SKILL.md" ]; then
        echo -e "${GREEN}✅ G1: SKILL.md found${NC}"
    else
        echo -e "${RED}❌ G1: SKILL.md NOT FOUND${NC}"
        ((ERRORS++))
        return
    fi
    
    # G2: Line count < 300
    LINES=$(wc -l < "${FOLDER}/SKILL.md")
    if [ "$LINES" -lt 300 ]; then
        echo -e "${GREEN}✅ G2: Line count: $LINES (< 300)${NC}"
    else
        echo -e "${RED}❌ G2: Line count: $LINES (EXCEEDS 300!)${NC}"
        ((ERRORS++))
    fi
    
    # G3: English only (check for Cyrillic)
    BODY=$(awk '/^---$/{n++; next} n>=2' "${FOLDER}/SKILL.md")
    CYRILLIC=$(echo "$BODY" | grep -oP '[\p{Cyrillic}]' 2>/dev/null | wc -l || echo 0)
    if [ "$CYRILLIC" -gt 10 ]; then
        echo -e "${RED}❌ G3: SKILL.md contains non-English ($CYRILLIC Cyrillic chars)${NC}"
        ((ERRORS++))
    else
        echo -e "${GREEN}✅ G3: SKILL.md is English${NC}"
    fi
    
    # G4: Frontmatter valid
    FIRST_LINE=$(head -1 "${FOLDER}/SKILL.md")
    if [ "$FIRST_LINE" = "---" ]; then
        # Check name field
        if grep -q "^name:" "${FOLDER}/SKILL.md"; then
            echo -e "${GREEN}✅ G4a: name field present${NC}"
        else
            echo -e "${RED}❌ G4a: name field missing${NC}"
            ((ERRORS++))
        fi
        
        # Check description field
        if grep -q "^description:" "${FOLDER}/SKILL.md"; then
            echo -e "${GREEN}✅ G4b: description field present${NC}"
        else
            echo -e "${RED}❌ G4b: description field missing${NC}"
            ((ERRORS++))
        fi
        
        # Check for invalid keys
        ALLOWED="name|description|license|allowed-tools|compatibility|metadata"
        KEYS=$(sed -n '2,/^---$/p' "${FOLDER}/SKILL.md" | grep -E '^[a-z-]+:' | cut -d: -f1)
        for KEY in $KEYS; do
            if ! echo "$KEY" | grep -qE "^($ALLOWED)$"; then
                echo -e "${RED}❌ G4c: Invalid frontmatter key: '$KEY'${NC}"
                ((ERRORS++))
            fi
        done
    else
        echo -e "${RED}❌ G4: No frontmatter (must start with ---)${NC}"
        ((ERRORS++))
    fi
    
    # G5: README exists
    SKILL_NAME=$(grep "^name:" "${FOLDER}/SKILL.md" 2>/dev/null | sed 's/name: *//' | tr -d '"' | tr -d "'")
    if [ -f "${FOLDER}/README.md" ] || [ -f "${FOLDER}/README-${SKILL_NAME}.md" ]; then
        echo -e "${GREEN}✅ G5: README found${NC}"
    else
        echo -e "${RED}❌ G5: README NOT FOUND${NC}"
        ((ERRORS++))
    fi
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
    
    # Check dirs exist
    if [ ! -d "$OLD" ] || [ ! -d "$NEW" ]; then
        echo -e "${RED}❌ Both directories required${NC}"
        ((ERRORS++))
        return
    fi
    
    # PHASE 1: File deletion
    echo "═══ PHASE 1: FILE DELETION ═══"
    for file in "$OLD"/*.md; do
        [ -f "$file" ] || continue
        basename=$(basename "$file")
        if [ ! -f "$NEW/$basename" ]; then
            echo -e "${RED}❌ DELETED: $basename${NC}"
            ((ERRORS++))
        fi
    done
    
    # PHASE 2: Content volume (>30% loss = violation)
    echo ""
    echo "═══ PHASE 2: CONTENT VOLUME ═══"
    for old_file in "$OLD"/*.md; do
        [ -f "$old_file" ] || continue
        basename=$(basename "$old_file")
        new_file="$NEW/$basename"
        
        if [ -f "$new_file" ]; then
            old_lines=$(wc -l < "$old_file")
            new_lines=$(wc -l < "$new_file")
            
            if [ "$old_lines" -gt 0 ]; then
                ratio=$((new_lines * 100 / old_lines))
                if [ "$ratio" -lt 70 ]; then
                    echo -e "${RED}❌ $basename: $old_lines → $new_lines (${ratio}% — >30% loss!)${NC}"
                    ((ERRORS++))
                else
                    echo -e "${GREEN}✅ $basename: $old_lines → $new_lines (${ratio}%)${NC}"
                fi
            fi
        fi
    done
    
    # PHASE 3: Key sections
    echo ""
    echo "═══ PHASE 3: KEY SECTIONS ═══"
    SECTIONS=("## Purpose" "## Flow" "## Commands" "## Context")
    for old_file in "$OLD"/*.md; do
        [ -f "$old_file" ] || continue
        basename=$(basename "$old_file")
        new_file="$NEW/$basename"
        
        if [ -f "$new_file" ]; then
            for section in "${SECTIONS[@]}"; do
                if grep -q "$section" "$old_file" 2>/dev/null; then
                    if ! grep -q "$section" "$new_file" 2>/dev/null; then
                        echo -e "${RED}❌ SECTION REMOVED: '$section' from $basename${NC}"
                        ((ERRORS++))
                    fi
                fi
            done
        fi
    done
}

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

if [ "$MODE" == "degrade" ]; then
    validate_degrade "$OLD" "$NEW"
else
    if [ -d "$INPUT" ]; then
        validate_standard "$INPUT"
    else
        echo -e "${RED}❌ Not found: $INPUT${NC}"
        exit 1
    fi
fi

# SUMMARY
echo ""
echo "═══════════════════════════════════════════════════════"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ VALIDATION PASSED${NC}"
    exit 0
else
    echo -e "${RED}❌ VALIDATION FAILED: $ERRORS error(s)${NC}"
    exit 1
fi
```

---

## 4.2 scripts/audit.sh

```bash
#!/bin/bash
# audit.sh — Full skill audit
# Usage: bash audit.sh <path>
# v1.0.0 | skill-architect v9.0.0

set -e

INPUT="$1"

echo "═══════════════════════════════════════════════════════"
echo "              FULL AUDIT v1.0.0"
echo "═══════════════════════════════════════════════════════"
echo ""

if [ -z "$INPUT" ] || [ ! -d "$INPUT" ]; then
    echo "Usage: bash audit.sh <skill-folder>"
    exit 1
fi

# Run validation
bash "$(dirname "$0")/validate.sh" "$INPUT"
VALIDATE_RESULT=$?

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

# File count
FILE_COUNT=$(find "$INPUT" -name "*.md" -o -name "*.sh" | wc -l)
echo "Files: $FILE_COUNT"

# Line count
TOTAL_LINES=$(find "$INPUT" -name "*.md" -exec cat {} \; | wc -l)
echo "Total lines: $TOTAL_LINES"

echo ""
if [ $VALIDATE_RESULT -eq 0 ]; then
    echo "VERDICT: ✅ PASS"
else
    echo "VERDICT: ❌ FAIL"
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
[P03-build] ────────── Create + validate
    │
    ▼
[P04-deliver] ⛔ ────── Package + deliver
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

## State Transitions

| From | Condition | To |
|------|-----------|-----|
| P01 | Config done | P02 |
| P02 | Confirmed | P03 |
| P03 | Validation pass | P04 |
| P04 | Skip | END |

---

*LOGIC-TREE-${SKILL_NAME}-v${VERSION}.md | ${SKILL_NAME} v${VERSION}*
EOF

# SCAN
cat > "$DOCS_DIR/SCAN-${SKILL_NAME}-v${VERSION}.md" << EOF
# SCAN: ${SKILL_NAME} v${VERSION}

Validation results.

---

## Summary

| Check | Result |
|-------|--------|
| SKILL.md exists | ☐ |
| SKILL.md < 300 lines | ☐ |
| SKILL.md English | ☐ |
| Frontmatter valid | ☐ |
| README exists | ☐ |

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

# Rename folder if needed
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

## Context

New skill for linting markdown files.

## Changes

### Add
- SKILL.md with lint commands
- README-markdown-linter.md
- MANIFEST.md

### Remove
- Nothing (new skill)

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
Building markdown-linter v1.0.0...

✅ SKILL.md created (45 lines, English)
✅ README-markdown-linter.md created
✅ MANIFEST.md created

Running validation...
✅ G1: SKILL.md found
✅ G2: Line count: 45 (< 300)
✅ G3: SKILL.md is English
✅ G4: Frontmatter valid
✅ G5: README found

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
Running full audit...

═══════════════════════════════════════════════════════
              AUDIT REPORT
═══════════════════════════════════════════════════════

Skill: skill-architect
Version: v9.0.0
Date: 2025-12-12

STRUCTURE ────────────────────────────
✅ G1: SKILL.md found
✅ G2: Line count: 85 (< 300)
✅ G3: SKILL.md is English
✅ G4: Frontmatter valid
✅ G5: README found

FILES ────────────────────────────────
Total: 28 files
Lines: 2,150

VERDICT: ✅ PASS
═══════════════════════════════════════════════════════

⚙️ skill-architect v9.0.0 · P04-deliver · audit complete
🟡 mid
```

---

# PART 6: DELIVERABLES

When complete, deliver:

1. **skill-architect-v9.0.0.skill** — ZIP archive containing:
   - SKILL.md (80-100 lines)
   - README-skill-architect.md
   - CHANGELOG-skill-architect.md
   - MANIFEST.md
   - protocols/ (5 files)
   - reference/ (6 files)
   - scripts/ (4 files)
   - docs/v9.0.0/ (3 files, including LOGIC-TREE)

2. **skill-architect-v9.0.0-docs.zip**

3. **Diff Report** comparing to "nothing" (new build)

---

# PART 7: SUCCESS CRITERIA

| Metric | Target |
|--------|--------|
| SKILL.md lines | 80-100 |
| Total files | ~28-32 |
| Language | English only |
| Protocols | 5 |
| Scripts | 4 |
| Doc types | 3 (DIFF, LOGIC-TREE, SCAN) |
| All validations | PASS |

---

# PART 8: BUILD CHECKLIST

```
□ Create folder skill-architect-v9.0.0/
□ Write SKILL.md (80-100 lines, English)
□ Write protocols/ (5 files)
□ Write reference/ (6 files)
□ Write scripts/ (4 files, make executable)
□ Write README-skill-architect.md
□ Write CHANGELOG-skill-architect.md
□ Generate MANIFEST.md
□ Run: bash scripts/generate-docs.sh . 9.0.0
□ Run: bash scripts/validate.sh .
□ Verify: ALL PASS
□ Run: bash scripts/package.sh skill-architect 9.0.0
□ Deliver .skill and -docs.zip
```

---

*SPEC-skill-architect-v9.0.0-COMPLETE.md | Self-contained specification for clean rebuild*
