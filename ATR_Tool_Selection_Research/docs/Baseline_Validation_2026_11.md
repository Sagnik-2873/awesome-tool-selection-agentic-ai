# Baseline validation record — 14 November 2026

## Verified by local execution
- `python -m unittest discover -s tests -v`: eight tests passed.
- `python -m src.run_experiment`: generated `dataset/` and `results/` on the bundled static ontology, without external network access or credentials.
- `python -m src.plot_results`: regenerated `figures/accuracy.png` and `figures/error_categories.png`.
- `python -m scripts.demo`: script ran successfully.
- Original-description test results: word TF-IDF 112/228 (49.12%); character TF-IDF 128/228 (56.14%); constraint-aware 228/228 (100%); no-domain ablation 148/228 (64.91%); no-format ablation 204/228 (89.47%).
- The actual CSV and environment records are in `results/` and support these manuscript numbers.

## Method-protocol discrepancies and scientific boundaries
- This is **not** a Gorilla, ToolLLM or ToolSandbox model reproduction. Comparators are independently implemented TF-IDF procedures from scikit-learn and a deterministic rule system.
- The selector is able to read exactly the metadata labels used to construct the test gold labels. A perfect score is expected under this closed-world generation process.
- Retrieval baselines always select some tool, and thus cannot score on 36 negative/no-tool cases. This makes overall accuracy an asymmetric comparison. The paper states this limitation.
- All tasks are templates. Test requests use disjoint text forms but not new domains or unseen catalog attributes. No independent annotation has been performed.
- Item-bootstrap intervals describe the synthetic cases and should not be advertised as population-level significance.
- Timing is uncontrolled and only descriptive.

## State of verification
**VERIFIED:** program execution, internal label integrity checks, measured outputs, figure generation, LaTeX compilation.  **UNCERTAIN:** independent generalization, externally audited test labels, reproducibility on other OS/software versions. **NOT CLAIMED:** published baseline reproduction, human-subject data, real LLM performance, novel algorithm.
