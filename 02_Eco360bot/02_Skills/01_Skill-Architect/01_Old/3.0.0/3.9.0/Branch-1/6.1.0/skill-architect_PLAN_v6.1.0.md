# skill-architect: План v6.0.0 → v6.1.0

**Date:** 2025-12-02
**Type:** Refactor — Protocol-First Architecture Alignment

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | < 300 |
| README language | Русский |
| Frontmatter | name + description |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

Skill-architect v6.0.0 заявляет Protocol-Driven подход, но:
- Диагностика (self-diagnostic.md) ожидает inline-секции в SKILL.md
- Скрипты проверяют структуру по старым правилам
- SSOT нарушен — одни правила в нескольких местах

**Цель:** Полное выравнивание под Protocol-First — SKILL.md = роутер, всё остальное в протоколах.

---

## 2. Проблемы (из диагностики)

| # | Проблема | Источник |
|---|----------|----------|
| 1 | self-diagnostic ожидает Activation, Config, REFACTOR, UPDATE секции | self-diagnostic.md |
| 2 | SSOT violations: BLOCKING × 4, Required × 5 | ssot-check.sh |
| 3 | Command duplication: `zip -r` × 12 | reference/ files |
| 4 | self-diagnostic.md ссылается на v5.4.0 | устаревший footer |
| 5 | 3 файла > 300 строк | engines.md, workflow.md, project-modules.md |
| 6 | Mixed languages в reference/ | 25/26 файлов с Cyrillic |

---

## 3. План изменений

### 3.1 Добавляем

| Файл | Что |
|------|-----|
| reference/commands.md | SSOT для всех команд (zip, cp, bash scripts/) |
| protocols/P00-router.md | Мета-протокол навигации |

### 3.2 Изменяем

| Файл | Изменение |
|------|-----------|
| SKILL.md | Упростить до чистого роутера, убрать дублирование |
| self-diagnostic.md | Переписать под Protocol-First (проверять протоколы, не inline-секции) |
| scripts/self-diagnostic.sh | Адаптировать под новые проверки |
| scripts/audit-skill.sh | Добавить Protocol-First mode |
| scripts/ssot-check.sh | Исключить протоколы из duplication check (там дублирование норма) |

### 3.3 Удаляем

Ничего не удаляем — только перемещаем/консолидируем.

### 3.4 Не трогаем

- Все 8 протоколов P01-P08 (они уже правильные)
- scripts/validate-skill.sh, validate-naming.sh
- reference/templates.md, engines.md, packaging.md
- Project Mode файлы (project-*.md)

---

## 4. Было → Стало

### SKILL.md

**Было (166 lines):**
```
- Protocol Flow diagram
- Protocol Router table
- Quick Start
- Modes table
- Clean Skill Principles (дублирует P04)
- Critical Rules (дублирует constraints в разных местах)
- Required Files
- Versioning
- Resources
```

**Станет (~120 lines):**
```
- NEVER DEGRADE (stays — это guard)
- Skill Dependencies (stays — это init)
- Context Tracking (stays — это meta)
- Protocol Router (simplified — only trigger → protocol)
- Quick Start (stays — UX)
- Resources (simplified — only paths)
```

### self-diagnostic.md

**Было:** Проверяет секции в SKILL.md
**Станет:** Проверяет наличие и содержимое протоколов

### New: commands.md

```markdown
# Commands Reference (SSOT)

## Packaging
zip -r [name].skill [folder]/

## Backup
cp -r [source] [source]-BACKUP

## Validation
bash scripts/validate-skill.sh [path]
bash scripts/validate-naming.sh [path]
bash scripts/ssot-check.sh [path]
```

---

## 5. Риски

| Риск | Вероятность | Mitigation |
|------|-------------|------------|
| Скрипты сломаются | Medium | Тестировать после каждого изменения |
| Потеря функционала | Low | NEVER DEGRADE check перед каждым edit |
| Регрессия диагностики | Medium | Сохранить backup, сравнить output |

---

## 6. Чат-верификация

Обсуждено в этом чате:
1. ✅ Полная диагностика запрошена
2. ✅ Выбран Вариант A (Protocol-First)
3. ✅ Цель: обкатать практику для других скилов
4. ✅ Логика: постоянное перечитывание инструкций = понимание прогресса

Missing: none

---

## 7. Чеклист подтверждения

- [ ] План понятен
- [ ] Изменения согласованы
- [ ] Риски приемлемы
- [ ] Можно начинать

---

**Ожидаю подтверждение: "да", "yes", "go", "делай"**

---

*skill-architect_PLAN_v6.1.0.md | 2025-12-02*
