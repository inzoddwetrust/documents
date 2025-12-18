# SPECIFICATION: skill-architect v9.0.0 "Registry"

**Purpose:** Complete specification with MANDATORY feature tracking.

**For:** Claude Opus (new window)

**Created:** 2025-12-12

**Core Principle:** NEVER DEGRADE = track EVERY feature, EVERY line, EVERY version.

---

# PART 0: THE PROBLEM THIS SOLVES

Previous attempts at v9.0.0 FAILED because:
1. "Simplification" deleted critical features
2. No mechanism to VERIFY what was kept vs lost
3. NEVER DEGRADE was just words, not enforced
4. No feature-by-feature tracking

**Solution: FEATURE-REGISTRY.md** — mandatory document that:
- Numbers every category
- Numbers every feature
- Counts lines for each
- Compares version to version
- BLOCKS delivery if features missing

---

# PART 1: FEATURE REGISTRY SPECIFICATION

## 1.1 What is Feature Registry

A structured document that tracks EVERY functional component of a skill:

```markdown
# FEATURE-REGISTRY: {skill-name} v{X.Y.Z}

## Summary

| Metric | Value |
|--------|-------|
| Categories | N |
| Features | N |
| Total lines | N |
| Coverage | 100% |

---

## Categories

| # | Category | Features | Lines |
|---|----------|----------|-------|
| C1 | Core | N | N |
| C2 | Protocols | N | N |
| C3 | Validation | N | N |
| ... | ... | ... | ... |

---

## C1: Core

| # | Feature | File | Lines | Status |
|---|---------|------|-------|--------|
| C1-F01 | Frontmatter constraints | SKILL.md | 15 | ✅ |
| C1-F02 | Purpose block | SKILL.md | 12 | ✅ |
| C1-F03 | Context anchor | SKILL.md | 8 | ✅ |
| C1-F04 | Session indicator | SKILL.md | 4 | ✅ |
| C1-F05 | Commands table | SKILL.md | 10 | ✅ |
| C1-F06 | Confirmation rules | SKILL.md | 6 | ✅ |

**Subtotal:** 6 features, 55 lines

---

## C2: Protocols
...

## C3: Validation
...

---

## Version Comparison

| Feature | v8.7.0 | v9.0.0 | Delta | Status |
|---------|--------|--------|-------|--------|
| C1-F01 | 15 | 15 | 0 | ✅ |
| C1-F02 | 12 | 12 | 0 | ✅ |
| C1-F03 | 8 | 8 | 0 | ✅ |
| ... | ... | ... | ... | ... |

---

## NEVER DEGRADE Check

| Check | Result |
|-------|--------|
| Features lost | 0 |
| Lines lost >30% | 0 |
| Categories removed | 0 |

**VERDICT:** ✅ PASSED / ❌ FAILED

---

*FEATURE-REGISTRY-{skill-name}-v{X.Y.Z}.md*
```

---

## 1.2 Numbering Convention

### Categories: C{N}

```
C1 — Core (SKILL.md essentials)
C2 — Protocols (state machine)
C3 — Validation (quality gates)
C4 — Scripts (automation)
C5 — Reference (templates, guides)
C6 — Documentation (docs system)
C7 — Inheritance (genes mechanism)
```

### Features: C{N}-F{NN}

```
C1-F01 — First feature in Core
C1-F02 — Second feature in Core
C2-F01 — First feature in Protocols
C3-F15 — 15th feature in Validation
```

---

## 1.3 Feature Registry Rules

| Rule | Enforcement |
|------|-------------|
| EVERY skill has FEATURE-REGISTRY.md | validate.sh |
| EVERY feature numbered | validate.sh |
| EVERY feature has line count | validate.sh |
| Updates MUST compare to previous | P04-deliver |
| Lost features = BLOCKED | P04-deliver |
| >30% line loss per feature = WARNING | P04-deliver |

---

# PART 2: skill-architect v9.0.0 FEATURE REGISTRY

## Complete Feature List for v9.0.0

This is what MUST be in v9.0.0. Each feature tracked.

---

### C1: Core (SKILL.md)

| # | Feature | Description | Lines |
|---|---------|-------------|-------|
| C1-F01 | Frontmatter | name + description only | 4 |
| C1-F02 | Version in description | vX.Y.Z format | 1 |
| C1-F03 | Flow diagram | Protocol visualization | 6 |
| C1-F04 | Protocol table | Purpose + blocking | 8 |
| C1-F05 | Critical rules table | 7 rules numbered | 12 |
| C1-F06 | First Step section | Protocol-first | 5 |
| C1-F07 | Commands table | 4 commands | 8 |
| C1-F08 | Confirmation table | Valid vs invalid | 5 |
| C1-F09 | Context anchor | Format specification | 8 |
| C1-F10 | Session indicator | 🟢🟡🔴 | 3 |

**C1 Total:** 10 features, ~60 lines

---

### C2: Protocols

| # | Feature | File | Lines |
|---|---------|------|-------|
| C2-F01 | P00-router | State machine | 60 |
| C2-F02 | Decision table | Routing logic | 15 |
| C2-F03 | P01-init | Activation | 50 |
| C2-F04 | P02-plan | Planning ⛔ | 70 |
| C2-F05 | Explicit confirmation | Valid/invalid | 10 |
| C2-F06 | Planning document template | Full template | 30 |
| C2-F07 | P03-build | Build + validate | 60 |
| C2-F08 | Prerequisites check | Checklist | 8 |
| C2-F09 | NEVER DEGRADE reminder | In P03 | 6 |
| C2-F10 | P04-deliver | Delivery ⛔ | 80 |
| C2-F11 | NEVER DEGRADE check | validate --degrade | 10 |
| C2-F12 | Diff report generation | Per format | 8 |
| C2-F13 | Package skill | ZIP command | 6 |
| C2-F14 | Generate docs | Script call | 6 |
| C2-F15 | Audit option | yes/skip | 8 |
| C2-F16 | Recovery procedure | After context loss | 10 |

**C2 Total:** 16 features, ~437 lines

---

### C3: Validation (Quality Gates)

| # | Feature | Description | Lines |
|---|---------|-------------|-------|
| C3-F01 | L1 Structure | SKILL.md exists, <300 | 10 |
| C3-F02 | L2 Content | Purpose, triggers | 10 |
| C3-F03 | L3 Logic | State machine, blocking | 10 |
| C3-F04 | L4 Naming | kebab-case | 8 |
| C3-F05 | L5 Integration | MANIFEST, footers | 10 |
| C3-F06 | L6 Testing | Flows work | 8 |
| C3-F07 | L7 Knowledge Redundancy | No bloat check | 25 |
| C3-F08 | L8 Version Integrity | Sync check | 15 |
| C3-F09 | L9 Documentation | Naming convention | 15 |
| C3-F10 | Quick test rule | "Delete and still works?" | 5 |
| C3-F11 | Redundancy score | 0-10/10-30/30+ | 8 |

**C3 Total:** 11 features, ~124 lines

---

### C4: Scripts

| # | Feature | File | Lines |
|---|---------|------|-------|
| C4-F01 | validate.sh | Main validation | 250 |
| C4-F02 | Standard validation | G1-G5 | 80 |
| C4-F03 | NEVER DEGRADE mode | --degrade | 60 |
| C4-F04 | Phase 1: File deletion | Check | 15 |
| C4-F05 | Phase 2: Content volume | >30% check | 20 |
| C4-F06 | Phase 3: Key sections | Section check | 20 |
| C4-F07 | L1-L6 structured | Layered output | 60 |
| C4-F08 | --docs mode | Docs validation | 30 |
| C4-F09 | --naming mode | Naming validation | 20 |
| C4-F10 | --ssot mode | SSOT check | 20 |
| C4-F11 | audit.sh | Full audit | 80 |
| C4-F12 | generate-docs.sh | Doc generation | 100 |
| C4-F13 | package.sh | ZIP packaging | 40 |
| C4-F14 | genetic-audit.sh | Inheritance check | 200 |
| C4-F15 | Phase 1: Parent genes | Extract | 50 |
| C4-F16 | Phase 2: Child requirements | Extract | 50 |
| C4-F17 | Phase 3: Inheritance % | Compare | 40 |
| C4-F18 | feature-registry.sh | Registry generation | 150 |

**C4 Total:** 18 features, ~1285 lines

---

### C5: Reference

| # | Feature | File | Lines |
|---|---------|------|-------|
| C5-F01 | templates.md | All templates | 170 |
| C5-F02 | Frontmatter constraints | Allowed/forbidden | 25 |
| C5-F03 | Purpose block (4 fields) | serves/goal/method/success | 15 |
| C5-F04 | Protocol-First rule | Read before act | 15 |
| C5-F05 | Context anchor format | 2-line format | 15 |
| C5-F06 | Template types | 5 types | 15 |
| C5-F07 | MANIFEST.md template | Full template | 20 |
| C5-F08 | Documentation naming | Convention | 25 |
| C5-F09 | PRE-BUILD CHECKPOINT | Checklist | 15 |
| C5-F10 | Lean Principle | What goes where | 5 |
| C5-F11 | quality-gates.md | L1-L9 | 150 |
| C5-F12 | session-indicator.md | 🟢🟡🔴 rules | 50 |
| C5-F13 | diff-format.md | Diff template | 60 |
| C5-F14 | naming.md | Naming rules | 40 |
| C5-F15 | evaluations.md | Test scenarios | 80 |

**C5 Total:** 15 features, ~700 lines

---

### C6: Documentation

| # | Feature | File | Lines |
|---|---------|------|-------|
| C6-F01 | DIFF document | Version delta | 80 |
| C6-F02 | Metrics table | Before/after | 10 |
| C6-F03 | Added/Changed/Removed | Tables | 30 |
| C6-F04 | NEVER DEGRADE status | Pass/fail | 5 |
| C6-F05 | LOGIC-TREE document | Flow visualization | 130 |
| C6-F06 | Main flow diagram | Box diagram | 40 |
| C6-F07 | Blocking points table | Full table | 10 |
| C6-F08 | State transitions table | Full table | 20 |
| C6-F09 | Quality gates table | G1-G7 | 15 |
| C6-F10 | File dependencies tree | Tree diagram | 20 |
| C6-F11 | Recovery procedure | 4 steps | 10 |
| C6-F12 | SCAN document | Validation results | 50 |
| C6-F13 | FEATURE-REGISTRY | This spec | 200 |
| C6-F14 | Version comparison table | Feature by feature | 50 |

**C6 Total:** 14 features, ~670 lines

---

### C7: Inheritance

| # | Feature | File | Lines |
|---|---------|------|-------|
| C7-F01 | Gene concept | Documentation | 20 |
| C7-F02 | Parent genes extraction | genetic-audit.sh | 50 |
| C7-F03 | 10 defined genes | List | 30 |
| C7-F04 | Child requirements | Check | 50 |
| C7-F05 | Inheritance % | Calculation | 20 |
| C7-F06 | Inherited genes table | In LOGIC-TREE | 15 |
| C7-F07 | Genes in planning doc | Checklist | 15 |
| C7-F08 | ALIGNED/GAPS/MISALIGNED | Verdict | 10 |

**C7 Total:** 8 features, ~210 lines

---

## FULL SUMMARY

| Category | Features | Lines |
|----------|----------|-------|
| C1: Core | 10 | 60 |
| C2: Protocols | 16 | 437 |
| C3: Validation | 11 | 124 |
| C4: Scripts | 18 | 1285 |
| C5: Reference | 15 | 700 |
| C6: Documentation | 14 | 670 |
| C7: Inheritance | 8 | 210 |
| **TOTAL** | **92** | **~3486** |

---

# PART 3: ENFORCEMENT MECHANISM

## 3.1 feature-registry.sh

New mandatory script:

```bash
#!/bin/bash
# feature-registry.sh — Generate and validate feature registry
# Usage: bash feature-registry.sh <path> [compare-to-path]
# v1.0.0 | skill-architect v9.0.0

set -e

PATH_NEW="$1"
PATH_OLD="$2"

echo "═══════════════════════════════════════════════════════"
echo "         FEATURE REGISTRY GENERATOR v1.0.0"
echo "═══════════════════════════════════════════════════════"

# Extract features from skill
extract_features() {
    local PATH="$1"
    local OUTPUT="$2"
    
    echo "# FEATURE-REGISTRY: $(basename $PATH)" > "$OUTPUT"
    echo "" >> "$OUTPUT"
    echo "Generated: $(date '+%Y-%m-%d %H:%M')" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    
    # Count by category
    echo "## Summary" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    
    local TOTAL_FEATURES=0
    local TOTAL_LINES=0
    
    # C1: Core (SKILL.md)
    if [ -f "$PATH/SKILL.md" ]; then
        local C1_LINES=$(wc -l < "$PATH/SKILL.md")
        echo "### C1: Core" >> "$OUTPUT"
        echo "| Feature | Lines |" >> "$OUTPUT"
        echo "|---------|-------|" >> "$OUTPUT"
        
        # Check each feature
        grep -q "^name:" "$PATH/SKILL.md" && echo "| C1-F01 Frontmatter | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "v[0-9]\+\.[0-9]\+\.[0-9]\+" "$PATH/SKILL.md" && echo "| C1-F02 Version | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "P01.*P02\|→" "$PATH/SKILL.md" && echo "| C1-F03 Flow | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "Purpose\|serves\|goal" "$PATH/SKILL.md" && echo "| C1-F04 Purpose | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "Context Anchor\|⚙️" "$PATH/SKILL.md" && echo "| C1-F05 Context Anchor | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "🟢\|🟡\|🔴\|session" "$PATH/SKILL.md" && echo "| C1-F06 Session Indicator | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "Command" "$PATH/SKILL.md" && echo "| C1-F07 Commands | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "yes.*go.*proceed\|Confirm" "$PATH/SKILL.md" && echo "| C1-F08 Confirmation | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "⛔\|BLOCKING" "$PATH/SKILL.md" && echo "| C1-F09 Blocking Points | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        grep -q "First Step\|Protocol-First\|P00-router" "$PATH/SKILL.md" && echo "| C1-F10 Protocol-First | ✅ |" >> "$OUTPUT" && ((TOTAL_FEATURES++))
        
        echo "" >> "$OUTPUT"
        TOTAL_LINES=$((TOTAL_LINES + C1_LINES))
    fi
    
    # C2: Protocols
    if [ -d "$PATH/protocols" ]; then
        echo "### C2: Protocols" >> "$OUTPUT"
        echo "| File | Lines |" >> "$OUTPUT"
        echo "|------|-------|" >> "$OUTPUT"
        
        for f in "$PATH/protocols"/*.md; do
            [ -f "$f" ] || continue
            local LINES=$(wc -l < "$f")
            echo "| $(basename $f) | $LINES |" >> "$OUTPUT"
            TOTAL_LINES=$((TOTAL_LINES + LINES))
            ((TOTAL_FEATURES++))
        done
        echo "" >> "$OUTPUT"
    fi
    
    # C3: Scripts
    if [ -d "$PATH/scripts" ]; then
        echo "### C4: Scripts" >> "$OUTPUT"
        echo "| File | Lines |" >> "$OUTPUT"
        echo "|------|-------|" >> "$OUTPUT"
        
        for f in "$PATH/scripts"/*.sh; do
            [ -f "$f" ] || continue
            local LINES=$(wc -l < "$f")
            echo "| $(basename $f) | $LINES |" >> "$OUTPUT"
            TOTAL_LINES=$((TOTAL_LINES + LINES))
            ((TOTAL_FEATURES++))
        done
        echo "" >> "$OUTPUT"
    fi
    
    # C5: Reference
    if [ -d "$PATH/reference" ]; then
        echo "### C5: Reference" >> "$OUTPUT"
        echo "| File | Lines |" >> "$OUTPUT"
        echo "|------|-------|" >> "$OUTPUT"
        
        for f in "$PATH/reference"/*.md; do
            [ -f "$f" ] || continue
            local LINES=$(wc -l < "$f")
            echo "| $(basename $f) | $LINES |" >> "$OUTPUT"
            TOTAL_LINES=$((TOTAL_LINES + LINES))
            ((TOTAL_FEATURES++))
        done
        echo "" >> "$OUTPUT"
    fi
    
    # Summary
    echo "## TOTAL" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    echo "Features: $TOTAL_FEATURES" >> "$OUTPUT"
    echo "Lines: $TOTAL_LINES" >> "$OUTPUT"
}

# Compare two registries
compare_registries() {
    local OLD="$1"
    local NEW="$2"
    
    echo ""
    echo "═══ VERSION COMPARISON ═══"
    echo ""
    
    # Compare line counts
    OLD_LINES=$(find "$OLD" -name "*.md" -o -name "*.sh" | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}')
    NEW_LINES=$(find "$NEW" -name "*.md" -o -name "*.sh" | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}')
    
    echo "Old total: $OLD_LINES lines"
    echo "New total: $NEW_LINES lines"
    
    if [ "$NEW_LINES" -lt "$((OLD_LINES * 70 / 100))" ]; then
        echo ""
        echo "❌ NEVER DEGRADE VIOLATION: >30% content loss!"
        exit 1
    fi
    
    # Check for missing files
    echo ""
    echo "═══ MISSING FILES CHECK ═══"
    
    MISSING=0
    for f in "$OLD"/*.md "$OLD"/**/*.md; do
        [ -f "$f" ] || continue
        REL=$(echo "$f" | sed "s|$OLD/||")
        if [ ! -f "$NEW/$REL" ]; then
            echo "❌ MISSING: $REL"
            ((MISSING++))
        fi
    done
    
    if [ "$MISSING" -gt 0 ]; then
        echo ""
        echo "❌ NEVER DEGRADE VIOLATION: $MISSING files missing!"
        exit 1
    fi
    
    echo "✅ All files present"
}

# Main
if [ -z "$PATH_NEW" ]; then
    echo "Usage: bash feature-registry.sh <path> [compare-to]"
    exit 1
fi

REGISTRY_FILE="$PATH_NEW/docs/FEATURE-REGISTRY.md"
extract_features "$PATH_NEW" "$REGISTRY_FILE"

echo "✅ Generated: $REGISTRY_FILE"

if [ -n "$PATH_OLD" ]; then
    compare_registries "$PATH_OLD" "$PATH_NEW"
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "✅ FEATURE REGISTRY COMPLETE"
echo "═══════════════════════════════════════════════════════"
```

---

## 3.2 Integration Points

### In P03-build.md:

```markdown
### 2.5 Generate Feature Registry

```bash
bash scripts/feature-registry.sh /path/to/skill
```

MUST run before P04-deliver.
```

### In P04-deliver.md:

```markdown
### 1.5 Feature Registry Check (ALL builds)

```bash
# New skill
bash scripts/feature-registry.sh /path/to/new

# Update — compare to previous
bash scripts/feature-registry.sh /path/to/new /path/to/old
```

| Result | Action |
|--------|--------|
| PASS | Continue |
| FAIL | ⛔ STOP — restore features |
```

### In validate.sh:

```bash
# Add --registry mode
if [ "$1" == "--registry" ]; then
    bash "$(dirname $0)/feature-registry.sh" "$2" "$3"
    exit $?
fi
```

---

# PART 4: MANDATORY DOCUMENTS

Every skill created by skill-architect MUST have:

| Document | Location | Purpose |
|----------|----------|---------|
| FEATURE-REGISTRY.md | docs/ | Feature tracking |
| DIFF.md | docs/vX.Y.Z/ | Version delta |
| LOGIC-TREE.md | docs/vX.Y.Z/ | Flow + dependencies |
| SCAN.md | docs/vX.Y.Z/ | Validation results |

---

# PART 5: VALIDATION BEFORE DELIVERY

## Checklist (P04-deliver)

```
□ FEATURE-REGISTRY.md generated
□ All 92 features present (for skill-architect)
□ No features lost vs previous version
□ No >30% line loss per feature
□ LOGIC-TREE has File Dependencies
□ LOGIC-TREE has State Transitions
□ NEVER DEGRADE: PASSED
```

---

# PART 6: BUILD INSTRUCTIONS

## Step-by-step:

1. **Create all files per PART 2 feature list**
2. **Run feature-registry.sh** — generates FEATURE-REGISTRY.md
3. **Compare to v8.7.0** — feature-registry.sh new/ old/
4. **Verify 92 features present**
5. **Verify LOGIC-TREE complete** (File Dependencies, State Transitions)
6. **Run validate.sh** — all checks pass
7. **Run genetic-audit.sh** — inheritance verified
8. **Package and deliver**

---

# PART 7: SUCCESS CRITERIA

| Check | Required |
|-------|----------|
| Features | 92 minimum |
| Categories | 7 (C1-C7) |
| FEATURE-REGISTRY.md | Present |
| LOGIC-TREE complete | File Dependencies + State Transitions |
| genetic-audit.sh | Present and working |
| NEVER DEGRADE | PASSED |
| All v8.7.0 functionality | Preserved |

---

# PART 8: DELIVERABLES

1. **skill-architect-v9.0.0.skill**
2. **skill-architect-v9.0.0-docs.zip** containing:
   - FEATURE-REGISTRY-skill-architect-v9.0.0.md
   - DIFF-skill-architect-v9.0.0.md
   - LOGIC-TREE-skill-architect-v9.0.0.md (with File Dependencies!)
   - SCAN-skill-architect-v9.0.0.md
3. **Comparison report** — v8.7.0 vs v9.0.0 feature-by-feature

---

---

# PART 9: COMPLETE FILE CONTENTS

## 9.1 SKILL.md (Target: 85 lines)

```markdown
---
name: skill-architect
description: "v9.0.0 | Protocol-driven skill creation with feature tracking. Triggers: create skill, update, refactor, checkup."
---

# Skill Architect v9.0.0

Lean skill creation with mandatory feature registry.

---

## Flow

```
P01-init → P02-plan ⛔ → P03-build → P04-deliver ⛔
```

| Protocol | Purpose | Blocking |
|----------|---------|----------|
| P01-init | Activation + config | |
| P02-plan | Planning + confirmation | ⛔ |
| P03-build | Create + validate + registry | |
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
| 7 | FEATURE-REGISTRY.md required | feature-registry.sh |

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

*v9.0.0 "Registry"*
```

---

## 9.2 protocols/P00-router.md

```markdown
# P00: Router

State machine for skill-architect.

---

## Flow Diagram

```
[START]
    │
    ▼
  P01-init ────────── Activation + config
    │
    ▼
  P02-plan ⛔ ─────── Planning + confirmation
    │
    ▼
  P03-build ───────── Create + validate + registry
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
| P04 → END | Any decision | — |

---

## Recovery

After context loss:
1. Re-read SKILL.md
2. Check last state
3. Resume from there

---

*P00-router.md v1.0.0 | skill-architect v9.0.0*
```

---

## 9.3 protocols/P02-plan.md

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
| FEATURE-REGISTRY | Mandatory |

## Context

[Why this change]

## Changes

### Add
- [items with C#-F## codes]

### Change
- [items with C#-F## codes]

### Remove
- [items] — NEVER DEGRADE check required

### Keep
- [items]

## Feature Impact

| Category | Before | After | Delta |
|----------|--------|-------|-------|
| C1: Core | N | N | ±N |
| C2: Protocols | N | N | ±N |
| ... | ... | ... | ... |

## Inherited Genes

| Gene | Source | Included |
|------|--------|----------|
| Purpose Block | templates.md | □ |
| Context Anchor | templates.md | □ |
| Session Indicator | templates.md | □ |
| Protocol-First | templates.md | □ |
| Feature Registry | templates.md | □ |

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
| "ok/got it" | ❌ Invalid, re-ask |

---

## Next

→ P03-build (only after valid confirmation)

---

*P02-plan.md v1.0.0 | skill-architect v9.0.0*
```

---

## 9.4 protocols/P03-build.md

```markdown
# P03: Build

Create files, validate, generate registry.

---

## Trigger

P02-plan confirmed with "yes/go/proceed"

---

## PRE-BUILD CHECKPOINT

**Re-read before building:**
```
□ Purpose Block (serves/goal/method/success)
□ Protocol-First (if has protocols)
□ Context Anchor
□ Session Indicator
□ Frontmatter (name + description only)
□ English only
□ < 300 lines
□ FEATURE-REGISTRY will be generated
```

---

## Steps

### 1. Create files per plan

- New skill → create in /home/claude/
- Update → copy, modify
- Log deviations

### 2. Validate immediately

```bash
bash scripts/validate.sh /path/to/skill
```

### 3. Generate Feature Registry

```bash
bash scripts/feature-registry.sh /path/to/skill
```

### 4. Compare to previous (updates)

```bash
bash scripts/feature-registry.sh /path/new /path/old
```

### 5. Handle results

| Result | Action |
|--------|--------|
| PASS | → P04-deliver |
| FAIL | Fix, re-validate |

---

## NEVER DEGRADE Reminder

- Don't remove working functionality
- Don't remove features without C#-F## tracking
- When in doubt, keep both

---

## Next

→ P04-deliver (on validation pass)

---

*P03-build.md v1.0.0 | skill-architect v9.0.0*
```

---

## 9.5 protocols/P04-deliver.md

```markdown
# P04: Deliver

Package, deliver, audit.

---

## ════════════════════════════════════════════════
## ⛔ BLOCKING — WAIT FOR USER AFTER DELIVERY
## ════════════════════════════════════════════════

---

## Steps

### 1. NEVER DEGRADE Check

```bash
bash scripts/validate.sh --degrade /old /new
```

| Result | Action |
|--------|--------|
| PASS | Continue |
| FAIL | ⛔ STOP, restore |

### 2. Feature Registry Check

```bash
bash scripts/feature-registry.sh /new /old
```

Verify:
- All features present
- No >30% line loss per feature
- No categories removed

### 3. Create Diff Report

Per reference/diff-format.md with feature comparison.

### 4. Package

```bash
bash scripts/package.sh skill-name X.Y.Z
```

### 5. Generate Docs

```bash
bash scripts/generate-docs.sh /path X.Y.Z
```

Creates:
- DIFF-{skill}-v{X.Y.Z}.md
- LOGIC-TREE-{skill}-v{X.Y.Z}.md
- SCAN-{skill}-v{X.Y.Z}.md
- FEATURE-REGISTRY-{skill}-v{X.Y.Z}.md

### 6. Deliver

```markdown
## Delivery Complete

| Item | File |
|------|------|
| Skill | [link] |
| Docs | [link] |
| Registry | [link] |

Version: vX.Y.Z
Features: N (±delta from previous)

---

Run audit? "yes" / "skip"
```

### 7. Optional Audit

If "yes" or "checkup":
- Run validate.sh
- Run genetic-audit.sh
- Run feature-registry.sh
- Generate report

---

*P04-deliver.md v1.0.0 | skill-architect v9.0.0*
```

---

## 9.6 reference/templates.md (COMPLETE)

```markdown
# Templates

Skill creation templates with mandatory genes.

---

## ⛔ Frontmatter (MANDATORY)

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

## ⛔ Purpose Block (MANDATORY) — GENE C1-F04

```markdown
## Purpose

| Field | Value |
|-------|-------|
| serves | Who uses this |
| goal | What result |
| method | How achieves |
| success | How to verify |
```

---

## ⛔ Protocol-First (MANDATORY) — GENE C1-F10

```markdown
## ⛔ First Step

Read protocol before action:
view → protocols/P00-router.md
```

| Rule | Reason |
|------|--------|
| Read before act | Prevents drift |
| Protocol determines action | Not user directly |
| State machine is law | Skip = broken |

---

## ⛔ Context Anchor (MANDATORY) — GENE C1-F09

```
⚙️ [skill-name] v[X.Y.Z] · [protocol] · [status]
[session-indicator]
```

Session: 🟢 fresh | 🟡 mid | 🔴 long

---

## ⛔ Feature Registry (MANDATORY) — GENE C6-F13

Every skill MUST have FEATURE-REGISTRY.md:
- All features numbered C#-F##
- Line counts tracked
- Version comparison

---

## Template Types

| Type | Keywords | Process |
|------|----------|---------|
| Analysis | analyze, review | Gather → Analyze → Report |
| Content | create, write | Plan → Generate → Review |
| Data | process, extract | Validate → Transform → Verify |
| Code | build, develop | Design → Implement → Test |
| Investigation | research, find | Define → Search → Present |

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

## MANIFEST.md Template

```markdown
# MANIFEST.md

## {skill-name} v{X.Y.Z}

Build: YYYY-MM-DD | Files: N

| File | Lines | Description |
|------|-------|-------------|
| SKILL.md | N | Main |
| README-{name}.md | N | User docs |

Total: N lines, N files
```

---

## Documentation Naming

```
{TYPE}-{skill-name}[-v{X.Y.Z}].md

Types: README, CHANGELOG, PLAN, DIFF, SCAN, LOGIC-TREE, FEATURE-REGISTRY
```

---

## PRE-BUILD CHECKPOINT

**Trigger:** Before any build, after long conversation.

```
□ C1-F01 Frontmatter (name + description)
□ C1-F04 Purpose Block (4 fields)
□ C1-F09 Context Anchor
□ C1-F10 Protocol-First
□ C6-F13 Feature Registry planned
□ English only
□ < 300 lines
```

---

*templates.md v1.0.0 | skill-architect v9.0.0*
```

---

## 9.7 reference/quality-gates.md (COMPLETE)

```markdown
# Quality Gates

L1-L10 validation with feature tracking.

---

## L1: Structure

| # | Check | Pass |
|---|-------|------|
| C3-F01 | SKILL.md exists | ✅ |
| C3-F01 | README-{name}.md exists | ✅ |
| C3-F01 | SKILL.md < 300 lines | ✅ |
| C3-F01 | Frontmatter valid | ✅ |
| C3-F01 | Body in English | ✅ |

---

## L2: Content

| # | Check | Pass |
|---|-------|------|
| C3-F02 | Purpose section (4 fields) | ✅ |
| C3-F02 | Triggers in description | ✅ |
| C3-F02 | Version vX.Y.Z | ✅ |
| C3-F02 | Context anchor | ✅ |

---

## L3: Logic

| # | Check | Pass |
|---|-------|------|
| C3-F03 | State machine clear | ✅ |
| C3-F03 | Blocking points ⛔ | ✅ |
| C3-F03 | No circular deps | ✅ |
| C3-F03 | Recovery defined | ✅ |

---

## L4: Naming

| # | Check | Pass |
|---|-------|------|
| C3-F04 | Folder: kebab-case | ✅ |
| C3-F04 | Files: kebab-case.ext | ✅ |
| C3-F04 | Version: vX.Y.Z | ✅ |

---

## L5: Integration

| # | Check | Pass |
|---|-------|------|
| C3-F05 | MANIFEST.md if reference/ | ✅ |
| C3-F05 | Scripts executable | ✅ |
| C3-F05 | Protocols numbered P0X | ✅ |
| C3-F05 | Footers synced | ✅ |

---

## L6: Testing

| # | Check | Pass |
|---|-------|------|
| C3-F06 | Primary flow works | ✅ |
| C3-F06 | Edge cases handled | ✅ |
| C3-F06 | Errors clear | ✅ |

---

## L7: Knowledge Redundancy

| # | Check | Pass | Fail |
|---|-------|------|------|
| C3-F07 | No concept explanations | ✅ | "what is X" |
| C3-F07 | No pattern tutorials | ✅ | Full XML templates |
| C3-F07 | Tables over prose | ✅ | Verbose paragraphs |

**Quick Test:** "Delete this. Still works?" YES = delete.

**Redundancy Score:**
| Score | Verdict |
|-------|---------|
| 0-10% | ✅ Lean |
| 10-30% | 🟡 Review |
| 30%+ | 🔴 Prune |

---

## L8: Version Integrity

| # | Check | Pass |
|---|-------|------|
| C3-F08 | Version in description | ✅ |
| C3-F08 | Header matches | ✅ |
| C3-F08 | Footers synced | ✅ |
| C3-F08 | MANIFEST matches | ✅ |

---

## L9: Documentation

| # | Check | Pass |
|---|-------|------|
| C3-F09 | README-{name}.md | ✅ |
| C3-F09 | CHANGELOG-{name}.md | ✅ |
| C3-F09 | docs/vX.Y.Z/ exists | ✅ |
| C3-F09 | DIFF present | ✅ |
| C3-F09 | LOGIC-TREE present | ✅ |
| C3-F09 | SCAN present | ✅ |
| C3-F09 | FEATURE-REGISTRY present | ✅ |

---

## L10: Feature Registry (NEW)

| # | Check | Pass |
|---|-------|------|
| C3-F10 | FEATURE-REGISTRY.md exists | ✅ |
| C3-F10 | All features numbered | ✅ |
| C3-F10 | Line counts present | ✅ |
| C3-F10 | Categories complete | ✅ |
| C3-F10 | Version comparison | ✅ |

---

## Validation Commands

```bash
bash scripts/validate.sh /path           # L1-L6
bash scripts/validate.sh --degrade /a /b # NEVER DEGRADE
bash scripts/validate.sh --docs /path    # L9
bash scripts/feature-registry.sh /path   # L10
bash scripts/audit.sh /path              # L1-L10
bash scripts/genetic-audit.sh /path      # Inheritance
```

---

*quality-gates.md v1.0.0 | skill-architect v9.0.0*
```

---

## 9.8 scripts/genetic-audit.sh (FROM v8.7.0)

```bash
#!/bin/bash
# genetic-audit.sh — "Eat your own dog food" verification
# Usage: bash genetic-audit.sh /path/to/skill
# v1.0.0 | skill-architect v9.0.0

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SKILL_PATH="${1:-.}"

echo "═══════════════════════════════════════════════════════"
echo "              GENETIC AUDIT v1.0.0"
echo "═══════════════════════════════════════════════════════"

if [ ! -f "$SKILL_PATH/SKILL.md" ]; then
    echo -e "${RED}❌ SKILL.md not found${NC}"
    exit 1
fi

INHERITED=0
LOST=0

# PHASE 1: Parent Genes
echo -e "${BLUE}═══ PHASE 1: PARENT GENES ═══${NC}"

declare -A PARENT_GENES

grep -q "< 300\|300 lines" "$SKILL_PATH/SKILL.md" 2>/dev/null && \
    PARENT_GENES["C1-F02"]="size_limit" && echo -e "${GREEN}  ✓ C1-F02${NC}"
grep -q "NEVER DEGRADE" "$SKILL_PATH/SKILL.md" 2>/dev/null && \
    PARENT_GENES["C1-F06"]="never_degrade" && echo -e "${GREEN}  ✓ C1-F06${NC}"
grep -q "🟢\|🟡\|🔴" "$SKILL_PATH/SKILL.md" 2>/dev/null && \
    PARENT_GENES["C1-F10"]="session" && echo -e "${GREEN}  ✓ C1-F10${NC}"
[ -d "$SKILL_PATH/protocols" ] && \
    PARENT_GENES["C2-F01"]="protocols" && echo -e "${GREEN}  ✓ C2-F01${NC}"
grep -q "⛔" "$SKILL_PATH/SKILL.md" 2>/dev/null && \
    PARENT_GENES["C1-F09"]="blocking" && echo -e "${GREEN}  ✓ C1-F09${NC}"
head -1 "$SKILL_PATH/SKILL.md" | grep -q "^---" && \
    PARENT_GENES["C1-F01"]="frontmatter" && echo -e "${GREEN}  ✓ C1-F01${NC}"
grep -q "FEATURE-REGISTRY" "$SKILL_PATH/SKILL.md" 2>/dev/null && \
    PARENT_GENES["C6-F13"]="registry" && echo -e "${GREEN}  ✓ C6-F13${NC}"
grep -q "Purpose\|serves" "$SKILL_PATH/SKILL.md" 2>/dev/null && \
    PARENT_GENES["C1-F04"]="purpose" && echo -e "${GREEN}  ✓ C1-F04${NC}"
grep -q "Context Anchor\|⚙️" "$SKILL_PATH/SKILL.md" 2>/dev/null && \
    PARENT_GENES["C1-F09b"]="anchor" && echo -e "${GREEN}  ✓ C1-F09b${NC}"

PARENT_COUNT=${#PARENT_GENES[@]}
echo "Parent genes: $PARENT_COUNT"

# PHASE 2: Child Requirements  
echo ""
echo -e "${BLUE}═══ PHASE 2: CHILD REQUIREMENTS ═══${NC}"

declare -A CHILD_REQS
TEMPLATES="$SKILL_PATH/reference/templates.md"

[ -f "$TEMPLATES" ] && {
    grep -q "< 300" "$TEMPLATES" && CHILD_REQS["C1-F02"]="✅"
    grep -q "NEVER DEGRADE" "$TEMPLATES" && CHILD_REQS["C1-F06"]="✅"
    grep -q "🟢\|session" "$TEMPLATES" && CHILD_REQS["C1-F10"]="✅"
    grep -q "Protocol-First" "$TEMPLATES" && CHILD_REQS["C2-F01"]="✅"
    grep -q "⛔" "$TEMPLATES" && CHILD_REQS["C1-F09"]="✅"
    grep -q "frontmatter\|name:" "$TEMPLATES" && CHILD_REQS["C1-F01"]="✅"
    grep -q "FEATURE-REGISTRY" "$TEMPLATES" && CHILD_REQS["C6-F13"]="✅"
    grep -q "Purpose Block" "$TEMPLATES" && CHILD_REQS["C1-F04"]="✅"
    grep -q "Context Anchor" "$TEMPLATES" && CHILD_REQS["C1-F09b"]="✅"
}

CHILD_COUNT=${#CHILD_REQS[@]}
echo "Child requirements: $CHILD_COUNT"

# PHASE 3: Compare
echo ""
echo -e "${BLUE}═══ PHASE 3: INHERITANCE ═══${NC}"
echo "| Gene | Status |"
echo "|------|--------|"

for gene in "${!PARENT_GENES[@]}"; do
    if [ -n "${CHILD_REQS[$gene]}" ]; then
        echo -e "| $gene | ${GREEN}✅${NC} |"
        ((INHERITED++))
    else
        echo -e "| $gene | ${RED}❌${NC} |"
        ((LOST++))
    fi
done

# VERDICT
echo ""
PERCENT=0
[ "$PARENT_COUNT" -gt 0 ] && PERCENT=$((INHERITED * 100 / PARENT_COUNT))

echo "═══════════════════════════════════════════════════════"
echo "Inherited: $INHERITED/$PARENT_COUNT ($PERCENT%)"

if [ "$PERCENT" -ge 80 ]; then
    echo -e "${GREEN}✅ ALIGNED${NC}"
else
    echo -e "${RED}❌ GAPS${NC}"
fi
echo "═══════════════════════════════════════════════════════"
```

---

## 9.9 LOGIC-TREE Template (with File Dependencies)

```markdown
# LOGIC-TREE: skill-architect v9.0.0

---

## Main Flow

```
[START]
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  P01-init                                               │
│  Trigger: create skill, update, refactor, checkup      │
│  Output: Ready for planning                             │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  P02-plan ⛔ BLOCKING                                   │
│  Wait: "yes", "go", "proceed"                           │
│  Invalid: "ok", "got it"                                │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  P03-build                                              │
│  PRE-BUILD → Create → Validate → Registry              │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  P04-deliver ⛔ BLOCKING                                │
│  Package → Docs → Registry → Deliver                   │
└─────────────────────────────────────────────────────────┘
    │
    ▼
[END]
```

---

## State Transitions

| From | Condition | To |
|------|-----------|-----|
| START | request | P01 |
| P01 | config done | P02 |
| P02 | confirmed | P03 |
| P02 | question | P02 |
| P03 | pass | P04 |
| P03 | fail | P03 |
| P04 | audit | END |
| P04 | skip | END |

---

## File Dependencies

```
SKILL.md
├── → protocols/P00-router.md
├── → scripts/validate.sh
└── → scripts/feature-registry.sh

protocols/P02-plan.md
└── → reference/templates.md

protocols/P03-build.md
├── → scripts/validate.sh
└── → scripts/feature-registry.sh

protocols/P04-deliver.md
├── → scripts/validate.sh --degrade
├── → scripts/feature-registry.sh
├── → scripts/package.sh
├── → scripts/generate-docs.sh
└── → scripts/genetic-audit.sh
```

---

## Quality Gates

| Gate | Check | Script |
|------|-------|--------|
| G1-G5 | Structure | validate.sh |
| G6 | Confirmation | P02-plan |
| G7 | NEVER DEGRADE | validate.sh --degrade |
| G8 | FEATURE-REGISTRY | feature-registry.sh |

---

## Inherited Genes

| Gene | Code | Required |
|------|------|----------|
| Purpose Block | C1-F04 | ✅ |
| Context Anchor | C1-F09 | ✅ |
| Session Indicator | C1-F10 | ✅ |
| Protocol-First | C2-F01 | ✅ |
| Feature Registry | C6-F13 | ✅ |
| NEVER DEGRADE | C1-F06 | ✅ |

---

*LOGIC-TREE-skill-architect-v9.0.0.md*
```

---

# PART 10: SUCCESS CRITERIA

| Check | Required |
|-------|----------|
| Features tracked | 92+ with C#-F## codes |
| Categories | 7 (C1-C7) |
| FEATURE-REGISTRY.md | Generated and present |
| LOGIC-TREE | With File Dependencies |
| genetic-audit.sh | Present and ALIGNED |
| validate.sh | All modes working |
| NEVER DEGRADE | PASSED |

---

# PART 11: BUILD CHECKLIST

```
□ Create skill-architect-v9.0.0/
□ SKILL.md (85 lines, C1 features)
□ protocols/ (5 files, C2 features)
□ reference/ (6 files, C5 features)
□ scripts/ (6 files including feature-registry.sh, genetic-audit.sh)
□ Run feature-registry.sh → FEATURE-REGISTRY.md
□ Run validate.sh → PASS
□ Run genetic-audit.sh → ALIGNED
□ Generate LOGIC-TREE with File Dependencies
□ Package .skill
□ Deliver with FEATURE-REGISTRY comparison
```

---

*SPEC-skill-architect-v9.0.0-REGISTRY.md | Complete specification with mandatory feature tracking*
