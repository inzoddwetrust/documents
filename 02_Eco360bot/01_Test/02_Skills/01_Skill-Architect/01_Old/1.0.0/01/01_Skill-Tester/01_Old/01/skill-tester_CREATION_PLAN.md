# skill-tester: План создания v1.0.0

**Дата:** 2025-06-02  
**Источник:** skill-tester-concept.md (Draft v0.1)

---

## 1. Контекст

Скилы создаются, но не тестируются системно. Нет инструмента для:
- Прогона скила через батарею тестов
- Поиска слабых мест
- Симуляции реального использования
- Структурированного отчёта

**Решение:** Skill Tester — 6-уровневый аудит любого скила.

---

## 2. Core Value

```
INPUT:  .skill файл или папка скила
OUTPUT: TEST_REPORT.md с находками + рекомендациями
```

---

## 3. План создания

### Создаём

| Файл | Назначение | Строк (≈) |
|------|------------|-----------|
| SKILL.md | Core protocol (EN) | ~250 |
| README.md | User docs (RU) | ~150 |
| MANIFEST.md | Integrity tracking | ~40 |
| reference/test-levels.md | L1-L6 детали | ~200 |
| reference/report-template.md | TEST_REPORT структура | ~100 |
| reference/test-cases.md | Генерация тестов | ~120 |
| scripts/unpack-skill.sh | Распаковка .skill | ~20 |

### Mapping: Концепт → Скил

| Секция концепта | Куда идёт |
|-----------------|-----------|
| §3 Уровни тестирования | reference/test-levels.md |
| §4 Output: TEST_REPORT | reference/report-template.md |
| §5 Workflow | SKILL.md (Process) |
| §6 Triggers | SKILL.md (frontmatter + Activation) |
| §7 Integration | SKILL.md (Integration) |
| §8-9 Value, Risks | README.md |
| §10 Roadmap | README.md (Future) |
| §11 Open Questions | README.md (Limitations) |

---

## 4. Структура скила

```
skill-tester/
├── SKILL.md              # EN, < 300 lines
├── README.md             # RU
├── MANIFEST.md           
├── reference/
│   ├── test-levels.md         # L1-L6 полные спецификации
│   ├── report-template.md     # TEST_REPORT.md шаблон
│   └── test-cases.md          # Категории и генерация тестов
└── scripts/
    └── unpack-skill.sh        # Распаковка .skill архива
```

---

## 5. SKILL.md Preview

### Frontmatter
```yaml
---
name: skill-tester
description: "v1.0.0 | 6-level skill testing and audit. Triggers: test skill, тестируй скил, audit, validate."
---
```

### Sections
| Секция | Содержание |
|--------|------------|
| Mandatory: Reference Reading | Какие файлы читать |
| When to Use | Когда активировать |
| Process | 6-step workflow |
| Test Modes | Quick (L1-3) vs Full (L1-6) |
| Output | TEST_REPORT.md |
| Integration | skill-architect |
| Context Tracking | Token counter |

---

## 6. Test Levels Summary

| Level | Name | Type | Что проверяет |
|-------|------|------|---------------|
| L1 | Structural Audit | Static | Файлы, naming, frontmatter |
| L2 | Logic Consistency | Static | Противоречия, конфликты |
| L3 | Coverage Analysis | Static | Gaps в покрытии |
| L4 | Simulation Testing | Dynamic | Happy path, edge cases |
| L5 | Methodology Viability | Analysis | Реалистичность методик |
| L6 | Interpretation Test | Analysis | Как Claude понимает |

---

## 7. Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Russian |
| Frontmatter | name + description (version in description) |
| Confirmation | explicit "да/yes/go" |

---

## 8. Риски

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| SKILL.md > 300 lines | Medium | Всё детальное → reference/ |
| Симуляция неточная | Medium | Disclaimer в отчёте |
| Долгий Full mode | Low | Quick mode по умолчанию |
| False positives | Medium | Severity levels + human review |

---

## 9. Out of Scope (v1.0.0)

- Custom test cases от пользователя
- Comparison mode (v1 vs v2)
- Regression testing
- Automated fix suggestions

→ Запланировано на v1.1.0+

---

## 10. Чеклист подтверждения

- [ ] Структура понятна
- [ ] 6 уровней сохранены из концепта
- [ ] Mapping концепт → файлы корректен
- [ ] Constraints приемлемы
- [ ] Out of scope согласован
- [ ] Можно начинать build

---

**Ожидаю подтверждение для старта**

---

*Planning Document | skill-tester v1.0.0*
