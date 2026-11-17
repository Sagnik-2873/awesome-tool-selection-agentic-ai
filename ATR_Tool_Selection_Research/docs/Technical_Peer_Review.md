# Critical technical review of the implementation study

**Review type:** internal technical audit, not anonymous journal peer review.

## Major concerns

**M1 — Generator/selector circularity (Methods and Limitations).** The test cases and rule-based selector use the same finite set of domain/region/recency/format markers. This creates a favorable problem representation for the 100% method. **Response:** report as a closed-world proof-of-execution only; restrict the conclusion. A truly independent natural-language test set would be needed for generalization claims.

**M2 — Abstention asymmetry (Methods and Results).** Word/character TF-IDF cannot abstain, while the constraint-aware method can. Of 228 test requests, 36 require no tool. **Response:** report feasible-only accuracy separately and state the asymmetry; a rejection-enabled retrieval baseline would be needed to isolate metadata filtering fairly.

**M3 — No published model reproduction (Related Work).** The experiments do not execute Gorilla, ToolLLM or other cited agent models. **Response:** explicitly use Pathway B comparative study and avoid claiming original-paper metric replication.

**M4 — Limited validity of bootstrap (Evaluation).** The 228 cases are not independent draws because they share task templates and domains. **Response:** label intervals descriptive and avoid inferential significance claims.

## Minor concerns

**m1 — Paper length:** the LaTeX implementation paper compiles to seven pages including a references page, approximately six pages of main matter. Further independent evaluation, not filler, would still strengthen the manuscript.

**m2 — Text perturbations:** field reorder and generic sales text are mild controlled perturbations and cannot represent adversarial documentation attacks.

**m3 — Timing:** current per-request execution times are uncontrolled; they should not be used for efficiency rankings.

**m4 — Provenance:** AI assistance is documented, but there is no independent evidence that the student reviewed every code path or ran the project personally on their lab machine.

## Revision disposition
Major methodological concerns are disclosed in the manuscript. Additional experiments would be needed to resolve them; they are not disguised as completed. The manuscript is a defensible scoped classroom demonstration, not a general reliability claim about LLM agents.
