# Research candidates: Self-consistency and its limitations

## 1. Scope and assignment

- Owner: researcher agent `/root/self_consistency`.
- Report slug: `self-consistency`; Phase 1 bibliographic discovery only.
- Observed research start: 2026-11-10T13:00:22-06:00 (America/Regina).
- Metadata/access checks completed: 2026-11-10T13:00:44-06:00.
- Assignment: 1,200-word APA 7 review of self-consistency, independent verification, and evidence-based fact-checking; peer-reviewed scholarly publications, at least three relevant sources, limitations and opposing findings. No publication-date cutoff specified.
- AI use is explicitly allowed for the demonstration, subject to the encompassing assignment's rules. No thesis selection, article summarization, evidence extraction, claim verification, synthesis, or drafting was performed.

## 2. Search strategy and sources

Queries submitted to web search:

1. `site.aclanthology.org SelfCheckGPT Zero Resource Black Box Hallucination Detection` (the first query contained this literal site-prefix typo; results were still returned).
2. `site:aclanthology.org self consistency hallucination detection limitations semantic entropy`

Primary records consulted: ACL Anthology publication landing pages and their publisher-hosted PDFs. Search results were used for discovery, not as final metadata evidence. The suggested SelfCheckGPT paper was evaluated for scope, publication status, identity, and accessible full text rather than accepted solely because it was suggested. Three additional papers provide an extension, an explicit limitations perspective, and a recent development. This targeted search is not a systematic or exhaustive literature review.

## 3. Candidate publications

### CAND-self-consistency-001 — SelfCheckGPT

- Existing Source ID: UNASSIGNED.
- Title: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models.
- Authors: Potsawee Manakul; Adian Liusie; Mark J. F. Gales (PDF byline). Anthology citation metadata shortens the final name to Mark Gales; preserve the PDF initials when preparing APA references.
- Publication year: 2023.
- Journal/conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 9004–9017. Association for Computational Linguistics.
- DOI: [10.18653/v1/2023.emnlp-main.557](https://doi.org/10.18653/v1/2023.emnlp-main.557).
- Publisher URL and metadata evidence: [ACL Anthology record](https://aclanthology.org/2023.emnlp-main.557/).
- Open-access URL and access evidence: [publisher PDF](https://aclanthology.org/2023.emnlp-main.557.pdf), successfully opened as a 14-page PDF; first-page bibliographic header and byline inspected.
- Publication type: Original conference research paper.
- Peer-reviewed status: CONFIRMED — published EMNLP main-proceedings paper, not merely an arXiv posting.
- Access status: FULL_TEXT; no local PDF downloaded.
- Relevance score: High.
- Research relevance: Directly addresses the assignment's consistency-based, black-box hallucination-detection topic. The publication's declared scope offers a suitable starting point for comparison with externally grounded checking.
- Potential contribution: Foundational candidate for the self-consistency approach.
- Limitations of evaluation: Full-text availability is established, but methods and results have not undergone detailed extraction or independent verification. No performance claim is approved for manuscript use.
- Bibliographic verification: Title, authors, year, venue, page range and DOI checked against publisher record; PDF confirms publication header/byline, with the name variation noted above. DOI checked as publisher-declared metadata, not independently registered through Crossref.

### CAND-self-consistency-002 — SAC³

- Existing Source ID: UNASSIGNED.
- Title: SAC³: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency.
- Authors: Jiaxin Zhang; Zhuohang Li; Kamalika Das; Bradley Malin; Sricharan Kumar.
- Publication year: 2023.
- Journal/conference: Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 15445–15458. Association for Computational Linguistics.
- DOI: [10.18653/v1/2023.findings-emnlp.1032](https://doi.org/10.18653/v1/2023.findings-emnlp.1032).
- Publisher URL and metadata evidence: [ACL Anthology record](https://aclanthology.org/2023.findings-emnlp.1032/).
- Open-access URL and access evidence: [publisher PDF](https://aclanthology.org/2023.findings-emnlp.1032.pdf), successfully opened as a 14-page PDF; publication header/byline inspected.
- Publication type: Original Findings research paper.
- Peer-reviewed status: CONFIRMED — published ACL Findings paper.
- Access status: FULL_TEXT; no local PDF downloaded.
- Relevance score: High.
- Research relevance: The abstract explicitly examines the adequacy of self-consistency checking and introduces semantic and cross-model checks. It is therefore relevant both to the consistency topic and to scrutiny of that approach's limitations.
- Potential contribution: Comparison candidate connecting self-consistency and cross-model checking.
- Limitations of evaluation: Abstract-level relevance screening and bibliographic/access inspection only; methodological strength and claimed improvements remain unverified.
- Bibliographic verification: Authors, title, year, venue, pages and DOI checked against the publisher record; PDF header/byline agree. DOI is publisher-declared, not separately Crossref-checked.

### CAND-self-consistency-003 — Too Consistent to Detect

- Existing Source ID: UNASSIGNED.
- Title: Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs.
- Authors: Hexiang Tan; Fei Sun; Sha Liu; Du Su; Qi Cao; Xin Chen; Jingang Wang; Xunliang Cai; Yuanzhuo Wang; Huawei Shen; Xueqi Cheng.
- Publication year: 2025.
- Journal/conference: Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 4755–4765. Association for Computational Linguistics.
- DOI: [10.18653/v1/2025.emnlp-main.238](https://doi.org/10.18653/v1/2025.emnlp-main.238).
- Publisher URL and metadata evidence: [ACL Anthology record](https://aclanthology.org/2025.emnlp-main.238/).
- Open-access URL and access evidence: [publisher PDF](https://aclanthology.org/2025.emnlp-main.238.pdf), successfully opened as an 11-page PDF; publication header/byline inspected.
- Publication type: Original conference research paper.
- Peer-reviewed status: CONFIRMED — published EMNLP main-proceedings paper.
- Access status: FULL_TEXT; no local PDF downloaded.
- Relevance score: High.
- Research relevance: The declared research focus is repeatedly generated incorrect answers and detection methods' limitations. It is a directly relevant counterevidence candidate for avoiding an assumption that consistency establishes truth.
- Potential contribution: Recent limitations-focused source and cross-model-verifier comparison candidate.
- Limitations of evaluation: No detector-performance claims were extracted or verified. PDF affiliation symbols show extraction artifacts, but the author list is readable and supported by the publisher metadata.
- Bibliographic verification: Title, all authors, venue, year, pages and DOI checked against the publisher record; PDF header confirms publication identity. DOI is publisher-declared, not separately Crossref-checked.

### CAND-self-consistency-004 — FactSelfCheck

- Existing Source ID: UNASSIGNED.
- Title: FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs.
- Authors: Albert Sawczyn; Jakub Binkowski; Denis Janiak; Bogdan Gabrys; Tomasz Kajdanowicz (PDF byline). Anthology metadata expands the last author's name to Tomasz Jan Kajdanowicz; retain this variation for later reference preparation.
- Publication year: 2026.
- Journal/conference: Findings of the Association for Computational Linguistics: EACL 2026, pp. 5603–5621. Association for Computational Linguistics.
- DOI: [10.18653/v1/2026.findings-eacl.296](https://doi.org/10.18653/v1/2026.findings-eacl.296).
- Publisher URL and metadata evidence: [ACL Anthology record](https://aclanthology.org/2026.findings-eacl.296/).
- Open-access URL and access evidence: [publisher PDF](https://aclanthology.org/2026.findings-eacl.296.pdf), successfully opened as a 19-page PDF; publication header/byline inspected.
- Publication type: Original Findings research paper.
- Peer-reviewed status: CONFIRMED — published ACL Findings paper.
- Access status: FULL_TEXT; no local PDF downloaded.
- Relevance score: High.
- Research relevance: Its declared fact-level sampling-based approach extends the directly relevant consistency-detection literature. It provides a current candidate for examining detection granularity and the relationship between detection and correction.
- Potential contribution: Recent extension of consistency-based detection.
- Limitations of evaluation: No numerical improvement claims were extracted or verified; full methodological comparison remains future work. Author-name variation is documented rather than silently normalized.
- Bibliographic verification: Title, author identities/order, year, venue, page range and DOI checked against publisher record and PDF header/byline. DOI is publisher-declared, not separately Crossref-checked.

## 4. Ranked recommendations and deduplication handoff

Recommend all four for coordinator screening. Priority for a short paper: (1) SelfCheckGPT as the directly relevant suggested source; (2) Too Consistent to Detect for limitations; (3) SAC³ for cross-model comparison; (4) FactSelfCheck as a recent extension. Ranking concerns coverage and relevance, not independently verified methodological superiority.

All four have different publisher DOIs and titles; no within-report duplicates remain. Search hits for SelfCheckGPT's arXiv version, mirror, GitHub repository, and duplicate PDF URLs were treated as alternate representations of the same publication, not additional candidates. Other search results were not onboarded because four directly relevant published papers already met this task's candidate scope; no claim of exhaustive screening is made. Cross-report deduplication and permanent source-ID allocation belong to the coordinator.

## 5. Access limitations and follow-up

- Four candidate records; four recommended; four FULL_TEXT; zero requiring manual access in this report.
- Full text means a publisher PDF was opened successfully, not that the complete article was read or its findings verified.
- No authentication, paywall bypass, unauthorized copy, or restricted IEEE access was used.
- Metadata name variants for candidates 001 and 004 should be preserved in the coordinator handoff. They do not indicate different publications.
- This search covers consistency-based checking. Independent verification and externally grounded fact-checking require the coordinator's other research tracks.
- Later authorized reading should examine evaluation scope, repeated-error failure modes, cross-model independence assumptions, sampling cost, and correction granularity. These are questions for extraction and verification, not findings established here.

## 6. Workflow handoff

The researcher contributed discovery, relevance screening, publisher metadata inspection, and full-text availability checks for CAND-self-consistency-001 through CAND-self-consistency-004. No permanent source IDs or global evidence claims were allocated. No shared matrix, workflow log, workflow metrics, or another agent's report was modified. The coordinator should log these actions and retain the bibliographic/name-variation limitations.
