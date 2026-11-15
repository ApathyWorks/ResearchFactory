# Research Synthesis: Detecting and Reducing Hallucinations in Large Language Models

## 1. Scope and Inputs

This Phase 3 report addresses the [assignment](../assignment.md): How do self-consistency checking, independent verification, and evidence-based fact-checking address hallucinations in LLM-generated text, and what limitations remain? It supports a prospective 1,200-word, APA 7 review; it is not the manuscript or an approved outline. Prepared 2026-11-13 by the designated synthesizer.

The authoritative input is the [evidence matrix](../evidence-matrix.md), checked against all eleven summaries and independent verification reports. All 135 current global claim IDs across 11 permanent source IDs were considered. Each is currently VERIFIED in the matrix and matching report. Verification establishes fidelity to the inspected publication, not replication, universal truth, or the reliability of this agentic workflow.

| Source | Publication | Summary | Independent verification | Eligible claims considered |
| --- | --- | --- | --- | --- |
| SRC-001 | SelfCheckGPT (2023) | [Summary](../summaries/SRC-001.md) | [Report](../reviews/verification/SRC-001.md) | 12 |
| SRC-002 | Chain-of-Verification (2024) | [Summary](../summaries/SRC-002.md) | [Report](../reviews/verification/SRC-002.md) | 12 |
| SRC-003 | FActScore (2023) | [Summary](../summaries/SRC-003.md) | [Report](../reviews/verification/SRC-003.md) | 13 |
| SRC-004 | SAC3 (2023) | [Summary](../summaries/SRC-004.md) | [Report](../reviews/verification/SRC-004.md) | 12 |
| SRC-005 | Too Consistent to Detect (2025) | [Summary](../summaries/SRC-005.md) | [Report](../reviews/verification/SRC-005.md) | 12 |
| SRC-006 | FactSelfCheck (2026) | [Summary](../summaries/SRC-006.md) | [Report](../reviews/verification/SRC-006.md) | 12 |
| SRC-007 | Large Language Models Cannot Self-Correct Reasoning Yet (2024) | [Summary](../summaries/SRC-007.md) | [Report](../reviews/verification/SRC-007.md) | 12 |
| SRC-008 | Understanding the Dark Side of LLMs' Intrinsic Self-Correction (2025) | [Summary](../summaries/SRC-008.md) | [Report](../reviews/verification/SRC-008.md) | 13 |
| SRC-009 | RARR (2023) | [Summary](../summaries/SRC-009.md) | [Report](../reviews/verification/SRC-009.md) | 13 |
| SRC-010 | VeriScore (2024) | [Summary](../summaries/SRC-010.md) | [Report](../reviews/verification/SRC-010.md) | 12 |
| SRC-011 | RAGTruth (2024) | [Summary](../summaries/SRC-011.md) | [Report](../reviews/verification/SRC-011.md) | 12 |

The summaries' retained PENDING_VERIFICATION labels document their extraction stage; the independent reports and integrated matrix supply current eligibility. Corrected wording for SRC-003-C006, SRC-003-C007, SRC-005-C007 and SRC-010-C007 is used. Expanded verifier locators for SRC-007 and SRC-011 take precedence as already integrated by the coordinator. No unresolved substantive matrix/report conflict was found.

Excluded from scientific support are the five unmapped ancillary notes identified in [Phase 2 results](phase2-results.md): SRC-002-U001, SRC-004-U001, SRC-008-U001, SRC-008-U002 and SRC-011-U001. They are traceability exclusions, not five rejected extracted claims. Historical superseded wording is also excluded. No outside publications, new evidence extraction, or invented measurements were introduced.

## 2. Evidence Quality Snapshot

The source register confirms all eleven publications as peer reviewed and accessible in full text. The set combines method proposals, benchmark evaluations, ablations, error analyses and a human-annotated corpus; it is a bounded research inventory, not a systematic review or meta-analysis.

Study designs provide useful within-study comparisons, but heterogeneous outcomes prevent pooling them into one ranking. SelfCheckGPT evaluates 238 predominantly biographical passages and 1,908 sentences; SAC3 combines synthesized binary answers with two 250-example generated-answer sets; CoVe includes 56 and 55 list questions and 418 closed-book factoid questions (SRC-001-C002; SRC-004-C004; SRC-002-C003). RAGTruth broadens task coverage through 2,965 inputs and 17,790 responses, but its 450-input detector test split and context-relative labels remain the relevant comparison conditions (SRC-011-C001; SRC-011-C003; SRC-011-C005). VeriScore covers six main domains with 50 prompts each, while its human verification study contains 320 claims, mostly singly annotated (SRC-010-C005; SRC-010-C008).

Human annotation supports several evaluations without making labels infallible: SelfCheckGPT double-annotates only 201 sentences, FActScore double-annotates 10%, and RAGTruth uses two initial annotators per response (SRC-001-C003; SRC-003-C002; SRC-011-C004). Conversely, FactSelfCheck's fact labels and correction judging are automated, while Too Consistent to Detect uses model labels with a 300-sample human check (SRC-006-C004; SRC-006-C008; SRC-005-C003). RARR's principal results use single runs and single post-pilot raters; its three-run variability check covers one automatic NQ condition (SRC-009-C011).

The synthesis therefore gives most cross-study performance conclusions MODERATE strength, specific exploratory correction conclusions LIMITED strength, and universal rankings INSUFFICIENT strength. These are qualitative judgments about the available evidence, not statistical confidence levels. Shared datasets and evaluators also limit independence: SelfCheckGPT and FactSelfCheck reuse WikiBio, while CoVe biographies are scored with a FActScore estimator (SRC-001-C002; SRC-006-C002; SRC-002-C003). Agreement among the summaries is never counted as scientific corroboration.

## 3. Thematic Findings

### Theme A: Consistency is useful evidence of stability, with a blind spot for repeated errors

SelfCheckGPT offers black-box checking without an external factual database. On its WikiBio benchmark, Prompt achieves NonFact AUC-PR 93.42 versus 83.21 for the average negative-log-probability baseline; these are detection-ranking scores, not accuracy percentages (SRC-001-C001; SRC-001-C006). Its main Prompt evaluator is ChatGPT applied to GPT-3 outputs, so even this approach is not simply the generator judging itself in every condition (SRC-001-C011).

SAC3 identifies both consistently wrong answers and misleading disagreement as possible failure modes, and improves its open-domain detection scores by varying questions and sometimes adding another model (SRC-004-C001; SRC-004-C002; SRC-004-C008). Too Consistent to Detect directly examines repeated-error subsets: semantic-entropy AUROC ranges from 0.3633 to 0.5427 there, with substantially higher scores on inconsistent-error subsets in the stated examples (SRC-005-C001; SRC-005-C002; SRC-005-C006). This is evidence against equating consistency with truth; it does not invalidate SelfCheckGPT's original benchmark result or establish that every consistency detector fails on every task.

**Strength: MODERATE.** Multiple designs establish a meaningful limitation, but they test different detectors, models, datasets and metrics. The repeated-error subset is deliberately constructed and cannot establish deployment prevalence. SelfCheckGPT's biography scope and computational cost further constrain extrapolation (SRC-001-C012; SRC-005-C002). More samples are not a universal remedy: diminishing WikiBio gains coexist with declining FavaMultiSamples hallucination AUC-PR in FactSelfCheck's sample ablation (SRC-001-C010; SRC-006-C012).

### Theme B: Independence must describe what is separated

Three distinct arrangements should be compared. CoVe separates verification-question contexts while retaining the same LLM; SAC3 consults another model without retrieving factual documents; cross-model probing trains classifiers on two models' internal representations. None of those arrangements by itself establishes independently sourced factual support (SRC-002-C001; SRC-002-C002; SRC-004-C002; SRC-005-C009).

There are bounded benefits. CoVe improves MultiSpanQA F1 from 0.39 to 0.48 in its selected closed-book subset (SRC-002-C003; SRC-002-C007). Cross-model probes improve the stated Llama consistent-error AUROCs, but a Qwen inconsistent-error score declines from 0.9174 to 0.9115, preventing an exceptionless benefit claim (SRC-005-C010). SAC3's preferred verifier configuration varies by dataset; verifier refusals are an author-proposed explanation for one weak condition (SRC-004-C008; SRC-004-C009). Cross-model error overlap remains nonzero, and lack of identical errors does not establish statistical independence or correctness (SRC-005-C008).

Intrinsic revision is also not interchangeable with targeted checking. Huang et al. find lower final reasoning scores after two intrinsic correction rounds, while the later Dark Side study reports BoolQ declines but also mitigation gains after prompt changes or supervised training (SRC-007-C005; SRC-007-C012; SRC-008-C003; SRC-008-C008; SRC-008-C009; SRC-008-C011). Its programming protocol includes executor feedback, so the whole study cannot be labeled purely unassisted (SRC-008-C013). These are scope/protocol differences, not a controlled refutation of CoVe.

**Strength: MODERATE** for conditional benefits and the need to specify feedback; **INSUFFICIENT** for a universal ranking of independent verification. Models, supervision, task selection and access to hidden states differ. Reasoning accuracy cannot stand in for a rate of factual hallucination (SRC-005-C005; SRC-007-C012; SRC-008-C004).

### Theme C: Documentary checking adds traceability, but source support and truth remain distinct

FActScore checks atomic facts against a specified knowledge source. Under oracle human decomposition, its retrieval evaluator exceeds its self-check comparator in Not-supported micro-F1 for two generators (78.7 versus 66.0, and 61.9 versus 48.4); this is not end-to-end extraction accuracy or proof of universal retrieval superiority (SRC-003-C001; SRC-003-C004; SRC-003-C007). SelfCheckGPT's reference-paragraph ablation also improves selected measures, but assumes an available reference rather than testing noisy retrieval (SRC-001-C009).

RARR explicitly retrieves evidence and revises text, raising human attribution in its three principal settings while retaining much of the original intent (SRC-009-C002; SRC-009-C005). Its task definition does not evaluate source trustworthiness or resolve conflicting sources, so improved attribution cannot be equated with improved objective truth (SRC-009-C001). FActScore finds web support for three of 30 selected Wikipedia-unsupported rare-person facts; VeriScore distinguishes insufficient/conflicting evidence from contradiction, and its qualitative analysis exposes the limits of snippets for complex claims (SRC-003-C008; SRC-010-C002; SRC-010-C005; SRC-010-C011). RAGTruth likewise measures faithfulness to supplied context, including cases potentially true outside that context (SRC-011-C001).

**Strength: STRONG** for the narrow conceptual distinction between support, contradiction and truth, because it is explicit in multiple verified operational definitions and supported by concrete cases; **MODERATE** for practical benefits in evaluated settings. The small, selected error samples do not establish general false-negative rates, and source coverage, retrieval and claim relations remain failure points (SRC-003-C008; SRC-003-C009; SRC-010-C011). A documentary citation provides an inspectable basis, not automatic validation of its reliability.

### Theme D: Granularity changes what checking can detect and what results mean

Sentence judgments can mix true and false content, motivating atomic facts and context-preserving claims (SRC-001-C012; SRC-003-C001; SRC-010-C001). FactSelfCheck's fact-level AUC-PR is 93.41 versus 86.18 for an adapted sentence-based Prompt comparator, but the fact labels are GPT-4o judgments and comparator conversion is a material limitation (SRC-006-C004; SRC-006-C007). Its sentence-level results do not show uniform superiority: WikiBio hallucination AUC-PR is 92.45 versus Prompt's 93.60, and the preferred Fava variant differs across hallucination versus factuality measures (SRC-006-C005; SRC-006-C006).

RAGTruth similarly distinguishes response detection from character-overlap span detection. Its fine-tuned detector leads aggregate F1, while prompted GPT-4 has higher recall; supervised training data and the particular implementations matter (SRC-011-C005; SRC-011-C006; SRC-011-C007; SRC-011-C008). Fact-level extraction can also fail or lose relations rather than simply make verification better (SRC-006-C011; SRC-010-C011).

**Strength: MODERATE** for granularity and metric dependence; **LIMITED** for general superiority of fact-guided correction. FactSelfCheck's correction thresholds were selected on the evaluation dataset and GPT-4o served as both corrector and judge; the reported improvement does not establish held-out human-evaluated robustness (SRC-006-C008; SRC-006-C009).

### Theme E: Detection, correction and useful retained content require separate evaluation

CoVe's Wikidata precision rises from 0.17 to 0.36 while mean correct entities fall from 0.59 to 0.38; its biography FActScore rises while mean fact count falls (SRC-002-C005; SRC-002-C008). FActScore itself recommends reporting abstention and fact count, and VeriScore's capped supported-count target can penalize concise answers without measuring all relevant true facts (SRC-003-C010; SRC-010-C003; SRC-010-C010).

RAGTruth's zero-span filtering reduces the labeled hallucination rate from 52.4% among 450 randomly selected responses to 19.3% among 328 retained responses for one candidate pair; rejected inputs are not verified successes (SRC-011-C009; SRC-011-C010). RARR trades attribution against preservation and does not uniformly improve downstream answers: NQ improves, StrategyQA does not, and exploratory SummEval attribution declines (SRC-009-C006; SRC-009-C010; SRC-009-C012). FActScore's editing experiment uses gold verification labels, which isolates editing from detector mistakes rather than proving an end-to-end system (SRC-003-C013).

**Strength: MODERATE** for the need to report multiple outcomes, supported by direct tradeoffs across distinct procedures. This does not imply all gains are merely deletion: CoVe improves both precision and recall on its MultiSpanQA subset, and RAGTruth's fewer-span policy lowers labeled hallucinations while retaining all 450 outputs (SRC-002-C007; SRC-011-C010). Cross-model detection gains alone are not correction results (SRC-005-C012).

## 4. Cross-Study Comparison

| Theme | Claim IDs | Agreement or Difference | Methodological Explanation | Evidence Strength | Remaining Uncertainty |
| --- | --- | --- | --- | --- | --- |
| Useful consistency with repeated-error blind spots | SRC-001-C006; SRC-004-C001; SRC-005-C002; SRC-005-C006 | DIFFERENCE_IN_SCOPE, with convergent caution | Biography AUC-PR versus constructed QA error subsets and AUROC; different detectors and labels | MODERATE | Frequency and detectability of repeated errors in deployment |
| CoVe gains versus intrinsic revision losses | SRC-002-C002; SRC-002-C007; SRC-007-C005; SRC-007-C012; SRC-008-C003; SRC-008-C013 | DIFFERENCE_IN_SCOPE | Separated factual questions versus answer-feedback revision; different tasks/models; some executor feedback in SRC-008 | MODERATE | Matched protocol comparison isolating context separation |
| Benefits of another model | SRC-004-C008; SRC-005-C008; SRC-005-C009; SRC-005-C010 | AGREEMENT on conditional benefit; no universal dominance | Black-box QA checks differ from trained hidden-state probes; nonzero overlapping errors remain | MODERATE | How to select verifiers under domain shift and common errors |
| Source-relative support | SRC-003-C001; SRC-003-C008; SRC-009-C001; SRC-010-C002; SRC-011-C001 | AGREEMENT on distinction; DIFFERENCE_IN_SCOPE in label policy | Wikipedia precision, permissive attribution, contradiction-aware search and strict context faithfulness measure different targets | STRONG for distinction | Evidence quality, conflicting sources and absent coverage |
| Fine-grained checking | SRC-001-C012; SRC-006-C004; SRC-006-C005; SRC-006-C007; SRC-010-C011; SRC-011-C006 | AGREEMENT on granularity problem; DIFFERENCE_IN_SCOPE in outcomes | Sentence, atomic fact and character-span units; automatic fact labels and adapted comparators | MODERATE | Human-validated end-to-end benefits without extraction losses |
| Precision, preservation and coverage | SRC-002-C005; SRC-002-C007; SRC-003-C010; SRC-009-C006; SRC-010-C010; SRC-011-C010 | AGREEMENT on importance of multiple measures, with counterexamples to inevitable content loss | List pruning, editing and response rejection change different denominators and objectives | MODERATE | Joint factuality/usefulness gains under equal budgets |
| Best overall method or combined pipeline | SRC-001-C009; SRC-002-C012; SRC-003-C007; SRC-005-C009; SRC-009-C010 | INSUFFICIENT_EVIDENCE | Available within-study tests do not jointly compare all three families under matched tasks, resources and targets | INSUFFICIENT | Whether a particular hybrid is superior, efficient or robust |

## 5. Contradictions and Counterarguments

No clean cross-publication contradiction on an identical method, dataset, model and outcome is established by this inventory. The apparent positive/negative divide largely reflects differences in protocols or endpoints. CoVe's factual checking gains and intrinsic reasoning-correction losses should both be retained; neither supports a universal claim about all self-correction (SRC-002-C007; SRC-002-C012; SRC-007-C005; SRC-007-C012).

There are decisive counterexamples to broader claims. Adding another verifier is not always best (SRC-004-C008); cross-model probing can slightly reduce an inconsistent-error score (SRC-005-C010); finer granularity need not improve sentence metrics (SRC-006-C005); and evidence-supported editing can fail to improve downstream reasoning (SRC-009-C010). Conversely, consistency can outperform same-model debate when response counts are matched, and training can improve refinement performance, so dismissing all internal checking would also overstate the evidence (SRC-007-C009; SRC-008-C009; SRC-008-C011).

Several within-source tensions must remain visible if selected for the eventual manuscript: the FactSelfCheck equations and parsing description conflict; the correction study selects thresholds on test-only data; SRC-008's main-table and small-training-set overturn rates differ; and VeriScore's fine-tuned-verifier score attribution is unresolved (SRC-006-C002; SRC-006-C003; SRC-006-C008; SRC-008-C010; SRC-010-C007). These are verified reporting qualifications, not invented resolutions or reasons to discard all unaffected evidence. The separate unmapped SAC3 table caution remains excluded from standalone scientific support.

A layered procedure is a plausible research direction because different methods expose different limitations, but this synthesis does not claim an optimal hybrid has been experimentally established. Nor does agreement among AI-produced summaries establish independent scientific evidence (SRC-001-C009; SRC-002-C012; SRC-003-C007; SRC-005-C009).

## 6. Research Gaps and Requested Follow-Up

These are gaps in the approved evidence set, not claims that no relevant study exists anywhere. No additional search was launched.

| Gap ID | Missing Question | Why It Matters | Recommended Research Action | Related Claim IDs |
| --- | --- | --- | --- | --- |
| GAP-01 | Which approach performs best under matched tasks, labels, output coverage and resource budgets? | Current metrics and settings cannot support a universal ranking or optimal hybrid | Optional for the recommended bounded review; required before asserting superiority. Seek peer-reviewed head-to-head evaluations with shared human labels, equal token/latency budgets, and coverage reporting | SRC-001-C005; SRC-003-C007; SRC-007-C009; SRC-011-C005 |
| GAP-02 | How do source quality, conflicts and missing evidence affect factual correctness? | Source support and externally established truth are distinct | Optional extension; seek evaluations with assessed source reliability, contradictory evidence, full-document retrieval and expert adjudication | SRC-003-C008; SRC-003-C009; SRC-009-C001; SRC-010-C011 |
| GAP-03 | Do granular checking and correction gains survive held-out human evaluation? | Automated labels, comparator conversion and evaluation-set selection limit inference | Optional unless claiming robust deployment gains. Seek independent replications with human fact labels, preregistered/fixed thresholds, and separate checkpoint-selection/test sets | SRC-006-C004; SRC-006-C007; SRC-006-C008; SRC-010-C007 |
| GAP-04 | How do methods transfer beyond the tested models and domains? | Historical models, narrow biographies/QA and changing domain rankings limit reach | Optional for historical bounded claims; required for current-model or domain-specific recommendations. Seek broad-domain, multilingual or specialized-domain benchmarks with explicit model versions | SRC-001-C012; SRC-003-C012; SRC-007-C003; SRC-008-C012; SRC-010-C008; SRC-010-C010; SRC-011-C012 |
| GAP-05 | What is the joint cost of checking, retained useful information and residual error? | Call counts are not runtime or monetary cost, and pruning can improve a conditional score | Optional extension; seek matched token, latency and cost reporting together with factuality, fact count, abstention and task utility | SRC-002-C011; SRC-003-C010; SRC-004-C012; SRC-006-C011; SRC-011-C010 |
| GAP-06 | Which disputed implementation or reporting details matter to the chosen argument? | Guessing would undermine traceability | No new research required if omitted or qualified. Before relying on disputed details, request authorized author/code clarification and separate extraction/verification | SRC-005-C011; SRC-006-C003; SRC-008-C010; SRC-008-C013; SRC-010-C007 |

**Before outlining:** No additional research is essential for the recommended thesis as narrowly phrased below. The existing eleven peer-reviewed sources exceed the assignment's minimum and support a comparison of mechanisms and limitations. This is a sufficiency judgment for a 1,200-word review, not a claim of exhaustive coverage. New research becomes necessary if the author wants a universal performance ranking, a validated hybrid architecture, current-system claims, or quantified deployment recommendations. Bibliographic cleanup already flagged in the matrix remains necessary before final references, particularly SRC-008's author-name order and SRC-007's repository-versus-conference DOI distinction.

## 7. Tentative Thesis Options

### Option 1 - TENTATIVE, recommended

**Self-consistency and separated model checks can improve hallucination detection or response quality in bounded settings, while documentary fact-checking provides traceable source support; their differing failure modes mean that consistency, verifier agreement and retrieved support should each be treated as fallible evidence rather than guarantees of factual truth.**

- Strongest support: SRC-001-C001; SRC-001-C006; SRC-002-C002; SRC-002-C007; SRC-004-C008; SRC-005-C006; SRC-005-C009; SRC-003-C001; SRC-003-C007; SRC-009-C001; SRC-010-C002.
- Countervailing evidence/limits: SRC-002-C005; SRC-002-C012; SRC-003-C008; SRC-004-C008; SRC-005-C010; SRC-009-C010; SRC-011-C001. These prevent universal ranking, complete-error-removal claims, or equating documentary attribution with truth.
- Feasibility: Best fit for all three assignment areas within 1,200 words. It supports direct mechanism comparison and concrete counterexamples without requiring an exhaustive survey or incompatible numerical rankings.
- Additional research: None essential before choosing this bounded argument. GAP-01 and GAP-02 are optional follow-up priorities. A claim that a specific combined pipeline is superior would require new evidence.

### Option 2 - TENTATIVE

**Claims of hallucination reduction are only informative when detection quality is distinguished from correction success and evaluated alongside retained information, abstention and source coverage, because improved precision or attribution can coexist with lost content or unchanged downstream accuracy.**

- Strongest support: SRC-002-C005; SRC-002-C008; SRC-003-C010; SRC-009-C005; SRC-009-C006; SRC-009-C010; SRC-010-C003; SRC-010-C010; SRC-011-C009; SRC-011-C010.
- Countervailing evidence/limits: SRC-002-C007 improves precision and recall together; SRC-011-C010's fewer-span policy retains all outputs; SRC-009-C007 qualifies mismatched comparator objectives. The thesis must not claim that all reported improvements result from content deletion.
- Feasibility: Strong critical argument with concrete tradeoffs, but the short paper would need deliberate space for self-consistency and cross-model checking so evaluation critique does not displace the assigned comparison.
- Additional research: None essential for these examples. GAP-05 is needed before a quantitative cost-benefit or universal metric recommendation.

### Option 3 - TENTATIVE

**The value of independent verification depends on what information is independent: separate prompts or models can improve checking but retain model-dependent errors, whereas documentary evidence changes the basis of assessment while introducing coverage, retrieval and interpretation limits.**

- Strongest support: SRC-002-C001; SRC-002-C002; SRC-002-C007; SRC-004-C002; SRC-004-C008; SRC-005-C008; SRC-005-C009; SRC-005-C010; SRC-003-C004; SRC-003-C008; SRC-010-C011.
- Countervailing evidence/limits: SRC-004-C009; SRC-007-C009; SRC-009-C001. Different errors do not prove statistical independence, same-model debate is not all verification, and external evidence need not be trustworthy.
- Feasibility: Defensible conceptual focus covering all three approaches, but terminology must stay explicit and avoid suggesting that another agent or model constitutes an independent scientific source.
- Additional research: None essential for the limited comparison. GAP-01 would be required to claim a causal improvement from a particular degree of independence.

**Recommendation:** Select Option 1 and use Option 2's tradeoffs as a limiting argument. Option 1 has the broadest direct fit to the assignment and is supported by both positive results and counterexamples across all three method families. Its conclusion does not depend on disputed source details, a universal superiority claim, or a proven hybrid. Option 3 supplies a useful conceptual distinction within that direction. The recommendation is an interpretive judgment from the mapped evidence; the human author retains the thesis decision.

## 8. Suggested Outline Handoff

Deferred until the human approves the thesis and research direction. No outline or proposed section sequence has been created. The required handoff schema is retained empty for the later authorized stage.

| Potential Section / Theme | Main Point | Supporting VERIFIED Claim IDs | Counterevidence or Caveats | Additional Research Needed |
| --- | --- | --- | --- | --- |

## 9. Limitations and Human Decisions

- Approve, revise or select a tentative thesis and confirm the research direction before Phase 4. No approval of any thesis is inferred from authorization to synthesize.
- Decide whether the bounded review is sufficient or whether a specific gap warrants additional research. The recommended scope requires no new sources before outlining.
- Retain the distinction between original-study findings, author interpretations and this synthesis's comparative judgments. No pooled effect, independent replication or universal consensus was computed.
- No current full-text or licensing blocker was reported for the eligible evidence. Prior verification used readable original text/tables; it did not establish a complete visual audit or reproduce raw experiments. The synthesis does not extend beyond verified evidence to uninspected graphics.
- Preserve the five excluded ancillary notes, historical corrections, and open source ambiguities in the underlying reports. No specialist report, matrix, log or metrics file was changed by the synthesizer.
- The workflow's independent verifier agents checked fidelity to publications. Their separation does not itself empirically validate the workflow or establish statistical independence of AI errors.
- Manuscript citation formatting, outstanding author-name normalization, and final approval remain later tasks. Nothing has been submitted.

## 10. Completion Status

**READY_FOR_HUMAN_REVIEW.** Phase 3 synthesis is complete using the current 135-claim eligible set from eleven sources. Three defensible tentative thesis options and a recommendation are supplied. No blocking evidence inconsistency was found; remaining limitations and conditional follow-up needs are explicit. Stop here for human approval of the thesis and research direction. Do not begin outlining, drafting or manuscript review.
