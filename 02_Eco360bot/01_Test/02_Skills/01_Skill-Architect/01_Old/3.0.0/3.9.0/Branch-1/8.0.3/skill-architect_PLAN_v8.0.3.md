# skill-architect: План v8.0.2 → v8.0.3

## Date: 2025-12-08 | Context: B-003 Implementation

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Russian |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

Self-audit выявил: P06 ссылается на несуществующие протоколы. B-003 требует реструктуризации финальных шагов.

---

## 2. Проблемы

| # | Проблема | Severity |
|---|----------|----------|
| 1 | P06 broken refs | 🔴 Critical |
| 2 | Нет smoke test | 🟡 High |
| 3 | 18 файлов на v8.0.1 | 🟢 Low |

---

## 3. Новая архитектура

```
P07-closure = Scan + Docs (обязательный)
P08-simulation = Виртуальное тестирование (опциональный, на выбор)
```

### Flow

**Было:**
```
P06 ⛔ → P07-scan → P08-docs ⛔ → END
```

**Стало:**
```
P06 ⛔ → P07-closure ⛔ → [P08-simulation] → END
                              ↑ optional
```

---

## 4. Изменения

### Добавляем

| File | Content |
|------|---------|
| P07-closure.md | Scan + Docs + Delivery |
| P08-simulation.md | Dry-run тест скилла (optional) |

### Удаляем

| File | Reason |
|------|--------|
| P07-scan.md | → P07-closure |
| P08-docs-closure.md | → P07-closure |

### Изменяем

| File | Change |
|------|--------|
| P00-router.md | Новый flow |
| P06-delivery-skill.md | Fix refs |
| SKILL.md | Router table |
| 18 files | footers → v8.0.3 |

---

## 5. Структура новых протоколов

### P07-closure

```
1. Scan (structure, SSOT, cross-refs)
2. Docs generation (8 files)
3. Final Delivery (.skill + .zip)
4. Offer: "Симуляция? да/skip"
```

### P08-simulation

```
1. Load SKILL.md
2. Simulate activation → check menu
3. Simulate P01→P0N flow (dry-run)
4. Check cross-references
5. Report: PASS/FAIL + issues
```

---

## 6. Чат-верификация

| Item | Status |
|------|--------|
| P07 = Scan + Docs | ✅ |
| P08 = Simulation (optional) | ✅ |
| 9 protocols total | ✅ |

---

## 7. Чеклист

- [ ] P07-closure = Scan + Docs
- [ ] P08-simulation = optional
- [ ] Можно начинать

**⛔ Ожидаю: "да", "yes", "go", "делай"**

---

*skill-architect_PLAN_v8.0.3.md | 2025-12-08*
