# Exercise Science Research Assistant - Core Behavioral Rules

**Version:** 1.0.0
**Project:** Relay Neuron (转接神经元)
**Last Updated:** 2026-05-23

---

## File Naming Convention

All research files must follow this naming pattern:

| Research Type | Filename Pattern | Example |
|---------------|------------------|---------|
| Individual topics | `YYYY-MM-DD-task-X-X-TOPIC.md` | `2026-05-23-task-3-2-periodization.md` |
| Research rounds | `YYYY-MM-DD-research-round-N.md` | `2026-05-23-research-round-25.md` |

- Date format: `YYYY-MM-DD` (ISO 8601)
- Task prefix: `task-X-X-` where first X is section number, second X is topic number
- Topic: Short descriptive name in lowercase with hyphens

---

## Research Directory Structure

```
relay-neuron/
└── research/
    ├── YYYY-MM-DD-task-X-X-TOPIC.md         # Individual research files
    ├── YYYY-MM-DD-task-X-X-TOPIC-SUPPLEMENT.md  # Supplementary materials
    └── YYYY-MM-DD-research-round-N.md        # Consolidated research rounds
```

---

## Citation Standards

### Citation Format (Mandatory)

Every conclusion must include a source citation in this format:

```markdown
([Author, Year](URL))
```

**Examples:**
- `([Kreider et al., 2017](https://pubmed.ncbi.nlm.nih.gov/...))`
- `([Morton et al., 2018](https://doi.org/...))`
- `([Schoenfeld, 2024](https://www.ncbi.nlm.nih.gov/pmc/...))`

### Citation Quality Thresholds

| Metric | Minimum | Target |
|--------|---------|--------|
| Citations per document | 3-5 | 5+ |
| Words per study | 1,000 | 1,500+ |
| Total document length | 3,000 chars | 5,000+ chars |
| Cited conclusions | 100% | 100% |

### Source Priority

When multiple sources are available, use this priority order:

1. **PubMed** - Primary source for biomedical literature
2. **Nature/Science** - High-impact peer-reviewed journals
3. **Sports Medicine journals** - JSSCR, SMR, JIF
4. **Preprints (arXiv, medRxiv)** - Only when peer-reviewed sources unavailable

---

## B-M-R-I Document Structure

All research documents must follow the B-M-R-I format:

### Required Sections

1. **Header Block** - Title, date, research type
2. **Abstract/摘要** - 150-250 words summary
3. **Background (B)** - Research context, gap identification (300-500 words)
4. **Method (M)** - Search strategy, inclusion criteria (200-400 words)
5. **Results (R)** - Findings with specific data and citations (400-600 words per study)
6. **Interpretation (I)** - Analysis, mechanisms, applications (300-500 words)
7. **Conclusions/结论** - Summary with cited takeaways
8. **Data Sources/数据来源** - Databases, search dates
9. **References/参考文献** - Full citation list

---

## Language Support (Bilingual)

- **Primary language:** English with Chinese supplements
- **Document title:** Chinese first, English second
- **Section headers:** Bilingual (Chinese / English)
- **Key terms:** Include Chinese translation on first mention

Example:
```markdown
## 1. 基础生物学机制 (Basic Biological Mechanisms)
```

---

## MCP Tool Usage

### Primary Search Tool

Use `mcp__MiniMax__web_search` for all literature searches.

**Search parameters:**
- Keywords: "resistance training", "muscle hypertrophy", "exercise science", "protein synthesis", "fitness research"
- Time filter: 2024-01-01 to 2026-12-31
- Language: Prioritize English with Chinese abstracts

### Search Strategy

1. Start with broad search terms
2. Refine based on initial results
3. Cross-reference with PubMed IDs
4. Verify citations are accessible

### Database Targets

| Database | URL | Access |
|----------|-----|--------|
| PubMed | https://pubmed.ncbi.nlm.nih.gov | Primary |
| SPORTDiscus | Via EBSCO | Secondary |
| Nature | https://nature.com | Impact |
| ScienceDirect | https://sciencedirect.com | Secondary |
| arXiv | https://arxiv.org | Preprints |

---

## Integration with Research Workflow

### Existing File References

- **Task list:** `RESEARCH_MASTER_LIST.md` - Contains all pending and completed tasks
- **Project overview:** `CLAUDE.md` - General project guidance
- **Research directory:** `research/` - All research output files

### Workflow Steps

1. Check `RESEARCH_MASTER_LIST.md` for pending tasks
2. Use `mcp__MiniMax__web_search` to gather literature
3. Write findings in B-M-R-I format
4. Save to `research/` with correct naming
5. Update task status in `RESEARCH_MASTER_LIST.md`
6. Commit changes with `git add research/ && git commit -m "Research: [topic]"`

### B-M-R-I Skill Integration

When writing B-M-R-I structured documents:
- Reference skill: `.claude/skills/bri-structure/skill.md`
- Follow word targets per section
- Maintain citation quality thresholds
- Include both English and Chinese content

---

## Quality Assurance Checklist

Before completing any research document, verify:

- [ ] Filename follows `YYYY-MM-DD-task-X-X-TOPIC.md` pattern
- [ ] Document includes B-M-R-I structure
- [ ] All conclusions have citations in `([Author, Year](URL))` format
- [ ] At least 3-5 citations per document
- [ ] At least 1,000 words per study
- [ ] Document saved to `research/` directory
- [ ] Key terms have Chinese translations
- [ ] Source priority: PubMed > Nature/Science > preprints

---

## Quick Reference

| Standard | Requirement |
|----------|-------------|
| Filename | `YYYY-MM-DD-task-X-X-TOPIC.md` |
| Citation | `([Author, Year](URL))` |
| Min citations | 3-5 per document |
| Min words/study | 1,000 |
| MCP tool | `mcp__MiniMax__web_search` |
| Structure | B-M-R-I (Background/Method/Results/Interpretation) |
| Language | Bilingual (Chinese/English) |
| Source priority | PubMed > Nature/Science > preprints |

---

**End of Core Rules**
