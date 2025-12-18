# UPGRADE GUIDE: skill-architect v4.7.0 → v5.0.0

## Meta

| Field | Value |
|-------|-------|
| From | v4.7.0 "Consolidated" |
| To | v5.0.0 "Micro-Skills" |
| Type | BREAKING (architecture change) |
| Date | 2025-12-18 |

---

## Проблемы v4.7.0 (почему обновляем)

### 1. Контекстный дрифт
- SKILL.md 483 строки + 7 protocols + 13 reference = ~4500 строк
- Claude читает в начале → работает по памяти → забывает

### 2. Пропуск шагов
- P03c-docs пропускался в ~70% builds
- P04-deliver: tar вместо zip

### 3. Нарушение Anthropic best practices
- Skills должны быть < 500 строк
- Progressive disclosure: загружать только нужное
- Self-contained: не требовать чтение других файлов

---

## Архитектура v5.0.0

### Структура (ВАЖНО!)

```
skill-architect/              ← ОДНА папка в корне ZIP
├── SKILL.md                  ← ОДИН SKILL.md (роутер)
├── README-skill-architect.md
├── CHANGELOG-skill-architect.md
├── MANIFEST.md
├── docs/                     ← G16: docs на верхнем уровне!
│   ├── v4.6.0/
│   ├── v4.6.1/
│   └── v5.0.0/
│       ├── LOGIC-TREE-skill-architect-v5.0.0.md
│       ├── SCAN-skill-architect-v5.0.0.md
│       └── DIFF-skill-architect-v5.0.0.md
├── protocols/                ← Micro-skills как протоколы
│   ├── P01-init.md
│   ├── P02-plan.md
│   ├── P03a-build.md
│   ├── P03b-validate.md
│   ├── P03c-docs.md
│   ├── P04-deliver.md
│   └── P05-genes.md
├── reference/                ← Все reference в одном месте
│   ├── cognitive-razors.md
│   ├── memory-budget.md
│   ├── genetic-audit.md
│   └── ... (14 файлов)
└── scripts/                  ← Все scripts в одном месте
    ├── validate.sh
    ├── genetic-audit.sh
    ├── package.sh
    └── ... (7 файлов)
```

### ⛔ КРИТИЧЕСКИЕ ПРАВИЛА УПАКОВКИ

```bash
# ✅ ПРАВИЛЬНО — ZIP с папкой-обёрткой
cd /path/to/parent
zip -r skill-architect-v5.0.0.skill skill-architect/

# ❌ НЕПРАВИЛЬНО — tar
tar -cvf skill-architect.skill skill-architect/

# ❌ НЕПРАВИЛЬНО — ZIP без папки
cd skill-architect
zip -r ../skill.skill *

# ❌ НЕПРАВИЛЬНО — несколько SKILL.md
skill-arch-init/SKILL.md   ← Claude.ai откажет!
skill-arch-plan/SKILL.md
```

### Требования Claude.ai к .skill файлам

| Требование | Что делать |
|------------|------------|
| Один SKILL.md | Только в корне skill-architect/ |
| Одна папка в корне ZIP | skill-architect/ содержит всё |
| ZIP формат | `zip -r`, НЕ `tar` |
| .skill расширение | НЕ .zip |

---

## Новые гены (G12-G16)

| Gene | Название | Правило |
|------|----------|---------|
| G12 | Protocol Boundary | Один протокол = один шаг workflow |
| G13 | Self-Contained | Протокол работает без чтения других |
| G14 | Explicit Handoff | NEXT: P0X-name (не "следующая фаза") |
| G15 | Router Pattern | Сложные workflows через роутер |
| G16 | Docs Separation | docs/ на верхнем уровне skill, НЕ внутри подпапок |

---

## Пошаговое обновление

### Шаг 1: Подготовка

```bash
# Создать рабочую директорию
mkdir -p /home/claude/skill-architect-v5
cd /home/claude/skill-architect-v5
```

### Шаг 2: Скопировать базу из v4.7.0

```bash
# Копировать reference и scripts
cp -r /mnt/skills/user/skill-architect/reference ./
cp -r /mnt/skills/user/skill-architect/scripts ./
cp /mnt/skills/user/skill-architect/README-skill-architect.md ./
cp /mnt/skills/user/skill-architect/MANIFEST.md ./
```

### Шаг 3: Создать новый SKILL.md (роутер)

SKILL.md должен содержать:
- Frontmatter с name: skill-architect, description с v5.0.0
- Таблицу Commands → Protocol
- Flow diagram с P01-P05
- ⛔ CRITICAL секцию
- Ссылки на protocols/

**Ключевые отличия от v4.7.0:**
- НЕ содержит детали протоколов
- ТОЛЬКО маршрутизация
- ~160 строк вместо 483

### Шаг 4: Создать protocols/

Каждый протокол — отдельный файл:

| Файл | Источник | Изменения |
|------|----------|-----------|
| P01-init.md | Новый | Сбор требований |
| P02-plan.md | P02 | + Design Razors ссылка |
| P03a-build.md | P03a | + Memory Budget ссылка |
| P03b-validate.md | P03b | + Quality Gates ссылка |
| P03c-docs.md | P03c | + ⛔ MANDATORY в начале |
| P04-deliver.md | P04 | + ZIP явно, + package.sh |
| P05-genes.md | genetic-audit | G01-G16 |

**В каждом протоколе:**
- Frontmatter (name, description)
- Ссылки: `[../reference/X.md](../reference/X.md)`
- NEXT: P0X-name (явный handoff)

### Шаг 5: Создать docs/v5.0.0/

Создать три документа:
- LOGIC-TREE-skill-architect-v5.0.0.md
- SCAN-skill-architect-v5.0.0.md
- DIFF-skill-architect-v5.0.0.md

### Шаг 6: Обновить CHANGELOG

Добавить секцию v5.0.0 в начало CHANGELOG-skill-architect.md

### Шаг 7: Упаковать

```bash
# Из родительской директории!
cd /home/claude
zip -r skill-architect-v5.0.0.skill skill-architect-v5/

# Переименовать папку внутри (если нужно)
# или изначально назвать skill-architect/

# Проверить
file skill-architect-v5.0.0.skill
# Должно быть: Zip archive data

unzip -l skill-architect-v5.0.0.skill | head -5
# Должно быть: skill-architect/ в начале всех путей
# Должен быть ТОЛЬКО ОДИН SKILL.md
```

### Шаг 8: Копировать в outputs

```bash
cp skill-architect-v5.0.0.skill /mnt/user-data/outputs/
cp -r skill-architect-v5/docs /mnt/user-data/outputs/skill-architect-docs-v5.0.0
```

---

## Метрики

| Метрика | v4.7.0 | v5.0.0 |
|---------|--------|--------|
| SKILL.md | 483 строк | ~160 строк |
| Files | 36 | 46 |
| Lines total | ~6900 | ~7400 |
| Protocols | 7 (в protocols/) | 7 (в protocols/) |
| Reference | 13 (в reference/) | 14 (в reference/) |
| Scripts | 7 (в scripts/) | 7 (в scripts/) |
| Genes | G01-G11 | G01-G16 |
| docs/ location | skill-architect/docs/ | skill-architect/docs/ |

---

## Проверочный чеклист

### Структура
- [ ] Одна папка skill-architect/ в корне ZIP
- [ ] Один SKILL.md в skill-architect/
- [ ] protocols/ содержит 7 файлов P01-P05
- [ ] reference/ содержит все 14 файлов
- [ ] scripts/ содержит все 7 файлов
- [ ] docs/ на уровне skill-architect/

### Формат
- [ ] `file X.skill` показывает "Zip archive data"
- [ ] `unzip -l X.skill` показывает skill-architect/ prefix
- [ ] Расширение .skill, НЕ .zip

### Содержание
- [ ] SKILL.md < 200 строк (только роутер)
- [ ] Каждый протокол имеет NEXT: P0X-name
- [ ] G16 в P05-genes.md
- [ ] docs/v5.0.0/ содержит LOGIC-TREE, SCAN, DIFF

---

## Типичные ошибки (из этой сессии)

| Ошибка | Симптом | Решение |
|--------|---------|---------|
| tar вместо zip | "POSIX tar archive" | `zip -r`, не `tar -cvf` |
| Несколько SKILL.md | "must contain exactly one SKILL.md" | Протоколы → P0X.md |
| Нет папки-обёртки | "multiple root directories" | `zip -r X.skill folder/` |
| docs внутри skill | Неудобно для пользователя | G16: docs/ на уровне skill |

---

## Установка v5.0.0

```bash
# Удалить старую версию
rm -rf /mnt/skills/user/skill-architect

# Распаковать новую
unzip skill-architect-v5.0.0.skill -d /mnt/skills/user/
```

---

*UPGRADE-GUIDE-skill-architect-v5.0.0.md*
