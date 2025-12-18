# Planning Document: skill-architect v5.1.0 → v5.2.0

**Дата:** 2025-12-02  
**Контекст:** Добавление протокола самодиагностики для замыкания цикла качества  
**Тип:** MINOR (новая фича)

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Russian |
| Frontmatter | name + description + version |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

После обновления v3.9.0 → v5.1.0 выявлена потребность в инструменте верификации:
- Проверка что ничего не потеряно после апдейта
- Сравнение с предыдущей версией
- Автоматизированная валидация модулей и протоколов

---

## 2. Задачи

| # | Задача |
|---|--------|
| 1 | Добавить протокол самодиагностики |
| 2 | Добавить скрипт автоматической проверки |
| 3 | Интегрировать триггеры в SKILL.md |
| 4 | Добавить Skill Dependencies — always-on skills |
| 5 | Расширить Reference Reading таблицу |

---

## 3. План изменений

### Добавляем

| Что | Зачем | Где |
|-----|-------|-----|
| self-diagnostic.md | Документация протокола | reference/ |
| self-diagnostic.sh | Автоматическая проверка | scripts/ |
| Триггер в Quick Start | Активация протокола | SKILL.md |
| Ссылка в Resources | Discoverability | SKILL.md |
| **Skill Dependencies** | Always-on skills при активации | SKILL.md (новая секция) |
| **Расширенная Reference Reading** | Больше триггеров | SKILL.md |

### Новая секция: Skill Dependencies

```markdown
## ⚠️ MANDATORY: Skill Dependencies

On skill-architect activation, ALSO read:

| Skill | Why | When |
|-------|-----|------|
| clean-protocol | Response formatting rules | ALWAYS |

Rule: First action = file_read on dependency skills.
```

### Расширенная Reference Reading таблица

```markdown
| Trigger | Read First |
|---------|------------|
| "project" keyword | `reference/project-mode.md` |
| "create skill" | `reference/templates.md` |
| "refactor" / "update" | `reference/planning-document.md` |
| Packaging | `reference/packaging.md` |
| **"self-test" / "diagnose"** | `reference/self-diagnostic.md` |
| **ANY output >10 lines** | Check clean-protocol rules |
```

### Изменяем

| Что | Было | Станет | Зачем |
|-----|------|--------|-------|
| version | v5.1.0 | v5.2.0 | SemVer |
| scripts count | 5 | 6 | +1 скрипт |
| reference count | 12 | 13 | +1 документ |
| SKILL.md | 274 lines | ~290 lines | +секции |
| Reference Reading | 4 triggers | 6 triggers | +self-test, +output check |

### Удаляем

| Что | Почему |
|-----|--------|
| — | Ничего не удаляем |

### Не трогаем

- Все существующие секции SKILL.md
- Все существующие reference/ файлы  
- Все существующие scripts/
- MANIFEST.md структура (обновим только версию)

---

## 4. Было → Стало

### Структура файлов

```
v5.1.0                          v5.2.0
scripts/ (5)                    scripts/ (6)
├── audit-skill.sh              ├── audit-skill.sh
├── audit-project.sh            ├── audit-project.sh
├── validate-skill.sh           ├── validate-skill.sh
├── validate-naming.sh          ├── validate-naming.sh
└── generate-manifest.sh        ├── generate-manifest.sh
                                └── self-diagnostic.sh   ← NEW

reference/ (12)                 reference/ (13)
├── ... (12 files)              ├── ... (12 files)
                                └── self-diagnostic.md   ← NEW
```

### SKILL.md секции

| Секция | v5.1.0 | v5.2.0 |
|--------|--------|--------|
| Frontmatter | v5.1.0 | v5.2.0 |
| MANDATORY: Skill Dependencies | — | NEW |
| Reference Reading | 4 triggers | 6 triggers |
| Quick Start | 2 modes | + self-test |
| Resources | 12 ref + 5 scripts | 13 ref + 6 scripts |
| Footer | v5.1.0 | v5.2.0 |

---

## 5. Риски

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| SKILL.md > 300 lines | Средняя (+16 строк) | Компактная Skill Dependencies секция |
| Конфликт с существующим | Нет | Новые файлы |
| Забуду читать dependencies | Низкая | Секция в начале SKILL.md |

---

## 6. Chat Verification

Из чата:
1. ✅ Протокол самодиагностики создан и протестирован
2. ✅ Скрипт self-diagnostic.sh работает (32/32 checks)
3. ✅ Регрессия против v3.9.0 пройдена
4. ✅ Триггеры определены: `self-test`, `diagnose`, `проверь себя`
5. ✅ clean-protocol требует файлы для >10 строк прозы
6. ✅ Проблема: не читал clean-protocol автоматически
7. ✅ Проблема: не читал planning-document.md перед планом
8. ✅ Решение: Skill Dependencies секция
9. ✅ Решение: расширить Reference Reading таблицу

**Verified: 9 items. Missing: none.**

---

## 7. Чеклист подтверждения

- [ ] План понятен
- [ ] Добавляем только новое, не трогаем старое
- [ ] SKILL.md останется < 300 строк
- [ ] Можно начинать

---

**Ожидаю:** явное "да" / "go" / "делай"

---

*Planning Document | skill-architect v5.2.0*
