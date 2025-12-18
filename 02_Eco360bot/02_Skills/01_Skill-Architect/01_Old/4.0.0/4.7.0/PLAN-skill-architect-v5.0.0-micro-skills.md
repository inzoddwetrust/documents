# PLAN: skill-architect v5.0.0 "Micro-Skills"

## Meta

| Field | Value |
|-------|-------|
| Date | 2025-12-18 |
| Mode | REFACTOR (architectural) |
| Baseline | v4.7.0 "Consolidated" |
| Target | v5.0.0 "Micro-Skills" |
| Breaking Change | YES — complete restructure |
| Estimated effort | 3-4 sessions |

---

## Problem Statement

### What happened

In v4.7.0 session, Claude (Opus) made 3 errors:
1. Skipped P03c-docs phase entirely
2. Used `tar` instead of `zip` for packaging
3. Required 3 iterations to deliver correct output

### Root cause

```
Current: Read SKILL.md (483 lines) + 7 protocols + 13 references
         → Work from MEMORY
         → Context drift
         → Forget steps
```

### Evidence

| Anthropic Best Practice | skill-architect v4.7.0 |
|------------------------|------------------------|
| SKILL.md < 500 lines | 483 lines (at limit) |
| One level deep references | 3+ levels deep |
| Progressive disclosure | Read everything upfront |
| Self-contained skills | Depends on protocol chain |

---

## Solution: Micro-Skills Architecture

### Core Principle

```
ONE SKILL = ONE STEP = ONE RESPONSIBILITY
```

### Target Structure

```
/mnt/skills/user/
├── skill-architect/              # Router only (~100 lines)
│   ├── SKILL.md
│   └── README-skill-architect.md
│
├── skill-arch-init/              # P01 equivalent
│   └── SKILL.md (~150 lines)
│
├── skill-arch-plan/              # P02 equivalent  
│   ├── SKILL.md (~200 lines)
│   └── templates/
│       └── planning-document.md
│
├── skill-arch-build/             # P03a equivalent
│   ├── SKILL.md (~180 lines)
│   └── templates/
│       ├── skill-template.md
│       └── readme-template.md
│
├── skill-arch-validate/          # P03b equivalent
│   ├── SKILL.md (~150 lines)
│   └── scripts/
│       └── validate.sh
│
├── skill-arch-docs/              # P03c equivalent
│   ├── SKILL.md (~150 lines)
│   └── templates/
│       ├── logic-tree.md
│       ├── scan.md
│       └── diff.md
│
├── skill-arch-deliver/           # P04 equivalent
│   ├── SKILL.md (~120 lines)
│   └── scripts/
│       └── package.sh
│
└── skill-arch-genes/             # Genetic audit (shared)
    ├── SKILL.md (~200 lines)
    └── scripts/
        └── genetic-audit.sh
```

### Flow

```
User: "create skill X"
         │
         ▼
┌─────────────────────┐
│  skill-architect    │  ← Router: identifies task, delegates
│  (router)           │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  skill-arch-init    │  ← Collect requirements, determine mode
└─────────┬───────────┘
          │ NEXT: skill-arch-plan
          ▼
┌─────────────────────┐
│  skill-arch-plan    │  ← Create Planning Document ⛔
└─────────┬───────────┘
          │ NEXT: skill-arch-build
          ▼
┌─────────────────────┐
│  skill-arch-build   │  ← Build in batches (G11)
└─────────┬───────────┘
          │ NEXT: skill-arch-validate
          ▼
┌─────────────────────┐
│  skill-arch-validate│  ← Validate created files ⛔
└─────────┬───────────┘
          │ NEXT: skill-arch-docs    ← EXPLICIT!
          ▼
┌─────────────────────┐
│  skill-arch-docs    │  ← Create LOGIC-TREE, SCAN, DIFF
└─────────┬───────────┘
          │ NEXT: skill-arch-deliver
          ▼
┌─────────────────────┐
│  skill-arch-deliver │  ← Package as .skill (ZIP!) ⛔
└─────────────────────┘
```

---

## Micro-Skill Specifications

### 1. skill-architect (Router)

```yaml
---
name: skill-architect
description: "v5.0.0 | Route skill creation/update tasks to specialized micro-skills. Triggers: create skill, update skill, refactor skill."
---
```

**Responsibilities:**
- Parse user intent (create/update/refactor/checkup)
- Delegate to appropriate micro-skill
- Track overall progress

**Content (~100 lines):**
- Purpose table
- Command → Micro-skill mapping
- Overall flow diagram
- Anchor format

**Does NOT contain:**
- Detailed instructions for any phase
- Templates
- Scripts

---

### 2. skill-arch-init

```yaml
---
name: skill-arch-init
description: "Initialize skill creation. Collect requirements, determine mode (CREATE/UPDATE/REFACTOR), load baseline. Use when starting new skill work."
---
```

**Responsibilities:**
- Collect: name, purpose, triggers, audience
- Determine mode from context
- For UPDATE: load baseline version
- Output: config for next phase

**Content (~150 lines):**
- Required questions checklist
- Mode detection logic
- Config output format
- NEXT: skill-arch-plan

---

### 3. skill-arch-plan

```yaml
---
name: skill-arch-plan
description: "Create Planning Document for skill. KEEP/REMOVE/ADD analysis, batch planning, chat verification. Use after skill-arch-init. ⛔ Blocking."
---
```

**Responsibilities:**
- Apply Design Razors (Occam's, Hume's, Hanlon's)
- Create Planning Document
- Pre-Build Calculator (batches)
- Chat Verification
- NEVER DEGRADE check (if UPDATE)
- Save to /outputs/

**Content (~200 lines):**
- Design Razors checklist
- Planning Document template (embedded)
- Pre-Build Calculator
- CRITICAL: Save before proceed
- NEXT: skill-arch-build

**⛔ Blocking:** Wait for user confirmation

---

### 4. skill-arch-build

```yaml
---
name: skill-arch-build
description: "Build skill files in batches. Memory Budget G11: max 5 files OR 300 lines per batch. Use after skill-arch-plan confirmed."
---
```

**Responsibilities:**
- PRE-BUILD: Re-read Planning Document
- Create files in batches
- Apply genes G01-G11
- Checkpoint after each batch

**Content (~180 lines):**
- Memory Budget limits
- Batch categories
- Gene checklist
- Checkpoint format
- NEXT: skill-arch-validate

**Contains:**
- templates/skill-template.md
- templates/readme-template.md

---

### 5. skill-arch-validate

```yaml
---
name: skill-arch-validate
description: "Validate built skill files. Re-read plan, check genes, NEVER DEGRADE. Use after skill-arch-build complete. ⛔ Blocking."
---
```

**Responsibilities:**
- Re-read Planning Document (context drift!)
- Validate created files
- Genetic audit (delegte to skill-arch-genes)
- NEVER DEGRADE check

**Content (~150 lines):**
- Validation checklist
- NEVER DEGRADE comparison
- Error handling
- NEXT: skill-arch-docs  ← EXPLICIT!

**⛔ Blocking:** Wait for user confirmation

---

### 6. skill-arch-docs

```yaml
---
name: skill-arch-docs
description: "Create documentation: LOGIC-TREE, SCAN, DIFF. MANDATORY phase after validation. Use after skill-arch-validate. Cannot skip."
---
```

**Responsibilities:**
- Create LOGIC-TREE (decision tree)
- Create SCAN (file inventory)
- Create DIFF (if UPDATE)
- Save to docs/v{version}/

**Content (~150 lines):**
- ⛔ CRITICAL: This phase is MANDATORY
- LOGIC-TREE template
- SCAN template
- DIFF template
- NEXT: skill-arch-deliver

**Contains:**
- templates/logic-tree.md
- templates/scan.md
- templates/diff.md

---

### 7. skill-arch-deliver

```yaml
---
name: skill-arch-deliver
description: "Package and deliver skill. ZIP format (not tar!), .skill extension. Use after skill-arch-docs complete. ⛔ Blocking."
---
```

**Responsibilities:**
- Pre-delivery checklist
- Package as ZIP with .skill extension
- Verify extension
- Copy to /outputs/
- Present to user

**Content (~120 lines):**
- ⛔ CRITICAL: zip -r, NOT tar
- ⛔ CRITICAL: .skill extension, NOT .zip
- Package contents checklist
- Verification script
- NEXT: Complete

**Contains:**
- scripts/package.sh

**⛔ Blocking:** Wait for user confirmation

---

### 8. skill-arch-genes

```yaml
---
name: skill-arch-genes
description: "Genetic audit for skills. Check G01-G15 compliance. Use for checkup command or during validation."
---
```

**Responsibilities:**
- Check genes G01-G15
- Report compliance status
- Suggest fixes

**Content (~200 lines):**
- Gene definitions (G01-G15)
- Audit checklist
- Script usage

**Contains:**
- scripts/genetic-audit.sh

---

## New Genes (G12-G15)

### G12: Micro-Skill Boundary

```
ONE skill = ONE step of workflow
If skill does multiple unrelated things → split
```

### G13: Self-Contained

```
Skill works WITHOUT reading other skills
All needed information is IN the skill
No "see protocol X for details"
```

### G14: Explicit Handoff

```
NEXT: skill-name (not "next phase")
Every skill ends with explicit handoff
User sees exactly which skill comes next
```

### G15: Router Pattern

```
Complex workflows (5+ steps) use Router skill
Router only dispatches, never executes
Each step is separate micro-skill
```

---

## Migration Plan

### Phase 1: Extract Critical Skills (fixes current problem)

| Task | Priority | Effort |
|------|----------|--------|
| Create skill-arch-docs | 🔴 HIGH | ~30 min |
| Create skill-arch-deliver | 🔴 HIGH | ~30 min |
| Update skill-architect to route to them | 🔴 HIGH | ~20 min |

**Deliverable:** Immediate fix for P03c/P04 problems

---

### Phase 2: Extract Remaining Skills

| Task | Priority | Effort |
|------|----------|--------|
| Create skill-arch-init | 🟡 MEDIUM | ~30 min |
| Create skill-arch-plan | 🟡 MEDIUM | ~45 min |
| Create skill-arch-build | 🟡 MEDIUM | ~45 min |
| Create skill-arch-validate | 🟡 MEDIUM | ~30 min |
| Create skill-arch-genes | 🟡 MEDIUM | ~30 min |

**Deliverable:** Full micro-skills architecture

---

### Phase 3: Router Transformation

| Task | Priority | Effort |
|------|----------|--------|
| Refactor skill-architect to pure router | 🟡 MEDIUM | ~30 min |
| Update README | 🟢 LOW | ~15 min |
| Create CHANGELOG v5.0.0 | 🟢 LOW | ~15 min |

**Deliverable:** skill-architect v5.0.0 "Micro-Skills"

---

### Phase 4: Ecosystem Update

| Task | Priority | Effort |
|------|----------|--------|
| Update test-architect to use new architecture | 🟢 LOW | ~1 hour |
| Update project-architect | 🟢 LOW | ~1 hour |
| Document pattern for future skills | 🟢 LOW | ~30 min |

**Deliverable:** Ecosystem aligned with micro-skills pattern

---

## Metrics Comparison

| Metric | v4.7.0 | v5.0.0 | Change |
|--------|--------|--------|--------|
| Main SKILL.md | 483 lines | ~100 lines | -80% |
| Files to read per step | 2-4 | 1 | -75% |
| Max context per step | ~1000 lines | ~200 lines | -80% |
| Total skills | 1 | 8 | +7 |
| Total lines | ~2700 | ~1250 | -54% |
| Self-contained steps | NO | YES | ✅ |
| Explicit handoffs | NO | YES | ✅ |

---

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| More skills to maintain | Each skill is simpler, easier to maintain |
| User must install 8 skills | Package as bundle, single install |
| Breaking change | Clear migration guide |
| Testing complexity | Each skill testable independently |

---

## NEVER DEGRADE Check

| Feature | v4.7.0 | v5.0.0 | Status |
|---------|--------|--------|--------|
| CREATE mode | ✅ | ✅ | Preserved |
| UPDATE mode | ✅ | ✅ | Preserved |
| REFACTOR mode | ✅ | ✅ | Preserved |
| Memory Budget G11 | ✅ | ✅ | Preserved |
| NEVER DEGRADE | ✅ | ✅ | Preserved |
| Genetic audit | ✅ | ✅ | Preserved |
| Planning Document | ✅ | ✅ | Preserved |
| LOGIC-TREE/SCAN/DIFF | ✅ | ✅ | Preserved |
| .skill packaging | ✅ | ✅ | Preserved |
| Cognitive razors | ✅ | ✅ | Preserved |

**All 73+ features preserved, architecture improved**

---

## Success Criteria

1. Claude never skips P03c-docs (skill-arch-docs forces it)
2. Claude always uses ZIP (skill-arch-deliver has explicit instruction)
3. Each step reads only ~150-200 lines (not 2700)
4. Explicit NEXT → skill-name in every skill
5. Can test each micro-skill independently

---

## Chat Verification

| Discussed Item | In Plan |
|----------------|---------|
| Micro-skills architecture | ✅ |
| Each step = separate skill | ✅ |
| Router pattern | ✅ |
| New genes G12-G15 | ✅ |
| Progressive disclosure | ✅ |
| < 500 lines per skill | ✅ |
| Self-contained skills | ✅ |
| Explicit handoffs | ✅ |
| NEVER DEGRADE | ✅ |
| Migration phases | ✅ |

---

## Appendix: Micro-Skill Template

```markdown
---
name: skill-arch-{phase}
description: "v5.0.0 | {one-line purpose}. Use after skill-arch-{previous}. {⛔ Blocking if applicable}."
---

# Skill Architect: {Phase Name}

| Field | Value |
|-------|-------|
| Previous | skill-arch-{previous} |
| Next | skill-arch-{next} |
| Blocking | YES/NO |

---

## ⛔ CRITICAL

1. {critical rule 1}
2. {critical rule 2}
3. {critical rule 3}

---

## Process

### Step 1: {name}
{instructions}

### Step 2: {name}
{instructions}

---

## Checklist

- [ ] {item 1}
- [ ] {item 2}
- [ ] {item 3}

---

## Anchor

```
🟢 skill-arch-{phase} · {status}
NEXT: skill-arch-{next}
```

---

*skill-arch-{phase} v5.0.0 | Part of skill-architect micro-skills*
```

---

*PLAN-skill-architect-v5.0.0-micro-skills.md | 2025-12-18*
