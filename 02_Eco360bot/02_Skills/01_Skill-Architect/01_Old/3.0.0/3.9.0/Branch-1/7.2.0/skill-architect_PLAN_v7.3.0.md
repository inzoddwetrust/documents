# skill-architect: План v7.2.0 → v7.3.0

## Дата: 2025-12-07 | Контекст: Полный рефакторинг после Self-Audit

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Russian (user's language) |
| Frontmatter | name + description + version |
| Confirmation | explicit "да/yes/go" |
| NEVER DEGRADE | Применяется |

---

## 1. Контекст

Провели полный аудит skill-architect v7.2.0:
- **Фаза 0:** Genetic Audit — 58% наследование генов
- **Фаза 1:** Self-Diagnostic — 35/36 (FAIL из-за битой ссылки)
- **Фаза 2:** Validation — MANIFEST устарел, false positives в скриптах
- **Фаза 3:** Virtual Testing — Score 65/100

**Главный вывод:** skill-architect не следует собственным стандартам в нескольких местах.

---

## 2. Проблемы / Задачи

### 🔴 CRITICAL (блокируют)

| # | Проблема | Файл | Описание |
|---|----------|------|----------|
| C1 | Битая ссылка P07→P08 | scripts/self-diagnostic.sh:164 | Ищет P07-delivery-docs.md вместо P07-scan.md |
| C2 | MANIFEST не sync | MANIFEST.md | Не отражает v7.2.0 "Docs Reorder" (P07↔P08 swap) |

### 🟡 SERIOUS (должны исправить)

| # | Проблема | Файл | Описание |
|---|----------|------|----------|
| S1 | NEVER DEGRADE без enforcement | reference/protocols/P04-build.md | Нет checklist проверки |
| S2 | Нет ## Output в SKILL.md | SKILL.md | audit-skill.sh не находит outputs |
| S3 | Правила размеров устарели | reference/quality-checklist.md | Нужно: модульная структура, 500 для reference |
| S4 | Кириллица — false positive | scripts/audit-skill.sh | Ругается на примеры в code blocks |
| S5 | SSOT без пометок | reference/packaging.md, workflow.md | Нет "SSOT Note" у примеров команд |

### 🟢 ДНК (передать детям)

| # | Что | Куда |
|---|-----|------|
| G1 | Модульная структура файлов (## sections) | quality-checklist.md |
| G2 | Правило размеров (SKILL.md < 300, reference < 500 с ##) | quality-checklist.md, packaging.md |
| G3 | SSOT Note паттерн | quality-checklist.md |

---

## 3. План изменений

### ✅ Добавляем

| Файл | Что добавляем |
|------|---------------|
| SKILL.md | `## Output` секция (краткая, ссылка на протоколы) |
| P04-build.md | NEVER DEGRADE checklist (4 пункта) |
| quality-checklist.md | Модульная структура файлов (## sections rule) |
| quality-checklist.md | Обновлённые правила размеров |
| quality-checklist.md | SSOT Note паттерн |
| packaging.md | "SSOT Note" к примерам команд |
| workflow.md | "SSOT Note" к примерам команд |

### ✏️ Изменяем

| Файл | Что меняем |
|------|------------|
| scripts/self-diagnostic.sh:164 | P07-delivery-docs.md → P07-scan.md |
| scripts/audit-skill.sh | Смягчить проверку кириллицы (игнорировать code blocks) |
| scripts/ssot-check.sh | Не ругаться на файлы с "SSOT Note" |
| MANIFEST.md | Регенерировать полностью |
| SKILL.md description | v7.2.0 → v7.3.0 |
| Все footers | v7.2.0 → v7.3.0 (в изменённых файлах) |

### ❌ Удаляем

| Что | Почему |
|-----|--------|
| Ничего | NEVER DEGRADE — не удаляем функционал |

### 🔒 Не трогаем

| Файлы | Причина |
|-------|---------|
| P00-router.md | Работает корректно |
| P01-activation.md | Работает корректно |
| P02-config.md | Работает корректно |
| P03-planning.md | Работает корректно |
| P05-validate.md | Работает корректно |
| P06-delivery-skill.md | Работает корректно |
| P07-scan.md | Работает корректно |
| P08-docs-closure.md | Работает корректно |
| reference/engines.md | Структура ОК (## модули) |
| reference/templates.md | Структура ОК (## модули) |
| reference/virtual-testing.md | Работает корректно |
| reference/test-levels.md | Работает корректно |
| reference/personas.md | Работает корректно |
| reference/adversarial.md | Работает корректно |
| reference/expert-panel.md | Работает корректно |
| scripts/validate-skill.sh | Работает корректно |
| scripts/validate-naming.sh | Работает корректно |
| scripts/generate-manifest.sh | Работает корректно |

---

## 4. Было → Стало

### SKILL.md

```
БЫЛО (169 строк):
- Нет ## Output секции

СТАЛО (~175 строк):
+ ## Output секция (таблица deliverables)
+ description: v7.3.0
```

### P04-build.md

```
БЫЛО:
- Нет NEVER DEGRADE enforcement

СТАЛО:
+ ## Pre-Build Checklist
  □ Does ANY change REMOVE working functionality? → STOP
  □ Does ANY change make instructions LESS specific? → STOP
  □ If removing content, is it moved to reference/? → Required
  □ New features ADD alongside, not replace? → Required
```

### quality-checklist.md

```
БЫЛО:
- Size: < 100KB (ideal: < 50KB)
- Нет правил модульной структуры

СТАЛО:
+ ## File Size Rules
  - SKILL.md: < 300 строк (hard limit)
  - reference/*.md: < 500 строк с ## модульной структурой
  - Total: < 250KB (с модульной архитектурой)
  
+ ## Modular File Structure
  - Файл > 300 строк? → Обязательна ## секционная структура
  - Claude читает нужную секцию, не весь файл
  
+ ## SSOT Note Pattern
  - Примеры команд вне commands.md → добавить "SSOT Note"
```

### scripts/self-diagnostic.sh

```
БЫЛО (строка 164):
check "$(grep -q 'P08' "$PROTOCOLS/P07-delivery-docs.md" ...

СТАЛО:
check "$(grep -q 'P08' "$PROTOCOLS/P07-scan.md" ...
```

### scripts/audit-skill.sh

```
БЫЛО:
- Любая кириллица = warning

СТАЛО:
- Кириллица ВНЕ code blocks = warning
- Кириллица В code blocks/примерах = OK
```

---

## 5. Риски

| Риск | Вероятность | Impact | Mitigation |
|------|-------------|--------|------------|
| Сломать self-diagnostic | Low | High | Тест после патча |
| Сломать audit-skill | Medium | Medium | Тест на skill-architect |
| Пропустить файл при обновлении footer | Medium | Low | grep проверка |
| MANIFEST рассинхрон | Low | Medium | generate-manifest.sh |

---

## 6. Чат-верификация

### Обсуждённые и согласованные пункты:

| # | Тема | Решение | Статус |
|---|------|---------|--------|
| 1 | Size 218KB — проблема? | НЕТ, модульность ОК, лимит 250KB | ✅ Согласовано |
| 2 | 4 файла > 300 строк | Вариант C: модульная ## структура внутри файла | ✅ Согласовано |
| 3 | Кириллица 32/34 файлов | Смягчить: warning только ВНЕ code blocks | ✅ Согласовано |
| 4 | zip -r 13 раз | Вариант B: SSOT + примеры с "SSOT Note" | ✅ Согласовано |
| 5 | Best Practices 75% | Вариант A+B: добавить ## Output + обновить скрипт | ✅ Согласовано |
| 6 | NEVER DEGRADE enforcement | Добавить checklist в P04-build | ✅ Согласовано |
| 7 | Genetic Audit gaps | Передать правила детям через quality-checklist | ✅ Согласовано |
| 8 | Модульная структура = ДНК | ДА, передаём детям | ✅ Согласовано |

**Verified: 8 items. Missing: none**

---

## 7. Порядок выполнения

```
PHASE 1: Critical Fixes
├── [1] Patch self-diagnostic.sh:164
├── [2] Regenerate MANIFEST.md
└── [3] Test self-diagnostic

PHASE 2: SKILL.md & Protocols
├── [4] Add ## Output to SKILL.md
├── [5] Add NEVER DEGRADE checklist to P04-build.md
└── [6] Update description version

PHASE 3: Quality & Rules
├── [7] Update quality-checklist.md (sizes, modular, SSOT Note)
├── [8] Add "SSOT Note" to packaging.md
└── [9] Add "SSOT Note" to workflow.md

PHASE 4: Scripts
├── [10] Update audit-skill.sh (Cyrillic check)
└── [11] Update ssot-check.sh (SSOT Note aware)

PHASE 5: Finalize
├── [12] Update all footers → v7.3.0
├── [13] Final MANIFEST regeneration
├── [14] Run full self-diagnostic
└── [15] Verify all tests pass
```

---

## 8. Чеклист подтверждения

- [ ] План понятен
- [ ] Изменения согласованы
- [ ] Риски приемлемы
- [ ] Порядок выполнения логичен
- [ ] Можно начинать

---

## ⛔ Ожидаю подтверждение

**Для начала рефакторинга скажи:** "да", "yes", "go", "делай"

---

```
skill-architect: P03-planning complete → WAITING confirmation
```
🟢 ~120k | ~5k 🟡
