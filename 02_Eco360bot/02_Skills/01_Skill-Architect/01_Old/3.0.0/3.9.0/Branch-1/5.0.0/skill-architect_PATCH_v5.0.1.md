# Skill Architect: PATCH v5.0.0 → v5.0.1

## Дата: 2025-12-02 | Источник: NC Project refactor session

---

## Обнаруженные проблемы

### 1. ❌ Отсутствует триггер перечитывания reference/

**Проблема:** Claude не перечитывает reference/ файлы при каждом запросе, хотя это критично для корректной работы.

**Где:** SKILL.md

**Симптом:** При работе с NC Project Claude не прочитал project-mode.md в начале сессии.

**Решение:** Добавить в SKILL.md секцию:

```markdown
## ⚠️ MANDATORY: Reference Reading

**BEFORE any action, read relevant reference files:**

| Trigger | Read First |
|---------|------------|
| Any "project" keyword | `reference/project-mode.md` |
| "create skill" | `reference/templates.md` |
| "refactor" or "update" | `reference/planning-document.md` |
| Packaging | `reference/packaging.md` |

**Rule:** First tool call = `file_read` on reference file. Always.
```

---

### 2. ❌ Нет SSOT правил для Project Mode data/

**Проблема:** project-mode.md говорит "SSOT documents marked in respective modules", но НЕТ правил как избежать дублирования ВНУТРИ data/ модулей.

**Где:** reference/project-mode.md

**Симптом:** NC Project имел формулу коллекции в 7 местах, японские концепции в 5 местах.

**Решение:** Добавить в project-mode.md:

```markdown
## SSOT Rules for data/

### Anti-Duplication Principle

Each fact exists in ONE module only. Other modules REFERENCE it.

| Data Type | SSOT Location | Other modules use |
|-----------|---------------|-------------------|
| Core formula/methodology | `core.yaml` | `(→ core.yaml)` |
| Definitions/terminology | `glossary.md` | `(→ glossary.md)` |
| Examples/instances | Domain module | `(→ domain.yaml)` |
| Metrics/numbers | Source module | `(→ source.yaml)` |

### Reference Syntax

```markdown
Japanese concepts like wabi-sabi (→ glossary.md) influence our design.
```

### Audit Checklist

Before packaging Project skill:
```
□ Search for duplicated definitions across modules
□ Search for repeated examples/instances
□ Search for copy-pasted tables
□ Each fact traceable to ONE source
```

### Common Violations

| Violation | Example | Fix |
|-----------|---------|-----|
| Formula in multiple files | Collection formula in core, positioning, formula, architecture | Keep in core.yaml, reference elsewhere |
| Definitions everywhere | Wabi-sabi defined in 5 files | Keep in glossary.md only |
| Examples duplicated | Sakura Mono details in 4 files | Keep in families.yaml, reference elsewhere |
```

---

### 3. ❌ Нет REFACTOR mode для Project

**Проблема:** project-mode.md имеет CREATE/IMPORT/UPDATE/GENERATE, но нет REFACTOR для глубокой реструктуризации.

**Где:** reference/project-mode.md

**Симптом:** При рефакторинге NC Project пришлось импровизировать процесс.

**Решение:** Добавить в project-mode.md:

```markdown
### REFACTOR (Project Mode)

Trigger: `refactor` + project skill attachment

**When to use:**
- Duplication discovered across modules
- Structure needs reorganization
- SSOT violations found

**Process:**
1. **Audit** — Analyze all modules for:
   - Duplicated content
   - Missing cross-references
   - Verbose sections that can be compressed
   - Secondary data derivable from primary
2. **Plan** — Create Planning Document with:
   - SSOT architecture diagram
   - KEEP/REMOVE/ADD tables
   - Line count: было → стало
3. **Confirm** — Wait for explicit confirmation
4. **Execute** — Apply changes
5. **Validate** — Check SSOT integrity
6. **Deliver** — Package + report savings

**Output format:**
```
REFACTOR COMPLETE: [project-name] v[old] → v[new]

Savings:
├── Lines: 3,418 → 2,500 (-27%)
├── Duplicates removed: 15
└── SSOT sources established: 4

SSOT Architecture:
├── core.yaml → Formula, mission, values
├── glossary.md → All definitions
├── families.yaml → All examples
└── [other sources]
```
```

---

### 4. ❌ Audit script не работает для Project Mode

**Проблема:** `scripts/audit-skill.sh` проверяет Tool Mode структуру (reference/), но не data/.

**Где:** scripts/

**Решение:** Создать `scripts/audit-project.sh`:

```bash
#!/bin/bash
# audit-project.sh — Deep audit for Project Mode skills

PROJECT_DIR="$1"

if [ -z "$PROJECT_DIR" ]; then
    echo "Usage: audit-project.sh /path/to/project-skill"
    exit 1
fi

echo "=== PROJECT AUDIT: $PROJECT_DIR ==="

# 1. Structure check
echo -e "\n[1] Structure:"
if [ -d "$PROJECT_DIR/data" ]; then
    echo "✓ data/ exists"
    find "$PROJECT_DIR/data" -name "*.yaml" -o -name "*.md" | wc -l | xargs echo "  Files:"
else
    echo "✗ data/ missing"
fi

# 2. SSOT violations (duplicate content)
echo -e "\n[2] SSOT Check (potential duplicates):"

# Check for repeated phrases across files
COMMON_DUPLICATES=(
    "formula"
    "wabi-sabi"
    "mono no aware"
    "География"
    "Культура"
)

for phrase in "${COMMON_DUPLICATES[@]}"; do
    count=$(grep -r -l "$phrase" "$PROJECT_DIR/data" 2>/dev/null | wc -l)
    if [ "$count" -gt 1 ]; then
        echo "⚠ '$phrase' found in $count files"
    fi
done

# 3. Line counts
echo -e "\n[3] Line Counts:"
find "$PROJECT_DIR/data" -type f \( -name "*.yaml" -o -name "*.md" \) -exec wc -l {} \; | sort -n

# 4. Total size
echo -e "\n[4] Total:"
find "$PROJECT_DIR/data" -type f \( -name "*.yaml" -o -name "*.md" \) -exec cat {} \; | wc -l | xargs echo "Lines:"
du -sh "$PROJECT_DIR/data" | cut -f1 | xargs echo "Size:"

echo -e "\n=== AUDIT COMPLETE ==="
```

---

## Summary: Патч v5.0.1

| File | Change |
|------|--------|
| SKILL.md | + "MANDATORY: Reference Reading" section |
| reference/project-mode.md | + SSOT Rules, + REFACTOR mode |
| scripts/audit-project.sh | NEW file |

**Version bump:** 5.0.0 → 5.0.1 (PATCH — bug fixes, no breaking changes)

---

## Changelog Entry

```markdown
### v5.0.1 (2025-12-02)

**Fixed:**
- Added mandatory reference reading trigger to SKILL.md
- Added SSOT rules for Project Mode data/ modules
- Added REFACTOR workflow for Project Mode

**Added:**
- `scripts/audit-project.sh` for Project Mode auditing
- Reference syntax `(→ source.md)` for cross-module links

**Source:** NC Project refactor session — discovered 27% duplication in production project skill
```

---

*Patch document for skill-architect v5.0.1*
*Ready for integration into next release*
