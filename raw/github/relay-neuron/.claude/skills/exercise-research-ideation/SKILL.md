---
name: exercise-research-ideation
description: Research gap analysis and question formulation for exercise science
version: 1.0.0
author: Relay Neuron Research
license: MIT
tags: [Exercise Science, Research, Ideation, Gap Analysis]
dependencies: [mcp__MiniMax__web_search]
---

# Exercise Research Ideation Skill

## Quick Start

Use this skill when starting a new research topic or identifying research gaps. This skill helps formulate answerable research questions using the PICO framework adapted for exercise science.

## Core Workflow

1. **Topic exploration** - Scan current knowledge
2. **Gap identification** - Find understudied areas
3. **Question formulation** - Apply PICO framework
4. **Feasibility check** - Assess research viability
5. **Generate research card** - Document the question

## PICO Framework (Exercise Science)

| Element | Definition | Example |
|---------|------------|---------|
| **P**opulation | Who is studied | Resistance-trained males, older adults, athletes |
| **I**ntervention | What is done | Blood flow restriction, protein supplementation |
| **C**omparison | Control/baseline | Traditional resistance training, placebo |
| **O**utcome | Measured result | Muscle hypertrophy, strength gains, recovery |

### PICO Examples

**Example 1: Protein Timing**
- P: Young resistance-trained males
- I: 40g whey protein post-exercise
- C: Same protein at different timing
- O: Muscle protein synthesis rates

**Example 2: BFR Training**
- P: Older adults (65+)
- I: Blood flow restriction at 20% 1RM
- C: Traditional resistance training at 70% 1RM
- O: Quadriceps hypertrophy, strength

**Example 3: Creatine Loading**
- P: Athletes in power sports
- I: Creatine loading (20g/day × 5 days)
- C: Placebo
- O: Bench press 1RM, vertical jump

## Research Gap Types

### 1. Literature Gaps
- No existing studies on topic
- Very few studies (n < 5)
- Outdated studies (pre-2010)

### 2. Methodological Gaps
- No RCTs exist
- No dose-response studies
- No long-term follow-up

### 3. Population Gaps
- Understudied populations (elderly, youth, clinical)
- Specific athlete populations
- Sex-based differences unexplored

### 4. Application Gaps
- Theory not translated to practice
- No practical guidelines exist
- Translation studies needed

## Question Formulation

### Good Research Questions
- Specific and focused
- Answerable with available methods
- Clinically/practically relevant
- Novel or builds on existing work

### Poor Research Questions
- Too broad ("What is exercise?")
- Unanswerable ("Does exercise work?")
- Already established ("Does protein build muscle?")

## Research Question Templates

### Template 1: Intervention Study
```
Does [INTERVENTION] compared to [COMPARISON] affect [OUTCOME] in [POPULATION]?
```

### Template 2: Mechanism Study
```
What is the mechanism by which [INTERVENTION] influences [OUTCOME]?
```

### Template 3: Dosage Study
```
What is the optimal [DOSAGE/PARAMETER] of [INTERVENTION] for [OUTCOME]?
```

### Template 4: Population Study
```
How does [POPULATION] respond to [INTERVENTION] compared to [OTHER POPULATION]?
```

## Gap Analysis Process

1. **Literature scan** - Quick search for existing studies
2. **Map evidence** - Create evidence matrix
3. **Identify gaps** - Find missing/incomplete areas
4. **Prioritize** - Rank by relevance, feasibility, novelty
5. **Form question** - Develop answerable question

## Research Question Card Template

```markdown
## Research Question Card

**Topic:** [Brief topic name]
**Date:** YYYY-MM-DD

### PICO Breakdown
- **Population:** [Description]
- **Intervention:** [Description]
- **Comparison:** [Description]
- **Outcome:** [Description]

### Research Question
[Formal research question]

### Gap Type
[ ] Literature  [ ] Methodological  [ ] Population  [ ] Application

### Rationale
[Why this question matters]

### Feasibility
- Difficulty: [Low/Medium/High]
- Resources needed: [Description]
- Estimated timeline: [Weeks/Months]

### Related Topics
- [Existing topic 1]
- [Existing topic 2]

### Literature Support
- [Key paper 1]
- [Key paper 2]
```

## Integration Points

- Outputs to `RESEARCH_MASTER_LIST.md`
- Uses `literature-search` for gap scanning
- Uses `mcp__MiniMax__web_search` for evidence
- Feeds into `bri-structure` for document writing

## Exercise Science Focus Areas

- Muscle hypertrophy mechanisms
- Protein synthesis optimization
- Training periodization
- Recovery strategies
- Ergogenic aids/supplements
- Population-specific responses
- Biomechanics
- Cardiorespiratory adaptations

## When to Use

**Use exercise-research-ideation when:**
- Starting a new research line
- Identifying research gaps
- Planning systematic review
- Generating research questions

**Use other skills instead:**
- `literature-search` - When you have a question and need papers
- `bri-structure` - When ready to write research document
