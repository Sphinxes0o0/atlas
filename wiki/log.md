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
