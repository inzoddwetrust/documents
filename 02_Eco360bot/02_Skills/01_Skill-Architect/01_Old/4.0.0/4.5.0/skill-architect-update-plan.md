# План обновления skill-architect

## Цель
Интеграция cognitive-razors v2.0 с приоритизацией конфликтов.

---

## Изменения

### 1. SKILL.md (skill-architect)

**Секция "Cognitive Razors"** — добавить:

```markdown
### Conflict Resolution

Priority stack (top wins):
1. Hitchens' → Ask, don't assume
2. Grice's → Intent over literal
3. Einstein's → Sufficient > minimal
4. Hume's → Match problem scale
5. Occam's → Simplify what remains
6. Hanlon's → Stay collaborative

Common: Occam's vs Einstein's → Einstein wins (sufficient first).
```

### 2. reference/cognitive-razors.md

Заменить на cognitive-razors-v2.md целиком.

### 3. protocols/P02-plan.md

В секцию Design Razors добавить:

```markdown
### Razor Conflict?

If Occam's says "simpler" but Einstein's says "insufficient":
→ Einstein wins. Cover requirements first, simplify second.

If unsure about intent AND want to simplify:
→ Hitchens wins. Ask before cutting.
```

### 4. protocols/P03-build.md

Добавить decision checkpoint:

```markdown
### Pre-Build Razor Check

Before writing code:
- [ ] All Hitchens' questions answered?
- [ ] Scale matches (Hume's)?
- [ ] Simplest sufficient (Occam's + Einstein's)?
```

---

## Не менять

- Genetic markers G08-G10 (уже покрывают)
- Protocol flow (P01→P04)
- Anchor format
- Quality Gates L1-L10

---

## Version

skill-architect: v4.4.0 → v4.5.0

```markdown
## CHANGELOG

### v4.5.0
- Added razor conflict resolution (priority stack)
- Updated cognitive-razors.md to v2.0
- Added decision tree for razor conflicts
- Added pre-build razor checkpoint to P03
```

---

## Команда

```
update skill /mnt/skills/user/skill-architect --degrade v4.4.0
```

Или загрузи этот план + cognitive-razors-v2.md и скажи "update skill-architect".
