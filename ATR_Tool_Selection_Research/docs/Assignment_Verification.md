# Assignment verification: Prompts 01–18

**Source checked:** `AI_Tools_for_Research_post_mid_sem_assignment.pdf` (11 pages, uploaded November 2026). Prompts 01–18 occur on pp. 5–9; deliverables on pp. 9–10. Review basis: `LATEXPAPER.pdf`, *Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems* (13 pages).

## Required submissions and actual package

| Requirement from assignment | Included evidence | Verification / boundary |
|---|---|---|
| A. Research paper PDF, LaTeX, BibTeX, figures | `docs/Research_Paper.pdf`, `.tex`, `references.bib`, `figures/*.png` | PDF successfully compiled by pdflatex from `.tex`, numbered tables/figures inspected. Manuscript describes an internal synthetic comparative study, not a published-method reproduction. |
| B. GitHub repository / executable source | `src/`, `scripts/`, `tests/`, `README.md`, `requirements.txt`, `configs/`, `.github/workflows/` | Fresh local run successful. This is a downloadable repository; no external GitHub upload/commit has been performed by this environment. |
| C. Real experimental evidence | `results/predictions.csv`, `metrics.csv`, `paired_bootstrap.csv`, `environment.json`, logs; `figures/` | Recomputed outputs agree with reported test numbers. Dataset is generated, not external or manually labeled. |
| D. Research provenance | `docs/research_decisions.md`, `docs/source_verification.md`, `docs/AI_Provenance_Audit.md`, `docs/Baseline_Validation_2026_11.md` | Records actual assistance and limitations; student-source review of AI outputs is not claimed as completed. |
| E. Five-minute demonstration | `docs/Lab_Demo_5_Minutes.md`, `scripts/demo.py` | Reproducible runnable demo and outline; no live human presentation is claimed. |

## Prompt-to-evidence index

| Prompt | Evidence | Current status |
|---|---|---|
| 01 workspace and log | `docs/research_decisions.md`, source review | Present |
| 02 literature gaps | `docs/Literature_Review_Revised.pdf`, `docs/research_decisions.md` | Present, gaps are hypotheses rather than proven novelty |
| 03 literature-to-experiment bridge | `docs/source_verification.md`, manuscript §2 | Present, published tools not reproduced |
| 04 novelty/feasibility check | `docs/source_verification.md`, manuscript §2 | Present, not an exhaustive systematic review |
| 05 research question and criteria | `configs/study.json`, manuscript §3 | Present |
| 06 dataset and comparator check | `src/benchmark.py`, manuscript §§4–5, `dataset/` | Synthetic primary data only; licenses of externally sourced datasets are not implicated |
| 07 experiment blueprint | `configs/study.json`, manuscript §§4–6 | Current config records executed settings, but no independently timestamped pre-results freeze exists |
| 08 environment test | `results/environment.json`, `results/tests.log` | Verified local runtime |
| 09 baseline implementation | `src/selectors.py`, `src/run_experiment.py` | Executable baseline |
| 10 baseline verification | `docs/Baseline_Validation_2026_11.md`, `tests/` | Algorithm sanity verified; **no reproduction of Gorilla or ToolLLM** |
| 11 debugging | `docs/AI_Provenance_Audit.md`, test/compilation record | Real coding/LaTeX corrections documented; no imaginary debugging story |
| 12 contribution comparison | manuscript §§3, 5, 9 | Pathway B controlled comparison; no novel architecture claim |
| 13 empirical evaluation | `results/*.csv`, `figures/*.png`, `src/run_experiment.py` | Actual local runs confirmed |
| 14 interpretation and limitations | manuscript §§8–9 | Reported including ceiling effect / architectural asymmetry |
| 15 LaTeX manuscript | `docs/Research_Paper.tex`, PDF, `references.bib` | Compiled, 7 pages including references, with approximately 6 pages of main text |
| 16 technical peer review | `docs/Technical_Peer_Review.md` | Critical AI-assisted technical audit, not independent peer review |
| 17 GitHub documentation | `README.md`, reproducibility script, dependencies | Present; remote GitHub status not checked |
| 18 AI audit | `docs/AI_Provenance_Audit.md` | Present with provenance; human approval/ownership verification not implied |

## Material caveats for a viva

1. The main benchmark has generated gold labels, with a matching ontology used by the rule system. Results are internally valid for that setup but cannot establish generalization.
2. There is no LLM inference, no live API tool call and no validated reproduction of a published Gorilla / ToolLLM model. The selected contribution pathway is **B: controlled comparative study**.
3. The lexical baselines lack abstention, unlike the constraint-aware selector; overall accuracy reflects this unequal capability as well as tool discrimination.
4. Template-family splits do not prevent generator-to-selector circularity, nor do they create unseen-domain generalization.
5. The assignment requires documented and genuine AI assistance; this repository reports AI-generated text/code assistance rather than pretending no AI was used.
