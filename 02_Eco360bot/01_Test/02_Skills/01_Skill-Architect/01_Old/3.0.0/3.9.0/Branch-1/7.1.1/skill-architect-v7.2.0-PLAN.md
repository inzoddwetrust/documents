# skill-architect: План v7.1.1 → v7.2.0

## 2025-12-07 | Docs Reorder

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Russian |
| Frontmatter | name + description (version IN description) |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

Пять проблем выявлены в v7.1.1:

1. **P07→P08 нелогично** — доки создаются ДО скана чата, результаты скана не попадают в доки
2. **decisions/ подпапка** — избыточная вложенность для одного файла
3. **Файлы без порядка** — непонятно что читать первым, что важнее
4. **Context Anchor формат** — inline backticks вместо блока кода (нельзя копировать кликом)
5. **Нет validate-docs.sh** — docs не валидируются

---

## 2. Проблемы / Задачи

| # | Задача | Priority | Source |
|---|--------|----------|--------|
| B-012 | Swap P07↔P08 (Scan before Docs) | High | v7.1.1 chat |
| B-013 | Flat numbered docs structure (8 files) | High | v7.1.1 chat |
| B-014 | Add 06-SCAN.md to docs | High | v7.1.1 chat |
| B-015 | Remove decisions/ subfolder | Medium | v7.1.1 chat |
| B-016 | Create validate-docs.sh | Medium | v7.1.1 chat |
| B-017 | Fix Context Anchor format (code block) | High | v7.1.1 chat |

---

## 3. План изменений

### Добавляем

| Файл | Что |
|------|-----|
| scripts/validate-docs.sh | Валидация структуры docs |
| 06-SCAN.md template | В docs-packaging.md |

### Изменяем

| Файл | Что меняем |
|------|------------|
| P00-router.md | State machine: P07↔P08 swap |
| P07-delivery-docs.md | → переименовать в P07-scan.md, переписать |
| P08-scan.md | → переименовать в P08-docs-closure.md, переписать |
| docs-packaging.md | Новая структура 8 файлов, нумерация |
| templates.md | Context Anchor = code block (не inline) |
| quality-checklist.md | Docs validation items |
| SKILL.md | Protocol Router table, Context Tracking format |
| P01-activation.md | Context Anchor format в примере |
| All 41+ files | Footer v7.1.1 → v7.2.0 |

### Удаляем

| Что | Почему |
|-----|--------|
| decisions/ subfolder pattern | Плоская структура |

### Не трогаем

- P02-config.md, P03-planning.md, P04-build.md, P05-validate.md, P06-delivery-skill.md (логика)
- Все скрипты кроме нового validate-docs.sh
- engines.md, packaging.md, naming-convention.md
- virtual-testing.md, test-*.md, personas.md, adversarial.md, expert-panel.md
- project-*.md

---

## 4. Было → Стало

### Protocol Flow

**Было:**
```
P06 → P07 (Docs) → P08 (Scan) → END
```

**Стало:**
```
P06 → P07 (Scan) → P08 (Docs+Closure) → END
```

### Docs Structure

**Было:**
```
skill-name-docs/
├── vX.Y.Z-PLAN.md
├── vX.Y.Z-DIFF.md
├── CHANGELOG.md
├── BACKLOG.md
├── LOGIC-TREE.md
├── README.md
└── decisions/
    └── vX.Y.Z-decisions.md
```

**Стало:**
```
skill-name-vX.Y.Z-docs/
├── 01-CHANGELOG.md
├── 02-DIFF.md
├── 03-PLAN.md
├── 04-DECISIONS.md
├── 05-BACKLOG.md
├── 06-SCAN.md          ← NEW
├── 07-README.md
└── 08-LOGIC-TREE.md    ← ОБЯЗАТЕЛЬНЫЙ
```

### Context Anchor

**Было (inline backticks):**
```markdown
`skill-architect: file_read → P00-router.md`
🟢 ~165k | ~3k 🟡
```

**Стало (code block):**
````markdown
```
skill-architect: file_read → P00-router.md
```
🟢 ~165k | ~3k 🟡
````

---

## 5. Риски

| Риск | Вероятность | Влияние | Митигация |
|------|-------------|---------|-----------|
| Breaking change docs format | Low | Low | Новый формат для новых, старые не ломаем |
| Путаница P07/P08 номеров | Medium | Low | Чёткое переименование файлов |
| Много файлов менять | Medium | Medium | Делаем последовательно, валидируем |

---

## 6. Чат-верификация

Проверка всех обсуждённых пунктов:

| # | Пункт | Статус |
|---|-------|--------|
| 1 | P07↔P08 swap (Scan before Docs) | ✅ В плане (B-012) |
| 2 | Flat numbered docs (8 files) | ✅ В плане (B-013) |
| 3 | 06-SCAN.md добавить | ✅ В плане (B-014) |
| 4 | decisions/ убрать | ✅ В плане (B-015) |
| 5 | validate-docs.sh создать | ✅ В плане (B-016) |
| 6 | Context Anchor = code block | ✅ В плане (B-017) |
| 7 | 08-LOGIC-TREE.md обязательный | ✅ В структуре |

**Verified: 7 items. Missing: none**

---

## 7. Чеклист подтверждения

- [ ] План понятен
- [ ] Изменения согласованы
- [ ] Риски приемлемы
- [ ] Можно начинать

---

**⛔ Ожидаю подтверждение: "да", "yes", "go", "делай"**

---

*v7.2.0-PLAN.md | skill-architect v7.1.1 → v7.2.0*
