# Update Master List Command

## Usage

```
/update-master-list [options]
```

## Description

Scans the `research/` directory to identify completed research topics and updates the task checkboxes in `RESEARCH_MASTER_LIST.md`. Generates summary statistics about research progress and optionally commits changes to git. This command ensures the master list accurately reflects the current state of the research archive.

## Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `options` | No | Optional flags: `--commit` to commit changes, `--stats` to show detailed statistics |

## Workflow

### Step 1: Scan Research Directory

1. List all files in the `research/` directory
2. Parse file names to extract:
   - Date (YYYY-MM-DD format)
   - Task number (X-X format from task-X-X pattern)
   - Topic description (from filename)
3. Identify file types:
   - Main research files: `YYYY-MM-DD-task-X-X-TOPIC.md`
   - Research rounds: `YYYY-MM-DD-research-round-N.md`
   - Supplements: `YYYY-MM-DD-task-X-X-TOPIC-SUPPLEMENT.md`

### Step 2: Match with Master List

1. Load `RESEARCH_MASTER_LIST.md`
2. Parse existing task entries in each section
3. For each section, match research files to tasks:
   - Compare topic keywords
   - Match task numbers when present
   - Handle Chinese and English topic descriptions
4. Identify:
   - Tasks already marked complete `[x]`
   - Tasks with matching research files but unchecked `[ ]`
   - Tasks with no corresponding files
   - New files not yet in master list

### Step 3: Update Checkboxes

1. For each completed task found:
   - Change `[ ]` to `[x]` in RESEARCH_MASTER_LIST.md
   - Add completion date in parentheses: `(YYYY-MM-DD)`
2. For new files not in master list:
   - Identify appropriate section
   - Add new task entry at correct position
   - Mark as completed with `[x]`
3. Preserve formatting and section structure

### Step 4: Generate Statistics

1. Calculate summary statistics:
   - Total tasks in master list
   - Tasks completed
   - Tasks pending
   - Completion percentage by section
2. List any orphaned files (files without master list entry)
3. List any missing files (tasks marked complete but file not found)

### Step 5: Commit Changes (Optional)

1. If `--commit` flag provided:
   - Stage RESEARCH_MASTER_LIST.md
   - Create commit with message following project conventions
   - Commit message format: `Update: Research progress - [summary]`
2. Do NOT commit research files (they should be committed separately)

## Output Format

```
## Update Master List Report

**Date:** YYYY-MM-DD
**Scan Path:** research/

### Summary Statistics

| Section | Completed | Total | Percentage |
|---------|-----------|-------|------------|
| Section 1: Muscle Hypertrophy | 5 | 5 | 100% |
| Section 2: Nutrition & Supplementation | 5 | 5 | 100% |
| ... | ... | ... | ... |
| **Total** | **XX** | **XX** | **XX%** |

### Completed Tasks
- 1.1 阻力训练诱导的肌肥大机制研究 (2026-05-12)
- 1.2 肌肉蛋白合成 (mTOR) 通路最新研究 (2026-05-12)
- ...

### Pending Tasks
- 3.6 Novel training methods review (no file found)
- ...

### Orphaned Files (not in master list)
- research/2026-05-20-novel-topic.md
- ...

### Changes Made
- Updated X task checkboxes
- Added X new entries
```

## Options

### --stats

Show detailed statistics including:
- File count by section
- Average document length
- Most active research areas
- Recent activity timeline

### --commit

Automatically commit changes to git:
1. Stage RESEARCH_MASTER_LIST.md
2. Create commit with timestamped message
3. Show commit hash

### --dry-run

Preview changes without modifying files:
- Show what would be updated
- Highlight discrepancies
- No git operations

## Examples

### Example 1: Basic Update

**Input:**
```
/update-master-list
```

**Output:**
```
## Update Master List Report

**Date:** 2026-05-23
**Scan Path:** research/

### Summary Statistics
[Statistics table]

### Changes Made
- Updated 3 task checkboxes
- Added 1 new entry
```

### Example 2: Update with Commit

**Input:**
```
/update-master-list --commit
```

**Output:**
```
## Update Master List Report

[Same as basic]

### Git Commit
- Staged: RESEARCH_MASTER_LIST.md
- Commit: abc1234
- Message: "Update: Research progress - 98% complete (2026-05-23)"
```

### Example 3: Statistics Only

**Input:**
```
/update-master-list --stats
```

**Output:**
```
## Research Archive Statistics

**Total Files:** 93
**Total Size:** 6.7 MB
**Average File Size:** 72 KB

### By Section
| Section | Files | Avg Length |
|---------|-------|------------|
| 1. Muscle Hypertrophy | 5 | 15.2 KB |
| ...

### Recent Activity (Last 7 days)
- 2026-05-16: Round 21 & 22 research
- 2026-05-17: No activity
- ...

### Most Active Topics
1. Muscle protein synthesis (3 files)
2. Blood flow restriction (2 files)
...
```

### Example 4: Dry Run

**Input:**
```
/update-master-list --dry-run
```

**Output:**
```
## Dry Run - No Changes Made

### Would Update
- [x] 1.1 阻力训练诱导的肌肥大机制研究 → already marked complete
- [ ] 3.6 Novel training → would mark complete, file found

### Discrepancies
- Task 4.5 marked complete but research/2026-05-12-task-4-5-*.md not found

### Orphaned Files
- research/2026-05-20-unknown-topic.md (no matching task)
```

## File Matching Patterns

### Research Files Pattern
```
YYYY-MM-DD-task-X-X-TOPIC.md
YYYY-MM-DD-task-X-X-TOPIC-SUPPLEMENT.md
YYYY-MM-DD-research-round-N.md
```

### Master List Pattern
```
- [x] X.X Topic description (YYYY-MM-DD)
- [ ] X.X Topic description
```

## Section Mapping

The command recognizes these sections in RESEARCH_MASTER_LIST.md:

| Section | Keywords |
|---------|----------|
| 1. Muscle Hypertrophy | 肌肥大, hypertrophy, muscle growth |
| 2. Nutrition & Supplementation | 营养, 补剂, protein, supplement, creatine |
| 3. Resistance Training Science | 阻力训练, resistance training, frequency |
| 4. Cardiovascular & Metabolic | 心血管, metabolic, HIIT, VO2max |
| 5. Sleep & Recovery | 睡眠, recovery, sleep quality |
| 6. Health & Disease | 健康, 疾病, health, disease, 衰老, diabetes |
| 7. Training Methods | 训练方法, training methods, technique |
| 8. Conferences & Journals | 学术会议, journals, SCSEPF, ACSM |
| 9. Emerging Research | 新兴研究, emerging |
| 10. Research Rounds | Round, research round |
| 11. Supplement Science | 补剂科学, supplement |
| 12. Carbohydrate Intake | 碳水化合物, carbohydrate |
| 13. Omega-3 & Fish Oil | 鱼油, Omega-3 |

## Skills Used

| Skill | Purpose |
|-------|---------|
| None required | This command uses file system operations only |

## Files Modified

| File | Modification |
|------|--------------|
| `RESEARCH_MASTER_LIST.md` | Task checkboxes updated, completion dates added, new entries inserted |

## Git Integration

When `--commit` is used:
- Only RESEARCH_MASTER_LIST.md is staged
- Research files should be committed separately when created
- Commit message follows format: `Update: Research progress - [percentage] complete (YYYY-MM-DD)`
- Uses project Co-Authored-By line for Claude attribution

## Error Handling

If RESEARCH_MASTER_LIST.md not found:
- Report error and exit
- Do not create new file

If research/ directory not found:
- Report error and exit
- List expected path

If file parsing fails:
- Skip malformed filenames
- Report skipped files in output
- Continue processing valid files
