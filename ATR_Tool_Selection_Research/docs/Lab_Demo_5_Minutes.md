# Five-minute demonstration outline

**00:00–00:45 — Problem.** Explain why tool description similarity is different from respecting domain, regional coverage, freshness and output-format requirements. Reference the original review's distinction between selection and downstream tool success.

**00:45–01:40 — Dataset.** Open `src/benchmark.py`. Show twelve service categories and the product of domain × region × freshness × format. Show a valid case and a no-suitable-tool case in `dataset/cases.json`. Explain the synthetic nature and generated gold labels.

**01:40–02:40 — Methods.** Open `src/selectors.py`. Show word and character TF-IDF retrieval, then the domain/region/mode/format checks and the two ablations. Explain why the constrained method can abstain but the lexical baselines cannot.

**02:40–03:30 — Live rerun.** Run `python -m unittest discover -s tests -v` and `python -m src.run_experiment`; display `results/metrics.csv` and test counts. Then run `python -m scripts.demo`.

**03:30–04:20 — Graphs.** Open `figures/accuracy.png` and `figures/error_categories.png`. Compare the five measured methods. Note that 100% is a ceiling effect caused by matched ontology and explicit metadata.

**04:20–05:00 — Validity and limitation.** State that this is Pathway B, an independently coded controlled comparison, not a reproduction of Gorilla. Mention template/case circularity, missing LLM execution and need for separately authored test cases to assess external validity.
