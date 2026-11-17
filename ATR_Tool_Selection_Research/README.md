# Constraint-Valid Tool Selection Under Description Variation

A reproducible computational study of tool-choice accuracy under overlapping API descriptions, explicit operational constraints, and abstention cases. The repository contains source code, an inspectable synthetic benchmark, original execution results, automated tests, analysis figures, and a research manuscript.

## Research question

How do conventional lexical tool retrieval methods compare with a metadata-aware selector when tools are similar in purpose but differ in coverage, freshness, and output format?

**Scope:** Static tool selection only. This experiment does not execute remote APIs or benchmark an LLM. It is a controlled, generated-data study, not a reproduction of Gorilla or ToolLLM.

## Key results

| Test set (n=228, original descriptions) | Accuracy |
|---|---:|
| Word TF-IDF | 49.12% |
| Character TF-IDF | 56.14% |
| Constraint-aware selector | 100.00% |
| Ablation: without domain filter | 64.91% |
| Ablation: without format filter | 89.47% |

The rule-based approach has direct access to the exact metadata schema used in the generated benchmark, making its perfect score unsurprising. Results should not be extrapolated to real-world or unseen schemas. Full metrics for three description variants and train/dev/test splits are saved in `results/metrics.csv`.

## Repository layout

```text
src/                benchmark generation, selectors, evaluation and plots
scripts/            convenience commands
configs/            evaluated study configuration
dataset/            generated tools and task records
tests/              eight automated unit tests
results/            predictions, summary tables, bootstrap intervals and logs
figures/            exported evaluation plots
docs/               manuscript, complete project dossier and bibliographic records
.github/workflows/  automated tests on push and pull request
```

## Reproduction

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m src.run_experiment
python -m src.plot_results
python -m scripts.demo
```

The scripts use fixed data templates and deterministic tie-breaking. Timing figures are descriptive and depend on machine load. `results/environment.json` records library versions, case counts and SHA-256 checksums of the evaluated data.

## Experimental design

- 96 tools: 12 service categories × 2 geographical coverages × 2 data recencies × 2 output formats.
- Separate generated query template families for train, development and test.
- Test subset: 192 feasible requests, 24 unavailable-format requests and 12 no-tool requests.
- Methods: word TF-IDF, character TF-IDF, constrained selection, and two constraint-removal ablations.
- Description conditions: original, field-reordered and generic-marketing-distractor descriptions.
- Accuracy is evaluated against feasible tool IDs; a no-tool / unavailable-tool task is correct only when the selector abstains.
- Paired bootstrap intervals (3,000 resamples) summarize differences on generated test cases; repeated template dependence makes them descriptive rather than population-level inferential claims.

## Reproducibility and integrity

All reported numeric results were produced by `python -m src.run_experiment`; no experimental results were imputed. The catalog and requests are automatically generated and do not contain private or externally sourced user data. Benchmark artifacts and model scripts are included to permit inspection and reruns. The project is a synthetic prototype and not a deployment-ready agent.

## Research context

The problem is motivated by prior published studies of API selection, tool-retrieval failure modes, tool-description effects, and redundant tools. Detailed citations and distinctions are provided in `docs/references.bib`, `docs/Research_Paper.tex`, and the manuscript PDF. The revised source literature review is also supplied as `docs/Literature_Review_Revised.tex` and `.pdf`. Assignment-specific mapping and evaluation caveats are documented in `docs/Assignment_Verification.md`. The required collaboration disclosure is `docs/AI_Provenance_Audit.md`.

## Manuscripts and research records

- **Implementation paper:** `docs/Research_Paper.pdf` and `docs/Research_Paper.tex`; experiment figures in `figures/`; citation metadata in `docs/references.bib` (the compiled LaTeX source uses a compatible inline bibliography because this runtime does not include BibTeX).
- **Revised literature review:** `docs/Literature_Review_Revised.pdf` and `.tex`; earlier source retained in `docs/Literature_Review_Original.pdf` for provenance.
- **Assignment and audit:** `docs/Assignment_Verification.md` maps evidence to Prompts 01–18. `docs/Baseline_Validation_2026_11.md`, `docs/Technical_Peer_Review.md` and `docs/AI_Provenance_Audit.md` report implementation strengths and research limitations. `docs/Lab_Demo_5_Minutes.md` supplies the evaluation walkthrough.

### LaTeX build

From the `docs/` directory, the PDF sources can be compiled by:

```bash
pdflatex -interaction=nonstopmode -halt-on-error Research_Paper.tex
pdflatex -interaction=nonstopmode -halt-on-error Research_Paper.tex
pdflatex -interaction=nonstopmode -halt-on-error Literature_Review_Revised.tex
pdflatex -interaction=nonstopmode -halt-on-error Literature_Review_Revised.tex
```

The paper cites the scientific literature but does not report published-model reproduction. The test cases and tool ontology are generated from the same code, and a perfect rule-based score is a controlled synthetic outcome rather than external validity. See the manuscript and audit for details.
