# skill-architect: План v8.1.0 → v8.2.0 "Lean Core"

## Date | Context

**Дата:** 2024-12-12  
**Автор:** Claude + User  
**Тип:** Major optimization + patch

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 (current: 240, target: ≤150) |
| README language | Russian |
| Frontmatter keys | ONLY: name, description, license, allowed-tools, compatibility, metadata |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

### Проблемы v8.1.0

1. **SKILL.md на пределе** — 240/300 строк (80% лимита)
2. **Frontmatter bug** — нет валидации ключей, скиллы падают при загрузке
3. **Избыточность** — 6,845 строк, ~40% это примеры которые LLM и так знает
4. **Нестабильность** — слишком много контекста для надёжной работы

### Что добавилось в 8.1.0 vs 8.0.3

| Файл | Строк | Назначение |
|------|-------|------------|
| reference/context-management.md | 214 | NEW: Context compaction strategy |
| reference/protocols/P09-full-audit.md | 234 | NEW: Comprehensive audit protocol |
| SKILL.md additions | +40 | "Protocol First" + "Iteration Principles" sections |
| **Итого прирост** | +542 | +8.6% |

### Цель v8.2.0

- **SKILL.md:** 240 → ≤150 строк (-40%)
- **Всего строк:** 6,845 → ~3,500 (-50%)
- **Принцип:** концепции > примеры, таблицы > prose

---

## 2. Проблемы / Задачи

| ID | Проблема | Severity | Решение |
|----|----------|----------|---------|
| BUG-001 | Frontmatter keys не валидируются | HIGH | PATCH-frontmatter |
| OPT-001 | engines.md 484 строки XML-шаблонов | MEDIUM | Сжать до ~80 |
| OPT-002 | templates.md 5 полных шаблонов | MEDIUM | Сжать до ~100 |
| OPT-003 | project-modules.md 10 YAML-схем | MEDIUM | Сжать до ~80 |
| OPT-004 | virtual-testing.md избыточные примеры | MEDIUM | Сжать до ~100 |
| OPT-005 | SKILL.md verbose sections | HIGH | Сжать до ~150 |
| OPT-006 | Дублирование context anchor в 4 файлах | LOW | SSOT в templates.md |
| **NEW-001** | **Нет проверки LLM-native redundancy** | **HIGH** | **Phase 2.5 + L7 + Gene** |
| **NEW-002** | **Все скиллы экосистемы раздуты** | **HIGH** | **Универсальный механизм аудита** |

---

## 3. План изменений

### ✅ Добавляем

| Что | Куда | Строк |
|-----|------|-------|
| Frontmatter constraints section | reference/templates.md | +15 |
| Frontmatter validation | scripts/validate-skill.sh | +10 |
| Platform constraints section | SKILL.md | +10 |
| **Phase 2.5: Knowledge Redundancy Check** | P09-full-audit.md | +30 |
| **Redundancy Gene Check** | genetic-audit.md | +25 |
| **L7: Knowledge Redundancy** | quality-checklist.md | +15 |

### ✏️ Изменяем (Aggressive Pruning)

| Файл | Было | Стало | Как сжимаем |
|------|------|-------|-------------|
| **SKILL.md** | 240 | 150 | Удалить verbose sections, compress tables |
| **engines.md** | 484 | 80 | Убрать XML-шаблоны, только таблицы + пресеты |
| **templates.md** | 431 | 120 | Убрать 5 полных шаблонов → 5 однострочных + frontmatter section |
| **project-modules.md** | 391 | 80 | Только required fields + validation rules |
| **virtual-testing.md** | 359 | 100 | Убрать примеры персон, только framework |
| **quality-checklist.md** | 349 | 120 | Сжать до essential checks |
| **workflow.md** | 329 | 80 | Только state machine + blocking |
| **packaging.md** | 293 | 100 | Убрать примеры, только rules |
| **docs-packaging.md** | 291 | 80 | Сжать шаблоны |
| **testing-framework.md** | 290 | 100 | Только L1-L6 specs, без примеров |
| **project-import.md** | 262 | 100 | Алгоритм без примеров |
| **project-mode.md** | 231 | 80 | Сжать workflow |
| **context-management.md** | 214 | 80 | Убрать примеры checkpoints |
| **P09-full-audit.md** | 234 | 100 | Сжать output format |
| **P05-validate.md** | 212 | 100 | Сжать чеклисты |
| **project-filters.md** | 199 | 60 | Только паттерны |
| **genetic-audit.md** | 187 | 80 | Сжать алгоритм |
| **P08-simulation.md** | 153 | 80 | Сжать |
| **ssot-check.md** | 149 | 60 | Сжать |
| **planning-document.md** | 145 | 60 | Только шаблон |
| **P07-closure.md** | 141 | 70 | Сжать |
| **self-diagnostic.md** | 141 | 60 | Сжать |
| **naming-convention.md** | 138 | 60 | + frontmatter keys |
| **Остальные P0X** | ~600 | 400 | Минимальное сжатие |

### 🗑️ Удаляем

| Что | Откуда | Причина |
|-----|--------|---------|
| XML-шаблоны INoT/Multi-Perspective | engines.md | LLM знает концепции |
| Полные template examples | templates.md | LLM умеет адаптировать |
| YAML-схемы с comments | project-modules.md | Оставляем только required |
| Persona examples | virtual-testing.md | LLM генерирует сам |
| Checkpoint examples | context-management.md | Достаточно формата |
| Verbose output format | P09-full-audit.md | Сжимаем |

### 🔒 Не трогаем

| Файл | Причина |
|------|---------|
| P00-router.md | Критичный роутинг |
| commands.md | SSOT для bash |
| scripts/*.sh | Работают, не ломать |
| README.md | User-facing |
| MANIFEST.md | Auto-generated |

---

## 4. Было → Стало

### Структура (без изменений)

```
skill-architect-v8.2.0/
├── SKILL.md              (240 → 150)
├── README.md             (211 → 200)
├── MANIFEST.md           (auto)
├── reference/
│   ├── engines.md        (484 → 80)
│   ├── templates.md      (431 → 120)
│   ├── project-modules.md(391 → 80)
│   ├── virtual-testing.md(359 → 100)
│   ├── ... (все сжаты)
│   └── protocols/
│       ├── P00-P09       (все сжаты)
└── scripts/              (без изменений + validation)
```

### Метрики

| Метрика | v8.1.0 | v8.2.0 | Δ |
|---------|--------|--------|---|
| SKILL.md | 240 | ≤150 | -40% |
| Всего строк | 6,845 | ~3,500 | -50% |
| Файлов | 41 | 41 | 0 |
| Запас SKILL.md | 20% | 50% | +30% |

---

## 5. Детальный план pruning

### 5.1 engines.md (484 → 80)

**Удаляем:**
- XML-шаблоны всех 5 engines (строки 35-70, 101-143, 174-206, 249-289, 324-368)
- Agent presets examples
- Security checklist
- Integration examples

**Оставляем:**
```markdown
# Engines

| Engine | Purpose | When | Result |
|--------|---------|------|--------|
| INoT | Agent debate | Critical decisions | +7.95% quality |
| Multi-Perspective | 4+ viewpoints | Coverage analysis | Completeness |
| Security | OWASP protection | User input | Safety |
| Validation | Self-check | Critical output | Confidence |
| Virtual Testing | Synthetic validation | Pre-release | Hypotheses |

## Presets
light: [Validation]
standard: [Multi-Perspective, Validation]
deep: [INoT, Multi-Perspective, Validation]
production: [Security, Validation]
maximum: [All]

## Integration
`<include engine="inot">` in Process section.

→ Concept knowledge: Claude knows INoT/debate, OWASP, self-check natively.
```

### 5.2 templates.md (431 → 120)

**Удаляем:**
- 5 полных шаблонов (строки 153-302)
- Customization guide verbose
- Hybrid templates examples

**Оставляем:**
```markdown
# Templates

## ⛔ Frontmatter Constraints (NEW)
ALLOWED keys ONLY: name, description, license, allowed-tools, compatibility, metadata
INVALID: version, ecosystem, type, author → PUT IN description

## Purpose Block (MANDATORY)
| serves | goal | method | success |

## Template Types
| Type | Keywords | Process |
|------|----------|---------|
| Analysis | analyze, assess | Gather → Analyze → Identify → Synthesize → Report |
| Investigation | research, find | Define → Search → Evaluate → Synthesize → Present |
| Content | create, write | Understand → Plan → Generate → Review → Finalize |
| Data | process, transform | Validate → Clean → Transform → Verify → Output |
| Code | build, implement | Requirements → Design → Implement → Test → Document |

## Context Anchor
`⚙️ [skill] · [state] · [status]`
`🟢 ~Xk | ~Yk 🟡`

## Token Counter
>100k: 🟢 | 50-100k: 🟡 | <50k: 🔴
```

### 5.3 project-modules.md (391 → 80)

**Удаляем:**
- Все optional fields
- Comments в YAML
- Empty module template

**Оставляем:**
```markdown
# Project Modules

## Required Fields

| Module | Required |
|--------|----------|
| core.yaml | name, tagline, stage, type, problem, solution |
| team.yaml | 1+ founder: name, role, background |
| product.yaml | name, type, status, value_proposition |
| market.yaml | target_customer (b2b/b2c), 1+ competitor |
| finances.yaml | revenue.model, funding.stage |
| tech.yaml | frontend OR backend stack |
| roadmap.yaml | vision.one_year, 1+ upcoming milestone |
| risks.yaml | 1+ risk: title, category, probability, impact |
| clients.yaml | 1+ segment OR key_account |
| decisions.yaml | id, title, date, status, context, decision |

## Validation
- Dates: YYYY-MM-DD
- Money: "$X" / "$XK" / "$XM"
- Percentages: "X%"
- URLs: https://
```

### 5.4 virtual-testing.md (359 → 100)

**Удаляем:**
- Persona examples (строки 105-142)
- Attack framework verbose
- Expert panel process details

**Оставляем:**
```markdown
# Virtual Testing

VT = filter for hypotheses, NOT facts.

## Architecture
INPUT → Context Detector → Personas (5-7) → Adversarial → Expert Panel → Score

## Personas
Required: 1 novice, 1 expert, 1 skeptic, 1 edge case
Template: Name, Role, Experience, Skepticism, Goal, Pain, Behavior

## Adversarial
For each claim: Attack → Probability × Impact → Mitigation
Risk: 🔴 Critical | 🟡 Warning | 🟢 Low

## Expert Panel
Experts: User (25%), Maintainer (20%), Skeptic (25%), Integrator (15%), Novice (15%)
Score: 1-10, weighted average

## Gate
≥70: PROCEED | 50-69: REVIEW | <50: REWORK | Any 🔴: BLOCK
```

### 5.5 SKILL.md (240 → 150)

**Удаляем:**
- "Protocol First, Always" section (38 строк) → move to P00
- "Iteration Principles" section → move to workflow.md
- Verbose examples in Context Anchor

**Добавляем:**
- Platform Constraints section (10 строк)

**Сжимаем:**
- Protocol Router table
- Resources tables

---

## 6. PATCH-frontmatter Integration

### 6.1 templates.md
```markdown
## ⛔ Frontmatter Constraints

**Allowed keys ONLY:**
- `name` (required)
- `description` (required) 
- `license`, `allowed-tools`, `compatibility`, `metadata`

**❌ INVALID (breaks upload):**
version, ecosystem, type, author → encode in description

**Example:**
```yaml
---
name: my-skill
description: "v1.0.0 | What it does. Triggers: a, b, c."
---
```
```

### 6.2 scripts/validate-skill.sh
```bash
# Add after frontmatter detection
ALLOWED_KEYS="name|description|license|allowed-tools|compatibility|metadata"
FRONTMATTER_KEYS=$(sed -n '2,/^---$/p' "$SKILL_FILE" | grep -E '^[a-z-]+:' | cut -d: -f1)

for key in $FRONTMATTER_KEYS; do
  if ! echo "$key" | grep -qE "^($ALLOWED_KEYS)$"; then
    echo "❌ Invalid frontmatter key: '$key'"
    ERRORS=$((ERRORS + 1))
  fi
done
```

### 6.3 naming-convention.md
```markdown
## Frontmatter Keys
Only valid: name, description, license, allowed-tools, compatibility, metadata
Version/ecosystem/type → encode in description field
```

### 6.4 P05-validate.md checklist
```markdown
□ Frontmatter contains only allowed keys
□ No LLM-native knowledge redundancy
```

### 6.6 P09-full-audit.md — NEW Phase 2.5: Knowledge Redundancy

```markdown
### Phase 2.5: Knowledge Redundancy Check

Identify content that LLM already knows natively.

**LLM-Native Categories (safe to remove/compress):**

| Category | Examples | Action |
|----------|----------|--------|
| General concepts | "what is API", "how REST works" | DELETE |
| Standard patterns | OWASP Top 10, design patterns, SOLID | COMPRESS to reference |
| Common formats | JSON/YAML/XML structure, markdown syntax | DELETE |
| Programming basics | loops, functions, error handling | DELETE |
| Industry standards | HTTP codes, SQL syntax, regex basics | DELETE |

**Skill-Specific (KEEP):**

| Category | Examples | Action |
|----------|----------|--------|
| Custom workflows | Skill-specific state machines | KEEP |
| Blocking points | Where to stop and wait | KEEP |
| Naming conventions | Skill-specific naming rules | KEEP |
| Integration rules | How skill connects to ecosystem | KEEP |
| Platform constraints | Claude.ai specific limits | KEEP |

**Redundancy Score:**
- 0-10% redundant: ✅ Lean
- 10-30% redundant: 🟡 Review  
- 30%+ redundant: 🔴 Prune required

**Check Questions:**
1. "Would Claude know this without the skill?" → YES = redundant
2. "Is this teaching LLM or configuring LLM?" → Teaching = redundant
3. "Is this a general concept or skill-specific rule?" → General = redundant
```

### 6.7 genetic-audit.md — NEW: Redundancy Gene

```markdown
## Redundancy Gene Check

When auditing skill inheritance, also check for knowledge bloat.

**Redundancy Markers:**

| Marker | Example | Verdict |
|--------|---------|---------|
| XML templates for known patterns | INoT debate structure | Redundant |
| Full examples of standard formats | Complete YAML schemas | Redundant |
| Explanations of concepts | "What is TAM/SAM/SOM" | Redundant |
| Step-by-step for obvious things | "How to create markdown" | Redundant |
| Persona examples | Full persona cards | Redundant |

**Lean Gene Pattern:**

```
BLOATED: "INoT is a technique where Agent_A presents analysis, 
Agent_B critiques, they iterate until consensus. Here's full XML template..."
(50 lines)

LEAN: "INoT: agent debate until consensus. Claude knows the pattern."
(1 line)
```

**Audit Output Addition:**
```
REDUNDANCY CHECK
────────────────
LLM-native content: X lines (Y%)
Skill-specific content: Z lines
Verdict: LEAN / REVIEW / PRUNE
Recommendation: [specific files to compress]
```
```

### 6.8 quality-checklist.md — NEW L7: Redundancy Check

```markdown
## L7: Knowledge Redundancy

| Check | Pass | Fail |
|-------|------|------|
| No general concept explanations | ✅ | Has "what is X" sections |
| No standard pattern tutorials | ✅ | Full XML/YAML templates for known patterns |
| No programming basics | ✅ | Explains loops, functions, etc |
| Tables over prose for rules | ✅ | Verbose paragraphs |
| References over examples | ✅ | Full examples of standard things |

**Quick Test:**
"Delete this section. Would skill still work?" 
→ YES = redundant, delete it
→ NO = keep it
```

### 6.5 SKILL.md
```markdown
## ⛔ PLATFORM CONSTRAINTS

| Constraint | Rule |
|------------|------|
| Frontmatter keys | ONLY: name, description, license, allowed-tools, compatibility, metadata |
| SKILL.md size | < 300 lines |
```

---

## 7. Чат-верификация

Проверка всех обсуждённых элементов:

| # | Item | Status |
|---|------|--------|
| 1 | PATCH-frontmatter применить | ✅ В плане |
| 2 | Сравнение v8.0.3 vs v8.1.0 | ✅ Выполнено |
| 3 | engines.md сжать | ✅ В плане: 484→80 |
| 4 | templates.md сжать | ✅ В плане: 431→120 |
| 5 | project-modules.md сжать | ✅ В плане: 391→80 |
| 6 | virtual-testing.md сжать | ✅ В плане: 359→100 |
| 7 | SKILL.md сжать до 150 | ✅ В плане |
| 8 | Убрать примеры, оставить концепции | ✅ Принцип pruning |
| 9 | Project mode сохранить | ✅ Не удаляем |
| 10 | Декомпозицию на скиллы НЕ делаем | ✅ Выбран вариант A |
| 11 | **Knowledge Redundancy Check в P09** | ✅ NEW: Phase 2.5 |
| 12 | **Redundancy Gene в genetic-audit** | ✅ NEW: Redundancy markers |
| 13 | **L7 Redundancy в quality-checklist** | ✅ NEW: Quick test |
| 14 | **Применять к ВСЕМ скиллам экосистемы** | ✅ Универсальный механизм |

**Verified: 14 items. Missing: none**

---

## 8. Риски

| Риск | Вероятность | Импакт | Митигация |
|------|-------------|--------|-----------|
| Потеря edge cases | Medium | Medium | Тестирование после pruning |
| LLM не поймёт сжатый формат | Low | High | Сохраняем ключевые таблицы |
| Сломаем scripts | Low | High | Scripts не трогаем (кроме validate) |
| Регрессия project mode | Medium | Medium | Отдельное тестирование |

---

## 9. Порядок выполнения

```
Phase 1: Core files
  ├── SKILL.md (сжать + platform constraints)
  ├── templates.md (сжать + frontmatter section)
  └── validate-skill.sh (добавить frontmatter validation)

Phase 2: Heavy files
  ├── engines.md
  ├── project-modules.md
  ├── virtual-testing.md
  └── quality-checklist.md

Phase 3: Medium files
  ├── workflow.md
  ├── packaging.md
  ├── docs-packaging.md
  ├── testing-framework.md
  └── context-management.md

Phase 4: Protocols
  ├── P05-validate.md (+ frontmatter check)
  ├── P09-full-audit.md
  └── Остальные P0X

Phase 5: Remaining
  ├── naming-convention.md
  ├── project-*.md files
  └── genetic-audit.md, ssot-check.md, etc.

Phase 6: Validation
  ├── Run validate-skill.sh
  ├── Test с invalid frontmatter
  ├── Test tool mode flow
  ├── Test project mode flow
  └── Generate MANIFEST
```

---

## 10. Чеклист подтверждения

- [ ] План понятен
- [ ] Aggressive pruning согласован
- [ ] PATCH-frontmatter интегрирован
- [ ] Риски приемлемы
- [ ] Порядок выполнения понятен
- [ ] Можно начинать

---

**Ожидаю подтверждение: "да", "yes", "go", "делай"**

---

*skill-architect_PLAN.md v1.0 | 2024-12-12*
