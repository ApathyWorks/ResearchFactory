# Citation and Evidence Audit: Detecting and Reducing Hallucinations in Large Language Models

## 1. Audit Scope

Initial review, draft-v1, 2026-11-13. Manuscript: [draft.md](../draft.md), SHA256 5b81fb18f0936edd6a14a2195d6994c20bdc400993acb1c954c21e5f97b8c638; unchanged at completion.

Inputs: [assignment](../assignment.md), [approved outline](../outline.md), [evidence matrix](../evidence-matrix.md), [coordinator mapping](draft-evidence-map.md), relevant summaries and independent verification reports for the nine cited sources. Required style: APA 7. Paragraphs P1-P9 are consecutive prose blocks excluding headings/references; sentence numbers are local to each paragraph.

Original publisher PDFs were independently opened and inspected at claim-bearing methods, tables, appendices and limitations. Publisher metadata was checked separately. Full text was accessible for all nine sources. No access bypass or processing prohibition was encountered. [ACL rights policy](https://aclanthology.org/faq/copyright/) permits attributed use of its post-2016 materials under CC BY 4.0; the prior SRC-007 rights record was also consulted. Inspection used readable PDF text/tables, not estimates from graphs. No experimental replication, comprehensive visual-layout inspection or plagiarism-database search was performed.

| Source | Original publication inspected | Principal evidence locations inspected | Metadata record |
| --- | --- | --- | --- |
| SRC-001 | [SelfCheckGPT PDF](https://aclanthology.org/2023.emnlp-main.557.pdf) | Sections 4-7; Tables 1-4; pp. 9008-9012 | [Publisher](https://aclanthology.org/2023.emnlp-main.557/) |
| SRC-002 | [CoVe PDF](https://aclanthology.org/2024.findings-acl.212.pdf) | Sections 3-4; Tables 1-2; pp. 3565-3568 | [Publisher](https://aclanthology.org/2024.findings-acl.212/) |
| SRC-003 | [FActScore PDF](https://aclanthology.org/2023.emnlp-main.741.pdf) | Sections 3.1/4.1; Limitations; Appendix B.2/Table 9 | [Publisher](https://aclanthology.org/2023.emnlp-main.741/) |
| SRC-004 | [SAC3 PDF](https://aclanthology.org/2023.findings-emnlp.1032.pdf) | Section 4; Table 4; Computational Cost; Appendix C.1 | [Publisher](https://aclanthology.org/2023.findings-emnlp.1032/) |
| SRC-005 | [Too Consistent PDF](https://aclanthology.org/2025.emnlp-main.238.pdf) | Sections 2-4; Tables 2-3 | [Publisher](https://aclanthology.org/2025.emnlp-main.238/) |
| SRC-007 | [ICLR PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf) | Sections 2-3, Table 3, pp. 2-4; scope discussion | [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) |
| SRC-009 | [RARR PDF](https://aclanthology.org/2023.acl-long.910.pdf) | Sections 2-3, 5-6, 9; Table 1/Figure 9 caption; Appendices A/C | [Publisher](https://aclanthology.org/2023.acl-long.910/) |
| SRC-010 | [VeriScore PDF](https://aclanthology.org/2024.findings-emnlp.552.pdf) | Sections 2.3/3.4/4.4; Appendix G, p. 9463 | [Publisher](https://aclanthology.org/2024.findings-emnlp.552/) |
| SRC-011 | [RAGTruth PDF](https://aclanthology.org/2024.acl-long.585.pdf) | Sections 3.1/3.4/6.3; Table 7 | [Publisher](https://aclanthology.org/2024.acl-long.585/) |

## 2. Executive Assessment

**Outcome: REVISE.**

- Substantive assertion/comparison units reviewed: **39**. Related clauses are grouped; these are draft audit units, not newly extracted scientific claims.
- **38 SUPPORTED; 1 PARTIALLY_SUPPORTED; 0 UNSUPPORTED; 0 UNVERIFIABLE; 0 MISSING_CITATION.**
- Unique open issues: **0 CRITICAL; 1 MAJOR; 0 MINOR.**
- Required fix: **A017**, documentary-checking P4 sentence 5, needs the Prompt-variant scope restored. The underlying verified evidence is sound; the manuscript drops a material qualifier.
- All nine in-text source identities match their references; all 35 mapped global IDs are VERIFIED. No nonexistent publication, fabricated numerical result or material bibliographic mismatch was found.
- A017 concerns comparative interpretation, not fabrication or failure of the approved thesis. Its repetition below is one issue.

## 3. Claim-to-Citation Audit

SUPPORTED includes clearly identifiable analytical inferences grounded in cited evidence; these do not certify new empirical results.

| Audit ID | Draft Location | Claim (short paraphrase) | In-Text Citation | Global VERIFIED Claim ID(s) | Support Status | Severity | Required Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A001 | Introduction P1 S2a | Sampling without external database | Manakul et al., 2023 | SRC-001-C001 | SUPPORTED | None | None |
| A002 | Introduction P1 S2b | Checking-question separation | Dhuliawala et al., 2024 | SRC-002-C002 | SUPPORTED | None | None |
| A003 | Introduction P1 S2c | Atomic source-relative assessment | Min et al., 2023 | SRC-003-C001 | SUPPORTED | None | None |
| A004 | Introduction P1 S3-S6 | Different evidential bases; qualified thesis | Prior citations; author's scope | SRC-001-C001; SRC-002-C002; SRC-003-C001 | SUPPORTED | None | Review framing, not new measurement |
| A005 | Consistency P2 S1-S2 | Prompt advantage over probability baseline | Manakul et al., 2023 | SRC-001-C006 | SUPPORTED | None | Preserve benchmark/scale |
| A006 | Consistency P2 S3-S4 | Evaluator, samples and metric caution | Continuing Manakul attribution | SRC-001-C006; SRC-001-C011 | SUPPORTED | None | None |
| A007 | Consistency P2 S5 | Repeated-error subset construction | Tan et al., 2025 | SRC-005-C001; SRC-005-C002 | SUPPORTED | None | None |
| A008 | Consistency P2 S6 | Semantic-entropy CE AUROC range | Continuing Tan attribution | SRC-005-C006 | SUPPORTED | None | Eight relevant cells match |
| A009 | Consistency P2 S7-S9 | Different tests; no deployment prevalence inference | Comparison of preceding sources | SRC-001-C006; SRC-005-C002; SRC-005-C006 | SUPPORTED | None | Qualified interpretation |
| A010 | Separated checking P3 S1-S2 | Same-model stages and factored prompts | Dhuliawala et al., 2024 | SRC-002-C001; SRC-002-C002 | SUPPORTED | None | None |
| A011 | Separated checking P3 S3-S4 | Closed-book F1 gain; limited independence | Continuing Dhuliawala attribution | SRC-002-C007; SRC-002-C002 | SUPPORTED | None | None |
| A012 | Separated checking P3 S5 | SAC3 design and dataset-dependent ranking | Zhang et al., 2023 | SRC-004-C002; SRC-004-C008 | SUPPORTED | None | None |
| A013 | Separated checking P3 S6 | Cross-model repeated-error overlap | Tan et al., 2025 | SRC-005-C008 | SUPPORTED | None | None |
| A014 | Separated checking P3 S7-S8 | Separation is no truth guarantee | Analysis of preceding evidence | SRC-002-C002; SRC-004-C008; SRC-005-C008 | SUPPORTED | None | No statistical independence asserted |
| A015 | Documentary P4 S1-S2 | Source-relative measure and retrieval estimator | Min et al., 2023 | SRC-003-C001; SRC-003-C004 | SUPPORTED | None | None |
| A016 | Documentary P4 S3-S4 | Oracle-decomposition retrieval comparison | Continuing Min attribution | SRC-003-C007 | SUPPORTED | None | Target/evaluator/conditions retained |
| A017 | Documentary P4 S5 | Reference substitution improves SelfCheckGPT measures | Manakul et al., 2023 | SRC-001-C009 | PARTIALLY_SUPPORTED | MAJOR | Specify Prompt variant, not all variants |
| A018 | Documentary P4 S6-S7 | Available reference is not noisy retrieval | Comparative inference | SRC-001-C009; SRC-003-C007 | SUPPORTED | None | Preserve after correction |
| A019 | Documentary P5 S2 | Retrieval/revision improves main attribution outcomes | Gao et al., 2023 | SRC-009-C002; SRC-009-C005 | SUPPORTED | None | None |
| A020 | Documentary P5 S1/S3-S4 | Attribution does not settle source truth/conflicts | Continuing Gao attribution | SRC-009-C001 | SUPPORTED | None | None |
| A021 | Documentary P5 S5 | Binary label combines contradiction/inconclusive | Song et al., 2024 | SRC-010-C002 | SUPPORTED | None | None |
| A022 | Documentary P5 S6-S7 | Balanced qualitative sample; snippet limits | Continuing Song attribution | SRC-010-C011 | SUPPORTED | None | None |
| A023 | Documentary P5 S8-S9 | Absent support differs from falsity | Synthesis of Gao and Song | SRC-009-C001; SRC-010-C002; SRC-010-C011 | SUPPORTED | None | Bounded interpretation |
| A024 | Critical P6 S1-S2 | Targeted gains versus intrinsic-revision declines | Huang et al., 2024; CoVe attribution next sentence | SRC-002-C007; SRC-007-C001; SRC-007-C005 | SUPPORTED | None | None |
| A025 | Critical P6 S3-S4 | Scope difference, not controlled contradiction | Dhuliawala et al., 2024; Huang et al., 2024 | SRC-002-C002; SRC-007-C012 | SUPPORTED | None | None |
| A026 | Critical P6 S5-S6 | RARR downstream outcomes differ by task | Gao et al., 2023 | SRC-009-C010 | SUPPORTED | None | No ambiguous effect units asserted |
| A027 | Critical P6 S7 | Assessment, attribution and repair differ | Comparative analysis | SRC-002-C007; SRC-007-C005; SRC-009-C010 | SUPPORTED | None | None |
| A028 | Critical P7 S1-S2 | Precision gain with fewer correct entities | Dhuliawala et al., 2024 | SRC-002-C005 | SUPPORTED | None | None |
| A029 | Critical P7 S3 | Filtering changes rate and retained denominator | Niu et al., 2024 | SRC-011-C009; SRC-011-C010 | SUPPORTED | None | None |
| A030 | Critical P7 S4 | Context faithfulness; rejection is not repair | Continuing Niu attribution | SRC-011-C001; SRC-011-C009 | SUPPORTED | None | None |
| A031 | Critical P7 S5 | Report abstention and fact counts | Min et al., 2023 | SRC-003-C010 | SUPPORTED | None | None |
| A032 | Critical P7 S6 | MultiSpanQA precision and recall both improve | Dhuliawala et al., 2024 | SRC-002-C007 | SUPPORTED | None | None |
| A033 | Critical P7 S7 | Preserve denominators and content distinction | Comparative inference | SRC-002-C005; SRC-003-C010; SRC-011-C010 | SUPPORTED | None | None |
| A034 | Limitations P8 S1-S2 | Restricted sampling; partial double annotation | Manakul et al., 2023 | SRC-001-C002; SRC-001-C003 | SUPPORTED | None | None |
| A035 | Limitations P8 S3 | RARR run/rater limitations | Gao et al., 2023 | SRC-009-C011 | SUPPORTED | None | None |
| A036 | Limitations P8 S4-S5 | Checkpoint selection; test-independence caution | Song et al., 2024 | SRC-010-C007 | SUPPORTED | None | Inference distinguished from measured bias |
| A037 | Limitations P8 S6 | Calls are not measured latency/money | Zhang et al., 2023 | SRC-004-C012 | SUPPORTED | None | None |
| A038 | Limitations P8 S7-S10 | Research needs and bounded scope | Author's recommendations | SRC-001-C002; SRC-009-C011; SRC-010-C007; SRC-004-C012; SRC-009-C001 | SUPPORTED | None | Not claims of absent research everywhere |
| A039 | Conclusion P9 | Qualified thesis; repeated errors/source reliability | Gao et al., 2023; Tan et al., 2025; prior argument | SRC-005-C006; SRC-009-C001; SRC-001-C006; SRC-002-C007; SRC-003-C007; SRC-004-C008; SRC-010-C011 | SUPPORTED | None | No new empirical result or proven hybrid |

## 4. Citation and Reference Consistency

All nine references are cited; all cited author-year pairs resolve. Ordering is alphabetical. Eight ACL DOIs match publisher records; ICLR uses its proceedings URL without inventing a DOI. Author order, year, title, page ranges and editors were compared with Section 1 records and original bylines.

| Reference or In-Text Citation | Problem | Verified Bibliographic Evidence | Severity | Required Correction |
| --- | --- | --- | --- | --- |
| Dhuliawala et al. (2024) | None found | Seven authors, three editors, pages and DOI match publisher | None | None |
| Gao et al. (2023) | No correction needed | PDF includes Vincent Y. Zhao; publisher confirms editors and article identity | None | Retain PDF-supported initial |
| Huang et al. (2024) | No material mismatch | PDF includes Adams Wei Yu; official ICLR record confirms version | None | Keep proceedings URL |
| Manakul et al. (2023) | No correction needed | PDF includes Mark J. F. Gales; editors match publisher | None | Retain full initials |
| Min et al. (2023) | No correction needed | PDF uses Pang Wei Koh; editors/pages/DOI match | None | Retain full initials |
| Niu et al. (2024) | None found | Kashun/KaShun capitalization does not alter K. Shum; metadata matches | None | None |
| Song et al. (2024) | None found | Three authors, three editors, pages and DOI match | None | None |
| Tan et al. (2025) | None found | Eleven authors and four editors match | None | None |
| Zhang et al. (2023) | None found | Five authors, editors, SAC3 title and DOI match | None | None |

## 5. Quotations, Paraphrases, and Numerical Findings

**A017, sole required correction:** P4 omits which variant supports the ablation assertion. [Original Table 3/section 7.3, p. 9011](https://aclanthology.org/2023.emnlp-main.557.pdf) shows the mapped Prompt gains, but other variants have mixed or worse outcomes. Restore the variant qualifier. MAJOR reflects its role in the cross-approach comparison; the present scope can mislead despite neighboring caveats. No source replacement or new ID is needed.

Other numerical checks passed: SelfCheckGPT baseline/evaluator details; Tan's subset definition/range; CoVe's F1 and precision/content comparisons; FActScore's oracle decomposition and target; VeriScore's sample/checkpoint procedure; RAGTruth's model pair, retained counts and conditional rates. Locations appear in Section 1 and existing verification reports.

No extended quotations are present. Quotation marks around unsupported identify a category label. No specific patchwriting concern was identified in this focused inspection; this is not a similarity-database clearance or proof of originality.

## 6. Missing, Unmapped, and Unverifiable Sources

None. All nine originals were accessed; all 35 mapped IDs exist and are VERIFIED. No unmapped ancillary U note supports the draft. A017 concerns manuscript scope, not SRC-001-C009 eligibility or access.

## 7. Style Compliance

APA 7 author-date usage, et al., author/year matching, alphabetical ordering, full author lists, article-title case, italicized containers, editors, pagination and DOI/URL presentation were checked. Multiple-source parenthetical citations are alphabetized. Continuing attribution is intelligible; citations were not mechanically required after every adjacent sentence.

ACL entries use edited-volume chapter form, consistent with [APA edited-book chapter guidance](https://apastyle.apa.org/style-grammar-guidelines/references/examples/edited-book-chapter-references). ICLR is an archival paper, not an unarchived presentation; missing DOI/editor/publisher fields were not invented. Proper conference/organization names are preserved.

No material citation-style issue was established. Markdown does not demonstrate final typography, double spacing or hanging indents; check those on export. This later presentation task is not counted as a current citation defect.

## 8. Priority Fix List

1. **MAJOR A017:** Restore Prompt-specific scope in P4/S5, preserving the available-reference/noisy-retrieval caveats and existing SRC-001-C009 mapping.
2. After human authorization, both independent reviewers should check the changed stable manuscript under revision-cycle rules. Do not mark this initial audit PASS before rechecking.

No CRITICAL or MINOR finding is recorded.

## 9. Evidence Matrix Handoff

Keep all 35 mapped global IDs VERIFIED. In the separately owned manuscript mapping, mark draft-v1 P4/S5, A017, NEEDS_CORRECTION; other 38 audit units are supported. Preserve this initial outcome before future report updates. This auditor edited no evidence matrix, mapping or manuscript.

Initial-cycle handoff: 39 units; SUPPORTED38, PARTIALLY_SUPPORTED1, UNSUPPORTED0, UNVERIFIABLE0, MISSING_CITATION0. Unique issue A017=MAJOR; critical0/major1/minor0. No repeated issue from a prior audit cycle. Outcome REVISE.

## 10. Outstanding Human Questions

Authorize the bounded A017 correction before editing. No new literature, thesis change or access assistance is needed. Human final approval remains separate from these review outcomes; this report does not approve submission.
