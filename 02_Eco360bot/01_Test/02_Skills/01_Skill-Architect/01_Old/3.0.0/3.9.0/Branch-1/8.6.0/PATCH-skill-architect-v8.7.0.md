# PATCH: skill-architect v8.7.0 "Lean Flow"

Упрощение протоколов: 8 → 5

**Created:** 2025-12-12  
**From:** Analysis of v8.6.0 flow

---

## 🎯 Цель

Убрать избыточность, сократить точки ожидания, сделать flow логичным.

---

## 📊 Было → Стало

```
БЫЛО (8 протоколов, 4 стопа):
P00 → P01 → P02 → P03 ⛔ → P04 → P05 → P06 ⛔ → P07 ⛔ → P08 → [P09]

СТАЛО (5 протоколов, 2 стопа):
P00 → P01-init → P02-plan ⛔ → P03-build → P04-deliver ⛔ → [P05-simulation] → [P06-audit]
```

---

## 🔀 Объединения

| Новый | Старые | Что объединяем |
|-------|--------|----------------|
| P01-init | P01 + P02 | Activation + Config в одном |
| P02-plan | P03 | Planning (без изменений, перенумерован) |
| P03-build | P04 + P05 | Build + Validate (одна операция) |
| P04-deliver | P06 + P07 | Skill + Docs (одна доставка) |
| P05-simulation | P08 | Simulation (optional) |
| P06-audit | P09 | Full audit (отдельная команда) |

---

## 📝 Детали изменений

### P01-init (было P01 + P02)

**Логика:** Зачем отдельно "что хочешь?" и "уточняющие вопросы"? Это одна фаза.

```markdown
# P01: Init

Activation and configuration in one step.

---

## Trigger

- User mentions skill-architect
- User describes purpose
- Triggers: create skill, update, refactor, etc.

---

## Steps

1. **Quick response:**
   ```
   Skill Architect v8.7.0
   ```

2. **If purpose unclear** → ask ONE question:
   ```
   Purpose? (create/update/refactor)
   ```

3. **If purpose clear** → gather config:
   - Mode: skill or project?
   - Complexity: simple (<100 lines) or full?
   - For update: what changes?

4. **Output:** Ready for planning

---

## Next

→ P02-plan (always)

---

*P01-init.md v1.0.0 | skill-architect v8.7.0*
```

**Сокращение:** 2 протокола → 1, убран лишний стоп

---

### P02-plan (было P03)

**Логика:** Остаётся как есть, только перенумерован. Это единственный обязательный стоп перед работой.

```markdown
# P02: Plan ⛔

Planning document with explicit confirmation.

---

## ⛔ BLOCKING

Cannot proceed without explicit "да/yes/go"

---

## Steps

1. Create Planning Document:
   - Context
   - Changes (add/change/remove/keep)
   - Risks
   - Chat verification

2. Save to outputs

3. **WAIT** for confirmation

---

## Next

→ P03-build (only after explicit yes)

---

*P02-plan.md v1.0.0 | skill-architect v8.7.0*
```

---

### P03-build (было P04 + P05)

**Логика:** Build и Validate — это не два шага, это одна операция. Написал код → сразу проверил.

```markdown
# P03: Build

Create files and validate in one step.

---

## Trigger

- P02-plan confirmed with "да/yes/go"

---

## Steps

1. **Create/update files** per plan
   - Follow plan exactly
   - Log deviations

2. **Validate immediately:**
   ```bash
   bash scripts/validate-skill.sh .
   ```

3. **If FAIL** → fix and re-validate

4. **If PASS** → ready for delivery

---

## NEVER DEGRADE Reminder

- Don't remove working functionality
- Don't replace specific with abstract
- Automated check runs in P04

---

## Next

→ P04-deliver (on validation pass)

---

*P03-build.md v1.0.0 | skill-architect v8.7.0*
```

**Сокращение:** 2 протокола → 1, убран переход P04→P05

---

### P04-deliver (было P06 + P07) ⛔

**Логика:** Skill и Docs — одна доставка. Зачем ждать подтверждения между ними?

```markdown
# P04: Deliver ⛔

Package and deliver skill + docs together.

---

## ⛔ BLOCKING

Wait for user confirmation after delivery.

---

## Steps

### Phase 1: NEVER DEGRADE Check

```bash
# For updates only
bash scripts/validate-degrade.sh /old /new
```

If FAIL → stop, fix, re-run.

### Phase 2: Package Skill

```bash
zip -r skill-name-vX.Y.Z.skill skill-name-vX.Y.Z/
cp *.skill /mnt/user-data/outputs/
```

### Phase 3: Generate Docs

```bash
# For updates: use update mode
bash scripts/generate-docs.sh . X.Y.Z update /prev-docs

# For new: generate templates
bash scripts/generate-docs.sh . X.Y.Z
```

### Phase 4: Package Docs

```bash
zip -r skill-name-vX.Y.Z-docs.zip docs/
cp *-docs.zip /mnt/user-data/outputs/
```

### Phase 5: Deliver

```markdown
| Item | File |
|------|------|
| Skill | [download link] |
| Docs | [download link] |

Simulation? "да" / "skip"
```

---

## Next

| User says | Action |
|-----------|--------|
| "да/simulation" | → P05-simulation |
| "skip/нет" | → END |

---

*P04-deliver.md v1.0.0 | skill-architect v8.7.0*
```

**Сокращение:** 2 протокола → 1, убран стоп между skill и docs

---

### P05-simulation (было P08)

**Логика:** Optional, без изменений кроме номера.

```markdown
# P05: Simulation

Optional smoke test.

---

## Trigger

- User requested "да/simulation" after delivery

---

## Steps

1. Load and verify SKILL.md
2. Check protocol flow
3. Verify cross-references
4. Run naming validation
5. Generate report
6. If issues → create PATCH

---

## Next

→ END

---

*P05-simulation.md v1.0.0 | skill-architect v8.7.0*
```

---

### P06-audit (было P09)

**Логика:** Отдельная команда, не часть основного flow.

```markdown
# P06: Audit

Full audit on demand. Trigger: "checkup", "full-audit"

---

*P06-audit.md v1.0.0 | skill-architect v8.7.0*
```

---

## 📉 Результат упрощения

| Метрика | v8.6.0 | v8.7.0 | Δ |
|---------|--------|--------|---|
| Протоколов в flow | 8 | 5 | -3 |
| Точек ожидания | 4 | 2 | -2 |
| Файлов протоколов | 10 | 7 | -3 |
| Переходов | 8 | 5 | -3 |

---

## 🗑️ Удаляем

| Файл | Причина |
|------|---------|
| P02-config.md | Merged into P01-init |
| P05-validate.md | Merged into P03-build |
| P07-closure.md | Merged into P04-deliver |

---

## ✏️ Переименовываем

| Старый | Новый |
|--------|-------|
| P01-activation.md | P01-init.md |
| P03-planning.md | P02-plan.md |
| P04-build.md | P03-build.md |
| P06-delivery-skill.md | P04-deliver.md |
| P08-simulation.md | P05-simulation.md |
| P09-full-audit.md | P06-audit.md |

---

## 📋 Implementation Checklist

```
□ Create P01-init.md (merge P01 + P02)
□ Rename P03 → P02-plan.md
□ Create P03-build.md (merge P04 + P05)
□ Create P04-deliver.md (merge P06 + P07)
□ Rename P08 → P05-simulation.md
□ Rename P09 → P06-audit.md
□ Delete old: P02, P05, P07
□ Update P00-router.md
□ Update SKILL.md (new flow diagram)
□ Update all cross-references
□ Run simulation
```

---

## ⏱️ Estimated Effort

| Task | Time |
|------|------|
| Create merged protocols | 45 min |
| Update router + SKILL.md | 15 min |
| Fix cross-references | 15 min |
| Testing | 15 min |
| **Total** | ~1.5 hours |

---

## 🆕 New Flow Diagram

```
[USER REQUEST]
      ↓
   P01-init ──────────── "что делаем?"
      ↓
   P02-plan ⛔ ────────── план + подтверждение
      ↓
   P03-build ─────────── создание + валидация
      ↓
   P04-deliver ⛔ ─────── skill + docs + подтверждение
      ↓
   P05-simulation ─────── (optional)
      ↓
    [END]
```

---

*PATCH-skill-architect-v8.7.0.md | skill-architect v8.6.0 → v8.7.0*
