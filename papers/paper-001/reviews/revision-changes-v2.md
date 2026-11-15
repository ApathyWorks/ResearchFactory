# Revision Handoff: draft-v2

## Authorization, version and scope

The human approved R01-R05 in the current [revision plan](revision-plan.md) and requested APA formatting. This is the first authorized manuscript revision cycle. The plan's preserved awaiting-approval label records its earlier state; the subsequent explicit authorization governs these edits.

- Revised manuscript: [draft.md](../draft.md).
- Preserved original: [drafts/draft-v1.md](../drafts/draft-v1.md), unchanged SHA256 `5b81fb18f0936edd6a14a2195d6994c20bdc400993acb1c954c21e5f97b8c638`.
- Stable v2 SHA256: `9ac07e41fa7eed4572ac88c6685c528d97d6c19964b7afec4a2b6ba1954f56ba`.
- Status: **REVISED_FOR_INDEPENDENT_REVIEW**. This is a drafter handoff, not a verdict that findings have been independently resolved.
- Only `draft.md` and this new handoff were written. Prior manuscripts, outline, synthesis, evidence matrix, verification reports and independent review reports were preserved.
- No new scientific publication, empirical claim, quotation or source identifier was introduced. The general academic audience default informed brief terminology clarification.

## Changes by approved plan item

| Plan item | Before | After / action | Evidence and limits |
| --- | --- | --- | --- |
| R01 — Prompt scope | P4: “Similarly, replacing SelfCheckGPT's samples with an available reference paragraph improved its reported measures (Manakul et al., 2023).” | “Similarly, replacing sampled responses with an available reference paragraph improved the reported measures for SelfCheckGPT's Prompt variant (Manakul et al., 2023).” | SRC-001-C009. The two following source-availability/noisy-retrieval caveats remain unchanged. This implements the requested scope repair; independent reassessment is pending. |
| R02 — operational framing | P1 began with a general question about what counts as evidence. | P1 now opens: “Evaluating a generated statement requires distinguishing factual error from lack of support in specified evidence: RAGTruth can label potentially true but contextually unsupported content as hallucinated (Niu et al., 2024).” | SRC-011-C001, already used in P7 and VERIFIED. This illustrates differing operational targets without inventing a universal definition or declaring unsupported content true. Two roadmap sentences were compressed to maintain length. |
| R03 — concrete verifier comparison | P3 said only that SAC3's best configuration differed between datasets. | P3 identifies the Guanaco question-and-model variant: detection AUROC 88.0 versus question-only 81.3 on HotpotQA-halu, but 72.7 versus 77.2 on NQ-open-halu, on the reported 0–100 scale. | SRC-004-C002 and SRC-004-C008; same Zhang et al. (2023) attribution. It does not claim every verifier behaves this way or compare these values with another paper's metrics. |
| R04 — metric and method terminology | AUC-PR, AUROC and F1/micro-F1 appeared without expansion; semantic entropy was unexplained; CoVe appeared without an explicit introduction. | At first use, AUC-PR becomes “area under the precision-recall curve”; AUROC becomes “area under the receiver operating characteristic curve.” F1 is identified as combining precision and recall; micro-F1 is described as pooling classification decisions before combining precision and recall. P1 introduces “Chain-of-Verification (CoVe).” The semantic-entropy name is replaced by “one tested detector,” preserving the same numeric range and experiment. | These are brief conventional methodological explanations, not new empirical findings. The numerical uses retain SRC-001-C006, SRC-005-C006, SRC-002-C007 and SRC-003-C007. No new semantic-entropy mechanism is asserted. SRC-005-C006 still identifies the detector in the evidence map. |
| R05 — APA treatment | The ICLR entry used an archival conference container and stable URL; no confirmed metadata error was established. Markdown did not establish final page typography. | Checked official APA proceedings, edited-chapter and missing-information guidance and the official ICLR record. Retained the existing bibliographically supported entry and reference list; no editors, publisher, DOI or presentation details were invented. | Rationale and remaining typography limitations are recorded below. This targeted check is not an independent citation-audit PASS. |

Other bounded wording changes accompany R02-R04: the P2 sentence announcing a “boundary of consistency” was removed because the next sentence already states the implication; the closing P3 sentence was shortened to “Independence must therefore specify what is separated.” No numerical conditions or counterexamples were removed. P5-P9 and the entire reference list are unchanged.

## Evidence mapping for the revised paragraphs

The [original paragraph map](draft-evidence-map.md) remains a preserved v1 artifact. The table here supplies the complete v2 handoff without changing that file or the matrix. All mapped scientific claims retain their existing VERIFIED status; faithful use in the revised prose awaits independent review. There remain **35 distinct global claim IDs across nine sources**. Moving SRC-011-C001 into P1 adds an application of an existing claim, not a newly extracted claim.

| Paragraph | Intended support | Global claim IDs |
| --- | --- | --- |
| P1 | Operational framing, three checking bases and thesis | SRC-011-C001; SRC-001-C001; SRC-002-C002; SRC-003-C001 |
| P2 | Consistency benefit and repeated-error test | SRC-001-C001; SRC-001-C006; SRC-001-C011; SRC-005-C001; SRC-005-C002; SRC-005-C006 |
| P3 | CoVe separation and concrete SAC3 comparison | SRC-002-C001; SRC-002-C002; SRC-002-C007; SRC-004-C002; SRC-004-C008; SRC-005-C008 |
| P4 | Retrieval evaluation and Prompt-specific reference ablation | SRC-003-C001; SRC-003-C004; SRC-003-C007; SRC-001-C009 |
| P5 | Attribution and insufficient evidence | SRC-009-C001; SRC-009-C002; SRC-009-C005; SRC-010-C002; SRC-010-C011 |
| P6 | Protocol differences and downstream correction | SRC-002-C002; SRC-002-C007; SRC-007-C001; SRC-007-C005; SRC-007-C012; SRC-009-C010 |
| P7 | Precision, faithfulness and retained information | SRC-002-C005; SRC-002-C007; SRC-003-C010; SRC-011-C001; SRC-011-C009; SRC-011-C010 |
| P8 | Methodological limitations and research needs | SRC-001-C002; SRC-001-C003; SRC-009-C011; SRC-010-C007; SRC-004-C012; SRC-009-C001 |
| P9 | Qualified comparative conclusion | SRC-001-C006; SRC-002-C007; SRC-004-C008; SRC-005-C006; SRC-003-C007; SRC-009-C001; SRC-010-C011 |

The P8 source-reliability research recommendation is mapped explicitly to SRC-009-C001 in addition to the original map's methodological IDs, consistent with its preceding P5 discussion. This is an interpretation/research recommendation, not a finding that no relevant research exists elsewhere.

## Reproducible length and structural checks

The revised body contains **1,201 prose words including in-text citations**, or **1,215 words including section-heading text**, excluding title and references. This is 37 prose words more than v1 and one word above the approximate 1,200-word target.

Counting method: read the UTF-8 manuscript; take the portion before `## References`; split on blank lines; exclude blocks beginning with `#`; count whitespace-separated tokens in the remaining nine prose blocks. For the heading-inclusive count, remove the title line and strip the `## ` prefix from section headings before counting. Hyphenated terms and unspaced numeric ranges count as one token. Markdown heading markers are not counted as words.

| Section | Paragraph counts | Section prose count |
| --- | --- | ---: |
| Introduction | P1: 123 | 123 |
| Consistency and Separated Checking | P2: 145; P3: 151 | 296 |
| Documentary Fact-Checking | P4: 137; P5: 132 | 269 |
| Critical Comparison | P6: 120; P7: 119 | 239 |
| Limitations and Research Needs | P8: 168 | 168 |
| Conclusion | P9: 106 | 106 |
| **Total** | **Nine paragraphs** | **1,201** |

The approved thesis is unchanged in the introduction and conclusion. The nine-paragraph progression, six substantive sections, nine-source selection, counterarguments and reference list remain intact. No manuscript evidence placeholders were introduced.

## APA 7 formatting decision and limits

Official [APA conference-proceedings guidance](https://apastyle.apa.org/style-grammar-guidelines/references/examples/conference-proceeding-references) distinguishes journal, whole-book and edited-chapter formats. Its chapter guidance supports the edited-volume treatment already used for the ACL entries. [APA edited-chapter guidance](https://apastyle.apa.org/style-grammar-guidelines/references/examples/edited-book-chapter-references) supports a stable chapter URL when no DOI exists; it does not require inventing missing identifiers. These are formatting authorities, not new scientific sources in the manuscript.

The [official ICLR record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) identifies the work as part of ICLR 2024 and links the published paper. Its available record does not supply editors or a distinct conference DOI. The selected treatment therefore retains the authors, year, nonitalic article title, italic conference container and stable archival URL. It does not recast the published paper as an unpublished presentation or substitute the arXiv DOI.

This is an evidence-based adaptation of the proceedings format to the available record. The consulted APA examples do not show this precise editorless online-conference case. [APA's missing-information guidance](https://apastyle.apa.org/style-grammar-guidelines/references/missing-information) supplies general adaptation principles and distinguishes a work from its larger container; it does not establish a unique ICLR-specific template. No institution-specific rule was supplied. Accordingly, the existing entry was retained rather than making an unsupported cosmetic change. The independent auditor can assess this documented choice; R05 is not self-certified as a resolved factual defect.

The requested canonical artifact remains Markdown. Italics, author-date citations, reference ordering and DOI/URL text are represented there, but Markdown does not enforce or demonstrate APA page layout, double spacing or a half-inch hanging indent. No rendered export was created or visually checked in this task. Those typography checks remain relevant if a paginated submission format is later requested. They are distinct from the accuracy of the reference information.

## Handoff and stopping condition

No new evidence or human clarification is required to hand this stable version to the independent reviewers. R01-R04 are implemented authorizations, not independently validated resolutions. R05's reference-treatment rationale is documented; final export typography remains outside this Markdown-only task. Prior review findings and their snapshots have not been edited or silently downgraded.

The coordinator may now conduct the authorized independent review of v2. The drafter has not spawned reviewers, declared PASS, approved final submission or made changes beyond the authorized scope. Stop after delivering this handoff.
