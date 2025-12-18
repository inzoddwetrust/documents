# Skill Architect: План v4.1.0 → v5.0.0

**Дата:** 2025-12-01  
**Тип:** MAJOR — добавление Project Mode + BACKLOG items  
**Суть:** Merge Project Architect + B-014 Naming Convention + B-005 Development Guide

---

## Источники

| Источник | Что берём |
|----------|-----------|
| Project Architect v2.1.0 | Project Mode (CREATE, IMPORT, UPDATE, GENERATE) |
| BACKLOG B-014 (HIGH) | Unified Naming Convention + Checker |
| BACKLOG B-005 (MEDIUM) | development-guide.md |
| LOGIC-TREE v1.1.0 | Обновить для Project Mode |

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Русский |
| Frontmatter | name + description + version |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

**Проблема:** Два отдельных скилла (Skill Architect и Project Architect) делают похожую работу с 90% пересечением:
- Одинаковый workflow (Plan → Confirm → Build → Validate → Deliver)
- Одинаковая упаковка (.skill)
- Одинаковые требования (SKILL.md English, README, MANIFEST)
- Одинаковая валидация

**Различие только 10%:**
- Tool skills: `reference/` с шаблонами
- Project skills: `data/` с YAML модулями

**Решение:** Объединить в один скилл с двумя режимами.

---

## 2. Архитектура после мержа

```
Skill Architect v5.0.0
├── Core (shared)
│   ├── Workflow: Plan → Confirm → Build → Validate → Deliver
│   ├── Packaging: .skill format
│   ├── Validation: scripts/
│   └── Delivery: 3-step protocol
│
├── Tool Mode (default)
│   ├── Output: reference/ folder
│   ├── Templates: Analysis, Investigation, Content, Data, Code
│   └── Engines: INoT, Validation, Security
│
└── Project Mode (NEW)
    ├── Output: data/ folder (YAML modules)
    ├── Modules: core, team, product, market, finances, tech, roadmap, risks, clients, decisions
    ├── Import: reverse engineer from docs
    └── Generate: documents from data (filters)
```

---

## 3. План изменений

### SKILL.md Изменения

| Секция | Изменение |
|--------|-----------|
| Description | Добавить Project Mode триггеры |
| Quick Start | Добавить `create project: [name]` |
| Modes (NEW) | Tool Mode vs Project Mode |
| Resources | Добавить project-*.md файлы |

**Новые триггеры:**
- `create project: [name]` → Project Mode CREATE
- `import project` + attachment → Project Mode IMPORT  
- `создай скилл проекта` → Project Mode

### Новые reference файлы

| Файл | Содержимое | Строк | Источник |
|------|------------|-------|----------|
| `reference/project-mode.md` | Основная инструкция Project Mode | ~150 | Project Architect |
| `reference/project-modules.md` | YAML схемы 10 модулей | ~300 | Project Architect |
| `reference/project-import.md` | Import flow | ~200 | Project Architect |
| `reference/project-filters.md` | Document generation filters | ~150 | Project Architect |
| `reference/naming-convention.md` | Unified naming policy | ~80 | B-014 BACKLOG |
| `scripts/validate-naming.sh` | Naming checker | ~50 | B-014 BACKLOG |

### Новые docs файлы

| Файл | Содержимое | Строк | Источник |
|------|------------|-------|----------|
| `docs/development-guide.md` | How to develop skill-architect | ~100 | B-005 BACKLOG |
| `docs/LOGIC-TREE.md` | Updated with Project Mode | ~250 | Update |
| `docs/decisions/v5.0.0-decisions.md` | Version decisions | ~80 | Standard |

### Изменяемые файлы

| Файл | Изменение |
|------|-----------|
| `reference/templates.md` | Добавить Project Skill template |
| `reference/workflow.md` | Добавить Project workflow variant |

### Удаляем

| Что | Причина |
|-----|---------|
| Project Architect skill | Полностью мержится в Skill Architect |

---

## 4. Детали новых файлов

### reference/naming-convention.md (~80 lines) — B-014

```markdown
# Naming Convention

Единая политика именования для всех артефактов.

## Runtime Files (без версий)
- SKILL.md
- README.md  
- MANIFEST.md

## Versioned Docs
- v{X.Y.Z}-PLAN.md
- v{X.Y.Z}-DIFF.md

## Packages
- {skill-name}-v{X.Y.Z}.skill
- {skill-name}-v{X.Y.Z}-docs.zip

## Docs Folder
- {skill-name}-docs/ (единая, без версии в имени)

## Script: validate-naming.sh
Проверяет соответствие всех файлов конвенции.
```

### reference/project-mode.md (~150 lines)

```markdown
# Project Mode

Create SSOT knowledge bases for any project.

## When to Use
- New project → create knowledge base
- Import → reverse engineer docs
- Generate → create documents from data

## Core Formula
DOCUMENT = [MODULES] × FORMAT × AUDIENCE × PURPOSE × TONE

## Modes
- CREATE: Interactive data collection
- IMPORT: Reverse engineer from docs
- UPDATE: Modify data, track changes
- GENERATE: Create documents

## Data Structure
data/
├── core.yaml, team.yaml, product.yaml...

## Document Coverage Matrix
[table]

## Stage Requirements
[table]

## Output Example
[example]
```

### reference/project-modules.md (~300 lines)

Полные YAML схемы всех 10 модулей:
- core.yaml — name, mission, stage, status
- team.yaml — founders, hires, advisors
- product.yaml — features, metrics, pricing
- market.yaml — TAM/SAM/SOM, competitors
- finances.yaml — revenue, funding, unit economics
- tech.yaml — stack, architecture
- roadmap.yaml — vision, OKRs, milestones
- risks.yaml — risk matrix, assumptions
- clients.yaml — accounts, testimonials
- decisions.yaml — ADR records

### reference/project-import.md (~200 lines)

- Supported input types (pitch deck, one-pager, website)
- 5-phase process (Analysis → Extract → Populate → Verify → Gap Analysis)
- Mapping tables (slide → module, page → module)
- Quality checklist

### reference/project-filters.md (~150 lines)

- FORMAT: slides, one-page, email, long-form, post
- AUDIENCE: investors, b2c, b2b, press, partners, team, board
- PURPOSE: educate, inspire, sell, update, recruit
- TONE: professional, inspirational, educational, conversational
- Common combinations table
- Application process

### docs/development-guide.md (~100 lines) — B-005

```markdown
# Development Guide

How to evolve skill-architect.

## Principles
1. Evaluation-driven development
2. BACKLOG as source of truth
3. Claude A/B testing pattern

## Versioning
- MAJOR: Breaking changes, new modes
- MINOR: New features, reference files
- PATCH: Bug fixes, typos

## Process
1. Check BACKLOG for priorities
2. Create Planning Document
3. Implement with tests (evaluations.md)
4. Update LOGIC-TREE if flow changes
5. Document decisions
6. Deliver with 3-Step Protocol

## Claude A/B Pattern
- Claude A: Creates/improves skill
- Claude B: Tests on real tasks
- Iterate based on observations
```

---

## 5. SKILL.md Preview (v5.0.0)

```markdown
---
name: skill-architect
description: "v5.0.0 | Creates Claude Skills and Project Knowledge Bases. 
  Modes: Tool (default), Project. Plan → Build → Validate → Deliver.
  Triggers: create skill, create project, import project, refactor."
version: 5.0.0
---

# Skill Architect v5.0.0

## Quick Start

**Tool Mode (default):**
- `create skill: [purpose]`
- `update: [changes]` + attachment
- `refactor` + attachment

**Project Mode:**
- `create project: [name]`
- `import project` + attachment
- `update [module]` (inside project skill)
- `generate [document]` (inside project skill)

## Modes

| Mode | Creates | Data Folder | Use Case |
|------|---------|-------------|----------|
| **Tool** | Claude instruments | reference/ | Skills, generators, analyzers |
| **Project** | Knowledge bases | data/ | Business projects, startups |

Auto-detect: "project" keyword → Project Mode, otherwise Tool Mode.

[rest of SKILL.md - workflow, validation, delivery...]
```

---

## 6. Миграция

### Что происходит с Project Architect

1. **v2.1.0 → deprecated** — помечаем как устаревший
2. **Redirect** — в README указываем: "Use Skill Architect v5.0.0 Project Mode"
3. **Archive** — сохраняем для истории, не удаляем сразу

### Пользователям

- Существующие project skills работают без изменений
- Новые создаются через `create project:` в Skill Architect
- Import работает так же

---

## 7. Файловая структура после мержа

```
skill-architect/
├── SKILL.md                    # Updated (English, <300 lines)
├── README.md                   # Updated (Russian)
├── MANIFEST.md                 # Updated (more files)
├── reference/
│   ├── planning-document.md    # Unchanged
│   ├── packaging.md            # Unchanged
│   ├── templates.md            # +Project template
│   ├── engines.md              # Unchanged
│   ├── quality-checklist.md    # Unchanged
│   ├── workflow.md             # +Project workflow
│   ├── evaluations.md          # Unchanged
│   ├── project-mode.md         # NEW
│   ├── project-modules.md      # NEW
│   ├── project-import.md       # NEW
│   └── project-filters.md      # NEW
└── scripts/
    ├── validate-skill.sh       # Unchanged
    ├── audit-skill.sh          # Unchanged
    └── generate-manifest.sh    # Unchanged
```

---

## 8. Метрики

| Metric | Before (v4.1.0) | After (v5.0.0) |
|--------|-----------------|----------------|
| SKILL.md lines | 257 | ~280 |
| Reference files | 7 | 13 (+6) |
| Scripts | 3 | 4 (+1) |
| Total lines | ~1,500 | ~3,000 |
| Modes | 1 (Tool) | 2 (Tool + Project) |
| Capabilities | Skills only | Skills + Projects |

---

## 9. BACKLOG Updates

### Closing (→ Done)
| ID | Задача | Реализовано |
|----|--------|-------------|
| B-014 | Unified Naming Convention | reference/naming-convention.md + validate-naming.sh |
| B-005 | development-guide.md | docs/development-guide.md |

### Adding (новые из Project Mode)
| ID | Задача | Приоритет |
|----|--------|-----------|
| B-015 | Project Mode: custom modules support | Medium |
| B-016 | Project Mode: auto-detect stage from content | Low |
| B-017 | Merge evaluations: add project mode scenarios | Medium |

### Unchanged
- B-001: @requires clean-protocol (ждёт clean-protocol update)
- B-006: Claude A/B pattern (documented in development-guide)
- B-007-B-013: As is

---

## 10. Риски

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| SKILL.md > 300 lines | Medium | Держим core в SKILL.md, детали в reference/ |
| Confusion between modes | Low | Clear triggers, auto-detection |
| Breaking existing skills | None | Only additive changes |
| Reference bloat | Medium | Project refs in separate folder |

---

## 11. LOGIC-TREE Update Preview

```
2. INIT (Quick Config)
   2.1. Проверка: purpose определён?
   2.2. Определение MODE: Tool | Project     ← NEW
      2.2.1. "project" keyword → Project Mode
      2.2.2. Otherwise → Tool Mode
   2.3. Определение type: CREATE | UPDATE | REFACTOR | IMPORT ← +IMPORT
   ...

8. BUILD
   8.1. IF Tool Mode:
      8.1.1. reference/ structure
   8.2. IF Project Mode:                    ← NEW BRANCH
      8.2.1. data/ structure
      8.2.2. YAML modules по stage
      8.2.3. Document Coverage Matrix
   ...
```

---

## 12. Чеклист подтверждения

- [ ] План понятен
- [ ] Merge логичен (90% overlap)
- [ ] Project Architect становится режимом, не отдельным скиллом
- [ ] B-014 Naming Convention включён
- [ ] B-005 Development Guide включён
- [ ] Существующие скиллы не ломаются
- [ ] Версия 5.0.0 (MAJOR change)
- [ ] Можно начинать

---

## 13. Deliverables

После подтверждения:

1. **Step 1:** `skill-architect-v5.0.0.skill`
   - SKILL.md (updated)
   - README.md (updated)
   - MANIFEST.md (updated)
   - reference/ (7 existing + 5 new)
   - scripts/ (3 existing + 1 new)

2. **Step 2:** `skill-architect-v5.0.0-docs.zip`
   - v5.0.0-PLAN.md
   - v5.0.0-DIFF.md
   - CHANGELOG.md (appended)
   - BACKLOG.md (updated)
   - LOGIC-TREE.md (updated)
   - decisions/v5.0.0-decisions.md
   - development-guide.md (NEW)

3. **Step 3:** Deprecation notice для Project Architect

---

**⏳ Ожидаю подтверждение: "да" / "go" / "делай"**
