# Research decisions

| Decision | Selection and justification |
|---|---|
| Focus | Tool-selection validity under overlapping API descriptions; separates tool choice from arguments and downstream execution. |
| Scope | One-step static choice, not autonomous multistep agents. Restriction enables inspectable labels and fast exact reruns. |
| Data | Generated, explicitly labeled tools and queries. No human-user or API usage data claims. |
| Primary outcome | Correct feasible tool selection, including explicit abstention when appropriate. |
| Comparators | Word and character TF-IDF rankers; both lightweight established IR baselines. |
| Constrained method | Deterministic filtering by exposed metadata, followed by lexical ranking among feasible candidates. |
| Ablations | Drop domain and format filters independently to locate the contributions of constraint classes. |
| Perturbations | Order changes and content-neutral generic distractor phrases. |
| Source of uncertainty | Paired bootstrap across generated test cases; not an independent estimate of natural-language population performance. |
| Novelty | No claim that tool-choice robustness, retrieval filtering or metadata-aware selection is newly invented. |
| Paper interpretation | Empirical controlled demonstration with strong closed-world limitations, not a state-of-the-art benchmark result. |
