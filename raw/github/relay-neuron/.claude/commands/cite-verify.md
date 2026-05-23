# Citation Verification Command

## Usage

```
/cite-verify [filepath]
```

## Description

Verifies all citations in a research file for accuracy, accessibility, and format compliance. This command extracts citations from a specified markdown file, validates DOI/URL accessibility, confirms metadata matches the claimed source, and checks relay-neuron format compliance. It uses the citation-verification skill to perform comprehensive quality assurance on research documents before they are committed to the archive.

## Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `filepath` | Yes | Absolute or relative path to the research markdown file to verify |

## Workflow

### Step 1: Extract Citations

1. Read the specified markdown file
2. Parse in-body citations using pattern: `([Author, Year](URL))`
3. Parse reference list entries:
   - Format: `- Author et al., Year. Journal Name. [Link](URL)`
4. Build a citation inventory with:
   - Citation ID (numeric sequence)
   - Author(s)
   - Year
   - URL/DOI
   - Location in document (line number)

### Step 2: Verify DOI/URL Accessibility

1. For each citation with DOI:
   - Resolve DOI using `https://doi.org/[DOI]`
   - Check HTTP response status
   - Follow redirects to final destination
   - Confirm content is accessible
2. For each citation with URL:
   - Check URL accessibility (not 404 or 5xx)
   - Verify URL matches claimed source (e.g., PubMed URL points to correct paper)
   - Detect redirect loops or broken links
3. For each citation without URL/DOI:
   - Flag as incomplete
   - Suggest DOI lookup

### Step 3: Validate Metadata

1. For accessible URLs, extract metadata:
   - Author names
   - Publication year
   - Journal name
   - Paper title
2. Compare extracted metadata with in-document citation:
   - Author names match (fuzzy match allowed for et al.)
   - Year is correct
   - Journal claims are accurate
   - Study design claims are valid
3. Flag discrepancies:
   - Wrong year
   - Incorrect author
   - Wrong journal
   - Claimed study type doesn't match

### Step 4: Check Format Compliance

1. Verify relay-neuron format:
   - In-body: `([Author, Year](URL))` exactly
   - Reference list: `- Author et al., Year. Journal. [Link](URL)`
2. Check for:
   - Missing parentheses
   - Missing brackets
   - Missing URL
   - Malformed citations
3. Verify DOI prefix is from legitimate publisher:
   - 10.1000+ (Springer)
   - 10.1016+ (Elsevier)
   - 10.1038+ (Nature)
   - 10.1111+ (Wiley)
   - 10.1177+ (SAGE)
   - 10.1093+ (Oxford)

### Step 5: Report Validation Status

1. Group citations by verification status:
   - **Verified (✓)**: DOI/URL accessible, metadata matches, format correct
   - **Warning (⚠)**: Minor issues (preprint, format deviation, redirect)
   - **Failed (✗)**: Broken link, wrong metadata, malformed citation
2. Generate summary statistics
3. Provide fix suggestions for each issue

## Output Format

```
## Citation Verification Report

**File:** research/2026-05-23-task-3-1-exercise-psychology-benefits.md
**Date:** YYYY-MM-DD
**Total Citations:** 12

---

### Verified (✓) - 9

1. ([Kreider et al., 2017](https://pubmed.ncbi.nlm.nih.gov/...)) - Line 45
2. ([Morton et al., 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/...)) - Line 67
...

### Warnings (⚠) - 2

1. ([Smith et al., 2024](https://www.researchgate.net/...)) - Line 123
   ⚠ Non-PubMed URL; consider finding PubMed version
2. ([Jones, 2025](https://doi.org/...)) - Line 156
   ⚠ Preprint detected; add "preprint" note if peer-reviewed version unavailable

### Failed (✗) - 1

1. ([Brown et al., 2023](https://pubmed.ncbi.nlm.nih.gov/invalid)) - Line 89
   ✗ URL returns 404; find alternate URL

---

### Summary

| Status | Count | Percentage |
|--------|-------|------------|
| Verified | 9 | 75% |
| Warnings | 2 | 17% |
| Failed | 1 | 8% |

### Issues by Type

| Issue Type | Count |
|------------|-------|
| Broken URLs | 1 |
| Non-PubMed sources | 1 |
| Preprint citations | 1 |
| Format deviations | 0 |

---

### Suggested Fixes

**Line 89:** Replace broken URL with:
- https://pubmed.ncbi.nlm.nih.gov/[CORRECT_ID]
- Or verify DOI: 10.xxxx/xxxxx

**Line 123:** Find PubMed version:
- Search PubMed for "Smith et al. 2024 exercise psychology"
- Replace with PubMed URL

**Line 156:** Add preprint notice:
- Change to: ([Jones, 2025](https://doi.org/...) - preprint)
- Or find peer-reviewed publication
```

## Examples

### Example 1: Basic Verification

**Input:**
```
/cite-verify research/2026-05-12-task-1-1-neuroscience-neural-drive.md
```

**Output:**
```
## Citation Verification Report

**File:** research/2026-05-12-task-1-1-neuroscience-neural-drive.md
**Date:** 2026-05-23
**Total Citations:** 15

[Verification results...]
```

### Example 2: Verify with Absolute Path

**Input:**
```
/cite-verify /Users/sphinx/github/relay-neuron/research/2026-05-12-task-2-1-soft-tissue-repair.md
```

**Output:**
```
## Citation Verification Report

**File:** ...research/2026-05-12-task-2-1-soft-tissue-repair.md
**Date:** 2026-05-23
**Total Citations:** 8

[Verification results...]
```

### Example 3: Multiple Files

**Input:**
```
/cite-verify research/2026-05-12-task-*.md
```

**Output:**
```
## Batch Citation Verification Report

**Date:** 2026-05-23
**Files Checked:** 5

| File | Total | Verified | Warnings | Failed |
|------|-------|----------|----------|--------|
| task-1-1-neuroscience-neural-drive.md | 15 | 14 | 1 | 0 |
| task-1-2-neuroscience-fatigue-mechanisms.md | 12 | 11 | 1 | 0 |
| task-2-1-soft-tissue-repair.md | 8 | 8 | 0 | 0 |
...

### Overall Summary

**Total Citations:** 58
**Verified:** 54 (93%)
**Warnings:** 3 (5%)
**Failed:** 1 (2%)
```

## Citation Formats

### Relay-Neuron In-Body Format
```
([Author, Year](URL))
```
**Examples:**
```markdown
([Kreider et al., 2017](https://pubmed.ncbi.nlm.nih.gov/...))
([Morton et al., 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/...))
([Schoenfeld et al., 2020](https://doi.org/...))
```

### Relay-Neuron Reference List Format
```markdown
- Author et al., Year. Journal Name. [Link](full URL)
```
**Examples:**
```markdown
- Kreider et al., 2017. Journal of the International Society of Sports Nutrition. [Link](https://pubmed.ncbi.nlm.nih.gov/...)
- Morton et al., 2018. Physiological Reviews. [Link](https://www.ncbi.nlm.nih.gov/pmc/articles/...)
```

## DOI Resolution

Common publishers and their DOI prefixes:
| Publisher | DOI Prefix | Example URL |
|-----------|------------|-------------|
| Nature | 10.1038 | https://www.nature.com/articles/... |
| Elsevier | 10.1016 | https://www.sciencedirect.com/science/article/... |
| Springer | 10.1007 | https://link.springer.com/article/... |
| Wiley | 10.1111 | https://onlinelibrary.wiley.com/doi/... |
| Oxford | 10.1093 | https://academic.oup.com/jes/article/... |
| PubMed | 10.XXXX | https://pubmed.ncbi.nlm.nih.gov/... |

## Verification Status Definitions

### Verified (✓)
- URL/DOI resolves correctly (200 OK)
- Metadata (author, year, journal) matches citation
- Format follows relay-neuron standard
- Source is from preferred database (PubMed preferred)

### Warning (⚠)
- Non-PubMed URL (ResearchGate, personal website)
- Preprint without notice
- Minor format deviation
- URL requires redirect to reach content
- Impact factor unknown

### Failed (✗)
- URL returns 404 or 5xx error
- DOI does not resolve
- Metadata mismatch (wrong author/year/journal)
- Malformed citation syntax
- Broken or incomplete URL

## Skills Used

| Skill | Purpose |
|-------|---------|
| `citation-verification` | Comprehensive citation validation workflow |
| `mcp__MiniMax__web_search` | DOI resolution and URL accessibility checks |

## Integration Points

- Run before committing research files with `git add && git commit`
- Use after `exercise-research` completes
- Run during quality review before publishing
- Integrate into research workflow before Round completion

## When to Use

**Use cite-verify when:**
- Completing a research document
- Reviewing existing files before update
- Before committing research files
- During quality assurance checks
- After literature search updates existing topic

**Don't use when:**
- Searching for papers (use `literature-search`)
- Writing new documents (use `bri-structure`)
- Assessing study quality (use `study-quality-appraisal`)
- Updating master list (use `update-master-list`)

## Files Modified

This command does not modify any files. It only reads and validates. Fix suggestions are provided for manual correction or can be applied using the suggested replacements.

## Error Handling

If file not found:
- Report error with full path attempted
- Suggest checking file name
- Exit with error code

If file is empty:
- Report "No citations found"
- Check if file is valid markdown

If citation parsing fails:
- Report line numbers with parsing errors
- Suggest format corrections
- Continue verifying other citations

If network error during verification:
- Report "Could not verify X citations due to network error"
- Show which citations could not be checked
- Suggest retry
