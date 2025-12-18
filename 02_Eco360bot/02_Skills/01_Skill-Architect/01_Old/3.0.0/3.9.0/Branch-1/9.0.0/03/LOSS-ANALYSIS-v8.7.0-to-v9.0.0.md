# LOSS ANALYSIS: v8.7.0 → v9.0.0

What was lost, at risk, or correctly removed.

---

## 🔴 CRITICAL LOSSES (Must restore)

### 1. Inheritance System ("Genes")

**v8.7.0 had:**
- templates.md with Protocol-First, Purpose Block, Template Types
- genetic-audit.md + genetic-audit.sh (248 lines)
- Core genes: Purpose table, Context anchor, Token counter, Blocking points

**v9 lost:**
- Protocol-First rule for children
- Template Types (Analysis/Content/Data/Code)
- Full Purpose Block (serves/goal/method/success)
- Genetic audit entirely

**Impact:** Children skills won't inherit best practices.

**Action:** RESTORE genetic audit concept + templates inheritance.

---

### 2. L7-L9 Quality Layers

**v8.7.0 had:**
- L7: Knowledge Redundancy (prevents bloat)
- L8: Version Integrity (sync check)
- L9: Documentation (naming validation)

**v9 kept only:** G1-G7 (basic gates)

**Lost:**
- L7 "Delete this section. Would skill still work?" test
- L7 LLM-Native vs Skill-Specific classification
- L7 Redundancy Score (0-10% lean, 10-30% review, 30%+ prune)
- L8 version sync bash command
- L9 documentation naming validation

**Impact:** Risk of bloat returning, version drift, naming errors.

**Action:** RESTORE L7-L9 to quality gates.

---

### 3. SSOT (Single Source of Truth)

**v8.7.0 had:**
- ssot-check.md with rules
- ssot-check.sh (143 lines)
- Duplicate detection

**v9 lost:** Entirely

**Impact:** Definitions can drift between files.

**Action:** RESTORE SSOT concept to reference.

---

### 4. Simulation Protocol Details

**v8.7.0 P05-simulation had:**
- Load Skill check
- Check Activation (frontmatter, triggers, version)
- Check Protocol Flow (all exist, Next pointers, no circular)
- Check Cross-References (grep -r "P0[0-9]")
- Check Versions (grep -h "skill-architect v")
- PATCH creation if issues found

**v9 P04-deliver has:** Only "optional audit" mention

**Impact:** Lost detailed simulation procedure.

**Action:** RESTORE simulation steps to P04-deliver audit section.

---

### 5. Context Management Strategy

**v8.7.0 had:**
- context-management.md
- When to Compact rules
- What to PRESERVE vs DROP
- Recovery procedure

**v9 has:** Only session-indicator.md

**Lost:**
- Compaction triggers (🟡🔴, >30 messages, before major phase)
- PRESERVE list: protocol, blocking points, skill name, file paths, decisions
- DROP list: verbose outputs, full file contents, duplicates

**Impact:** No guidance for long session handling.

**Action:** MERGE context-management into session-indicator.

---

### 6. Commands SSOT

**v8.7.0 had:**
- commands.md with ALL bash commands
- Packaging, Backup, Unpack, Validation, Diagnostics sections

**v9 lost:** Entirely (commands scattered in protocols)

**Impact:** No single reference for commands.

**Action:** RESTORE commands.md or consolidate in templates.

---

### 7. Docs System Architecture

**v8.7.0 had:**
- docs-system.md (167 lines)
- Full architecture diagram
- Naming convention
- 7 document types with required/optional
- Footer convention
- Workflow integration
- L9 Quality Gate
- Lean Principle

**v9 has:** Only diff-format.md

**Lost:**
- Architecture diagram
- Document types table
- Lean Principle ("SKILL.md contains ONLY what Claude needs")

**Action:** RESTORE docs-system or merge key parts.

---

## 🟡 AT RISK (Simplified but may need more)

### 8. Project Mode

**v8.7.0 had:**
- project-mode.md
- project-modules.md
- project-filters.md
- project-import.md
- E-006, E-007, E-008 evaluations

**v9 decision:** Removed for simplification

**Trade-off:** v9 is SKILL-ONLY mode. Project mode is lost functionality.

**Action:** Document explicitly that v9 doesn't support project mode OR restore it.

---

### 9. Self-Diagnostic

**v8.7.0 had:**
- self-diagnostic.md
- self-diagnostic.sh (192 lines)
- Quick health check

**v9 has:** audit.sh only

**Trade-off:** audit.sh covers this but less focused.

**Action:** Consider adding "diagnose" as alias to quick audit.

---

### 10. PRE-BUILD CHECKPOINT

**v8.7.0 had:**
- Explicit in templates.md
- Trigger: "After web search, long conversation, any doubt"
- Action: re-read SKILL.md

**v9 lost:** Not explicitly documented

**Impact:** Context drift after web search.

**Action:** ADD PRE-BUILD CHECKPOINT to P03-build.

---

## 🟢 CORRECTLY SIMPLIFIED

### 11. Protocols Merge

**v8.7.0:** P05-simulation + P06-audit separate

**v9:** Merged into P04-deliver audit section

**Status:** ✅ OK - reduces overhead while keeping functionality

---

### 12. Scripts Consolidation

**v8.7.0:** 12 scripts (2,682 lines)

**v9:** 4-5 scripts (~400 lines)

**Status:** ✅ OK - same functionality, less files

BUT need to ensure consolidated scripts have:
- --docs mode
- --naming mode
- SSOT checks
- L7-L9 checks

---

### 13. Reference Files Reduction

**v8.7.0:** 23 reference files

**v9:** 6-8 reference files

**Status:** ✅ OK if content merged properly

BUT engines.md, virtual-testing.md, testing-framework.md content needs home.

---

## 📋 RESTORE CHECKLIST

### Must Add to v9.0.0 Spec:

1. **templates.md additions:**
   - [ ] Protocol-First (MANDATORY) section
   - [ ] Purpose Block with serves/goal/method/success
   - [ ] Template Types (Analysis/Content/Data/Code)
   - [ ] PRE-BUILD CHECKPOINT trigger

2. **quality-gates.md additions:**
   - [ ] L7: Knowledge Redundancy
   - [ ] L8: Version Integrity
   - [ ] L9: Documentation naming

3. **session-indicator.md additions:**
   - [ ] When to Compact rules
   - [ ] PRESERVE vs DROP lists
   - [ ] Recovery procedure

4. **validate.sh additions:**
   - [ ] --docs mode
   - [ ] --naming mode
   - [ ] --ssot mode
   - [ ] L7-L9 checks

5. **P04-deliver.md additions:**
   - [ ] Full simulation steps (load, check activation, check flow, etc.)
   - [ ] PATCH creation logic

6. **New files to add:**
   - [ ] genetic-audit.md (inheritance verification)
   - [ ] commands.md OR merge into templates

7. **evaluations.md:**
   - [ ] Keep E-001 to E-005 (Tool Mode)
   - [ ] Add E-006: Inheritance check
   - [ ] Mark Project Mode as "not supported in v9"

---

## 📊 SUMMARY

| Category | v8.7.0 | v9 v1/v2 | Gap |
|----------|--------|----------|-----|
| Inheritance | Full | ❌ None | CRITICAL |
| L7-L9 | Full | ❌ Basic only | CRITICAL |
| SSOT | Full | ❌ None | HIGH |
| Context mgmt | Full | ⚠️ Partial | MEDIUM |
| Simulation | Full | ⚠️ Brief | MEDIUM |
| Commands ref | Full | ❌ None | MEDIUM |
| Docs system | Full | ⚠️ Partial | LOW |
| Project mode | Full | ❌ Removed | ACCEPTED |

---

**Conclusion:** v9 specs were too aggressive in cutting. Need to restore ~30% of removed content while keeping lean architecture.

---

*LOSS-ANALYSIS-v8.7.0-to-v9.0.0.md | 2025-12-12*
