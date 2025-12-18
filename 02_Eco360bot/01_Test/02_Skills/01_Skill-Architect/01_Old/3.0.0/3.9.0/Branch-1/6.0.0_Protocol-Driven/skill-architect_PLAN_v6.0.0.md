# skill-architect: План обновления v5.4.0 → v6.0.0 "Protocol-Driven"
## 2025-12-02 | Major architectural refactor

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | User's language |
| Frontmatter | name + description + version |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

**Триггер:** В процессе v5.4.0 выявлено системное нарушение протоколов:
- Не прочитал docs-packaging.md перед созданием доков
- Предложил v6.0.0 без Planning Document
- Пропустил Reference Reading триггер

**Причина:** Протоколы фрагментированы, нет явного flow, легко пропустить шаг.

**Решение:** Protocol-Driven Architecture — все действия через явные протоколы с BLOCKING точками.

---

## 2. Проблемы / Задачи

| # | Проблема | Влияние |
|---|----------|---------|
| 1 | Протоколы разбросаны по SKILL.md | Легко пропустить |
| 2 | Нет явного flow между шагами | Непонятно что дальше |
| 3 | Reference Reading таблица неполная | Не все триггеры покрыты |
| 4 | Delivery не ссылается на docs-packaging | Доки делаются неправильно |
| 5 | Нет BLOCKING enforcement | Можно пропустить шаг |

---

## 3. План изменений

### Добавляем

| Что | Зачем | Где |
|-----|-------|-----|
| reference/protocols/ папка | Организация протоколов | reference/ |
| P01-activation.md | Старт сессии | protocols/ |
| P02-config.md | Сбор требований | protocols/ |
| P03-planning.md | Создание плана (BLOCKING) | protocols/ |
| P04-build.md | Реализация | protocols/ |
| P05-validate.md | Проверки | protocols/ |
| P06-delivery-skill.md | Выдача .skill (BLOCKING) | protocols/ |
| P07-delivery-docs.md | Выдача docs (BLOCKING) | protocols/ |
| P08-scan.md | Финальный скан | protocols/ |
| Protocol Router в SKILL.md | Диспетчер протоколов | SKILL.md |

### Изменяем

| Что | Было | Станет | Зачем |
|-----|------|--------|-------|
| SKILL.md структура | Монолит с секциями | Router + ссылки на протоколы | Чёткий flow |
| Reference Reading | Таблица триггеров | Автоматический dispatch | Нельзя пропустить |
| planning-document.md | Отдельный reference | Часть P03-planning.md | Консолидация |
| docs-packaging.md | Отдельный reference | Часть P07-delivery-docs.md | Консолидация |

### Удаляем

| Что | Почему безопасно удалить |
|-----|--------------------------|
| Inline протоколы из SKILL.md | Переносятся в protocols/ |
| Дублирующие секции | Консолидируются в протоколы |

### Не трогаем

- NEVER DEGRADE (остаётся в SKILL.md как guard)
- Clean Skill Principles
- Critical Rules
- Все scripts/
- Project Mode reference files
- engines.md, templates.md (domain knowledge)

---

## 4. Было → Стало (Preview)

### SKILL.md

| Секция | v5.4.0 | v6.0.0 |
|--------|--------|--------|
| NEVER DEGRADE | ✓ | ✓ (unchanged) |
| Skill Dependencies | ✓ | ✓ (unchanged) |
| Reference Reading | Таблица | → Protocol Router |
| Context Tracking | ✓ | ✓ (unchanged) |
| Quick Start | ✓ | ✓ (simplified) |
| Activation | Inline | → P01 |
| Config | Inline | → P02 |
| Planning Document | Inline | → P03 |
| PRE-BUILD | Inline | → P04 |
| REFACTOR Protocol | Inline | → P04 |
| UPDATE Protocol | Inline | → P04 |
| Delivery Protocol | Inline | → P06, P07 |
| Diff Report | Inline | → P05 |
| Clean Skill Principles | ✓ | ✓ (unchanged) |
| Required Files | ✓ | ✓ (unchanged) |
| Critical Rules | ✓ | ✓ (unchanged) |
| Versioning | ✓ | ✓ (unchanged) |
| Resources | ✓ | Updated |

**Ожидаемо:** SKILL.md ~150-180 lines (сейчас 293)

### Структура файлов

**До (v5.4.0):**
```
skill-architect/
├── SKILL.md (293 lines)
├── README.md
├── MANIFEST.md
├── reference/ (15 files)
│   ├── planning-document.md
│   ├── docs-packaging.md
│   └── ... 
└── scripts/ (7 files)
```

**После (v6.0.0):**
```
skill-architect/
├── SKILL.md (~170 lines)
├── README.md
├── MANIFEST.md
├── reference/ (21+ files)
│   ├── protocols/
│   │   ├── P01-activation.md
│   │   ├── P02-config.md
│   │   ├── P03-planning.md
│   │   ├── P04-build.md
│   │   ├── P05-validate.md
│   │   ├── P06-delivery-skill.md
│   │   ├── P07-delivery-docs.md
│   │   └── P08-scan.md
│   ├── planning-document.md (deprecated → P03)
│   ├── docs-packaging.md (deprecated → P07)
│   └── ...
└── scripts/ (7 files)
```

---

## 5. Риски

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| Слишком много файлов | Medium | protocols/ подпапка |
| Потеря контекста при переходах | Medium | Next/Prev в каждом протоколе |
| SKILL.md станет слишком абстрактным | Low | Сохраняем Quick Start, Critical Rules |
| Breaking change для пользователей | Low | README обновление, миграция |

---

## 6. Чат-верификация

| # | Обсуждённый пункт | Включён в план? |
|---|-------------------|-----------------|
| 1 | Не прочитал docs-packaging.md | ✅ → P07 |
| 2 | Предложил v6.0.0 без плана | ✅ → P03 BLOCKING |
| 3 | Protocol-Driven Architecture идея | ✅ → Core concept |
| 4 | Каждый протокол: Trigger, Prerequisites, Steps, Checklist, Output, Next | ✅ → Protocol template |
| 5 | SKILL.md как роутер | ✅ → Protocol Router |
| 6 | Вопрос "почему не спросил?" | ✅ → BLOCKING enforcement |

**Verified: 6 items. Missing: none**

---

## 7. Чеклист подтверждения

- [ ] План понятен
- [ ] Protocol-Driven Architecture подход согласован
- [ ] Структура protocols/ согласована
- [ ] Риски приемлемы
- [ ] Можно начинать

**Ожидаю подтверждение: "да", "yes", "go", "делай"**

---

*Planning Document v6.0.0 | skill-architect*
