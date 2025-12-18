# Skill Architecture Reference

Полный сборник рабочих механик, паттернов и архитектурных решений для создания AI-скиллов.

**Дата компиляции:** 2025-12-13

---

## Содержание

1. [Философия и принципы](#1-философия-и-принципы)
2. [Архитектура скилла](#2-архитектура-скилла)
3. [Anchor System](#3-anchor-system)
4. [Protocol Architecture](#4-protocol-architecture)
5. [Validation System](#5-validation-system)
6. [Genetic Audit](#6-genetic-audit)
7. [NEVER DEGRADE](#7-never-degrade)
8. [Planning & Verification](#8-planning--verification)
9. [INoT Engine](#9-inot-engine)
10. [Documentation System](#10-documentation-system)
11. [Packaging & Delivery](#11-packaging--delivery)
12. [Recovery Mechanisms](#12-recovery-mechanisms)
13. [Anti-Patterns](#13-anti-patterns)
14. [Templates](#14-templates)

---

# 1. Философия и принципы

## 1.1 Core Philosophy

**Скилл — это расширение возможностей Claude через структурированные инструкции.**

Ключевые осознания:
- Claude не имеет памяти между ответами → нужны anchor'ы
- Контекст ограничен → нужна компактность
- Claude склонен к дрифту → нужны blocking points
- Фичи теряются при обновлениях → нужен NEVER DEGRADE

## 1.2 Clean Skill Principles

| Принцип | Правило | Пример |
|---------|---------|--------|
| **Density** | Каждая строка несёт смысл | ❌ "Sure! I'll help you" |
| **No fluff** | Нет disclaimers, очевидностей | ❌ "Here's a simple example" |
| **N/2 rule** | Запросили N слов → выдай N/2 | Просили 500 → пиши 250 |
| **Show > explain** | Примеры лучше описаний | ✅ Code sample vs. paragraph |
| **Specificity** | Конкретные triggers > абстрактные | ✅ "create skill" vs "help me" |

## 1.3 Архитектурные аксиомы

```
1. SKILL.md — единственный entry point
2. Всё что Claude должен делать — должно быть в SKILL.md или references
3. Anchor в конце каждого ответа — обязателен
4. Blocking points (⛔) предотвращают преждевременные действия
5. Validation перед delivery — обязательна
```

---

# 2. Архитектура скилла

## 2.1 Структура файлов

### Минимальная (простые скиллы)

```
skill-name/
├── SKILL.md          # < 300 lines
└── README-{name}.md  # User documentation
```

### Стандартная (средняя сложность)

```
skill-name/
├── SKILL.md              # 200-300 lines
├── README-{name}.md
├── MANIFEST.md           # If reference/ exists
└── reference/
    └── *.md              # Reusable components
```

### Полная (сложные скиллы)

```
skill-name/
├── SKILL.md              # < 500 lines
├── README-{name}.md
├── CHANGELOG-{name}.md
├── MANIFEST.md
├── protocols/            # P00-P04
│   ├── P00-router.md
│   ├── P01-init.md
│   ├── P02-plan.md
│   ├── P03-build.md
│   └── P04-deliver.md
├── reference/
│   └── *.md
├── scripts/
│   └── *.sh
└── docs/vX.Y.Z/
    ├── DIFF-*.md
    ├── LOGIC-TREE-*.md
    └── SCAN-*.md
```

## 2.2 SKILL.md Anatomy

```markdown
---
name: kebab-case-name
description: "vX.Y.Z | One-line purpose. Triggers: trigger1, trigger2."
---

# Skill Name vX.Y.Z

[Purpose Table or one-liner]

---

## Commands / Triggers
[Table of activation triggers]

---

## Flow
[Visual flow with → arrows and ⛔ blocking points]

---

## Process / Phases
[Step-by-step instructions]

---

## Rules
[Critical constraints]

---

## Anchor Format
[How to end responses]

---

*vX.Y.Z | Tagline*
```

## 2.3 Purpose Table (v10/v11)

Компактный способ описать назначение:

```markdown
| Field | Value |
|-------|-------|
| Serves | Target users |
| Goal | What it achieves |
| Method | How it works |
| Success | Measurable outcome |
```

## 2.4 Frontmatter Requirements

```yaml
---
name: kebab-case-name           # Required
description: "vX.Y.Z | ..."     # Required, must include version and triggers
---
```

---

# 3. Anchor System

## 3.1 Проблема

**Claude не имеет памяти между ответами.** Каждый ответ начинается с нуля. Без anchor'а Claude теряет контекст: где он в workflow, что делал, что делать дальше.

## 3.2 Формат Anchor

```
⚙️ {skill-name} v{X.Y.Z} · {protocol} · {status}
{session} | NEXT: {explicit next action}
```

### Компоненты

| Компонент | Описание | Примеры |
|-----------|----------|---------|
| Skill ID | Имя + версия | `skill-architect v4.0.0` |
| Protocol | Текущий протокол | `P01-init`, `P02-plan`, `—` |
| Status | Состояние | `activating`, `⛔ waiting`, `✅ confirmed` |
| Session | Индикатор контекста | 🟢 🟡 🔴 |
| NEXT | Следующее действие | `create Planning Document` |

### Session Indicator

| Индикатор | Сообщений | Значение |
|-----------|-----------|----------|
| 🟢 | < 5 | Свежий контекст |
| 🟡 | 5-15 | Средняя сессия |
| 🔴 | > 15 | Длинная сессия, риск потери контекста |

## 3.3 NEXT — критический компонент

**NEXT — это self-instruction.** Claude читает свой предыдущий anchor и понимает что делать.

### Правила NEXT

1. Должен быть explicit action
2. Должен быть achievable в одном ответе
3. Если ожидание — включить условие

### Примеры NEXT

```
NEXT: collect config (purpose, triggers)
NEXT: create Planning Document
NEXT: user confirms → P03-build
NEXT: validate → if pass → Diff Report
NEXT: package and deliver
NEXT: END
```

### Anti-patterns

```
❌ NEXT: continue
❌ NEXT: proceed
❌ NEXT: (empty)
✅ NEXT: create SKILL.md with purpose table and flow diagram
```

---

# 4. Protocol Architecture

## 4.1 Зачем протоколы

Протоколы решают проблему:
- Claude не держит длинные инструкции в контексте
- Разбиение на шаги уменьшает когнитивную нагрузку
- Каждый протокол можно прочитать отдельно

## 4.2 Protocol Chain

```
P00-router → P01-init → P02-plan ⛔ → P03-build → P04-deliver ⛔ → END
```

## 4.3 PRE/DO/EXIT Structure (v10)

Каждый протокол имеет три секции:

```markdown
# P0X: Name

## PRE-ACTION
- [ ] Checklist что должно быть готово
- [ ] Условия входа

## DO
1. Конкретные действия
2. Что создать/проверить
3. Какой output

## EXIT
- [ ] Checklist выхода
- [ ] Условия перехода

**NEXT:** → P0Y (следующий протокол)
```

## 4.4 Protocol Descriptions

### P00-router

```markdown
State machine для определения следующего действия.

Входные сигналы → Protocol mapping:
- "create skill" → P01
- "update skill" → P01
- User confirms → next protocol
- Context lost → Recovery
```

### P01-init

```markdown
Активация и сбор конфигурации.

DO:
1. Определить mode (create/update/refactor)
2. Собрать config: purpose, triggers
3. Для UPDATE: snapshot baseline
4. Для UPDATE: проверить retrospective (1-3 версии)

EXIT → P02-plan
```

### P02-plan ⛔

```markdown
Создание Planning Document + Chat Verification.

⛔ BLOCKING — не переходить без explicit confirmation

DO:
1. Создать Planning Document (KEEP/REMOVE/ADD)
2. Chat Verification — сканировать весь чат
3. NEVER DEGRADE check
4. Представить план
5. ЖДАТЬ подтверждения

Valid confirmations: да, yes, ок, подтверждаю, го, confirm
Invalid: угу, ладно, maybe, looks good

EXIT → P03-build (only after confirmation)
```

### P03-build

```markdown
Создание файлов и валидация.

DO:
1. PRE-BUILD Checkpoint — перечитать план!
2. Создать файлы по плану
3. Применить genes (G01-G07)
4. Запустить validation (L1-L6)
5. NEVER DEGRADE check

EXIT → P04-deliver
```

### P04-deliver ⛔

```markdown
Финальная доставка с Diff Report.

⛔ BLOCKING — не паковать без confirmation

DO:
1. Создать Diff Report
2. Представить для подтверждения
3. После confirmation:
   - Generate MANIFEST
   - Create .skill package
   - Copy to /mnt/user-data/outputs/
4. Optional: suggest test-architect

EXIT → END
```

## 4.5 Blocking Points ⛔

**Blocking point** — место где Claude ОБЯЗАН остановиться и ждать explicit confirmation.

Зачем:
- Предотвращает преждевременные действия
- Даёт пользователю контроль
- Уменьшает риск ошибок

Где использовать:
- После Planning Document (P02)
- После Diff Report (P04)
- Перед любым destructive action

---

# 5. Validation System

## 5.1 Quality Gates L1-L10

| Level | Name | Focus | Required |
|-------|------|-------|----------|
| L1 | Structure | Files exist | ✅ |
| L2 | Content | Frontmatter valid | ✅ |
| L3 | Logic | Flow coherent | ✅ |
| L4 | Naming | Conventions | ✅ |
| L5 | Integration | References work | ✅ |
| L6 | Testing | Scripts pass | ✅ |
| L7 | Knowledge | No redundancy | ⚠️ |
| L8 | Version | SemVer correct | ⚠️ |
| L9 | Documentation | README complete | ⚠️ |
| L10 | Registry | Features tracked | ⚠️ |

✅ = Required for release
⚠️ = Recommended

## 5.2 L1: Structure

```bash
[ -f "SKILL.md" ] || FAIL
[ -f README*.md ] || FAIL
[ -d reference ] && [ ! -f MANIFEST.md ] && WARN
```

## 5.3 L2: Content

```bash
grep -q "^name:" SKILL.md || FAIL
grep -q "^description:" SKILL.md || FAIL
grep -Eq "v[0-9]+\.[0-9]+\.[0-9]+" SKILL.md || FAIL
[ $(wc -l < SKILL.md) -lt 500 ] || FAIL
```

## 5.4 L3: Logic

- [ ] Clear entry point
- [ ] Flow diagram with →
- [ ] Commands/triggers defined
- [ ] Exit conditions clear

## 5.5 L4: Naming

| Item | Convention |
|------|------------|
| Skill name | kebab-case |
| Files | UPPER.md or kebab-case.md |
| Scripts | kebab-case.sh |
| Version | vX.Y.Z |

## 5.6 L5: Integration

```bash
for ref in $(grep -oE "reference/[a-z-]+\.md" SKILL.md); do
  [ -f "$ref" ] || FAIL
done
```

## 5.7 L6: Testing

```bash
for script in scripts/*.sh; do
  bash -n "$script" || FAIL  # Syntax check
done
```

---

# 6. Genetic Audit

## 6.1 Концепция

**Genes** — обязательные паттерны которые должен наследовать каждый скилл. Если gene отсутствует — скилл не полностью функционален.

## 6.2 Required Genes (все скиллы)

| Gene | Check | Validation |
|------|-------|------------|
| G01 | Frontmatter | `name:` + `description:` |
| G02 | Version | vX.Y.Z в description |
| G03 | Purpose | Секция purpose или table |
| G04 | Flow | Диаграмма с → |
| G05 | Commands | Таблица triggers |
| G06 | Anchor | NEXT: в формате |
| G07 | Session | 🟢🟡🔴 indicator |

## 6.3 Conditional Genes

| Gene | Условие | Check |
|------|---------|-------|
| G08 | Есть workflow | ⛔ blocking points |
| G09 | Есть reference/ | MANIFEST.md |
| G10 | Нужна автоматизация | scripts/ |

## 6.4 Self-Audit Genes (skill-architect)

| Gene | Check |
|------|-------|
| G11 | NEVER DEGRADE validator |
| G12 | Protocol architecture |
| G13 | Quality Gates L1-L10 |
| G14 | INoT Engine |
| G15 | Chat Verification |

## 6.5 Validation Script

```bash
#!/bin/bash
# genetic-audit.sh

ERRORS=0

# G01
grep -q "^name:" SKILL.md && grep -q "^description:" SKILL.md || ((ERRORS++))

# G02
grep -Eq "v[0-9]+\.[0-9]+\.[0-9]+" SKILL.md || ((ERRORS++))

# G03
grep -qi "purpose\|serves\|goal" SKILL.md || ((ERRORS++))

# G04
grep -q "→" SKILL.md || echo "WARN: no flow"

# G05
grep -qi "command\|trigger" SKILL.md || ((ERRORS++))

# G06
grep -q "NEXT:" SKILL.md || ((ERRORS++))

# G07
grep -qE "🟢|🟡|🔴" SKILL.md || echo "WARN: no session"

[ $ERRORS -eq 0 ] && echo "PASS" || echo "FAIL: $ERRORS"
```

---

# 7. NEVER DEGRADE

## 7.1 Принцип

**При обновлении скилла количество фич не должно уменьшаться.**

```
features(v_new) >= features(v_old)
```

## 7.2 Workflow

```
1. Snapshot baseline: cp -r old/ backup/
2. Count baseline features: N
3. Make changes
4. Count new features: M
5. Assert M >= N
6. If M < N → restore missing or document reason
```

## 7.3 NEVER DEGRADE Table

Формат для Planning Document:

```markdown
| ID | Feature | v_old | v_new | Status |
|----|---------|-------|-------|--------|
| F01 | Frontmatter | ✅ | ✅ | ✅ KEEP |
| F02 | Flow diagram | ✅ | ✅ | ✅ KEEP |
| F03 | New anchor | ❌ | ✅ | ➕ ADD |
| F04 | Old feature | ✅ | ❌ | ⚠️ REMOVE (reason) |
```

Статусы:
- ✅ KEEP — сохраняем
- ➕ ADD — добавляем
- ⚠️ REMOVE — удаляем (обязательно с reason!)
- 📋 BACKLOG — откладываем

## 7.4 Validation

```bash
#!/bin/bash
# validate.sh --degrade

BASELINE_FEATURES=$(grep -c "^## " "$BASELINE/SKILL.md")
CURRENT_FEATURES=$(grep -c "^## " "$CURRENT/SKILL.md")

if [ "$CURRENT_FEATURES" -ge "$BASELINE_FEATURES" ]; then
  echo "✅ PASS: $CURRENT_FEATURES >= $BASELINE_FEATURES"
else
  echo "❌ FAIL: Lost $((BASELINE_FEATURES - CURRENT_FEATURES)) features"
  exit 1
fi
```

---

# 8. Planning & Verification

## 8.1 Planning Document

Создаётся ПЕРЕД любыми изменениями.

### Структура

```markdown
# Planning Document: {skill-name} v{version}

## Meta
| Field | Value |
|-------|-------|
| Date | YYYY-MM-DD |
| Mode | CREATE / UPDATE / REFACTOR |
| Baseline | vX.Y.Z |

## KEEP (from baseline)
| Item | Reason |
|------|--------|
| Feature X | Still needed |

## REMOVE
| Item | Reason |
|------|--------|
| Feature Y | Replaced by Z |

## ADD
| Item | Source |
|------|--------|
| Feature Z | User request |

## Architecture
[File structure]

## Chat Verification
[See below]

## NEVER DEGRADE Check
| Metric | Baseline | Planned |
|--------|----------|---------|
| Features | N | M |
```

## 8.2 Chat Verification

**CRITICAL:** Сканировать ВЕСЬ чат чтобы ничего не потерять.

### Процесс

```
1. Прочитать все сообщения
2. Извлечь все упомянутые items:
   - Requested features
   - Discussed changes
   - Questions answered
   - Decisions made
3. Для каждого item проверить:
   - Есть в KEEP?
   - Есть в ADD?
   - Есть в REMOVE?
4. Отчёт: "Verified: N items. Missing: [list or 'none']"
```

### Формат отчёта

```markdown
## Chat Verification

Scanned: 15 messages

### Items Found
1. User wants triggers in Russian
2. Should support refactor command
3. Need validation script

### Verification
| Item | In Plan? |
|------|----------|
| Russian triggers | ✅ ADD |
| Refactor command | ✅ KEEP |
| Validation script | ✅ ADD |

**Result:** 3/3 verified. Missing: none
```

## 8.3 PRE-BUILD Checkpoint

**Перечитать план ПЕРЕД началом build!**

Зачем: context drift. После web search, длинных обсуждений Claude может забыть план.

```markdown
## PRE-BUILD Checkpoint

Re-read Planning Document: ✅

Confirmed:
- [ ] KEEP list: N items
- [ ] REMOVE list: N items  
- [ ] ADD list: N items
- [ ] Architecture: understood

Ready to build.
```

## 8.4 UPDATE Requirements

Для UPDATE и REFACTOR требуется **retrospective**:

- Minimum: 1 предыдущая версия analysis
- Ideal: 2-3 версии history

Это предотвращает потерю рабочих механизмов.

---

# 9. INoT Engine

## 9.1 Концепция

**INoT (Inner Negotiation of Thoughts)** — виртуальные дебаты агентов внутри одного LLM call.

Agent_A предлагает → Agent_B критикует → итерации до consensus.

## 9.2 Результаты исследований

| Metric | Improvement |
|--------|-------------|
| Quality | +7.95% |
| Tokens | -58.3% vs multi-turn |

## 9.3 Когда использовать

- Сложные решения с multiple factors
- Критический анализ
- Валидация перед important outputs
- Архитектурные решения
- Уменьшение hallucinations

## 9.4 Template

```xml
<INoT-Engine task="{TASK}">

<Agents>
  <Agent name="Analyst" focus="systematic_analysis">
    Analyzes facts, builds logical chains
  </Agent>
  <Agent name="Critic" focus="critical_review">
    Finds weaknesses, checks assumptions
  </Agent>
</Agents>

<Config>
  max_rounds = 3
  consensus_threshold = "semantic_agreement"
</Config>

<Process>
  FOR round = 1 TO max_rounds:
    analysis_A = Analyst.analyze(task)
    critique = Critic.critique(analysis_A)
    refined = Analyst.refine(analysis_A, critique)
    
    IF consensus_reached:
      RETURN synthesize(refined)
</Process>

<Output>
  <Conclusion>{result}</Conclusion>
  <Confidence>{HIGH|MEDIUM|LOW}</Confidence>
  <KeyDebatePoints>{resolved_disagreements}</KeyDebatePoints>
</Output>

</INoT-Engine>
```

## 9.5 Agent Presets

| Context | Agents |
|---------|--------|
| Business | Optimist, Skeptic |
| Technical | Architect, Security |
| Content | Author, Editor |
| Decision | Advocate, Devil's Advocate |
| Skill creation | Designer, Validator |

## 9.6 Пример использования

```xml
<INoT-Engine task="Should we remove feature X in update?">
  <Agent name="Analyst">
    Feature X has 2 uses in chat history.
    Removal saves 15 lines.
  </Agent>
  <Agent name="Critic">
    User mentioned X explicitly.
    NEVER DEGRADE principle applies.
    Risk: functionality loss.
  </Agent>
  <Conclusion>
    KEEP feature X. Document reason.
  </Conclusion>
  <Confidence>HIGH</Confidence>
</INoT-Engine>
```

## 9.7 Когда НЕ использовать

- Simple factual lookups
- Straightforward file operations
- User wants quick answer
- Mechanical tasks (copy, format)

---

# 10. Documentation System

## 10.1 Структура docs/

```
docs/vX.Y.Z/
├── DIFF-{name}-vX.Y.Z.md       # Что изменилось
├── LOGIC-TREE-{name}-vX.Y.Z.md # Decision tree для PO
└── SCAN-{name}-vX.Y.Z.md       # File scan report
```

## 10.2 DIFF Report

```markdown
# Diff Report: {skill-name}

## Version
vX.Y.Z → vX.Y.Z

## Metrics
| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Files | N | N | ±N |
| Lines | N | N | ±N |
| Features | N | N | ±N |

## Added
| Item | Lines | Reason |
|------|-------|--------|

## Removed
| Item | Lines | Reason |
|------|-------|--------|

## Preserved
- Item 1
- Item 2

## Plan Deviation
[Any differences from plan, or "None"]

## NEVER DEGRADE
✅ PASS / ❌ FAIL

## Validation
L1-L6: ✅ PASS
```

## 10.3 LOGIC-TREE

Decision tree для Product Owner review:

```markdown
# LOGIC-TREE: {skill-name} vX.Y.Z

## 1. Activation Logic
```
User message received
    │
    ├─ Contains "trigger1"?
    │   └─ YES → Action 1
    │
    └─ Contains "trigger2"?
        └─ YES → Action 2
```

## 2. Main Flow
```
Step 1
    │
    ├─ Condition A?
    │   └─ YES → Path A
    │
    └─ Condition B?
        └─ YES → Path B
```
```

## 10.4 SCAN Report

```markdown
# SCAN: {skill-name} vX.Y.Z

## Build Info
| Field | Value |
|-------|-------|
| Version | vX.Y.Z |
| Files | N |
| Lines | N |

## File Inventory
| File | Lines | Purpose |
|------|-------|---------|
| SKILL.md | N | Main entry |
```

## 10.5 MANIFEST.md

Required если есть reference/ или scripts/:

```markdown
# MANIFEST: {skill-name}

## Build Info
| Field | Value |
|-------|-------|
| Version | vX.Y.Z |
| Build Date | YYYY-MM-DD |
| Files | N |
| Lines | N |

## Files
| File | Lines | Description |
|------|-------|-------------|

## Integrity
Total lines: N

## Changelog
### vX.Y.Z (date)
- Added: ...
- Changed: ...
```

---

# 11. Packaging & Delivery

## 11.1 Package Format

```
skill-name-vX.Y.Z.skill
```

Это ZIP архив с содержимым скилла.

## 11.2 Packaging Commands

```bash
# 1. Validate
bash scripts/validate.sh /path/to/skill

# 2. Generate MANIFEST
bash scripts/generate-manifest.sh /path/to/skill X.Y.Z

# 3. Create package
cd /path/to
zip -r skill-name-vX.Y.Z.skill skill-name/

# 4. Deliver
cp skill-name-vX.Y.Z.skill /mnt/user-data/outputs/
```

## 11.3 Delivery Checklist

- [ ] L1-L6 validation passed
- [ ] NEVER DEGRADE check passed
- [ ] Genetic audit passed
- [ ] Diff Report confirmed
- [ ] MANIFEST generated
- [ ] Package created
- [ ] Copied to outputs

## 11.4 Post-Delivery Message

```markdown
✅ {skill-name} v{X.Y.Z} delivered.

📦 Package: skill-name-vX.Y.Z.skill
📁 Location: /mnt/user-data/outputs/

Contents:
- SKILL.md (N lines)
- README-{name}.md (N lines)
- N reference files
- N scripts
```

---

# 12. Recovery Mechanisms

## 12.1 Context Loss Recovery

Если контекст потерян mid-conversation:

```
1. Найти последний anchor в чате
2. Прочитать: protocol, status, NEXT
3. Продолжить с NEXT instruction
```

## 12.2 Recovery Protocol

```markdown
🔴 Context lost?
    │
    ├─ Search conversation for last anchor
    │   Format: ⚙️ {skill} v{X} · {protocol} · {status}
    │
    ├─ Found?
    │   ├─ YES → Extract NEXT → Execute
    │   └─ NO → Start from P01
    │
    └─ Inform user of recovery
```

## 12.3 Session Management

При 🔴 (длинная сессия):
- Рассмотреть summarization
- Checkpoint critical state
- Warn user о риске потери контекста

---

# 13. Anti-Patterns

## 13.1 Architecture Anti-Patterns

| ❌ Anti-Pattern | ✅ Solution |
|-----------------|-------------|
| Monolith >500 lines | Split to protocols + references |
| Too many files (70+) | Consolidate to ~30 files |
| No entry point | Clear activation section |
| Inline everything | Extract to references |

## 13.2 Anchor Anti-Patterns

| ❌ Anti-Pattern | ✅ Solution |
|-----------------|-------------|
| No anchor | Add anchor to every response |
| Vague NEXT: "continue" | Explicit: "create SKILL.md" |
| No session indicator | Add 🟢🟡🔴 |
| Missing protocol | Include current protocol |

## 13.3 Process Anti-Patterns

| ❌ Anti-Pattern | ✅ Solution |
|-----------------|-------------|
| Skip planning | Always create Planning Document |
| No chat verification | Scan entire chat |
| Build before confirm | Wait for explicit confirmation |
| Skip validation | Run L1-L6 before delivery |
| Remove without reason | Document every removal |

## 13.4 Naming Anti-Patterns

| ❌ Anti-Pattern | ✅ Solution |
|-----------------|-------------|
| MySkill.md | my-skill |
| README.md | README-my-skill.md |
| v4 | v4.0.0 |
| skill.md | SKILL.md |

---

# 14. Templates

## 14.1 SKILL.md Template (Standard)

```markdown
---
name: {skill-name}
description: "v{X.Y.Z} | {purpose}. Triggers: {triggers}."
---

# {Skill Name} v{X.Y.Z}

| Field | Value |
|-------|-------|
| Serves | {users} |
| Goal | {goal} |
| Method | {method} |
| Success | {metric} |

---

## Commands

| Command | Action |
|---------|--------|
| `{trigger}` | {action} |

---

## Flow

```
{step1} → {step2} ⛔ → {step3}
```

---

## Process

### 1. {Step}
{description}

### 2. {Step}
{description}

---

## Rules

| Rule | Requirement |
|------|-------------|
| {rule} | {req} |

---

## Anchor Format

```
⚙️ {name} v{X.Y.Z} · {phase} · {status}
{session} | NEXT: {action}
```

---

*v{X.Y.Z} | {tagline}*
```

## 14.2 README Template

```markdown
# {Skill Name}

{One paragraph description.}

## Installation

1. Download `{name}-v{X.Y.Z}.skill`
2. Upload to Claude Projects or `/mnt/skills/user/`
3. Trigger with: `{trigger}`

## Usage

### Basic
```
User: {trigger}
Claude: {response}
```

### Commands
| Command | Description |
|---------|-------------|
| `{trigger}` | {desc} |

## Examples

### Example 1: {Use Case}
```
User: {input}
Claude: {output}
```

## Version History
| Version | Date | Changes |
|---------|------|---------|
| v{X.Y.Z} | {date} | {changes} |

---
*Created by skill-architect*
```

## 14.3 Planning Document Template

```markdown
# Planning Document: {skill-name} v{version}

## Meta
| Field | Value |
|-------|-------|
| Date | {date} |
| Mode | CREATE / UPDATE / REFACTOR |
| Baseline | {version} |

## KEEP
| Item | Reason |
|------|--------|

## REMOVE
| Item | Reason |
|------|--------|

## ADD
| Item | Source |
|------|--------|

## Architecture
```
{file structure}
```

## Chat Verification
Scanned: N messages
Result: N/N verified. Missing: none

## NEVER DEGRADE
| Metric | Baseline | Planned |
|--------|----------|---------|
| Features | N | N |

Status: ✅ PASS
```

---

# Appendix: Version Evolution

## Ключевые инновации по версиям

| Version | Codename | Key Innovation |
|---------|----------|----------------|
| v3.9.0 | — | Planning Document, Chat Verification |
| v8.7.0 | Lean Flow | Protocol architecture, NEVER DEGRADE |
| v9.0.0 | Registry | FEATURE-REGISTRY, Session indicator |
| v10.0.0 | Anchor | NEXT in anchor, PRE/DO/EXIT |
| v11.0.0 | Monolith | All-in-one approach |
| v4.0.0 | Unified | Best of all, ecosystem integration |

## Lessons Learned

1. **NEXT критичен** — без него Claude теряет контекст
2. **Specific > Abstract** — конкретные правила работают лучше
3. **NEVER DEGRADE обязателен** — иначе фичи теряются
4. **Blocking points нужны** — иначе Claude спешит
5. **Chat Verification спасает** — люди забывают что обсуждали
6. **Protocols помогают** — но не больше 5-6
7. **500 lines — разумный лимит** — 80 слишком мало, 500+ слишком много

---

*SKILL-ARCHITECTURE-REFERENCE.md*
*2025-12-13*
