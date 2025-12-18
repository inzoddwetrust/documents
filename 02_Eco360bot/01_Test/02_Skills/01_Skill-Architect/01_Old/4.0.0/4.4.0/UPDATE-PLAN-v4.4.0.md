# Update Plan: skill-architect v4.4.0 "Autonomous Razors"

> v4.1.0 (база) + v4.3.0 (razors) = v4.4.0 (автономность + когнитивные инструменты)

---

## Концепция

**Проблема v4.2.0-v4.3.0:** Потеря автономности — скилл не может валидировать без test-architect.

**Решение v4.4.0:** Делегирует когда возможно, работает автономно когда нужно.

```
┌─────────────────────────────────────────────────────────┐
│                    v4.4.0 Strategy                      │
├─────────────────────────────────────────────────────────┤
│  checkup/validate                                       │
│       │                                                 │
│       ▼                                                 │
│  ┌─────────────────┐                                    │
│  │ test-architect  │──exists?──▶ YES → delegate        │
│  │   available?    │                                    │
│  └─────────────────┘                                    │
│       │                                                 │
│       ▼ NO                                              │
│  ┌─────────────────┐                                    │
│  │ Own validation  │──▶ validate.sh + genetic-audit.sh │
│  └─────────────────┘                                    │
└─────────────────────────────────────────────────────────┘
```

---

## Source Mapping

### Из v4.1.0 (полностью сохранить)

| Компонент | Файл | Статус |
|-----------|------|--------|
| Universal Router | protocols/P00-router.md | ✅ Keep |
| Init Protocol | protocols/P01-init.md | ✅ Keep + extend |
| Plan Protocol | protocols/P02-plan.md | ✅ Keep + extend |
| Build Protocol | protocols/P03-build.md | ✅ Keep + extend |
| Deliver Protocol | protocols/P04-deliver.md | ✅ Keep + extend |
| **validate.sh** | scripts/validate.sh | ✅ Keep (!) |
| **genetic-audit.sh** | scripts/genetic-audit.sh | ✅ Keep (!) |
| audit.sh | scripts/audit.sh | ✅ Keep |
| feature-registry.sh | scripts/feature-registry.sh | ✅ Keep |
| generate-manifest.sh | scripts/generate-manifest.sh | ✅ Keep |
| package.sh | scripts/package.sh | ✅ Keep |
| update-version.sh | scripts/update-version.sh | ✅ Keep |
| **quality-gates.md** | reference/quality-gates.md | ✅ Keep (!) |
| **genetic-audit.md** | reference/genetic-audit.md | ✅ Keep (!) |
| anchor-format.md | reference/anchor-format.md | ✅ Keep + extend |
| diff-format.md | reference/diff-format.md | ✅ Keep |
| ecosystem-paths.md | reference/ecosystem-paths.md | ✅ Keep |
| evaluations.md | reference/evaluations.md | ✅ Keep |
| inot-engine.md | reference/inot-engine.md | ✅ Keep |
| naming.md | reference/naming.md | ✅ Keep |
| packaging.md | reference/packaging.md | ✅ Keep |
| planning-document.md | reference/planning-document.md | ✅ Keep + extend |
| templates.md | reference/templates.md | ✅ Keep |

**Итого из v4.1.0:** 7 скриптов, 11 reference файлов, 5 протоколов

### Из v4.3.0 (интегрировать)

| Компонент | Куда интегрировать | Статус |
|-----------|-------------------|--------|
| Cognitive Razors (6 шт) | NEW: reference/cognitive-razors.md | ✅ Add |
| Grice's Razor | P01-init.md | ✅ Integrate |
| Hitchens' Razor | P01-init.md, P02-plan.md | ✅ Integrate |
| Occam's Razor | P02-plan.md, P03-build.md | ✅ Integrate |
| Hume's Razor | P02-plan.md | ✅ Integrate |
| Hanlon's Razor | P02-plan.md, P04-deliver.md | ✅ Integrate |
| Einstein's Razor | P03-build.md | ✅ Integrate |
| G08-G10 Genes | genetic-audit.md, SKILL.md | ✅ Add |
| Interactive Options | anchor-format.md | ✅ Integrate |
| Language Policy | SKILL.md | ✅ Add |
| Intent Interpretation | P01-init.md | ✅ Integrate |
| Design Razors section | P02-plan.md | ✅ Integrate |
| Build Razors section | P03-build.md | ✅ Integrate |
| Feedback Razors section | P04-deliver.md | ✅ Integrate |

**Итого из v4.3.0:** 1 новый reference файл, расширения в 4 протоколах

---

## Файловая структура v4.4.0

```
skill-architect-v4.4.0/
├── SKILL.md                          # Main (extended)
├── README-skill-architect.md         # User guide
├── CHANGELOG-skill-architect.md      # History
├── MANIFEST.md                       # File registry
│
├── protocols/
│   ├── P00-router.md                 # Universal Router + fallback
│   ├── P01-init.md                   # + Intent Interpretation
│   ├── P02-plan.md                   # + Design Razors
│   ├── P03-build.md                  # + Build Razors
│   └── P04-deliver.md                # + Feedback Razors + Options
│
├── reference/
│   ├── anchor-format.md              # + Interactive Options
│   ├── cognitive-razors.md           # NEW from v4.3.0
│   ├── diff-format.md
│   ├── ecosystem-paths.md
│   ├── evaluations.md
│   ├── genetic-audit.md              # RESTORED + G08-G10
│   ├── inot-engine.md
│   ├── naming.md
│   ├── packaging.md
│   ├── planning-document.md          # + Razors section
│   ├── quality-gates.md              # RESTORED
│   └── templates.md
│
├── scripts/
│   ├── audit.sh
│   ├── feature-registry.sh
│   ├── generate-manifest.sh
│   ├── genetic-audit.sh              # RESTORED
│   ├── package.sh
│   ├── update-version.sh
│   └── validate.sh                   # RESTORED
│
└── docs/
    └── v4.4.0/
        ├── DIFF-skill-architect-v4.4.0.md
        ├── LOGIC-TREE-skill-architect-v4.4.0.md
        └── SCAN-skill-architect-v4.4.0.md
```

**Итого:** 27 файлов (vs 27 в v4.3.0, но с восстановленными скриптами)

---

## Изменения в SKILL.md

### Header

```markdown
---
name: skill-architect
description: "v4.4.0 | Protocol-driven skill creation with cognitive razors. Triggers: create skill, update, refactor, checkup, validate."
---

# Skill Architect v4.4.0 "Autonomous Razors"
```

### Новая секция: Validation Strategy

```markdown
## Validation Strategy

skill-architect supports two validation modes:

### Delegated Mode (preferred)
When test-architect is available:
```
checkup → test-architect test [path] --full
validate → test-architect test [path]
```

### Autonomous Mode (fallback)
When test-architect is NOT available:
```
checkup → bash scripts/genetic-audit.sh [path]
validate → bash scripts/validate.sh [path]
```

### Auto-Detection
P00-router checks test-architect availability:
1. Check /mnt/skills/user/test-architect
2. Check /mnt/user-data/uploads/test-architect*
3. If found → delegate
4. If not found → autonomous validation
```

### Новая секция: Language Policy (из v4.3.0)

```markdown
## Language Policy

### Production Rule
All artifacts in English:
- SKILL.md, README.md, CHANGELOG.md
- Planning Documents, Diff Reports
- Protocol files, reference files

### Chat Rule
Dialogue adapts to user's language:
- User writes Russian → respond Russian
- User writes English → respond English
```

### Расширенная секция: Required Genes

```markdown
## Required Genes

### Core Genes (G01-G07)
| Gene | Requirement |
|------|-------------|
| G01 Frontmatter | `name:` + `description:` with version |
| G02 Purpose | serves/goal/method/success OR clear purpose |
| G03 Flow | Visual flow with → arrows |
| G04 Commands | Table with triggers |
| G05 Anchor | NEXT instruction in every response |
| G06 Session | 🟢🟡🔴 indicator |
| G07 Blocking | ⛔ where confirmation required |

### Cognitive Genes (G08-G10) — NEW
| Gene | Requirement |
|------|-------------|
| G08 Occam's Design | Simplest structure covering requirements |
| G09 Hume's Scale | Complexity matches task size |
| G10 Einstein's Balance | Complete but not bloated |

Validation: 
- Delegated: `test-architect test [path] --genetic`
- Autonomous: `bash scripts/genetic-audit.sh [path]`
```

---

## Изменения в P00-router.md

### Новая секция: Validation Routing

```markdown
## Validation Routing

### Auto-Detection Algorithm

```bash
# Check test-architect availability
if [ -d "/mnt/skills/user/test-architect" ]; then
    MODE="delegated"
elif ls /mnt/user-data/uploads/test-architect* 2>/dev/null; then
    MODE="delegated"
elif [ -d "/home/claude/test-architect" ]; then
    MODE="delegated"
else
    MODE="autonomous"
fi
```

### Routing Table

| Command | Delegated Mode | Autonomous Mode |
|---------|----------------|-----------------|
| `checkup` | test-architect test --full | genetic-audit.sh + validate.sh |
| `checkup [path]` | test-architect test [path] | genetic-audit.sh [path] |
| `validate [path]` | test-architect test [path] --quick | validate.sh [path] |

### Response Format

When autonomous:
```
⚠️ test-architect not found. Using autonomous validation.
Running: bash scripts/validate.sh [path]
```
```

---

## Изменения в протоколах

### P01-init.md — добавить Intent Interpretation

```markdown
## Intent Interpretation

Before proceeding, apply cognitive razors:

### Grice's Razor Check
- [ ] What did user MEAN vs what did they SAY?
- [ ] Cultural/language context?
- [ ] Need clarification?

### Hitchens' Razor Check
- [ ] What's explicitly stated?
- [ ] What am I inferring?
- [ ] Questions to ask?

**Rule:** If ANY ambiguity → ask before planning.
```

### P02-plan.md — добавить Design Razors

```markdown
## Design Razors

Before creating Planning Document, apply:

### Occam's Razor Check
- [ ] Simplest architecture covering requirements?
- [ ] Unnecessary abstractions?
- [ ] Minimum viable structure?

### Hume's Razor Check
- [ ] Solution complexity = problem complexity?
- [ ] Over-engineering for future?
- [ ] Proportional design?

### Hanlon's Razor Mindset
- Change requests = iteration, not criticism
- Stay open, not defensive

**Design principle:** Minimum sufficient architecture.
```

### P03-build.md — добавить Build Razors

```markdown
## Build Razors

During implementation:

### Occam's Razor (continuous)
- Remove code/sections until breaks
- Every abstraction must justify itself

### Einstein's Razor
- Too simple? Missing functionality?
- Too complex? Unnecessary features?
- Balance = all requirements met, nothing extra
```

### P04-deliver.md — добавить Feedback Razors + Options

```markdown
## Feedback Razors

When receiving user feedback:

### Hanlon's Razor Reminder
- Questions = seeking clarity
- Changes = natural iteration
- Criticism = improvement opportunity

Response tone: collaborative, not defensive.

---

## Interactive Options

At ⛔ blocking points, present:

```
Options:
1 → [action] (→ [next])
2 → [action]
3 → [action]
```

### Standard Option Sets

| Point | Options |
|-------|---------|
| After P02-plan | 1-Confirm, 2-Edit, 3-Cancel |
| After P04-deliver | 1-Deliver, 2-Test first, 3-Edit |
| Validation fail | 1-Fix, 2-Skip, 3-Cancel |
```

---

## Изменения в genetic-audit.md

### Добавить G08-G10

```markdown
## Cognitive Genes (G08-G10)

| Gene | Name | Validation |
|------|------|------------|
| G08 | Occam's Design | No unused sections, minimal abstractions |
| G09 | Hume's Scale | Complexity matches task size |
| G10 | Einstein's Balance | Complete but not bloated |

### Checklist for G08-G10

```markdown
### G08 Occam's Design
- [ ] No empty sections
- [ ] No unused protocols
- [ ] Each file has clear purpose
- [ ] Could be simpler? → simplify

### G09 Hume's Scale
- [ ] Simple task → simple skill (1 file ok)
- [ ] Medium task → medium skill (SKILL + few refs)
- [ ] Complex task → complex skill (full structure)

### G10 Einstein's Balance
- [ ] All stated requirements covered
- [ ] No "just in case" features
- [ ] Nothing missing, nothing extra
```
```

---

## Новый файл: reference/cognitive-razors.md

Полностью скопировать из v4.3.0 (352 строки) — отличный reference документ.

---

## Метрики

| Metric | v4.1.0 | v4.3.0 | v4.4.0 | Delta vs v4.3.0 |
|--------|--------|--------|--------|-----------------|
| Files | 30 | 27 | 29 | +2 |
| Scripts | 7 | 5 | 7 | +2 |
| Reference | 11 | 10 | 12 | +2 |
| Genes | 7+5 | 10 | 10+5 | +5 self-check |
| SKILL.md lines | ~290 | ~340 | ~380 | +40 |
| Autonomy | ✅ Full | ❌ Partial | ✅ Full | Restored |

---

## Verification Checklist

После сборки v4.4.0:

### Автономность
- [ ] `bash scripts/validate.sh` работает без test-architect
- [ ] `bash scripts/genetic-audit.sh` работает без test-architect
- [ ] checkup fallback срабатывает когда test-architect недоступен

### Razors Integration
- [ ] P01-init содержит Intent Interpretation
- [ ] P02-plan содержит Design Razors
- [ ] P03-build содержит Build Razors
- [ ] P04-deliver содержит Feedback Razors + Options

### Genes
- [ ] G01-G07 специфицированы в genetic-audit.md
- [ ] G08-G10 добавлены в genetic-audit.md
- [ ] G11-G15 сохранены для self-check

### NEVER DEGRADE
- [ ] Все 7 скриптов присутствуют
- [ ] Все 11+ reference файлов присутствуют
- [ ] Все фичи v4.1.0 сохранены
- [ ] Razors из v4.3.0 интегрированы

---

## Execution Plan

1. **Копировать v4.1.0 как базу** в /home/claude/skill-architect-v4.4.0
2. **Добавить cognitive-razors.md** из v4.3.0
3. **Расширить P01-init.md** — Intent Interpretation
4. **Расширить P02-plan.md** — Design Razors
5. **Расширить P03-build.md** — Build Razors
6. **Расширить P04-deliver.md** — Feedback Razors + Options
7. **Расширить anchor-format.md** — Interactive Options
8. **Расширить genetic-audit.md** — G08-G10
9. **Обновить P00-router.md** — Validation Routing с fallback
10. **Обновить SKILL.md** — Validation Strategy, Language Policy
11. **Обновить версию** везде → v4.4.0 "Autonomous Razors"
12. **Валидация** — запустить собственные скрипты
13. **Package** — создать .skill архив

---

*Plan created: 2025-12-16*
*Target: skill-architect v4.4.0 "Autonomous Razors"*
