# skill-architect: ОБЪЕДИНЁННЫЙ ПЛАН v7.2.0 → v8.0.0

## "Testing Evolution"

**Дата:** 2025-12-07  
**Тип:** Major refactor (баги + архитектура тестирования)  
**Статус:** ✅ ВЫПОЛНЕНО

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Russian |
| NEVER DEGRADE | Применяется |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

Провели полный self-audit skill-architect v7.2.0:

| Фаза | Результат |
|------|-----------|
| Genetic Audit | 58% наследование — **проблема** |
| Self-Diagnostic | 35/36 — битая ссылка P07 |
| Validation | MANIFEST устарел, false positives |
| Virtual Testing | Score 65/100 < 70 gate |

**Главный вывод:** skill-architect не следует собственным стандартам.

---

## 2. Цели

### План A: Исправить баги v7.2.0
- Критические баги после "Docs Reorder" refactor
- False positives в скриптах
- Недостающие DNA правила

### План B: Улучшить систему тестирования
- Консолидация файлов (8 → 4)
- Новый Genetic Audit
- Интегрированный self-audit flow

**Решение:** Объединить в один релиз v8.0.0

---

## 3. Проблемы / Задачи

### 🔴 CRITICAL (из Плана A)

| # | Проблема | Файл |
|---|----------|------|
| C1 | Битая ссылка P07→P08 | scripts/self-diagnostic.sh:164 |
| C2 | MANIFEST не sync | MANIFEST.md |

### 🟡 SERIOUS (из Плана A)

| # | Проблема | Файл |
|---|----------|------|
| S1 | NEVER DEGRADE без enforcement | P04-build.md |
| S2 | Нет ## Output | SKILL.md |
| S3 | Правила размеров устарели | quality-checklist.md |
| S4 | Кириллица false positive | audit-skill.sh |
| S5 | SSOT без пометок | ssot-check.sh |

### 🔵 ARCHITECTURE (из Плана B)

| # | Задача | Описание |
|---|--------|----------|
| A1 | Genetic Audit | Новый протокол + скрипт |
| A2 | Testing consolidation | 8 файлов → 4 |
| A3 | VT integration | Personas, adversarial, expert в один файл |
| A4 | Self-audit flow | Интегрированная команда |

---

## 4. План изменений

### ✅ ДОБАВЛЯЕМ

| Файл | Источник |
|------|----------|
| reference/genetic-audit.md | План B: A1 |
| scripts/genetic-audit.sh | План B: A1 |
| reference/testing-framework.md | План B: A2 |
| ## Output в SKILL.md | План A: S2 |
| NEVER DEGRADE checklist в P04 | План A: S1 |
| File Size Rules в quality-checklist | План A: S3 |
| Modular Structure pattern | План A: S3 |
| SSOT Note pattern | План A: S5 |
| Update Safety rules | План A: S1 |

### ✏️ ИЗМЕНЯЕМ

| Файл | Что | Источник |
|------|-----|----------|
| scripts/self-diagnostic.sh:164 | P07 link fix | План A: C1 |
| scripts/audit-skill.sh | Cyrillic \p{Cyrillic}, 250KB | План A: S4, S3 |
| scripts/ssot-check.sh | SSOT Note awareness | План A: S5 |
| reference/virtual-testing.md | +personas, +adversarial, +expert | План B: A3 |
| SKILL.md | +Output, +triggers, v8.0.0 | План A+B |
| MANIFEST.md | Regenerate | План A: C2 |

### ❌ УДАЛЯЕМ (merge)

| Файл | Куда | Источник |
|------|------|----------|
| test-levels.md | → testing-framework.md | План B: A2 |
| test-cases.md | → testing-framework.md | План B: A2 |
| evaluations.md | → testing-framework.md | План B: A2 |
| personas.md | → virtual-testing.md | План B: A3 |
| adversarial.md | → virtual-testing.md | План B: A3 |
| expert-panel.md | → virtual-testing.md | План B: A3 |

### 🔒 НЕ ТРОГАЕМ

- Все протоколы P00-P08 (кроме P04)
- Project Mode файлы
- validate-naming.sh, validate-docs.sh
- engines.md, templates.md, workflow.md

---

## 5. Порядок выполнения

```
PHASE 1: Critical Fixes (План A)
├── [1] Fix self-diagnostic.sh:164           ✅
└── [2] Test self-diagnostic                 ✅

PHASE 2: Create New (План B)
├── [3] Create genetic-audit.md              ✅
├── [4] Create genetic-audit.sh              ✅
└── [5] Create testing-framework.md          ✅

PHASE 3: Consolidate (План B)
├── [6] Enhance virtual-testing.md           ✅
├── [7] Remove merged files (6)              ✅
└── [8] Update internal links                ✅

PHASE 4: Update Scripts (План A)
├── [9] audit-skill.sh (Cyrillic, size)      ✅
├── [10] ssot-check.sh (SSOT Note)           ✅
└── [11] self-diagnostic.sh (genetic link)   ✅

PHASE 5: Update Core (План A + B)
├── [12] SKILL.md (Output, triggers)         ✅
├── [13] P04-build.md (NEVER DEGRADE)        ✅
├── [14] quality-checklist.md (DNA)          ✅
└── [15] All footers → v8.0.0                ✅

PHASE 6: Validate (P05)
├── [16] self-diagnostic.sh                  ✅ 36/36
├── [17] validate-skill.sh                   ✅ VALID
├── [18] validate-naming.sh                  ✅ VALID
├── [19] audit-skill.sh                      ✅ 87% BP
├── [20] genetic-audit.sh                    ✅ 87%
└── [21] Regenerate MANIFEST.md              ✅

PHASE 7: Deliver (P06-P08)
├── [22] Package .skill                      ✅
├── [23] Create DIFF Report                  ✅
├── [24] P07 Scan                            ✅
└── [25] P08 Docs (8 files)                  ✅
```

---

## 6. Чат-верификация

### Из обсуждения согласовано:

| # | Тема | Решение |
|---|------|---------|
| 1 | Size 218KB проблема? | НЕТ, модульность ОК, лимит 250KB |
| 2 | Файлы > 300 строк | Модульная ## структура внутри файла |
| 3 | Кириллица 32/34 | Warning только ВНЕ code blocks |
| 4 | zip -r 13 раз | SSOT + примеры с "SSOT Note" |
| 5 | Best Practices 75% | Добавить ## Output + обновить скрипт |
| 6 | NEVER DEGRADE | Добавить checklist в P04-build |
| 7 | Genetic Audit | Новый протокол + скрипт |
| 8 | Testing files | Консолидация 8 → 4 |
| 9 | Объединить планы | В один релиз v8.0.0 |

**Verified: 9 items. Missing: none**

---

## 7. Риски

| Риск | Mitigation | Результат |
|------|------------|-----------|
| Потеря контента при merge | Diff review | ✅ Ничего не потеряно |
| Сломать ссылки | grep проверка | ✅ Все работают |
| Сломать скрипты | Тест после каждого изменения | ✅ Все pass |
| Слишком большие merged файлы | Модульная ## структура | ✅ Работает |

---

## 8. Результаты

| Метрика | v7.2.0 | v8.0.0 | Δ |
|---------|--------|--------|---|
| Files | 45 | 39 | -6 |
| Lines | ~9,200 | ~7,900 | -14% |
| Scripts | 7 | 8 | +1 |
| Self-diagnostic | 35/36 ❌ | 36/36 ✅ | Fixed |
| Best Practices | 75% | 87% | +12% |
| Genetic Inheritance | 58% | 87% | +29% |
| VT Score (estimated) | 65 | 75+ | +10 |

---

## 9. Deliverables

| Item | Status |
|------|--------|
| skill-architect-v8.0.0.skill | ✅ Delivered |
| skill-architect-v8.0.0-docs.zip | ✅ Delivered |
| DIFF Report | ✅ Delivered |

---

## 10. Lessons Learned

1. **Объединённый план нужен ДО начала работы** — создавать единый документ при merge планов
2. **Genetic Audit — полезная концепция** — стоит формализовать как стандартную практику
3. **Modular file structure** — эффективный паттерн для больших reference файлов
4. **"Eat your own dog food"** — критически важно для credibility

---

*UNIFIED-PLAN v1.0.0 | skill-architect v8.0.0*
