# Ecosystem Update Plan v2.0

**Date:** 2025-12-15  
**Scope:** All 4 architect-skills  
**Type:** Major ecosystem enhancement

---

## Executive Summary

Комплексное обновление экосистемы на основе:
- Анализа текущего состояния (ecosystem-analysis-report.md)
- Interactive Anchors + Language Policy (skill-architect-update-task.md)
- Cognitive Razors + New Genes G08-G10 (skill-architect-razors-update-plan.md)
- User feedback (версии, soсials module, taplink)

---

## Part 1: Ecosystem-Wide Changes

Эти изменения применяются ко ВСЕМ 4 скилам одинаково.

### 1.1 Remove Internal File Versioning

**Problem:** Версии в footer каждого файла → рассинхрон, лишняя поддержка, нет пользы

**Solution:** Версия только в одном месте

**Before:**
```
skill-architect/
├── SKILL.md                          # v4.2.0
├── protocols/P00-router.md           # v4.2.0 "Delegation"
├── protocols/P01-init.md             # v4.1.0 ← рассинхрон!
├── reference/ecosystem-paths.md      # v4.1.0 ← рассинхрон!
```

**After:**
```
skill-architect/
├── SKILL.md                          # description: "v4.3.0 | ..."
├── protocols/P00-router.md           # NO version footer
├── protocols/P01-init.md             # NO version footer
├── reference/ecosystem-paths.md      # NO version footer

Export: skill-architect-v4.3.0.zip
```

**Files to update (per skill):**
| Skill | Files with version footers | Action |
|-------|---------------------------|--------|
| skill-architect | ~15 files | Remove `*vX.Y.Z*` footer |
| test-architect | ~20 files | Remove `*vX.Y.Z*` footer |
| project-architect | ~12 files | Remove `*vX.Y.Z*` footer |
| role-architect | ~15 files | Remove `*vX.Y.Z*` footer |

---

### 1.2 Interactive Anchor Format

**Problem:** User must type "да", "подтверждаю" → inconsistent, slow

**Solution:** Numbered Options at blocking points

**Before:**
```
⚙️ skill-architect v4.2.0 · P02-plan · waiting-confirm
🟢 fresh | NEXT: user confirms → P03-build
```

**After:**
```
🟢 P02-plan · waiting-confirm
NEXT: confirm → P03-build

Options:
1 → Confirm (→ P03-build)
2 → Edit plan
3 → Cancel
```

**Format specification:**

```markdown
## Anchor Format

Every response ends with:

[session] [protocol] · [status]
NEXT: [explicit next action]

Options: (only at ⛔ blocking points)
1 → [action] (→ [next protocol])
2 → [action]
3 → [action]

### Session Indicators
- 🟢 fresh (<5 messages)
- 🟡 mid (5-15 messages)  
- 🔴 long (>15 messages)

### Standard Option Sets

| Point | Options |
|-------|---------|
| After plan | 1-Confirm, 2-Edit, 3-Cancel |
| After build | 1-Deliver, 2-Test first, 3-Edit |
| After validation fail | 1-Fix, 2-Skip, 3-Cancel |
| After NEVER DEGRADE fail | 1-Restore, 2-Explain, 3-Cancel |

### User Input
User types: "1" or "2" or "3"
Claude interprets: corresponding action

### Recovery
If context lost → find anchor → read NEXT → continue
Options provide explicit recovery path
```

**Files to update (per skill):**
- SKILL.md → Anchor Format section
- reference/anchor-format.md (if exists)
- All protocol files → update anchor examples

---

### 1.3 Language Policy

**Problem:** Inconsistent language switching, unclear rules

**Solution:** Simple rule — English production, localized chat

**New section in every SKILL.md:**

```markdown
## Language Policy

### Production Rule
All artifacts in English (always):
- SKILL.md, README.md, CHANGELOG.md
- Planning Documents, Diff Reports
- Protocol files, reference files
- Created skills (SKILL.md, README.md)
- All documentation

### Chat Rule  
Dialogue adapts to user's language:
- User writes Russian → Claude responds Russian
- User writes English → Claude responds English
- Auto-detect from first message

### Override Rule
User can explicitly request artifact language:
- "создай README на русском" → README in Russian
- Default: always English unless explicitly requested

### Reasoning
- Token efficiency (English ~25% more compact)
- Universal accessibility
- No confusion with switching
```

---

### 1.4 Confirmation → Options Migration

**Problem:** Inconsistent confirmation words across skills

**Before (confirmation words):**
```markdown
| ✅ Valid | ❌ Invalid |
|----------|-----------|
| да, yes, confirm... | ок, понял, maybe... |
```

**After (Options system):**
```markdown
## User Input

At ⛔ blocking points, user responds with option number:

| Input | Interpretation |
|-------|----------------|
| 1, 2, 3 | Select corresponding option |
| Text matching option | Select that option |
| Other text | Treat as clarification, stay at current point |

### Examples
- "1" → Confirm
- "confirm" → matches option 1 → Confirm  
- "edit" → matches option 2 → Edit
- "actually add feature X" → clarification → stay, update plan
```

**Note:** This replaces the entire "Confirmation Words" section in all skills.

---

### 1.5 Genes Inheritance for Created Skills

Skills created by skill-architect inherit these genes:

**Core Genes (G01-G07)** — existing, no change

**NEW Cognitive Genes (G08-G10):**

| Gene | Name | Validation |
|------|------|------------|
| G08 | Occam's Design | No unused sections, minimal abstractions |
| G09 | Hume's Scale | Complexity matches task size |
| G10 | Einstein's Balance | Complete but not bloated |

**Inheritance rule:**
- skill-architect applies razors during creation
- Created skill gets genetic markers in SKILL.md
- test-architect validates G08-G10 for tool profile

---

## Part 2: Skill-Specific Changes

### 2.1 skill-architect v4.2.0 → v4.3.0 "Interactive Razors"

**Unique changes:**

| Change | Description |
|--------|-------------|
| Cognitive Razors | 6 razors integrated into protocols |
| New Genes | G08-G10 for created skills |
| Pre-Protocol Checklist | Intent + complexity assessment |
| Genetic Validation | Verify G01-G10 before delivery |

**Files to create:**
- `reference/cognitive-razors.md` — full razor framework

**Files to update:**
- `SKILL.md` — version, Language Policy, Anchor Format, Razors summary
- `protocols/P01-init.md` — Intent Interpretation (Grice's, Hitchens')
- `protocols/P02-plan.md` — Design Razors (Occam's, Hume's, Hanlon's)
- `protocols/P03-build.md` — Build Razors (Occam's, Einstein's)
- `protocols/P04-deliver.md` — Feedback Razors (Hanlon's), Genetic Validation
- All files — remove version footers

**Razors integration summary:**

```
P01-init:
  - Grice's Razor: intent vs literal
  - Hitchens' Razor: stated vs assumed
  
P02-plan:
  - Occam's Razor: simplest architecture
  - Hume's Razor: proportional complexity
  - Hanlon's Razor: iteration mindset
  
P03-build:
  - Occam's Razor: remove until breaks
  - Einstein's Razor: simple but sufficient
  
P04-deliver:
  - Hanlon's Razor: feedback = collaboration
  - Genetic Validation: G01-G10 check
```

---

### 2.2 test-architect v1.3.0 → v1.4.0 "Genetic Razors"

**Unique changes:**

| Change | Description |
|--------|-------------|
| G08-G10 validation | New genes for tool profile |
| Remove version check | Don't validate internal file versions |
| Update ecosystem.md | Fix outdated references |

**Files to update:**
- `SKILL.md` — version, Language Policy, Anchor Format
- `reference/genes.md` — add G08-G10
- `reference/tool-genes.md` — add G08-G10 for tool profile
- `reference/ecosystem.md` — fix version references
- `engines/genetic.md` — add G08-G10 checks
- `scripts/genetic-audit.sh` — add G08-G10 validation
- All files — remove version footers

**New validation rules:**

```markdown
## G08: Occam's Design Test

Check:
- [ ] No sections with zero references
- [ ] No files with <50 lines content  
- [ ] No abstractions used once
- [ ] Protocol count ≤ command count

## G09: Hume's Scale Test

| Commands | Expected Files | Expected Lines |
|----------|---------------|----------------|
| 1-5 | 1 file | <500 |
| 6-15 | 1-3 files | <1500 |
| 15+ | 3+ files | proportional |

## G10: Einstein's Balance Test

- All stated requirements present
- No unstated features (unless justified)
```

---

### 2.3 project-architect v1.2.0 → v1.3.0 "Social Presence"

**Unique changes:**

| Change | Description |
|--------|-------------|
| socials.yaml | New module for social media presence |
| Taplink requirement | Link aggregator check |
| Gaps report update | Include social presence gaps |

**New module: socials.yaml**

```yaml
# socials.yaml - Social Media Presence

company:
  website: ""          # required
  link_aggregator: ""  # required (taplink, linktree, etc)
  
  social_profiles:
    linkedin: ""       # required for B2B
    twitter: ""
    facebook: ""
    instagram: ""
    youtube: ""
    tiktok: ""
    telegram: ""
    
  content_platforms:
    blog: ""
    medium: ""
    substack: ""
    
team:
  founders:
    - name: ""
      linkedin: ""     # required
      twitter: ""
      
  key_members:
    - name: ""
      role: ""
      linkedin: ""

validation:
  link_aggregator_required: true
  minimum_social_profiles: 2
  founder_linkedin_required: true
```

**Link aggregator check:**

```markdown
## Link Aggregator Requirement

Every project MUST have a link aggregator:

| Service | URL Pattern |
|---------|-------------|
| Taplink | taplink.cc/username |
| Linktree | linktr.ee/username |
| Beacons | beacons.ai/username |
| Bio.link | bio.link/username |
| Custom | any single-page with all links |

### Why Required
- Instagram/TikTok allow only 1 link in bio
- Link aggregator solves "one link" problem
- Essential for social media presence

### Validation
If missing → Gaps report shows:
"❌ No link aggregator. Create: taplink.cc or linktree"
```

**Files to update:**
- `SKILL.md` — version, Language Policy, Anchor Format, add socials module
- `reference/modules.md` — add socials.yaml specification
- `protocols/P03-collect.md` — collect social data
- `protocols/P05-validate.md` — validate link aggregator
- `scripts/validate-project.sh` — add socials validation
- `scripts/gaps-report.sh` — report social presence gaps
- All files — remove version footers

**Updated modules count: 10 → 11**

| # | Module | Required Fields |
|---|--------|-----------------|
| 1 | core.yaml | name, stage, problem, solution |
| 2 | team.yaml | 1+ founder with name, role |
| 3 | product.yaml | name, status, value_proposition |
| 4 | market.yaml | target_customer, 1+ competitor |
| 5 | finances.yaml | revenue.model, funding.stage |
| 6 | tech.yaml | frontend OR backend stack |
| 7 | roadmap.yaml | vision.one_year, 1+ milestone |
| 8 | risks.yaml | 1+ risk with title, probability, impact |
| 9 | clients.yaml | 1+ segment OR key_account |
| 10 | decisions.yaml | id, title, date, status, decision |
| **11** | **socials.yaml** | **website, link_aggregator, 2+ profiles** |

---

### 2.4 role-architect v1.3.0 → v1.4.0 "Protocol Extraction"

**Unique changes:**

| Change | Description |
|--------|-------------|
| Extract protocols/ | Move inline protocols to separate files |
| Add Chat Verification | Explicit checkpoint before compose |
| Reduce SKILL.md size | From 367 to ~250 lines |

**New directory structure:**

```
role-architect/
├── SKILL.md                          # ~250 lines (was 367)
├── protocols/                        # NEW directory
│   ├── P00-router.md
│   ├── P01-create.md
│   ├── P02-switch.md
│   ├── P03-query.md
│   ├── P04-route.md
│   ├── P05-recovery.md
│   └── P06-build-skill.md
├── layers/
├── domains/
├── reference/
├── templates/
└── scripts/
```

**Files to create:**
- `protocols/P00-router.md`
- `protocols/P01-create.md`
- `protocols/P02-switch.md`
- `protocols/P03-query.md`
- `protocols/P04-route.md`
- `protocols/P05-recovery.md`
- `protocols/P06-build-skill.md`

**Files to update:**
- `SKILL.md` — extract PROTOCOLS section, add Language Policy, Anchor Format
- All files — remove version footers

**Add Chat Verification:**

```markdown
## Chat Verification (before P01-create step 3)

Before COMPOSE, scan chat for:
1. Mentioned domain keywords
2. Level indicators
3. Type hints
4. Boundary requirements
5. Specific tools/metrics

Create verification table:

| # | Item from chat | Captured in | Status |
|---|----------------|-------------|--------|
| 1 | {keyword} | L1/L2/L3 | ✅/❌ |

All items must be ✅ before proceeding.
```

---

## Part 3: Implementation Order

### Phase 1: Ecosystem Foundation (Day 1)

**All skills simultaneously:**

1. Remove version footers from all internal files
2. Update SKILL.md with:
   - New version number
   - Language Policy section
   - Interactive Anchor Format section
   - Remove Confirmation Words section

**Validation:** Each skill SKILL.md updated, no version footers in internal files

---

### Phase 2: skill-architect (Day 2)

1. Create `reference/cognitive-razors.md`
2. Update `protocols/P01-init.md` — Intent Interpretation
3. Update `protocols/P02-plan.md` — Design Razors
4. Update `protocols/P03-build.md` — Build Razors
5. Update `protocols/P04-deliver.md` — Feedback Razors + Genetic Validation
6. Update anchor examples in all protocols

**Validation:** `test-architect test skill-architect --full`

---

### Phase 3: test-architect (Day 3)

1. Update `reference/genes.md` — add G08-G10
2. Update `reference/tool-genes.md` — add G08-G10
3. Update `engines/genetic.md` — G08-G10 validation
4. Update `scripts/genetic-audit.sh`
5. Fix `reference/ecosystem.md` — remove outdated versions
6. Update anchor examples in all protocols

**Validation:** `test-architect self-test`

---

### Phase 4: project-architect (Day 4)

1. Create `socials.yaml` template
2. Update `reference/modules.md` — add socials specification
3. Update `protocols/P03-collect.md` — social data collection
4. Update `protocols/P05-validate.md` — link aggregator validation
5. Update `scripts/validate-project.sh`
6. Update `scripts/gaps-report.sh`
7. Update anchor examples in all protocols

**Validation:** `test-architect test project-architect --full`

---

### Phase 5: role-architect (Day 5)

1. Create `protocols/` directory
2. Extract P00-P06 from SKILL.md to separate files
3. Add Chat Verification to P01-create
4. Update SKILL.md — references to protocols
5. Update anchor examples in all protocols

**Validation:** `test-architect test role-architect --full`

---

### Phase 6: Ecosystem Test (Day 6)

```
test-architect test-ecosystem
```

Expected result:
```
═══════════════════════════════════════
ECOSYSTEM HEALTH REPORT
═══════════════════════════════════════

skill-architect:   ✅ v4.3.0 (score: 95+)
test-architect:    ✅ v1.4.0 (score: 95+)
project-architect: ✅ v1.3.0 (score: 95+)
role-architect:    ✅ v1.4.0 (score: 95+)

ECOSYSTEM STATUS: HEALTHY
═══════════════════════════════════════
```

---

## Part 4: Version Summary

| Skill | Current | New | Codename |
|-------|---------|-----|----------|
| skill-architect | v4.2.0 "Delegation" | v4.3.0 "Interactive Razors" |
| test-architect | v1.3.0 "Clean Differentiated" | v1.4.0 "Genetic Razors" |
| project-architect | v1.2.0 "Resilient" | v1.3.0 "Social Presence" |
| role-architect | v1.3.0 "INoT Skill Builder" | v1.4.0 "Protocol Extraction" |

---

## Part 5: Checklist

### Ecosystem-Wide

- [ ] Remove version footers from ALL internal files (all 4 skills)
- [ ] Add Language Policy to ALL SKILL.md
- [ ] Add Interactive Anchor Format to ALL SKILL.md
- [ ] Remove Confirmation Words from ALL SKILL.md
- [ ] Update anchor examples in ALL protocols

### skill-architect v4.3.0

- [ ] Update SKILL.md frontmatter → v4.3.0
- [ ] Create reference/cognitive-razors.md
- [ ] Update P01-init.md — Intent Interpretation
- [ ] Update P02-plan.md — Design Razors
- [ ] Update P03-build.md — Build Razors
- [ ] Update P04-deliver.md — Feedback Razors + Genetic Validation
- [ ] Verify all anchor examples have Options

### test-architect v1.4.0

- [ ] Update SKILL.md frontmatter → v1.4.0
- [ ] Update reference/genes.md — add G08-G10
- [ ] Update reference/tool-genes.md — add G08-G10
- [ ] Update engines/genetic.md — G08-G10 validation
- [ ] Update scripts/genetic-audit.sh
- [ ] Fix reference/ecosystem.md
- [ ] Remove internal version checking from validation

### project-architect v1.3.0

- [ ] Update SKILL.md frontmatter → v1.3.0
- [ ] Create socials.yaml template in reference/modules.md
- [ ] Update protocols/P03-collect.md
- [ ] Update protocols/P05-validate.md
- [ ] Update scripts/validate-project.sh
- [ ] Update scripts/gaps-report.sh
- [ ] Add socials to NEVER DEGRADE (modules: 10 → 11)

### role-architect v1.4.0

- [ ] Update SKILL.md frontmatter → v1.4.0
- [ ] Create protocols/ directory
- [ ] Extract P00-router.md
- [ ] Extract P01-create.md
- [ ] Extract P02-switch.md
- [ ] Extract P03-query.md
- [ ] Extract P04-route.md
- [ ] Extract P05-recovery.md
- [ ] Extract P06-build-skill.md
- [ ] Add Chat Verification to P01-create
- [ ] Update SKILL.md — shrink to ~250 lines

### Final Validation

- [ ] test-architect self-test → PASS
- [ ] test skill-architect --full → PASS
- [ ] test project-architect --full → PASS
- [ ] test role-architect --full → PASS
- [ ] test-ecosystem → ALL HEALTHY

---

## Part 6: Risk Mitigation

| Risk | Probability | Mitigation |
|------|-------------|------------|
| Breaking existing skills | Low | All changes additive, backward compatible |
| Options confusion | Low | NEXT remains for recovery, Options for UX |
| Razors over-applied | Medium | Razors = suggestions, can skip with justification |
| Social module incomplete | Low | Mark as TBD, gaps report shows missing |
| role-architect extraction breaks flow | Medium | Test each protocol after extraction |

---

## Part 7: Success Criteria

Update is successful when:

1. ✅ All 4 skills pass test-architect --full (score ≥90)
2. ✅ No version footers in internal files
3. ✅ Interactive Options work at all ⛔ points
4. ✅ Language Policy respected (English artifacts, localized chat)
5. ✅ Cognitive Razors applied in skill-architect
6. ✅ G08-G10 validated for tool profile
7. ✅ socials.yaml collected and validated
8. ✅ role-architect protocols extracted
9. ✅ Ecosystem test passes

---

*Ecosystem Update Plan v2.0 | Ready for implementation*
