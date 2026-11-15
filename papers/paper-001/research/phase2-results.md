# Phase 2 Completion Report: paper-001

Coordinator-owned handoff, recorded 2026-11-13T21:55:29Z. Status: PHASE_2_COMPLETE_PENDING_HUMAN_APPROVAL. This reports extraction/verification operations, not cross-study synthesis.

## Scope and outcome

All 11 Phase 1-approved articles were processed using original full text by summarizer agents and separate verifier agents. At most three specialists ran concurrently. Only the coordinator integrated the shared evidence matrix. No new publications were added.

- Articles summarized: 11; independently verified: 11; current report outcomes: 11 PASS.
- Distinct extracted claims: 135; current VERIFIED: 135; PARTIALLY_SUPPORTED: 0; UNSUPPORTED: 0; UNVERIFIABLE: 0; PENDING_VERIFICATION: 0.
- Initial assessment counts: 133 VERIFIED and 2 PARTIALLY_SUPPORTED; zero UNSUPPORTED or UNVERIFIABLE.
- Three articles underwent one correction/reverification cycle each; none needed a second attempt. Four distinct evidence records were revised. Two initially nonverified claims became VERIFIED.
- Five ancillary narrative findings remain outside the verified evidence ledger and are excluded from standalone evidence use. They are not five failed extracted claims.
- No full-text access or licensing blocker was reported. Source ambiguities and tool limitations are preserved below.

## Article-level results

| Source | Publication | Claims | Current verification | Correction attempts | Summary | Verification report |
| --- | --- | --- | --- | --- | --- | --- |
| SRC-001 | SelfCheckGPT | 12 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-001.md) | [Report](../reviews/verification/SRC-001.md) |
| SRC-002 | Chain-of-Verification | 12 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-002.md) | [Report](../reviews/verification/SRC-002.md) |
| SRC-003 | FActScore | 13 | PASS; all VERIFIED | 1 | [Summary](../summaries/SRC-003.md) | [Report](../reviews/verification/SRC-003.md) |
| SRC-004 | SAC3 | 12 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-004.md) | [Report](../reviews/verification/SRC-004.md) |
| SRC-005 | Too Consistent to Detect | 12 | PASS; all VERIFIED | 1 | [Summary](../summaries/SRC-005.md) | [Report](../reviews/verification/SRC-005.md) |
| SRC-006 | FactSelfCheck | 12 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-006.md) | [Report](../reviews/verification/SRC-006.md) |
| SRC-007 | Large Language Models Cannot Self-Correct Reasoning Yet | 12 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-007.md) | [Report](../reviews/verification/SRC-007.md) |
| SRC-008 | Understanding the Dark Side of LLMs Intrinsic Self-Correction | 13 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-008.md) | [Report](../reviews/verification/SRC-008.md) |
| SRC-009 | RARR | 13 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-009.md) | [Report](../reviews/verification/SRC-009.md) |
| SRC-010 | VeriScore | 12 | PASS; all VERIFIED | 1 | [Summary](../summaries/SRC-010.md) | [Report](../reviews/verification/SRC-010.md) |
| SRC-011 | RAGTruth | 12 | PASS; all VERIFIED | 0 | [Summary](../summaries/SRC-011.md) | [Report](../reviews/verification/SRC-011.md) |

## Corrections and preserved initial findings

| Source / finding | Initial issue | Correction and current disposition |
| --- | --- | --- |
| SRC-003-C007 | PARTIALLY_SUPPORTED: omitted oracle human atomic facts and Not-supported detection target | Scope added and independently rechecked; VERIFIED. |
| SRC-003-C006 / U001 | Narrative incorrectly called ChatGPT retrieval the best PerplexityAI error result | Evidence row/narrative distinguish minimum error from ranking preservation; C006 VERIFIED, U001 resolved. |
| SRC-005-C007 | PARTIALLY_SUPPORTED: generalized probe superiority beyond supported ID comparisons | Added the OOD counterexample and narrowed comparison; VERIFIED. |
| SRC-010-C007 / U001 | All initial evidence rows VERIFIED, but substantive checkpoint-selection narrative lacked a mapped qualification; report REVISE | Checkpoint selection on both datasets added to C007 qualification and independently confirmed; U001 resolved, report PASS. |

Initial and corrected summaries/reports are preserved under [phase2-history](phase2-history/), with hashes and status snapshots in [workflow-metrics.md](../workflow-metrics.md). Verifier reports retain prior rejected wording and feedback. Correction counts concern distinct edited evidence records, including qualifications; they do not count every prose edit. Infrastructure restarts consumed no evidence-correction attempts.

Verifiers also expanded SRC-007 C008/C011 locators and corrected SRC-011 C009 to section 6.3 in their reports; the matrix uses verifier-confirmed locators. These locator refinements did not change summary claim wording or consume a correction cycle. Original summaries remain preserved.

## Excluded narrative findings and remaining limitations

| Finding | Reason it remains outside the verified ledger | Required action before standalone reuse |
| --- | --- | --- |
| SRC-002-U001 | Confidence-interval reporting note lacks a dedicated evidence mapping | Extract/map and independently verify the intended wording. |
| SRC-004-U001 | Table 5 metric/setting ambiguity is an ancillary caution, not an extracted numerical result | Do not use its disputed comparisons; map the caution if used as criticism. |
| SRC-008-U001 | Appendix B author-position statement is not an evidence-table row | Extract/map and verify if needed. |
| SRC-008-U002 | Narrow uncertainty-reporting observation is not mapped | Do not generalize to absence of all statistical analysis; map and verify if used. |
| SRC-011-U001 | Reporting observation extends beyond the narrower existing Table 5 qualification | Exclude as standalone evidence until mapped and verified. |

No claim has been promoted merely because its summary sounds plausible. VERIFIED means the particular qualified wording is supported by the inspected publication, not that results were replicated or that the source is universally true.

Important source-level ambiguities retained in the reports include SRC-004 Table 5 metric/setting wording; SRC-005 Tables 2/4 baseline differences; SRC-006 yes/no parsing and evaluation-set threshold selection; SRC-008 training-size conditions and executor-feedback scope; SRC-009 percentage/prose interpretation; and SRC-010 inconsistent metric attribution and binary/ternary descriptions. Do not remove those qualifications or invent reconciliations. Any disputed detail becoming essential requires further authorized investigation or author clarification.

Publisher/PDF author variants and SRC-007 repository-versus-conference DOI distinction remain in the inventory and reports. No conference DOI has been fabricated. Screenshot attempts did not provide usable images for several tasks; original PDF text, tables and captions were readable. No precise figure values were inferred from uninspected graphics. Verification does not represent a full visual audit or raw-data reproduction.

## Workflow records and timing

- [Evidence matrix](../evidence-matrix.md): authoritative 135-claim ledger.
- [Workflow log](../workflow-log.md): assignments, completions, approvals, interruptions and corrections.
- [Workflow metrics](../workflow-metrics.md): current counts and immutable historical snapshots.
- Exact starts/durations of repeated credit and usage-limit interruptions are NOT_RECORDED. Wall-clock elapsed time includes these gaps and is not active work or compute time. Human approval wait is tracked separately with observed boundaries.
- Some assignment times are observation checkpoints rather than precise spawn times; the log preserves these gaps and corrections.

## Approval boundary

Phase 2 is complete. Await explicit human approval before synthesis. No synthesis, thesis selection, outline, manuscript, citation audit, or peer review was performed. Those outcomes and manuscript readiness remain NOT_STARTED. The overall workflow is not complete and no paper has been submitted.
