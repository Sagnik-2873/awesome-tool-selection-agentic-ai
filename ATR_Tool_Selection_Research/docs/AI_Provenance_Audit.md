# AI assistance and research integrity record

This audit accompanies a postgraduate coursework project that explicitly requires recording human–AI collaboration (assignment Prompt 18). It documents known activities; it does not infer unobserved student judgments, manual source checks, or Git commits.

| Task | Tool / assistance | Evidence of output | Verification or unresolved human ownership |
|---|---|---|---|
| Topic and gap narrowing from earlier review | ChatGPT GPT-6, conversations during Oct.–Nov. 2026 | Literature-gap and methodology records; `docs/research_decisions.md` | Uploaded review was examined; original-primary-source cross-check is selective, not exhaustive. |
| Synthetic case generator and comparator code | ChatGPT GPT-6 programming assistance | `src/benchmark.py`, `src/selectors.py`, `tests/` | Eight local tests passed; real predictions and CSV outputs saved. Student code-understanding demonstration not independently observed. |
| Experiment execution and interpretation | ChatGPT GPT-6 / Python shell | `results/run.log`, `results/metrics.csv`, `results/predictions.csv`, figures | Re-executed locally on 14 Nov. 2026; reported numbers reconcile with CSV. No claim of external reproduction. |
| Manuscript drafting and LaTeX source | ChatGPT GPT-6 writing and technical assistance | `docs/Research_Paper.tex`, `docs/Literature_Review_Revised.tex` | Both compile in local pdfLaTeX; scholarly accuracy remains author responsibility. |
| Assignment correspondence and audit | ChatGPT GPT-6 | `docs/Assignment_Verification.md`, this file | Both user-provided PDFs inspected; 18 prompts verified; identified missing LaTeX source in prior package. |

## Actual verification / correction examples

1. **Earlier prototype ceiling effect:** an earlier 32-tool/96-query proof-of-execution scored 100% for both simple methods and was recognized as uninformative. The expanded 96-tool/228-test benchmark was generated and executed. This does not remove the shared-ontology limitation.
2. **Deliverable gap:** the previously prepared submission ZIP did not contain an implementation paper `.tex` even though the assignment specifically requires LaTeX. An actual buildable `.tex` plus its PDF and supporting bibliography were added.
3. **LaTeX compilation errors:** the first implementation-paper LaTeX build failed because `xcolor` was absent and subsequently because the runtime lacked `bibtex`; the document was corrected and compiled with a manual bibliography while retaining a separate reference `.bib` data file. No fake successful BibTeX build is claimed.
4. **Code and output re-verification:** eight tests and the experiment/plot/demo commands were rerun. Reported test counts matched saved CSVs.

## Accountability and limits

The coursework's goal is supervised use of AI rather than concealment. AI-assisted drafting, coding and technical checking are explicitly acknowledged; no Turnitin AI-detection percentage or independent student-authorship score has been measured. Authorship, final source checking, judgment about claims and ability to explain the repository remain the student's responsibility. Nothing in this report claims human verification that has not actually been observed.
