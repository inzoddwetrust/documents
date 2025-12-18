# UPDATE Plan: skill-architect v3.8.0 → v3.9.0

## Цель

1. Интегрировать принципы clean-protocol (краткость)
2. Добавить MANIFEST.md для целостности многофайловых скиллов
3. Добавить Chat Verification в протокол

---

## Проблемы текущей версии

| # | Проблема | Решение |
|---|----------|---------|
| 1 | SKILL.md 344 строки, избыточность | Сократить до ~220 |
| 2 | Config Dialog 9 вопросов | Smart Config: 2 вопроса |
| 3 | Activation response длинный | 1 строка |
| 4 | Шаблоны содержат воду | Убрать generic фразы |
| 5 | Нет правил краткости для скиллов | Clean Skill Principles |
| 6 | Нет реестра файлов | MANIFEST.md |
| 7 | Нет проверки целостности | validate-skill.sh +manifest |
| 8 | Можно забыть детали из чата | Chat Verification step |

---

## KEEP

- 5-Phase Process
- Planning Document requirement
- Validation + packaging flow
- Token counter
- SemVer versioning

---

## REMOVE

| Что | Причина |
|-----|---------|
| Verbose Config (9 полей) | → Smart Config |
| Self-Test block в SKILL.md | → reference/ |
| Повторы "CRITICAL", "MANDATORY" | Один раз достаточно |
| Длинный activation | → 1 строка |

---

## ADD

### 1. Clean Skill Principles

```markdown
## Clean Skill Principles

Skills you create MUST follow:
1. **Density** — every line carries meaning
2. **No fluff** — no "Sure!", disclaimers, obvious explanations
3. **Chat = 2-4 sentences** — unless user asks more
4. **Show, don't explain** — examples > descriptions
5. **N/2 rule** — asked N words, deliver N/2
```

### 2. Smart Config

```markdown
## Config

Ask: Purpose? Triggers?
Auto-derive: type, complexity, tools.
Ask more only if unclear.
```

### 3. Compact Activation

```markdown
## Activation

Response: `Skill Architect ready. Purpose?`
```

### 4. Chat Verification Step

```markdown
### Step 3.5: Chat Verification — BLOCKING

Before confirming plan:
1. Scan ENTIRE chat history
2. List all discussed items
3. Check each against plan
4. Report: "Verified: [N] items. Missing: [list or 'none']"

Then ask for confirmation.
```

### 5. MANIFEST.md

**Формат:**
```markdown
# MANIFEST.md

## skill-name vX.Y.Z

Build: YYYY-MM-DD
Files: N

| File | Version | Lines | Description |
|------|---------|-------|-------------|
| SKILL.md | x.y.z | n | desc |
| README.md | x.y.z | n | desc |

## Integrity

Total lines: N

## Changelog

### vX.Y.Z (DATE)
- Added: [files]
- Changed: [files]
- Unchanged: N files
```

**Правило:** Required для скиллов с reference/, recommended для простых (<3 файлов).

### 6. generate-manifest.sh (NEW)

Скрипт автогенерации MANIFEST.md из папки скила.

### 7. validate-skill.sh v1.3

+manifest check: сверка файлов и line count с манифестом.

---

## Файлы для изменения

| Файл | Действие |
|------|----------|
| SKILL.md | Сократить, +Clean Principles, +Chat Verification |
| reference/packaging.md | +MANIFEST section, Golden Rule #8 |
| reference/templates.md | +MANIFEST template, убрать воду |
| reference/quality-checklist.md | +density check |
| scripts/validate-skill.sh | v1.2 → v1.3, +manifest check |
| scripts/generate-manifest.sh | NEW |
| MANIFEST.md | NEW (self-reference) |

---

## Before → After

### Config

**Before:** 9 полей, таблица  
**After:** `Purpose? Triggers?`

### Activation

**Before:** ~20 строк с таблицами и self-test  
**After:** `Skill Architect ready. Purpose?`

### SKILL.md

**Before:** 344 lines  
**After:** ~220 lines

### Структура

```
skill-architect/
├── SKILL.md (updated)
├── README.md
├── MANIFEST.md (NEW)
├── reference/
│   ├── packaging.md (updated)
│   ├── templates.md (updated)
│   ├── planning-document.md
│   ├── engines.md
│   ├── workflow.md
│   └── quality-checklist.md
└── scripts/
    ├── validate-skill.sh (v1.3)
    ├── audit-skill.sh
    └── generate-manifest.sh (NEW)
```

---

## Риски

| Риск | Митигация |
|------|-----------|
| Потеря инфы при сокращении | Перенос в reference/ |
| Короткий config → плохие скиллы | Smart defaults + ask if unclear |
| MANIFEST overhead для простых | Recommended, не required для <3 files |
| Line count drift | Warning, не error |

---

## Chat Verification

| # | Из чата | В плане |
|---|---------|---------|
| 1 | Краткость из clean-protocol | ✅ |
| 2 | Chat 2-4 предложения | ✅ |
| 3 | Без "Sure!", preambles | ✅ |
| 4 | Компактный config | ✅ |
| 5 | Создаваемые скиллы краткие | ✅ |
| 6 | Chat Verification step | ✅ |
| 7 | MANIFEST.md | ✅ |
| 8 | generate-manifest.sh | ✅ |
| 9 | validate-skill.sh +manifest | ✅ |

**Verified: 9 items. Missing: none.**

---

## Версия

v3.8.0 → v3.9.0 (MINOR: Clean Principles + MANIFEST)

---

**Жду подтверждения.**
