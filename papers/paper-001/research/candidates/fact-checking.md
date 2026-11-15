# Research Candidates: Evidence-Based Fact Checking

## Scope and assignment

Phase 1 discovery and bibliographic screening only for paper-001. Read AGENTS.md and assignment.md. The assignment requires a 1,200-word scholarly review, APA 7, at least three relevant scholarly publications, peer-reviewed sources, comparison of verification approaches, and attention to limitations and opposing findings. No publication-date cutoff is specified. This report addresses evidence-based factuality evaluation and retrieval-supported correction. It does not extract evidence claims, verify findings, summarize articles in detail, or select a thesis.

Report owner: researcher / fact_checking. Report slug: fact-checking. All permanent source IDs remain UNASSIGNED for coordinator allocation. Searches and access checks took place on 2026-11-10. First retained explicit clock observation: 19:00:44 UTC; a later pre-write observation: 19:01:14 UTC. These observations do not establish the full task runtime.

## Search strategy and sources searched

Queries executed through web search:

- `site:aclanthology.org FActScore Fine-grained Atomic Evaluation Factual Precision Long Form Text Generation`
- `site:aclanthology.org retrieval augmented generation hallucination RARR research revising attribution`
- `site:aclanthology.org/2023 FActScore Min Krishna Lyu`
- `site:aclanthology.org RARR Researching and Revising What Language Models Say Using Language Models`
- `site:aclanthology.org RAGTruth A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models`

Primary records consulted: ACL Anthology publisher pages and their linked proceedings PDFs. Selection favored direct relevance, established peer-reviewed venues, public full text, and complementary evaluation/correction perspectives. This is a targeted search, not a systematic or exhaustive literature review. Search-result occurrences alone are not counted as catalogued candidates. The four records below are distinct by DOI; alternative PDF paths were collapsed into their canonical publication rather than counted again.

## Candidate publications

### CAND-fact-checking-001 — FActScore

- Existing Source ID: UNASSIGNED
- Title: FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation
- Authors: Sewon Min; Kalpesh Krishna; Xinxi Lyu; Mike Lewis; Wen-tau Yih; Pang Wei Koh; Mohit Iyyer; Luke Zettlemoyer; Hannaneh Hajishirzi.
- Publication year: 2023
- Journal/conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 12076–12100. Association for Computational Linguistics.
- DOI: [10.18653/v1/2023.emnlp-main.741](https://doi.org/10.18653/v1/2023.emnlp-main.741)
- Publisher URL: [ACL record](https://aclanthology.org/2023.emnlp-main.741/)
- Open-access URL: [Publisher PDF](https://aclanthology.org/2023.emnlp-main.741.pdf)
- Publication type / peer-reviewed status: Original conference research; CONFIRMED (EMNLP main proceedings).
- Access status: FULL_TEXT; publisher PDF opened successfully, 25 pages. No local download created.
- Relevance: High. The suggested publication directly addresses retrieval-supported factual precision evaluation. It is suitable for comparison with consistency-based detection.
- Potential contribution: Atomic-fact evaluation and external evidence as an alternative to model agreement.
- Limitations of screening: Bibliographic and access screening only; empirical performance is not independently verified. Generalizability beyond the studied tasks requires later inspection.
- Bibliographic verification: Title, year, venue, pages, DOI and author order checked against publisher record and PDF first page. Publisher metadata abbreviates Pang Wei Koh as Pang Koh; use the PDF's fuller author form.

### CAND-fact-checking-002 — RARR

- Existing Source ID: UNASSIGNED
- Title: RARR: Researching and Revising What Language Models Say, Using Language Models
- Authors: Luyu Gao; Zhuyun Dai; Panupong Pasupat; Anthony Chen; Arun Tejasvi Chaganty; Yicheng Fan; Vincent Y. Zhao; Ni Lao; Hongrae Lee; Da-Cheng Juan; Kelvin Guu.
- Publication year: 2023
- Journal/conference: Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 16477–16508. Association for Computational Linguistics.
- DOI: [10.18653/v1/2023.acl-long.910](https://doi.org/10.18653/v1/2023.acl-long.910)
- Publisher URL: [ACL record](https://aclanthology.org/2023.acl-long.910/)
- Open-access URL: [Publisher PDF](https://aclanthology.org/2023.acl-long.910.pdf)
- Publication type / peer-reviewed status: Original conference research; CONFIRMED (ACL main proceedings).
- Access status: FULL_TEXT; publisher PDF opened successfully, 32 pages. No local download created.
- Relevance: High. This work addresses external attribution and post-generation revision. It extends the inventory from detection/evaluation to correction.
- Potential contribution: Retrieval-backed editing and the relationship between attribution and preservation of generated text.
- Limitations of screening: No performance claims verified; source reliability and the distinction between attribution and truth need later examination.
- Bibliographic verification: Title, year, venue, pages, DOI and author order checked against publisher record and PDF first page. Publisher listing omits the middle initial in Vincent Y. Zhao; the PDF supplies it.

### CAND-fact-checking-003 — VeriScore

- Existing Source ID: UNASSIGNED
- Title: VeriScore: Evaluating the factuality of verifiable claims in long-form text generation
- Authors: Yixiao Song; Yekyung Kim; Mohit Iyyer.
- Publication year: 2024
- Journal/conference: Findings of the Association for Computational Linguistics: EMNLP 2024, pp. 9447–9474. Association for Computational Linguistics.
- DOI: [10.18653/v1/2024.findings-emnlp.552](https://doi.org/10.18653/v1/2024.findings-emnlp.552)
- Publisher URL: [ACL record](https://aclanthology.org/2024.findings-emnlp.552/)
- Open-access URL: [Publisher PDF](https://aclanthology.org/2024.findings-emnlp.552.pdf)
- Publication type / peer-reviewed status: Original research in peer-reviewed Findings; CONFIRMED.
- Access status: FULL_TEXT; publisher PDF opened successfully, 28 pages. No local download created.
- Relevance: High. Its stated scope addresses verifiable versus unverifiable content in long-form generation. It offers a focused candidate for examining limitations of atomic-fact scoring.
- Potential contribution: Evaluation assumptions and task-dependent factuality measurement.
- Limitations of screening: Abstract and access screening do not establish the validity of the paper's criticisms or results; those remain for independent extraction and verification.
- Bibliographic verification: Authors, title, year, venue, pages and DOI confirmed from publisher page, with author/title/venue/page-range checks against the PDF first page. No material discrepancy observed.

### CAND-fact-checking-004 — RAGTruth

- Existing Source ID: UNASSIGNED
- Title: RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models
- Authors: Cheng Niu; Yuanhao Wu; Juno Zhu; Siliang Xu; Kashun Shum; Randy Zhong; Juntong Song; Tong Zhang.
- Publication year: 2024
- Journal/conference: Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 10862–10878. Association for Computational Linguistics.
- DOI: [10.18653/v1/2024.acl-long.585](https://doi.org/10.18653/v1/2024.acl-long.585)
- Publisher URL: [ACL record](https://aclanthology.org/2024.acl-long.585/)
- Open-access URL: [Publisher PDF](https://aclanthology.org/2024.acl-long.585.pdf)
- Publication type / peer-reviewed status: Original conference research/dataset; CONFIRMED (ACL main proceedings).
- Access status: FULL_TEXT; publisher PDF opened successfully, 17 pages. No local download created.
- Relevance: High. The corpus specifically concerns hallucination in retrieval-augmented generation. It supplies a candidate perspective on limitations that can persist with retrieved context.
- Potential contribution: Benchmarking detection against source-conditioned annotations.
- Limitations of screening: Annotation quality, task coverage and generalization have not been independently evaluated.
- Bibliographic verification: Title, author order, year, venue, pages and DOI checked against publisher metadata and PDF first page. Publisher displays KaShun Shum; PDF displays Kashun Shum (capitalization variant only).

## Ranked recommendations

1. CAND-fact-checking-001: prioritize as the independently screened suggested source for factuality evaluation.
2. CAND-fact-checking-002: prioritize as an evidence-backed correction approach.
3. CAND-fact-checking-003: prioritize for limitations and complementary evaluation design.
4. CAND-fact-checking-004: retain as a relevant benchmark and retrieval-limitation source.

All four are recommended for coordinator screening, not automatically accepted or citation-ready. The 1,200-word limit may favor a smaller final reading subset after cross-topic integration.

## Access limitations and next-stage questions

- All four public publisher PDFs opened successfully without authentication or paywall circumvention. FULL_TEXT denotes accessibility, not complete reading or verified findings.
- DOI strings were verified in the publisher's metadata; a separate Crossref API or DOI-resolution audit was not performed.
- Peer-review classification follows the identified archival main-conference/Findings venue, not inspection of individual reviewer reports.
- No local copies were saved. URLs may change; later agents must independently reopen sources and respect applicable rights.
- Author-name variants are disclosed above; preserve the PDF forms when preparing APA references rather than silently copying abbreviated publisher metadata.
- Later research may examine source reliability, factuality versus faithfulness, task generalizability, and claim decomposition. These are follow-up questions, not verified conclusions.
- Newer search hits were visible, but this bounded four-candidate selection emphasizes direct coverage and established relevant publications; it is not a claim to cover all literature through 2026.

## Handoff

Catalogued candidates: 4. Distinct publications within this report: 4. Recommended: 4. FULL_TEXT accessible: 4. Manual-access requests: 0. Bibliographic/name variants: 3 as disclosed. Permanent IDs assigned: 0. Evidence claims extracted or verified: 0. No downstream workflow phase executed. Coordinator must deduplicate across other reports and determine acceptance and permanent IDs.
