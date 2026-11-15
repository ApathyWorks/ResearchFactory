# Academic Paper Outline: Detecting and Reducing Hallucinations in Large Language Models: A Review of Verification Techniques

## 1. Assignment and Thesis

- **Course / assignment:** Self-defined demonstration of a multi-agent academic research and writing workflow; no separate course rubric or weighted criteria supplied.
- **Research question:** How do self-consistency checking, independent verification, and evidence-based fact-checking address hallucinations in LLM-generated text, and what limitations remain?
- **Paper type:** Short comparative, critical literature review, not a systematic review or an experimental report.
- **Approved thesis (exact wording):** Consistency checks, separated verification, and documentary fact-checking offer distinct benefits, but each provides fallible evidence rather than guarantees of factual truth.
- **Approval provenance:** The coordinator presented the wording above as Option 1; the human replied, "yes go with option 1." This is the approved concise formulation of synthesis Option 1, not an independently substituted thesis. The approved direction is a bounded comparison without a universal winner or a proven optimal hybrid.
- **Required length and citation style:** Approximately 1,200 body words; APA 7 citations and references; at least three relevant scholarly publications, preferably original peer-reviewed research.
- **Word-count convention:** Allocate 1,200 words to introduction through conclusion, including in-text citations. Title and references are outside this proposed body allocation because the assignment does not explicitly include them. Workflow measurements are explicitly a separate deliverable outside the target.
- **Inputs:** [Assignment](assignment.md), [evidence matrix](evidence-matrix.md), [Phase 3 synthesis](research/synthesis.md), and the relevant summaries and matching independent reports listed below. Synthesis status is READY_FOR_HUMAN_REVIEW in the preserved report; the subsequent human approval governs this outline. Stale pending-approval text in that historical artifact or the unchanged matrix does not negate the explicit approval.
- **Evidence eligibility:** The matrix contains 135 current VERIFIED claims across 11 sources. This outline selects a manageable subset; retained PENDING_VERIFICATION cells in summarizer files are historical extraction labels, not current eligibility. Corrected claim wording and verifier-confirmed locators govern.
- **Exclusions:** The five unmapped ancillary notes identified in Phase 2 remain excluded from factual support. No quotations or new publications are proposed.

| Selected source | Role in the argument | Summary | Verification |
| --- | --- | --- | --- |
| SRC-001, SelfCheckGPT | Consistency design, bounded detection benefit and domain limits | [Summary](summaries/SRC-001.md) | [Report](reviews/verification/SRC-001.md) |
| SRC-002, Chain-of-Verification | Context separation, response improvements and content tradeoffs | [Summary](summaries/SRC-002.md) | [Report](reviews/verification/SRC-002.md) |
| SRC-003, FActScore | Atomic source support, retrieval comparison and missing-source caution | [Summary](summaries/SRC-003.md) | [Report](reviews/verification/SRC-003.md) |
| SRC-004, SAC3 | Cross-model checking and task-dependent outcomes | [Summary](summaries/SRC-004.md) | [Report](reviews/verification/SRC-004.md) |
| SRC-005, Too Consistent to Detect | Repeated errors and nonzero cross-model error overlap | [Summary](summaries/SRC-005.md) | [Report](reviews/verification/SRC-005.md) |
| SRC-007, Large Language Models Cannot Self-Correct Reasoning Yet | Qualified counterpoint to targeted checking | [Summary](summaries/SRC-007.md) | [Report](reviews/verification/SRC-007.md) |
| SRC-009, RARR | Evidence-supported revision, attribution and downstream limits | [Summary](summaries/SRC-009.md) | [Report](reviews/verification/SRC-009.md) |
| SRC-010, VeriScore | Unsupported versus contradicted claims and evaluation limitations | [Summary](summaries/SRC-010.md) | [Report](reviews/verification/SRC-010.md) |
| SRC-011, RAGTruth | Context faithfulness and filtering/coverage tradeoffs | [Summary](summaries/SRC-011.md) | [Report](reviews/verification/SRC-011.md) |

SRC-006 and SRC-008 remain eligible in the research inventory but are not needed in this short outline. Their omission is a scope/space choice, not a rejection of their verified findings. The source register confirms peer review for all nine selected publications.

## 2. Argument Roadmap

Begin by distinguishing three bases for a checking decision: repeated outputs, separately elicited model judgments, and documentary support. Compare consistency with context/model separation, keeping their genuine gains beside their failure modes. Then examine how retrieved evidence changes the basis of checking without resolving source quality or coverage automatically. A dedicated comparison asks whether reported gains concern detection, correction, attribution or retained useful content. Methodological limitations bound the conclusion: the methods are useful in studied settings, but no signal warrants an unconditional truth guarantee.

This is a thematic comparison throughout. Each body section relates more than one publication, and the critical comparison revisits the same methods under common questions rather than repeating their descriptions. The planned manuscript has nine paragraphs; the outline's instructions, tables and evidence lists are not manuscript prose or part of its word allocation.

## 3. Detailed Paper Outline

### 1. Introduction: What counts as verification? - 120 words

**Purpose:** State the research question, establish comparison terms, and present the exact approved thesis.

#### P1 - Orientation and central argument - 120 words

- **Main point / proposed topic sentence:** The three approaches differ in the evidence they use to assess a generated statement.
- **Supporting points:** Briefly contrast sampled-response consistency (SRC-001-C001), separated question contexts (SRC-002-C002), and atomic claims assessed against a specified source (SRC-003-C001). State the approved thesis exactly at the end.
- **Sources:** SRC-001, SRC-002, SRC-003.
- **Qualification:** These are operational distinctions for this review, not a claim that all systems fit mutually exclusive categories. Avoid an unsupported general definition, prevalence estimate, or societal-harm claim.
- **Transition:** Ask whether agreement among model outputs can provide a dependable factuality signal.
- **Evidence need:** None for the bounded introduction.

### 2. Consistency and separated checking: Benefits without independence guarantees - 300 words

**Purpose:** Compare two model-based approaches and establish why a useful signal can remain fallible.

#### P2 - Consistency gains and repeated-error counterevidence - 150 words

- **Main point / proposed topic sentence:** Consistency can support useful detection while failing to distinguish stable mistakes from stable correct answers.
- **Supporting points:** Explain the absence of an external database in SelfCheckGPT (SRC-001-C001). Use one within-study result: Prompt NonFact AUC-PR 93.42 versus 83.21 for the average negative-log-probability baseline (SRC-001-C006). Contrast this with semantic entropy's 0.3633-0.5427 AUROC on constructed consistent-error subsets (SRC-005-C001; SRC-005-C002; SRC-005-C006).
- **Sources:** SRC-001, SRC-005.
- **Qualifications / counterargument:** AUC-PR and AUROC are different metrics; this is not a numerical head-to-head comparison or a refutation of SelfCheckGPT's reported result. The latter subset is not a deployment-prevalence sample. SelfCheckGPT's main Prompt results use ChatGPT evaluating GPT-3 samples, not a purely same-generator check (SRC-001-C006; SRC-001-C011).
- **Transition:** Consider whether separating checking questions or adding another model addresses the limitation.
- **Evidence need:** None; a universal detector ranking would require new matched evidence.

#### P3 - What separation does and does not establish - 150 words

- **Main point / proposed topic sentence:** Separate checking contexts or models can improve outcomes, but neither constitutes independently sourced factual evidence.
- **Supporting points:** Distinguish CoVe's same-model stages and context separation (SRC-002-C001; SRC-002-C002) from SAC3's target/verifier model comparison (SRC-004-C002). Give CoVe's selected closed-book MultiSpanQA F1 improvement, 0.39 to 0.48 (SRC-002-C007). Explain that SAC3's preferred configuration varies by dataset (SRC-004-C008), while repeated errors can overlap across models (SRC-005-C008).
- **Sources:** SRC-002, SRC-004, SRC-005.
- **Qualifications / counterargument:** Retain the 418-question factoid-subset condition with CoVe's result. Non-overlap does not imply correct answers or statistical independence. SAC3 gains support conditional benefit, not a claim that another verifier always helps. Keep detailed model-overlap percentages out unless space permits their full denominators.
- **Transition:** Contrast additional model judgments with checking against inspectable documents.
- **Evidence need:** None for these distinctions; no causal estimate of the effect of independence is proposed.

### 3. Documentary fact-checking: Traceability with source limitations - 260 words

**Purpose:** Compare source-supported evaluation and revision with internal model signals.

#### P4 - External evidence changes the basis of checking - 130 words

- **Main point / proposed topic sentence:** Documentary checking can improve source-relative assessment by connecting individual claims to retrieved evidence.
- **Supporting points:** Explain FActScore's atomic source-relative precision and retrieval-based estimator (SRC-003-C001; SRC-003-C004). Use one comparison, not a catalogue of results: with oracle human atomic facts, Retrieve-to-LM reaches Not-supported micro-F1 78.7 versus self-check 66.0 on InstructGPT outputs (SRC-003-C007). Relate this to SelfCheckGPT's reference-paragraph ablation as corroborating motivation for external information (SRC-001-C009).
- **Sources:** SRC-003, SRC-001.
- **Qualifications / counterargument:** The FActScore comparison does not test end-to-end automatic decomposition or every consistency method. The reference paragraph is already available; it is not a noisy retrieval pipeline. Neither result proves universal documentary superiority.
- **Transition:** Ask what finding support in a document actually establishes.
- **Evidence need:** None; keep these as distinct within-study comparisons.

#### P5 - Attribution and missing evidence are not truth labels - 130 words

- **Main point / proposed topic sentence:** Retrieved support makes checking traceable, but source reliability and incomplete evidence still limit the conclusion.
- **Supporting points:** Introduce RARR's retrieval-and-revision process and improved human attribution in its main settings (SRC-009-C002; SRC-009-C005). Pair that benefit with its explicit lack of source-trustworthiness evaluation or conflict resolution (SRC-009-C001). Compare VeriScore's grouping of contradictory and inconclusive outcomes under binary unsupported labels, with its finding that snippets may not resolve complex claims (SRC-010-C002; SRC-010-C011).
- **Sources:** SRC-009, SRC-010.
- **Qualifications / counterargument:** Attribution improvements are not measured reductions in objectively false statements. VeriScore's qualitative inspection is purposively balanced, not a population prevalence estimate. Unavailable support must not be rewritten as proven falsehood.
- **Transition:** Compare what each approach improves and what its outcome measure omits.
- **Evidence need:** None for the argument; source-quality superiority requires additional evidence.

### 4. Critical comparison: Outcomes, counterarguments and retained content - 240 words

**Purpose:** Test the thesis against contrary findings and compare the practical meaning of measured improvements.

#### P6 - Apparent disagreement depends on intervention and outcome - 120 words

- **Main point / proposed topic sentence:** Positive verification results and negative self-correction results can coexist because they evaluate different procedures and outcomes.
- **Supporting points:** Contrast CoVe's targeted factual-question improvement (SRC-002-C002; SRC-002-C007) with intrinsic answer-feedback-revision and lower final-round reasoning scores in Huang et al. (SRC-007-C001; SRC-007-C005). Connect the distinction to RARR: increased attribution does not uniformly improve downstream answers, with NQ improvement but no StrategyQA improvement (SRC-009-C010).
- **Sources:** SRC-002, SRC-007, SRC-009.
- **Qualifications / counterargument:** Label this DIFFERENCE_IN_SCOPE, not a controlled contradiction. Huang et al.'s results concern tested reasoning tasks/models, not an impossibility theorem or direct open-ended hallucination rate (SRC-007-C012). Do not assign a precise downstream percentage to RARR because its source wording leaves units ambiguous.
- **Transition:** Even an improved score needs a denominator and a measure of retained useful information.
- **Evidence need:** None for the qualified comparison; a direct causal comparison would require new research.

#### P7 - Better precision can trade off against coverage - 120 words

- **Main point / proposed topic sentence:** Assessing hallucination reduction requires attention to what useful content remains after checking.
- **Supporting points:** Use CoVe's Wikidata precision increase, 0.17 to 0.36, alongside fewer correct entities, 0.59 to 0.38 (SRC-002-C005). Compare RAGTruth zero-span filtering: the labeled rate falls from 52.4% among 450 randomly selected responses to 19.3% among 328 retained outputs (SRC-011-C009; SRC-011-C010). Link this to FActScore's recommendation to report abstention and fact count (SRC-003-C010).
- **Sources:** SRC-002, SRC-003, SRC-011.
- **Qualifications / counterargument:** RAGTruth measures context faithfulness, not independent external truth (SRC-011-C001). Rejection is not correction or verified success. Avoid suggesting all gains merely remove content: CoVe improves precision and recall together on MultiSpanQA (SRC-002-C007). Use this brief counterexample instead of adding another full results table.
- **Transition:** These comparisons require a final appraisal of evidence quality and generalization.
- **Evidence need:** None; cost-effectiveness or overall usefulness is not quantified.

### 5. Limitations and unresolved research questions - 180 words

**Purpose:** Assess how strongly the study designs support the approved claim and identify what a broader claim would require.

#### P8 - Strength of evidence and boundaries of the review - 180 words

- **Main point / proposed topic sentence:** The evidence supports bounded benefits and distinct failure modes more securely than a universal ranking of verification techniques.
- **Supporting points:** Explain narrow sampling and annotation limits using SelfCheckGPT's selected WikiBio population and partially double-annotated sentences (SRC-001-C002; SRC-001-C003). Compare RARR's single-run main evaluation and single-rater post-pilot annotation (SRC-009-C011). Identify VeriScore checkpoint selection involving both synthetic test and human evaluation data as a reason not to assume an untouched final test set (SRC-010-C007). Note that SAC3's simplified call accounting is not measured runtime or monetary cost (SRC-004-C012).
- **Sources:** SRC-001, SRC-009, SRC-010, SRC-004.
- **Interpretation and qualifications:** Frame these as reasons to bound inference, not proof that the reported effects disappear. Do not invent a magnitude of selection bias or claim all papers lack uncertainty analysis. Pair the limitations with the positive within-study evidence already discussed. This bounded inventory is not a systematic review; verified source fidelity is not experimental replication.
- **Research gaps:** Recommend matched human-labeled comparisons with common outcomes and coverage/cost reporting, plus tests of source reliability and missing evidence. These are proposed research needs arising from the selected limitations, not claims that such research exists nowhere.
- **Transition:** Return to the approved thesis at the level the evidence supports.
- **Evidence need:** No section-blocking gap. New evidence is required only for stronger ranking, deployment or current-model claims.

### 6. Conclusion: Useful checks, qualified confidence - 100 words

**Purpose:** Answer the research question without introducing new findings or a new thesis.

#### P9 - Qualified answer and implications - 100 words

- **Main point:** Reaffirm the exact approved thesis. Summarize the comparative distinction: consistency supplies a stability signal, separated checks can improve model responses, and documentary checking adds traceable support; each remains conditional.
- **Previously developed evidence:** SRC-001-C006; SRC-005-C006; SRC-002-C007; SRC-004-C008; SRC-003-C007; SRC-009-C001; SRC-010-C011.
- **Sources:** SRC-001, SRC-005, SRC-002, SRC-004, SRC-003, SRC-009, SRC-010. Use only the citations needed to support the final compressed synthesis; do not repeat every source mechanically.
- **Qualifications:** No universal winner, guaranteed truth, empirically proven optimal hybrid, or newly introduced numerical result. A combined approach may be a research direction, not an established solution.
- **Transition / next step:** End the manuscript's argument; no further substantive section.
- **Evidence need:** None for the approved conclusion.

### 7. References and citation preparation - outside the proposed body count

- Plan an APA 7 reference list for the nine sources actually cited, alphabetized by author. Use the verified inventory/PDF metadata rather than reconstructing references from memory.
- Planned author-year cues: Manakul et al. (2023), Dhuliawala et al. (2024), Min et al. (2023), Zhang et al. (2023), Tan et al. (2025), Huang et al. (2024), Gao et al. (2023), Song et al. (2024), and Niu et al. (2024), corresponding respectively to SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-007, SRC-009, SRC-010 and SRC-011.
- Source/claim IDs belong to the planning and evidence records; they do not replace APA author-date citations in the eventual manuscript.
- Resolve author-initial/name variants against the recorded bylines before final references. For SRC-007, use the canonical ICLR publication URL when citing the conference paper; do not present its separately labeled arXiv DOI as a conference DOI.
- Paraphrase verified findings. No direct quotations or invented locators are planned. This is citation preparation guidance, not a completed citation audit.

## 4. Section-to-Evidence Mapping

All listed global claims are currently VERIFIED. Paragraph-level mapping above gives the intended uses and qualifications; this table summarizes the route through the argument.

| Section | Intended Argument | Supporting VERIFIED Claim IDs | Source IDs | Counterevidence / Limitations | Citation or Evidence Gaps |
| --- | --- | --- | --- | --- | --- |
| 1 / P1 | Distinguish bases of checking and introduce approved thesis | SRC-001-C001; SRC-002-C002; SRC-003-C001 | SRC-001; SRC-002; SRC-003 | Operational categories can overlap | None for scoped introduction |
| 2 / P2-P3 | Model-based signals have demonstrated but conditional benefits | SRC-001-C001; SRC-001-C006; SRC-001-C011; SRC-002-C001; SRC-002-C002; SRC-002-C007; SRC-004-C002; SRC-004-C008 | SRC-001; SRC-002; SRC-004; SRC-005 | SRC-005-C001; SRC-005-C002; SRC-005-C006; SRC-005-C008; unlike metrics and constructed subsets | No matched universal ranking; do not imply one |
| 3 / P4-P5 | Documents provide a different evidential basis, with retrieval/source limits | SRC-003-C001; SRC-003-C004; SRC-003-C007; SRC-001-C009; SRC-009-C002; SRC-009-C005 | SRC-003; SRC-001; SRC-009; SRC-010 | SRC-009-C001; SRC-010-C002; SRC-010-C011; oracle decomposition and reference availability | Source reliability/conflict evaluation remains an optional extension |
| 4 / P6-P7 | Compare intervention, outcome and retained content, not headline scores alone | SRC-002-C002; SRC-002-C007; SRC-007-C001; SRC-007-C005; SRC-009-C010; SRC-002-C005; SRC-011-C009; SRC-011-C010; SRC-003-C010 | SRC-002; SRC-007; SRC-009; SRC-011; SRC-003 | SRC-007-C012; SRC-011-C001; CoVe MultiSpanQA counters inevitable-content-loss claim | No precise RARR downstream effect units; no quantified general usefulness |
| 5 / P8 | Bound evidence strength and specify research needs | SRC-001-C002; SRC-001-C003; SRC-009-C011; SRC-010-C007; SRC-004-C012 | SRC-001; SRC-009; SRC-010; SRC-004 | These limitations do not nullify reported results or establish measured bias | Matched studies, independent held-out human evaluation, source-quality and actual-cost tests needed for stronger claims |
| 6 / P9 | Reaffirm approved thesis without overgeneralization | SRC-001-C006; SRC-005-C006; SRC-002-C007; SRC-004-C008; SRC-003-C007; SRC-009-C001; SRC-010-C011 | SRC-001; SRC-005; SRC-002; SRC-004; SRC-003; SRC-009; SRC-010 | No universal winner, truth guarantee or proven hybrid | None for bounded conclusion |
| 7 / References | Attribute original publications accurately | Claim mappings above; bibliographic source register | All nine selected sources | Author variants; repository versus conference DOI | Final APA formatting and later authorized audit remain pending |

## 5. Assignment / Rubric Coverage

COVERED means planned in this outline, not already satisfied by a completed manuscript. No numerical grading rubric was supplied, and no criteria or weights are invented.

| Requirement or Rubric Criterion | Planned Section(s) | Evidence / Approach | Coverage Status (COVERED / PARTIAL / UNRESOLVED) |
| --- | --- | --- | --- |
| Working title and research question | Title; 1; 6 | Preserve assignment title and answer the stated three-approach question | COVERED |
| Approximately 1,200 words | 1-6 | Nine paragraph budgets sum to 1,200 | COVERED |
| Academic writing style | All | Qualified analytical topic sentences; distinguish results, author interpretations and comparative judgments | COVERED |
| APA 7 citations and references | 1-7 | Author-year plan and reference preparation; traceable original publications | COVERED |
| Introduction, analytical body, limitations and conclusion | 1; 2-4; 5; 6 | Explicit section progression | COVERED |
| Self-consistency checking | 2; 4; 5 | SelfCheckGPT, repeated errors and comparison with other checks | COVERED |
| Independent verification | 2; 4 | Separate contexts/models distinguished from external documentary evidence | COVERED |
| Evidence-based fact-checking | 3; 4; 5 | FActScore, RARR and VeriScore; source support and truth distinguished | COVERED |
| Compare findings across multiple publications | 2-5 | Thematic pairing within sections and dedicated cross-approach analysis | COVERED |
| Strengths and weaknesses of each approach | 2-5 | Positive within-study results beside method-specific failure modes | COVERED |
| Opposing findings and methodological limitations | P2; P3; P6-P8 | Repeated errors, task-dependent benefits, correction declines, coverage and design cautions | COVERED |
| At least three relevant scholarly publications; prefer original peer-reviewed work | 2-5; 7 | Nine selected sources with confirmed peer-review status in the register | COVERED |
| Support factual claims with verified evidence | All substantive paragraphs | Stable global claim IDs and matching independent reports; exclude unmapped notes | COVERED |
| Distinguish empirical findings from author interpretations | P6; P8; qualifications throughout | No causal explanation presented as a measured result; no invented effect or pooled estimate | COVERED |
| Avoid unsupported generalization | All | Bounded models/tasks/outcomes; no universal ranking or current-system recommendation | COVERED |
| Independently evaluate suggested starting publications | 2-3; research provenance | SRC-001, SRC-002 and SRC-003 screened and independently verified earlier; use their limitations as well as gains | COVERED |
| Separate workflow measurement deliverable outside manuscript target | Companion artifacts, not body | Coordinator maintains workflow-metrics.md and workflow-log.md; this outline supplies contribution and evidence handoff | COVERED |
| Document AI contributions, sources, verification, human interventions and outstanding issues | Companion artifacts; outline sections 1 and 7-9 | Existing research/report links; coordinator records this handoff and approval boundary | COVERED |
| Demonstration AI-use rules and human responsibility | All stages | Assignment permits AI generation for demonstration; encompassing-project compliance and final writing/submission remain human responsibilities | COVERED |
| Separate weighted rubric, if any | Not supplied | No hidden rubric assumed; recheck only if the human supplies additional requirements | UNRESOLVED |

## 6. Suggested Length Allocation

| Manuscript section | Paragraphs | Approximate words | Main emphasis |
| --- | --- | ---: | --- |
| 1. Introduction | P1: 120 | 120 | Question, comparison terms and approved thesis |
| 2. Consistency and separated checking | P2: 150; P3: 150 | 300 | Benefits, repeated errors and limits of independence |
| 3. Documentary fact-checking | P4: 130; P5: 130 | 260 | Source-relative benefits and evidence limitations |
| 4. Critical comparison | P6: 120; P7: 120 | 240 | Conflicting outcomes, scope and retained-content tradeoffs |
| 5. Limitations and research questions | P8: 180 | 180 | Evidence quality and boundaries |
| 6. Conclusion | P9: 100 | 100 | Qualified answer, no new findings |
| **Body total** | **9 paragraphs** | **1,200** | **980 words (sections 2-5) devoted to comparative analysis and its limitations** |

Title, references, this planning outline, evidence mappings and workflow artifacts are outside the proposed body allocation. The 980 words include brief method explanation needed for analysis; they are not all purely evaluative sentences. Use only a few representative numerical comparisons, retaining their necessary conditions instead of trying to reproduce every mapped result.

## 7. Open Questions and Additional Research

1. **No blocking evidence gap for the approved thesis.** Each substantive paragraph has VERIFIED support, and no selected claim conflicts with its current report. Nine sources exceed the assignment minimum. No new literature search is necessary before approving this bounded outline.
2. **Optional research if scope expands:** Synthesis GAP-01/GAP-05 call for matched comparisons, common outcomes, retained-content reporting and actual cost measurements before a universal ranking or deployment recommendation. GAP-02 concerns source reliability/conflicting evidence. GAP-03/GAP-04 concern held-out human validation and broader domains/models. These are conditional needs, not authorization to begin research.
3. **Bibliographic cleanup before final references:** Preserve recorded author variants and normalize them from the original bylines; do not invent a conference DOI for SRC-007. SRC-008's unresolved name-order issue remains in the inventory but does not affect this selected source set.
4. **Reporting ambiguities:** Avoid disputed numerical attributions and unmapped notes. The only selected VeriScore checkpoint-design caution is the verified qualification within SRC-010-C007; do not adopt its disputed fine-tuned F1 attribution. If disputed details become central, request separately authorized clarification and verification.
5. **Word-count convention:** The assignment does not say whether references count. This plan uses 1,200 body words with references separate; adjust if the human supplies a different rule.
6. **No separate grading rubric:** All stated assignment requirements are planned. Missing optional rubric weights do not block this self-defined assignment; additional supplied requirements would need a coverage check.
7. **Approval still needed:** Human approval of this outline is required before manuscript creation. Thesis approval does not approve the paragraph plan, citation choices, final wording or submission.

## 8. Human Review Checklist

- [ ] The approved thesis is reproduced exactly and remains the central argument.
- [ ] The comparison of all three approaches and nine-paragraph progression is acceptable.
- [ ] The 1,200-word allocation gives sufficient space to critical analysis and limitations.
- [ ] The selected nine-source set is appropriate for the short review.
- [ ] The scope/metric differences, counterexamples, coverage tradeoffs and source-quality cautions remain visible.
- [ ] No optional research extension is required before drafting.
- [ ] The body-only word-count convention and planned APA 7 treatment are acceptable.
- [ ] The human explicitly approves the outline before Phase 5.

## 9. Completion Status

**DRAFT_FOR_APPROVAL.** The outline preserves the approved thesis, supplies paragraph-level purposes and evidence, maps the assignment, and allocates exactly 1,200 planned body words. No section lacks sufficient verified evidence for its scoped argument. No manuscript draft, citation audit, peer review, new research or modification to the shared evidence matrix or verification reports was performed. Stop for human outline approval.
