---
name: study-quality-appraisal
description: Quality assessment tools for RCTs and cohort studies in exercise science
version: 1.0.0
author: Relay Neuron Research
license: MIT
tags: [Exercise Science, Research, Quality, RCT, Evidence]
dependencies: []
---

# Study Quality Appraisal Skill

## Quick Start

Use this skill to assess the methodological quality of exercise science studies. This helps evaluate evidence strength and informs how much weight to give study findings.

## Study Types in Exercise Science

| Type | Evidence Level | Description |
|------|----------------|-------------|
| Systematic Review | 1 | Multiple RCTs synthesized |
| RCT | 2 | Randomized controlled trial |
| Cohort Study | 3 | Follow-up over time |
| Case-Control | 4 | Compare cases/controls |
| Case Report | 5 | Single subject observation |
| Expert Opinion | 6 | Clinical experience |

## RCT Quality: PEDro Scale

The Physiotherapy Evidence Database scale (0-10):

| Item | Criterion | Points |
|------|-----------|--------|
| 1 | Eligibility criteria specified | N/A (not counted) |
| 2 | Random allocation | 1 |
| 3 | Concealed allocation | 1 |
| 4 | Baseline comparability | 1 |
| 5 | Subject blinding | 1 |
| 6 | Therapist blinding | 1 |
| 7 | Assessor blinding | 1 |
| 8 | <15% dropout | 1 |
| 9 | Intention-to-treat | 1 |
| 10 | Between-group comparisons | 1 |
| 11 | Point/variability reporting | 1 |

### PEDro Interpretation
- **9-10:** Excellent
- **6-8:** Good
- **4-5:** Fair
- **<4:** Poor

## Cohort Study Quality: Newcastle-Ottawa Scale

### Selection (0-4)
- Representativeness of exposed cohort
- Selection of non-exposed cohort
- Ascertainment of exposure
- Outcome not present at start

### Comparability (0-2)
- Study controls for age/sex
- Study controls for other factors

### Outcome (0-3)
- Assessment method
- Follow-up length
- Adequacy of follow-up

### Interpretation
- **7-9:** Good quality
- **4-6:** Fair quality
- **<4:** Poor quality

## Critical Appraisal Checklist

### For All Studies
- [ ] Is the research question clearly stated?
- [ ] Is the study design appropriate?
- [ ] Is the sample size adequate/power calculated?
- [ ] Are inclusion/exclusion criteria specified?
- [ ] Is the intervention clearly described?
- [ ] Are outcomes measured validly/reliably?
- [ ] Are statistical methods appropriate?
- [ ] Are limitations acknowledged?

### For RCTs
- [ ] Was randomization proper?
- [ ] Was allocation concealed?
- [ ] Were participants blinded?
- [ ] Was intention-to-treat used?
- [ ] Was funding source disclosed?

### For Exercise Science Specific
- [ ] Was training volume/intensity reported?
- [ ] Was protein intake controlled?
- [ ] Was training status documented?
- [ ] Was prior training controlled?

## Quality Appraisal Template

```markdown
## Study Quality Appraisal

**Paper:** [Author, Year]
**Study Type:** [RCT/Cohort/etc.]
**Overall Quality:** [Excellent/Good/Fair/Poor]

### PEDro Scale (if RCT)
| Item | Score |
|------|-------|
| Random allocation | /1 |
| Concealed allocation | /1 |
| Baseline comparability | /1 |
| Subject blinding | /1 |
| Therapist blinding | /1 |
| Assessor blinding | /1 |
| <15% dropout | /1 |
| Intention-to-treat | /1 |
| Between-group comparisons | /1 |
| Point/variability reporting | /1 |
| **Total** | **/10** |

### Strengths
- [Strength 1]
- [Strength 2]

### Limitations
- [Limitation 1]
- [Limitation 2]

### Risk of Bias
- [ ] Low
- [ ] Some concerns
- [ ] High

### Applicability to Question
- [ ] Directly applicable
- [ ] Somewhat applicable
- [ ] Limited applicability
```

## Evidence Hierarchy by Outcome

### Muscle Hypertrophy
Best: DXA/MRI measures
Acceptable: Circumference, BIA
Poor: Self-report

### Strength
Best: 1RM testing
Acceptable: Isokinetic dynamometry
Poor: Self-report

### Performance
Best: Time-trial, 1RM
Acceptable: Submax tests
Poor: Self-report

## Integration Points

- Used alongside `literature-search`
- Feeds into `bri-structure` interpretation section
- Informs `citation-verification` quality assessment
- Supports evidence-based conclusions

## Red Flags in Exercise Science Studies

1. No control for protein intake
2. Training status not documented
3. Single time-point measurement
4. No blinding in subjective outcomes
5. Industry funding without disclosure
6. No mention of ethical approval
7. Retention rate <80% without explanation
8. Effect sizes suspiciously large

## When to Use

**Use study-quality-appraisal when:**
- Evaluating paper for inclusion
- Writing interpretation section
- Determining evidence strength
- Critiquing existing literature

**Use other skills instead:**
- `literature-search` - Finding papers
- `bri-structure` - Writing research document
- `citation-verification` - Checking citation accuracy
