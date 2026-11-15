# Academic Article Summary

## 1. Bibliographic Information

- Source ID: SRC-003
- Title: FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation
- Authors: Sewon Min; Kalpesh Krishna; Xinxi Lyu; Mike Lewis; Wen-tau Yih; Pang Wei Koh; Mohit Iyyer; Luke Zettlemoyer; Hannaneh Hajishirzi. PDF byline retained; publisher metadata abbreviates Pang Wei Koh as Pang Koh.
- Publication Year: 2023
- Journal or Conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 12076-12100, Association for Computational Linguistics.
- DOI: [10.18653/v1/2023.emnlp-main.741](https://doi.org/10.18653/v1/2023.emnlp-main.741)
- Original Publication URL: [publisher record](https://aclanthology.org/2023.emnlp-main.741/); [original PDF](https://aclanthology.org/2023.emnlp-main.741.pdf)
- Local Document Path: Not downloaded; original publisher PDF accessed directly.
- Access Status: FULL_TEXT. Original methods, results, limitations, and relevant appendices inspected on 2026-11-12; no authentication or access bypass used.
- Rights: ACL's [copyright policy](https://aclanthology.org/faq/copyright/) identifies ACL materials published from 2016 onward as CC BY 4.0. This is an attributed paraphrase, not a reproduction of the paper. No AI-processing prohibition was encountered in the consulted policy.
- Locator convention: PDF page numbers are one-based; printed page 12076 is PDF page 1.
- Summary version: initial extraction, awaiting independent verification.

## 2. Research Overview

The paper defines factual precision through atomic claims supported by a specified knowledge source, then evaluates an automated retrieval-and-language-model estimator against human judgments (C001-C006). Its principal evaluation concerns biographies and English Wikipedia; a small supplementary NLP-paper experiment explores broader application (C002, C012). It also separates aggregate score estimation from correctness of individual verification decisions (C007).

## 3. Research Questions

The operational questions are paraphrased from Sections 3-4: how can factual precision of long responses be measured at a finer level than whole sentences, and can that measure be estimated automatically? C001 defines the target; C002-C007 describe its evaluation. Appendix C asks whether verification labels can assist correction, under a gold-label experimental assumption (C013). These are extracted research objectives, not a formally numbered hypothesis list.

## 4. Methodology

- **Human reference evaluation:** 183 people with Wikipedia pages were sampled from Wikidata. InstructGPT, ChatGPT, and PerplexityAI generated biographies. Human annotators revised InstructGPT-produced atomic decompositions, and another annotation stage labeled relevant facts against English Wikipedia; irrelevant facts and abstentions were separately identified (C002).
- **Estimator:** atomic decomposition precedes fact validation. Variants include no-context prompting, retrieved-context prompting, nonparametric probability, and a conjunction ensemble. Main evaluators are instruction-tuned LLaMA 7B and ChatGPT; the retrieval implementation uses GTR and five passages from the topic entity's page (C004).
- **Evaluation:** aggregate error rate measures the difference between estimated and human FActScore, whereas supplementary micro-F1 concerns individual fact classifications. These are different objectives (C005-C007).
- **Additional application:** the later case study evaluates 500 biography prompts across 12 LMs and a human-text comparator, for 13 subjects. This is separate from the 183-entity human reference evaluation (C011).
- **Editing experiment:** ChatGPT editors are evaluated with gold verification labels, retrieved context, and/or atomic-fact labels; it is not an end-to-end test using imperfect automatic verification (C013).

## 5. Key Findings

1. Human-reference FActScores were 42.5% for InstructGPT, 58.3% for ChatGPT, and 71.5% for PerplexityAI on this biography evaluation, with different response rates (C003).
2. Estimator quality depends on the evaluated generator. The same LLaMA-plus-NP ensemble has aggregate errors of 1.4, 0.4, and 9.9 percentage points across the three generators; the best result for PerplexityAI instead comes from ChatGPT with retrieval (C005-C006).
3. Retrieval-supported classification outperforms the tested self-check baseline in Table 9, but that comparison concerns this implementation and dataset (C007).
4. Source coverage remains a limitation: three of 30 sampled Wikipedia-unsupported claims about rare people were supported elsewhere on the web (C008).
5. Among 30 errors from the ChatGPT retrieval evaluator, missing direct evidence in retrieved passages and distraction by other passages were frequent categories (C009).
6. The small NLP-domain extension had a larger aggregate error than the headline sub-2-point examples, and should not establish general robustness (C012).
7. In preliminary editing, retrieval and gold atomic-fact labels improved selected editing metrics for ChatGPT-generated inputs, subject to the gold-label assumption (C013).

## 6. Evidence Table

| Claim ID | Claim | Source Location | Evidence Type | Qualifications | Verification Status |
| --- | --- | --- | --- | --- | --- |
| C001 | FActScore averages, over non-abstaining responses, the fraction of atomic facts supported by a given knowledge source. The definition assumes clear support judgments, equally weighted facts, and nonconflicting/nonoverlapping source information; it measures precision rather than recall. | Printed p. 12078 (PDF p. 3), Section 3.1, definition and assumptions | Metric definition | Support is relative to the chosen source, not an assertion of universal truth. Abstentions are excluded from the conditional average. | PENDING_VERIFICATION |
| C002 | The human evaluation sampled 183 Wikidata people with Wikipedia pages and obtained biographies from InstructGPT, ChatGPT and PerplexityAI; annotators revised machine-proposed atomic facts, then labeled them Irrelevant, Supported or Not-supported using English Wikipedia. Two annotators covered 10% of data; reported agreement was 96%, 90% and 88% for the three generators respectively. | Printed p. 12079 (PDF p. 4), Sections 3.2-3.3 and continuation from p. 12078 | Study design and annotation | This is a biography-specific sample; agreement is not proof of reference-label infallibility. | PENDING_VERIFICATION |
| C003 | Table 1 reports human-reference FActScores of 42.5%, 58.3% and 71.5% for InstructGPT, ChatGPT and PerplexityAI respectively; their response rates are 99.5%, 85.8% and 90.7%. | Printed p. 12079 (PDF p. 4), Table 1 and Section 3.4 | Empirical result | These are study-era systems and source-conditioned biography scores, not current general model accuracy. Different abstention rates affect interpretation. | PENDING_VERIFICATION |
| C004 | The estimator decomposes text into atomic facts, then compares no-context LM, Retrieve-to-LM, nonparametric probability (NP), and an ensemble requiring both retrieval-LM and NP support. Main evaluators are instruction-tuned LLaMA 7B and ChatGPT; GTR retrieves five passages restricted to the topic entity's page from the English Wikipedia snapshot dated 04/01/2023, with passages up to 256 tokens. | Printed pp. 12081-12082 (PDF pp. 6-7), Section 4.1; p. 12092 (PDF p. 17), Appendix B.1 | Method | Date is retained exactly as printed to avoid silently changing date convention. No-context is a comparison baseline; NP and ensemble rules differ from ordinary prompting. | PENDING_VERIFICATION |
| C005 | Error Rate in Section 4.2 is the difference between the estimated aggregate FActScore and the human-reference score. Table 3 gives Inst-LLaMA Retrieve-to-LM+NP errors of 1.4, 0.4 and 9.9 percentage points for InstructGPT, ChatGPT and PerplexityAI outputs respectively. | Printed p. 12082 (PDF p. 7), Section 4.2 and Table 3 | Evaluation definition and empirical result | These are aggregate score errors, not percentages of individual facts misclassified. The sub-2-point result is not universal across generators or estimator variants. | PENDING_VERIFICATION |
| C006 | For PerplexityAI outputs, ChatGPT Retrieve-to-LM has 0.8 percentage-point aggregate error; for InstructGPT and ChatGPT outputs its errors are 5.1 and 6.8. The authors recommend trying both leading estimator variants and reporting their correlation because the best choice depends on the generator. | Printed p. 12082 (PDF p. 7), Table 3 and Section 4.2 | Empirical result and author recommendation | A recommendation for evaluator comparison, not a guarantee of accuracy on unseen domains. | PENDING_VERIFICATION |
| C007 | Table 9, using Inst-LLaMA 7B, reports self-check micro-F1 of 66.0 and 48.4 on InstructGPT and ChatGPT outputs, versus 78.7 and 61.9 for Retrieve-to-LM. The paper distinguishes aggregate score error from individual classification performance, which can favor different evaluators. | Printed pp. 12092-12093 (PDF pp. 17-18), Appendix B.2, Tables 9-10; p. 12082, Section 4.2 | Comparative empirical result | This is the paper's self-check implementation and benchmark, not every consistency method; self-check is unavailable for the paper's semi-deterministic PerplexityAI setting. Micro-F1 is not aggregate ER. | PENDING_VERIFICATION |
| C008 | In a sample of 30 ChatGPT facts labeled unsupported by Wikipedia concerning rare or very rare people, three (10%) were supported elsewhere on the web. | Printed pp. 12091-12092 (PDF pp. 16-17), Appendix A.5, Coverage of English Wikipedia | Small-sample source-coverage analysis | Sample is narrow and selected from unsupported facts; this is not an overall false-negative estimate for every fact or knowledge source. | PENDING_VERIFICATION |
| C009 | Table 13 categorizes 30 mistakes by ChatGPT Retrieve-to-LM: 70% lacked direct evidence in retrieved passages and 17% involved distraction by other passages. | Printed p. 12094 (PDF p. 19), Appendix B.3 and Table 13 | Qualitative error analysis | Percentages are within a 30-error sample, not all verification decisions; lack of retrieved evidence does not itself prove a fact false. | PENDING_VERIFICATION |
| C010 | The authors identify limitations for nuanced/debatable facts and conflicting knowledge sources; the estimator is imperfect on individual judgments. FActScore does not penalize frequent abstention or fewer facts, and they recommend reporting abstention rate and average fact count alongside it. | Printed pp. 12084-12085 (PDF pp. 9-10), Limitations; p. 12078, Section 3.1 | Author-reported limitations | These limitations restrict interpretation of a high score; they do not establish failure of every retrieval-based method. | PENDING_VERIFICATION |
| C011 | Section 4.3 and Tables 4-5 describe 500 new biography entities evaluated for 12 LMs plus a human-text comparator, totaling 13 subjects; Figure 3 reports Pearson correlation 0.99 between scores from the two leading retrieval-based estimators. | Printed pp. 12083-12084 (PDF pp. 8-9), Section 4.3, Tables 4-5, Figure 3 | Application design and empirical result | Human text is not a thirteenth LM. This case study is distinct from the human-labeled 183-entity evaluation; correlation between estimators is not independent truth verification. | PENDING_VERIFICATION |
| C012 | Appendix B.5's proof of concept used 10 prompts about NLP papers, ChatGPT responses, and ACL Anthology as the knowledge source. Human and model FActScores were 66.20 and 73.61, giving ER 7.41; the authors call for larger-scale generalizability research. | Printed pp. 12094-12095 (PDF pp. 19-20), Appendix B.5 | Small-scale domain extension | Ten prompts are insufficient to establish broad domain generalization; human labels were supplied by authors. | PENDING_VERIFICATION |
| C013 | In Appendix C's gold-verification-label editing setup, ChatGPT-input EditCorr scores were 6.8 for no-context editing, 16.8 with retrieval and 28.3 with retrieval plus atomic-fact labels; corresponding SimAl values were 4.0, 9.5 and 19.3. | Printed pp. 12095-12097 (PDF pp. 20-22), Appendix C introduction, C.2-C.3 and Table 14 | Preliminary correction experiment | Gold verification labels isolate editing from estimator errors. EditCorr (called ErrCorr in the results table) is token-level F1 on added material; SimAl is semantic alignment with gold edits, not a direct factual-accuracy percentage. | PENDING_VERIFICATION |

## 7. Author Conclusions

The authors present atomic, source-relative scoring as a practical basis for human and automated evaluation (C001-C006). Their recommendation to compare estimator variants recognizes generator-dependent performance (C006-C007). Broader-domain evaluation and correction remain qualified extensions rather than universal demonstrations (C010, C012-C013).

## 8. Research Limitations

**AUTHOR_REPORTED_LIMITATIONS:** source-relative support and precision-only evaluation (C001, C010); reference-source coverage and annotation fallibility (C002, C008); imperfect individual judgments and retrieved-evidence failure modes (C007, C009); limited evidence for domain transfer (C012); preliminary correction relies on gold verification labels (C013).

**ADDITIONAL_OBSERVATIONS:** As an interpretation of C005-C007, small aggregate score error should not be paraphrased as near-perfect claim verification. As an interpretation of C011, agreement between two automatic estimators cannot alone establish their validity. These are summarizer cautions, not new empirical findings.

## 9. Relevance to Assignment

This source directly addresses evidence-based fact-checking through C001-C009 and supplies an explicitly qualified correction experiment in C013. C007 offers a source-specific comparison to self-checking; C008-C010 and C012 prevent treating external retrieval or high aggregate agreement as guarantees. No cross-paper synthesis or thesis is selected here.

## 10. Questions and Uncertainties

- The verifier should preserve the distinction between aggregate ER and individual fact-level errors (C005-C007).
- The abstract's shorthand about 13 LMs should not replace the detailed 12-LM-plus-human account in C011. No cost-savings claim is extracted because the abstract/body/conclusion should first be reconciled if that topic becomes necessary.
- The date string in C004 is retained verbatim as a date format, without assuming a locale convention.
- Future source use should distinguish source-unsupported claims from facts disproven independently (C001, C008).

## 11. Summary Status

COMPLETE for the assigned focused extraction; independent verification pending. Seven key findings and 13 evidence records (C001-C013), all PENDING_VERIFICATION. Full text accessible; no licensing or access blocker encountered. No original PDFs, other summaries, verification reports, matrix, log or metrics were modified. The coordinator should assign a separate verifier to inspect the original publication and every claim.
