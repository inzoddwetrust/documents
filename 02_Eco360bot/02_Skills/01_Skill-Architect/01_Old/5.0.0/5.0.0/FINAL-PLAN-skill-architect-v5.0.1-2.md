# FINAL PLAN: skill-architect v5.0.0 → v5.0.1

## Meta

| Field | Value |
|-------|-------|
| From | v5.0.0 "Micro-Skills" |
| To | v5.0.1 "Micro-Skills Polished" |
| Type | Patch (fixes, no breaking changes) |
| Date | 2025-12-18 |
| Files to modify | 22 |
| Lines to add | ~180 |
| Lines to remove | ~50 |

---

## 1. Выявленные проблемы в v5.0.0

### 1.1 Критические несогласованности

| Проблема | Где | Что не так |
|----------|-----|------------|
| **G12-G16 конфликт** | reference/genetic-audit.md | Старые Self-Audit Genes v4.x вместо Protocol Genes v5.0 |
| **SPEED KILL отсутствует** | SKILL.md | Был в v4.7.0, потерян при рефакторинге |
| **G16 пропущен** | P03a-build, README | Списки показывают G12-G15, не G12-G16 |
| **Счётчик генов** | P05-genes | "15 genes" вместо "16 genes" |

### 1.2 Footers с устаревшей версией

Все 14 reference файлов имеют footer `*X.md | skill-architect v4.6.0*`

### 1.3 Отсутствующие секции

| Что | Где должно быть |
|-----|-----------------|
| Dependencies | README-skill-architect.md |
| Self-Audit Checklist | P05-genes.md |
| "User time is irreplaceable" | P03a-build.md |

---

## 2. Принятые решения

| # | Вопрос | Решение |
|---|--------|---------|
| 1 | SPEED KILL | Полный блок в SKILL.md + напоминания в протоколах |
| 2 | G12-G16 naming | "Protocol Genes" везде (не "Micro-Skills Genes") |
| 3 | Self-Audit | Отдельный чеклист в P05-genes (не гены) |
| 4 | Reference footers | Убрать версии → "Part of skill-architect reference" |
| 5 | Dependencies | Добавить в README-skill-architect.md |

---

## 3. Batch Plan

### Batch 1: SKILL.md — добавить SPEED KILL (~40 строк)

**Файл:** `SKILL.md`

**Действие:** Добавить секцию после "## Commands":

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
```

**Также:** Обновить frontmatter description → v5.0.1

---

### Batch 2: Протоколы — SPEED KILL напоминания (4 файла)

#### P02-plan.md
После "## ⛔ CRITICAL" добавить:
```markdown
> ⚠️ **SPEED KILL:** Do NOT proceed without explicit user confirmation. Checkpoint = insurance.
```

#### P03a-build.md
1. Заменить строку 22-23:
```markdown
5. **Never optimize for speed** — correct > fast
```
На:
```markdown
5. **SPEED KILL applies here:**
   - Never optimize for speed — correct > fast
   - User time is irreplaceable — your assumptions cost their hours
   - After EVERY batch: checkpoint → STOP → wait → continue
```

2. Заменить строку 139:
```markdown
### Micro-Skills Genes (G12-G15)
```
На:
```markdown
### Protocol Genes (G12-G16)
```

3. Добавить G16 в таблицу:
```markdown
| G16 | docs/ at skill root level |
```

#### P03b-validate.md
После "## ⛔ CRITICAL" добавить:
```markdown
> ⚠️ **SPEED KILL:** ⛔ means STOP. Wait for user. No exceptions.
```

#### P04-deliver.md
После "## ⛔ CRITICAL" добавить:
```markdown
> ⚠️ **SPEED KILL:** Don't rush delivery. One mistake = user hours lost.
```

**Для всех 4 файлов:** Обновить description → v5.0.1

---

### Batch 3: P05-genes.md — исправление генов + Self-Audit

**Изменения:**

1. Строка 3: `G01-G15` → `G01-G16`
2. Строка 17: `15 genes` → `16 genes`
3. Строка 53: `Micro-Skills Genes` → `Protocol Genes`

4. Добавить новую секцию после "## Self-Checkup":

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

\`\`\`markdown
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
\`\`\`
```

5. Обновить description → v5.0.1

---

### Batch 4: reference/genetic-audit.md — полная синхронизация

**⚠️ КРИТИЧЕСКИ ВАЖНО:** Этот файл имеет старые G12-G16!

**Изменения:**

1. **Заменить секцию** строки 82-91:

```markdown
## Protocol Genes (G12-G16)

| ID | Gene | Requirement | Validation |
|----|------|-------------|------------|
| G12 | Protocol Boundary | One protocol = one step | Single responsibility |
| G13 | Self-Contained | Works without reading others | No cross-dependencies |
| G14 | Explicit Handoff | NEXT: P0X-name | `grep "NEXT:"` shows protocol name |
| G15 | Router Pattern | Complex workflows via router | Router file exists |
| G16 | Docs Separation | docs/ at skill root level | `test -d docs/` |
```

2. **Добавить новую секцию** после Protocol Genes:

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

3. **Обновить Gene Summary** строки 94-101:

```markdown
## Gene Summary

| Category | Genes | Scope |
|----------|-------|-------|
| Core | G01-G07 | All skills |
| Cognitive | G08-G11 | All skills |
| Protocol | G12-G16 | All micro-skills |

**Note:** skill-architect has additional Self-Audit Checklist (see above).
```

4. **Обновить Gene Inheritance Report** строка 147:
`{N}/11 genes` → `{N}/16 genes`

5. **Удалить footer** строка 170

---

### Batch 5: README-skill-architect.md — Dependencies + G16

**Изменения:**

1. Строка 65: `(G12-G15)` → `(G12-G16)`

2. Добавить G16 в таблицу после G15:
```markdown
| G16 | Docs Separation — docs/ на уровне skill |
```

3. **Добавить секцию** перед "## Миграция с v4.x":

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
| `zip` | Archive creation | Packaging phase |

### System
- Python 3.x (for ZIP packaging fallback)
```

4. Обновить заголовок → v5.0.1

---

### Batch 6: Reference файлы — footers (14 файлов)

**Файлы:**
- anchor-format.md
- checkpoint-format.md
- cognitive-razors.md
- diff-format.md
- ecosystem-paths.md
- evaluations.md
- inot-engine.md
- memory-budget.md
- naming.md
- packaging.md
- planning-document.md
- quality-gates.md
- templates.md

**Действие для каждого:** Найти последнюю строку вида:
```
*X.md | skill-architect vN.N.N*
```

Заменить на:
```
*Part of skill-architect reference*
```

---

### Batch 7: CHANGELOG + MANIFEST + Version bump

#### CHANGELOG-skill-architect.md

Добавить в начало после заголовка:

```markdown
## [5.0.1] - 2025-12-18 "Micro-Skills Polished"

### Fixed
- **SPEED KILL restored** — full block in SKILL.md + reminders in all ⛔ protocols
- **Genes G12-G16 synchronized** — now "Protocol Genes" everywhere
- **G16 added** to P03a-build and README gene lists
- **reference/genetic-audit.md** — replaced old v4.x Self-Audit Genes with Protocol Genes

### Added
- Self-Audit Checklist in P05-genes.md (separate from genes)
- Self-Audit Checklist in genetic-audit.md
- Dependencies section in README-skill-architect.md
- "User time is irreplaceable" in P03a-build SPEED KILL

### Changed
- All reference files: footer changed to "Part of skill-architect reference"
- Gene count: 15 → 16 in all places

### Metrics
| Metric | v5.0.0 | v5.0.1 | Delta |
|--------|--------|--------|-------|
| Files | 40 | 40 | — |
| Lines | ~6178 | ~6358 | +180 |

---
```

#### MANIFEST.md

Обновить version → 5.0.1

#### Version bump в файлах:

| File | Field |
|------|-------|
| SKILL.md | description → v5.0.1 |
| P01-init.md | description → v5.0.1 |
| P02-plan.md | description → v5.0.1 |
| P03a-build.md | description → v5.0.1 |
| P03b-validate.md | description → v5.0.1 |
| P03c-docs.md | description → v5.0.1 |
| P04-deliver.md | description → v5.0.1 |
| P05-genes.md | description → v5.0.1 |

---

## 4. Execution Order

```
Batch 1 (SKILL.md + SPEED KILL)
    │
    ▼
Batch 2 (P02, P03a, P03b, P04 — reminders)
    │
    ▼
Batch 3 (P05-genes — Self-Audit)
    │
    ▼
Batch 4 (genetic-audit.md — CRITICAL fix)
    │
    ▼
Batch 5 (README — Dependencies + G16)
    │
    ▼
Batch 6 (14 reference footers)
    │
    ▼
Batch 7 (CHANGELOG + version bump)
    │
    ▼
✅ Validate → Package → Deliver
```

---

## 5. Pre-Release Checklist

### Structure
- [ ] SPEED KILL в SKILL.md
- [ ] SPEED KILL напоминания в P02, P03a, P03b, P04
- [ ] G12-G16 = "Protocol Genes" везде
- [ ] G16 в списках P03a-build и README
- [ ] Self-Audit Checklist в P05-genes
- [ ] Self-Audit Checklist в genetic-audit.md
- [ ] Dependencies в README

### Versions
- [ ] Все protocols/*.md → v5.0.1
- [ ] SKILL.md → v5.0.1
- [ ] MANIFEST.md → 5.0.1
- [ ] README → v5.0.1
- [ ] CHANGELOG содержит v5.0.1

### Footers
- [ ] Все 13 reference files → "Part of skill-architect reference"
- [ ] genetic-audit.md footer удалён

### Validation
- [ ] `checkup` проходит без ошибок
- [ ] Genetic audit показывает 16/16 genes

---

## 6. File Change Summary

| File | Changes |
|------|---------|
| SKILL.md | +SPEED KILL (~40 lines), version bump |
| P02-plan.md | +reminder (1 line), version bump |
| P03a-build.md | +SPEED KILL (5 lines), G16, rename section, version bump |
| P03b-validate.md | +reminder (1 line), version bump |
| P04-deliver.md | +reminder (1 line), version bump |
| P05-genes.md | Fix counts, +Self-Audit (~30 lines), rename section, version bump |
| README-skill-architect.md | +Dependencies (~20 lines), +G16, version bump |
| reference/genetic-audit.md | **MAJOR FIX:** replace G12-G16, +Self-Audit Checklist |
| 13 × reference/*.md | Footer update |
| CHANGELOG-skill-architect.md | +v5.0.1 section |
| MANIFEST.md | Version bump |

**Total: 22 files modified**

---

## 7. Risks

| Risk | Mitigation |
|------|------------|
| Пропустить файл | Чеклист + grep проверка |
| Несогласованность версий | `grep -r "v5.0.0" после update |
| SPEED KILL слишком длинный | ~40 строк — приемлемо для SKILL.md |
| genetic-audit.md сломан | Полная замена секции G12-G16 |

---

*FINAL-PLAN-skill-architect-v5.0.1.md | Ready for execution*
