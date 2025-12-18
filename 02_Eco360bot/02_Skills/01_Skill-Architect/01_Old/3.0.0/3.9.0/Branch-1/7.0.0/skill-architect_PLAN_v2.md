# skill-architect: План v6.2.0 → v7.0.0

**Date:** 2025-12-05 | **Context:** Unified Ecosystem (Create + Test + Validate)

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

## ⛔ НЕПРИКОСНОВЕННОЕ ЯДРО (50 итераций!)

**НЕ ТРОГАЕМ:**
```
SKILL.md структура (router pattern)     → НЕ МЕНЯЕМ
├── ⛔ NEVER DEGRADE                    → НЕ МЕНЯЕМ
├── ⛔ FIRST STEP — MANDATORY           → НЕ МЕНЯЕМ
├── ⛔ BEFORE EVERY RESPONSE            → НЕ МЕНЯЕМ
├── Protocol Router table               → НЕ МЕНЯЕМ
├── Quick Start                         → НЕ МЕНЯЕМ
└── Resources tables                    → ТОЛЬКО ДОБАВЛЯЕМ строки

reference/protocols/
├── P00-router.md                       → НЕ ТРОГАЕМ
├── P01-activation.md                   → НЕ ТРОГАЕМ
├── P02-config.md                       → НЕ ТРОГАЕМ
├── P03-planning.md                     → НЕ ТРОГАЕМ
├── P04-build.md                        → НЕ ТРОГАЕМ
├── P05-validate.md                     → РАСШИРЯЕМ (добавляем шаги)
├── P06-delivery-skill.md               → НЕ ТРОГАЕМ
├── P07-delivery-docs.md                → НЕ ТРОГАЕМ
└── P08-scan.md                         → НЕ ТРОГАЕМ

scripts/
├── validate-skill.sh                   → НЕ ТРОГАЕМ
├── validate-naming.sh                  → НЕ ТРОГАЕМ
├── ssot-check.sh                       → НЕ ТРОГАЕМ
├── audit-skill.sh                      → НЕ ТРОГАЕМ
├── self-diagnostic.sh                  → НЕ ТРОГАЕМ
└── generate-manifest.sh                → НЕ ТРОГАЕМ

Пайплайн:
SKILL.md → Router → Read Protocol → Execute → Blocking → Next
                    ↑
              НЕПРИКОСНОВЕННО
```

---

## 1. Контекст

Объединение трёх компонентов в единую самодостаточную экосистему:

| Источник | Что забираем | Куда |
|----------|--------------|------|
| skill-architect v6.2.0 | Ядро (create, protocols, scripts) | База |
| skill-tester v1.0.1 | 6-level testing (L1-L6) | P05-validate |
| ideathor VT + research | Virtual Testing (personas, devil's advocate, expert panel) | P05-validate |

**Результат:** Один скил = полный цикл (Create → Validate → Test → Deliver)

---

## 2. Задачи

### 2.1 Расширить P05-validate
Добавить слои тестирования БЕЗ удаления существующих:

```
P05-validate.md (БЫЛО):
├── 1. Run validators (validate-skill.sh, etc.)
├── 2. Create Diff Report
└── 3. Generate MANIFEST

P05-validate.md (СТАНЕТ):
├── 0. [NEW] Virtual Testing Layer (optional, +vt flag)
│   ├── Context Detection
│   ├── Persona Simulation
│   ├── Devil's Advocate
│   ├── Expert Panel
│   └── Hypothesis Output
├── 1. Run validators                    ← БЕЗ ИЗМЕНЕНИЙ
├── 2. [NEW] Deep Testing (optional, +full flag)
│   ├── L4: Simulation Testing
│   ├── L5: Methodology Viability
│   └── L6: Interpretation Test
├── 3. Create Diff Report               ← БЕЗ ИЗМЕНЕНИЙ
└── 4. Generate MANIFEST                 ← БЕЗ ИЗМЕНЕНИЙ
```

### 2.2 Добавить reference файлы

| New File | Source | Purpose |
|----------|--------|---------|
| reference/virtual-testing.md | ideathor + research | VT protocol |
| reference/test-levels.md | skill-tester | L1-L6 definitions |
| reference/test-cases.md | skill-tester | Test case patterns |
| reference/personas.md | NEW | Persona templates by context |
| reference/adversarial.md | NEW | Devil's advocate + red team |
| reference/expert-panel.md | NEW | Multi-agent evaluation |

### 2.3 Update существующих файлов

| File | Change | Preserves |
|------|--------|-----------|
| SKILL.md | Version 7.0.0, add VT/Test resources | Router structure, all sections |
| reference/engines.md | Add VT Engine | All existing engines |
| reference/templates.md | Add VT hook option | All 5 templates |
| reference/quality-checklist.md | Add VT gate | All existing gates |

---

## 3. Архитектура P05 (расширенная)

```
╔══════════════════════════════════════════════════════════════╗
║                    P05-VALIDATE (v7.0.0)                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ LAYER 0: VIRTUAL TESTING (optional, +vt)                │ ║
║  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐ │ ║
║  │ │ Context     │→│ Persona     │→│ Adversarial Layer   │ │ ║
║  │ │ Detector    │ │ Generator   │ │ (Devil's Advocate)  │ │ ║
║  │ └─────────────┘ └─────────────┘ └─────────────────────┘ │ ║
║  │        ↓                               ↓                │ ║
║  │ ┌─────────────────────┐ ┌────────────────────────────┐ │ ║
║  │ │ Expert Panel        │→│ Scoring + Hypothesis       │ │ ║
║  │ │ (Multi-Agent Eval)  │ │ Output (NOT facts!)        │ │ ║
║  │ └─────────────────────┘ └────────────────────────────┘ │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                            ↓                                 ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ LAYER 1: STATIC VALIDATION (always runs)                │ ║
║  │ ├── validate-skill.sh   (structure, frontmatter)       │ ║
║  │ ├── validate-naming.sh  (kebab-case, conventions)      │ ║
║  │ └── ssot-check.sh       (duplicates, constraints)      │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                            ↓                                 ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ LAYER 2: DEEP TESTING (optional, +full)                 │ ║
║  │ ├── L4: Simulation (happy path, edge cases)            │ ║
║  │ ├── L5: Methodology (step viability, dependencies)     │ ║
║  │ └── L6: Interpretation (how Claude understands)        │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                            ↓                                 ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ LAYER 3: REPORTING (always runs)                        │ ║
║  │ ├── Diff Report                                         │ ║
║  │ ├── MANIFEST.md                                         │ ║
║  │ └── [Optional] TEST_REPORT.md (if +full)               │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 4. Было → Стало

### skill-architect structure

**v6.2.0 (было):** 17 files
```
skill-architect/
├── SKILL.md (155 lines)
├── README.md
├── MANIFEST.md
├── reference/ (14 files)
│   ├── protocols/P00-P08 (9 files)
│   ├── commands.md
│   ├── engines.md
│   ├── templates.md
│   ├── quality-checklist.md
│   └── ... (other)
└── scripts/ (7 files)
```

**v7.0.0 (станет):** 23 files (+6)
```
skill-architect/
├── SKILL.md                         # UPDATED (version, resources)
├── README.md                        # UPDATED (VT docs)
├── MANIFEST.md                      # REGENERATED
├── reference/
│   ├── protocols/
│   │   ├── P00-P08                  # P05 EXPANDED, rest UNCHANGED
│   │   └── ...
│   ├── commands.md                  # UNCHANGED
│   ├── engines.md                   # UPDATED (+VT Engine)
│   ├── templates.md                 # UPDATED (+VT hook)
│   ├── quality-checklist.md         # UPDATED (+VT gate)
│   ├── virtual-testing.md           # NEW
│   ├── test-levels.md               # NEW (from skill-tester)
│   ├── test-cases.md                # NEW (from skill-tester)
│   ├── personas.md                  # NEW
│   ├── adversarial.md               # NEW
│   ├── expert-panel.md              # NEW
│   └── ... (other UNCHANGED)
└── scripts/                         # ALL UNCHANGED
```

### skill-tester → DEPRECATED
```
skill-tester/ → absorbed into skill-architect
└── Functionality preserved in P05-validate + reference files
```

---

## 5. Флаги валидации

| Command | Layers | Duration |
|---------|--------|----------|
| (default) | L1 only | ~1 min |
| `+full` | L1 + L2 (L4-L6) | ~5 min |
| `+vt` | L0 + L1 | ~3 min |
| `+full +vt` | L0 + L1 + L2 | ~8 min |

---

## 6. Риски

| Risk | Prob | Impact | Mitigation |
|------|------|--------|------------|
| P05 становится слишком большой | Med | Med | Layers are optional, reference files |
| VT добавляет latency | Med | Low | Optional flag (+vt) |
| skill-tester users confused | Low | Low | README migration guide |
| Ядро случайно изменено | Low | Critical | Явный checklist "НЕ ТРОГАЕМ" |

---

## 7. Чат-верификация

Обсуждённые требования:
1. ✅ Универсальный VT модуль (автодетект контекста)
2. ✅ Встраивание в skill-architect (не отдельный скил)
3. ✅ Интеграция skill-tester в skill-architect
4. ✅ Единая экосистема (create → validate → test → deliver)
5. ✅ Multi-agent архитектура (personas, devil's advocate, expert panel)
6. ✅ Выход VT = гипотезы, не факты
7. ✅ Ядро skill-architect НЕПРИКОСНОВЕННО (50 итераций!)
8. ✅ Router pattern сохраняется
9. ✅ Все протоколы P00-P08 сохраняются (P05 расширяется)
10. ✅ Все скрипты сохраняются

**Verified: 10 items. Missing: none**

---

## 8. Файлы к созданию/изменению

### NEW FILES (6):
```
reference/virtual-testing.md      # VT protocol
reference/test-levels.md          # L1-L6 definitions (from skill-tester)
reference/test-cases.md           # Test patterns (from skill-tester)
reference/personas.md             # Persona templates
reference/adversarial.md          # Devil's advocate protocol
reference/expert-panel.md         # Multi-agent evaluation
```

### UPDATED FILES (6):
```
SKILL.md                          # Version 7.0.0, resources table
README.md                         # VT + testing docs
reference/protocols/P05-validate.md  # Expanded with layers
reference/engines.md              # +VT Engine
reference/templates.md            # +VT hook option
reference/quality-checklist.md    # +VT gate
```

### REGENERATED (1):
```
MANIFEST.md                       # New file list
```

### UNCHANGED (16):
```
reference/protocols/P00-P04, P06-P08 (8 files)
reference/commands.md
reference/packaging.md
reference/naming-convention.md
reference/workflow.md
reference/project-*.md (4 files)
scripts/* (7 files)
```

---

## 9. Чеклист подтверждения

- [ ] План понятен
- [ ] Единая экосистема согласована
- [ ] Ядро НЕПРИКОСНОВЕННО — подтверждаю
- [ ] skill-tester растворяется в skill-architect
- [ ] VT встраивается как optional layer
- [ ] Изменения минимальны, добавления максимальны
- [ ] Риски приемлемы
- [ ] Можно начинать

---

**⛔ BLOCKING POINT**

Ожидаю подтверждение: "да", "yes", "go", "делай"
