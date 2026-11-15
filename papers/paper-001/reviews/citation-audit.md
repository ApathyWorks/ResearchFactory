# Citation and Evidence Audit: Detecting and Reducing Hallucinations in Large Language Models: A Review of Verification Techniques

## 1. Audit Scope

- Independent Phase 6 audit, completed 2026-11-13 (America/Regina). This is a fresh assessment of the original first draft, not a revision review.
- Manuscript: [drafts/draft-v1.md](../drafts/draft-v1.md), SHA-256 `5b81fb18f0936edd6a14a2195d6994c20bdc400993acb1c954c21e5f97b8c638`, independently checked. Full manuscript and all nine references inspected.
- Requirements: [assignment.md](../assignment.md), APA 7th edition; explicitly AI-generated demonstration. Read repository AGENTS.md and citation-auditor configuration. No manuscript changes or submission performed.
- Traceability inputs: [evidence-matrix.md](../evidence-matrix.md), [approved outline](../outline.md), [synthesis](../research/synthesis.md), [inventory](../research/inventory.md), and relevant entries in `summaries/SRC-001–005,007,009–011.md` and matching `reviews/verification/` reports. The matrix's draft-mapping table is empty; the mappings below were independently reconstructed from its claim ledger and the outline. All mapped ledger claims have current VERIFIED status; historical PENDING labels in summaries are not their current verification status.
- Independence: no previous/current manuscript citation audit, peer review, revision plan, drafting report, draft-evidence-map, workflow log, metrics, or review-history artifact was read. No peer conclusions were received or used. Earlier source-verification reports were used only as traceability aids.
- Direct inspection used the archival publisher PDFs below: claim-bearing methods, tables, limitations and appendices, not merely abstracts. Metadata records were separately inspected. This was not a line-by-line reading of unrelated portions of every publication or experimental replication. No graph values were estimated. Text/table extraction was legible for all audited claims; no essential original source was unavailable.
- ACL access follows its [copyright policy](https://aclanthology.org/faq/copyright/). Public publisher copies were accessed without authentication bypass; no applicable AI-processing prohibition was encountered. No unauthorized copies were used.

| Source | Original full text consulted | Principal inspected locators (printed pages) |
| --- | --- | --- |
| SRC-001 / Manakul et al. (2023) | [Publisher PDF](https://aclanthology.org/2023.emnlp-main.557.pdf) | §§4–7.3; pp. 9008–9012; Tables 1–4; Appendix C |
| SRC-002 / Dhuliawala et al. (2024) | [Publisher PDF](https://aclanthology.org/2024.findings-acl.212.pdf) | §§3–4.3; pp. 3565–3568; Tables 1–2 |
| SRC-003 / Min et al. (2023) | [Publisher PDF](https://aclanthology.org/2023.emnlp-main.741.pdf) | §3.1, §4; pp. 12078, 12084–12085; Appendix B.2, pp. 12092–12093, Table 9 |
| SRC-004 / Zhang et al. (2023) | [Publisher PDF](https://aclanthology.org/2023.findings-emnlp.1032.pdf) | §§4–6.2.2; Table 4, p. 15452; cost discussion p. 15453; Appendix C.1 |
| SRC-005 / Tan et al. (2025) | [Publisher PDF](https://aclanthology.org/2025.emnlp-main.238.pdf) | §§2.1–3.1, pp. 4756–4757; Tables 2–3 and §4, p. 4758 |
| SRC-007 / Huang et al. (2024) | [Publisher PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf) | §§2–3.2, PDF pp. 2–4; Table 3 |
| SRC-009 / Gao et al. (2023) | [Publisher PDF](https://aclanthology.org/2023.acl-long.910.pdf) | §§1–3, 5–6, 9; Table 1 p. 16482; Fig. 9 and prose p. 16485; Appendices A/C pp. 16490/16492 |
| SRC-010 / Song et al. (2024) | [Publisher PDF](https://aclanthology.org/2024.findings-emnlp.552.pdf) | §§2.2–2.3, 4.4.2, pp. 9449, 9454–9455; Appendix G p. 9463 |
| SRC-011 / Niu et al. (2024) | [Publisher PDF](https://aclanthology.org/2024.acl-long.585.pdf) | §3.1, p. 10864; suppression experiment §6.3 and Table 7, p. 10869 |

## 2. Executive Assessment

**Outcome: REVISE.** One confirmed claim-scope problem requires correction: IA030 generalizes the external-reference ablation without naming the SelfCheckGPT variant. No fabricated reference, materially false numerical transcription, or critical attribution problem was found.

Counting scope: 71 audit units cover all nine body paragraphs, including analytical statements and roadmap text. Compound claims are split where they have different sources; a numerical comparison and its conditions remain one unit. This is not the matrix's 135 extracted research claims, and repeated manuscript statements are separately located rather than counted as new research findings.

| Measurement | Count |
| --- | ---: |
| Citation-dependent factual/comparative claim units | 36 |
| SUPPORTED | 35 |
| PARTIALLY_SUPPORTED | 1 |
| UNSUPPORTED | 0 |
| UNVERIFIABLE | 0 |
| MISSING_CITATION | 0 |
| Substantive analytical/recommendation units, citation not separately required | 34 |
| Roadmap unit, not a substantive factual assertion | 1 |
| Total substantive units considered (facts plus analysis) | 70 |
| Confirmed CRITICAL / MAJOR / MINOR issues | 0 / 1 / 0 |
| Cited publications / matched references | 9 / 9 |

The severity total counts unique confirmed problems, not every occurrence or every optional check. The major issue is IA030. Bibliography checks IB001–IB009 found no confirmed identity/metadata errors. IB010 is a minor-priority **REVIEW_REQUIRED formatting question**, not a confirmed error, and is excluded from confirmed severity totals. Source access and citation-style identification did not block completion. A final rendered-document typography check remains outside this Markdown audit.

## 3. Claim-to-Citation Audit

Locations use global body paragraphs P1–P9 and sentence numbers S, excluding headings. P1=Introduction line 5; P2/P3=Consistency and Separated Checking lines 9/11; P4/P5=Documentary Fact-Checking lines 15/17; P6/P7=Critical Comparison lines 21/23; P8=Limitations and Research Needs line 27; P9=Conclusion line 31. Semicolon-linked clauses count as one sentence. Source locators in the last column refer to the original PDFs linked in §1.

`ANALYSIS` means an explicit inference, evaluative principle, recommendation, or synthesis grounded in adjacent reported findings; it is outside the five factual-support categories and does not need an artificial additional citation. `ROADMAP` is authorial scope text. An inherited citation means the immediately preceding attribution clearly governs the continued discussion of the same named study. `None` in the severity column means no confirmed issue.

| Audit ID | Draft Location | Claim (short paraphrase) | In-Text Citation | Global VERIFIED Claim ID(s) | Support Status | Severity | Required Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IA001 | Introduction P1 S1, L5 | Evaluation needs an evidential criterion | None | Not applicable | ANALYSIS | None | Framing premise; no source required. |
| IA002 | Introduction P1 S2a, L5 | SelfCheckGPT uses samples, no external database | Manakul et al., 2023 | SRC-001-C001 | SUPPORTED | None | §§4–5. |
| IA003 | Introduction P1 S2b, L5 | CoVe separates checking from the initial response | Dhuliawala et al., 2024 | SRC-002-C002 | SUPPORTED | None | §3.3, p. 3566; read with factored qualification in P3. Optional precision: name separated execution here too. |
| IA004 | Introduction P1 S2c, L5 | FActScore checks atomic source support | Min et al., 2023 | SRC-003-C001 | SUPPORTED | None | §3.1, p. 12078. |
| IA005 | Introduction P1 S3, L5 | The methods use different evidential judgments | Preceding three citations | SRC-001-C001; SRC-002-C002; SRC-003-C001 | ANALYSIS | None | Comparative categorization, not an exhaustive taxonomy. |
| IA006 | Introduction P1 S4–5, L5 | Review question, scope and comparison strategy | None | Not applicable | ROADMAP | None | Authorial description of this review. |
| IA007 | Introduction P1 S6, L5 | Distinct benefits do not guarantee truth | Developed throughout | See IA008–IA065 | ANALYSIS | None | Thesis, supported by the ensuing argument. |
| IA008 | Consistency P2 S1, L9 | Useful consistency detection has repeated-error limits | Citations later in P2 | SRC-001-C006; SRC-005-C006 | ANALYSIS | None | Topic-sentence synthesis. |
| IA009 | Consistency P2 S2, L9 | Prompt AUC-PR 93.42 versus 83.21 | Manakul et al., 2023 | SRC-001-C006 | SUPPORTED | None | Table 2, p. 9010; baseline/scale match. |
| IA010 | Consistency P2 S3, L9 | ChatGPT evaluates 20 GPT-3 samples | Inherited Manakul et al., 2023 | SRC-001-C004; SRC-001-C011 | SUPPORTED | None | §7 and Table 4, pp. 9009/9012. |
| IA011 | Consistency P2 S4, L9 | These ranking measures are not accuracy | Inherited Manakul et al., 2023 | SRC-001-C005 | SUPPORTED | None | §7.1/Table 2 metric definitions. |
| IA012 | Consistency P2 S5, L9 | Error subsets use 15 stochastic samples | Tan et al. (2025) | SRC-005-C001; SRC-005-C002 | SUPPORTED | None | §§2.2/3.1, pp. 4756–4757. This is error labeling, not the detector's sampling count. |
| IA013 | Consistency P2 S6, L9 | SE AUROC range 0.3633–0.5427 | Inherited Tan et al. (2025) | SRC-005-C006 | SUPPORTED | None | Eight CE cells, Table 2 p. 4758; four models/two tasks. |
| IA014 | Consistency P2 S7, L9 | Cross-study scores do not refute each other | Manakul/Tan attributions in P2 | SRC-001-C005; SRC-005-C002; SRC-005-C006 | ANALYSIS | None | Design/metric comparison, not a pooled result. |
| IA015 | Consistency P2 S8, L9 | Consistency has an evidential boundary | P2 citations | SRC-005-C006 | ANALYSIS | None | Explicit inference from preceding result. |
| IA016 | Consistency P2 S9, L9 | Stable errors and selected samples limit inference | P2 citations | SRC-005-C001; SRC-005-C002; SRC-005-C006 | ANALYSIS | None | Existence is demonstrated; deployment prevalence is expressly not inferred. |
| IA017 | Separation P3 S1, L11 | Separation need not supply independent knowledge | Citations later in P3 | SRC-002-C001; SRC-002-C007 | ANALYSIS | None | Topic-sentence distinction. |
| IA018 | Separation P3 S2, L11 | Same model; factored checks omit initial response | Dhuliawala et al., 2024 | SRC-002-C001; SRC-002-C002 | SUPPORTED | None | §§3.3–3.4, pp. 3566–3567. |
| IA019 | Separation P3 S3, L11 | 418-question MultiSpanQA F1 0.39→0.48 | Inherited Dhuliawala et al., 2024 | SRC-002-C003; SRC-002-C004; SRC-002-C007 | SUPPORTED | None | §4.1.3/Table 2, pp. 3567–3568; model and baseline retained. |
| IA020 | Separation P3 S4, L11 | Useful intervention differs from external evidence | Inherited Dhuliawala et al., 2024 | SRC-002-C002; SRC-002-C007 | ANALYSIS | None | Bounded interpretation; not an isolated causal effect size for separation. |
| IA021 | Separation P3 S5a, L11 | SAC³ checks question variants and two models | Zhang et al., 2023 | SRC-004-C002 | SUPPORTED | None | §§4.1–4.3.1, pp. 15448–15449. |
| IA022 | Separation P3 S5b, L11 | Best SAC³ configuration varies by dataset | Zhang et al., 2023 | SRC-004-C008 | SUPPORTED | None | Table 4, p. 15452; no universal winner implied. |
| IA023 | Separation P3 S6, L11 | Repeated errors overlap across models | Tan et al. (2025) | SRC-005-C008 | SUPPORTED | None | Table 3, p. 4758. |
| IA024 | Separation P3 S7, L11 | Another model does not guarantee correctness/independence | Preceding Zhang/Tan citations | SRC-004-C008; SRC-005-C008 | ANALYSIS | None | Logical caution; no statistical independence test is claimed. |
| IA025 | Separation P3 S8, L11 | Specify what is separated | Preceding P3 citations | Not a new empirical claim | ANALYSIS | None | Terminological recommendation. |
| IA026 | Documentary P4 S1, L15 | Documents alter the evidential basis | Citations later in P4 | SRC-003-C001 | ANALYSIS | None | Conceptual framing. |
| IA027 | Documentary P4 S2, L15 | Atomic precision and Wikipedia retrieval | Min et al., 2023 | SRC-003-C001; SRC-003-C004 | SUPPORTED | None | §§3.1/4; Appendix B.1. |
| IA028 | Documentary P4 S3, L15 | Oracle-fact micro-F1 78.7 versus 66.0 | Inherited Min et al., 2023 | SRC-003-C007 | SUPPORTED | None | Appendix B.2/Table 9, pp. 12092–12093; correct target, evaluator and generator. |
| IA029 | Documentary P4 S4, L15 | Comparison does not establish universal superiority | Inherited Min et al., 2023 | SRC-003-C007 | ANALYSIS | None | Explicit scope limitation. |
| IA030 | Documentary P4 S5, L15 | Reference paragraph improves SelfCheckGPT measures | Manakul et al., 2023 | SRC-001-C009 | PARTIALLY_SUPPORTED | MAJOR | Name Prompt (or specify particular variant/metrics). Table 3, p. 9011, has mixed results across variants; the ledger claim is Prompt-specific. |
| IA031 | Documentary P4 S6, L15 | Reference ablation assumes available evidence | Inherited Manakul et al., 2023 | SRC-001-C009 | SUPPORTED | None | §7.3, p. 9011; available WikiBio paragraph. |
| IA032 | Documentary P4 S7, L15 | No guarantee for a noisy retrieval pipeline | Min/Manakul citations in P4 | SRC-003-C007; SRC-001-C009 | ANALYSIS | None | Valid limit on extrapolation; not a claim that FActScore used no retrieval. |
| IA033 | Documentary P5 S1, L17 | Traceability differs from truth | Citations later in P5 | SRC-009-C001 | ANALYSIS | None | Conceptual distinction. |
| IA034 | Documentary P5 S2, L17 | RARR retrieves/revises and improves attribution | Gao et al., 2023 | SRC-009-C002; SRC-009-C005 | SUPPORTED | None | §3 and Table 1, p. 16482; all three human-AIS comparisons increase. |
| IA035 | Documentary P5 S3, L17 | RARR leaves trustworthiness/conflicts unassessed | Inherited Gao et al., 2023 | SRC-009-C001 | SUPPORTED | None | §9, p. 16486. |
| IA036 | Documentary P5 S4, L17 | Attribution gain is not measured objective-truth gain | Inherited Gao et al., 2023 | SRC-009-C001 | ANALYSIS | None | Follows operational definition; footnote 2, p. 16478. |
| IA037 | Documentary P5 S5, L17 | Binary unsupported can merge two outcomes | Song et al., 2024 | SRC-010-C002 | SUPPORTED | None | Appendix G, p. 9463; contradiction/inconclusive distinction retained. |
| IA038 | Documentary P5 S6, L17 | 80-claim inspection exposes snippet limitations | Inherited Song et al., 2024 | SRC-010-C011 | SUPPORTED | None | §4.4.2, pp. 9454–9455. |
| IA039 | Documentary P5 S7, L17 | Balanced sample is not a prevalence estimate | Inherited Song et al., 2024 | SRC-010-C011 | SUPPORTED | None | §4.4.2 specifies half supported, half unsupported; inferential qualification is appropriate. |
| IA040 | Documentary P5 S8, L17 | Source quality/completeness/interpretation remain relevant | Gao/Song citations in P5 | SRC-009-C001; SRC-010-C011 | ANALYSIS | None | Cross-study inference. |
| IA041 | Documentary P5 S9, L17 | Absent retrieved support is not evidence of falsity | P5 citations | SRC-010-C002; SRC-010-C011 | ANALYSIS | None | Logical distinction, no invented false-negative rate. |
| IA042 | Critical P6 S1, L21 | Apparent opposition concerns differing interventions | Citations in P6 | SRC-002-C002; SRC-007-C001 | ANALYSIS | None | Read as this review's comparison, not a field-wide frequency estimate. |
| IA043 | Critical P6 S2a, L21 | Targeted CoVe improved tested performance | Dhuliawala et al., 2024 in S3; P3 | SRC-002-C007 | SUPPORTED | None | Table 2, p. 3568; attribution clear across comparison. |
| IA044 | Critical P6 S2b, L21 | Final reasoning scores decline after two rounds | Huang et al. (2024) | SRC-007-C001; SRC-007-C005 | SUPPORTED | None | Table 3, PDF p. 4; all six final comparisons decline. |
| IA045 | Critical P6 S3, L21 | Procedures, tasks and models differ | Dhuliawala et al., 2024; Huang et al., 2024 | SRC-002-C002; SRC-002-C007; SRC-007-C001; SRC-007-C005 | SUPPORTED | None | CoVe §3.3/Table 2 versus Huang §3/Table 3; controlled-contradiction inference is appropriately denied. |
| IA046 | Critical P6 S4, L21 | Reasoning accuracy differs from open-ended factuality | P6 comparison | SRC-007-C012 | ANALYSIS | None | Outcome distinction. |
| IA047 | Critical P6 S5, L21 | Assessment and improvement also differ for external evidence | Following Gao citation | SRC-009-C010 | ANALYSIS | None | Transition to the reported counterexample. |
| IA048 | Critical P6 S6, L21 | RARR improves NQ answers but not StrategyQA | Gao et al., 2023 | SRC-009-C010 | SUPPORTED | None | §6.2/Fig. 9 caption, p. 16485. |
| IA049 | Critical P6 S7, L21 | Detection, attribution and reasoning repair differ | Preceding citations | SRC-009-C010; SRC-007-C012 | ANALYSIS | None | Outcome taxonomy; no new result. |
| IA050 | Critical P7 S1, L23 | Interpret scores with retained information | Citations later in P7 | SRC-002-C005; SRC-003-C010 | ANALYSIS | None | Evaluation principle. |
| IA051 | Critical P7 S2, L23 | Wikidata precision rises, correct-entity mean falls | Dhuliawala et al., 2024 | SRC-002-C005 | SUPPORTED | None | Table 1, p. 3568: 0.17→0.36 and 0.59→0.38, two-step versus few-shot. |
| IA052 | Critical P7 S3, L23 | Filtering: 52.4%/450 to 19.3%/328 | Niu et al., 2024 | SRC-011-C009; SRC-011-C010 | SUPPORTED | None | Table 7 group 1, p. 10869; retained-response denominator preserved. |
| IA053 | Critical P7 S4, L23 | Context faithfulness, selection not correction | Inherited Niu et al., 2024 | SRC-011-C001; SRC-011-C009 | SUPPORTED | None | §§3.1/6.3; task definition and selection procedure. |
| IA054 | Critical P7 S5, L23 | FActScore recommends abstention/fact counts | Min et al., 2023 | SRC-003-C010 | SUPPORTED | None | Limitations, pp. 12084–12085. |
| IA055 | Critical P7 S6, L23 | CoVe raises both MultiSpanQA precision and recall | Dhuliawala et al., 2024 | SRC-002-C007 | SUPPORTED | None | Table 2, p. 3568; legitimate counterexample to inevitable deletion. |
| IA056 | Critical P7 S7, L23 | Preserve denominators and useful-content measures | P7 citations | Not a new empirical claim | ANALYSIS | None | Methodological recommendation. |
| IA057 | Limitations P8 S1, L27 | Designs limit generalization | Citations later in P8 | Not a new empirical claim | ANALYSIS | None | Standard inferential principle. |
| IA058 | Limitations P8 S2, L27 | Longest-20% selection; 201/1,908 double annotation | Manakul et al., 2023 | SRC-001-C002; SRC-001-C003 | SUPPORTED | None | §6, p. 9008. Optional precision: explicitly name the WikiBio test set. |
| IA059 | Limitations P8 S3, L27 | Single runs/raters; narrow rerun condition | Gao et al., 2023 | SRC-009-C011 | SUPPORTED | None | Appendices A/C, pp. 16490/16492; qualification retained. |
| IA060 | Limitations P8 S4, L27 | Checkpoint selection considers synthetic and human tests | Song et al., 2024 | SRC-010-C007 | SUPPORTED | None | Appendix G, p. 9463; this concerns the verifier checkpoint. |
| IA061 | Limitations P8 S5, L27 | Human evaluation is not necessarily untouched | Inherited Song et al., 2024 | SRC-010-C007 | ANALYSIS | None | Warranted caution, expressly not a measured bias estimate. |
| IA062 | Limitations P8 S6, L27 | SAC³ call accounting is not measured latency/cost | Zhang et al., 2023 | SRC-004-C012 | SUPPORTED | None | Cost discussion p. 15453 and Appendix C.1; symbolic accounting only. |
| IA063 | Limitations P8 S7, L27 | Limitations do not erase observed benefits | P8 and earlier citations | Not a new empirical claim | ANALYSIS | None | Balanced inference, not a replication claim. |
| IA064 | Limitations P8 S8–9, L27 | Recommend matched comparisons and source-quality tests | Prior reported limitations | Not a new empirical claim | ANALYSIS | None | Clearly recommendations, not assertions that no such studies exist. |
| IA065 | Limitations P8 S10, L27 | Review supports conditional conclusions only | Whole review | Not a new empirical claim | ANALYSIS | None | Scope statement. |
| IA066 | Conclusion P9 S1, L31 | Recaps the three bases for confidence | Earlier method citations | SRC-001-C001; SRC-002-C002; SRC-003-C001 | ANALYSIS | None | Previously developed categorization. |
| IA067 | Conclusion P9 S2, L31 | Benefits depend on procedure and setting | Earlier findings | Not a new empirical claim | ANALYSIS | None | Bounded synthesis. |
| IA068 | Conclusion P9 S3, L31 | Repeated errors/source reliability remain unresolved | Gao et al., 2023; Tan et al., 2025 | SRC-009-C001; SRC-005-C006; SRC-005-C008 | SUPPORTED | None | Gao §9 p. 16486; Tan Tables 2–3 p. 4758. Correct claim-to-source association despite alphabetical citation order. |
| IA069 | Conclusion P9 S4, L31 | Repeats approved thesis | Whole review | See IA007 | ANALYSIS | None | No new empirical assertion. |
| IA070 | Conclusion P9 S5, L31 | Identify evidence and information loss | Whole review | Not a new empirical claim | ANALYSIS | None | Normative recommendation. |
| IA071 | Conclusion P9 S6, L31 | Qualified use; no universal winner/optimal hybrid established | Whole review | Not a new empirical claim | ANALYSIS | None | Limited to the reviewed results, not an exhaustive literature claim. |

## 4. Citation and Reference Consistency

All nine author-year cues match exactly one reference, and every reference is used. No duplicates, unused references, journal volume/issue fields mistakenly demanded for proceedings, or nonexistent DOI were identified. The eight ACL DOI strings match their publisher records; the ICLR URL identifies the intended conference version, not an arXiv DOI presented as a proceedings DOI. Author order, initials, years, article titles, proceedings, editors where supplied, page ranges, and publisher were checked against the records and PDF bylines.

| Reference or In-Text Citation | Problem | Verified Bibliographic Evidence | Severity | Required Correction |
| --- | --- | --- | --- | --- |
| IB001: Dhuliawala (L35), SRC-002 | No confirmed error | [Publisher record](https://aclanthology.org/2024.findings-acl.212/), PDF byline; 2024, pp. 3563–3578; Ku/Martins/Srikumar editors | None | None. |
| IB002: Gao (L37), SRC-009 | No confirmed error | [Publisher record](https://aclanthology.org/2023.acl-long.910/), PDF byline; 2023, pp. 16477–16508; Rogers/Boyd-Graber/Okazaki editors | None | Retain Zhao's PDF middle initial despite shortened landing-page form. |
| IB003: Huang (L39), SRC-007 | Identity/author-year supported; special proceedings format considered in IB010 | [ICLR record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html), PDF byline, 2024 | None | Retain PDF's Adams Wei Yu initials. No DOI or pages invented. |
| IB004: Manakul (L41), SRC-001 | No confirmed error | [Publisher record](https://aclanthology.org/2023.emnlp-main.557/), PDF byline; 2023, pp. 9004–9017; Bouamor/Pino/Bali editors | None | Full Gales initials correctly follow PDF. |
| IB005: Min (L43), SRC-003 | No confirmed error | [Publisher record](https://aclanthology.org/2023.emnlp-main.741/), PDF byline; 2023, pp. 12076–12100; same EMNLP editors | None | Full Koh initials correctly follow PDF. |
| IB006: Niu (L45), SRC-011 | No confirmed error | [Publisher record](https://aclanthology.org/2024.acl-long.585/), PDF byline; 2024, pp. 10862–10878; Ku/Martins/Srikumar editors | None | None; Kashun/KaShun capitalization does not change K. Shum. |
| IB007: Song (L47), SRC-010 | No confirmed error | [Publisher record](https://aclanthology.org/2024.findings-emnlp.552/), PDF byline; 2024, pp. 9447–9474; Al-Onaizan/Bansal/Chen editors | None | None. |
| IB008: Tan (L49), SRC-005 | No confirmed error | [Publisher record](https://aclanthology.org/2025.emnlp-main.238/), PDF byline; 2025, pp. 4755–4765; four listed editors match | None | None. |
| IB009: Zhang (L51), SRC-004 | No confirmed error | [Publisher record](https://aclanthology.org/2023.findings-emnlp.1032/), PDF byline; 2023, pp. 15445–15458; Bouamor/Pino/Bali editors | None | None. |
| IB010: Reference typography, particularly L39 | REVIEW_REQUIRED, not a confirmed error: ICLR's editorless online proceedings do not map neatly onto the edited-book example; final typography is unrendered | [APA edited-book guidance](https://apastyle.apa.org/style-grammar-guidelines/references/examples/edited-book-chapter-references), [APA conference-presentation guidance](https://apastyle.apa.org/style-grammar-guidelines/references/examples/conference-presentation-references), and ICLR record | MINOR review priority; excluded from confirmed counts | Confirm the institution's treatment of editorless ICLR proceedings and final title/volume capitalization; check hanging indents and spacing in the rendered document. Do not substitute an unpublished-presentation reference merely because it is a conference paper. |

## 5. Quotations, Paraphrases, and Numerical Findings

- **IA030, confirmed:** The draft says the reference paragraph improved SelfCheckGPT's reported measures without specifying Prompt. Original Table 3 contains improvements and regressions across variants. The appropriate next action is to restore the missing variant/metric qualification, not replace the source. This is a scope problem, not a fabricated experiment. [Manakul et al., §7.3/Table 3](https://aclanthology.org/2023.emnlp-main.557.pdf).
- All explicit numerical assertions were checked: IA009/010/012/013/019/028/038/039/044/051/052/058/059. Their displayed values, denominators, comparison directions, and named metrics match the originals. The audit checks faithful reporting, not recalculation from raw data.
- IA028 retains oracle decomposition and the Not-supported target; IA052 retains the smaller selected-response denominator. IA044 restricts its decline to the final round and tested model conditions. No causal claim was inferred from an observational correlation.
- No substantive direct quotation or block quote appears. The quoted word “unsupported” is a category label, not an unlocated evidentiary excerpt. Technical method names and conventional metric phrases do not alone establish patchwriting. No passage inspected warranted a confirmed quotation-integrity finding. No comprehensive similarity/plagiarism test was performed.
- Potential precision improvements, **not counted as confirmed problems**: IA003 could identify factored execution in the introduction; IA058 could say “WikiBio test set”; IA060 could identify the selected checkpoint as the verifier. Later context and source-specific wording presently preserve their intended scope.

## 6. Missing, Unmapped, and Unverifiable Sources

- No missing reference, UNMAPPED_SOURCE, or inaccessible essential publication was found. All nine cited sources have permanent source IDs; SRC-006 and SRC-008 are uncited inventory items, not missing manuscript references.
- The shared matrix's §4 draft-claim mapping is unpopulated. The table above supplies a proposed mapping for coordinator integration. This administrative traceability gap does not make the original publications unverifiable.
- No cited factual assertion relies on a currently non-VERIFIED ledger entry. IA030 shows why a VERIFIED ledger entry alone cannot certify the final manuscript wording.
- Final typesetting is not available in the supplied Markdown. This limits certification of hanging indents, spacing and page layout, not source access or factual verification.

## 7. Style Compliance

APA 7 is specified, so STYLE_UNSPECIFIED does not apply. Author-date forms, use of *et al.* for three or more authors, parenthetical punctuation, alphabetical multi-source ordering, reference-list alphabetical order, author count/order, initials, year matching, article-title sentence case, proceedings italics, page ranges, editors and DOI presentation were checked. All nine entries list their complete author groups, each under APA's 21-author truncation threshold.

Long paraphrases retain clear named-study continuity; an immediately repeated citation is not required after every sentence. The switch to another study is explicitly attributed. Optional citation repetition at numerical sentences may aid readers, but no mandatory missing-citation problem was established. Source-relative interpretation and the author's recommendations remain distinguishable in context.

The [APA edited-book chapter example](https://apastyle.apa.org/style-grammar-guidelines/references/examples/edited-book-chapter-references) supports the general structure used for the edited ACL proceedings. Conference/proceedings proper names should not be mechanically lowercased. IB010 remains a targeted human formatting check; this report does not assert full rendered APA compliance.

## 8. Priority Fix List

1. **MAJOR — IA030:** Restore the Prompt-specific scope at Documentary Fact-Checking P4 S5, line 15, or identify the exact variant/metrics intended. Preserve the available-reference qualification. The author/coordinator must decide and apply any revision; no replacement prose or source was inserted.
2. **MINOR-PRIORITY REVIEW, not a confirmed error — IB010:** Confirm editorless ICLR reference treatment and final rendered reference typography. Retain verified bibliographic identity and do not invent missing publication fields.

No critical fix is required. Optional precision suggestions in §5 are not additional confirmed errors. Detecting an issue does not establish that any later Stage 7 edit improves factual accuracy; the actual revised wording would require independent reassessment.

## 9. Evidence Matrix Handoff

- Coordinator only: populate §4 from the IA table while retaining its original source/global claim IDs. Do not add these 71 manuscript units to the 135 extracted-claim count.
- IA030 at P4 S5/L15 maps to **SRC-001-C009**. Proposed manuscript citation-audit status: **NEEDS_CORRECTION**. The source-ledger claim itself remains VERIFIED and already contains the needed Prompt qualification; no change to that research claim is requested.
- Other factual rows: proposed **CHECKED** for this draft version. Analytical and roadmap rows: **NOT_APPLICABLE** for standalone factual-citation status, with their supporting connections retained.
- Confirmed audit-cycle measurement: one MAJOR issue, IA030; zero CRITICAL and zero MINOR confirmed issues. IB010 is a separate unresolved formatting review item with minor priority, not an established defect. No classification as new versus repeated across earlier audits is made because this independent pass did not consult them.
- No source allocation, evidence-matrix edit, manuscript revision, peer-review follow-up, or workflow-log/metrics edit was performed by this auditor.

## 10. Outstanding Human Questions

1. Does the author intend P4 S5 to describe the Prompt variant specifically? If so, the needed scope is already supported by SRC-001-C009; broader wording would require a different, accurately delimited comparison.
2. For final formatting, does the receiving institution prescribe a particular APA treatment of editorless ICLR online proceedings? IB010 needs that decision or a final bibliographic-format check, not source access assistance.

No essential access assistance or citation-style clarification is needed to act on the confirmed finding. This audit neither certifies originality nor evaluates overall scientific quality, and it does not authorize submission. Phase 6 report complete; stop before revision.
