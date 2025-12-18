# Финальная сверка: skill-architect v5.2.0 → v5.3.0

**Дата:** 2025-12-02  
**Цель:** Убедиться что ничего не упущено перед апдейтом в новом чате

---

## 1. Что имеем сейчас (v5.2.0)

### Skill файлы:

```
skill-architect/
├── SKILL.md (291 lines, v5.2.0) ✅
├── README.md (v5.1.0 ❌ — должен быть v5.2.0)
├── MANIFEST.md (v5.2.0) ✅
├── reference/ (13 файлов)
│   ├── engines.md (v1.1.0 | v5.1.0)
│   ├── evaluations.md (v1.0.0 | v4.1.0 ❌)
│   ├── naming-convention.md (v1.0.0 | v5.0.0)
│   ├── packaging.md (НЕТ ФУТЕРА ❌)
│   ├── planning-document.md (НЕТ ФУТЕРА ❌)
│   ├── project-filters.md (v1.0.0 | v5.0.0)
│   ├── project-import.md (v1.0.0 | v5.0.0)
│   ├── project-mode.md (v1.1.0 | v5.1.0)
│   ├── project-modules.md (v1.0.0 | v5.0.0)
│   ├── quality-checklist.md (v1.1.0 | v5.1.0)
│   ├── self-diagnostic.md (v1.0.0 | v5.2.0) ✅
│   ├── templates.md (v1.1.0 | v5.1.0)
│   └── workflow.md (v1.1.0 | v5.1.0)
└── scripts/ (6 файлов) ✅
```

### Docs файлы (v5.2.0-docs.zip):

```
skill-architect-docs/
├── LOGIC-TREE.md (v1.2.0 | v5.0.0 ❌ — устарел на 2 версии)
├── BACKLOG.md (v1.3.0 | v5.0.0 ❌ — нет v5.2.0 в Done)
├── CHANGELOG.md (есть v5.2.0 entry) ✅
├── development-guide.md (v1.0.0 | v5.0.0)
├── README.md (v5.1.0 ❌)
├── v5.0.0-PLAN.md ✅
├── v5.0.0-DIFF.md ✅
├── v5.1.0-PLAN.md ✅
├── v5.1.0-DIFF.md ✅
├── v5.2.0-PLAN.md ✅
├── v5.2.0-DIFF.md ✅
└── decisions/ (5 файлов) ✅
```

---

## 2. Проблемы найденные в этом чате

| # | Проблема | Источник | В плане? |
|---|----------|----------|----------|
| 1 | 13 файлов с устаревшей skill-architect версией в футере | Аудит | ✅ |
| 2 | 2 файла без футера (packaging, planning-document) | Аудит | ✅ |
| 3 | LOGIC-TREE.md на v5.0.0, нет v5.1/v5.2 changes | Аудит | ✅ |
| 4 | BACKLOG.md нет v5.2.0 в Done | Аудит | ✅ |
| 5 | Нет инструкций docs для создаваемых скиллов | Аудит | ✅ docs-packaging.md |
| 6 | Нет Phase 6: DOCS в workflow.md | Аудит | ✅ |
| 7 | README (skill) v5.1.0 вместо v5.2.0 | Аудит | ✅ |
| 8 | README (docs) v5.1.0 | Аудит | ✅ |

---

## 3. Правила из старых версий (не потерять!)

### Из v3.9.0 SELF_AUDIT:

| Правило | Статус |
|---------|--------|
| Версия файла ≠ версия скилла | ✅ В плане |
| Формат: `*FileName vX.Y.Z \| skill-architect vA.B.C*` | ✅ В плане |
| Версия файла меняется только если контент изменился | ✅ В плане |
| MANIFEST отслеживает версии файлов | ✅ Есть |

### Из v3.8.0-PLAN:

| Правило | Статус |
|---------|--------|
| Planning Document First | ✅ Работает |
| Chat Verification step | ✅ Работает |
| BLOCKING перед реализацией | ✅ Работает |

### Из v5.0.0-PLAN:

| Правило | Статус |
|---------|--------|
| docs.zip структура | ✅ Есть |
| LOGIC-TREE обновлять при изменении flow | ❌ Не делали для v5.1/v5.2 |
| development-guide.md | ✅ Есть |

### Из v5.1.0-PLAN:

| Правило | Статус |
|---------|--------|
| NEVER DEGRADE | ✅ В SKILL.md |
| Reference Reading trigger | ✅ В SKILL.md |
| Restore REFACTOR/UPDATE protocols | ✅ В SKILL.md |

---

## 4. Что добавляем в v5.3.0

| # | Что | Файл | Версия файла |
|---|-----|------|--------------|
| 1 | Новый файл docs-packaging.md | reference/ | v1.0.0 |
| 2 | Phase 6: DOCS | workflow.md | v1.1.0 → v1.2.0 |
| 3 | Футер | packaging.md | v1.0.0 (NEW) |
| 4 | Футер | planning-document.md | v1.0.0 (NEW) |
| 5 | v5.1/v5.2/v5.3 changes | LOGIC-TREE.md | v1.2.0 → v1.3.0 |
| 6 | v5.2.0 в Done + B-018/B-019 | BACKLOG.md | v1.3.0 → v1.4.0 |
| 7 | v5.3.0-decisions.md | decisions/ | v1.0.0 (NEW) |

---

## 5. Что НЕ меняем (версия файла остаётся)

| Файл | Версия файла | Причина |
|------|--------------|---------|
| engines.md | v1.1.0 | Контент не менялся |
| evaluations.md | v1.0.0 | Контент не менялся |
| naming-convention.md | v1.0.0 | Контент не менялся |
| project-*.md (4 файла) | v1.0.0/v1.1.0 | Контент не менялся |
| quality-checklist.md | v1.1.0 | Контент не менялся |
| self-diagnostic.md | v1.0.0 | Контент не менялся |
| templates.md | v1.1.0 | Контент не менялся |
| development-guide.md | v1.0.0 | Контент не менялся |
| SKILL.md | — | Только description version |

**НО:** skill-architect version в футере обновляем до v5.3.0 везде!

---

## 6. Файлы для нового чата

Загрузить в новый чат:

1. **skill-architect-v5.3.0-PLAN.md** — план работ
2. **skill-architect-v5.2.0.skill** — текущий скилл (если есть)
3. **skill-architect-v5.2.0-docs.zip** — текущие docs

Или дать Claude доступ к `/mnt/skills/user/skill-architect/` + docs.

---

## 7. Команда для нового чата

```
Обнови skill-architect по плану v5.3.0-PLAN.md

Файлы:
- План: skill-architect-v5.3.0-PLAN.md
- Текущий skill: /mnt/skills/user/skill-architect/
- Текущие docs: skill-architect-v5.2.0-docs.zip
```

---

## 8. Контрольные вопросы

### Ничего не упустили?

- [x] Все проблемы из аудита в плане
- [x] Правило версионирования файлов задокументировано
- [x] LOGIC-TREE будет обновлён
- [x] BACKLOG будет обновлён
- [x] docs-packaging.md будет создан
- [x] workflow.md получит Phase 6
- [x] Футеры будут добавлены/исправлены

### Что может пойти не так?

| Риск | Митигация |
|------|-----------|
| Claude забудет правило версий файлов | Явно в плане + этот чеклист |
| Пропустит файл | MANIFEST как чеклист |
| Сломает SKILL.md | Только description меняем |

---

## 9. Итог

**Готово к апдейту:** ✅

**План полный:** ✅ (22 пункта в Chat Verification)

**Риски минимальны:** ✅ (только футеры + 1 новый файл + обновление docs)

---

*Финальная сверка v5.3.0 | 2025-12-02*
