# Academic Article Summary

## 1. Bibliographic Information

- Source ID: SRC-006
- Title: FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs
- Authors: Albert Sawczyn; Jakub Binkowski; Denis Janiak; Bogdan Gabrys; Tomasz Kajdanowicz (PDF byline; publisher metadata uses Tomasz Jan Kajdanowicz).
- Publication Year: 2026
- Journal or Conference: Findings of the Association for Computational Linguistics: EACL 2026, pp. 5603-5621.
- DOI: [10.18653/v1/2026.findings-eacl.296](https://doi.org/10.18653/v1/2026.findings-eacl.296)
- Original Publication URL: [publisher record](https://aclanthology.org/2026.findings-eacl.296/); [original PDF](https://aclanthology.org/2026.findings-eacl.296.pdf).
- Local Document Path: None; original publisher PDF inspected online.
- Access Status: FULL_TEXT. Relevant methods, results, tables, limitations and appendices inspected. PDF page 1 corresponds to printed p. 5603; PDF locators below are one-based.
- Rights/access check: [ACL copyright policy](https://aclanthology.org/faq/copyright/) identifies post-2016 ACL materials as CC BY 4.0. No AI-processing prohibition or access-control barrier was observed. This summary paraphrases with attribution.
- Version: Initial extraction, 2026-11-13; independent verification pending.

## 2. Research Overview

FactSelfCheck represents generated text as head-relation-tail triples and compares each extracted fact with additional model responses, either through their knowledge graphs or their text (C001). Its detection pipeline does not consult an external factual reference, whereas evaluation and correction judging use Wikipedia references (C004, C008). The study compares sentence-level and fact-level detection and explores whether granular error indications improve correction (C005-C009). Results depend on dataset, metric, and evaluation granularity rather than establishing universal superiority.

## 3. Research Questions

The paper's objectives are to construct a black-box fact-level detector, test how its aggregated sentence scores compare with sentence-level methods, and assess the usefulness of fact-level error indications for correction (C001, C005-C009). These are methodological objectives rather than a formal universal hypothesis that consistency proves truth. The sample-size experiment examines whether additional samples improve detection on both datasets (C012).

## 4. Methodology

- **Representation and scoring:** Extract entities, relations and triples from the response; assess support in sampled knowledge graphs or sampled text; aggregate fact scores using mean or max when sentence scores are needed (C001).
- **Data:** WikiBio contains 238 passages and 1,908 sentences; FavaMultiSamples contains 460 passages and 5,660 sentences. The latter adds 20 temperature-1.0 samples per original passage and substitutes a newer GPT-3.5 version when the original version is unavailable (C002).
- **Models:** Llama-3.1-70B-Instruct performs the detection pipeline and LLM-requiring baselines; GPT-4o performs fact annotation, correction and correction judging. Pipeline calls use temperature 0.0 except correction at 0.5 (C003, C008).
- **Labels and metrics:** Sentence labels are human-derived, whereas WikiBio's 5,488 fact labels are GPT-4o judgments against biographies. Detection is measured with AUC-PR; the sentence-level comparator is adapted to fact-level scoring by averaging scores of sentences containing a fact (C002, C004).
- **Correction:** The WikiBio experiment compares baseline revision with sentence-indicated and fact-indicated revision. It selects thresholds by highest F1 on that dataset, a material qualification to the general test-only-data warning (C008).
- **Implementation uncertainty:** Section 3.4's valid-response scoring and Section 4.3's yes/no parsing sentence conflict; this summary does not silently infer the actual code behavior (C003).

## 5. Key Findings

1. WikiBio sentence-level hallucination AUC-PR is 92.45 for FSC-Text/max, versus 93.60 for SelfCheckGPT Prompt; its factuality AUC-PR is also lower, 65.55 versus 74.30 (C005).
2. On FavaMultiSamples, frequency-based FSC-KG/max exceeds Prompt in hallucination AUC-PR, 48.52 versus 46.91, but has lower factuality and average AUC-PR (C006).
3. With GPT-4o-labeled WikiBio facts, FSC-Text obtains 93.41 AUC-PR versus 86.18 for the adapted sentence-level Prompt comparator (C007). The comparison changes the granularity the comparator was designed for (C004, C007).
4. The correction table reports factual-sentence proportions of 0.23 for baseline, 0.25 for sentence guidance, and 0.31 for fact guidance. Its stated 35.5% and 10.6% gains are relative changes, not percentage-point gains, and remain qualified by same-dataset threshold selection and automated evaluation (C008-C009).
5. Fact extraction leaves some sentences with no facts; these receive score 0.5. Empty-fact rates differ between datasets, and the number of LLM calls depends on sentence, sample and fact counts (C003, C011).
6. The reported sample-count trends differ across datasets; the authors' explanation in terms of calibration is interpretive rather than a universal calibration guarantee established by the plotted AUC-PR curves (C012).

## 6. Evidence Table

| Claim ID | Claim | Source Location | Evidence Type | Qualifications | Verification Status |
| --- | --- | --- | --- | --- | --- |
| C001 | FactSelfCheck extracts head-relation-tail triples using entity, relation and fact prompts. Its KG variants score sample consistency by exact occurrence frequency or LLM support judgments; its Text variant judges support directly in sampled text. Sentence scores aggregate fact scores by mean or max. | Printed pp. 5606-5607, Sections 3.1-3.5 and Eqs. 1-11 (PDF pp. 4-5) | Method design | Detection is black-box and uses no external factual reference or task-specific training data, but relies on pretrained LLMs and multiple generated samples. A consistency score is not independently sourced truth. | PENDING_VERIFICATION |
| C002 | Table 5 gives WikiBio 238 passages/1,908 sentences/1,392 hallucinated sentences and FavaMultiSamples 460/5,660/1,228. FavaMultiSamples adds 20 temperature-1.0 samples per FAVA passage; GPT-3.5-turbo-1106 replaces unavailable original GPT-3.5-turbo-0301, alongside Llama2-Chat-70B. Both evaluation datasets have only test data. | Printed p. 5608, Section 4.1 (PDF p. 6); p. 5615, Appendices A-B and Table 5 (PDF p. 13) | Dataset and experimental design | Sentence labels are human-derived; WikiBio minor/major errors are merged. Replacement sampling model is not identical to the original GPT generator. The paper warns against tuning thresholds on these test-only datasets; see C008 for the correction experiment's actual selection. | PENDING_VERIFICATION |
| C003 | Llama-3.1-70B-Instruct is used for detection and LLM-requiring baselines; GPT-4o handles fact annotation and correction. Calls use temperature 0.0 except correction at 0.5. Sentences with no extracted facts receive score 0.5. Section 3.4 excludes invalid judgments from averaging, but Section 4.3 literally says responses are excluded if either yes or no is detected. | Printed p. 5607, Section 3.4/Eqs. 8-10 (PDF p. 5); p. 5609, Section 4.3 (PDF p. 7) | Implementation and source-text ambiguity | The yes/no parsing sentence conflicts with the valid-answer equations. Actual implementation behavior cannot be resolved from these passages alone; do not silently repair the wording or claim code inspection. Dataset sampling temperature in C002 is a separate stage. | PENDING_VERIFICATION |
| C004 | WikiBio fact evaluation uses 5,488 binary fact labels generated by GPT-4o with external Wikipedia biographies. AUC-PR measures detection; SelfCheckGPT Prompt is adapted to facts by averaging scores of sentences containing each fact. | Printed p. 5608, Section 4.1 fact-level evaluation (PDF p. 6); p. 5609, Sections 4.4-4.5 (PDF p. 7) | Annotation and evaluation design | These fact labels are model judgments, not human fact-level gold annotations. Reference access is in evaluation, not the detector. Conversion from sentence to fact granularity affects comparator fairness. | PENDING_VERIFICATION |
| C005 | WikiBio sentence-level hallucination AUC-PR is 92.45 for FSC-Text/max, 91.82 for LLM-based FSC-KG/max, 93.60 for SelfCheckGPT Prompt and 92.50 for SelfCheckGPT NLI. Table 6 factuality AUC-PR is 65.55 for FSC-Text/max versus 74.30 for Prompt. | Printed p. 5610, Table 1 (PDF p. 8); p. 5616, Table 6 (PDF p. 14); pp. 5610-5611, Section 5.1 | Experimental result | Displayed 0-100 AUC-PR scale, not classification accuracy. Prompt was reproduced with Llama-3.1-70B-Instruct, not the original GPT-3.5 evaluator; neither higher granularity nor competitiveness implies superiority on every metric. | PENDING_VERIFICATION |
| C006 | On FavaMultiSamples, frequency-based FSC-KG/max has hallucination AUC-PR 48.52 versus Prompt 46.91; FSC-Text/max gives 42.80. Table 7 gives the frequency-based variant factuality/average AUC-PR 80.21/64.36 versus Prompt 88.39/67.65. | Printed p. 5610, Table 2 (PDF p. 8); p. 5617, Table 7 (PDF p. 15) | Experimental result | The frequency-based variant leads the displayed hallucination metric but not factuality or average AUC-PR. Dataset label balance differs substantially from WikiBio (C002); do not interpret cross-dataset AUC-PR differences as an isolated causal effect. | PENDING_VERIFICATION |
| C007 | On WikiBio fact-level evaluation, Table 3 reports AUC-PR 93.41 for FSC-Text, 92.25 for LLM-based FSC-KG, 87.99 for frequency-based FSC-KG and 86.18 for adapted SelfCheckGPT Prompt. | Printed p. 5611, Section 5.2 and Table 3 (PDF p. 9) | Experimental result | Uses GPT-4o fact labels and the comparator conversion in C004. The authors acknowledge that comparing methods across their native granularity is not fully appropriate; no statistical-significance claim is extracted. | PENDING_VERIFICATION |
| C008 | Correction is tested only on WikiBio with GPT-4o as both corrector and judge. The corrector receives the original prompt/response plus either no error list, a sentence error list or a fact error list, without the external biography; the judge receives that biography. Error lists use thresholds chosen for highest F1 on the dataset: 0.3 for FSC-Text and 0.75 for SelfCheckGPT Prompt. | Printed p. 5609, Sections 4.3 and 4.6 (PDF p. 7) | Correction experiment design | This is same-dataset threshold selection despite Section 4.1's warning about test-only data (C002), so the correction result is not demonstrated held-out threshold generalization. Correction and evaluation use the same model family and automated judgments; documentary grounding belongs to the judge, not the corrector. | PENDING_VERIFICATION |
| C009 | Table 4 reports factual/nonfactual/refused proportions of 0.23/0.74/0.04 for baseline correction, 0.25/0.70/0.05 with sentence guidance and 0.31/0.64/0.05 with fact guidance. Reported relative factual-content increases are 10.6% and 35.5%, respectively; reported nonfactual reductions are 4.8% and 12.5%. | Printed p. 5611, Section 5.3 and Table 4 (PDF p. 9) | Experimental result | These are source-reported relative changes, not percentage points. Rounded displayed proportions do not exactly reproduce the percentages or always sum to 1; retain the reported precision rather than invent unrounded counts. Apply all C008 evaluation qualifications; residual nonfactual content remains substantial. | PENDING_VERIFICATION |
| C010 | Authors identify limited suitable datasets/native fact-level annotations, greater computational complexity from multiple LLM stages, and potential extraction failure for short or uninformative sentences. Prompt engineering was empirical and not optimized for token usage; shorter/combined prompts and improved datasets are future work. | Printed p. 5612, Limitations (PDF p. 10) | Author-reported limitations and future work | The annotation limitation must be read with the automatically labeled fact evaluation in C004, not as absence of any fact-level experiment. Proposed efficiency improvements are not established outcomes. | PENDING_VERIFICATION |
| C011 | Table 11 reports zero extracted facts for 22 WikiBio sentences (1.15%) and 344 FavaMultiSamples sentences (6.08%). Table 12 counts LLM calls as 2+U+S for frequency KG, 2+U+S+K*S for LLM KG, 2+U+K*S for FSC-Text and U*S for SelfCheckGPT Prompt, where U, S and K denote numbers of sentences, samples and extracted passage facts. | Printed p. 5618, Appendix C.4 (PDF p. 16); p. 5620, Tables 11-12 (PDF p. 18) | Extraction statistics and computational accounting | Counts of calls are not wall-clock time, token consumption, or monetary cost. The default score for empty extraction is C003. Formula variables are counts, not evidence of equal cost per call across methods. | PENDING_VERIFICATION |
| C012 | In the 1-to-20-sample ablation, the authors describe WikiBio performance improving most up to about five samples and then flattening, whereas FavaMultiSamples hallucination AUC-PR decreases with more samples. They interpret the latter in terms of changing score calibration and dataset characteristics. | Printed pp. 5616-5617, Appendix C.3 (PDF pp. 14-15); p. 5619, Figs. 4-5 (PDF p. 17) | Qualitative ablation trend and author interpretation | No numerical graph heights are estimated. AUC-PR trends alone do not establish the authors' stronger universal-calibration wording; the calibration explanation is retained as interpretation, not a demonstrated general law. | PENDING_VERIFICATION |

## 7. Author Conclusions

The authors conclude that fact-level detection offers finer error information while remaining competitive with sentence-based alternatives, and that supplying fact-level error indications improves correction in their experiment (C005-C009). The direct results are more qualified than universal method superiority: preferred variants and metric rankings differ by dataset, and the correction experiment has the selection/evaluator conditions in C008. Their future efficiency and dataset proposals are not demonstrated results (C010).

## 8. Research Limitations

**AUTHOR_REPORTED_LIMITATIONS:** Lack of suitable native fact-annotated long passages, computational burden, and extraction failure for short/uninformative sentences; empirical prompt design leaves efficiency improvement open (C010). Cross-granularity comparisons are explicitly qualified (C007).

**ADDITIONAL_OBSERVATIONS:** Same-test-set threshold selection limits the strength of the correction comparison (C002, C008). Automated fact labels and judging create evaluator dependencies (C004, C008). Consistency-based detection should not be treated as documentary verification (C001). Distinct hallucination/factuality rankings and class balances require metric-specific interpretation (C002, C005-C006). The parsing inconsistency in C003 remains unresolved. These are source-grounded assessment cautions, not independent experimental findings.

## 9. Relevance to Assignment

This paper provides a fact-level consistency-based approach and a correction experiment for the assignment's comparison of hallucination detection and reduction (C001, C007-C009). It also helps distinguish model agreement from external evidence used only for evaluation (C004, C008). The present summary does not select a thesis or synthesize findings across papers.

## 10. Questions and Uncertainties

- Resolve the yes/no parsing contradiction before asserting implementation fidelity beyond the published equations (C003); no code audit was performed.
- Correction thresholds are selected on the evaluation dataset (C008). Performance using independently fixed thresholds is not established by the reported comparison.
- Preserve the reported relative changes and rounded proportions without reconstructing unavailable precision (C009).
- The source's calibration interpretation is not independently demonstrated by the AUC-PR trends alone (C012).
- Publisher metadata includes the middle name Jan for Kajdanowicz, whereas the PDF byline does not; retain this discrepancy in later citation preparation.
- Screenshot requests produced no inspectable images. Original PDF text gave readable table rows, equations and captions; no precise plotted values were inferred.

## 11. Summary Status

COMPLETE_FOR_INDEPENDENT_VERIFICATION. Twelve claims C001-C012, all PENDING_VERIFICATION; six key findings. Original full text was accessible and no licensing/access blocker was identified. Only this assigned summary was written. A separate verifier must inspect each claim and all relevant qualifications against the original publication before evidence advances.
