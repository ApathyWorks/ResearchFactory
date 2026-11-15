# Phase 5 Drafting Report: paper-001

## Status and scope

**DRAFTED — awaiting human approval.** This report completes the drafting handoff for the existing, unchanged manuscript. It does not revise or polish the manuscript, initiate a review, or certify readiness for submission.

- Working manuscript: [draft.md](../draft.md).
- Preserved version-one copy: [drafts/draft-v1.md](../drafts/draft-v1.md), created by the coordinator and confirmed byte-identical to the working manuscript during this report update.
- Original and current manuscript SHA256: `5b81fb18f0936edd6a14a2195d6994c20bdc400993acb1c954c21e5f97b8c638`.
- This handoff task writes only `reviews/drafting-report.md`. The manuscript and all existing evidence, outline, synthesis and review files remain unchanged.
- The current user instruction limits this work to Phase 5 deliverables. Earlier review findings already present in the workspace are disclosed below as prior history; no reviewer was invoked and no new audit was performed for this report.

## Authorization and inputs

The assignment explicitly permits an AI-generated demonstration. The human approved Option 1 and subsequently stated, “outline is approved.” The manuscript follows the [approved outline](../outline.md), [assignment](../assignment.md), [research synthesis](../research/synthesis.md), [evidence matrix](../evidence-matrix.md), and relevant article summaries and independent verification reports. The encompassing project's AI-use compliance and final submission remain human responsibilities.

Approved thesis, retained exactly in the manuscript:

> Consistency checks, separated verification, and documentary fact-checking offer distinct benefits, but each provides fallible evidence rather than guarantees of factual truth.

The approved direction is a bounded comparison of the three approaches, without a universal winner or an experimentally established optimal hybrid. Historical pending-approval labels in preserved planning files do not override the explicit human approvals.

## Reproducible word count

The manuscript contains **1,164 prose words**, including in-text citations; **1,178 words including section-heading text**, or **1,184 whitespace tokens when the six Markdown heading markers are also counted**. The title and reference list are excluded. Counts use whitespace-separated tokens, so hyphenated terms and numeric ranges without spaces each count as one token. This is an approximate manuscript count rather than a claim that every word processor will return an identical number.

To reproduce the prose count: read `draft.md` as UTF-8; take the text before the first `## References`; split on blank lines; exclude blocks beginning with `#`; sum the lengths of each remaining block's whitespace split. To reproduce the heading-inclusive count: take the same pre-reference text, remove its first title line, remove Markdown heading markers (`##`) from the remaining section headings, and count whitespace-separated tokens. This latter procedure returns 1,178 lexical tokens; the earlier drafting handoff's 1,184 count includes the six Markdown `##` tokens. The 1,164 prose-word measure is unchanged and is the primary reported count.

| Section | Paragraphs | Prose words | Approved allocation |
| --- | --- | ---: | ---: |
| Introduction | P1: 118 | 118 | 120 |
| Consistency and Separated Checking | P2: 139; P3: 138 | 277 | 300 |
| Documentary Fact-Checking | P4: 124; P5: 132 | 256 | 260 |
| Critical Comparison | P6: 120; P7: 119 | 239 | 240 |
| Limitations and Research Needs | P8: 168 | 168 | 180 |
| Conclusion | P9: 106 | 106 | 100 |
| **Total** | **Nine paragraphs** | **1,164** | **1,200** |

The prose is 36 words below the approximate target, a 3% difference. No padding or shortening was applied during this handoff. The approved body-only convention excludes references and the separate workflow deliverables.

## Completed content and evidence mapping

All six substantive sections are drafted, with the assignment title, APA author-date citations and nine references. The body compares checking mechanisms, conditional benefits, apparent disagreements, source support versus truth, coverage tradeoffs and methodological limits. The conclusion preserves the approved thesis. No direct quotations or `[EVIDENCE NEEDED]` placeholders appear in the manuscript.

The coordinator-owned [draft evidence map](draft-evidence-map.md) links every paragraph to global claim IDs. It covers **35 distinct VERIFIED source claims across nine publications**. The matrix remains authoritative for source-claim eligibility. Eligibility does not itself establish that every manuscript sentence preserves the source's scope; the prior A017 finding below illustrates that distinction.

| Source ID | Publication | Manuscript role |
| --- | --- | --- |
| SRC-001 | SelfCheckGPT | Consistency design, benchmark result, reference ablation and study limits |
| SRC-002 | Chain-of-Verification | Context separation, response improvement and retained-content tradeoffs |
| SRC-003 | FActScore | Atomic source support, qualified retrieval comparison and evaluation limits |
| SRC-004 | SAC3 | Cross-model comparison and simplified resource accounting |
| SRC-005 | Too Consistent to Detect | Repeated errors and cross-model overlap |
| SRC-007 | Large Language Models Cannot Self-Correct Reasoning Yet | Scoped counterpoint to targeted checking |
| SRC-009 | RARR | Attribution, revision, downstream outcomes and methodological limits |
| SRC-010 | VeriScore | Inconclusive evidence, snippet limits and checkpoint selection |
| SRC-011 | RAGTruth | Context faithfulness and filtering/coverage tradeoffs |

SRC-006 and SRC-008 were omitted in accordance with the approved nine-source outline. This is not a rejection of their verified findings. The five unmapped ancillary notes remain excluded from manuscript support.

## Assumptions and deviations

- No substantive change to the thesis, nine-paragraph organization, source selection or comparative direction was made.
- Section wording was shortened for manuscript headings; the body totals and individual paragraph lengths vary slightly from the outline's approximate allocations as shown above.
- APA references use the independently checked original-PDF author initials where publisher display names were abbreviated. Publisher metadata supplied proceedings editors during the original drafting task. SRC-007 uses the conference record URL rather than presenting its repository DOI as a conference DOI.
- The original drafting task's reference preparation is not an independent citation audit. This report does not newly verify references or quotations.
- No separate weighted rubric was supplied; the manuscript was drafted against the stated assignment requirements.

## Prior known findings — preserved, not re-audited

These findings were already recorded in the existing [citation audit](citation-audit.md) and [peer review](peer-review.md) for the same manuscript hash. They are disclosed to avoid concealing known limitations. No correction, new assessment, reviewer invocation or review-cycle increment occurred in preparing this report.

| Prior finding | Existing severity | Location and issue | Current disposition |
| --- | --- | --- | --- |
| A017 / PR002 | MAJOR; the same underlying issue in both reports | Documentary Fact-Checking, P4 sentence 5: the reference-paragraph improvement is attributed broadly to SelfCheckGPT, while SRC-001-C009 supports the Prompt variant | Unchanged. Existing feedback requests restoring the Prompt qualifier while preserving the available-reference/noisy-retrieval caveat. No correction applied; not a new source-verification failure. |
| PR001 | MINOR | AUC-PR, AUROC and F1/micro-F1 lack brief explanations; CoVe is not explicitly introduced as the abbreviation for Chain-of-Verification | Unchanged. Existing feedback proposes concise terminology clarification. No polish or correction applied. |

A017 and PR002 must not be counted as two unique citation defects. The current handoff reports prior findings; it does not replace, update or approve the earlier review reports.

## Evidence gaps and human decisions

No new missing source, access problem or evidence gap was identified by the drafting handoff. There are no manuscript placeholders. The known A017 scope issue prevents treating the existing prose as fully cleared merely because its underlying source claim is VERIFIED.

Additional research remains optional for the approved bounded comparison. Universal rankings, deployment recommendations, a proven combined architecture or quantitative cost-benefit claims would require further evidence, as recorded in the synthesis. Disputed source details excluded from the draft remain unresolved in their original reports.

The next human decisions are whether to approve the Phase 5 deliverables and whether to authorize any later corrections or review activity. No permission to revise, resume reviews, submit or publish is inferred. **Stop after this Phase 5 handoff.**
