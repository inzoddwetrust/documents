# Skill-Architect Update Plan: Cognitive Razors Integration

**Version:** 4.2.0 → 4.3.0
**Type:** Enhancement
**Scope:** Decision-making framework

---

## Problem Statement

### Current Issues in skill-architect:

| Issue | Impact | Example |
|-------|--------|---------|
| **Overplanning** | 200-line plans for simple skills | Simple command skill → complex architecture |
| **Overthinking edge cases** | Feature creep, delayed delivery | "What if user wants X, Y, Z?" when they asked for A |
| **Defensive on changes** | Emotional response to iterations | Change request → "I planned poorly" |
| **Assumption making** | Wrong direction, rework | Guessing intent instead of asking |
| **Literal interpretation** | Missed user intent | "Бритва Акаме" → anime, not philosophy |
| **Complexity creep** | Unnecessary abstractions | 3 commands → 15 modules "just in case" |

**Root cause:** No explicit decision framework for:
- When to ask vs assume
- How simple is "simple enough"
- How to interpret ambiguous requests
- When complexity is justified

---

## Solution: Cognitive Razors Framework

### Philosophy

Add 6 philosophical razors as **mental models** at key decision points in protocol flow:

```
P01-init → interpret request (Grice's, Hitchens')
    ↓
P02-plan → design solution (Occam's, Hume's, Hanlon's)
    ↓
P03-build → implement (Occam's, Einstein's)
    ↓
P04-deliver → respond to feedback (Hanlon's)
```

---

## Razors to Integrate

### 1. Occam's Razor
**"Simplest solution that covers requirements"**

**Protocol:** P02-plan, P03-build
**Application:**
- Planning: Minimum viable architecture
- Building: Remove abstractions until needed
- Review: "Can this be simpler without losing functionality?"

**Checklist:**
- [ ] Does architecture match problem complexity?
- [ ] Are all abstractions necessary NOW?
- [ ] Can I achieve the same with fewer modules?

**Example:**
```diff
❌ BAD: 
Skill with 3 commands → ecosystem with:
- router.md (5 routes)
- state-manager.md
- validator.md
- error-handler.md
- config-loader.md

✅ GOOD:
Skill with 3 commands → SKILL.md with:
- Commands table
- Flow diagram
- 3 sections for commands
```

---

### 2. Hanlon's Razor
**"Iteration, not criticism"**

**Protocol:** P02-plan, P04-deliver
**Application:**
- When user changes requirements → natural iteration
- When user questions plan → seeking clarity, not criticizing
- When feedback comes → improvement signal, not failure

**Checklist:**
- [ ] Am I taking change requests personally?
- [ ] Is this criticism or clarification?
- [ ] Is defensiveness creeping into my response?

**Example:**
```diff
❌ BAD:
User: "Actually I want feature X too"
Me: "I can update the plan. Sorry, should have asked earlier."

✅ GOOD:
User: "Actually I want feature X too"
Me: "Got it. Adding X to plan. Scope now: A, B, X."
```

---

### 3. Grice's Razor
**"Understand intent, not literal words"**

**Protocol:** P01-init
**Application:**
- Parse user request for MEANING before planning
- When ambiguous → consider context
- Cultural/language nuances

**Checklist:**
- [ ] What did user MEAN vs what did they SAY?
- [ ] Is there context I'm missing?
- [ ] Should I clarify intent before proceeding?

**Example:**
```diff
❌ BAD:
User: "Скилл на основе бритвы Акаме"
Me: *thinks about anime Akame ga Kill*

✅ GOOD:
User: "Скилл на основе бритвы Акаме"
Me: "Уточню — ты про философские бритвы (Occam's Razor и т.д.)?"
```

---

### 4. Hume's Razor
**"Solution complexity = Problem complexity"**

**Protocol:** P02-plan
**Application:**
- Match architecture scale to task scale
- Don't over-engineer for future "what-ifs"
- Proportional response

**Checklist:**
- [ ] Is solution proportional to problem?
- [ ] Am I solving for hypothetical futures?
- [ ] Does this need ecosystem or just SKILL.md?

**Example:**
```diff
❌ BAD:
Task: "Convert temperature C→F"
Solution: Multi-module system with:
- Unit registry
- Conversion engine
- Plugin system for future units
- Configuration loader
- Validation framework

✅ GOOD:
Task: "Convert temperature C→F"
Solution: Single function: (C * 9/5) + 32
Note: Extensible if needed, but sufficient now
```

---

### 5. Hitchens' Razor
**"What isn't stated → ask, don't assume"**

**Protocol:** P01-init, P02-plan
**Application:**
- Unclear requirement → question
- Missing info → explicit request
- Don't fill gaps with guesses

**Checklist:**
- [ ] Am I making assumptions about requirements?
- [ ] Is this explicitly stated or am I inferring?
- [ ] Should I ask before proceeding?

**Example:**
```diff
❌ BAD:
User: "Make calculator skill"
Me: *assumes they want +, -, *, /, ^, sqrt, log, trig...*

✅ GOOD:
User: "Make calculator skill"
Me: "What operations? Basic (+,-,*,/) or scientific (trig, log...)?"
```

---

### 6. Einstein's Razor
**"As simple as possible, but no simpler"**

**Protocol:** P03-build
**Application:**
- Balance between simplicity and functionality
- Don't sacrifice needed features for "purity"
- Simple != incomplete

**Checklist:**
- [ ] Am I cutting needed functionality?
- [ ] Is this still sufficient?
- [ ] Where's the line between simple and insufficient?

**Example:**
```diff
❌ TOO SIMPLE:
Skill needs 5 commands → make 1 command "do everything"
(Simple but unusable)

❌ TOO COMPLEX:
Skill needs 5 commands → make 20 commands "for all cases"
(Comprehensive but overwhelming)

✅ BALANCED:
Skill needs 5 commands → make 5 commands + 1 helper
(Sufficient and clear)
```

---

## Integration Points

### P01-init.md Enhancement

**ADD SECTION: "Intent Interpretation"**

```markdown
## Intent Interpretation

Before proceeding to P02, apply:

### Grice's Razor Check
- [ ] What did user MEAN vs what did they SAY?
- [ ] Cultural/language context?
- [ ] Need clarification?

### Hitchens' Razor Check
- [ ] What's explicitly stated?
- [ ] What am I inferring?
- [ ] What needs confirmation?

If ANY ambiguity → ask before planning.
```

---

### P02-plan.md Enhancement

**ADD SECTION: "Design Razors"**

```markdown
## Design Razors

Before creating Planning Document, apply:

### Occam's Razor Check
- [ ] Simplest architecture covering requirements?
- [ ] Unnecessary abstractions?
- [ ] Minimum viable structure?

### Hume's Razor Check
- [ ] Solution complexity = problem complexity?
- [ ] Over-engineering for future?
- [ ] Proportional design?

### Hanlon's Razor Mindset
- Remember: change requests = iteration, not criticism
- Stay open, not defensive
- User feedback = collaboration signal

Design principle: **Minimum sufficient architecture.**
```

---

### P03-build.md Enhancement

**ADD SECTION: "Build Razors"**

```markdown
## Build Razors

During implementation:

### Occam's Razor Check (continuous)
- Remove code/sections until breaks
- Every abstraction must justify itself
- When in doubt → simpler

### Einstein's Razor Check
- Too simple? Missing functionality?
- Too complex? Unnecessary features?
- Balance point = all requirements met, nothing extra
```

---

### P04-deliver.md Enhancement

**ADD SECTION: "Feedback Razors"**

```markdown
## Feedback Razors

When receiving user feedback:

### Hanlon's Razor Reminder
- Questions = seeking clarity
- Changes = natural iteration
- Criticism = improvement opportunity
- Not: testing, disappointment, or failure

Response tone: collaborative, not defensive.
```

---

## New File: pre-protocol-checklist.md

```markdown
# Pre-Protocol Checklist

Run this BEFORE starting any protocol:

## Request Analysis

1. **Literal vs Intent** (Grice's)
   - What did user say? _____________
   - What did they mean? _____________
   - Clarification needed? Y/N

2. **Explicit vs Assumed** (Hitchens')
   - Stated requirements: _____________
   - My assumptions: _____________
   - Questions to ask: _____________

## Complexity Assessment

3. **Problem Scale** (Hume's)
   - Simple / Medium / Complex?
   - Solution should be: Simple / Medium / Complex?

4. **Simplicity Target** (Occam's)
   - Minimum architecture: _____________
   - Necessary abstractions: _____________

## Mindset

5. **Collaboration Mode** (Hanlon's)
   - Expect: iteration and questions
   - Not: perfect first draft
   - Tone: open and collaborative

ONLY after completing checklist → proceed to P01.
```

---

## Implementation Plan

### Phase 1: Documentation
- [ ] Add razors section to SKILL.md
- [ ] **Update Required Genes section (G01-G10)**
- [ ] Enhance P01, P02, P03, P04 with razor checks
- [ ] Create pre-protocol-checklist.md
- [ ] Update examples with razor application
- [ ] **Add genetic markers documentation**

### Phase 2: Protocol Integration
- [ ] P01-init: add intent interpretation
- [ ] P02-plan: add design razors
- [ ] P03-build: add build razors
- [ ] P04-deliver: add feedback razors
- [ ] **P04-deliver: add genetic validation checklist**

### Phase 3: Genetic Transmission
- [ ] Define G08, G09, G10 manifestation format
- [ ] Create genetic validation tests
- [ ] Update test-architect integration
- [ ] Document inheritance examples
- [ ] Create migration guide for existing skills

### Phase 4: Validation
- [ ] Test with simple skill (3 commands)
- [ ] Test with complex skill (ecosystem)
- [ ] Test with ambiguous request
- [ ] Verify razors prevent previous issues
- [ ] **Verify genes properly inherited**
- [ ] **Run genetic validation tests**

---

## Success Metrics

**Goals:**
1. ✅ Planning Documents 30-50% shorter for simple skills
2. ✅ Zero defensive responses to change requests
3. ✅ Catch ambiguous requests BEFORE planning
4. ✅ Architecture matches problem complexity
5. ✅ No unnecessary abstractions in delivered skills
6. ✅ **All created skills pass G08-G10 validation**
7. ✅ **Genetic markers present in all new skills**

**Failure indicators:**
- Still making 200-line plans for simple skills
- Still defensive on feedback
- Still assuming instead of asking
- Still over-engineering
- **Created skills missing genetic markers**
- **Skills fail Occam's/Hume's/Einstein's tests**

---

## Required Genes: Genetic Transmission

### Critical Understanding

**Razors in skill-architect workflow ≠ Razors in created skills**

| Razor | For skill-architect | For created skills |
|-------|--------------------|--------------------|
| Occam's | How I design | Gene → skill structure |
| Hanlon's | How I react to feedback | ❌ Not inherited |
| Grice's | How I interpret requests | ❌ Not inherited |
| Hume's | How I match complexity | Gene → skill scope |
| Hitchens' | How I handle ambiguity | ❌ Not inherited |
| Einstein's | How I balance simplicity | Gene → skill completeness |

**Result:** 3 razors become GENES (G08, G09, G10)

---

### Updated Gene Table

Skills created by skill-architect MUST inherit these genes:

| Gene | Requirement | Validation |
|------|-------------|------------|
| G01 Frontmatter | `name:` + `description:` with version | Present + valid |
| G02 Purpose | serves/goal/method/success OR clear purpose | Explicit statement |
| G03 Flow | Visual flow with → arrows | Diagram present |
| G04 Commands | Table with triggers | Table format |
| G05 Anchor | NEXT instruction in every response | In all responses |
| G06 Session | 🟢🟡🔴 indicator | In all responses |
| G07 Blocking | ⛔ where confirmation required | Marked clearly |
| **G08 Occam's Design** | Simplest sufficient structure | No unused sections |
| **G09 Hume's Scale** | Complexity matches task | Proportional architecture |
| **G10 Einstein's Balance** | Simple but not simplified | All requirements met |

---

### G08: Occam's Design

**Definition:** Skill structure must be the simplest that covers all requirements.

**Manifestation in created skill:**

```markdown
## Design Principle

This skill follows Occam's Razor:
- Simplest structure covering all requirements
- No unnecessary abstractions
- Every section serves a purpose

Structure:
- [X] sections present
- [Y] total files
- Justification: [why this structure is minimum]
```

**Validation checklist:**
- [ ] No unused sections in SKILL.md
- [ ] No "future-proofing" abstractions
- [ ] No protocol files unless >5 protocols
- [ ] No separate modules unless >1000 lines
- [ ] Clear purpose stated for each component

**Violation examples:**
- ❌ Skill with 3 commands → separate router.md
- ❌ Single-file skill → multi-file architecture
- ❌ Sections with "Reserved for future use"

**Correct examples:**
- ✅ 3 commands → SKILL.md with Commands table
- ✅ 10+ protocols → protocols/ directory
- ✅ Every section actively used

---

### G09: Hume's Scale

**Definition:** Skill complexity must match task complexity.

**Manifestation in created skill:**

```markdown
## Scope Statement

Task complexity: [Simple / Medium / Complex]
Implementation: [Simple / Medium / Complex]

Scale justification:
- Task requires: [X features]
- Implementation provides: [X features]
- Architecture: [proportional/over-engineered/under-engineered]
```

**Complexity levels:**

| Level | Task indicators | Appropriate structure |
|-------|----------------|----------------------|
| Simple | 1-5 commands, single domain | SKILL.md only (100-300 lines) |
| Medium | 6-15 commands, 2-3 domains | SKILL.md + protocols/ if needed |
| Complex | 15+ commands, ecosystem | SKILL.md + protocols/ + data/ + scripts/ |

**Validation checklist:**
- [ ] Simple task ≠ complex architecture
- [ ] Complex task ≠ oversimplified implementation
- [ ] File count matches scope
- [ ] Abstraction level matches need

**Violation examples:**
- ❌ Temperature converter → 5 modules
- ❌ Full IDE → single 200-line file
- ❌ 3 commands → state manager + router + validator

**Correct examples:**
- ✅ Temperature converter → 1 function
- ✅ Project system → project-architect scale
- ✅ 3 commands → inline handling in SKILL.md

---

### G10: Einstein's Balance

**Definition:** Skill must be as simple as possible, but no simpler.

**Manifestation in created skill:**

```markdown
## Completeness Check

Required features: [list]
Implemented features: [list]
Missing: [none / justified omissions]

Balance verification:
- All requirements: ✅ / ❌
- No feature bloat: ✅ / ❌
- Sufficient but not excessive: ✅ / ❌
```

**Validation checklist:**
- [ ] All stated requirements implemented
- [ ] No requirements simplified away
- [ ] No unnecessary features added
- [ ] Edge cases handled appropriately
- [ ] Error handling present

**Violation examples:**
- ❌ User wants A, B, C → skill has A, B (too simple)
- ❌ User wants A, B → skill has A, B, C, D, E (too complex)
- ❌ "Simplified" by removing error handling

**Correct examples:**
- ✅ User wants A, B, C → skill has A, B, C
- ✅ User wants "basic calc" → +,-,*,/ (not trig)
- ✅ Essential features + essential error handling

---

### Genetic Validation

**During P04-deliver, verify ALL genes:**

```markdown
## Genetic Validation Checklist

Legacy Genes:
- [ ] G01 Frontmatter present and valid
- [ ] G02 Purpose clearly stated
- [ ] G03 Flow diagram included
- [ ] G04 Commands table formatted
- [ ] G05 Anchor format in responses
- [ ] G06 Session indicator in responses
- [ ] G07 Blocking points marked

NEW Cognitive Genes:
- [ ] G08 Occam's: No unused sections
- [ ] G09 Hume's: Complexity proportional
- [ ] G10 Einstein's: Complete but not bloated

If ANY gene missing → fix before delivery.
```

**Test command:**
```bash
test-architect test [skill-path] --genetic
```

This should validate all 10 genes.

---

### Genetic Inheritance Example

**User request:**
"Create a skill for converting units (temperature, length, weight)"

**skill-architect applies razors:**

1. **Occam's (G08):** 
   - Simple: 3 conversion functions in SKILL.md
   - Not: Separate modules, plugin system, extensibility framework

2. **Hume's (G09):**
   - Task = Medium (3 domains, 9 conversions)
   - Implementation = Medium (structured but not over-engineered)
   - Not: Simple (missing domains) or Complex (unnecessary abstractions)

3. **Einstein's (G10):**
   - Required: temp (C/F/K), length (m/ft/in), weight (kg/lb/oz)
   - Implemented: exactly that
   - Not: Missing conversions or adding currency/time/etc

**Created skill inherits:**

```markdown
---
name: unit-converter
description: "v1.0.0 | Convert temperature, length, weight units"
---

# Unit Converter

## Design Principle (G08: Occam's)

Simplest structure covering all requirements:
- 3 conversion domains in single file
- Direct formula implementation
- No unnecessary abstractions

## Scope Statement (G09: Hume's)

Task complexity: Medium (3 domains)
Implementation: Medium (structured, proportional)

## Completeness Check (G10: Einstein's)

Required features:
- ✅ Temperature: C, F, K
- ✅ Length: m, ft, in
- ✅ Weight: kg, lb, oz

Balance: All requirements met, no bloat.
```

---

### Why These 3 Genes?

**Occam's (G08):**
- Directly prevents overengineering in created skills
- Ensures every skill starts minimal
- Inherited by nature of architecture choices

**Hume's (G09):**
- Prevents both over/under-engineering
- Creates proportional designs
- Visible in file structure

**Einstein's (G10):**
- Ensures completeness
- Prevents both feature creep and feature cuts
- Balances simplicity with sufficiency

**NOT genes (workflow only):**

**Hanlon's:** 
- About MY emotional response to feedback
- Not applicable to skill behavior
- Stays in skill-architect internals

**Grice's:**
- About MY interpretation of requests
- Not applicable to skill documentation
- Stays in P01-init

**Hitchens':**
- About MY handling of ambiguity
- Not applicable to skill design
- Stays in P01-init + P02-plan

---

### Validation in test-architect

**New test cases needed:**

```markdown
## G08: Occam's Design Test

Check:
- [ ] No sections with zero references
- [ ] No files with <50 lines content
- [ ] No abstractions used once
- [ ] Protocol count ≤ command count
- [ ] Module count ≤ domain count

Score: Pass if all checks pass
```

```markdown
## G09: Hume's Scale Test

Measure:
- Command count
- File count
- Total lines

Compare:
- 1-5 commands → 1 file, <500 lines
- 6-15 commands → 1-3 files, <1500 lines
- 15+ commands → 3+ files OK

Score: Pass if proportional
```

```markdown
## G10: Einstein's Balance Test

Extract:
- Requirements from README/description
- Implemented features from SKILL.md

Verify:
- All requirements present
- No extra features (unless justified)

Score: Pass if balanced
```

---

### Documentation Requirements

**Every created skill MUST include:**

```markdown
## Genetic Markers

This skill inherits:
- G08 Occam's Design: [1-line justification]
- G09 Hume's Scale: [task=X, implementation=X]
- G10 Einstein's Balance: [requirements met: Y/Y]
```

**In README-{name}.md:**

Brief explanation in user's language why the skill is designed this way.

---

### Backward Compatibility

**Existing skills without G08-G10:**
- Still valid (genes are additive)
- Recommended to add on next update
- test-architect shows "missing genes" warning

**Migration path:**
1. Identify existing skills
2. Add genetic markers section
3. Verify compliance
4. Document in DIFF

---

## Rollback Plan

If razors cause issues:
1. Razors = suggestions, not mandates
2. Can be ignored when justified
3. Document when/why razor was skipped
4. Review if pattern emerges

**Gene rollback:**
- If G08-G10 prove problematic, can be deprecated
- Existing skills with G08-G10 remain valid
- New skills revert to G01-G07 only

---

## Example: Before/After

### Before (Current skill-architect):

```
User: "Make me a timer skill"
Me: *Creates Planning Document with*
  - Multi-format timer (countdown, stopwatch, pomodoro)
  - Persistent state management
  - Notification system
  - History tracking
  - Analytics
  - Export functionality
  - Configuration module
  Result: 180-line plan, 4 files, 2 weeks
  Genes: G01-G07 only
```

### After (With Razors + Genes):

```
User: "Make me a timer skill"
Me: [Grice's] What did they mean? Probably simple countdown.
    [Hitchens'] What's stated? Just "timer". ASK.
    
    "What kind of timer? Simple countdown or full time-tracking?"
    
User: "Just countdown"
Me: [Occam's] Simplest: 1 command, basic countdown
    [Hume's] Simple request = simple solution
    [Einstein's] Sufficient = countdown that works
    
    Result: 40-line SKILL.md, 1 file, 2 hours
    Genes: G01-G10 including:
      - G08: Single-file design, no abstractions
      - G09: Simple task → simple implementation
      - G10: Countdown feature complete, no extras
```

**Created skill contains:**

```markdown
---
name: timer
description: "v1.0.0 | Simple countdown timer"
---

# Timer

## Design Principle (G08)
Single command in SKILL.md. No separate modules.

## Scope Statement (G09)
Task: Simple (1 feature)
Implementation: Simple (1 file, <100 lines)

## Completeness Check (G10)
Required: countdown
Implemented: countdown
Balance: ✅
```

---

## Version Changes

### v4.2.0 → v4.3.0

**Added:**
- Cognitive Razors framework (6 razors)
- **3 new genes (G08, G09, G10)**
- Pre-protocol checklist
- Intent interpretation in P01
- Design razors in P02
- Build razors in P03
- Feedback razors in P04
- Genetic transmission documentation
- Genetic validation checklist

**Changed:**
- Planning approach: minimum sufficient → explicit
- Response tone: defensive → collaborative
- Ambiguity handling: assume → ask
- **Required Genes: 7 → 10**

**Gene additions:**
- G08 Occam's Design: simplest sufficient structure
- G09 Hume's Scale: complexity matches task
- G10 Einstein's Balance: simple but not simplified

**Reasoning:**
Current issues (overplanning, assumptions, defensiveness) stem from lack of explicit decision framework. Razors provide:
1. Clear rules for "how simple?"
2. Framework for "when to ask?"
3. Mindset for "how to respond?"
4. **Inheritable design principles for created skills**

---

## Notes

**Why these 6 razors specifically?**

Tested against skill-architect's actual workflow:
- Occam's → directly addresses overplanning
- Hanlon's → directly addresses defensiveness
- Grice's → directly addresses misinterpretation
- Hume's → directly addresses over-engineering
- Hitchens' → directly addresses assumptions
- Einstein's → prevents over-simplification

**Why not other razors?**
- Popper's Falsifiability → not applicable to skill creation
- Sagan's Standard → not applicable to skill creation
- Newton's Laser Sword → covered by Hitchens'
- Hume's Guillotine → too abstract for workflow

---

*This update plan to be reviewed and confirmed before implementation.*
