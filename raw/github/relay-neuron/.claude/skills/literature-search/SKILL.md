---
name: literature-search
description: PubMed and SPORTDiscus search strategies for exercise science literature review
version: 1.0.0
author: Relay Neuron Research
license: MIT
tags: [Exercise Science, Research, Literature Search, Database]
dependencies: [mcp__MiniMax__web_search]
---

# Literature Search Skill

## Quick Start

Use this skill when you need to find exercise science research. This skill provides database-specific search strategies for PubMed, SPORTDiscus, and other exercise science databases.

## Core Workflow

1. **Define search scope** - Topic, time range, study types
2. **Build search string** - Keywords, MeSH terms, boolean operators
3. **Execute search** - Use `mcp__MiniMax__web_search`
4. **Filter results** - By relevance, date, study type
5. **Extract citations** - DOI, author, year, journal

## Search String Templates

### Muscle Hypertrophy
```
("resistance training" OR "strength training") AND ("muscle hypertrophy" OR "muscle growth" OR "skeletal muscle hypertrophy")
```

### Protein Synthesis
```
("protein synthesis" OR "muscle protein synthesis") AND ("mTOR" OR "mechanistic target of rapamycin")
```

### Blood Flow Restriction
```
("blood flow restriction" OR "BFR" OR "occlusion training") AND ("muscle hypertrophy" OR "strength")
```

### Creatine Supplementation
```
("creatine" OR "creatine monohydrate") AND ("supplementation" OR "exercise performance")
```

### Periodization
```
("periodization" OR "training periodization") AND ("resistance training" OR "strength training")
```

### High-Altitude Training
```
("high altitude" OR "hypoxic training") AND ("erythropoiesis" OR "VO2max" OR "performance")
```

## Time Filters

- **Default:** 2024-01-01 to 2026-12-31
- **Classic studies:** Include foundational papers regardless of date
- **Recent reviews:** Prioritize 2024-2026 meta-analyses and systematic reviews

## Database Priority

1. **PubMed** - Primary database for biomedical research
2. **SPORTDiscus** - Exercise science and sports medicine
3. **Cochrane Library** - Systematic reviews
4. **Google Scholar** - Supplementary search

## Search Strategy by Topic

### For New Topics
1. Start with broad search using main keywords
2. Filter to 2024-2026 for recent findings
3. Identify key authors/journals in field
4. Search cited references of key papers
5. Cross-reference with related terms

### For Deep Dive
1. Use MeSH terms for precise retrieval
2. Combine multiple related terms
3. Filter by study type (RCT > cohort > case study)
4. Look for dose-response studies

## Boolean Operators

- **AND** - Both terms must appear
- **OR** - Either term can appear
- **NOT** - Exclude term
- **""** - Exact phrase
- **()** - Grouping

Example:
```
("resistance training" OR "strength training") AND ("muscle hypertrophy" OR "muscle growth") NOT "review"
```

## Citation Extraction

For each relevant paper, extract:
- Authors (first 3 + et al.)
- Year
- Journal
- DOI/URL
- Study design (RCT, cohort, etc.)
- Sample size
- Key findings

## Quality Indicators

**Prioritize:**
- Peer-reviewed journals
- Impact factor > 3.0
- Recent systematic reviews
- Multi-site studies
- Registered trials (ClinicalTrials.gov)

**Include cautiously:**
- Preprints (cite with note)
- Industry-funded studies
- Small sample sizes (n < 20)

## Integration Points

- Output feeds into `bri-structure` for document writing
- Uses `mcp__MiniMax__web_search` for execution
- References `citation-verification` for validation
- Results saved to research files

## Search Record Template

```markdown
## Search Record

**Date:** YYYY-MM-DD
**Topic:** [Topic Name]
**Database:** PubMed/SPORTDiscus

**Search String:**
```
[Full search string]
```

**Results:** [Number] papers found
**Relevant:** [Number] papers selected

**Papers:**
1. [Author, Year] - [Title] - [DOI]
2. ...
```

## When to Use

**Use literature-search when:**
- Starting new research topic
- Updating existing topic with new findings
- Searching for specific study types

**Use other skills instead:**
- `citation-verification` - When you have citations and need to verify
- `study-quality-appraisal` - When assessing paper quality
