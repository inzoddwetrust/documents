# PLAN: skill-architect v4.6.0 "Memory Budget"

| Field | Value |
|-------|-------|
| Current Version | v4.5.1 |
| Target Version | v4.6.0 |
| Codename | Memory Budget |
| Date | 2025-12-16 |
| Status | PLANNING |

---

## Problem Statement

### Observed Issues

| # | Problem | Frequency | Impact |
|---|---------|-----------|--------|
| 1 | LOGIC-TREE, SCAN docs not produced | ~70% of builds | Missing deliverables |
| 2 | Wrong package extension (.zip vs .skill) | ~50% of builds | User frustration |
| 3 | Protocol drift after ~10 files | ~80% of long builds | Quality degradation |
| 4 | Planning Document skipped | ~60% of sessions | No audit trail |

### Root Cause Analysis

```
P03-build = monolithic block
    │
    ├── 15-30 files in one go
    ├── 10-20 minutes continuous work
    ├── No memory refresh points
    │
    └── Result: cognitive overload
            │
            ├── Forget docs (LOGIC-TREE, SCAN)
            ├── Forget protocol details (.skill extension)
            └── Cut corners on validation
```

**Metaphor:** "Feeding a snake a chunk of meat too large to digest"

---

## Solution Overview

### 1. Memory Budget System (G11)

Universal batching mechanism based on cognitive limits, not file structure.

### 2. Pipeline Restructure

Split P03-build into phases with mandatory checkpoints.

### 3. Mandatory Planning Document

Planning Document becomes blocking artifact, not optional step.

---

## Detailed Specification

### G11: Memory Budget Gene

```markdown
# G11: Memory Budget

## Purpose
Prevent cognitive overload during multi-file production.

## Scope
ANY skill that produces 5+ files in single operation.

## Limits

| Metric | Soft Limit | Hard Limit | Action |
|--------|------------|------------|--------|
| Lines per batch | 300 | 500 | Checkpoint |
| Files per batch | 5 | 8 | Checkpoint |
| Time per batch | 5 min | 8 min | Checkpoint |

## Rule
Batch closes when FIRST limit reached.

## Pre-Build Calculator

Before starting build phase:
1. Count planned files
2. Estimate total lines
3. Calculate expected batches
4. Announce batch plan to user

Formula:
  batches_by_lines = total_lines ÷ 300
  batches_by_files = total_files ÷ 5
  expected_batches = max(batches_by_lines, batches_by_files)

## Inheritance
All child skills that produce files MUST implement G11.
```

### Checkpoint Format

```markdown
# Checkpoint Format Specification

## After Each Batch

┌────────────────────────────────────────┐
│ ✅ Batch {N}/{total} complete          │
│                                        │
│ Created:                               │
│   • file1.md (~80 lines)               │
│   • file2.md (~120 lines)              │
│   • file3.md (~95 lines)               │
│                                        │
│ Batch stats: 3 files, ~295 lines       │
│ Total progress: {done}/{total} files   │
│ ──────────────────────────────────────│
│ NEXT: Batch {N+1} — {description}      │
└────────────────────────────────────────┘

## After All Batches (P03-build complete)

┌────────────────────────────────────────┐
│ 🏁 BUILD PHASE COMPLETE                │
│                                        │
│ Summary:                               │
│   Batches: 5                           │
│   Files: 23                            │
│   Lines: ~2200                         │
│   Time: ~18 min                        │
│                                        │
│ Files by category:                     │
│   • core: 3 ✅                         │
│   • protocols: 5 ✅                    │
│   • reference: 10 ✅                   │
│   • scripts: 5 ✅                      │
│ ──────────────────────────────────────│
│ ⛔ CHECKPOINT: Review before validate  │
│                                        │
│ NEXT: P03-validate                     │
│ Options:                               │
│   1 → Continue to validation           │
│   2 → Review specific files            │
│   3 → Fix issues first                 │
└────────────────────────────────────────┘
```

### New Pipeline Structure

```
P01-init
    │
    ▼
P02-plan ⛔ BLOCKING
    │
    ├── Create Planning Document (MANDATORY)
    ├── Save to /mnt/user-data/outputs/
    ├── User confirms plan
    │
    ▼
P03-build (batched)
    │
    ├── Pre-build: Calculate batches
    │
    ├── Batch 1 ⏸️ checkpoint
    ├── Batch 2 ⏸️ checkpoint
    ├── Batch N ⏸️ checkpoint
    │
    └── Build complete summary
    │
    ▼
P03-validate ⛔ BLOCKING (NEW)
    │
    ├── Re-read Planning Document
    ├── Run genetic-audit.sh
    ├── Run validate.sh
    ├── Check: all planned files exist?
    ├── Check: NEVER DEGRADE (if update)
    │
    └── Validation report
    │
    ▼
P03-docs ⏸️ (NEW)
    │
    ├── LOGIC-TREE-{name}-{version}.md
    ├── SCAN-{name}-{version}.md
    ├── DIFF-{name}-{version}.md (if update)
    │
    └── Docs complete checkpoint
    │
    ▼
P04-deliver ⛔ BLOCKING
    │
    ├── Final checklist
    ├── Package as .skill (NOT .zip!)
    ├── Copy to /mnt/user-data/outputs/
    │
    └── Delivery confirmation
```

---

## Changes Summary

### KEEP (from v4.5.1)

| Item | Reason |
|------|--------|
| Protocol chain P01→P02→P03→P04 | Core architecture works |
| Cognitive Razors | Decision framework valid |
| Genes G01-G10 | Quality genes work |
| Quality Gates L1-L10 | Validation framework works |
| INoT Engine | Critical decision support |
| NEVER DEGRADE | Essential for updates |
| Anchor format | Navigation works |
| Session indicators 🟢🟡🔴 | Context awareness |

### ADD (new in v4.6.0)

| Item | Purpose |
|------|---------|
| G11: Memory Budget | Universal batching |
| Pre-build Calculator | Batch planning |
| Checkpoint format | Progress tracking |
| P03-validate phase | Dedicated validation |
| P03-docs phase | Dedicated documentation |
| Mandatory Planning Document | Audit trail |
| .skill extension enforcement | Correct packaging |

### MODIFY

| Item | Change |
|------|--------|
| P02-plan | Add: Planning Document MUST be saved to outputs |
| P03-build | Split into batches with checkpoints |
| P04-deliver | Add: explicit .skill check |
| genetic-audit.sh | Add: G11 check |
| validate.sh | Add: Planning Document existence check |

### REMOVE

| Item | Reason |
|------|--------|
| — | No removals (NEVER DEGRADE) |

---

## File Changes

### New Files

| File | Purpose | Lines |
|------|---------|-------|
| reference/memory-budget.md | G11 specification | ~100 |
| reference/checkpoint-format.md | Checkpoint templates | ~80 |
| protocols/P03a-build.md | Batched build | ~120 |
| protocols/P03b-validate.md | Validation phase | ~80 |
| protocols/P03c-docs.md | Documentation phase | ~60 |

### Modified Files

| File | Changes |
|------|---------|
| SKILL.md | Add G11, update flow diagram |
| protocols/P02-plan.md | Mandatory Planning Document save |
| protocols/P04-deliver.md | .skill extension enforcement |
| reference/genetic-audit.md | Add G11 |
| scripts/genetic-audit.sh | Add G11 check |
| scripts/validate.sh | Add Planning Document check |

### Total Impact

| Metric | v4.5.1 | v4.6.0 | Delta |
|--------|--------|--------|-------|
| Files | 29 | 34 | +5 |
| Lines | ~2200 | ~2600 | +400 |
| Features | 65 | 72 | +7 |
| Genes | 10+5 | 11+5 | +1 |

---

## Implementation Batches

### Pre-build Calculation

```
34 files ÷ 5 = 7 batches
~2600 lines ÷ 300 = 9 batches
→ Expect: 7-9 batches
→ Estimated time: 35-45 min
```

### Batch Plan

| Batch | Files | Category |
|-------|-------|----------|
| 1 | 3 | Core: SKILL.md, README, CHANGELOG |
| 2 | 3 | Protocols: P00, P01, P02 |
| 3 | 3 | Protocols: P03a, P03b, P03c, P04 |
| 4 | 5 | Reference: templates, quality-gates, anchor, genetic, inot |
| 5 | 5 | Reference: naming, packaging, planning, diff, memory-budget |
| 6 | 2 | Reference: checkpoint-format, evaluations |
| 7 | 5 | Scripts: all |
| 8 | 3 | Docs: LOGIC-TREE, SCAN, DIFF |
| 9 | 1 | Package: .skill |

---

## Validation Criteria

### Must Pass

- [ ] All 34 files created
- [ ] G11 implemented and documented
- [ ] Checkpoint format working
- [ ] Planning Document auto-saved
- [ ] .skill extension correct
- [ ] LOGIC-TREE produced
- [ ] SCAN produced
- [ ] DIFF produced
- [ ] genetic-audit.sh passes
- [ ] validate.sh passes
- [ ] NEVER DEGRADE: 72 >= 65 ✓

---

## Risks & Mitigations

| Risk | Probability | Mitigation |
|------|-------------|------------|
| Context loss mid-batch | Medium | Checkpoint format includes full state |
| User impatience with pauses | Low | Explain benefits upfront |
| Over-batching simple skills | Low | Calculator adapts to size |

---

## Approval

| Role | Status | Date |
|------|--------|------|
| User | ⏳ PENDING | — |
| skill-architect | ✅ READY | 2025-12-16 |

---

**NEXT:** User approval required before P03-build

**Options:**
1. Confirm plan → start build
2. Request changes → modify plan
3. Cancel → abort update

---

*PLAN-skill-architect-v4.6.0.md | Planning Document*
