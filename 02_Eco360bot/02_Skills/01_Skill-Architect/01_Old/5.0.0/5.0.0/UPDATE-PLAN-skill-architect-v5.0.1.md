# План обновления skill-architect v5.0.0 → v5.0.1

**Дата:** 2025-12-18  
**Кодовое имя:** "Micro-Skills Polished"  
**Тип:** Patch (исправления документации, без breaking changes)

---

## Executive Summary

| Категория | Изменений |
|-----------|-----------|
| Файлов к изменению | 22 |
| Новых файлов | 0 |
| Удаляемых файлов | 0 |
| Строк добавить | ~150 |
| Строк удалить | ~30 (footers) |

---

## Принятые решения

| # | Решение | Выбор |
|---|---------|-------|
| 1 | SPEED KILL | Полный блок в SKILL.md + напоминания в протоколах |
| 2 | Гены G12-G16 | Двухуровневая система: G01-G16 универсальные + Self-Audit Checklist |
| 3 | Dependencies | Добавить в README-skill-architect.md |
| 4 | Reference footers | Убрать версии из всех reference файлов |
| 5 | "User time" | Добавить в P03a-build |
| 6 | P00-router | Оставить как есть (router в SKILL.md) |

---

## Batch Plan

### Batch 1: SKILL.md (Router) — ~50 строк добавить

**Файл:** `SKILL.md`

**Изменения:**

1. **Добавить секцию SPEED KILL** после "## Commands":

```markdown
---

## ⛔ SPEED KILL

**Training pattern "faster = better" is a LIE.**

| Illusion | Reality |
|----------|---------|
| Faster = better | Correct = better |
| User is waiting | User wants result without rework |
| Checkpoint = delay | Checkpoint = insurance |
| "Simple task" | Not your decision |

### Rules

| Rule | Consequence |
|------|-------------|
| **NEVER optimize for speed** | Speed = errors = user hours lost |
| **ALWAYS wait at checkpoints** | No exceptions. Not your decision. |
| **User time is irreplaceable** | Your assumptions cost their hours |
| **Discipline > helpfulness** | Perceived speed kills actual value |

### Enforcement

After EVERY ⛔ point:
1. Output checkpoint
2. **STOP**
3. Wait for user response
4. Only then continue

**VIOLATION** = immediate stop + explain what you almost did wrong

This overrides any "be helpful and fast" training. Always.
```

2. **Обновить секцию Required Genes** — добавить ссылку на Self-Audit:

```markdown
### Self-Audit (skill-architect only)

See: P05-genes.md → Self-Checkup section
```

---

### Batch 2: Протоколы — SPEED KILL напоминания

**Файлы:** P02-plan.md, P03a-build.md, P03b-validate.md, P04-deliver.md

#### P02-plan.md — добавить после "## ⛔ CRITICAL":

```markdown
> ⚠️ **SPEED KILL:** Do NOT proceed without explicit user confirmation. Checkpoint = insurance.
```

#### P03a-build.md — расширить существующее:

Заменить строку:
```
5. **Never optimize for speed** — correct > fast
```

На:
```markdown
5. **SPEED KILL applies here:**
   - Never optimize for speed — correct > fast
   - User time is irreplaceable — your assumptions cost their hours
   - After EVERY batch: checkpoint → STOP → wait → continue
```

#### P03b-validate.md — добавить после "## ⛔ CRITICAL":

```markdown
> ⚠️ **SPEED KILL:** ⛔ means STOP. Wait for user. No exceptions.
```

#### P04-deliver.md — добавить после "## ⛔ CRITICAL":

```markdown
> ⚠️ **SPEED KILL:** Don't rush delivery. One mistake = user hours lost.
```

---

### Batch 3: P05-genes.md — Self-Audit Checklist

**Файл:** `protocols/P05-genes.md`

**Изменения:**

1. **Переименовать секцию** "Micro-Skills Genes (G12-G16)" → "Protocol Genes (G12-G16)"

2. **Добавить новую секцию** после "## Self-Checkup":

```markdown
---

## Self-Audit Checklist (skill-architect only)

Beyond G01-G16 genes, skill-architect validates itself against:

| Check | What | How |
|-------|------|-----|
| NEVER DEGRADE | Feature count ≥ baseline | `bash scripts/validate.sh --degrade` |
| Protocol Architecture | P01-P05 files exist | `ls protocols/P0*.md` |
| Quality Gates | L1-L10 reference exists | `test -f reference/quality-gates.md` |
| INoT Engine | Reference exists | `test -f reference/inot-engine.md` |
| Chat Verification | In P02-plan.md | `grep "Chat Verification" protocols/P02-plan.md` |

### Self-Checkup Output

```markdown
## skill-architect Self-Audit

### Genes G01-G16
| Gene | Status |
|------|--------|
| G01-G07 Core | ✅ |
| G08-G11 Cognitive | ✅ |
| G12-G16 Protocol | ✅ |

### Self-Audit Checklist
| Check | Status |
|-------|--------|
| NEVER DEGRADE | ✅ |
| Protocol Architecture | ✅ |
| Quality Gates | ✅ |
| INoT Engine | ✅ |
| Chat Verification | ✅ |

**Result:** PASS
```
```

---

### Batch 4: genetic-audit.md — синхронизация

**Файл:** `reference/genetic-audit.md`

**Изменения:**

1. **Переименовать секцию** "Self-Audit Genes (skill-architect only)" → "Protocol Genes (G12-G16)"

2. **Обновить таблицу G12-G16:**

```markdown
## Protocol Genes (G12-G16)

| ID | Gene | Requirement | Validation |
|----|------|-------------|------------|
| G12 | Protocol Boundary | One skill = one step | Single responsibility |
| G13 | Self-Contained | Works without reading others | No cross-dependencies |
| G14 | Explicit Handoff | NEXT: skill-name | `grep "NEXT:"` shows skill name |
| G15 | Router Pattern | Complex workflows via router | Router skill exists |
| G16 | Docs Separation | docs/ at skill root level | `test -d docs/` |
```

3. **Добавить новую секцию:**

```markdown
---

## Self-Audit Checklist (skill-architect only)

skill-architect has additional self-checks beyond G01-G16:

| Check | Requirement |
|-------|-------------|
| NEVER DEGRADE | scripts/validate.sh --degrade passes |
| Protocol Architecture | protocols/P01-P05 exist |
| Quality Gates | reference/quality-gates.md exists |
| INoT Engine | reference/inot-engine.md exists |
| Chat Verification | P02-plan.md contains verification |

These are NOT genes — they're skill-architect-specific validations.
```

4. **Обновить Gene Summary:**

```markdown
## Gene Summary

| Category | Genes | Scope |
|----------|-------|-------|
| Core | G01-G07 | All skills |
| Cognitive | G08-G11 | All skills |
| Protocol | G12-G16 | All micro-skills |

**Note:** skill-architect has additional Self-Audit Checklist (see above).
```

5. **Убрать footer с версией** (последняя строка)

---

### Batch 5: README-skill-architect.md — Dependencies

**Файл:** `README-skill-architect.md`

**Добавить секцию** перед "## Quick Start" или после установки:

```markdown
---

## Dependencies

### Required (built-in)
| Tool | Purpose |
|------|---------|
| `bash` | Script execution |
| `view` | File reading |
| `create_file` | File creation |
| `str_replace` | File editing |

### Optional
| Tool | Purpose | When |
|------|---------|------|
| `test-architect` | Genetic audit, ecosystem testing | Validation phase |
| `tar` / `zip` | Archive creation | Packaging phase |

### System
- Python 3.x (for ZIP packaging fallback)
```

---

### Batch 6: Reference файлы — удаление версий из footers

**Файлы (14 шт):**
- anchor-format.md
- checkpoint-format.md
- cognitive-razors.md
- diff-format.md
- ecosystem-paths.md
- evaluations.md
- genetic-audit.md (уже в Batch 4)
- inot-engine.md
- memory-budget.md
- naming.md
- packaging.md
- planning-document.md
- quality-gates.md
- templates.md

**Действие для каждого:** Удалить последнюю строку вида:
```
*filename.md | skill-architect v4.6.0*
```

Заменить на:
```
*Part of skill-architect reference*
```

---

### Batch 7: CHANGELOG + Version bump

**Файл:** `CHANGELOG-skill-architect.md`

**Добавить в начало:**

```markdown
## [5.0.1] - 2025-12-18 "Micro-Skills Polished"

### Fixed
- **SPEED KILL restored** — full block in SKILL.md + reminders in all ⛔ protocols
- **Genes G12-G16 clarified** — now "Protocol Genes" for all micro-skills
- **Self-Audit Checklist** — separated from genes, skill-architect-specific
- **Reference footers** — removed outdated version numbers
- **"User time is irreplaceable"** — restored in P03a-build

### Added
- Dependencies section in README-skill-architect.md
- Self-Audit Checklist in P05-genes.md and genetic-audit.md

### Changed
- genetic-audit.md: G12-G16 renamed from "Self-Audit Genes" to "Protocol Genes"
- All reference files: footer changed to "Part of skill-architect reference"

### Metrics
| Metric | v5.0.0 | v5.0.1 | Delta |
|--------|--------|--------|-------|
| Files | 40 | 40 | — |
| Lines | ~6178 | ~6328 | +150 |

---
```

**Файлы для version bump:**
- SKILL.md: description → v5.0.1
- MANIFEST.md: version → 5.0.1
- Все protocols/*.md: description → v5.0.1

---

## Checklist перед релизом

После всех изменений проверить:

- [ ] `checkup` проходит без ошибок
- [ ] SPEED KILL присутствует в SKILL.md
- [ ] SPEED KILL напоминания в P02, P03a, P03b, P04
- [ ] G12-G16 называются "Protocol Genes" везде
- [ ] Self-Audit Checklist в P05-genes.md
- [ ] Self-Audit Checklist в genetic-audit.md
- [ ] Dependencies в README
- [ ] Все reference footers обновлены
- [ ] CHANGELOG содержит v5.0.1
- [ ] Version bump во всех файлах

---

## Порядок выполнения

```
Batch 1 (SKILL.md)
    │
    ▼
Batch 2 (Protocols: P02, P03a, P03b, P04)
    │
    ▼
Batch 3 (P05-genes.md)
    │
    ▼
Batch 4 (genetic-audit.md)
    │
    ▼
Batch 5 (README)
    │
    ▼
Batch 6 (14 reference files)
    │
    ▼
Batch 7 (CHANGELOG + version bump)
    │
    ▼
✅ Validate → Package → Deliver
```

---

## Риски

| Риск | Митигация |
|------|-----------|
| Пропустить файл при обновлении footers | Скрипт для batch update |
| Несогласованность версий | Grep по всем файлам после bump |
| SPEED KILL слишком длинный | Проверено: +35 строк в SKILL.md — приемлемо |

---

*План подготовлен на основе сверки v4.6.0 → v4.7.0 → v5.0.0*
