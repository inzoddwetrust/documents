# Planning Document: skill-architect v4.1.0 "Universal"

## Meta

| Field | Value |
|-------|-------|
| Date | 2025-12-13 |
| Mode | UPDATE |
| Baseline | v4.0.0 "Unified" |
| Retrospectives | 1 version + ecosystem test analysis |
| Target Score | 92 → 96+ |

---

## Current State Analysis

**Score:** 92/100 — лидер экосистемы  
**Main Gap:** P00-router минимальный, нет ecosystem awareness на уровне роутера

### Comparison: Router Quality

| Aspect | skill-architect | test-architect |
|--------|-----------------|----------------|
| Lines | 64 | 72 |
| Decision Table | ❌ basic signals | ✅ structured |
| Ecosystem Paths | ❌ | ✅ with fallbacks |
| Mode Detection | ❌ | ✅ flags system |
| Ecosystem Sequence | ❌ | ✅ |
| Recovery | ✅ | ✅ |

**Вывод:** Интегрируем Universal Router pattern из test-architect.

---

## KEEP (from v4.0.0)

| # | Item | Reason |
|---|------|--------|
| K01 | Protocol-driven workflow P01-P04 | Core architecture |
| K02 | Genetic Audit G01-G07 | Quality inheritance |
| K03 | Self-Checkup G11-G15 | Self-validation |
| K04 | NEVER DEGRADE validator | Feature protection |
| K05 | INoT Engine | Critical decisions |
| K06 | Quality Gates L1-L10 | Comprehensive validation |
| K07 | Blocking points (⛔) | User control |
| K08 | Anchor format with NEXT | Context persistence |
| K09 | Chat Verification | Requirement capture |
| K10 | PRE-BUILD Checkpoint | Quality assurance |
| K11 | Diff Report | Change tracking |
| K12 | Planning Document | Structured planning |
| K13 | Confirmation words table | Clear triggers |
| K14 | Recovery mechanism | Context restoration |
| K15 | Clean Skill Principles | Quality standards |
| K16 | Ecosystem awareness (basic) | Sibling knowledge |
| K17 | Scripts suite (7) | Automation |
| K18 | Reference docs (10) | Documentation |
| K19 | UPDATE requirements | Version control |

**Feature Count (Baseline):** 19

---

## REMOVE

| Item | Reason |
|------|--------|
| — | Nothing removed. NEVER DEGRADE! |

---

## ADD

| # | Item | Source | Priority |
|---|------|--------|----------|
| A01 | Universal Router pattern | test-architect | P1 |
| A02 | Ecosystem Paths table | test-architect | P1 |
| A03 | Mode Detection (flags) | test-architect | P1 |
| A04 | Ecosystem Sequence | test-architect | P2 |
| A05 | Cross-skill routing | new | P2 |
| A06 | Fallback paths | test-architect | P2 |
| A07 | Post-build auto-test suggestion | ecosystem integration | P3 |

---

## Detailed ADD Specifications

### A01: Universal Router Pattern

**Current P00-router (v4.0.0):**
```markdown
## State Detection

| Signal | Protocol |
|--------|----------|
| `create skill` | → P01 |
| `update skill` | → P01 |
...
```

**New P00-router (v4.1.0):**
```markdown
# P00-router: Universal Router

Routes requests and manages ecosystem awareness.

---

## Decision Table

| Input | Route | Mode |
|-------|-------|------|
| create skill [name] | → P01-init | create |
| create skill [name] --quick | → P01-init | quick-create |
| update skill [path] | → P01-init | update |
| update skill [path] --full | → P01-init | full-update |
| refactor skill [path] | → P01-init | refactor |
| checkup | → Genetic Audit | self-check |
| checkup [path] | → Genetic Audit | external-check |
| validate [path] | → Direct validation | validate |
| package [path] | → Direct packaging | package |

---

## Mode Detection

| Flag | Mode | Behavior |
|------|------|----------|
| (none) | standard | Full workflow with confirmations |
| --quick | quick | Minimal confirmations, fast delivery |
| --full | full | Extended validation, VT included |
| --degrade [old] | compare | NEVER DEGRADE check against old version |

---

## Ecosystem Paths

| Skill | Primary Path | Fallback |
|-------|--------------|----------|
| skill-architect | /mnt/skills/user/skill-architect | self |
| test-architect | /mnt/skills/user/test-architect | /mnt/user-data/uploads/ |
| project-architect | /mnt/skills/user/project-architect | /mnt/user-data/uploads/ |
| role-architect | /mnt/skills/user/role-architect | /mnt/user-data/uploads/ |

---

## Ecosystem Sequence

For ecosystem-wide operations:
```
skill-architect (self-checkup)
    ↓
target skill (create/update)
    ↓
test-architect (optional validation)
    ↓
Delivery
```

---

## Cross-Skill Routing

| Situation | Route To |
|-----------|----------|
| After P04-deliver | Suggest: test-architect validation |
| Project with data/ needed | Suggest: project-architect |
| Role creation needed | Suggest: role-architect |

---

## Protocol Chain

```
START → P01-init → P02-plan ⛔ → P03-build → P04-deliver ⛔ → [test?] → END
```

---

## Recovery

If context lost:
1. Find last anchor in conversation
2. Read protocol and status from anchor
3. Read NEXT instruction
4. Resume from that point

---

*P00-router.md | skill-architect v4.1.0*
```

### A02: Ecosystem Paths Table

Добавить в SKILL.md секцию:

```markdown
## Ecosystem Paths

| Skill | Path | Role |
|-------|------|------|
| skill-architect | /mnt/skills/user/skill-architect | Create/update skills |
| test-architect | /mnt/skills/user/test-architect | Validate skills |
| project-architect | /mnt/skills/user/project-architect | Project knowledge bases |
| role-architect | /mnt/skills/user/role-architect | Virtual professional roles |

Fallback: /mnt/user-data/uploads/ (for uploaded skills)
```

### A03: Mode Detection

Добавить в Commands таблицу:

```markdown
## Commands

| Command | Protocol | Mode |
|---------|----------|------|
| `create skill` | P01→P04 | standard |
| `create skill --quick` | P01→P04 | quick (fewer confirmations) |
| `update skill` | P01→P04 | standard |
| `update skill --full` | P01→P04 | full (extended validation) |
| `refactor skill` | P01→P04 | refactor |
| `checkup` | — | self-check |
| `validate [path]` | — | direct validation |
```

### A04: Ecosystem Sequence

```markdown
## Ecosystem Sequence

Recommended workflow:
```
1. skill-architect checkup (verify self)
       ↓
2. create/update skill
       ↓
3. test-architect validate (optional)
       ↓
4. Deploy
```
```

### A05: Cross-Skill Routing

Добавить в P04-deliver:

```markdown
## Post-Delivery Options

After successful delivery, suggest:

| Option | Command | When |
|--------|---------|------|
| Validate | `test [skill-path]` | Always recommended |
| Create project | `create project: [name]` | If skill needs data/ |
| Create role | `create role: [domain]/[level]` | If skill is role-based |

Example:
```
Skill delivered! ✅

Next steps:
- Validate: `test /mnt/skills/user/new-skill`
- Or start using the skill
```
```

### A06: Fallback Paths

В ecosystem paths добавить fallback логику:

```markdown
## Path Resolution

1. Check primary path
2. If not found → check fallback
3. If not found → check /home/claude/
4. If not found → error with suggestion

```python
def resolve_skill_path(name):
    paths = [
        f"/mnt/skills/user/{name}",
        f"/mnt/user-data/uploads/{name}",
        f"/home/claude/{name}"
    ]
    for p in paths:
        if exists(p): return p
    return None
```
```

### A07: Post-Build Auto-Test Suggestion

В P04-deliver добавить:

```markdown
## Auto-Test Suggestion

After successful build:
```
✅ Build complete: {skill-name} v{version}

Recommended: Run validation
→ test {skill-path}

Proceed to delivery? [yes/no/test first]
```
```

---

## Architecture (Updated)

```
skill-architect/
├── SKILL.md                      # +A02, A03 additions (~260 lines)
├── README-skill-architect.md     # Updated
├── CHANGELOG-skill-architect.md  # v4.1.0 entry
├── MANIFEST.md                   # Updated
├── docs/
│   ├── v4.0.0/                   # Existing
│   └── v4.1.0/                   # NEW
│       ├── LOGIC-TREE.md
│       ├── DIFF-REPORT.md
│       └── FEATURE-SCAN.md
├── protocols/
│   ├── P00-router.md             # MAJOR UPDATE (A01, A04, A05, A06)
│   ├── P01-init.md               # Minor: mode detection
│   ├── P02-plan.md               # Unchanged
│   ├── P03-build.md              # Unchanged
│   └── P04-deliver.md            # +A07 auto-test suggestion
├── reference/                    # +1 file
│   ├── (existing 10 files)
│   └── ecosystem-paths.md        # NEW (A02, A06)
└── scripts/                      # Unchanged (7 files)
```

---

## Chat Verification

### Scanned Messages
4 messages scanned

### Discussed Items

1. Тест экосистемы выполнен
2. План обновления test-architect готов
3. Интеграция Universal Router в skill-architect
4. Ecosystem awareness улучшение

### Verification Table

| # | Item | In Plan? | Section |
|---|------|----------|---------|
| 1 | Ecosystem test | ✅ | Completed earlier |
| 2 | test-architect plan | ✅ | Completed earlier |
| 3 | Universal Router | ✅ | A01 |
| 4 | Ecosystem awareness | ✅ | A02, A04, A05 |

**Result:** 4/4 verified. Missing: none

---

## NEVER DEGRADE Check

| Metric | Baseline (v4.0.0) | Planned (v4.1.0) | Status |
|--------|-------------------|------------------|--------|
| Features | 19 | 26 (+7) | ✅ PASS |
| SKILL.md Lines | 247 | ~280 | ✅ |
| Files | 31 | 33 (+2) | ✅ |
| Protocols | 5 | 5 | ✅ |
| Reference | 10 | 11 (+1) | ✅ |
| Scripts | 7 | 7 | ✅ |

**Status:** ✅ PASS — No degradation, +7 features

---

## Expected Score Impact

| Category | v4.0.0 | v4.1.0 | Delta |
|----------|--------|--------|-------|
| Structure (L1-L2) | 20/20 | 20/20 | — |
| Logic (L3-L4) | 18/20 | 20/20 | +2 |
| Integration (L5-L6) | 18/20 | 20/20 | +2 |
| Genetic | 20/20 | 20/20 | — |
| SSOT | 16/20 | 18/20 | +2 |
| **Total** | **92/100** | **98/100** | **+6** |

---

## Cross-Pollination Summary

| Feature | From | To | Status |
|---------|------|-----|--------|
| Universal Router | test-architect | skill-architect | ✅ In plan |
| Ecosystem Paths | test-architect | skill-architect | ✅ In plan |
| Mode Detection | test-architect | skill-architect | ✅ In plan |
| Recovery | skill-architect | test-architect | ✅ In test-architect plan |
| Confirmation words | skill-architect | test-architect | ✅ In test-architect plan |

**Ecosystem Synergy:** Лучшие практики распространяются между скиллами.

---

## Version Naming

| Version | Codename | Focus |
|---------|----------|-------|
| v4.0.0 | "Unified" | Protocol consolidation |
| v4.1.0 | "Universal" | Universal Router integration |

---

## Confirmation Checklist

- [x] KEEP items reviewed (19 items)
- [x] REMOVE items have reasons (0 removed)
- [x] ADD items captured (7 items)
- [x] Chat Verification passed (4/4)
- [x] NEVER DEGRADE passed (+7 features)
- [x] Architecture defined
- [x] Score projection calculated
- [x] Cross-pollination documented

---

## Dependency Note

**Build Order:**
1. test-architect v1.1.0 (добавляет фичи из skill-architect)
2. skill-architect v4.1.0 (интегрирует Universal Router из test-architect)

Или параллельно, так как изменения независимы.

---

## Ready for Confirmation

План обновления skill-architect v4.0.0 → v4.1.0 готов.

**Ключевые изменения:**
- Universal Router pattern интегрирован
- +7 новых фич (A01-A07)
- 0 удалений (NEVER DEGRADE)
- Ожидаемый score: 98/100 (было 92)
- Codename: "Universal"

**Подтвердить план?**

---

*Planning Document | skill-architect v4.1.0 "Universal"*  
*Prepared by: test-architect v1.0.0*
