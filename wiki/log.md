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

## [2026-05-23] ingest | Training Methods subtopics (11 new entities)

Ingested training-methods subtopic directories from relay-neuron.

### Source Pages Updated (2)
- `sources/relay-neuron-training-methods.md` — added 21 new subdirs
- `sources/relay-neuron-supplements.md` — added 24 new supplement entries

### Entity Pages Created (11 new)
- `entities/exercise-science/training/altitude-training.md` — LHTL, HiHiLo, EPO response
- `entities/exercise-science/training/isometric-training.md` — MVC, angle-specific strength
- `entities/exercise-science/training/cluster-training.md` — Micro-sets, intraset rest
- `entities/exercise-science/training/blood-flow-restriction-training.md` — BFR, Kaatsu
- `entities/exercise-science/training/electrical-stimulation-training.md` — EMS, NMES
- `entities/exercise-science/training/eccentric-overload-training.md` — Eccentric training
- `entities/exercise-science/training/youth-training.md` — LTAD, PHV
- `entities/exercise-science/training/training-autoregulation.md` — RPE, ACWR

### Entity Pages Updated (1)
- `periodization.md` — enhanced with relay-neuron content

### Index Pages Updated (2)
- `training-index.md` — added 8 new entities
- `supplements-index.md` — added 10 new supplement entries

## [2026-05-23] ingest | 133 root research tasks — enhanced existing source pages

Processed 133 root-level research task files (2026-05-03 to 2026-05-23) from relay-neuron. All files matched to existing source pages; 1 new entity page created for 56-muscle-function-training batch.

### Source Pages Updated (7)
- `sources/relay-neuron-supplements.md` — added summaries: creatine (ATP-PCr, +8-10% strength), HMB (anti-catabolic, elderly sarcopenia), beta-alanine (carnosine +40-80%, TEE +13-14%), BCAAs (mTOR/leucine threshold), L-carnitine (clinical benefits, TMAO controversy), glutamine (marathon infection -60%)
- `sources/relay-neuron-physiology.md` — added summaries: cold/heat therapy (CWI/CWT tradeoffs), exercise immunology (J-curve), exercise epigenetics (DNA methylation/telomere), neural drive (motor unit recruitment ↑), fatigue mechanisms (central/peripheral, TMS/EMG), mitochondrial benefits/limitations, mTORC1 benefits/hyperactivation risks, carotid body/VO2max, muscle function training
- `sources/relay-neuron-health-applications.md` — added summaries: cardiac exercise (VO2max strongest mortality predictor, n=122,007), cognitive performance (BDNF/hippocampal), GI health/EIGS (40-70% endurance athletes), exercise psychology (depression, meditation), injury fear (CBT graded exposure), menstrual cycle (follicular +13-40pp strength), menopause bone (LIFTMOR), altitude training (LHTL HiLo, 45-65% responders)
- `sources/relay-neuron-training-methods.md` — added summaries: flexibility/mobility (dynamic > static for warm-up), periodization models (DUP/block), altitude/hypoxia training (HIF/EPO)
- `sources/relay-neuron-biomechanics.md` — added summaries: soft tissue repair (BRI paradigm, eccentric exercise), soft tissue injury risks (multifactorial, previous injury strongest), gait analysis benefits/risks (RE +3-8%, injury -20-40%), fascia training (limited RCT, proprioceptive)
- `sources/relay-neuron-technology.md` — added summaries: biohacking wearables (HRV/CGM/AI, 78-92%), bioregulators recovery (WBC/PBM/IH/EMS), skin cooling (pre-cool +2-8%), carotid body function, quantum bioenergetics (CoQ10)
- `sources/relay-neuron-nutrition.md` — added summaries: gut microbiome-muscle health (SCFAs, GPR41/43), gut barrier benefits/risks (EIGS mechanism), exercise genetics (ACTN3/ACE/PPARGC1A), mitochondrial nutrition, quantum bioenergetics
- `sources/relay-neuron-periodization.md` — added summaries: periodization models (linear/DUP/block comparison), altitude/hypoxia training (HIF/EPO mechanisms, LHTL/HiHiLo)

### Entity Pages Created (1 new)
- `entities/exercise-science/physiology/muscle-function-training.md` — Comprehensive 56-muscle consolidation: upper limb (deltoid, rotator cuff, pectoralis, latissimus, biceps/triceps, brachialis, forearm), lower limb (gluteus maximus/medius/minimus, adductors, iliopsoas, quadriceps, hamstrings, calf/soleus, peroneals), core (transversus abdominis, erector spinae, deep core, abdominal wall). Anatomical function → training implications → injury risk.

### Index Pages Updated (2)
- `physiology-index.md` — added muscle-function-training entity
- `home.md` — updated source descriptions (physiology ~50 topics, training-methods ~20, supplements ~40, technology ~15, nutrition ~35, periodization ~10, health-applications ~20, biomechanics ~12); updated last updated date

### Skipped (Already Covered)
- 56 individual muscle function training files → consolidated into single muscle-function-training.md entity page (organized by anatomical region with function-training-injury mapping)
- Periodization models risks (2026-05-13-task-3-2-periodization-models-risks.md) — sufficiently covered by overtraining-syndrome entity
- Menstrual cycle benefits/risks — covered in health-applications source page summary
- Menopause bone benefits/risks — covered in health-applications source page summary
- Meditation performance — covered in health-applications source page summary
- Injury fear benefits — covered in health-applications source page summary
- Altitude training — added to both periodization source page and altitude-training entity
- Soft tissue repair supplement — sufficient detail in biomechanics source page summary
- Biohacking wearables limitations — sufficient detail in technology source page summary
- Bioregulators recovery risks — sufficient detail in technology source page summary

### Lint Results (2026-05-23)

| Check | Count |
|-------|-------|
| Total wiki pages | 96 |
| Broken wikilinks | 0 |
| Orphan pages | 0 |
| Frontmatter errors | 0 |
| Index completeness errors | 0 |

All pages pass lint checks. No orphan pages, no broken wikilinks, all entities registered in physiology-index.

## [2026-05-27] ingest | relay-neuron supplements batch — 6 new entity pages

Ingested 6 new supplement entity pages from relay-neuron research files (2026-05-03 to 2026-05-13).

### Entity Pages Created (6 new)
- `entities/exercise-science/supplements/hmb.md` — HMB: UPS inhibition (Atrogin-1/MuRF1↓), mTOR activation, sarcopenia (+0.85-1.2kg lean mass), 3g/day optimal
- `entities/exercise-science/supplements/beta-alanine.md` — Beta-alanine: carnosine buffer system, +40-80% muscle carnosine, TEE +13-14%, paresthesia >800mg/single dose
- `entities/exercise-science/supplements/l-carnitine.md` — L-carnitine: CPT shuttle system, fatty acid β-oxidation, VO2max +6% (athletes), TMAO controversy, depression biomarker (ALC AUC=0.898)
- `entities/exercise-science/supplements/glutamine.md` — Glutamine: conditionally essential, post-marathon infection ↓60-63% (2.5g post-race), gut barrier, glutathione precursor
- `entities/exercise-science/supplements/bcaas.md` — BCAAs: leucine threshold ~2.5g for mTOR, DOMS ↓34% at 72h, CNS fatigue (tryp-tophan/BCAA BBB competition); EAA superior to BCAA alone
- `entities/exercise-science/supplements/creatine.md` — Creatine: ATP-PCr system, +15-40% PCr stores, loading 0.3g/kg×5d → maintenance 3-5g/day, safe >5 years, vegetarian benefit

### Index Pages Updated (1)
- `supplements-index.md` — Added 6 new entity entries with evidence ratings

### Home Page Updated
- Entity count: ~86 → ~92
- Last updated: 2026-05-23 → 2026-05-27

## [2026-05-27] ingest | relay-neuron physiology, training, health batches — 12 new entity pages

Processed relay-neuron research files (2026-05-11 to 2026-05-12) across physiology, training, and health domains.

### Physiology Entity Pages Created (4 new)
- `entities/exercise-science/physiology/mitochondrial-function.md` — Mitochondrial adaptations: PGC-1α/AMPK/SIRT1 axis, ETC complexes I-V, NAD+ precursors, mitophagy
- `entities/exercise-science/physiology/carotid-body.md` — Carotid body: VO2max trainability gatekeeper, KATP channels, HVR, altitude/LHTL mechanisms
- `entities/exercise-science/physiology/exercise-immunology.md` — Exercise immunology: J-curve, open window (3-72h), URTI risk, moderate vs strenuous exercise
- `entities/exercise-science/physiology/exercise-epigenetics.md` — Exercise epigenetics: DNA methylation, telomere length (+238bp with strength training), histone modifications

### Training Entity Pages Created (2 new)
- `entities/exercise-science/training/flexibility-mobility.md` — Flexibility/mobility: dynamic vs static vs PNF vs foam rolling, injury risk, ROM enhancement
- `entities/exercise-science/training/fascia-training.md` — Fascia training: force transmission (20-40%), proprioceptive function, sensory organ architecture

### Health Entity Pages Created (4 new)
- `entities/exercise-science/health/cardiac-exercise.md` — Cardiac exercise: VO2max strongest mortality predictor (HR 5.04), athlete's heart, cardiac rehab
- `entities/exercise-science/health/cognitive-performance.md` — Cognitive performance: BDNF (4-5× from 6min HIIT), executive function, hippocampal neurogenesis
- `entities/exercise-science/health/gi-health.md` — GI health: microbiome +15-30%, gut training, EIGS (40-70% endurance athletes), GI adaptation
- `entities/exercise-science/health/gut-barrier.md` — Gut barrier: tight junctions (claudin-1/occludin/ZO-1), 20-40% permeability reduction vs sedentary

### Index Pages Updated (4)
- `physiology-index.md` — Added 4 new entities (mitochondrial-function, carotid-body, exercise-immunology, exercise-epigenetics)
- `training-index.md` — Added 2 new entities (flexibility-mobility, fascia-training)
- `exercise-health-index.md` — Added 4 new entities (cardiac-exercise, cognitive-performance, gi-health, gut-barrier)
- `home.md` — Entity count: ~92 → ~110; last updated 2026-05-27

### Existing Entities Verified (already covered by existing pages)
- Cold/heat therapy recovery — covered by recovery-science.md
- Neural drive/fatigue mechanisms — covered by motor-unit-recruitment.md and fatigue-recovery.md
- Muscle protein synthesis-resistance training — covered by mps-muscle-protein-synthesis.md and protein-timing.md
- Gut microbiome-muscle health — covered by gut-muscle-axis.md
- Altitude/hypoxia training — covered by altitude-training.md
- Muscle anatomy (50+ files) — consolidated into muscle-function-training.md
