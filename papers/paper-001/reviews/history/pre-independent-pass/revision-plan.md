# Proposed Revision Plan: draft-v1

Coordinator-owned consolidation of independent reviews. Status: AWAITING_HUMAN_AUTHORIZATION. No manuscript edits applied.

Draft SHA256: 5b81fb18f0936edd6a14a2195d6994c20bdc400993acb1c954c21e5f97b8c638.

## 1. Required evidence-scope correction

- Audit issue: A017, MAJOR; manuscript P4 sentence 5; VERIFIED evidence SRC-001-C009.
- Current: "Similarly, replacing SelfCheckGPT's samples with an available reference paragraph improved its reported measures (Manakul et al., 2023)."
- Proposed: "Similarly, replacing sampled responses with an available reference paragraph improved the reported measures for SelfCheckGPT's Prompt variant (Manakul et al., 2023)."
- Retain the following available-reference/noisy-retrieval caveats. This restores the verified claim's scope without changing thesis, source or claim ID.
- Other variants do not support the unqualified generalization; see [citation audit](citation-audit.md).

## 2. Recommended clarity edits

- Peer issue: PR001, MINOR.
- At first use, expand AUC-PR to "area under the precision-recall curve (AUC-PR)" and AUROC to "area under the receiver operating characteristic curve (AUROC)".
- Briefly identify F1 as a measure combining precision and recall; identify micro-F1 as its pooled form when that term first appears. Preserve each experiment's target, scale and population.
- Introduce "Chain-of-Verification (CoVe)" at first mention.
- These are terminology clarifications, not new empirical claims or changes to the approved argument.

## 3. Authorized scope needed and subsequent checks

Human authorization is required before applying either item under AGENTS.md Phase7. Recommended scope: both bounded fixes, no structural/thesis/source changes.

After authorization, return draft.md to its designated drafter for these edits, preserve draft-v1 and initial reports, recount words, and rerun both independent reviews on the new stable version. This would be revision-review cycle1 of at most2; the initial peer audit-dependency followup does not consume a cycle.

The evidence matrix and source verification reports stay unchanged. The separate draft-evidence-map.md carries manuscript-specific audit status. Final human approval and submission remain separate.
