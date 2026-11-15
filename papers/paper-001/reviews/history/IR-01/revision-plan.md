# Consolidated Revision Plan: Independent Review IR-01

**Status: AWAITING_HUMAN_APPROVAL. No manuscript changes implemented.**

## Scope, version and independence

Phase5 is complete. Both newly assigned review agents assessed the same original [drafts/draft-v1.md](../drafts/draft-v1.md), byte-identical to [draft.md](../draft.md), SHA256 `5b81fb18f0936edd6a14a2195d6994c20bdc400993acb1c954c21e5f97b8c638`.

The citation auditor and peer reviewer ran in parallel with fresh conversation contexts. Neither received the other's findings or the earlier manuscript reviews. Both explicitly report that those materials were not read. The coordinator read and compared their completed reports afterward. This is documented procedural separation, not proof that model errors are statistically independent.

The user-required isolation overrides the usual peer-audit dependency followup: no reviewer will be sent the other report, and neither completed report is altered during consolidation. The peer's PENDING/not-consulted audit label describes its knowledge boundary, not an unfinished assigned review.

- [Citation audit](citation-audit.md): REVISE.
- [Peer review](peer-review.md): REVISE, minor scholarly revisions; citation-dependent readiness not assessed by that reviewer.
- Byte-identical originals: [audit snapshot](history/IR-01/citation-audit.md), [peer snapshot](history/IR-01/peer-review.md).
- [Review metrics](review-metrics.md) distinguish factual audit units, editorial findings and unresolved questions.
- Earlier canonical reports and revision plan were archived unchanged under [pre-independent-pass](history/pre-independent-pass/).

## Prioritized findings

| Plan ID | Priority / classification | Detected by / original ID | Draft location | Evidence and diagnosis | Proposed action, not implemented |
| --- | --- | --- | --- | --- | --- |
| R01 | MAJOR; confirmed factual-scope error | Citation auditor only / IA030 | P4 S5, Documentary Fact-Checking, line15 | SRC-001-C009 and original SelfCheckGPT Table3, p.9011, support the Prompt variant; other variants have mixed outcomes. Draft omits the variant and can imply method-wide gains. | Restore explicit Prompt scope; retain citation and following reference-availability/noisy-retrieval caveats. No new source or changed thesis needed. |
| R02 | MINOR; confirmed presentation gap, editorial recommendation | Peer reviewer only / IP001 | P1, Introduction, line5 | The draft introduces detection results before explaining differing meanings of hallucination; distinctions occur later. Existing SRC-003-C001, SRC-009-C001 and SRC-011-C001 support source-relative distinctions. | Add a short operational framing sentence, distinguishing factual error from lack of support in specified evidence. Do not invent a universal definition. |
| R03 | MINOR; confirmed compressed comparison, editorial recommendation | Peer reviewer only / IP002 | P3, SAC3 sentence, line11 | Reviewer independently checked original Table4 against SRC-004-C008: Guanaco question/model AUROC 88.0 versus question-only81.3 on HotpotQA-halu, but72.7 versus77.2 on NQ-open-halu. Existing sentence says only that best configurations differ. | Name the datasets and give the direction of this specific comparison. Numbers optional; preserve model, variant and detection outcome. Do not generalize to every verifier. |
| R04 | MINOR; confirmed terminology omission, audience-sensitive recommendation | Peer reviewer only / IP003 | P2-P4, lines9/11/15 | AUC-PR, AUROC, F1/micro-F1 and semantic entropy are not explained. This is a clarity issue, not a false numerical result. | Expand key metric names and briefly distinguish ranking measures from precision/recall-based measures. Gloss semantic entropy only if mapped verified evidence supports the wording; otherwise simplify its presentation. Keep experimental conditions. |
| R05 | MINOR review priority; potential formatting concern, NOT a confirmed error | Citation auditor only / IB010 | Huang/ICLR reference, line39, and final reference typography | Bibliographic identity and conference URL are verified; editorless online proceedings treatment and unrendered layout leave a formatting question. | Check applicable APA treatment and any institution-specific rule, then inspect hanging indents/spacing on export. Do not invent editors/DOI or reclassify an archival paper as an unpublished presentation. No factual-source access issue. |

There are no CRITICAL citation findings and no BLOCKER or MAJOR peer findings. The consolidated major priority arises from the citation audit alone. R02-R04 are genuine observations about the text; their proposed remedies remain editorial judgments, not established factual errors.

### Concrete R01 proposal

Current:

> Similarly, replacing SelfCheckGPT's samples with an available reference paragraph improved its reported measures (Manakul et al., 2023).

Proposed for later authorized revision:

> Similarly, replacing sampled responses with an available reference paragraph improved the reported measures for SelfCheckGPT's Prompt variant (Manakul et al., 2023).

This is a proposed scope repair, not an implemented or independently reassessed correction. Retain the next two sentences' retrieval caveats.

## Overlap, unique findings and historical correspondence

Within this independent pass, **zero issues were identified by both reviewers**. The auditor's confirmed issue is R01, with R05 separately unresolved. The peer's three findings are R02-R04. Broadly similar attention to methodological care is not counted as overlap without the same concrete issue and location. The peer did not detect or adopt IA030; the coordinator does not retroactively add it to that report.

For longitudinal measurement only, after both reviews finished:

- IA030 repeats the earlier A017/PR002 scope issue; this is one underlying citation problem, not a new unique error or evidence of improvement.
- IP003 overlaps the metric-clarity portion of prior PR001 and adds semantic-entropy explanation. Prior PR001's CoVe-introduction suggestion was not independently repeated here; it remains in the earlier archived report and is not silently relabeled resolved.
- IP001 and IP002 are additional editorial findings relative to that earlier pass.
- IB010 is an additional potential formatting question, not a confirmed reference error.
- Differences between prior39 grouped audit units and current36 factual/34 analytical/1 roadmap units reflect different counting schemes, not a change in the unchanged manuscript.

## Optional observations and unresolved checks

The auditor also noted optional precision at IA003 (factored CoVe execution), IA058 (WikiBio test set) and IA060 (verifier checkpoint). These were classified SUPPORTED, not additional defects. They are not required corrections and are excluded from issue totals.

No factual audit unit was UNVERIFIABLE; all nine original publications were accessible to the citation auditor. The peer independently inspected SAC3 passages only and explicitly did not reverify every original source. Its narrower scope must not be presented as a second full factual audit.

The matrix's draft-mapping section remains empty because the user prohibited modifying it; the separate [paragraph map](draft-evidence-map.md) and audit IA table provide traceability. This is not missing evidence or permission to edit the matrix. The audit's39 mapped existing research IDs do not increase the135 extracted-claim total.

## Decisions and stopping boundary

1. Approve or modify the proposed Stage7 scope: R01 required; R02-R04 recommended; R05 a targeted formatting check.
2. Confirm whether the audience is general academic or NLP-specialist if a different level of technical explanation is desired. A general academic audience is a reasonable proposed default, not a new requirement.
3. Supply any applicable institution-specific reference rule if one exists. No such rule is inferred.
4. The encompassing project's AI-use/disclosure compliance remains the human author's responsibility; no unprovided prohibition or approval is invented.

No new research, thesis change or access assistance is needed for R01-R03. Any new explanatory assertion must retain verified support. If edits are later authorized, preserve this first draft and both review reports, record actual changes, recount the approximately1200-word body, and independently assess corrected wording in Stage7. Detection alone does not demonstrate improved factual accuracy.

**STOP after Phase6. No drafter invoked, manuscript rewritten, finding resolved, or Stage7 action authorized by this plan.**
