# Academic Article Summary

## 1. Bibliographic Information

- Source ID: SRC-004
- Title: SAC³: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency
- Authors: Jiaxin Zhang; Zhuohang Li; Kamalika Das; Bradley Malin; Sricharan Kumar
- Publication Year: 2023
- Journal or Conference: Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 15445-15458. Association for Computational Linguistics.
- DOI: [10.18653/v1/2023.findings-emnlp.1032](https://doi.org/10.18653/v1/2023.findings-emnlp.1032)
- Original Publication URL: [publisher record](https://aclanthology.org/2023.findings-emnlp.1032/); [original publisher PDF](https://aclanthology.org/2023.findings-emnlp.1032.pdf)
- Local Document Path: Not downloaded; original publisher PDF inspected online.
- Access Status: FULL_TEXT. Main text, methods, result tables, limitations, and relevant appendices inspected. Fourteen PDF pages; one-based PDF page 1 corresponds to printed p. 15445.
- Rights/access check: [ACL copyright policy](https://aclanthology.org/faq/copyright/) identifies post-2016 ACL materials as CC BY 4.0. No prohibition on this attributed summarization was identified. No access controls bypassed.
- Summary version: Initial extraction, 2026-11-13; all evidence awaits independent verification.

## 2. Research Overview

SAC³ extends sampled-response self-checking by varying the question while preserving its meaning and by consulting another language model. Its motivation is that repeated agreement can coexist with error, while disagreement can surround a correct original response (C001-C003). The evaluation distinguishes synthetic binary-answer classification tasks from manually annotated, model-generated open-domain answers (C004). Reported improvements depend on task, detector variant, and evaluation metric (C006-C009); the method does not supply an external factual reference or a guarantee of truth (C001-C003, C011).

## 3. Research Questions

The paper investigates whether question-level perturbation and model-level cross-checking improve hallucination detection beyond self-checking alone (C001-C003). Its ablations examine verifier weighting and the number of perturbed questions (C010). These are research aims inferred from the method and experiment structure rather than a formally numbered hypothesis list. The broader generalizability and efficiency questions remain open (C011-C012).

## 4. Methodology

- **Design:** Generate and filter paraphrased questions, sample target/verifier answers, compare whole question-answer pairs, and aggregate disagreement scores (C002-C003).
- **Data:** Prime Number and Senator Search each contain 500 questions with synthesized factual/nonfactual binary responses; HotpotQA-halu and NQ-open-halu each use 250 examples with generated answers and manual factuality labels (C004).
- **Models/settings:** Main target gpt-3.5-turbo; verifiers Falcon-7b-instruct and Guanaco-33b. The default setting uses ten question variants, temperature-zero perturbation/checking, and ten temperature-one baseline self-check samples (C005).
- **Measurement:** Balanced binary classification is reported as AUROC; all-hallucinated classification uses thresholded detection accuracy; open-domain results use AUROC (C006-C008). These values are not interchangeable.
- **Caveats:** Annotation details and source-internal reporting inconsistencies are retained below; no numeric plot heights were estimated (C004, C012).

## 5. Key Findings

1. On balanced Prime Number/Senator Search datasets, SAC³-Q score AUROC is 99.4/99.7, versus SC²'s 65.9/56.1 (C006).
2. On all-hallucinated sets at threshold 0.5, SAC³-Q detection accuracy is 93.2/97.0 versus SC²'s 48.2/29.6. Adding a verifier is not uniformly better: Guanaco-based SAC³-all gives 99.4/85.6 (C007).
3. Open-domain AUROC rises from SC²'s 74.2/70.5 to SAC³-Q's 81.3/77.2 on HotpotQA-halu/NQ-open-halu. The highest HotpotQA score in Table 4 is 88.0 for Guanaco SAC³-QM, not the 87.0 of Guanaco SAC³-all (C008).
4. The authors attribute weak verifier-only Senator Search performance to refusals caused by insufficient information; cross-model checks can therefore introduce a task-specific limitation rather than reliably resolve uncertainty (C009).
5. Verifier weighting and question sample count affect outcomes; gains diminish beyond five perturbed questions in the reported ablation, with costs and latency remaining relevant (C010-C012).

## 6. Evidence Table

Every row is an extraction awaiting independent verification. PDF locators below are one-based.

| Claim ID | Claim | Source Location | Evidence Type | Qualifications | Verification Status |
| --- | --- | --- | --- | --- | --- |
| C001 | The authors identify two failures of self-consistency as a factuality proxy: consistently wrong sampled responses can produce false negatives, while incorrect stochastic samples can cause a correct original response to be flagged. | Printed pp. 15447-15448 (PDF pp. 3-4), Section 3; Fig. 1 on p. 15446 (PDF p. 2) | Conceptual analysis with illustrative observations | Illustrations establish possible failure modes, not their prevalence in arbitrary models/domains. Agreement or disagreement alone is not a factual guarantee. | PENDING_VERIFICATION |
| C002 | SAC³ generates semantically equivalent question variants, filters variants through pairwise semantic-equivalence checking, obtains answers from target and verifier LMs, and compares whole QA pairs rather than answer strings alone. | Printed pp. 15448-15449 (PDF pp. 4-5), Sections 4.1-4.3.1; Table 7 on p. 15457 (PDF p. 13) | Method design | The equivalence checks are themselves model judgments. Different surface answers may express equivalent QA meanings. This is black-box checking without external factual resources, not evidence retrieval. | PENDING_VERIFICATION |
| C003 | Semantic equivalence is mapped to 0 for agreement and 1 for disagreement; question/model components average comparisons, and the final score is Z(SAC³-Q) + lambda times [Z(SAC³-M) + Z(SAC³-QM)], with lambda=1 by default. | Printed pp. 15449-15450 (PDF pp. 5-6), Sections 4.3.2-4.3.5, Eqs. 2-8 | Scoring rule | Higher component values indicate greater disagreement. The combined score is a weighted sum, not a calibrated probability; model confidence is reported separately. | PENDING_VERIFICATION |
| C004 | Prime Number has 500 questions about randomly chosen primes between 1,000 and 20,000, with true Yes and synthesized false No answers; Senator Search has 500 questions with true No and synthesized false Yes answers. HotpotQA-halu samples 250 training examples; NQ-open-halu contains 250 examples. Both generation sets use gpt-3.5-turbo answers manually compared with ground truth. | Printed p. 15450 (PDF p. 6), Section 5; pp. 15457-15458 (PDF pp. 13-14), Appendix C.3 | Dataset and labeling design | Classification responses are synthesized, not all naturally occurring errors. Generation labels are manual; annotator count and inter-annotator agreement are not reported in these descriptions. Do not infer a 50/50 generation-label balance. | PENDING_VERIFICATION |
| C005 | The main target is gpt-3.5-turbo, with Falcon-7b-instruct or Guanaco-33b verifiers. Perturbation and semantic checking use temperature 0.0; k=10 equivalent questions are generated. SC² uses 10 stochastic samples at temperature 1.0; nq=nqm=1 and nm=1 are defaults for SAC³ variants. | Printed pp. 15450-15451 (PDF pp. 6-7), Section 6.1 | Experimental setup | Model versions and prompts are those tested in this paper, not current systems. The paper combines SAC³-M with SAC³-QM when reporting model-level results; comparisons involve different response sources. | PENDING_VERIFICATION |
| C006 | Table 2's score AUROC values for balanced classification data (50% hallucinated, 50% factual) are 65.9/56.1 for SC² and 99.4/99.7 for SAC³-Q on Prime Number/Senator Search, respectively. | Printed p. 15451 (PDF p. 7), Table 2 and Section 6.2.1 | Experimental result | Values use the displayed 0-100 AUROC scale and the score columns, not accuracy or verbalized-confidence columns. Synthetic binary-response setting; no general deployment accuracy claim. | PENDING_VERIFICATION |
| C007 | At threshold 0.5 on 100%-hallucinated classification data, Table 3 score-based accuracy is 48.2/29.6 for SC², 93.2/97.0 for SAC³-Q, 97.8/84.6 for Falcon SAC³-all, and 99.4/85.6 for Guanaco SAC³-all on Prime Number/Senator Search. | Printed p. 15451 (PDF p. 7), Table 3 and unbalanced-dataset discussion | Experimental result | These are detection accuracies on positive-only data, not balanced accuracy or AUROC. SAC³-all is best among these rows for Prime Number, whereas SAC³-Q is better on Senator Search. | PENDING_VERIFICATION |
| C008 | Table 4 score AUROC on HotpotQA-halu/NQ-open-halu is 74.2/70.5 for SC², 81.3/77.2 for SAC³-Q, 83.0/67.5 for Falcon SAC³-QM, 88.0/72.7 for Guanaco SAC³-QM, 84.5/77.1 for Falcon SAC³-all, and 87.0/77.2 for Guanaco SAC³-all. | Printed p. 15452 (PDF p. 8), Table 4 and Section 6.2.2 | Experimental result | Each generation dataset has 250 examples. No single added-verifier variant wins on both datasets; 88.0 belongs to Guanaco SAC³-QM, not SAC³-all. These are AUROC values, not percentages of corrected answers. | PENDING_VERIFICATION |
| C009 | For all-hallucinated Senator Search, Table 3 reports score accuracies of 21.0 for Falcon SAC³-QM and 45.6 for Guanaco SAC³-QM; the authors explain weak model-level performance by verifier refusals on many questions due to insufficient information. | Printed p. 15451 (PDF p. 7), Table 3 and unbalanced-dataset discussion | Experimental result and author explanation | Refusal-based explanation is the authors' interpretation; refusal frequency is not numerically reported here. The result does not show that a verifier's disagreement is automatically factual evidence. | PENDING_VERIFICATION |
| C010 | The authors report that a higher verifier weight helps on HotpotQA-halu where the verifier is stronger, whereas a smaller weight helps on NQ-open-halu; varying k from 2 to 10 yields diminishing gains after more than five perturbed questions. | Printed p. 15452 (PDF p. 8), verifier-weight/sample-count discussions, Figs. 5-6; Appendix C.1 on p. 15456 (PDF p. 12) | Ablation and author interpretation | Qualitative reported trends, not graph-digitized values or a universal optimal weight/sample count. The suggested 2-4 samples are a practical tradeoff, not a guarantee. | PENDING_VERIFICATION |
| C011 | The authors limit their experiments to QA and call for further evaluation of generalizability and semantic-equivalence accuracy in conversational/dialogue settings; they also flag the sampling cost-latency tradeoff and possible parallelization. | Printed p. 15453 (PDF p. 9), Limitations | Author-reported limitations | Broader task performance and latency improvements are future work, not established deployment results. Detection improvement should not be presented as elimination of hallucinations. | PENDING_VERIFICATION |
| C012 | Under the paper's equal-sample-count assumption, its cost discussion assigns SC² ns model calls and SAC³-all ns target calls plus 2ns verifier calls, excluding additional question-perturbation and equivalence-checking costs; Appendix C.1 proposes batching/parallelism to reduce overhead. | Printed p. 15453 (PDF p. 9), Computational Cost; pp. 15456-15457 (PDF pp. 12-13), Appendix C.1 | Analytic cost discussion and proposed optimization | This is the authors' simplified accounting, not measured runtime, dollar cost, or a complete API-call budget. Do not apply it as an exact cost formula for the unequal default sampling settings in C005. | PENDING_VERIFICATION |

## 7. Author Conclusions

The authors conclude that checking only repeated responses can miss errors and that question/model cross-checks improve detection on their benchmarks (C001, C006-C008). Their interpretation favors task-dependent verifier selection rather than assuming that another model is always beneficial (C009-C010). Broader conversational use and more efficient implementation remain research directions (C011-C012).

## 8. Research Limitations

**AUTHOR_REPORTED_LIMITATIONS:** QA-only evaluation; unestablished generalizability and semantic-equivalence accuracy for dialogue; sampling expense and latency (C011-C012). The reported verifier refusal issue is an additional task-specific limitation (C009).

**ADDITIONAL_OBSERVATIONS:** Synthetic binary responses and small generation datasets constrain extrapolation (C004). Model-judged equivalence and cross-model agreement do not independently certify factual truth (C001-C003). Positive-only detection accuracy cannot establish a false-positive rate on factual answers (C007). The data descriptions do not report annotator count or agreement (C004). These are qualifications of the reported design, not new experimental findings.

## 9. Relevance to Assignment

This paper connects self-consistency checking to model-level verification and supplies concrete limitations of agreement-based factuality signals (C001-C003). Its task-dependent results provide material for a later comparison, subject to independent verification, while keeping model cross-checks distinct from external evidence retrieval (C006-C012). No cross-paper synthesis or thesis is selected here.

## 10. Questions and Uncertainties

- **Internal reporting ambiguity:** Table 5 (printed p. 15453, PDF p. 9) is captioned as accuracy and its nearby prose mentions balanced data, yet its gpt-3.5 classification numbers repeat Table 3's positive-only accuracies and its generation numbers repeat Table 4's AUROCs. Its cross-model numeric comparisons are deliberately not promoted into evidence claims; clarification is required before using them.
- The introductory headline on printed p. 15446 combines classification numbers without the distinctions clear in Tables 2-3. Claims C006-C007 follow the specifically labeled tables instead.
- Exact generation-class balance, annotator count, and agreement are not supplied in the inspected dataset descriptions (C004). Do not invent these details.
- Screenshot retrieval was unavailable in the web tool. Numeric table columns were inspected in readable extracted PDF text; no values were estimated from plot geometry. Qualitative ablation claims follow the accompanying prose (C010).
- The framework's cost notation is simplified; retain the assumptions in C012 rather than extrapolating exact operational cost.

## 11. Summary Status

COMPLETE_FOR_INDEPENDENT_VERIFICATION: 12 claims, C001-C012, all PENDING_VERIFICATION; five key findings. Original full text and relevant appendices were inspected. No access/licensing blocker identified. Source-internal Table 5 ambiguity is explicitly preserved. Only this assigned summary was written; no independent claim verification or subsequent phase was performed.
