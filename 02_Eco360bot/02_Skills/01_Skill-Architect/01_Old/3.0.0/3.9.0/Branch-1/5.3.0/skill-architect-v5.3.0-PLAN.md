# Planning Document: skill-architect v5.3.0 "Version Sync"

**Дата:** 2025-12-02  
**Источник:** Аудит v5.2.0 docs + reference файлов + v3.9.0 SELF_AUDIT  
**Тип:** PATCH (синхронизация версий + недостающая документация)

---

## Executive Summary

**Проблема:** После v5.2.0 версии в файлах не синхронизированы, LOGIC-TREE устарел, нет инструкций по docs для других скиллов.

**Решение:** Исправить версии по правилу "версия файла меняется только если контент изменился", обновить LOGIC-TREE, добавить docs-packaging.md.

---

## ⚠️ ВАЖНО: Правило версионирования файлов

Из v3.9.0 MANIFEST концепции:

```
Версия ФАЙЛА ≠ Версия СКИЛЛА

- Версия файла меняется ТОЛЬКО если контент файла изменился
- Формат футера: *FileName vX.Y.Z | skill-architect vA.B.C*
- Пример: *engines.md v1.1.0 | skill-architect v5.3.0*
```

**Это значит:**
- НЕ обновляем версию файла если контент не менялся
- Обновляем только `skill-architect vX.Y.Z` в футере
- MANIFEST.md отслеживает версии каждого файла отдельно

---

## 🔴 Проблема 1: Рассинхрон версий в футерах

### Текущее состояние reference/ файлов:

| Файл | Версия файла | skill-architect v | Контент менялся? |
|------|--------------|-------------------|------------------|
| engines.md | v1.1.0 | v5.1.0 | Нет с v5.1.0 |
| evaluations.md | v1.0.0 | v4.1.0 ❌ | Нет с v4.1.0 |
| naming-convention.md | v1.0.0 | v5.0.0 | Нет с v5.0.0 |
| packaging.md | **нет футера** ❌ | — | — |
| planning-document.md | **нет футера** ❌ | — | — |
| project-filters.md | v1.0.0 | v5.0.0 | Нет с v5.0.0 |
| project-import.md | v1.0.0 | v5.0.0 | Нет с v5.0.0 |
| project-mode.md | v1.1.0 | v5.1.0 | Нет с v5.1.0 |
| project-modules.md | v1.0.0 | v5.0.0 | Нет с v5.0.0 |
| quality-checklist.md | v1.1.0 | v5.1.0 | Нет с v5.1.0 |
| self-diagnostic.md | v1.0.0 | v5.2.0 | Нет с v5.2.0 |
| templates.md | v1.1.0 | v5.1.0 | Нет с v5.1.0 |
| workflow.md | v1.1.0 | v5.1.0 | Нет с v5.1.0 |

### Текущее состояние корневых файлов:

| Файл | Версия | Проблема |
|------|--------|----------|
| README.md | v5.1.0 | Должно быть v5.2.0 (контент менялся) |
| SKILL.md | v5.2.0 | ✅ OK |
| MANIFEST.md | v5.2.0 | ✅ OK |

### Текущее состояние docs файлов:

| Файл | Версия файла | skill-architect v | Проблема |
|------|--------------|-------------------|----------|
| LOGIC-TREE.md | v1.2.0 | v5.0.0 ❌ | Устарел, нет v5.1/v5.2 changes |
| BACKLOG.md | v1.3.0 | v5.0.0 ❌ | Нет v5.2.0 в Done |
| development-guide.md | v1.0.0 | v5.0.0 | OK если контент не менялся |
| README.md (docs) | — | v5.1.0 ❌ | Устарел |

---

## 🔴 Проблема 2: LOGIC-TREE.md устарел

**Текущая версия:** v5.0.0

**Отсутствует:**
- ⛔ NEVER DEGRADE check (добавлен в v5.1.0)
- Skill Dependencies read (добавлен в v5.2.0)
- Reference Reading trigger (добавлен в v5.1.0)
- self-test/diagnose type (добавлен в v5.2.0)
- Diff секции v5.1.0 и v5.2.0

**Нужно добавить:**
```
0. PRE-ACTIVATION (NEW in v5.1.0)
   0.1. Read Skill Dependencies (clean-protocol)
   0.2. Read relevant reference/ based on trigger

2.3. Определение type: CREATE | UPDATE | REFACTOR | IMPORT | SELF-TEST ← NEW

7. PRE-BUILD CHECKPOINT
   7.1.6. □ NEVER DEGRADE verified ← NEW in v5.1.0
```

---

## 🔴 Проблема 3: BACKLOG не обновлён для v5.2.0

**В секции Done отсутствует v5.2.0:**

| # | Задача | Реализовано |
|---|--------|-------------|
| — | Skill Dependencies section | SKILL.md |
| — | Self-diagnostic protocol | reference/self-diagnostic.md |
| — | Self-diagnostic script | scripts/self-diagnostic.sh |
| — | Extended Reference Reading | +2 triggers |

---

## 🔴 Проблема 4: Нет инструкций про docs для ДРУГИХ скиллов

**Ситуация:** LOGIC-TREE Step 12 описывает docs.zip, но:
- ❌ Нет в SKILL.md детального описания
- ❌ Нет в workflow.md фазы для DOCS
- ❌ Нет шаблонов LOGIC-TREE, BACKLOG, CHANGELOG
- ❌ Нет reference/docs-packaging.md

**Последствие:** При создании скиллов Claude не делает docs.zip для пользователей.

---

## 🔴 Проблема 5: Нет автоматизации версий

- ❌ Версии в 17+ файлах обновляются вручную
- ❌ Забываем обновить → рассинхрон
- ❌ Нет скрипта bump-version.sh

---

## KEEP (не трогать)

```
□ SKILL.md — логика и структура
□ reference/*.md — контент (только версии в футерах)
□ scripts/*.sh — логика (только добавляем новый)
□ Структура docs
```

---

## FIX (исправить)

### Правило: версия файла vs версия скилла

```
Футер: *FileName vX.Y.Z | skill-architect vA.B.C*
         ↑                  ↑
         Версия ФАЙЛА       Версия СКИЛЛА
         (меняем если       (всегда актуальная)
         контент изменился)
```

### Skill reference/ файлы — обновить skill-architect версию в футере:

| Файл | Действие |
|------|----------|
| engines.md | `v5.1.0` → `v5.3.0` (только skill version) |
| evaluations.md | `v4.1.0` → `v5.3.0` (только skill version) |
| naming-convention.md | `v5.0.0` → `v5.3.0` |
| packaging.md | **ДОБАВИТЬ футер:** `*packaging.md v1.0.0 | skill-architect v5.3.0*` |
| planning-document.md | **ДОБАВИТЬ футер:** `*planning-document.md v1.0.0 | skill-architect v5.3.0*` |
| project-filters.md | `v5.0.0` → `v5.3.0` |
| project-import.md | `v5.0.0` → `v5.3.0` |
| project-mode.md | `v5.1.0` → `v5.3.0` |
| project-modules.md | `v5.0.0` → `v5.3.0` |
| quality-checklist.md | `v5.1.0` → `v5.3.0` |
| self-diagnostic.md | `v5.2.0` → `v5.3.0` |
| templates.md | `v5.1.0` → `v5.3.0` |
| workflow.md | `v5.1.0` → `v5.3.0` + **ДОБАВИТЬ Phase 6: DOCS** → версия файла `v1.1.0` → `v1.2.0` |

### Skill корневые файлы:

| Файл | Действие |
|------|----------|
| README.md | Обновить до v5.3.0 (контент менялся — добавить v5.2.0/v5.3.0 info) |
| SKILL.md | Обновить description до v5.3.0 |
| MANIFEST.md | Полностью перегенерировать |

### Docs файлы — обновить контент И версии:

| Файл | Версия файла | Действие |
|------|--------------|----------|
| LOGIC-TREE.md | v1.2.0 → **v1.3.0** | Добавить v5.1.0, v5.2.0, v5.3.0 changes |
| BACKLOG.md | v1.3.0 → **v1.4.0** | Добавить v5.2.0 в Done, обновить header |
| development-guide.md | v1.0.0 | Без изменений (контент OK) |
| README.md | — → **v1.0.0** | Обновить до v5.3.0 |

---

## ADD (добавить)

### 1. reference/docs-packaging.md (~150 lines)

**Зачем:** Инструкции по созданию docs.zip для скиллов, которые мы создаём.

Содержимое:
- Когда создавать docs (complex skills с >3 reference файлов)
- Структура docs.zip
- Шаблоны: LOGIC-TREE, BACKLOG, CHANGELOG, decisions/
- Команды упаковки
- Версионирование файлов (правило: версия файла ≠ версия скилла)

### 2. workflow.md: Phase 6 DOCS (~30 lines)

Добавить после Phase 5:
```markdown
## Phase 6: Documentation (optional, 5 min)

**When:** Complex skills (>3 reference files) or user requests docs.

### Create docs folder
skill-name-docs/
├── vX.Y.Z-PLAN.md      # Planning document
├── vX.Y.Z-DIFF.md      # Changes summary  
├── CHANGELOG.md        # Version history
├── BACKLOG.md          # Future ideas (optional)
├── LOGIC-TREE.md       # Flow visualization (if complex)
├── README.md           # Detailed documentation
└── decisions/          # Architectural decisions (optional)
    └── vX.Y.Z-decisions.md

### Package
zip -r skill-name-vX.Y.Z-docs.zip skill-name-docs/
cp skill-name-vX.Y.Z-docs.zip /mnt/user-data/outputs/
```

### 3. LOGIC-TREE.md обновления (~50 lines)

Добавить:
- Step 0: PRE-ACTIVATION (Skill Dependencies, Reference Reading)
- type: SELF-TEST в 2.3
- 7.1.6: NEVER DEGRADE verified
- Diff v5.0.0 → v5.1.0
- Diff v5.1.0 → v5.2.0
- Diff v5.2.0 → v5.3.0

### 4. BACKLOG.md обновления

Добавить в Done v5.2.0:
```markdown
### v5.2.0

| # | Задача | Реализовано |
|---|--------|-------------|
| — | Skill Dependencies section | SKILL.md |
| — | Self-diagnostic protocol | reference/self-diagnostic.md |
| — | Self-diagnostic script | scripts/self-diagnostic.sh |
| — | Extended Reference Reading | +2 triggers |
```

Добавить новые задачи из этого чата:
```markdown
### B-018: Docs packaging для создаваемых скиллов
**Источник:** v5.3.0 audit  
**Суть:** Claude не создаёт docs.zip для скиллов которые делает
**Статус:** Реализовано в v5.3.0

### B-019: Версионирование файлов enforcement
**Источник:** v5.3.0 audit  
**Суть:** Футеры в файлах рассинхронизируются
**Статус:** Документировано в docs-packaging.md
```

---

## Метрики

| Metric | Before | After |
|--------|--------|-------|
| Files with wrong skill-architect version | 13 | 0 |
| Files missing footer | 2 | 0 |
| LOGIC-TREE version | v1.2.0 (v5.0.0) | v1.3.0 (v5.3.0) |
| BACKLOG version | v1.3.0 | v1.4.0 |
| Reference files | 13 | 14 (+docs-packaging.md) |
| workflow.md version | v1.1.0 | v1.2.0 (+Phase 6) |

---

## Chat Verification

Проверено из чата и загруженных документов:

### Из текущего чата:
1. ✅ LOGIC-TREE.md в docs, не в skill (это OK)
2. ✅ LOGIC-TREE версия v5.0.0 (устарел)
3. ✅ BACKLOG версия рассинхрон
4. ✅ development-guide версия v5.0.0
5. ✅ README (docs) версия v5.1.0
6. ✅ README (skill) версия v5.1.0
7. ✅ evaluations.md версия v4.1.0
8. ✅ packaging.md нет футера
9. ✅ planning-document.md нет футера
10. ✅ Нет инструкций docs для других скиллов
11. ✅ Нарушение clean-protocol (план в чате)

### Из v3.9.0 SELF_AUDIT_REPORT:
12. ✅ Правило версионирования: версия файла ≠ версия скилла
13. ✅ Формат футера: `*FileName vX.Y.Z | skill-architect vA.B.C*`
14. ✅ MANIFEST отслеживает версии файлов отдельно
15. ✅ Рассинхрон версий — известная проблема

### Из v5.0.0-PLAN:
16. ✅ LOGIC-TREE должен обновляться при изменении flow
17. ✅ docs.zip включает: PLAN, DIFF, CHANGELOG, BACKLOG, LOGIC-TREE, decisions/

### Из v3.8.0-PLAN (SKILL_ARCHITECT_UPDATE_PLAN):
18. ✅ Planning Document First концепция
19. ✅ Chat Verification step

### Из v3.9.0-PLAN (skill-architect_UPDATE_PLAN):
20. ✅ MANIFEST.md для целостности
21. ✅ generate-manifest.sh
22. ✅ Clean Skill Principles

**Verified: 22 items. Missing: none.**

---

## Deliverables

### Step 1: skill-architect-v5.3.0.skill

```
skill-architect/
├── SKILL.md (v5.3.0 в description)
├── README.md (v5.3.0)
├── MANIFEST.md (перегенерирован)
├── reference/
│   ├── docs-packaging.md (NEW v1.0.0)
│   ├── engines.md (v1.1.0 | v5.3.0)
│   ├── evaluations.md (v1.0.0 | v5.3.0)
│   ├── naming-convention.md (v1.0.0 | v5.3.0)
│   ├── packaging.md (v1.0.0 | v5.3.0) +footer
│   ├── planning-document.md (v1.0.0 | v5.3.0) +footer
│   ├── project-filters.md (v1.0.0 | v5.3.0)
│   ├── project-import.md (v1.0.0 | v5.3.0)
│   ├── project-mode.md (v1.1.0 | v5.3.0)
│   ├── project-modules.md (v1.0.0 | v5.3.0)
│   ├── quality-checklist.md (v1.1.0 | v5.3.0)
│   ├── self-diagnostic.md (v1.0.0 | v5.3.0)
│   ├── templates.md (v1.1.0 | v5.3.0)
│   └── workflow.md (v1.2.0 | v5.3.0) +Phase 6
└── scripts/
    ├── audit-project.sh (v1.0.0)
    ├── audit-skill.sh (v1.0.0)
    ├── generate-manifest.sh (v1.0.0)
    ├── self-diagnostic.sh (v1.0.0)
    ├── validate-naming.sh (v1.0.0)
    └── validate-skill.sh (v1.4.0)
```

### Step 2: skill-architect-v5.3.0-docs.zip

```
skill-architect-docs/
├── v5.3.0-PLAN.md (этот файл)
├── v5.3.0-DIFF.md (NEW)
├── CHANGELOG.md (v1.4.0, +v5.3.0 entry)
├── BACKLOG.md (v1.4.0, +v5.2.0 Done, +B-018/B-019)
├── LOGIC-TREE.md (v1.3.0, +v5.1/v5.2/v5.3 changes)
├── development-guide.md (v1.0.0, без изменений)
├── README.md (v1.0.0, обновлён до v5.3.0)
├── v5.0.0-PLAN.md (сохранён)
├── v5.0.0-DIFF.md (сохранён)
├── v5.1.0-PLAN.md (сохранён)
├── v5.1.0-DIFF.md (сохранён)
├── v5.2.0-PLAN.md (сохранён)
├── v5.2.0-DIFF.md (сохранён)
└── decisions/
    ├── v4.0.0-decisions.md
    ├── v4.1.0-decisions.md
    ├── v5.0.0-decisions.md
    ├── v5.1.0-decisions.md
    ├── v5.2.0-decisions.md
    └── v5.3.0-decisions.md (NEW)
```

---

## Риски

| Риск | Митигация |
|------|-----------|
| Пропустить файл при обновлении | MANIFEST.md как чеклист |
| Сломать контент | Только футеры + новый файл |
| workflow.md сломается | Добавляем Phase 6, не меняем 1-5 |

---

**Ожидаю подтверждение: "да" / "go" / "делай"**

---

*Planning Document v5.3.0 | skill-architect*
