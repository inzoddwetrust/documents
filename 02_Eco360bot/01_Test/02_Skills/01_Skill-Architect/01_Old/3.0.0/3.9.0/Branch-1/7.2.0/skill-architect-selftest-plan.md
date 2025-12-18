# План работ: Комплексное тестирование skill-architect v7.2.0

**Дата:** 2025-12-07  
**Цель:** Genetic Audit + Виртуальное тестирование + Самодиагностика + Полная валидация + Анализ на рефакторинг

---

## Архитектура тестирования skill-architect

```
                    ┌─────────────────────────────┐
                    │  0. GENETIC AUDIT           │
                    │     "Eat your own dog food" │
                    │     Свои гены → детям?      │
                    └───────────┬─────────────────┘
                                ↓
                    ┌─────────────────────────────┐
                    │  1. САМОДИАГНОСТИКА         │
                    │     self-diagnostic.sh      │
                    │     self-diagnostic.md      │
                    └───────────┬─────────────────┘
                                ↓
                    ┌─────────────────────────────┐
                    │  2. ПОЛНАЯ ВАЛИДАЦИЯ        │
                    │     validate-skill.sh       │
                    │     audit-skill.sh          │
                    │     ssot-check.sh           │
                    │     validate-naming.sh      │
                    │     validate-docs.sh        │
                    └───────────┬─────────────────┘
                                ↓
                    ┌─────────────────────────────┐
                    │  3. ВИРТУАЛЬНОЕ ТЕСТИРОВАНИЕ│
                    │     virtual-testing.md      │
                    │     test-levels.md (L1-L6)  │
                    │     personas.md             │
                    │     adversarial.md          │
                    │     expert-panel.md         │
                    └───────────┬─────────────────┘
                                ↓
                    ┌─────────────────────────────┐
                    │  4. АНАЛИЗ НА РЕФАКТОРИНГ   │
                    │     Выводы и рекомендации   │
                    └─────────────────────────────┘
```

---

## Фаза 0: Genetic Audit (НОВАЯ)

**Философия:** "Eat your own dog food" — делает ли skill-architect сам то, что требует от своих "детей"?

### Цель
Сверить принципы и механизмы skill-architect с требованиями, которые он закладывает в создаваемые скиллы.

### Источники "генов родителя" (skill-architect):

| Файл | Что извлекаем |
|------|---------------|
| SKILL.md | Архитектурные принципы (NEVER DEGRADE, FIRST STEP, Context Tracking) |
| P00-router.md | Blocking points, State machine |
| clean-protocol | Token counter, Response style, Forbidden patterns |
| self-diagnostic.md | Структурные требования |
| Все protocols/ | Workflow patterns |

### Источники "генов детей" (создаваемые скиллы):

| Файл | Что извлекаем |
|------|---------------|
| quality-checklist.md | 6-Dimensional Quality Model, Best Practices, Anti-patterns |
| templates.md | Шаблоны SKILL.md для детей |
| packaging.md | Требования к упаковке |
| evaluations.md | Критерии успеха |

### Матрица наследования

```
┌────────────────────────────────────────────────────────────────┐
│                    GENETIC INHERITANCE MATRIX                   │
├─────────────────────────┬──────────────┬──────────────┬────────┤
│ Принцип родителя        │ Передаётся?  │ Где?         │ Gap?   │
├─────────────────────────┼──────────────┼──────────────┼────────┤
│ SKILL.md < 300 lines    │ ✅/❌        │ quality-*.md │        │
│ Frontmatter + version   │ ✅/❌        │ quality-*.md │        │
│ README.md обязателен    │ ✅/❌        │ quality-*.md │        │
│ Progressive disclosure  │ ✅/❌        │ quality-*.md │        │
│ SSOT (Single Source)    │ ✅/❌        │ ?            │        │
│ NEVER DEGRADE           │ ✅/❌        │ ?            │        │
│ Protocol-First          │ ✅/❌        │ ?            │        │
│ Blocking points (⛔)    │ ✅/❌        │ ?            │        │
│ Context tracking (🟢🟡) │ ✅/❌        │ ?            │        │
│ Token counter           │ ✅/❌        │ ?            │        │
│ Forbidden phrases       │ ✅/❌        │ ?            │        │
│ kebab-case naming       │ ✅/❌        │ ?            │        │
│ English SKILL.md        │ ✅/❌        │ ?            │        │
│ MANIFEST.md             │ ✅/❌        │ ?            │        │
└─────────────────────────┴──────────────┴──────────────┴────────┘
```

### Типы генов

**1. Универсальные гены** — должны передаваться всем детям:
- Структурные требования (файлы, размеры, naming)
- Quality gates (валидация перед деливери)
- Best practices документации

**2. Специализированные гены** — только для сложных скиллов:
- Protocol-First архитектура
- Blocking points
- State machine

**3. Внутренние гены** — только для skill-architect:
- NEVER DEGRADE (защита от деградации при апдейтах)
- Self-diagnostic
- Context recovery после web search

### Вопросы для сверки

1. **Потерянные гены:** Какие принципы я использую, но НЕ документирую для детей?
2. **Мутации:** Где требования к детям ОТЛИЧАЮТСЯ от моих собственных практик?
3. **Рецессивные гены:** Какие принципы задокументированы, но НЕ применяются?
4. **Обоснование различий:** Почему некоторые гены не передаются? (если это осознанно)

### Deliverable Фазы 0

```markdown
═══════════════════════════════════════
GENETIC AUDIT REPORT
═══════════════════════════════════════

Extracted parent genes: [N]
Documented child requirements: [M]

INHERITANCE STATUS
──────────────────
✅ Inherited: [list]
❌ Lost genes: [list]  
⚠️ Mutations: [list]
📋 Justified gaps: [list]

RECOMMENDATIONS
───────────────
1. [Add to quality-checklist]
2. [Add to templates]
3. [Document why not inherited]

═══════════════════════════════════════
```

---

## Фаза 1: Самодиагностика (Quick Check)

**Скрипт:** `scripts/self-diagnostic.sh`  
**Протокол:** `reference/self-diagnostic.md`

### Что проверяется:
| Компонент | Ожидание | Проверка |
|-----------|----------|----------|
| SKILL.md | < 300 строк | wc -l |
| README.md | существует | -f |
| MANIFEST.md | существует | -f |
| protocols/ | 9 файлов (P00-P08) | ls \| wc -l |
| scripts/ | ≥ 6 файлов | ls \| wc -l |
| commands.md | существует (SSOT) | -f |

### Целостность протоколов:
- Каждый P0X должен иметь: `## Trigger`, `## Steps`, версию в footer
- P00-router: `Decision Table`, `Blocking Points`

### SKILL.md как роутер:
- ✓ NEVER DEGRADE
- ✓ FIRST STEP — MANDATORY
- ✓ Context Tracking
- ✓ Protocol Router
- ✓ Quick Start
- ✓ Resources

### SSOT Compliance:
- Команды только в `commands.md`
- Блокирующие правила только в `P00-router.md`

---

## Фаза 2: Полная валидация

**Скрипты:**
1. `validate-skill.sh` — структура, frontmatter, язык
2. `audit-skill.sh` — размер, дубликаты, best practices
3. `ssot-check.sh` — единый источник истины
4. `validate-naming.sh` — kebab-case
5. `validate-docs.sh` — структура документации

### Test Levels (L1-L6):

| Level | Название | Тип | Что проверяет |
|-------|----------|-----|---------------|
| L1 | Structural | Static | Файлы, naming, frontmatter |
| L2 | Logic | Static | Противоречия, undefined terms |
| L3 | Coverage | Static | Trigger → handler map, gaps |
| L4 | Simulation | Dynamic | Happy path, edge cases, errors |
| L5 | Methodology | Analysis | Feasibility, red flags |
| L6 | Interpretation | Analysis | Ambiguities, priority conflicts |

---

## Фаза 3: Виртуальное тестирование (VT)

**Протокол:** `reference/virtual-testing.md`

### Архитектура VT:
```
INPUT (skill-architect)
       ↓
1. CONTEXT DETECTOR → type = "skill"
       ↓
2. PERSONA GENERATOR → 5-7 синтетических юзеров
       ↓
3. ADVERSARIAL LAYER → атаки на гипотезы
       ↓
4. EXPERT PANEL → 5 перспектив
       ↓
5. SCORING → гипотезы для валидации
```

### Персоны для тестирования:
| Персона | Experience | Skepticism | Фокус |
|---------|------------|------------|-------|
| Новичок | novice | low | "Могу ли я вообще это использовать?" |
| Разработчик | intermediate | medium | "Подойдёт ли для моих задач?" |
| Архитектор | expert | high | "Масштабируется ли это?" |
| Скептик | intermediate | high | "Где тут подвох?" |
| Edge-case юзер | mixed | medium | "Что если я сделаю X?" |

### Adversarial Framework:
```
HYPOTHESIS: [утверждение из скилла]
ATTACK: "Почему это НЕ сработает?"
├─ Feasibility: Claude это может?
├─ Clarity: Однозначно?
├─ Edge cases: Что ломает?
├─ Dependencies: Что не хватает?
└─ Conflicts: Что противоречит?

PROBABILITY × IMPACT → Risk Matrix
```

### Expert Panel:
| Эксперт | Вопрос |
|---------|--------|
| User | "Могу ли я это использовать?" |
| Maintainer | "Можно ли это поддерживать?" |
| Skeptic | "Как это сломается?" |
| Integrator | "Вписывается в экосистему?" |
| Novice | "Понятно ли мне это?" |

---

## Фаза 4: Анализ на рефакторинг

### Критерии для рефакторинга:
1. **Size** — файлы > 300 строк
2. **Duplication** — повторяющийся контент
3. **SSOT violations** — команды вне commands.md
4. **Dead code** — неиспользуемые файлы
5. **Protocol flow** — битые связи P0X → P0Y
6. **Best practices score** — < 80%

### Deliverable:
- Отчёт с найденными проблемами
- Конкретные рекомендации
- При необходимости — патчи для рефакторинга

---

## Порядок выполнения

```
ФАЗА 0: GENETIC AUDIT
[ ] 0.1. Извлечь гены родителя (SKILL.md, protocols, clean-protocol)
[ ] 0.2. Извлечь требования к детям (quality-checklist, templates)
[ ] 0.3. Построить Inheritance Matrix
[ ] 0.4. Найти потерянные гены и мутации
[ ] 0.5. Сформировать Genetic Audit Report

ФАЗА 1: САМОДИАГНОСТИКА
[ ] 1.1. Запуск self-diagnostic.sh
[ ] 1.2. Анализ результатов

ФАЗА 2: ПОЛНАЯ ВАЛИДАЦИЯ
[ ] 2.1. Запуск validate-skill.sh
[ ] 2.2. Запуск audit-skill.sh
[ ] 2.3. Запуск ssot-check.sh
[ ] 2.4. Запуск validate-naming.sh
[ ] 2.5. Ручной L1-L6 анализ

ФАЗА 3: ВИРТУАЛЬНОЕ ТЕСТИРОВАНИЕ
[ ] 3.1. Генерация персон (VT)
[ ] 3.2. Adversarial тестирование (VT)
[ ] 3.3. Expert Panel оценка (VT)
[ ] 3.4. VT Report

ФАЗА 4: АНАЛИЗ И РЕФАКТОРИНГ
[ ] 4.1. Сводный отчёт всех фаз
[ ] 4.2. Список проблем с приоритетами
[ ] 4.3. Рекомендации по рефакторингу
[ ] 4.4. Патчи (если нужны)
```

---

**Готов к старту после подтверждения.**

```
skill-architect: file_read → P00-router.md, SKILL.md, self-diagnostic.md, virtual-testing.md, test-levels.md
```
🟢 ~195k | ~5k 🟡
