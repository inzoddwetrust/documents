# UPDATE NOTES: skill-architect v4.6.0

Заметки для следующего обновления. Собраны из независимого аудита + обсуждения.

---

## Дата аудита

2025-12-16

## Аудитор

Claude Opus 4.5 (независимая проверка, не через собственные скрипты)

---

## ✅ ПОДТВЕРЖДЕНО: Работает как задумано

| Аспект | Статус | Комментарий |
|--------|--------|-------------|
| Версии в footer'ах reference/ | Отключено в v4.4 | Сознательное решение — overhead без пользы |
| Сложность структуры | Принято | Meta-tool может быть сложнее продуктов |
| naming.md, packaging.md, evaluations.md | Справочники | Работают "by convention", не мёртвые |
| Дублирование Anchor/Genes | Контекстуализация | Разные применения одного концепта |
| Cognitive Razors 6 шт | Согласовано | Priority stack работает |

---

## 🔧 К ИСПРАВЛЕНИЮ

### 1. README-skill-architect.md

**Проблема:** Footer с версией устаревает

**Сейчас:**
```markdown
*skill-architect v4.0.0 "Unified"*
```

**Должно быть:**
```markdown
*skill-architect*
```

**Также:** Секция Installation упоминает v4.0.0 — убрать версию или заменить на "latest"

---

### 2. SKILL.md — Resources секция

**Проблема:** Не все reference файлы упомянуты явно

**Добавить в таблицу Resources:**
```markdown
| `reference/naming.md` | Naming conventions |
| `reference/packaging.md` | Package creation |
| `reference/evaluations.md` | Test scenarios |
```

---

### 3. validate.sh — опциональная проверка

**Идея:** Добавить warning если reference файл не упомянут нигде

```bash
# L7: Knowledge (optional)
for ref in "$SKILL_DIR"/reference/*.md; do
    name=$(basename "$ref")
    if ! grep -rq "$name" "$SKILL_DIR/SKILL.md" "$SKILL_DIR/protocols/" 2>/dev/null; then
        echo "  ⚠️ Orphan reference: $name"
        ((WARNINGS++))
    fi
done
```

**Статус:** LOW priority, можно не делать

---

## 📋 CHANGELOG для v4.6.0

```markdown
## [4.6.0] - YYYY-MM-DD "Documentation Cleanup"

### Changed
- README-skill-architect.md: Removed version from footer
- README-skill-architect.md: Installation section uses "latest" instead of specific version
- SKILL.md: Added missing reference files to Resources table

### Preserved (NEVER DEGRADE)
- All features from v4.5.0
- 6 cognitive razors + conflict resolution
- Protocol chain P01-P04
- Genes G01-G10 + G11-G15
- All 7 scripts
- All 12 reference files
```

---

## 🤔 ОТЛОЖЕНО / НЕ ДЕЛАЕМ

| Идея | Причина отказа |
|------|----------------|
| Синхронизация версий в footer'ах | Отключено в v4.4, не влияет на качество |
| Упрощение cognitive razors | Работают, согласованы |
| Удаление "мёртвых" файлов | Не мёртвые — справочники |
| Объединение reference файлов | Каждый имеет своё назначение |

---

## 💡 ИДЕИ НА БУДУЩЕЕ

1. **Self-checkup расширение** — проверять что все reference упомянуты
2. **Version-free mode** — официально задокументировать что footer-версии опциональны
3. **Minimal mode** — флаг `--minimal` для создания простых скиллов без full ecosystem

---

*Создано: 2025-12-16*
*Для: skill-architect v4.6.0*
