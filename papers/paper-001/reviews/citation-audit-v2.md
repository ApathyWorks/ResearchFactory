# Citation and Evidence Audit: Detecting and Reducing Hallucinations in Large Language Models: A Review of Verification Techniques

## 1. Audit Scope

- **Revision-review cycle 1**, completed 2026-11-13 (America/Regina). Manuscript: [drafts/draft-v2.md](../drafts/draft-v2.md); independently confirmed SHA-256 `9ac07e41fa7eed4572ac88c6685c528d97d6c19964b7afec4a2b6ba1954f56ba`.
- Read the entire revised manuscript and reference list and compared v1/v2 directly. References and paragraphs P5–P9 are unchanged; revisions occur in P1–P4. The review covers the whole manuscript, not just the original issue.
- Requirements remain [assignment.md](../assignment.md), APA 7, approved AI-generated demonstration. Original [citation-audit.md](citation-audit.md) is preserved unchanged and used only for this auditor's stable IDs and findings.
- Inputs include the previously read assignment, AGENTS.md, agent configuration, approved outline, synthesis, inventory, relevant summaries and independent source-verification reports. Current claim entries in [evidence-matrix.md](../evidence-matrix.md) were checked for the revised uses. All factual mappings below have VERIFIED ledger support; labels alone were not treated as proof.
- Original-source inspections from this auditor's initial pass remain applicable to unchanged claims. Revised claims were checked directly against original publisher text/tables, including RAGTruth §3.4, SAC³ Table 4, SelfCheckGPT Table 3, FActScore Appendix B.2, CoVe Table 2 and Tan §3.1/Table 2. Additional preserved numerical/methodological claims were reopened as needed. No report or AI summary substituted for those original inspections.
- Independence preserved: no peer-review report, consolidation, revision plan, workflow log/metrics, or revision-changes-v2.md was read. No peer findings were requested or used. Only this new report was written.
- All nine essential original publications were accessible and inspected at claim-bearing locations in this audit thread. No authentication bypass, unauthorized copy, or applicable AI-processing prohibition was encountered. Public ACL access is described in its [copyright policy](https://aclanthology.org/faq/copyright/). Text and numerical tables were legible; no plot values were estimated and no experiments were rerun.
- Markdown is the deliverable. No paginated export or full page-layout certification was requested. The ICLR BibTeX download could not be rendered by the web tool (unsupported MIME type), but its publisher record and original PDF were readable; this did not block metadata verification.

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

**Outcome: PASS** for citation accuracy and evidence fidelity in the supplied Markdown manuscript. All citation-dependent claims are supported by inspected original material. The actual scope correction resolves IA030. No new confirmed citation/evidence problems were found.

| Measurement | Count |
| --- | ---: |
| Citation-dependent factual/comparative units | 37 |
| SUPPORTED | 37 |
| PARTIALLY_SUPPORTED | 0 |
| UNSUPPORTED | 0 |
| UNVERIFIABLE | 0 |
| MISSING_CITATION | 0 |
| Analytical/recommendation units, no separate citation required | 32 |
| Roadmap unit | 1 |
| Total current audit units | 70 |
| Total substantive units (facts plus analysis) | 69 |
| Current confirmed CRITICAL / MAJOR / MINOR issues | 0 / 0 / 0 |
| New / repeated unresolved confirmed issues this cycle | 0 / 0 |
| Prior confirmed issues resolved | 1 (IA030) |
| Cited publications / matched references | 9 / 9 |

Counting continuity: retain IA001–IA071 where the same rhetorical/claim unit remains, with IA015 retired because its separate analytical sentence was removed. IA001 now contains a source-dependent RAGTruth assertion instead of an uncited framing premise; this adds one factual unit and removes one analytical unit. Together these changes account for v1's 36 factual/34 analysis/1 roadmap units becoming 37/32/1. Short metric definitions stay within their numerical units. These manuscript units are distinct from the evidence matrix's 135 extracted research claims.

**IA030:** PARTIALLY_SUPPORTED/MAJOR → SUPPORTED/resolved, based on the revised variant-specific wording. **IB010:** prior unconfirmed formatting question → CLOSED, no material defect established after reviewing official APA guidance and the archival source. This is not a silently downgraded confirmed issue: IB010 was never counted as a confirmed error. Page-layout limits are scope boundaries, not unresolved manuscript defects.

## 3. Claim-to-Citation Audit

Locations refer to v2: P1=Introduction L5; P2/P3=Consistency and Separated Checking L9/L11; P4/P5=Documentary Fact-Checking L15/L17; P6/P7=Critical Comparison L21/L23; P8=Limitations and Research Needs L27; P9=Conclusion L31. S denotes sentences, with semicolon clauses remaining one sentence. Stable IA015 is absent from the current table because its sentence was removed.

`ANALYSIS` identifies explicit synthesis, inference or recommendations grounded in nearby findings, rather than a new external factual assertion. `ROADMAP` is authorial scope text. An inherited citation denotes clear continuing attribution to the same study. Original source locators refer to §1 links. None means no confirmed issue.

| Audit ID | Draft Location | Claim (short paraphrase) | In-Text Citation | Global VERIFIED Claim ID(s) | Support Status | Severity | Required Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IA001 | Introduction P1 S1, L5 | RAGTruth may label true but context-unsupported content hallucinated | Niu et al., 2024 | SRC-011-C001 | SUPPORTED | None | §3.4, p. 10866; implicit_true policy. The opening inference preserves source-relative scope. |
| IA002 | Introduction P1 S2a, L5 | SelfCheckGPT uses samples, no external database | Manakul et al., 2023 | SRC-001-C001 | SUPPORTED | None | §§4–5. |
| IA003 | Introduction P1 S2b, L5 | CoVe separates checking from the initial response | Dhuliawala et al., 2024 | SRC-002-C002 | SUPPORTED | None | §3.3, p. 3566; read with factored qualification in P3. Optional precision: name separated execution here too. |
| IA004 | Introduction P1 S2c, L5 | FActScore checks atomic source support | Min et al., 2023 | SRC-003-C001 | SUPPORTED | None | §3.1, p. 12078. |
| IA005 | Introduction P1 S3, L5 | The methods use different evidential judgments | Preceding three citations | SRC-001-C001; SRC-002-C002; SRC-003-C001 | ANALYSIS | None | Comparative categorization, not an exhaustive taxonomy. |
| IA006 | Introduction P1 S4, L5 | Review question, scope and comparison strategy | None | Not applicable | ROADMAP | None | Authorial description of this review. |
| IA007 | Introduction P1 S5, L5 | Distinct benefits do not guarantee truth | Developed throughout | See IA008–IA065 | ANALYSIS | None | Thesis, supported by the ensuing argument. |
| IA008 | Consistency P2 S1, L9 | Useful consistency detection has repeated-error limits | Citations later in P2 | SRC-001-C006; SRC-005-C006 | ANALYSIS | None | Topic-sentence synthesis. |
| IA009 | Consistency P2 S2, L9 | Prompt AUC-PR 93.42 versus 83.21; acronym expanded | Manakul et al., 2023 | SRC-001-C005; SRC-001-C006 | SUPPORTED | None | §7.1 and Table 2, p. 9010; precision-recall curve, baseline and scale match. |
| IA010 | Consistency P2 S3, L9 | ChatGPT evaluates 20 GPT-3 samples | Inherited Manakul et al., 2023 | SRC-001-C004; SRC-001-C011 | SUPPORTED | None | §7 and Table 4, pp. 9009/9012. |
| IA011 | Consistency P2 S4, L9 | These ranking measures are not accuracy | Inherited Manakul et al., 2023 | SRC-001-C005 | SUPPORTED | None | §7.1/Table 2 metric definitions. |
| IA012 | Consistency P2 S5, L9 | Error subsets use 15 stochastic samples | Tan et al. (2025) | SRC-005-C001; SRC-005-C002 | SUPPORTED | None | §§2.2/3.1, pp. 4756–4757. This is error labeling, not the detector's sampling count. |
| IA013 | Consistency P2 S6, L9 | One detector AUROC range 0.3633–0.5427; acronym expanded | Inherited Tan et al. (2025) | SRC-005-C002; SRC-005-C006 | SUPPORTED | None | §3.1 and Table 2, pp. 4757–4758; the detector is SE. Less specific wording does not generalize its numbers to every detector. |
| IA014 | Consistency P2 S7, L9 | Cross-study scores do not refute each other | Manakul/Tan attributions in P2 | SRC-001-C005; SRC-005-C002; SRC-005-C006 | ANALYSIS | None | Design/metric comparison, not a pooled result. |
| IA016 | Consistency P2 S8, L9 | Stable errors and selected samples limit inference | P2 citations | SRC-005-C001; SRC-005-C002; SRC-005-C006 | ANALYSIS | None | Existence is demonstrated; deployment prevalence is expressly not inferred. |
| IA017 | Separation P3 S1, L11 | Separation need not supply independent knowledge | Citations later in P3 | SRC-002-C001; SRC-002-C007 | ANALYSIS | None | Topic-sentence distinction. |
| IA018 | Separation P3 S2, L11 | Same model; factored checks omit initial response | Dhuliawala et al., 2024 | SRC-002-C001; SRC-002-C002 | SUPPORTED | None | §§3.3–3.4, pp. 3566–3567. |
| IA019 | Separation P3 S3, L11 | 418-question MultiSpanQA F1 0.39→0.48; F1 combines precision/recall | Inherited Dhuliawala et al., 2024 | SRC-002-C003; SRC-002-C004; SRC-002-C007 | SUPPORTED | None | §4.1.3/Table 2, pp. 3567–3568. Brief metric gloss is standard and accurate; no added experimental result. |
| IA020 | Separation P3 S4, L11 | Useful intervention differs from external evidence | Inherited Dhuliawala et al., 2024 | SRC-002-C002; SRC-002-C007 | ANALYSIS | None | Bounded interpretation; not an isolated causal effect size for separation. |
| IA021 | Separation P3 S5, L11 | SAC³ checks equivalent variants and target/verifier responses | Zhang et al., 2023 in S6 | SRC-004-C002 | SUPPORTED | None | §§4.1–4.3.1, pp. 15448–15449; adjacent attribution clearly covers named method. |
| IA022 | Separation P3 S6, L11 | Guanaco QM versus Q: 88.0/81.3 and 72.7/77.2 AUROC | Zhang et al., 2023 | SRC-004-C008 | SUPPORTED | None | Table 4, p. 15452, Score columns: HotpotQA-halu then NQ-open-halu; correct variant, directions and 0–100 scale. |
| IA023 | Separation P3 S7, L11 | Repeated errors overlap across models | Tan et al. (2025) | SRC-005-C008 | SUPPORTED | None | Table 3, p. 4758. |
| IA024 | Separation P3 S8, L11 | Another model does not guarantee correctness/independence | Preceding Zhang/Tan citations | SRC-004-C008; SRC-005-C008 | ANALYSIS | None | Logical caution; no statistical independence test is claimed. |
| IA025 | Separation P3 S9, L11 | Specify what is separated | Preceding P3 citations | Not a new empirical claim | ANALYSIS | None | Terminological recommendation. |
| IA026 | Documentary P4 S1, L15 | Documents alter the evidential basis | Citations later in P4 | SRC-003-C001 | ANALYSIS | None | Conceptual framing. |
| IA027 | Documentary P4 S2, L15 | Atomic precision and Wikipedia retrieval | Min et al., 2023 | SRC-003-C001; SRC-003-C004 | SUPPORTED | None | §§3.1/4; Appendix B.1. |
| IA028 | Documentary P4 S3, L15 | Oracle-fact micro-F1 78.7 versus 66.0; pooled-decision explanation | Inherited Min et al., 2023 | SRC-003-C007 | SUPPORTED | None | Appendix B.2/Table 9, pp. 12092–12093; set-based precision/recall over Not-supported facts supports the gloss. |
| IA029 | Documentary P4 S4, L15 | Comparison does not establish universal superiority | Inherited Min et al., 2023 | SRC-003-C007 | ANALYSIS | None | Explicit scope limitation. |
| IA030 | Documentary P4 S5, L15 | Available reference improves Prompt-variant measures | Manakul et al., 2023 | SRC-001-C009 | SUPPORTED | None | RESOLVED: Table 3, p. 9011, Prompt rows improve all five displayed measures. Variant scope now explicit. |
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

All nine in-text author-year cues map to one reference each; every reference is used. The reference list is unchanged, preserving the bylines, years, title identities, eight publisher DOIs, proceedings/editor information and page ranges independently checked in the initial pass. Complete revised-text attribution was reviewed again. No duplicate, irrelevant reference, incorrect author-year cue or material metadata mismatch was found. PDF bylines govern fuller initials where publisher metadata abbreviates a name.

| Reference or In-Text Citation | Problem | Verified Bibliographic Evidence | Severity | Required Correction |
| --- | --- | --- | --- | --- |
| IB001: Dhuliawala (L35), SRC-002 | No confirmed error | [Publisher record](https://aclanthology.org/2024.findings-acl.212/), PDF byline; 2024, pp. 3563–3578; Ku/Martins/Srikumar editors | None | None. |
| IB002: Gao (L37), SRC-009 | No confirmed error | [Publisher record](https://aclanthology.org/2023.acl-long.910/), PDF byline; 2023, pp. 16477–16508; Rogers/Boyd-Graber/Okazaki editors | None | Retain Zhao's PDF middle initial despite shortened landing-page form. |
| IB003: Huang (L39), SRC-007 | No confirmed error; editorless archival proceedings treatment accepted | [ICLR record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html), PDF byline, 2024 | None | Retain PDF's Adams Wei Yu initials. No DOI or pages invented. |
| IB004: Manakul (L41), SRC-001 | No confirmed error | [Publisher record](https://aclanthology.org/2023.emnlp-main.557/), PDF byline; 2023, pp. 9004–9017; Bouamor/Pino/Bali editors | None | Full Gales initials correctly follow PDF. |
| IB005: Min (L43), SRC-003 | No confirmed error | [Publisher record](https://aclanthology.org/2023.emnlp-main.741/), PDF byline; 2023, pp. 12076–12100; same EMNLP editors | None | Full Koh initials correctly follow PDF. |
| IB006: Niu (L45), SRC-011 | No confirmed error | [Publisher record](https://aclanthology.org/2024.acl-long.585/), PDF byline; 2024, pp. 10862–10878; Ku/Martins/Srikumar editors | None | None; Kashun/KaShun capitalization does not change K. Shum. |
| IB007: Song (L47), SRC-010 | No confirmed error | [Publisher record](https://aclanthology.org/2024.findings-emnlp.552/), PDF byline; 2024, pp. 9447–9474; Al-Onaizan/Bansal/Chen editors | None | None. |
| IB008: Tan (L49), SRC-005 | No confirmed error | [Publisher record](https://aclanthology.org/2025.emnlp-main.238/), PDF byline; 2025, pp. 4755–4765; four listed editors match | None | None. |
| IB009: Zhang (L51), SRC-004 | No confirmed error | [Publisher record](https://aclanthology.org/2023.findings-emnlp.1032/), PDF byline; 2023, pp. 15445–15458; Bouamor/Pino/Bali editors | None | None. |
| IB010: ICLR entry and Markdown typography | CLOSED: no material APA defect established; layout outside supplied format | Official APA proceedings guidance and ICLR publisher record, discussed in §7 | None | No manuscript correction required; any later paginated export has its own layout check. |

## 5. Quotations, Paraphrases, and Numerical Findings

- **IA030 resolution:** The sentence now explicitly concerns SelfCheckGPT's Prompt variant. Original Table 3 supports the direction for each of that variant's five measures; the available-reference caveat remains. This establishes fidelity of the particular correction, not general effectiveness of the revision workflow. [Original Table 3, p. 9011](https://aclanthology.org/2023.emnlp-main.557.pdf).
- **IA001 new factual content:** RAGTruth's strict grounding policy explicitly accommodates potentially truthful unsupported material under its hallucination labels. The draft does not equate those labels with objective falsity. [Original §3.4, p. 10866](https://aclanthology.org/2024.acl-long.585.pdf).
- **IA022 new exact comparison:** Values are the Score AUROC columns for Guanaco SAC³-QM and SAC³-Q, not SAC³-all or verbalized confidence. Both datasets and comparison directions are correct. The narrow reversal does not imply that every added verifier worsens results. [Original Table 4, p. 15452](https://aclanthology.org/2023.findings-emnlp.1032.pdf).
- **Metric explanations:** IA009 correctly expands AUC-PR; IA013 correctly expands AUROC and limits the reported range to one detector (SE). IA019's short F1 gloss is mathematically conventional. IA028's pooled-decision gloss matches the paper's set-based Not-supported precision/recall calculation, retaining oracle atomic facts and the original evaluator/generator. [FActScore Appendix B.2, pp. 12092–12093](https://aclanthology.org/2023.emnlp-main.741.pdf).
- Numerical support remains intact for IA010/012/019/028/038/039/044/051/052/058/059. Sampling counts, comparison baselines and selected-response denominators remain visible. The detector sampling procedure is not confused with Tan's 15-sample error-labeling procedure.
- No substantive direct quotations or block quotations were added. The quoted category label “unsupported” does not require a page locator as an evidentiary quotation. No inspected passage warranted a patchwriting or missing-quotation-mark finding. No full similarity or plagiarism test was performed.
- Optional specificity remains possible (naming factored execution earlier, the WikiBio test split, or the VeriScore verifier checkpoint), but current context preserves these claims' intended scope. These are not unresolved defects and are excluded from issue counts.

## 6. Missing, Unmapped, and Unverifiable Sources

No MISSING_CITATION, UNMAPPED_SOURCE, or UNVERIFIABLE claim remains. All factual units have legitimate source IDs and VERIFIED ledger mappings. The new introductory use maps to existing SRC-011-C001; the exact SAC³ comparison maps to SRC-004-C008. No new publication or research-claim ID is needed. Definitions of conventional metric abbreviations do not require invented ledger claims.

The matrix's manuscript-mapping integration belongs to the coordinator; §3 supplies this report's handoff independently of any external draft-evidence-map. Original-source access is sufficient. The unavailable BibTeX rendering does not undermine identity established by readable publisher metadata/PDF.

## 7. Style Compliance

APA 7 is specified and was applied. Checked author-date forms, three-or-more-author *et al.* use, placement and continuity of citations, alphabetical grouped citations, reference ordering, complete author lists, initials, years, source titles, editors, page ranges, DOI URLs and Markdown italics. No material APA citation/reference error is established.

The [official APA proceedings guidance](https://apastyle.apa.org/style-grammar-guidelines/references/examples/conference-proceeding-references) directs published proceedings contributions to the edited-book-chapter pattern where appropriate. The eight edited ACL entries follow that structure. Proper conference/organization names need not be mechanically lowercased.

For **IB010**, the [ICLR publisher record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) identifies the archival conference work but supplies no editors, separate publisher or proceedings DOI. The retained entry provides author, year, title, named source and a retrievable canonical URL. On these available facts, the editorless proceedings adaptation is acceptable; no missing bibliographic field should be invented. APA's [missing-information guidance](https://apastyle.apa.org/style-grammar-guidelines/references/missing-information) supports adapting incomplete references, but does not provide an exact ICLR template; acceptance here is the auditor's application of the standard, not a claim that APA expressly endorses this particular entry. The publication should not be reclassified as an unpublished presentation.

IB010 is therefore closed without manuscript modification. Hanging indents, line spacing and page layout cannot be certified from plain Markdown, but that is outside the requested artifact and is not a reason to withhold this citation/evidence PASS. No STYLE_UNSPECIFIED condition exists.

## 8. Priority Fix List

No required citation/evidence corrections for this version. IA030 is resolved; IB010 is closed. No author decision, access assistance or further source onboarding is required by this audit.

If a paginated version is subsequently created, verify its layout as a separate production task. This is not a pending dependency of the current Markdown review.

## 9. Evidence Matrix Handoff

| Item | Previous state | Current state and coordinator action |
| --- | --- | --- |
| IA030, P4 S5/L15; SRC-001-C009 | PARTIALLY_SUPPORTED; MAJOR; NEEDS_CORRECTION | SUPPORTED; resolved; set manuscript mapping CHECKED for v2. Preserve v1 history. Source ledger claim remains VERIFIED. |
| IB010 | Unconfirmed formatting review question; excluded from issue totals | CLOSED, no material APA defect; layout limitation is outside scope. Do not count as a corrected factual claim. |
| IA001, P1 S1/L5; SRC-011-C001 | ANALYSIS framing premise | Revised factual unit SUPPORTED; add its manuscript mapping, not a new research claim. |
| IA022, P3 S6/L11; SRC-004-C008 | Qualitative configuration comparison | Exact numerical comparison SUPPORTED; update manuscript wording/location mapping. |
| IA009/013/019/028 | Previously supported numerical units | SUPPORTED with correct added metric explanations; retain stable research IDs. |
| IA015 | Analytical sentence | Removed in v2; retire manuscript audit unit, preserve its historical record. |

Other factual units remain CHECKED; analytical/roadmap units are NOT_APPLICABLE for separate factual-citation status. Current counts: 37 SUPPORTED; other support statuses zero; confirmed severity counts 0/0/0. One earlier confirmed major issue resolved; zero new or repeated unresolved confirmed issues. Do not sum audit-cycle totals as distinct problems or confuse manuscript units with the 135 extracted research claims.

Only reviews/citation-audit-v2.md was created. Original audit, manuscript, matrix, other reports and workflow files were preserved. This is an independent citation outcome, not a peer-review or overall assignment verdict.

## 10. Outstanding Human Questions

None required for the citation/evidence audit. Final author approval and any submission remain human responsibilities. PASS does not certify originality, absence of plagiarism, experimental reproducibility or overall scientific quality.

Revision-review cycle 1 citation audit complete. Stop; no manuscript edits, peer consultation or submission.

