# Academic Article Summary

## 1. Bibliographic Information

- Source ID: SRC-005
- Title: Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs
- Authors: Hexiang Tan; Fei Sun; Sha Liu; Du Su; Qi Cao; Xin Chen; Jingang Wang; Xunliang Cai; Yuanzhuo Wang; Huawei Shen; Xueqi Cheng.
- Publication Year: 2025
- Journal or Conference: Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 4755-4765. Association for Computational Linguistics.
- DOI: [10.18653/v1/2025.emnlp-main.238](https://doi.org/10.18653/v1/2025.emnlp-main.238)
- Original Publication URL: [publisher record](https://aclanthology.org/2025.emnlp-main.238/); [original PDF](https://aclanthology.org/2025.emnlp-main.238.pdf)
- Local Document Path: None; original publisher PDF inspected online.
- Access Status: FULL_TEXT. Main methods/results, Tables 1-4, limitations, and relevant appendices inspected. PDF page 1 corresponds to printed p. 4755; PDF pagination below is one-based.
- Rights/access check: [ACL copyright policy](https://aclanthology.org/faq/copyright/) identifies ACL materials published from 2016 onward as CC BY 4.0. No AI-processing restriction or access barrier was identified for this paper. The summary is attributed paraphrase, not a reproduction.
- Extraction version: Initial summary; independent verification pending.

## 2. Research Overview

The paper studies incorrect answers that remain semantically equivalent across stochastic generations, rather than treating agreement as sufficient evidence of correctness (C001). It compares detection performance on consistent-error and inconsistent-error subsets of TriviaQA and SciQ (C002-C007). It then evaluates combining a generating model's hidden-state probe with a separately trained probe on another model's representations of the same question/answer (C008-C011). Its experiments concern detection, not a demonstrated correction procedure or causal explanation for the errors (C012).

## 3. Research Questions

The explicit investigations concern the prevalence of self-consistent errors across model scales, the ability of existing detector families to identify them, and whether an external model's representations improve detection (C004-C011). The possibility that training-data misconceptions cause such errors is a case-based hypothesis, not a causal finding (C012).

## 4. Methodology

- **Operational definition:** Compare a greedy answer with 15 samples at temperature 0.5 and test semantic equivalence using mutual entailment; distinguish this labeling procedure from the SE baseline's ten samples (C001, C005).
- **Data and evaluation:** Use TriviaQA and SciQ with paired consistent-error/inconsistent-error subsets; evaluate AUROC rather than classification accuracy (C002). Llama-3.1-70B judges correctness against reference answers; refusals are excluded (C003).
- **Baselines:** Token probability, prompted P(True), semantic entropy, and supervised hidden-state probes, evaluated on four generator configurations; distinguish in-domain and cross-dataset probe evaluation (C005).
- **Intervention:** Train an external-model probe and mix its score with the original-model probe using a validation-selected weight; the verifier reads the existing question/answer rather than providing external documentary evidence (C009).

## 5. Key Findings

1. The authors observe that self-consistent errors persist across tested model scales, unlike the stronger decline in inconsistent errors; this is not a universal monotonic scaling law (C004).
2. Semantic entropy performs much worse on consistent-error subsets, with Table 2 CE AUROC ranging from 0.3633 to 0.5427. Not every CE value is at or below chance (C006).
3. Supervised probes also have CE/IE gaps, although their CE scores exceed the corresponding training-free scores in the reported table (C007).
4. Tested verifier models often produce different errors from Qwen2.5-7B, but overlap is nonzero and the result does not imply independent errors in every setting (C008).
5. Cross-model probes improve the selected CE results, with an explicit exception to a blanket claim of no IE performance loss (C010).
6. The verifier-selection experiment favors the displayed larger/different-family alternatives, but its baseline must be kept separate from Table 2's slightly different values (C011).

## 6. Evidence Table

| Claim ID | Claim | Source Location | Evidence Type | Qualifications | Verification Status |
| --- | --- | --- | --- | --- | --- |
| C001 | A self-consistent error is an incorrect greedy answer semantically equivalent to all 15 stochastic samples, generated with temperature 0.5, top_p=1 and top_k=-1; equivalence uses mutual entailment. Appendix A.5 reports declining identified CE counts as k grows from 1 to 15, with a convergence trend above 10. | Printed p. 4756, Sections 2.1-2.2 (PDF p. 2); pp. 4762-4763, Fig. 4 and Appendix A.5 (PDF pp. 8-9) | Definition and operationalization | Sample-dependent categorization, not proof that an error will repeat indefinitely. The 15-sample labeling procedure differs from the ten-sample SE detector in C005. | PENDING_VERIFICATION |
| C002 | On TriviaQA and SciQ, the CE subset uses self-consistent incorrect answers as negatives and the IE subset uses inconsistent incorrect answers; the two subsets have identical negative-example counts and are paired with the same number of positive examples for training. Detection is measured with AUROC. | Printed p. 4757, Section 3.1 (PDF p. 3) | Evaluation design | Controls training-volume differences between error types; does not establish natural deployment prevalence or classification accuracy. Exact split sizes are not supplied in this cited description. | PENDING_VERIFICATION |
| C003 | Correctness labels compare responses with reference answers using Llama-3.1-70B; refusal responses are filtered out. The authors report one disagreement with human annotation in a manual review of 300 samples. | Printed p. 4763, Appendix A.4; pp. 4764-4765, evaluation prompt (PDF pp. 9-11) | Labeling and validation | Labels are model judgments against reference answers, not independent human annotation of the entire dataset. The 300-sample check does not establish error-free labels or performance on refusals. | PENDING_VERIFICATION |
| C004 | The prevalence analysis spans Qwen2.5-3/7/14/32/72B-Instruct and Llama3.2-1/3B plus Llama3.1-8/70B-Instruct on TriviaQA and SciQ; the authors report that self-consistent error counts remain relatively stable or increase while inconsistent errors decrease more strongly with scale. | Printed pp. 4755-4756, Fig. 1 and Section 2.3; p. 4762, Fig. 3 (PDF pp. 1-2, 8) | Empirical trend and author interpretation | Restricted to tested families/tasks and the C001 definition. Counts need not be monotonic at each successive model size; this is not proof of an immutable scaling law. No numerical plot heights are estimated here. | PENDING_VERIFICATION |
| C005 | Detection comparisons use Llama3.1-8B, Qwen2.5-7B/14B and Mistral-12B, with mean token log-probability, prompted P(True), semantic entropy, and supervised probes. SE uses ten samples at temperature 0.5. Probes use an FFN with hidden dimensions (256,128,64), validation-based layer/checkpoint choice, and ID versus cross-dataset OOD evaluation. | Printed p. 4757, Section 3.1; p. 4763, Appendix A.3 (PDF pp. 3, 9) | Baselines and implementation | Model-internal probability/hidden-state access differs from black-box-only checking. ID and OOD describe dataset relationships, not guaranteed robustness across all domains. | PENDING_VERIFICATION |
| C006 | In Table 2, semantic-entropy CE AUROC ranges from 0.3633 to 0.5427 across the four models and two tasks. For Llama3.1-8B, SciQ CE/IE values are 0.4608/0.8820 and TriviaQA CE/IE values 0.5216/0.9226. | Printed p. 4758, Table 2 (PDF p. 4) | Experimental result | AUROC, not accuracy. These numbers show severe CE degradation, but contradict a literal interpretation that every SE CE result is at or below 0.5. The range is a minimum/maximum read from the displayed eight CE entries. | PENDING_VERIFICATION |
| C007 | For Llama3.1-8B, the baseline ID probe has SciQ CE/IE AUROC 0.7917/0.9249 and TriviaQA 0.7922/0.9272; the OOD probe has 0.7287/0.9080 and 0.7396/0.8989 respectively. Across Table 2, baseline probes have lower CE than IE scores and higher CE scores than the displayed training-free alternatives. | Printed p. 4758, Table 2 and Section 3.2 (PDF p. 4) | Experimental result | Supports difficulty under the controlled CE/IE setup; does not establish that hidden states contain no useful information. The numerical example concerns one generator and two datasets. | PENDING_VERIFICATION |
| C008 | Table 3 compares verifier errors with Qwen2.5-7B: Qwen2.5-14B repeats equivalent self-consistent errors for 273 of 952 SciQ-CE questions (28.7% reported), while Llama3.1-70B does so for 251 of 4,638 TriviaQA-CE questions (5.4% reported). The largest displayed overlap percentage is 28.7%. | Printed p. 4758, Table 3 and Section 4 (PDF p. 4) | Cross-model error-overlap result | Applies to the table's reference-model CE question sets and tested verifiers; non-overlap does not mean the verifier necessarily answers correctly or that model errors are statistically independent. | PENDING_VERIFICATION |
| C009 | The cross-model method trains separate probes on generator and verifier hidden states for the same question/generated response, combining their scores as (1-lambda)*generator_score + lambda*verifier_score. Table 2 uses Qwen2.5-14B as verifier except for that generator, which uses Llama3.1-70B; lambda is selected on validation from 0,0.05,...,1. | Printed p. 4758, Section 4, Section 4.1 and Table 2 caption (PDF p. 4) | Method design | Requires supervised probe training and internal representations of both models. An external verifier model is not external documentary evidence. Validation-selected mixing weights are not a fixed universal setting. | PENDING_VERIFICATION |
| C010 | In Table 2, adding the cross-model probe to Llama3.1-8B OOD increases SciQ-CE AUROC from 0.7287 to 0.8289 and TriviaQA-CE from 0.7396 to 0.8024. For Qwen2.5-14B OOD, TriviaQA-CE rises from 0.7871 to 0.8754, but TriviaQA-IE falls from 0.9174 to 0.9115. | Printed p. 4758, Table 2 (PDF p. 4) | Experimental result and numerical qualification | CE improvements do not justify an exceptionless assertion that IE performance never decreases. These are displayed benchmark scores, not evidence of statistical significance or guaranteed deployment gains. | PENDING_VERIFICATION |
| C011 | In Table 4, the Qwen2.5-7B probe baseline has SciQ-CE/TriviaQA-CE AUROC 0.8250/0.8662. Adding Qwen2.5-3B yields 0.8357/0.8712, and adding Llama3.1-70B yields 0.8794/0.9511. | Printed p. 4759, Table 4 and verifier-selection discussion (PDF p. 5) | Verifier-selection experiment | Keep this experiment separate: Table 4 baseline TriviaQA-CE 0.8662 differs from Table 2 ID baseline 0.8626, and some IE baselines also differ. The inspected discussion does not explain those discrepancies. Selected values do not isolate model size from all other factors. | PENDING_VERIFICATION |
| C012 | The paper offers case-based hypotheses about widespread misconceptions or conceptual confusion and explicitly says causal determination needs further investigation, including access to training data or controlled experiments; its main contribution concerns detection, while causes and mitigation are future questions. | Printed p. 4757, Section 2.3; pp. 4759-4760, Conclusion and Limitations (PDF pp. 3, 5-6) | Author-reported limitations and interpretation | Do not turn illustrative cases into causal proof or detection improvements into demonstrated correction of generated content. | PENDING_VERIFICATION |

## 7. Author Conclusions

The authors conclude that self-consistent errors expose limitations of detectors using only the generating model's signals and that an external-model probe offers a promising direction (C006-C011). This interpretation should retain the scope of the datasets, model families and labeling procedure (C001-C005), the explicit IE exception (C010), and the unresolved causal explanation (C012).

## 8. Research Limitations

**AUTHOR_REPORTED_LIMITATIONS:** Root causes remain unestablished; training-data misconceptions or training-induced biases are hypotheses requiring controlled investigation (C012).

**ADDITIONAL_OBSERVATIONS (summarizer interpretation):** The operational definition depends on sampling and entailment decisions (C001). Reference-conditioned model labels and refusal exclusion limit what the evaluation establishes (C003). Task-specific AUROC does not directly establish deployed accuracy, error prevalence, or correction success (C002, C010, C012). Cross-model probing assumes access to internal states and labeled probe training data (C009). Table-level exceptions and baseline discrepancies should remain visible rather than be replaced by stronger narrative generalizations (C006, C010-C011).

## 9. Relevance to Assignment

The study directly informs limitations of consistency-based detection (C001, C006-C007) and offers a form of cross-model checking that must be distinguished from evidence-based fact checking using documentary sources (C009). It supplies a critical perspective without selecting a thesis or drawing cross-publication conclusions.

## 10. Questions and Uncertainties

- Table 4 and Table 2 baseline differences remain unexplained in the inspected passages (C011); do not merge their results.
- Table 3's reference-set counts should not be substituted for a complete training/test split specification (C002, C008).
- Screenshot calls returned no inspectable images. Tables were read from original PDF text; no numeric graph values were inferred from plotted heights.
- The main methods text does not fully specify split counts in the cited subset description (C002). Do not invent them.
- How far the results generalize to other tasks, model families, or refusal behavior remains an open interpretation question (C002-C005).

## 11. Summary Status

COMPLETE_FOR_INDEPENDENT_VERIFICATION. Twelve claims C001-C012, all PENDING_VERIFICATION; six key findings. Full text was accessible, with no observed licensing/access blocker. Only this summary was written. A separate verifier must independently inspect every claim and the narrative before any claim advances.
