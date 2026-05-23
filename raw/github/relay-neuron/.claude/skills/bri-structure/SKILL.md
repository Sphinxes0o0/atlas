---
name: bri-structure
description: B-M-R-I (Background/Method/Results/Interpretation) document template for exercise science research papers
version: 1.0.0
author: Relay Neuron Research
license: MIT
tags: [Exercise Science, Research, Writing, Template]
dependencies: []
---

# B-M-R-I Structure Skill

## Quick Start

Use this skill when you need to write a structured exercise science research document. The B-M-R-I format provides a standardized structure for research reports with Background, Method, Results, and Interpretation sections.

## Document Structure

### Header Block
```markdown
# [Topic Title]

**Research Date:** YYYY-MM-DD
**Topic:** [Description]
**Search Scope:** 2024-2026 literature review

---
```

### Required Sections

#### 1. Abstract / 摘要
- 150-250 words summary
- Research question, methods, key findings, conclusions

#### 2. Key Findings with Citations / 关键发现
- 3-5 named studies per document
- Full citations: author, year, journal, DOI
- Use format: `([Author, Year](URL))`

#### 3. Background (B)
**Purpose:** Establish research context and significance

Content:
- Current state of knowledge
- Research gap identification
- Study objectives

Word target: 300-500 words

#### 4. Method (M)
**Purpose:** Document research methodology

Content:
- Search strategy (databases, keywords, time range)
- Inclusion/exclusion criteria
- Data extraction methods

Word target: 200-400 words

#### 5. Results (R)
**Purpose:** Present findings with evidence

Content:
- Study characteristics (n, population, intervention)
- Key outcomes with specific data (effect sizes, p-values)
- Citation-backed claims

Word target: 400-600 words per study

#### 6. Interpretation (I)
**Purpose:** Analyze and contextualize findings

Content:
- Mechanism explanations
- Practical applications
- Limitations
- Future research directions

Word target: 300-500 words

#### 7. Conclusions / 结论
- Summary of main findings
- Practical takeaways
- Every conclusion must cite source

#### 8. Data Sources / 数据来源
- PubMed, SPORTDiscus, etc.
- Search dates

#### 9. References / 参考文献
- Full citation list in relay-neuron format

## Quality Standards

| Metric | Minimum | Ideal |
|--------|---------|-------|
| Citations per document | 3-5 | 5+ |
| Words per study | 1,000 | 1,500+ |
| Total characters | 3,000 | 5,000+ |
| Cited conclusions | 100% | 100% |

## Citation Format

**In-body citation:**
```markdown
([Kreider et al., 2017](https://pubmed.ncbi.nlm.nih.gov/...)
```

**Reference list:**
```markdown
- Kreider et al., 2017. Journal of the International Society of Sports Nutrition. [Link](URL)
```

## Integration Points

- References `literature-search` for database access
- Uses `mcp__MiniMax__web_search` for literature search
- Output goes to `research/` directory
- Naming: `YYYY-MM-DD-task-X-X-TOPIC.md`

## Examples

See existing research files:
- `research/2026-05-12-task-1-1-neuroscience-neural-drive.md`
- `research/2026-05-12-task-1-2-neuroscience-fatigue-mechanisms.md`

## When to Use

**Use B-M-R-I when:**
- Writing new research topic files
- Expanding existing research topics
- Creating supplement-specific analysis

**Don't use when:**
- Updating RESEARCH_MASTER_LIST.md
- Writing brief notes or annotations
- Creating simple task reminders
