# Project Architect v2.0: План разработки

**Дата:** 2025-11-28  
**Тип:** Полная переработка (MAJOR rewrite)  
**Версия:** v1.0 → v2.0.0

---

## 1. Концепция

### Что это
**Project Architect** — скилл-фреймворк для создания "живых" баз знаний проектов. Один проект = один скилл = единый источник правды (SSOT).

### Ключевой инсайт
Скилл проекта — это не генератор документов, а **RAG-база знаний**, которую Claude читает и использует для:
- Генерации любых документов (pitch, one-pager, FAQ, пост)
- Ответов на вопросы о проекте
- Поддержки клиентов/инвесторов
- Контент-маркетинга

### Формула
```
Данные (YAML) + Контекст (стадия/аудитория) + Запрос = Любой документ
```

---

## 2. Источники (что берём)

| Скилл | Берём | Не берём |
|-------|-------|----------|
| **modular-docs** | YAML frontmatter, SSOT принцип, типизация | Папочную структуру для людей |
| **project-architect v1** | Living Skill концепт, модули, update protocol | Шаблоны документов |
| **startup-docs** | Метрики, бенчмарки, формулы | Статичные шаблоны |
| **venture-catalyst** | Virtual testing, investor personas | Одноразовый отчёт |
| **project-docs** | ADR формат, discovery flow | Статичные документы |

---

## 3. Архитектура скилла

### Структура файлов
```
project-architect/
├── SKILL.md              # Главный контроллер (English, <300 lines)
├── README.md             # Документация для человека (Russian)
├── reference/
│   ├── modules.md        # Структура всех модулей данных
│   ├── stages.md         # Критическая масса по стадиям
│   ├── outputs.md        # Типы выходных документов
│   └── examples.md       # Примеры заполненных проектов
└── CHANGELOG.md          # История версий
```

### Структура генерируемого project-skill
```
[project-name]-project/
├── SKILL.md              # Интерфейс проекта
├── data/
│   ├── core.yaml         # Название, миссия, стадия
│   ├── team.yaml         # Команда, роли, история
│   ├── product.yaml      # Продукт, фичи, метрики
│   ├── market.yaml       # Рынок, конкуренты, позиционирование
│   ├── finances.yaml     # Финансы, runway, unit economics
│   ├── tech.yaml         # Стек, инфраструктура
│   ├── roadmap.yaml      # Цели, milestones
│   ├── risks.yaml        # Риски, митигации
│   ├── clients.yaml      # Клиенты, кейсы, отзывы
│   └── decisions.yaml    # ADR-записи
├── README.md             # Человекочитаемое описание
└── CHANGELOG.md          # История изменений данных
```

---

## 4. Модули данных (полный набор)

### 4.1 core.yaml
```yaml
project:
  name: ""
  tagline: ""           # One-liner
  description: ""       # 2-3 предложения
  stage: ""             # idea | mvp | growth | scale | mature
  type: ""              # startup | enterprise | consulting | personal
  founded: ""           # YYYY-MM
  location: ""
  website: ""
  
mission:
  problem: ""           # Какую боль решаем
  solution: ""          # Как решаем
  vision: ""            # Куда идём
  values: []            # Ценности команды

status:
  current_focus: ""     # На чём сейчас фокус
  last_updated: ""      # YYYY-MM-DD
```

### 4.2 team.yaml
```yaml
founders:
  - name: ""
    role: ""
    background: ""      # Релевантный опыт
    linkedin: ""
    
team:
  - name: ""
    role: ""
    joined: ""          # YYYY-MM
    status: active      # active | left | advisor
    
advisors:
  - name: ""
    expertise: ""
    
hiring:
  open_positions: []
  team_size_target: ""
  
history:              # Изменения в команде
  - date: ""
    event: ""
```

### 4.3 product.yaml
```yaml
product:
  name: ""
  type: ""              # SaaS | marketplace | hardware | service
  status: ""            # concept | prototype | beta | live
  
features:
  core:                 # Must-have
    - name: ""
      status: ""        # planned | in-progress | done
      description: ""
  differentiators:      # Что отличает от конкурентов
    - ""
    
metrics:
  users: ""
  active_users: ""
  growth_rate: ""       # MoM или YoY
  retention: ""
  nps: ""
  
tech_debt: []           # Известные проблемы
roadmap_link: ""        # Ссылка на roadmap.yaml
```

### 4.4 market.yaml
```yaml
market:
  tam: ""               # Total Addressable Market
  sam: ""               # Serviceable Addressable Market
  som: ""               # Serviceable Obtainable Market
  tam_source: ""        # Откуда данные
  growth_rate: ""       # Рост рынка YoY
  
target_customer:
  b2b:
    segment: ""         # SMB | Mid-market | Enterprise
    industry: []
    company_size: ""
    decision_maker: ""
  b2c:
    demographics: ""
    psychographics: ""
    
competitors:
  direct:
    - name: ""
      strengths: []
      weaknesses: []
      pricing: ""
  indirect:
    - name: ""
      threat_level: ""  # low | medium | high
      
positioning:
  category: ""          # В какой категории играем
  differentiation: ""   # Почему мы лучше
  unfair_advantage: ""  # Что сложно скопировать
```

### 4.5 finances.yaml
```yaml
revenue:
  model: ""             # subscription | transaction | ads | hybrid
  mrr: ""
  arr: ""
  growth_rate: ""
  
pricing:
  tiers:
    - name: ""
      price: ""
      features: []
      
unit_economics:
  cac: ""
  ltv: ""
  ltv_cac_ratio: ""
  payback_months: ""
  gross_margin: ""
  
funding:
  stage: ""             # bootstrapped | pre-seed | seed | series-a
  raised_total: ""
  last_round:
    amount: ""
    date: ""
    valuation: ""
    investors: []
  seeking:
    amount: ""
    use_of_funds: []
    
burn:
  monthly_burn: ""
  runway_months: ""
  
history:
  - date: ""
    event: ""           # raised, revenue milestone, etc.
```

### 4.6 tech.yaml
```yaml
stack:
  frontend: []
  backend: []
  database: []
  infrastructure: []
  tools: []
  
architecture:
  type: ""              # monolith | microservices | serverless
  diagram_link: ""
  
integrations:
  - name: ""
    purpose: ""
    status: ""          # active | planned | deprecated
    
security:
  certifications: []
  compliance: []        # GDPR, SOC2, etc.
  
scalability:
  current_capacity: ""
  bottlenecks: []
```

### 4.7 roadmap.yaml
```yaml
vision_2025: ""         # Где хотим быть через год

current_quarter:
  goal: ""
  okrs:
    - objective: ""
      key_results: []
      
milestones:
  completed:
    - name: ""
      date: ""
  upcoming:
    - name: ""
      target_date: ""
      dependencies: []
      
backlog:
  - item: ""
    priority: ""        # high | medium | low
    effort: ""          # S | M | L | XL
```

### 4.8 risks.yaml
```yaml
risks:
  - category: ""        # market | tech | team | financial | legal
    description: ""
    probability: ""     # low | medium | high
    impact: ""          # low | medium | high
    mitigation: ""
    owner: ""
    status: ""          # identified | mitigating | resolved
    
assumptions:
  - assumption: ""
    validated: false
    validation_method: ""
```

### 4.9 clients.yaml
```yaml
segments:
  - name: ""
    count: ""
    revenue_share: ""
    
key_accounts:
  - name: ""
    since: ""
    contract_value: ""
    use_case: ""
    testimonial: ""
    logo_permission: false
    
pipeline:
  - stage: ""           # lead | qualified | proposal | negotiation | closed
    count: ""
    value: ""
    
churn:
  rate: ""
  reasons: []
  
case_studies:
  - client: ""
    problem: ""
    solution: ""
    results: ""
```

### 4.10 decisions.yaml
```yaml
decisions:
  - id: "ADR-001"
    title: ""
    date: ""
    status: ""          # proposed | accepted | deprecated | superseded
    context: ""
    decision: ""
    consequences: []
    alternatives_considered: []
```

---

## 5. Стадии и критическая масса

### 5.1 Матрица обязательности

| Модуль | Idea | MVP | Growth | Scale |
|--------|------|-----|--------|-------|
| core | ✅ full | ✅ full | ✅ full | ✅ full |
| team | 👤 founders | 👥 +key hires | 👥 full | 👥 full |
| product | 💡 concept | 🔧 features | 📊 +metrics | 📊 +metrics |
| market | 🎯 target | 🎯 +competitors | 📈 TAM/SAM/SOM | 📈 full |
| finances | — | 💰 basic | 💰 unit economics | 💰 full |
| tech | — | 🔧 stack | 🔧 +architecture | 🔧 full |
| roadmap | 🎯 vision | 🎯 +milestones | 🎯 +OKRs | 🎯 full |
| risks | — | ⚠️ top 3 | ⚠️ full | ⚠️ full |
| clients | — | — | 👥 key accounts | 👥 full |
| decisions | — | 📝 key ADRs | 📝 ongoing | 📝 ongoing |

### 5.2 Критическая масса для документов

| Документ | Минимум модулей |
|----------|-----------------|
| Pitch Deck | core, team, product, market, finances |
| One-Pager | core, product, market |
| Investor Update | core, product, finances, roadmap |
| Job Posting | core, team, product, tech |
| Press Release | core, product, market |
| FAQ (Support) | core, product, clients |
| Blog Post | core, product (+ тема) |
| Sales Deck | core, product, market, clients |

---

## 6. Процесс работы скилла

### 6.1 Режимы работы

```
┌─────────────────────────────────────────────────────┐
│                 PROJECT ARCHITECT                    │
├─────────────────────────────────────────────────────┤
│  MODE 1: CREATE                                      │
│  "создай скилл проекта" / "new project skill"       │
│  → Интерактивный сбор данных                        │
│  → Генерация project-skill                          │
│  → .skill файл                                      │
├─────────────────────────────────────────────────────┤
│  MODE 2: IMPORT                                      │
│  User uploads: pitch deck, docs, descriptions       │
│  → Автоматический парсинг                           │
│  → Раскладка по модулям                             │
│  → Верификация с пользователем                      │
│  → .skill файл                                      │
├─────────────────────────────────────────────────────┤
│  MODE 3: UPDATE (внутри project-skill)              │
│  "обнови team" / "Вася ушёл"                        │
│  → Определение модуля                               │
│  → Обновление данных                                │
│  → Запись в CHANGELOG                               │
│  → Новая версия .skill                              │
├─────────────────────────────────────────────────────┤
│  MODE 4: GENERATE (внутри project-skill)            │
│  "сделай pitch deck" / "напиши пост о запуске"     │
│  → Проверка критической массы                       │
│  → Сбор данных из модулей                          │
│  → Поиск best practices (если нужно)               │
│  → Генерация документа                              │
└─────────────────────────────────────────────────────┘
```

### 6.2 CREATE Flow

```
1. Определяем стадию проекта
   ↓
2. Показываем что нужно заполнить (по матрице)
   ↓
3. Собираем данные:
   - Интерактивно (вопросы)
   - Или из загруженных файлов
   - Или комбинация
   ↓
4. Заполняем пробелы:
   - Поиск по рынку/конкурентам
   - Предлагаем добавить
   ↓
5. Верификация с пользователем
   ↓
6. Генерация project-skill
   ↓
7. .skill файл + Quick Start
```

### 6.3 UPDATE Flow

```
Триггер: любое упоминание изменений
   ↓
Определяем модуль(и)
   ↓
Обновляем данные в YAML
   ↓
Записываем в CHANGELOG:
  - date: YYYY-MM-DD
  - module: team
  - change: "Вася ушёл, пришла Маша"
   ↓
Версия: patch bump (v1.0.0 → v1.0.1)
   ↓
Предлагаем скачать обновлённый .skill
```

### 6.4 GENERATE Flow

```
Запрос: "сделай pitch deck для Series A"
   ↓
Проверяем критическую массу
   ↓
Если не хватает данных:
  → "Для pitch deck нужны finances. Заполним?"
   ↓
Собираем данные из модулей
   ↓
Определяем аудиторию/контекст
   ↓
Поиск: актуальные бенчмарки, примеры
   ↓
Генерация документа
   ↓
Артефакт / файл
```

---

## 7. SKILL.md структура

```markdown
---
name: project-architect
description: "v2.0.0 | Create living project knowledge bases. 
Triggers: create project skill, new project, импорт проекта."
---

# Project Architect

Create single-source-of-truth skills for any project.

## Modes

### CREATE — New project skill
### IMPORT — From existing docs  
### [Inside project-skill] UPDATE — Modify data
### [Inside project-skill] GENERATE — Create documents

## CREATE Process

[Simplified flow]

## Data Modules

[List of 10 modules with brief description]
→ See reference/modules.md for full structure

## Stage Requirements

[Matrix: stage × modules]
→ See reference/stages.md

## Output Types

[List of document types]
→ See reference/outputs.md

## Commands

[Inside generated project-skill]
- "show status"
- "update [module]"
- "create [document]"
- "what's missing for [document]?"

## Critical Rules

- One project = one skill
- YAML for data (machine-readable)
- Always verify with user
- Search for missing market data
- CHANGELOG on every update

## Context Tracking

🟡 -[cost] | ~[remaining] 🟢
```

---

## 8. План реализации

### Phase 1: Подготовка (30 мин)
- [ ] Финализировать YAML-схемы модулей
- [ ] Определить discovery questions для каждого модуля
- [ ] Написать reference/modules.md
- [ ] Написать reference/stages.md

### Phase 2: Ядро (45 мин)
- [ ] Написать SKILL.md (главный контроллер)
- [ ] Написать CREATE flow
- [ ] Написать IMPORT flow
- [ ] Тестовая генерация project-skill

### Phase 3: Project-Skill Template (30 мин)
- [ ] Шаблон SKILL.md для генерируемого скилла
- [ ] UPDATE protocol
- [ ] GENERATE protocol
- [ ] CHANGELOG format

### Phase 4: Reference & Examples (20 мин)
- [ ] reference/outputs.md — типы документов
- [ ] reference/examples.md — пример заполненного проекта
- [ ] README.md (русский)

### Phase 5: Validation & Packaging (15 мин)
- [ ] validate-skill.sh
- [ ] Тест CREATE flow
- [ ] Тест UPDATE flow
- [ ] Тест GENERATE flow
- [ ] Упаковка v2.0.0

**Total: ~2.5 часа**

---

## 9. Риски

| Риск | Вероятность | Митигация |
|------|-------------|-----------|
| SKILL.md > 350 lines | High | Агрессивный вынос в reference/ |
| Сложный CREATE flow | Medium | Адаптивные вопросы по стадии |
| YAML слишком сложный | Medium | Примеры + авто-заполнение |
| Потеря данных при UPDATE | Low | CHANGELOG + версионирование |

---

## 10. Backlog (v2.1+)

### v2.1 — Интеграции
- [ ] GitHub repo sync (push/pull данных)
- [ ] Notion import
- [ ] Google Docs import

### v2.2 — Расширения
- [ ] Template packs (industry-specific)
- [ ] Multi-language support
- [ ] Export to different formats

### v2.3 — Продвинутые фичи
- [ ] "Человек как проект" — personal brand skill
- [ ] Virtual assistant mode (секретарь)
- [ ] Auto-update reminders
- [ ] Связка проектов (портфолио)

### v3.0 — AI-native
- [ ] Embeddings для семантического поиска
- [ ] Auto-enrichment (фоновый сбор данных)
- [ ] Anomaly detection (метрики упали)
- [ ] Competitor monitoring

---

## 11. Чеклист подтверждения

- [ ] Концепция понятна
- [ ] Архитектура модулей согласована
- [ ] Процессы (CREATE/UPDATE/GENERATE) ок
- [ ] План реализации реалистичен
- [ ] Риски приемлемы
- [ ] Backlog записан

**Ожидаю подтверждение для старта разработки.**

---

*Project Architect v2.0 Development Plan | 2025-11-28*
