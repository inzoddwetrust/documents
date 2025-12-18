# PATCH: skill-architect v8.6.0

Issues found during v8.5.0 simulation. Apply in next release.

**Created:** 2025-12-12  
**From:** P08 Simulation of v8.5.0

---

## 🔴 Critical Issues

### ISSUE-005: NEVER DEGRADE has no automated enforcement
- Fundamental protection doesn't work
- I violated it myself (proof of failure)  
- **Fix:** validate-degrade.sh with REQUIRE prev docs

### ISSUE-006: NEVER DEGRADE check is in wrong place
- Check sits in P04 (build) where nothing to compare yet
- **Fix:** Move to P06/P07 as BLOCKING gate

### ISSUE-002: generate-docs.sh causes massive content loss
- Script generates templates, not content
- **DAMAGE:** 822 lines would have been LOST (caught and fixed)
- **Fix:** Require prev docs for "update" mode

---

## 🟡 Medium Issues

### ISSUE-001: Protocol footers show v8.4.0

**Location:** `reference/protocols/*.md` (9 of 10 files)

**Current state:**
```
*P0X-name.md v1.X.0 | skill-architect v8.4.0*
```

**Expected:**
```
*P0X-name.md v1.X.0 | skill-architect v8.5.0*
```

**Fix:**
```bash
# Update all protocol footers
cd reference/protocols
sed -i 's/skill-architect v8.4.0/skill-architect v8.5.0/g' *.md
# Or use: bash scripts/update-version.sh . 8.5.0
```

**Files affected:**
- P00-router.md
- P01-activation.md
- P02-config.md
- P03-planning.md
- P04-build.md
- P05-validate.md
- P06-delivery-skill.md
- P08-simulation.md
- P09-full-audit.md

(P07-closure.md already v8.5.0)

---

### ISSUE-002: generate-docs.sh causes massive content loss

**Location:** `scripts/generate-docs.sh` + P07 workflow

**Problem:** Script generates EMPTY TEMPLATES. When used to "update" existing docs, it REPLACES detailed content with blank templates.

**ACTUAL DAMAGE in v8.5.0:**

| Document | v8.4.0 | v8.5.0 | Loss |
|----------|--------|--------|------|
| PLAN | 639 | 52 | 🔴 **-92%** |
| DECISIONS | 136 | 30 | 🔴 **-78%** |
| BACKLOG | 78 | 43 | 🔴 **-45%** |
| DIFF | 131 | 76 | 🟡 -42% |
| SCAN | 139 | 100 | 🟡 -29% |
| LOGIC-TREE | 222 | 203 | ✅ -9% (fixed manually) |

**Total lines lost:** 639+136+78+131+139+222 = 1345 → 504 = **~840 lines GONE**

**Root cause:** generate-docs.sh is for NEW skills, not updates. P07 doesn't require previous version docs.

**Fix — Multi-part:**

**A) generate-docs.sh must REQUIRE previous docs for updates:**

```bash
#!/bin/bash
# generate-docs.sh v2.0

MODE="$3"  # "new" or "update"
PREV_DOCS="$4"  # path to previous version docs

if [ "$MODE" == "update" ]; then
    if [ -z "$PREV_DOCS" ] || [ ! -d "$PREV_DOCS" ]; then
        echo "❌ ERROR: Update mode requires previous docs!"
        echo "Usage: bash generate-docs.sh . X.Y.Z update /path/to/prev-docs"
        exit 1
    fi
    
    # Copy previous docs as base
    echo "📋 Copying previous docs as base..."
    for file in "$PREV_DOCS"/*.md; do
        # ... rename to new version, preserve content
    done
fi
```

**B) P07 must require previous docs for ANY update:**

```markdown
### Prerequisites for Update (not new skill)

⛔ BLOCKING: Previous version docs required!

```bash
# User must provide previous docs
ls /path/to/skill-name-vPREV-docs/
```

If previous docs not available:
1. Ask user to provide them
2. Do NOT proceed without them
3. NEVER generate blank templates over existing content
```

**C) Add warning to generate-docs.sh output:**

```
⚠️ WARNING: This generates TEMPLATES only!
⚠️ For updates, use: bash generate-docs.sh . X.Y.Z update /prev-docs
⚠️ NEVER replace existing detailed docs with templates!
```

---

### ISSUE-003: P08 should create PATCH document

**Location:** `reference/protocols/P08-simulation.md`

**Problem:** P08 doesn't specify creating PATCH document when issues found.

**Add to P08 Steps:**

```markdown
### 7. Create Patch Document (if issues found)

If simulation found issues:

```bash
mkdir -p /home/claude/patches
```

Create `PATCH-{skill-name}-v{NEXT}.md`:

| Section | Content |
|---------|---------|
| Critical Issues | Blockers requiring immediate fix |
| Medium Issues | Should fix in next release |
| Minor Issues | Nice to have |

Each issue:
- Location (file path)
- Current state
- Expected state
- Fix command/steps

User downloads PATCH → applies in next release.
```

---

### ISSUE-005: NEVER DEGRADE has no automated enforcement

**Location:** Entire system

**Problem:** NEVER DEGRADE is a CRITICAL rule but has NO automated check. It exists only as:
- Text in SKILL.md (rules 9-10)
- Manual checklist in P04-build (wrong place!)
- Word mention check in genetic-audit.sh (checks if word exists, not if content preserved!)

**Evidence:** I violated NEVER DEGRADE myself — replaced ALL docs with templates. System didn't catch it.

**ACTUAL DAMAGE:** ~840 lines of documentation LOST in v8.5.0

**Current state:**
```
NEVER DEGRADE = "Claude, please don't delete anything"
Enforcement = NONE
Previous docs = NOT REQUIRED
```

**Expected:**
```
NEVER DEGRADE = automated pre/post comparison
Enforcement = BLOCKING gate in P06/P07
Previous docs = MANDATORY for updates
```

**Proposed solution — validate-degrade.sh v1.0:**

```bash
#!/bin/bash
# validate-degrade.sh — BLOCKING check for content loss
# Usage: bash validate-degrade.sh <old-dir> <new-dir>
# Exit: 0 = pass, 1 = fail (BLOCKS delivery)
# v1.0.0 | skill-architect v8.6.0

set -e

OLD="$1"
NEW="$2"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "═══════════════════════════════════════════════════════"
echo "       ⛔ NEVER DEGRADE VALIDATOR v1.0.0"
echo "═══════════════════════════════════════════════════════"
echo ""

# ═══════════════════════════════════════════════════════════
# PHASE 0: REQUIRE previous docs
# ═══════════════════════════════════════════════════════════
if [ -z "$OLD" ] || [ ! -d "$OLD" ]; then
    echo -e "${RED}❌ ERROR: Previous version docs REQUIRED!${NC}"
    echo ""
    echo "Usage: bash validate-degrade.sh /path/to/old /path/to/new"
    echo ""
    echo "You MUST provide previous docs for comparison."
    echo "This is a BLOCKING requirement — no exceptions."
    exit 1
fi

if [ -z "$NEW" ] || [ ! -d "$NEW" ]; then
    echo -e "${RED}❌ ERROR: New version path required!${NC}"
    exit 1
fi

echo "OLD: $OLD"
echo "NEW: $NEW"
echo ""

VIOLATIONS=0
WARNINGS=0

# ═══════════════════════════════════════════════════════════
# PHASE 1: Check for deleted files
# ═══════════════════════════════════════════════════════════
echo -e "${YELLOW}═══ PHASE 1: FILE DELETION CHECK ═══${NC}"
echo ""

for file in "$OLD"/*.md; do
    if [ -f "$file" ]; then
        basename_old=$(basename "$file")
        # Extract doc type (PLAN, DIFF, etc) from old naming
        doc_type=$(echo "$basename_old" | grep -oE '^[0-9]+-[A-Z-]+' | sed 's/^[0-9]*-//' || echo "$basename_old")
        
        # Check if equivalent exists in new (any naming convention)
        found=false
        for new_file in "$NEW"/*.md; do
            if [ -f "$new_file" ] && echo "$new_file" | grep -qi "$doc_type"; then
                found=true
                break
            fi
        done
        
        if [ "$found" = false ]; then
            echo -e "${RED}❌ FILE DELETED: $basename_old (no equivalent in new)${NC}"
            ((VIOLATIONS++))
        else
            echo -e "${GREEN}✅ $doc_type: found${NC}"
        fi
    fi
done
echo ""

# ═══════════════════════════════════════════════════════════
# PHASE 2: Check line count (>30% loss = violation)
# ═══════════════════════════════════════════════════════════
echo -e "${YELLOW}═══ PHASE 2: CONTENT VOLUME CHECK ═══${NC}"
echo ""

echo "| Document | Old | New | Change |"
echo "|----------|-----|-----|--------|"

for old_file in "$OLD"/*.md; do
    if [ -f "$old_file" ]; then
        basename_old=$(basename "$old_file")
        doc_type=$(echo "$basename_old" | grep -oE '[A-Z]+-?[A-Z]*' | head -1)
        
        # Find matching new file
        for new_file in "$NEW"/*.md; do
            if [ -f "$new_file" ] && echo "$new_file" | grep -qi "$doc_type"; then
                old_lines=$(wc -l < "$old_file")
                new_lines=$(wc -l < "$new_file")
                
                if [ "$old_lines" -gt 0 ]; then
                    change=$((new_lines * 100 / old_lines - 100))
                    
                    if [ "$change" -lt -30 ]; then
                        echo -e "| $doc_type | $old_lines | $new_lines | ${RED}${change}% ❌${NC} |"
                        ((VIOLATIONS++))
                    elif [ "$change" -lt -10 ]; then
                        echo -e "| $doc_type | $old_lines | $new_lines | ${YELLOW}${change}% ⚠️${NC} |"
                        ((WARNINGS++))
                    else
                        echo "| $doc_type | $old_lines | $new_lines | ${change}% ✅ |"
                    fi
                fi
                break
            fi
        done
    fi
done
echo ""

# ═══════════════════════════════════════════════════════════
# PHASE 3: Check key sections preserved
# ═══════════════════════════════════════════════════════════
echo -e "${YELLOW}═══ PHASE 3: KEY SECTIONS CHECK ═══${NC}"
echo ""

SECTIONS=("## Purpose" "## Main Flow" "## Blocking" "## Quality" "## Context" "## Constraints")

for old_file in "$OLD"/*.md; do
    if [ -f "$old_file" ]; then
        basename_old=$(basename "$old_file")
        doc_type=$(echo "$basename_old" | grep -oE '[A-Z]+-?[A-Z]*' | head -1)
        
        for new_file in "$NEW"/*.md; do
            if [ -f "$new_file" ] && echo "$new_file" | grep -qi "$doc_type"; then
                for section in "${SECTIONS[@]}"; do
                    if grep -q "$section" "$old_file" 2>/dev/null; then
                        if ! grep -q "$section" "$new_file" 2>/dev/null; then
                            echo -e "${RED}❌ SECTION REMOVED: '$section' from $doc_type${NC}"
                            ((VIOLATIONS++))
                        fi
                    fi
                done
                break
            fi
        done
    fi
done
echo ""

# ═══════════════════════════════════════════════════════════
# VERDICT
# ═══════════════════════════════════════════════════════════
echo "═══════════════════════════════════════════════════════"
echo "NEVER DEGRADE VALIDATION RESULT"
echo "═══════════════════════════════════════════════════════"
echo ""
echo -e "Violations: ${RED}$VIOLATIONS${NC}"
echo -e "Warnings:   ${YELLOW}$WARNINGS${NC}"
echo ""

if [ "$VIOLATIONS" -eq 0 ]; then
    echo -e "${GREEN}✅ NEVER DEGRADE: PASSED${NC}"
    echo ""
    echo "Safe to proceed with delivery."
    exit 0
else
    echo -e "${RED}════════════════════════════════════════════════════${NC}"
    echo -e "${RED}⛔ NEVER DEGRADE: FAILED — $VIOLATIONS violations!${NC}"
    echo -e "${RED}════════════════════════════════════════════════════${NC}"
    echo ""
    echo "DELIVERY BLOCKED. You must:"
    echo "1. Review violations above"
    echo "2. Restore lost content from previous version"
    echo "3. Re-run this check"
    echo ""
    echo "DO NOT proceed without fixing violations!"
    exit 1
fi
```

**Integration — P06-delivery-skill.md:**

```markdown
### ⛔ NEVER DEGRADE Check (BLOCKING)

Before packaging, you MUST run:

```bash
bash scripts/validate-degrade.sh /path/to/old-skill /path/to/new-skill
```

| Result | Action |
|--------|--------|
| PASSED | Continue to packaging |
| FAILED | ⛔ STOP — restore content, re-run |

**Previous version is REQUIRED.** Ask user to provide if not available.

This check is NON-NEGOTIABLE. No exceptions.
```

**Integration — P07-closure.md:**

```markdown
### ⛔ NEVER DEGRADE Check (Docs)

If updating existing docs (not new skill):

```bash
bash scripts/validate-degrade.sh /path/to/old-docs /path/to/new-docs
```

**Previous docs are REQUIRED for updates.**
```

---

### ISSUE-006: NEVER DEGRADE check is in wrong protocol

**Location:** `reference/protocols/P04-build.md`

**Problem:** NEVER DEGRADE checklist sits in P04 (build phase) where there's nothing to compare yet. We're still CREATING files — no OLD vs NEW comparison possible.

**Current flow:**
```
P04 (build) → "Please don't delete anything" (manual reminder)
P06 (delivery) → Package and ship (no check!)
P07 (closure) → Generate docs (no check!)
```

**Correct flow:**
```
P04 (build) → Create files
P06 (delivery) → validate-degrade.sh OLD_SKILL vs NEW_SKILL ⛔
P07 (closure) → validate-degrade.sh OLD_DOCS vs NEW_DOCS ⛔
```

**Changes needed:**

1. **P04-build.md** — Remove or simplify NEVER DEGRADE section to just a reminder:
```markdown
## ⚠️ NEVER DEGRADE Reminder

While building, remember:
- Don't remove working functionality
- Don't replace specific with abstract
- When in doubt, keep both old and new

Automated check runs in P06 before delivery.
```

2. **P06-delivery-skill.md** — Add actual check:
```markdown
### ⛔ NEVER DEGRADE Check (BLOCKING)

Before packaging:

```bash
bash scripts/validate-degrade.sh /path/to/old-skill /path/to/new-skill
```

| Result | Action |
|--------|--------|
| PASSED | Continue to packaging |
| FAILED | ⛔ STOP — review violations, restore content |
```

3. **P07-closure.md** — Add docs check:
```markdown
### NEVER DEGRADE Check (Docs)

If updating existing docs:

```bash
bash scripts/validate-degrade.sh old-docs/ new-docs/
```
```

**Rationale:** Check belongs where comparison is possible, not where files are being created.

---

## 🟢 Minor Issues

### ISSUE-004: Cyrillic in SKILL.md examples

**Location:** `SKILL.md` lines containing "да/yes/go"

**Status:** Known issue, documented. Acceptable as examples show multilingual triggers.

**Action:** No fix needed, document in README.

---

## Implementation Checklist

```
□ ISSUE-005: Create validate-degrade.sh script (with REQUIRE prev docs)
□ ISSUE-006: Move NEVER DEGRADE from P04 to P06/P07 (BLOCKING)
□ ISSUE-002: Update generate-docs.sh to require prev docs for updates
□ ISSUE-003: Add PATCH creation to P08-simulation.md
□ ISSUE-001: Update protocol footers to v8.6.0
□ Update CHANGELOG
□ Update version to 8.6.0
□ Run validate-degrade.sh on final result
```

---

## Estimated Effort

| Issue | Priority | Time |
|-------|----------|------|
| ISSUE-005 | 🔴 CRITICAL | 60 min |
| ISSUE-006 | 🔴 CRITICAL | 20 min |
| ISSUE-002 | 🔴 HIGH | 45 min |
| ISSUE-003 | 🟡 Medium | 15 min |
| ISSUE-001 | 🟡 Medium | 5 min |
| **Total** | | ~2.5 hours |

---

## Priority Order

1. **ISSUE-005** — Create validate-degrade.sh (the enforcement tool)
2. **ISSUE-006** — Move check to P06/P07 (put it where it belongs)
3. **ISSUE-002** — generate-docs.sh require prev docs (prevent future loss)
4. **ISSUE-003** — PATCH in P08 (document future issues)
5. **ISSUE-001** — Footer versions (cosmetic)

---

*PATCH-skill-architect-v8.6.0.md | skill-architect v8.5.0 → v8.6.0*
