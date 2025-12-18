# Skill Tester — Концепция

**Версия:** Draft v0.1  
**Дата:** 2025-06-02  
**Назначение:** Всестороннее тестирование Claude Skills

---

## 1. Проблема

Скилы создаются, но не тестируются системно. В результате:
- Логические противоречия между секциями
- Неработающие edge cases
- Методики которые звучат хорошо, но не применимы
- Пробелы в покрытии user stories
- Инструкции которые Claude интерпретирует не так как задумано
- Конфликты между SKILL.md и reference файлами

**Нет инструмента** который бы:
1. Прогонял скил через батарею тестов
2. Находил слабые места
3. Симулировал реальное использование
4. Выдавал структурированный отчёт

---

## 2. Решение: Skill Tester

Скил-тестировщик который проводит **многоуровневый аудит** любого скила.

### Core Value
```
INPUT:  .skill файл или папка скила
OUTPUT: TEST_REPORT.md с находками + рекомендациями
```

---

## 3. Уровни тестирования

### Level 1: Structural Audit (статический анализ)

**Что проверяем:**
- [ ] Соответствие naming convention
- [ ] SKILL.md < 300 lines
- [ ] Frontmatter корректный (name, description, version)
- [ ] Все reference файлы существуют и ссылки валидны
- [ ] MANIFEST.md актуален
- [ ] README.md существует

**Выход:** Список structural issues

---

### Level 2: Logic Consistency (логический анализ)

**Что проверяем:**
- [ ] Противоречия между секциями SKILL.md
- [ ] Конфликты SKILL.md ↔ reference files
- [ ] Циклические зависимости в workflow
- [ ] Неопределённые термины (используется но не определено)
- [ ] Мёртвые ветки (условия которые никогда не выполнятся)
- [ ] Дублирование инструкций (одно и то же разными словами)

**Метод:** 
1. Парсинг всех файлов в единую модель
2. Поиск конфликтующих statements
3. Graph analysis для workflow

**Выход:** Список logic issues с severity

---

### Level 3: Coverage Analysis (покрытие)

**Что проверяем:**
- [ ] Все triggers покрыты инструкциями
- [ ] Все session types имеют protocol
- [ ] Все роли имеют описание когда активируются
- [ ] Есть handling для ошибок/edge cases
- [ ] Есть fallback для неизвестных ситуаций

**Метод:**
1. Извлечение всех заявленных capabilities
2. Проверка что каждая имеет implementation
3. Gap analysis

**Выход:** Coverage map + gaps list

---

### Level 4: Simulation Testing (симуляция использования)

**Что проверяем:**
- [ ] Скил работает на happy path
- [ ] Скил обрабатывает edge cases
- [ ] Скил не ломается на adversarial input
- [ ] Скил выдаёт consistent output format
- [ ] Скил использует заявленные tools правильно

**Метод:**
1. Генерация test cases из triggers + user stories
2. Симуляция диалога (Claude играет и user и skill)
3. Валидация output против expected format
4. Stress testing (длинные сессии, противоречивые запросы)

**Test Case Categories:**
- **Happy Path:** стандартное использование
- **Edge Cases:** граничные условия
- **Error Handling:** некорректный input
- **Adversarial:** попытки "сломать" скил
- **Long Session:** устойчивость на длинных диалогах

**Выход:** Test results с pass/fail + observations

---

### Level 5: Methodology Viability (применимость методик)

**Что проверяем:**
- [ ] Методики реалистичны для выполнения
- [ ] Шаги достижимы с заявленными ресурсами
- [ ] Нет "магических" переходов (A → ??? → B)
- [ ] Временные оценки адекватны
- [ ] Dependencies между шагами корректны

**Метод:**
1. Извлечение всех workflows/protocols
2. Анализ каждого шага на feasibility
3. Проверка transitions между шагами
4. Sanity check на реалистичность

**Выход:** Methodology audit с red flags

---

### Level 6: Claude Interpretation Test

**Что проверяем:**
- [ ] Claude понимает инструкции однозначно
- [ ] Нет ambiguous формулировок
- [ ] Приоритеты понятны при конфликтах
- [ ] Скил не конфликтует с base Claude behavior

**Метод:**
1. Попросить Claude пересказать скил своими словами
2. Сравнить интерпретацию с intent
3. Найти расхождения

**Выход:** Interpretation gaps

---

## 4. Output: TEST_REPORT.md

```markdown
# Skill Test Report

**Skill:** [name] v[version]
**Tested:** [date]
**Tester:** Skill Tester v[X]

---

## Executive Summary

| Level | Status | Issues |
|-------|--------|--------|
| Structural | ✅/⚠️/❌ | N |
| Logic | ✅/⚠️/❌ | N |
| Coverage | ✅/⚠️/❌ | N |
| Simulation | ✅/⚠️/❌ | N |
| Methodology | ✅/⚠️/❌ | N |
| Interpretation | ✅/⚠️/❌ | N |

**Overall:** PASS / PASS WITH WARNINGS / FAIL

---

## Critical Issues (must fix)

### [ISSUE-001] [Title]
- **Level:** [which level found]
- **Location:** [file:line or section]
- **Problem:** [description]
- **Impact:** [what breaks]
- **Fix:** [recommendation]

---

## Warnings (should fix)

### [WARN-001] [Title]
[same structure]

---

## Observations (nice to fix)

### [OBS-001] [Title]
[same structure]

---

## Test Cases Results

| ID | Category | Input | Expected | Actual | Status |
|----|----------|-------|----------|--------|--------|
| TC-001 | Happy Path | "trigger X" | [output] | [output] | ✅ |
| TC-002 | Edge Case | "weird input" | [handling] | [actual] | ⚠️ |

---

## Recommendations

### Priority 1 (Critical)
1. [Action]
2. [Action]

### Priority 2 (Important)
1. [Action]

### Priority 3 (Nice to have)
1. [Action]

---

## Appendix

### A. Full Test Log
[detailed simulation transcripts]

### B. Structural Analysis
[full file analysis]

### C. Coverage Map
[visual or table]
```

---

## 5. Workflow

```
USER: "тестируй скил" + attachment (.skill или folder)

SKILL TESTER:
1. Unpack если .skill
2. Level 1: Structural Audit
3. Level 2: Logic Consistency  
4. Level 3: Coverage Analysis
5. Level 4: Simulation Testing
6. Level 5: Methodology Viability
7. Level 6: Interpretation Test
8. Generate TEST_REPORT.md
9. Deliver report + summary

USER: получает отчёт, фиксит, повторяет
```

---

## 6. Triggers

- `тестируй скил` + attachment
- `test skill` + attachment
- `аудит скила`
- `skill audit`
- `проверь скил`
- `validate skill`

---

## 7. Integration

```
@uses: file operations (unpack, read)
@uses: web_search (для проверки best practices если нужно)

@integrates: skill-architect
  → После теста можно сразу в refactor

@output: TEST_REPORT.md
  → Формат понятный skill-architect для исправлений
```

---

## 8. Unique Value

**Почему это нужно:**

1. **Объективность** — тестирование по чеклисту, не "кажется норм"
2. **Полнота** — 6 уровней покрывают разные типы проблем
3. **Симуляция** — не просто читаем, а пробуем использовать
4. **Actionable output** — отчёт с конкретными фиксами
5. **Repeatability** — можно прогонять после каждого изменения

**Чего нет у ручного ревью:**
- Систематичность
- Симуляция edge cases
- Проверка интерпретации Claude
- Структурированный отчёт

---

## 9. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Слишком долгий тест | Можно выбрать уровни: quick (1-3), full (1-6) |
| False positives | Severity levels + human review |
| Не все проблемы находятся | Честно заявляем limitations |
| Симуляция не = реальность | Disclaimer + рекомендация live testing |

---

## 10. Version Roadmap

### v1.0.0
- 6 уровней тестирования
- TEST_REPORT.md output
- Basic simulation (5-10 test cases)

### v1.1.0
- Custom test cases от пользователя
- Comparison mode (v1 vs v2)
- Integration с skill-architect

### v2.0.0
- Regression testing (сохранение baseline)
- Automated fix suggestions
- CI/CD integration concept

---

## 11. Open Questions

1. **Глубина симуляции** — сколько test cases генерировать?
2. **Self-testing** — может ли skill-tester тестировать сам себя?
3. **Benchmarks** — нужна ли база "хороших" скилов для сравнения?
4. **Partial testing** — можно ли тестировать только изменения?

---

## 12. Next Steps

1. ✅ Концепция (этот документ)
2. ⏳ Feedback + доработка
3. ⏳ Planning Document (Skill Architect format)
4. ⏳ Build v1.0.0
5. ⏳ Self-test на virtual-team
6. ⏳ Iterate

---

*Draft concept — Skill Tester*
*Ready for review and expansion*
