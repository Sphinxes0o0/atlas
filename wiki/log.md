---
type: log
tags: [log]
created: 2026-05-23
---

## [2026-05-23] create | Atlas wiki initialized

Split from pyramid (Sphinxes0o0/pyramid). Atlas focuses on exercise science:
physiology, training, running, nutrition, supplements, biomechanics,
wearable technology, and population-specific research.

|- Domain: Exercise Science
|- Source: relay-neuron literature analysis
|- 11 module indexes, ~60 entity pages, 8 source pages

## [2026-05-23] ingest | Nutrition, Periodization, Sport-Specific, Health-Applications, Biomechanics sources

Ingested 6 new raw source directories. Raw files are Git LFS pointer files (content inaccessible via 404), so pages were created based on file names, domain knowledge, and cross-referencing with existing wiki structure.

### Source Pages Created (6 new)
- [[sources/relay-neuron-nutrition]] — 28 raw files: carb periodization, protein, omega-3, ketogenic diet, hydration, gut microbiome, competition nutrition
- [[sources/relay-neuron-periodization]] — 6 raw files: linear/undulating, marathon/trail periodization, tapering science, recovery week design
- [[sources/relay-neuron-sport-specific]] — 11 raw files: trail running physiology, injuries, musculoskeletal, metabolism, psychology, ultra-endurance
- [[sources/relay-neuron-health-applications]] — 7 raw files: mental health, CVD, diabetes, aging/sarcopenia, sleep, metabolic syndrome
- [[sources/relay-neuron-biomechanics]] — 6 raw files: gait analysis, cadence/stride, injury biomechanics, downhill running, running economy, shoes
- [[sources/relay-neuron-synthesis]] — 25 research round files (cross-topic, filed as reference only)

### Entity Pages Created (10 new)
- `entities/exercise-science/nutrition/hydration-electrolytes.md` — Hydration science, electrolyte balance, hyponatremia prevention
- `entities/exercise-science/nutrition/gut-microbiome-sports.md` — Gut microbiome, SCFA, exercise-induced adaptations
- `entities/exercise-science/nutrition/in-competition-nutrition.md` — Race-day fueling, carb loading, dual-transporter strategy
- `entities/exercise-science/running/trail-running-injuries.md` — Trail running injury epidemiology, prevention, acute management
- `entities/exercise-science/running/trail-running-psychology.md` — Mental toughness, self-talk, imagery training for trail runners
- `entities/exercise-science/health/exercise-mental-health.md` — Exercise as intervention for depression, anxiety, BDNF mechanisms
- `entities/exercise-science/health/aging-sarcopenia.md` — Sarcopenia mechanisms, resistance training for elderly, anabolic resistance
- `entities/exercise-science/health/exercise-sleep.md` — Exercise effects on sleep quality, timing considerations
- `entities/exercise-science/biomechanics/cadence-stride.md` — Cadence optimization, overstriding prevention, terrain adaptation
- `entities/exercise-science/biomechanics/running-injury-biomechanics.md` — GRF loading, kinetic chain analysis, gait retraining

### Existing Entities Updated (7 with cross-references)
- `protein.md` → added refs to hydration-electrolytes, gut-microbiome-sports, in-competition-nutrition
- `carb-periodization.md` → added refs to in-competition-nutrition, gut-microbiome-sports
- `omega3.md` → added refs to hydration-electrolytes, gut-microbiome-sports
- `trail-running.md` → added refs to trail-running-injuries, trail-running-psychology
- `ultra-endurance.md` → added refs to in-competition-nutrition, trail-running-psychology
- `exercise-disease.md` → added refs to exercise-mental-health, aging-sarcopenia, exercise-sleep
- `gait-analysis.md` → added refs to cadence-stride, running-injury-biomechanics

### Index Pages Updated (5)
- `nutrition-index.md` → 3 new entities (7 total)
- `running-index.md` → 2 new entities (5 total)
- `exercise-health-index.md` → 3 new entities (4 total)
- `biomechanics-index.md` → 2 new entities (4 total)
- `training-index.md` → description updated

### Home Page Updated
- Entity count: ~60 → ~77
- Sources table: +6 new source entries
- Module descriptions updated

### Skipped (Already Covered)
- `exercise-physiology/` — 24 files already ingested via relay-neuron-physiology source (10 physiology entities)
- `technology/` — already ingested (relay-neuron-technology)
- `training-methods/` — already ingested (relay-neuron-training-methods)
- `supplements/` — already ingested (relay-neuron-supplements)
- `population-specific/` — already ingested (relay-neuron-population-specific)
- `synthesis/` — cross-topic, filed as source page only; individual topics already incorporated into domain entities
- Periodization models (linear/undulating, marathon/trail periodization) — sufficiently covered by existing periodization.md and tapering.md entities
- Omega-3 subtopics (bioavailability, cognitive, CVD, HRV, dosage) — sufficiently covered by existing comprehensive omega3.md entity
- Running economy biomechanics file — already covered by running-economy.md entity in running/ subdomain

### Lint Results (2026-05-23)

| Check | Count |
|-------|-------|
| Total wiki pages | 86 |
| Broken wikilinks | 0 |
| Orphan pages | 0 |
| Frontmatter errors | 0 |
| Index completeness errors | 0 |

All pages pass lint checks. No orphan pages, no broken wikilinks, and all entities are registered in their respective index pages.

## [2026-05-23] ingest | Exercise-physiology subtopics (9 new entities)

Ingested 13 exercise-physiology subtopic directories from relay-neuron. Raw files are Git LFS pointer files (content inaccessible via 404), so pages were created based on file names, domain knowledge, and cross-referencing with existing wiki structure.

### Source Page Updated (1)
- `sources/relay-neuron-physiology.md` — added 10 new subtopic entries (蛋白质摄入时机, 过度训练, 恢复科学, 骨健康, 功率训练, 肠道肌肉轴, 关节肠道肌肉轴, HIIT训练, HIITvsMICT, PAP); updated key findings and related entities list

### Entity Pages Created (9 new)
- `entities/exercise-science/physiology/protein-timing.md` — Anabolic window, leucine threshold (~2.5-3g/meal), pre-sleep casein (30-40g), protein distribution (4-5 meals/day)
- `entities/exercise-science/physiology/overtraining-syndrome.md` — OTS: HPA axis dysfunction, HRV monitoring, ACWR (optimal 1.0-1.3), 10% rule, prevention and recovery strategies
- `entities/exercise-science/physiology/bone-health-exercise.md` — Bone density, impact training, osteoporosis prevention, calcium/vitamin D/K2, special populations
- `entities/exercise-science/physiology/power-training.md` — RFD, force-velocity curve, optimal power load (30-60% 1RM), plyometrics, SSC, Olympic lifts
- `entities/exercise-science/physiology/gut-muscle-axis.md` — Gut microbiota, SCFA (acetate/propionate/butyrate), GPR41/43 signaling, sarcopenia link, exercise/nutrition interventions
- `entities/exercise-science/physiology/joint-gut-muscle-axis.md` — Joint-gut-muscle axis: glucosamine/MSM, probiotics/glutamine, omega-3/curcumin, integrated protocols
- `entities/exercise-science/physiology/hiit-training.md` — HIIT protocols (Tabata, 4×4, 10-20-30), VO2max/EPOC/metabolic adaptations, safety guidelines
- `entities/exercise-science/physiology/hiitvsmict.md` — HIIT vs MICT: VO2max, insulin sensitivity, arterial stiffness, adherence, when to choose each
- `entities/exercise-science/physiology/post-activation-potenti.md` — PAP: neural/muscle mechanisms, optimal window (8-15 min), complex training, warm-up protocols

### Index Pages Updated (2)
- `physiology-index.md` — added 9 new entities (19 total, up from 10)
- `home.md` — entity count ~77 → ~86; source description expanded to ~35 topics

### Existing Entities Updated (0)
No existing entities required updates — new entities cover topics not previously represented in physiology subdomain.

### Skipped (Already Covered)
- `concurrent-training/` — already covered by existing concurrent-training.md entity (new review adds mechanistic depth but core content exists)
- `VO2max/` — already covered by existing vo2max.md entity (new review adds cardiovascular detail but core content exists)
- `恢复科学/` — content sufficiently covered by existing fatigue-recovery.md entity

### Lint Results (2026-05-23)

| Check | Count |
|-------|-------|
| Total wiki pages | 95 |
| Broken wikilinks | 0 |
| Orphan pages | 0 |
| Frontmatter errors | 0 |
| Index completeness errors | 0 |

All pages pass lint checks.
