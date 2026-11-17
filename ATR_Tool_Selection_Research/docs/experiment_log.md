# Experiment log

**Run date:** 2026-11-14 (UTC environment; exact wall-clock timing not the research variable)

**Research objective:** Measure constraint-valid tool choices on a controlled synthetic catalog.

**Implementation:** TF-IDF retrieval with word or character n-grams; deterministic hard-constraint filtering for region, recency, output format and tool domain; two ablations.

**Evaluation:** 96 generated tools; train/dev/test query-template families; 228 test cases (192 valid, 24 no-feasible-tool, 12 no-tool-needed); five methods; original, reordered and distractor descriptions.

**Executed commands:** `python -m unittest discover -s tests -v`; `python -m src.run_experiment`; `python -m src.plot_results`.

**Observations:** Eight tests pass. Original test accuracy: 49.12% word TF-IDF, 56.14% character TF-IDF, 100.00% constraint-aware, 64.91% without domain constraint, 89.47% without format constraint. See `results/metrics.csv` and `results/predictions.csv` for exact records.

**Interpretation:** The generated queries consistently expose domain/region/recency/format markers. The constraint-aware system is deliberately optimized for that schema; its perfect score is a validation of a closed-world rule system, not proof of superiority on naturally occurring LLM tool choices.

**Reproducibility:** Environment and dataset hashes in `results/environment.json`; bootstrap seed 2026; method definitions in `src/selectors.py`. Runtime latency is recorded but not compared statistically due to uncontrolled execution environment.
