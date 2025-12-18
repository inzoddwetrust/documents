# Skill Architect: План v6.1.0 → v6.2.0
## 2025-12-02 | Self-Compliance Fix

---

## Constraints

| Rule | Value |
|------|-------|
| SKILL.md language | English |
| SKILL.md max lines | 300 |
| README language | Russian |
| Frontmatter | name + description + version |
| Confirmation | explicit "да/yes/go" |

---

## 1. Контекст

Claude игнорирует собственные протоколы skill-architect:
- Не читает P00-router при активации
- Не читает протоколы перед выполнением этапов
- Игнорирует naming-convention.md
- Не ждёт подтверждений на blocking points
- Выдаёт файлы с неправильными именами (v6_0_0 вместо v6.0.0)

**Root cause:** MANDATORY секции написаны текстом, но не форсируют действие. Claude "видит" их, но не выполняет.

---

## 2. Проблемы

| # | Проблема | Severity |
|---|----------|----------|
| 1 | MANDATORY секции игнорируются | 🔴 Critical |
| 2 | Нет явного FIRST STEP | 🔴 Critical |
| 3 | Naming convention не читается | 🔴 Critical |
| 4 | Blocking points пропускаются | 🔴 Critical |
| 5 | Нет self-check перед каждым ответом | 🟡 Important |

---

## 3. План изменений

### Добавляем

| Что | Зачем | Где |
|-----|-------|-----|
| `## ⛔ FIRST STEP` секция | Форсировать чтение P00-router | SKILL.md, после frontmatter |
| Explicit file_read path | Указать ТОЧНЫЙ путь для чтения | SKILL.md |
| `## ⛔ BEFORE EVERY RESPONSE` | Чеклист перед каждым ответом | SKILL.md |
| Naming check в P06 | Проверка имён перед выдачей | P06-delivery-skill.md |
| Self-compliance warning | "Ты читал протокол?" | Протоколы P01-P08 |

### Изменяем

| Файл | Было | Станет |
|------|------|--------|
| SKILL.md: MANDATORY | Текст "Read router" | `⛔ FIRST STEP: file_read → /mnt/.../P00-router.md` |
| SKILL.md: Protocol Router | Относительные пути | Абсолютные пути `/mnt/skills/user/...` |
| P06-delivery-skill.md | Нет проверки naming | Добавить `bash validate-naming.sh` |

### Удаляем

| Что | Почему |
|-----|--------|
| — | Ничего не удаляем |

### Не трогаем

| Что | Причина |
|-----|---------|
| Все протоколы P00-P08 | Логика работает |
| Reference файлы | Работают |
| Scripts | Работают |
| Project mode | Не затронут |

---

## 4. Было → Станет

### SKILL.md структура

**Было:**
```markdown
## ⚠️ MANDATORY: On Activation

1. Read dependency: `/mnt/skills/user/clean-protocol/SKILL.md`
2. Read router: `protocols/P00-router.md`
3. Determine current state
4. Execute appropriate protocol
```

**Станет:**
```markdown
## ⛔ FIRST STEP — MANDATORY

**STOP. Before ANYTHING else:**

```
file_read → /mnt/skills/user/skill-architect/reference/protocols/P00-router.md
```

Then:
1. Read clean-protocol: `/mnt/skills/user/clean-protocol/SKILL.md`
2. Determine current state from P00-router
3. Read the SPECIFIC protocol needed
4. Execute

**If you skip this → you WILL break naming, blocking points, delivery.**

---

## ⛔ BEFORE EVERY RESPONSE

```
□ Did I read the protocol for this step?
□ Am I at a blocking point? → STOP and wait
□ File names follow naming-convention.md?
□ Token counter at end?
```
```

### P06-delivery-skill.md добавка

```markdown
## Pre-Delivery Check

Before packaging:
1. `bash scripts/validate-naming.sh /home/claude/[skill]`
2. Verify: `{name}-v{X.Y.Z}.skill` format
3. NO underscores in version (v6.0.0, NOT v6_0_0)
```

---

## 5. Риски

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| SKILL.md превысит 300 строк | Low | Добавляем ~15 строк, сейчас 135 |
| Claude всё равно проигнорирует | Medium | Максимально явные инструкции + ⛔ |
| Избыточность | Low | Лучше повторить чем пропустить |

---

## 6. Чат-верификация

Обсуждённые пункты:
1. ✅ Claude игнорировал протоколы доставки (P06, P07)
2. ✅ Неправильный формат имён файлов (v6_0_0 vs v6.0.0)
3. ✅ Не читал naming-convention.md
4. ✅ Не ждал blocking points
5. ✅ Требуется план обновления

**Verified: 5 items. Missing: none.**

---

## 7. Версионирование

| Change | Type |
|--------|------|
| FIRST STEP секция | MINOR |
| BEFORE EVERY RESPONSE | MINOR |
| P06 naming check | MINOR |

**v6.1.0 → v6.2.0** (MINOR: усиление существующих правил)

Codename: **"Self-Compliance"**

---

## 8. Чеклист подтверждения

- [ ] План понятен
- [ ] Изменения согласованы
- [ ] Риски приемлемы
- [ ] Можно начинать

---

**⛔ BLOCKING: Ожидаю "да" / "yes" / "go" для старта**

---

*Planning Document | skill-architect v6.1.0 → v6.2.0 | 2025-12-02*
