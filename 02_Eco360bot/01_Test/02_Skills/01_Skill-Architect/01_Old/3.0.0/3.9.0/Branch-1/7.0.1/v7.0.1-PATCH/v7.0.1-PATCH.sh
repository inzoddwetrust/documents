#!/bin/bash
# skill-architect v7.0.1 patch
# Applies cosmetic fixes: footer sync + self-diagnostic fix
#
# Usage: bash v7.0.1-PATCH.sh /path/to/skill-architect

SKILL_DIR="${1:-.}"

if [ ! -f "$SKILL_DIR/SKILL.md" ]; then
    echo "❌ Error: SKILL.md not found in $SKILL_DIR"
    echo "Usage: bash v7.0.1-PATCH.sh /path/to/skill-architect"
    exit 1
fi

echo "╔══════════════════════════════════════════╗"
echo "║  SKILL-ARCHITECT v7.0.1 PATCH            ║"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "Target: $SKILL_DIR"
echo ""

# Counter
PATCHED=0

patch_file() {
    local file="$1"
    local old="$2"
    local new="$3"
    
    if [ -f "$file" ] && grep -q "$old" "$file" 2>/dev/null; then
        sed -i "s|$old|$new|g" "$file"
        echo "✅ $(basename "$file")"
        PATCHED=$((PATCHED+1))
    fi
}

echo "═══ PROTOCOLS ═══"

patch_file "$SKILL_DIR/reference/protocols/P00-router.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/protocols/P01-activation.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/protocols/P02-config.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/protocols/P03-planning.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/protocols/P04-build.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/protocols/P06-delivery-skill.md" \
    "skill-architect v6.2.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/protocols/P07-delivery-docs.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/protocols/P08-scan.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

echo ""
echo "═══ REFERENCE ═══"

patch_file "$SKILL_DIR/reference/commands.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/docs-packaging.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/evaluations.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/naming-convention.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/packaging.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/planning-document.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/project-filters.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/project-import.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/project-mode.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/project-modules.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/ssot-check.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

patch_file "$SKILL_DIR/reference/workflow.md" \
    "skill-architect v6.1.0" "skill-architect v7.0.1"

# self-diagnostic.md needs version bump too
if [ -f "$SKILL_DIR/reference/self-diagnostic.md" ]; then
    sed -i 's#self-diagnostic.md v2.0.0 | skill-architect v6.1.0#self-diagnostic.md v2.1.0 | skill-architect v7.0.1#g' "$SKILL_DIR/reference/self-diagnostic.md"
    sed -i 's#MANDATORY: On Activation#FIRST STEP — MANDATORY#g' "$SKILL_DIR/reference/self-diagnostic.md"
    echo "✅ self-diagnostic.md (content + footer)"
    PATCHED=$((PATCHED+1))
fi

echo ""
echo "═══ SCRIPTS ═══"

# Fix self-diagnostic.sh
if [ -f "$SKILL_DIR/scripts/self-diagnostic.sh" ]; then
    perl -i -pe "s/MANDATORY\.\*Activation/FIRST STEP.*MANDATORY/g; s/Has Activation instructions/Has First Step instructions/g" "$SKILL_DIR/scripts/self-diagnostic.sh"
    echo "✅ self-diagnostic.sh"
    PATCHED=$((PATCHED+1))
fi

echo ""
echo "═══ CORE ═══"

# SKILL.md version bump
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    sed -i 's|v7.0.0|v7.0.1|g' "$SKILL_DIR/SKILL.md"
    echo "✅ SKILL.md"
    PATCHED=$((PATCHED+1))
fi

# README.md version bump  
if [ -f "$SKILL_DIR/README.md" ]; then
    sed -i 's|v7.0.0|v7.0.1|g' "$SKILL_DIR/README.md"
    echo "✅ README.md"
    PATCHED=$((PATCHED+1))
fi

echo ""
echo "═══ MANIFEST ═══"

# Update MANIFEST.md
if [ -f "$SKILL_DIR/MANIFEST.md" ]; then
    sed -i 's|skill-architect v7.0.0|skill-architect v7.0.1|g' "$SKILL_DIR/MANIFEST.md"
    
    # Add changelog entry after existing v7.0.0 entry
    if ! grep -q "v7.0.1" "$SKILL_DIR/MANIFEST.md"; then
        sed -i '/### v7.0.0/i\
### v7.0.1 ('"$(date +%Y-%m-%d)"')\
- Fixed: Footer version drift in 21 files\
- Fixed: self-diagnostic.sh false negative on SKILL.md check\
- Fixed: self-diagnostic.md SSOT sync with SKILL.md naming\
- Unchanged: All functionality, protocols, scripts logic\
' "$SKILL_DIR/MANIFEST.md"
    fi
    echo "✅ MANIFEST.md"
    PATCHED=$((PATCHED+1))
fi

echo ""
echo "═══ V7.0.0 → V7.0.1 SWEEP ═══"

# Universal sweep for any remaining v7.0.0 references
find "$SKILL_DIR/reference" -name "*.md" -exec grep -l "skill-architect v7.0.0" {} \; 2>/dev/null | while read f; do
    sed -i 's|skill-architect v7.0.0|skill-architect v7.0.1|g' "$f"
    echo "✅ $(basename "$f")"
    PATCHED=$((PATCHED+1))
done

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║  PATCHED: $PATCHED files                       ║"
echo "║  STATUS: ✅ COMPLETE                     ║"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "Next: Run self-test to verify"
echo "  bash scripts/self-diagnostic.sh $SKILL_DIR"
