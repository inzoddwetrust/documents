---
name: venture-360-lite
description: Lightweight project analysis framework for quick venture assessment (5-15 min). Analyzes crypto and traditional startups using 100-point scoring system across 5 dimensions. Designed for fast screening via Claude API with web verification. Outputs structured markdown reports. Best for initial screening, batch processing, and automated analysis pipelines.
---

# Venture 360° LITE - Quick Project Analysis

**Version**: 1.0-lite | **Processing Time**: 5-15 minutes | **Format**: JSON → Markdown  
**Use Case**: Fast screening, API integration, batch processing

## 🎯 Overview

This is a **lightweight version** of the Venture 360° framework, optimized for:
- ✅ **Fast processing** via Claude API (5-15 min per project)
- ✅ **Simplified scoring** (100 points vs 360 in full version)
- ✅ **Both crypto and traditional** startups
- ✅ **Automated workflows** with JSON input/output
- ✅ **Web verification** of key claims

---

## 📊 Scoring System (100 Points Total)

### 5 Core Dimensions (20 points each):

#### 1. **Team** (0-20 points)
**What to evaluate:**
- Founder experience and expertise
- Team completeness (tech + business)
- Advisors and network
- Track record of execution

**Scoring bands:**
- **18-20**: Exceptional - experienced founders with exits/deep domain expertise
- **15-17**: Strong - solid backgrounds, complete team
- **12-14**: Adequate - some experience, key roles filled
- **9-11**: Weak - limited experience or incomplete team
- **0-8**: Critical - major gaps or no relevant experience

#### 2. **Product** (0-20 points)
**What to evaluate:**
- Development status (MVP/Beta/Live)
- Core functionality and features
- Technical implementation
- Differentiation from competitors

**Scoring bands:**
- **18-20**: Exceptional - live product with strong traction
- **15-17**: Strong - beta/MVP with clear value proposition
- **12-14**: Adequate - working prototype, basic features
- **9-11**: Weak - early concept, unclear execution
- **0-8**: Critical - no working product or poor quality

#### 3. **Market** (0-20 points)
**What to evaluate:**
- Industry/niche attractiveness
- Market size and growth potential
- Competitive landscape
- Positioning and timing

**Scoring bands:**
- **18-20**: Exceptional - large growing market, clear opportunity
- **15-17**: Strong - attractive niche, manageable competition
- **12-14**: Adequate - viable market, competitive
- **9-11**: Weak - small/saturated market
- **0-8**: Critical - no clear market or declining

#### 4. **Traction** (0-20 points)
**What to evaluate:**
- Users/customers and growth
- Revenue (if any)
- Partnerships and integrations
- Media coverage and community

**Scoring bands:**
- **18-20**: Exceptional - strong metrics, rapid growth
- **15-17**: Strong - good traction, consistent growth
- **12-14**: Adequate - early traction, some validation
- **9-11**: Weak - minimal traction
- **0-8**: Critical - no traction or declining

#### 5. **Economics/Tokenomics** (0-20 points)
**What to evaluate:**

**For Crypto:**
- Token distribution fairness
- Vesting schedules
- Economic model sustainability
- Utility and value capture

**For Traditional Startups:**
- Business model clarity
- Revenue streams
- Unit economics (CAC/LTV if known)
- Funding and runway

**Scoring bands:**
- **18-20**: Exceptional - strong economics, clear value capture
- **15-17**: Strong - solid model, sustainable
- **12-14**: Adequate - working model, some concerns
- **9-11**: Weak - questionable economics
- **0-8**: Critical - unsustainable or unfair

---

## 🎯 Final Categories

**Total Score → Recommendation:**

- **🌟 90-100**: Отличный проект - требует детального изучения для подтверждения потенциала
- **✅ 70-89**: Хороший проект - необходимо детальное изучение для выявления возможностей
- **⚖️ 50-69**: Средний проект - требуется углублённое изучение, есть риски
- **⚠️ 30-49**: Слабый проект - необходим детальный анализ для выявления скрытых факторов  
- **❌ 0-29**: Критический - требует экспертного анализа (возможность пивота?)

---

## 📥 Input Format (JSON)

```json
{
  "project_url": "https://example.com",
  "parsed_at": "2025-11-19T12:00:00Z",
  "content_hash": "abc123def456",
  
  "basic_info": {
    "title": "Project Name",
    "tagline": "One-line description",
    "description": "Full description...",
    "industry": "DeFi | Gaming | AI | SaaS | etc"
  },
  
  "team": {
    "founders": [
      {
        "name": "Founder Name",
        "role": "CEO",
        "linkedin": "url",
        "bio": "Background..."
      }
    ],
    "team_size": 10,
    "advisors": ["Advisor 1", "Advisor 2"]
  },
  
  "product": {
    "status": "MVP | Beta | Live",
    "description": "What it does...",
    "features": ["Feature 1", "Feature 2"],
    "technology": ["Tech stack"]
  },
  
  "market": {
    "target": "Target audience",
    "competitors": ["Competitor 1"],
    "market_size": "Optional"
  },
  
  "traction": {
    "users": "10K+ users",
    "revenue": "N/A or amount",
    "partnerships": ["Partner 1"],
    "media": ["Coverage 1"]
  },
  
  "tokenomics": {
    "token": "TOKEN",
    "supply": "1,000,000,000",
    "distribution": {
      "team": "20%",
      "investors": "15%",
      "community": "65%"
    },
    "vesting": "Description"
  },
  
  "funding": {
    "stage": "Seed | Series A",
    "raised": "$1M",
    "investors": ["Investor 1"],
    "valuation": "N/A"
  },
  
  "roadmap": [
    {
      "period": "Q4 2024",
      "milestones": ["Milestone 1"]
    }
  ],
  
  "social": {
    "twitter": "url",
    "discord": "url",
    "telegram": "url",
    "github": "url"
  },
  
  "extracted_text": "All relevant text..."
}
```

---

## 📤 Output Format (Markdown Report)

### Structure:

```markdown
# 🔍 Анализ проекта: [Project Name]

**Дата:** [Date]  
**URL:** [URL]  
**Индустрия:** [Industry]

---

## 📊 Общая оценка: [Score]/100 [Emoji]

**Категория:** [Category Description]

### Детальные оценки:

| Критерий | Оценка | Комментарий |
|----------|--------|-------------|
| 👥 Команда | XX/20 | ... |
| 💡 Продукт | XX/20 | ... |
| 📈 Рынок | XX/20 | ... |
| 🚀 Трекшн | XX/20 | ... |
| 💰 Экономика | XX/20 | ... |

---

## 🎯 Ключевые сильные стороны

1. **[Strength 1]** - description
2. **[Strength 2]** - description
3. **[Strength 3]** - description

---

## ⚠️ Основные риски

1. **[Risk 1]** - description
2. **[Risk 2]** - description
3. **[Risk 3]** - description

---

## 🔎 Детальный анализ

### 👥 Команда (XX/20)
[Detailed analysis...]

### 💡 Продукт (XX/20)
[Detailed analysis...]

### 📈 Рынок (XX/20)
[Detailed analysis...]

### 🚀 Трекшн (XX/20)
[Detailed analysis...]

### 💰 Экономика/Токеномика (XX/20)
[Detailed analysis...]

---

## 💡 Рекомендации

1. **Немедленно (0-1 мес)** - [actions]
2. **Краткосрочно (1-3 мес)** - [actions]
3. **Долгосрочно (3-6 мес)** - [actions]

---

## 📋 Выводы

**Итоговая рекомендация:** [ИЗУЧИТЬ ДЕТАЛЬНЕЕ / НАБЛЮДАТЬ / ИЗУЧИТЬ С ОСТОРОЖНОСТЬЮ]

**Обоснование:** [Summary]

---

*Отчёт сгенерирован автоматически. Не является инвестиционной рекомендацией.*
*Для детального анализа рекомендуется заказать полную версию отчёта.*
```

---

## 🔍 Analysis Workflow

When you receive a JSON input:

### Step 1: Parse and Validate
- Read all fields from JSON
- Identify project type (crypto vs traditional)
- Note any missing critical information

### Step 2: Web Verification (if URL provided)
Use `web_search` to verify:
```
web_search("Project Name team founders")
web_search("Project Name token OR funding")  
web_search("Project Name reviews OR scam")
web_search("Competitor comparison Project Name")
```

### Step 3: Score Each Dimension
For each of 5 dimensions:
- Review the data provided
- Apply scoring bands (0-20)
- Justify the score with specific evidence
- Note red flags or exceptionally positive signals

### Step 4: Calculate Total Score
- Sum all 5 dimension scores (max 100)
- Assign category based on total
- Identify top 3 strengths and top 3 risks

### Step 5: Generate Report
- Follow the markdown structure exactly
- Keep language clear and professional (Russian)
- Include specific data points, not generic statements
- End with clear actionable recommendations

---

## ⚠️ Important Notes

### What This Analysis Provides:
- ✅ Structured initial screening
- ✅ Data-driven scoring framework
- ✅ Web-verified key claims
- ✅ Risk identification
- ✅ Directional recommendations

### What This Analysis Does NOT Replace:
- ❌ Full due diligence process
- ❌ Financial audit
- ❌ Technical code review
- ❌ Legal compliance check
- ❌ Deep customer interviews
- ❌ Reference checks

### Best Used For:
- First-pass screening of projects
- Batch processing multiple projects
- Consistent evaluation criteria
- Identifying which projects warrant deeper DD
- Structuring thinking for investment memos

---

## 🎯 Usage Example

**Input:** JSON file with parsed project data  
**Process:** 
1. Validate JSON structure
2. Run web searches for verification  
3. Score 5 dimensions with evidence
4. Generate markdown report

**Output:** Structured markdown file ready for:
- PDF conversion
- Database storage
- Further human review
- Batch comparison

**Time:** 5-15 minutes per project

---

## 📊 Quality Standards

**For Each Score:**
- Cite specific evidence from input data
- Reference web search findings when available
- Explain reasoning clearly
- Be consistent across projects

**For Final Report:**
- No generic statements
- Specific numbers and facts
- Balanced view (not overly optimistic or pessimistic)
- Clear next steps

**Verification:**
- Always attempt web search for key claims
- Note when claims cannot be verified
- Flag suspicious or contradictory information

---

## 🚀 Integration

This skill is designed to work with:
- **Claude API** (via programmatic calls)
- **Automated pipelines** (JSON in → Markdown out)
- **Batch processing** (multiple projects)
- **Database integration** (store results)

For full comprehensive analysis (40-80 hours), use the main Venture 360° framework.

---

*Version: 1.0-lite | Last Updated: November 2025 | License: MIT*
