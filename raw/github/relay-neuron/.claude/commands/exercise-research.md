# Exercise Science Research Command

## Usage

```
/exercise-research [topic]
```

## Description

Initiates a new exercise science research topic by orchestrating a multi-step workflow that generates research questions, executes literature searches, creates structured research documents, and updates the master task list. This command coordinates the exercise-research-ideation, literature-search, and bri-structure skills to produce complete B-M-R-I (Background/Method/Results/Interpretation) formatted research files.

## Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `topic` | Yes | The research topic or research question to investigate. Can be a broad topic (e.g., "blood flow restriction training") or a specific PICO question. |

## Workflow

### Step 1: Parse Topic and Subtasks

1. Receive the topic argument from user
2. Break down the topic into searchable concepts
3. Identify any PICO elements if explicitly provided
4. Determine if this is a new research direction or expansion of existing topic

### Step 2: Generate Research Questions (exercise-research-ideation)

1. Invoke the `exercise-research-ideation` skill
2. Apply the PICO framework adapted for exercise science:
   - **P**opulation: Who is studied (e.g., resistance-trained males, older adults, athletes)
   - **I**ntervention: What is done (e.g., blood flow restriction, protein supplementation)
   **C**omparison: Control/baseline (e.g., traditional resistance training, placebo)
   **O**utcome: Measured result (e.g., muscle hypertrophy, strength gains, recovery)
3. Identify research gaps (literature, methodological, population, application)
4. Formulate specific, answerable research questions
5. Generate a Research Question Card

### Step 3: Execute Literature Search (literature-search)

1. Invoke the `literature-search` skill
2. Build search strings using Boolean operators:
   - Combine terms with AND/OR
   - Use exact phrases with quotes
   - Apply time filters: 2024-01-01 to 2026-12-31
3. Execute searches using `mcp__MiniMax__web_search`
4. Search databases in priority order:
   - PubMed (primary for biomedical research)
   - SPORTDiscus (exercise science and sports medicine)
   - Cochrane Library (systematic reviews)
   - Google Scholar (supplementary)
5. Extract citations: authors, year, journal, DOI/URL, study design, sample size, key findings
6. Prioritize: peer-reviewed journals, impact factor > 3.0, recent systematic reviews

### Step 4: Create Research Files (bri-structure)

1. Invoke the `bri-structure` skill
2. Create research file with B-M-R-I format:
   - **Header**: Title, Research Date, Topic description, Search Scope
   - **Abstract**: 150-250 words summarizing research question, methods, findings, conclusions
   - **Key Findings**: 3-5 named studies with full citations in format `([Author, Year](URL))`
   - **Background (B)**: Context, research gap, objectives (300-500 words)
   - **Method (M)**: Search strategy, inclusion/exclusion criteria (200-400 words)
   - **Results (R)**: Study characteristics, outcomes with effect sizes and p-values (400-600 words per study)
   - **Interpretation (I)**: Mechanisms, applications, limitations, future directions (300-500 words)
   - **Conclusions**: Summary with cited sources
   - **Data Sources**: Database names, search dates
   - **References**: Full citation list in relay-neuron format
3. File naming: `YYYY-MM-DD-task-X-X-TOPIC.md` for individual topics
4. Minimum quality standards:
   - 3-5 citations per document
   - 1,000+ words per study
   - 3,000+ total characters
   - 100% cited conclusions

### Step 5: Update RESEARCH_MASTER_LIST.md

1. Locate the appropriate section in RESEARCH_MASTER_LIST.md
2. Add new task entry with format: `- [ ] X.X Topic description (YYYY-MM-DD)`
3. Mark task as completed with `[x]`
4. Add the research date in parentheses
5. Preserve alphabetical/numerical ordering within sections

## Examples

### Example 1: Basic Topic Research

**Input:**
```
/exercise-research blood flow restriction training
```

**Output:**
1. Research Question Card generated using PICO framework
2. Literature search on PubMed/SPORTDiscus for BFR studies (2024-2026)
3. File created: `research/2026-05-23-task-X-X-blood-flow-restriction-training.md`
4. RESEARCH_MASTER_LIST.md updated with new task

### Example 2: PICO-Formatted Research

**Input:**
```
/exercise-research Does blood flow restriction at 20% 1RM compared to traditional resistance training at 70% 1RM affect quadriceps hypertrophy in older adults (65+)?
```

**Output:**
1. PICO elements extracted:
   - P: Older adults (65+)
   - I: Blood flow restriction at 20% 1RM
   - C: Traditional resistance training at 70% 1RM
   - O: Quadriceps hypertrophy, strength
2. Literature search focused on BFR in elderly populations
3. File created with specific research question addressed
4. RESEARCH_MASTER_LIST.md updated

### Example 3: Supplement Research

**Input:**
```
/exercise-research creatine supplementation effects on strength performance
```

**Output:**
1. Gap analysis identifies dose-response and timing questions
2. Literature search for creatine studies (2024-2026)
3. File created: `research/2026-05-23-task-X-X-creatine-supplementation-strength.md`
4. Summary added to section 2 (Nutrition & Supplementation) or 11 (Supplement Science)

### Example 4: Expanding Existing Research

**Input:**
```
/exercise-research expand protein timing research to include plant-based protein sources
```

**Output:**
1. Identifies existing protein timing research (e.g., task 2.1)
2. Gap analysis focuses on plant-based protein literature
3. New research file created addressing the gap
4. RESEARCH_MASTER_LIST.md updated with expanded scope

## Citation Format

All citations must follow relay-neuron format:

**In-body citation:**
```markdown
([Kreider et al., 2017](https://pubmed.ncbi.nlm.nih.gov/...))
```

**Reference list:**
```markdown
- Kreider et al., 2017. Journal of the International Society of Sports Nutrition. [Link](URL)
```

## Skills Used

| Skill | Purpose |
|-------|---------|
| `exercise-research-ideation` | Research gap analysis and question formulation using PICO framework |
| `literature-search` | PubMed and SPORTDiscus search strategies for literature review |
| `bri-structure` | B-M-R-I document template for exercise science research papers |
| `mcp__MiniMax__web_search` | Web search API for finding exercise science literature |

## Files Created

| File | Description |
|------|-------------|
| `research/YYYY-MM-DD-task-X-X-TOPIC.md` | Main research document in B-M-R-I format |
| `research/YYYY-MM-DD-task-X-X-TOPIC-SUPPLEMENT.md` | Supplementary analysis (if needed) |

## Files Modified

| File | Modification |
|------|--------------|
| `RESEARCH_MASTER_LIST.md` | New task entry added and marked as completed |

## Quality Checklist

- [ ] Research question is specific and answerable
- [ ] PICO framework applied correctly
- [ ] Literature search covers 2024-2026 timeframe
- [ ] Minimum 3-5 citations included
- [ ] All conclusions have citations
- [ ] B-M-R-I structure complete
- [ ] File naming follows convention
- [ ] RESEARCH_MASTER_LIST.md updated

## Error Handling

If the topic is too broad:
- Request clarification on specific PICO elements
- Suggest narrowing the scope

If no literature is found:
- Expand search terms
- Include older foundational studies
- Note gap in literature in the document

If citation verification fails:
- Use `cite-verify` command to check individual file
- Find alternate URLs for broken links
