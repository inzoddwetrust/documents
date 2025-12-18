# Skill Architect: План обновления v3.7.1 → v3.8.0
## Концепция: Planning Document First | 2025-11-27

---

## Мета: Что это за документ

Это документ самообновления skill-architect. Он демонстрирует новую концепцию, которую мы внедряем: **Planning Document First** — никаких изменений без предварительного документа-плана.

Этот документ одновременно:
- План того, что будет изменено
- Контракт (изменения начинаются только после подтверждения)
- История (было → стало)
- Лог для будущих версий

---

## Часть 1: Проблема

### Текущее поведение skill-architect

Сейчас при запросе "обнови скил" происходит следующее:
1. Snapshot (копия оригинала)
2. Анализ
3. **Сразу изменения**
4. Diff Report (постфактум)
5. Подтверждение (когда уже поздно)

### Что не так

**Проблема 1: Diff Report приходит ПОСЛЕ изменений**

Пользователь видит "что изменилось" когда файлы уже переписаны. Если что-то не так — нужно откатывать или переделывать. Это неэффективно.

**Проблема 2: Нет документации ПОЧЕМУ**

Diff показывает ЧТО изменилось, но не ЗАЧЕМ. Через месяц непонятно, почему убрали секцию X или добавили параметр Y.

**Проблема 3: Нет версионной истории**

Каждый апдэйт — это чёрный ящик. Нельзя сравнить v3.5 → v3.6 → v3.7 и понять траекторию развития.

**Проблема 4: "Одно лечим — другое калечим"**

Без явного плана легко сломать работающее, пытаясь добавить новое. Нет точки сверки.

---

## Часть 2: Решение — Planning Document First

### Новый процесс

```
ЗАПРОС: "обнови скил" или "создай скил"
           ↓
    [1] Анализ текущего состояния
           ↓
    [2] Создание Planning Document (MD файл)
        - Проблемы
        - План изменений
        - Было → Стало (preview)
        - Риски
           ↓
    [3] СТОП. Ждём подтверждения.
           ↓
    [4] Пользователь: "да" / "нет" / "измени X"
           ↓
    [5] Только после "да" → реализация
           ↓
    [6] Финальный Diff Report (сверка с планом)
```

### Planning Document структура

```markdown
# [Skill Name]: План [создания/обновления] v[X.Y.Z] → v[A.B.C]
## Дата | Автор запроса

---

## 1. Контекст
[Зачем этот апдэйт, что триггернуло]

## 2. Проблемы / Задачи
[Что не работает или чего не хватает]

## 3. План изменений

### Добавляем
| Что | Зачем | Где |
|-----|-------|-----|
| ... | ...   | ... |

### Изменяем
| Что | Было | Станет | Зачем |
|-----|------|--------|-------|
| ... | ...  | ...    | ...   |

### Удаляем
| Что | Почему безопасно удалить |
|-----|--------------------------|
| ... | ...                      |

### Не трогаем
[Явный список того, что остаётся как есть]

## 4. Было → Стало (Preview)

### SKILL.md
| Секция | v[old] | v[new] |
|--------|--------|--------|
| ...    | ...    | ...    |

### Структура файлов
```
До:                    После:
skill/                 skill/
├── SKILL.md           ├── SKILL.md
├── ...                ├── ...
```

## 5. Риски
| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| ...  | ...         | ...       |

## 6. Чеклист подтверждения

- [ ] План понятен
- [ ] Изменения согласованы
- [ ] Риски приемлемы
- [ ] Можно начинать

**Ожидаю подтверждение: "да" для старта**

---

*Planning Document v1.0*
```

---

## Часть 3: Изменения в skill-architect

### 3.1 Добавляем

| Что | Зачем | Где |
|-----|-------|-----|
| Planning Document Protocol | Core feature — документ до изменений | SKILL.md, новая секция |
| planning-document.md | Шаблон Planning Document | reference/ |
| BLOCKING перед реализацией | Не начинать без "да" | SKILL.md |

### 3.2 Изменяем

| Что | Было | Станет | Зачем |
|-----|------|--------|-------|
| UPDATE Protocol | Snapshot → Change → Diff | Snapshot → **Planning Doc** → Confirm → Change → Diff | Контроль до изменений |
| REFACTOR Protocol | Audit → Plan → Confirm → Rebuild | Audit → **Planning Doc** → Confirm → Rebuild | Унификация |
| Config Dialog | Сразу после конфига — работа | После конфига — **Planning Doc** | Единый flow |
| Version | v3.7.1 | v3.8.0 | Minor feature add |

### 3.3 Удаляем

| Что | Почему безопасно |
|-----|------------------|
| Ничего | Это additive change, не breaking |

### 3.4 Не трогаем

- 5-Phase Process (остаётся)
- Validation scripts (остаются)  
- Language Rules (остаются)
- Context Tracking (остаётся)
- Self-Test (остаётся)
- Critical Rules (остаются)

---

## Часть 4: Было → Стало (Preview)

### SKILL.md секции

| Секция | v3.7.1 | v3.8.0 |
|--------|--------|--------|
| Header description | "v3.7.1 \| Professional skill creation system..." | "v3.8.0 \| Planning Document First..." |
| Pre-Flight Checks | 6 пунктов | 7 пунктов (+Planning Doc) |
| UPDATE Protocol | Step 1-3 | Step 1-4 (+Planning Doc step) |
| REFACTOR Protocol | Step 1-6 | Step 1-7 (+Planning Doc step) |
| NEW: Planning Document Protocol | — | Новая секция |
| Resources | 5 items | 6 items (+planning-document.md) |

### Структура файлов

```
До (v3.7.1):                    После (v3.8.0):
skill-architect/                skill-architect/
├── SKILL.md                    ├── SKILL.md (updated)
├── README.md                   ├── README.md (updated)
├── reference/                  ├── reference/
│   ├── packaging.md            │   ├── packaging.md
│   ├── templates.md            │   ├── templates.md
│   ├── engines.md              │   ├── engines.md
│   └── ...                     │   ├── planning-document.md (NEW)
│                               │   └── ...
└── scripts/                    └── scripts/
    ├── validate-skill.sh           ├── validate-skill.sh
    └── audit-skill.sh              └── audit-skill.sh
```

---

## Часть 5: Детали реализации

### 5.1 Новая секция в SKILL.md: Planning Document Protocol

```markdown
## Planning Document Protocol — MANDATORY

**Triggers:** ANY skill creation or update

### Why
- No changes without documented plan
- User confirms BEFORE implementation
- Creates version history
- "Было → Стало" visible upfront

### Process

```
1. Analyze current state (if update)
2. Create Planning Document (MD file)
3. Save to /mnt/user-data/outputs/
4. STOP. Wait for confirmation.
5. User says "да" / "yes" → proceed
6. User says "нет" / adjustments → revise plan
7. Only after confirmation → implement
8. Final Diff Report (verify against plan)
```

### Planning Document Must Include
- Context (why this change)
- Problems / Tasks
- Changes: Add / Modify / Remove / Keep
- Было → Стало preview
- Risks
- Confirmation checklist

### BLOCKING
**Do NOT start implementation until user confirms.**
Response to confirmation request must be explicit "да", "yes", "подтверждаю", "proceed".

Silence or unclear response = ask again.
```

### 5.2 Изменения в UPDATE Protocol

**Было (v3.7.1):**
```markdown
## UPDATE Protocol

### Step 1: Snapshot
### Step 2: Analyze, then Change
### Step 3: Diff Report
```

**Станет (v3.8.0):**
```markdown
## UPDATE Protocol

### Step 1: Snapshot
```bash
cp -r /mnt/skills/user/skill-name /home/claude/skill-name-ORIGINAL
```

### Step 2: Analyze
Read and understand current state. Never remove what you haven't understood.

### Step 3: Planning Document — BLOCKING
Create Planning Document with:
- Problems identified
- Planned changes (add/modify/remove/keep)
- Было → Стало preview
- Risks

Save to `/mnt/user-data/outputs/[skill-name]_UPDATE_PLAN.md`

**STOP. Wait for user confirmation.**

### Step 4: Implement (only after "да")
Make changes according to confirmed plan.

### Step 5: Diff Report
Compare result with plan. Note any deviations.
```

### 5.3 Новый reference файл: planning-document.md

```markdown
# Planning Document Template

## Purpose
Planning Document is created BEFORE any skill changes.
It serves as:
- Plan (what will change)
- Contract (changes start only after confirmation)
- History (было → стало)
- Log (for future versions)

## Template

[Полный шаблон из Части 2]

## Rules
1. ALWAYS create Planning Document before changes
2. ALWAYS wait for explicit confirmation
3. ALWAYS save to /mnt/user-data/outputs/
4. NEVER skip for "small" changes
5. NEVER proceed on unclear confirmation

## Confirmation Phrases (valid)
- "да", "yes", "подтверждаю", "proceed", "go", "делай", "начинай"

## Non-Confirmation (ask again)
- "ок", "хорошо", "понял" (acknowledgment, not confirmation)
- Silence
- Questions
- Requests for changes
```

---

## Часть 6: Риски

| Риск | Вероятность | Влияние | Митигация |
|------|-------------|---------|-----------|
| Замедление процесса | High | Low | Это фича, не баг. Качество > скорость |
| Пользователь не читает план | Medium | Medium | Чеклист подтверждения + явный STOP |
| Большие документы для простых изменений | Medium | Low | Масштабировать детальность под сложность |
| Забыть создать Planning Doc | Low | High | Добавить в Pre-Flight Checks |

---

## Часть 7: Чеклист подтверждения

- [ ] Концепция Planning Document First понятна
- [ ] Изменения в UPDATE Protocol согласованы
- [ ] Изменения в REFACTOR Protocol согласованы
- [ ] Новый reference файл согласован
- [ ] Риски приемлемы
- [ ] Версия 3.8.0 корректна

**Ожидаю подтверждение: "да" для старта реализации**

---

## Часть 8: После подтверждения

Когда скажешь "да", я:

1. Создам snapshot текущего skill-architect
2. Обновлю SKILL.md по плану выше
3. Создам reference/planning-document.md
4. Обновлю README.md
5. Запущу validate-skill.sh
6. Создам финальный Diff Report (сверка с этим планом)
7. Упакую в .skill файл

---

## Использование этого документа

**Для самообновления в новом чате:**

1. Загрузи этот файл в новый чат
2. Скажи: "обнови skill-architect по этому плану"
3. Claude прочитает план и выполнит реализацию
4. Финальный Diff Report покажет соответствие плану

**Для обновления idea-pipeline:**

1. После обновления skill-architect
2. Используй новый skill-architect для обновления idea-pipeline
3. Он автоматически создаст Planning Document для idea-pipeline
4. И так далее для любых скилов

---

*Planning Document для skill-architect v3.7.1 → v3.8.0*
*Создан: 2025-11-27*
*Статус: Ожидает подтверждения*
