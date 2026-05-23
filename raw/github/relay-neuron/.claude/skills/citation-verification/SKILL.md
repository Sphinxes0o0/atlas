---
name: citation-verification
description: Verify exercise science citations for accuracy and accessibility
version: 1.0.0
author: Relay Neuron Research
license: MIT
tags: [Exercise Science, Research, Citation, Quality Control]
dependencies: []
---

# Citation Verification Skill

## Quick Start

Use this skill to verify that citations in research documents are accurate, accessible, and properly formatted. Citation verification ensures research integrity.

## Verification Workflow

1. **Extract citations** - Find all citations in document
2. **Check DOI/URL** - Verify DOI resolution or URL accessibility
3. **Validate metadata** - Confirm author, year, journal match
4. **Check format** - Ensure relay-neuron format compliance
5. **Report issues** - Flag any problems

## Relay-Neuron Citation Format

**In-body format:**
```markdown
([Author, Year](URL))
```

**Examples:**
```markdown
([Kreider et al., 2017](https://pubmed.ncbi.nlm.nih.gov/...))
([Morton et al., 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/...))
([Schoenfeld et al., 2020](https://doi.org/...))
```

**Reference list format:**
```markdown
- Author et al., Year. Journal Name. [Link](full URL)
```

## Verification Checklist

### DOI Verification
- [ ] DOI resolves correctly
- [ ] DOI matches paper metadata
- [ ] DOI prefix is from legitimate publisher

### URL Verification
- [ ] URL is accessible (not 404)
- [ ] URL matches claimed source
- [ ] Prefer PubMed/NIH URLs for biomedical research

### Metadata Validation
- [ ] Author names match actual paper
- [ ] Year is correct
- [ ] Journal name is accurate
- [ ] Study design claims are valid

### Format Compliance
- [ ] In-body citation matches template
- [ ] Reference list entry is complete
- [ ] No broken or malformed citations

## Common Issues

### 1. Broken URLs
**Problem:** URL returns 404 or redirect loop
**Fix:** Find alternate URL (PubMed, DOI resolver, journal site)

### 2. Incorrect Metadata
**Problem:** Author/year/journal don't match
**Fix:** Cross-reference with DOI resolver or original source

### 3. Citation Drift
**Problem:** Citation claims don't match paper content
**Fix:** Read abstract/full text to verify claims

### 4. Preprint Citation
**Problem:** Citing preprint without notice
**Fix:** Add note "preprint" or find peer-reviewed version

### 5. Format Inconsistency
**Problem:** Citations don't follow relay-neuron format
**Fix:** Reformat to `([Author, Year](URL))`

## DOI Resolver

Use CrossRef or DOI.org to resolve DOIs:
```
https://doi.org/[DOI]
```

Common publishers:
- Nature: https://www.nature.com
- Elsevier: https://www.sciencedirect.com
- Springer: https://link.springer.com
- Wiley: https://onlinelibrary.wiley.com
- PubMed: https://pubmed.ncbi.nlm.nih.gov/

## Batch Verification

For documents with multiple citations:

1. Extract all citations to list
2. Check each DOI/URL systematically
3. Group by verification status:
   - ✓ Verified
   - ⚠ Warning (access issue, preprint)
   - ✗ Failed (broken link, wrong metadata)

4. Report summary

## Verification Report Template

```markdown
## Citation Verification Report

**File:** [Filename]
**Date:** YYYY-MM-DD
**Total Citations:** [N]

### Verified (✓)
1. [Citation 1]
2. [Citation 2]

### Warnings (⚠)
1. [Citation] - [Issue]
2. [Citation] - [Issue]

### Failed (✗)
1. [Citation] - [Issue]
2. [Citation] - [Issue]

### Summary
- Verified: [N]
- Warnings: [N]
- Failed: [N]
```

## Integration Points

- Input from `literature-search` results
- Input from `bri-structure` documents
- Feeds into quality assurance workflow
- Used before committing research files

## When to Use

**Use citation-verification when:**
- Completing a research document
- Reviewing existing files
- Before committing research files
- When accuracy is in doubt

**Don't use when:**
- Searching for papers (use `literature-search`)
- Writing new documents (use `bri-structure`)
- Assessing study quality (use `study-quality-appraisal`)
