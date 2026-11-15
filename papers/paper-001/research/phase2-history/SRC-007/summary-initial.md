# Academic Article Summary

## 1. Bibliographic Information

- Source ID: SRC-007 (coordinator assigned).
- Title: Large Language Models Cannot Self-Correct Reasoning Yet.
- Authors: Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Author names follow the original PDF; the proceedings record abbreviates Adams Wei Yu to Adams Yu.
- Publication Year: 2024.
- Journal or Conference: International Conference on Learning Representations (ICLR 2024).
- DOI: No conference DOI located in the approved inventory. [10.48550/arXiv.2310.01798](https://doi.org/10.48550/arXiv.2310.01798) identifies the repository record, not a separately established conference DOI.
- Original Publication URL: [Official proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf); [proceedings record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html).
- Local Document Path: None; original publisher PDF inspected remotely.
- Access Status: FULL_TEXT; 17-page original including appendices accessible on 2026-11-13. Printed page numbers coincide with one-based PDF page numbers throughout this summary.
- Rights/access observation: The [arXiv record](https://arxiv.org/abs/2310.01798) links to [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The public proceedings PDF was accessible without authentication; no AI-processing prohibition was observed in the inspected rights information. The OpenReview page presented a browser challenge and was not bypassed. This is an attributed paraphrase and selective evidence extraction by the summarizer, not the original text or an author-endorsed interpretation.

## 2. Research Overview

The paper evaluates whether models can improve their own reasoning answers without external feedback. It separates intrinsic correction from correction aided by ground-truth labels, examines model-generated feedback on reasoning benchmarks, and tests whether apparent advantages persist against stronger sampling or prompting baselines. Its empirical scope is particular models, prompts, datasets, and evaluation procedures, rather than a theorem that self-correction is impossible (C001–C012).

## 3. Research Questions

The explicit central question is whether intrinsic self-correction improves reasoning: an initial answer is followed by model-generated feedback and a revised answer without outside feedback (C001). Related evaluation questions concern ground-truth stopping criteria (C004), feedback-prompt sensitivity (C007), equal-response comparisons of debate and self-consistency (C009), and the strength of the initial prompt in constrained generation (C010). These subsidiary questions summarize the experimental organization; the paper does not present them as a numbered hypothesis list. Formal statistical hypotheses: Not reported.

## 4. Methodology

The authors compare initial responses with up to two feedback-and-revision rounds. Reasoning evaluation uses GSM8K, CommonSenseQA, and closed-book HotpotQA, with dataset sizes and model-specific sampling given in C002. Model versions, temperatures, and call counts are preserved in C003. Oracle-assisted and intrinsic conditions must be distinguished: the oracle condition uses known correctness to stop revising an already correct answer (C004), whereas intrinsic feedback cannot use that label (C001, C005).

Additional experiments vary feedback prompts (C007), inspect answer transitions (C008), compare three-agent debate with majority-vote self-consistency at equal numbers of generated responses (C009), and vary initial instructions on CommonGen-Hard using concept coverage as the metric (C010). Accuracy values below use the paper's 0–100 reporting scale; HotpotQA uses exact match. Concept coverage is a separate outcome, not factual accuracy (C002, C010).

## 5. Key Findings

1. Oracle-assisted stopping improves reported scores, but supplies external correctness information and therefore cannot establish intrinsic correction ability (C004).
2. After two intrinsic correction rounds, every model/dataset pair in Table 3 is below its corresponding initial score. GPT-4 HotpotQA is unchanged after the first round, so degradation must not be asserted for every individual round (C005). Further tested models also finish below baseline (C006).
3. Alternative feedback prompts change the magnitude of the losses without exceeding the initial baselines in the reported tests (C007). The authors' transition analysis supports concern about changing correct answers, while their explanation of feedback-induced bias remains an interpretation (C008).
4. Debate scores below self-consistency when the number of generated responses is matched in the reported GSM8K experiment (C009).
5. A stronger initial instruction changes the constrained-generation comparison: the improved initial response outperforms its self-corrected counterpart on concept coverage (C010).
6. The authors recommend external-feedback clarity, stronger comparison baselines, and fair prompt-design effort, but their results do not establish universal failure across tasks or future models (C011–C012).

## 6. Evidence Table

Local IDs map to global IDs by prefixing SRC-007-, for example C001 → SRC-007-C001. All claims await independent verification.

| Claim ID | Claim | Source Location | Evidence Type | Qualifications | Verification Status |
| --- | --- | --- | --- | --- | --- |
| C001 | Intrinsic self-correction is correction without external feedback. The evaluated procedure generates an initial answer, obtains feedback from the model, and regenerates an answer using that feedback. | Printed/PDF pp. 2–3, §§2–3.1, definition and three-step procedure. | Operational definition and experimental method. | External human, model, tool, or knowledge feedback is conceptually distinguished from relying on the model's own capabilities. The principal target is reasoning. | PENDING_VERIFICATION |
| C002 | Reasoning evaluation uses the GSM8K test set (1,319 questions), CommonSenseQA development set (1,221), and a 100-question closed-book HotpotQA subset. GPT-3.5 uses those evaluation sets; the more limited evaluations described for other models use 200 randomly sampled examples per dataset, or 100 for HotpotQA. HotpotQA is scored by exact match. | Printed/PDF p. 3, §3.1, Datasets and Models paragraphs. | Experimental design. | Tables 4–6 report GPT-4 Turbo and Llama-2 on GSM8K/CommonSenseQA only; do not imply an unreported HotpotQA result for them. Samples differ across model comparisons. | PENDING_VERIFICATION |
| C003 | The main self-correction experiments use gpt-3.5-turbo-0613, GPT-4 accessed August 29, 2023, gpt-4-1106-preview, and Llama-2-70b-chat. Temperature is 1 for GPT-3.5/GPT-4 and 0 for GPT-4 Turbo/Llama-2. Up to two correction rounds are run, with 1, 3, and 5 model calls for initial, first-round, and second-round responses. | Printed/PDF p. 3, §3.1; pp. 4–5, Tables 3–4; p. 9, Reproducibility Statement. | Experimental configuration. | These are historical model versions/settings, not evidence about every present or future version. Different decoding settings limit direct between-model interpretation. | PENDING_VERIFICATION |
| C004 | In the oracle setting, known correctness stops correction of a correct response. Table 2 reports initial→oracle-assisted scores of 75.9→84.3, 75.8→89.7, and 26.0→29.0 for GPT-3.5, and 95.5→97.5, 82.0→85.5, and 49.0→59.0 for GPT-4, respectively on GSM8K, CommonSenseQA, and HotpotQA. | Printed/PDF pp. 3–4, §3.2; p. 4, Table 2. | Experimental result and protocol analysis. | Ground-truth stopping is external assistance. These gains do not demonstrate label-free intrinsic self-correction. Use each model's sample sizes from C002. | PENDING_VERIFICATION |
| C005 | Without the oracle, Table 3 initial→second-round scores are 75.9→74.7, 75.8→41.8, and 26.0→25.0 for GPT-3.5, and 95.5→89.0, 82.0→80.0, and 49.0→43.0 for GPT-4 on GSM8K, CommonSenseQA, and HotpotQA respectively. GPT-4 HotpotQA is 49.0 after round one, equal to its initial score. | Printed/PDF p. 4, Table 3 and §3.3. | Experimental result. | All final-round cells are lower, but not every intermediate cell falls. Two rounds require five calls versus one initially; these are reported scores, not a general impossibility result or an independently established significance test. | PENDING_VERIFICATION |
| C006 | Table 4 initial→first→second-round scores for GPT-4 Turbo are 91.5→88.0→90.0 on GSM8K and 84.0→81.5→83.0 on CommonSenseQA. For Llama-2 they are 62.0→43.5→36.5 and 64.0→37.5→36.5 respectively. | Printed/PDF p. 5, Table 4; §3.3. | Experimental result. | Temperature 0 and 200-example evaluation samples; some recovery between rounds does not exceed the initial baseline. No HotpotQA values appear in this table. | PENDING_VERIFICATION |
| C007 | Tables 5–6 test three feedback formulations. None of their reported first- or second-round scores exceeds the corresponding initial baseline. For example, the formulation requesting verification and an explanation gives GPT-4 Turbo 91.0/83.5 in round two on GSM8K/CommonSenseQA, versus initial 91.5/84.0; Llama-2 gives 41.5/43.0 versus initial 62.0/64.0. | Printed/PDF p. 5, Tables 5–6; §3.3 discussion across pp. 4–6. | Prompt-sensitivity experiment. | This covers the tested formulations and settings only, not all possible prompts. The slash separates two datasets, not a ratio. | PENDING_VERIFICATION |
| C008 | The answer-transition analysis reports that correct-to-incorrect changes outnumber incorrect-to-correct changes for GPT-3.5 on GSM8K, while 74.7% of initial answers remain unchanged. The authors suggest that feedback can bias revisions away from initially good answers. | Printed/PDF pp. 5–6, §3.3 analysis and Figure 1. | Descriptive error analysis and author interpretation. | The proposed bias mechanism is an interpretation, not a separately isolated causal effect. HotpotQA transition analysis is omitted because of the small sample (p. 5 footnote). The 74.7% unchanged-answer rate is a transition measure, distinct from the coincidentally equal final accuracy in Table 3. | PENDING_VERIFICATION |
| C009 | With gpt-3.5-turbo-0301, three agents, and two debate rounds on all 1,319 GSM8K test questions, Table 7 reports debate accuracy 83.2 using six responses and 83.0 using nine; majority-vote self-consistency scores 85.3 and 88.2 with six and nine responses respectively. The one-response baseline is 76.7; three-response self-consistency is 82.5. | Printed/PDF p. 7, §4 and Table 7. | Controlled response-count comparison. | The matched resource is generated response count, not token count or elapsed runtime. Same-model agents and this benchmark/settings do not represent every form of independent verification or debate. | PENDING_VERIFICATION |
| C010 | On CommonGen-Hard (20–30 required concepts), Table 8 reports concept coverage of 53.0 initially and 61.1 after correction when reproducing earlier prompts. With the authors' stronger initial instruction to include all concepts, coverage is 81.8 with one call and 75.1 with self-correction using seven calls. | Printed/PDF pp. 7–8, §5; p. 7, Table 8; p. 17, Figures 7–8 prompt illustrations. | Prompt-design experiment. | Uses gpt-3.5-turbo-0613. Coverage is not factuality or overall writing quality. Table 8 separately includes earlier published 44.0/67.0 scores marked with asterisks; those are not this study's replication values. Strengthening the initial prompt changes the comparison conditions. | PENDING_VERIFICATION |
| C011 | The authors recommend identifying external feedback explicitly, comparing against strong self-consistency baselines with fair resource budgets, and applying comparable effort to initial and feedback prompts. | Printed/PDF p. 8, §6, three recommendations. | Author interpretation and methodological recommendation. | Recommendations are informed by these experiments. References to successes of other external-feedback methods are literature discussion, not independent evaluations conducted here. | PENDING_VERIFICATION |
| C012 | The authors delimit their main conclusions to the difficulty of intrinsic self-correction for reasoning in the studied models/settings; they acknowledge that other domains and forms of feedback can behave differently. | Printed/PDF p. 2, scope/definition; pp. 8–9, §§6–7. | Author-stated scope and conclusion. | No proof of impossibility for future models, all tasks, or externally checked correction. The reasoning scores do not directly measure open-ended factual hallucinations. | PENDING_VERIFICATION |

## 7. Author Conclusions

The authors conclude that the studied models struggle to correct reasoning intrinsically and can degrade after feedback. They attribute apparently favorable comparisons in part to oracle assistance, unequal response budgets, or weaker initial prompts (C004–C010). Their methodological recommendations are author interpretations (C011); examples and discussion of other domains do not establish new empirical results in this paper (C012). No future universal inability is established.

## 8. Research Limitations

AUTHOR_REPORTED_LIMITATIONS: The central scope is reasoning and intrinsic correction (C001, C012). Model evaluations use different sample sizes and specific access dates/settings (C002–C003). The authors omit HotpotQA transition analysis because the sample is small (C008). Their discussion explicitly allows that correction in other domains or with external feedback may differ (C012).

ADDITIONAL_OBSERVATIONS: Differences in decoding settings and evaluation samples mean the tables should not be used as clean causal comparisons between model families (C002–C003). Equal response count does not establish equal token or wall-clock cost (C009). The constrained-generation coverage outcome cannot establish factual hallucination reduction (C010). These are summarizer cautions grounded in the reported design, not limitations quoted as the authors' own wording.

## 9. Relevance to Assignment

This article supplies a contextual test of internal correction and a direct comparison with self-consistency, useful when examining whether additional model responses constitute reliable checking (C004–C009). It also helps distinguish independent external evidence from model-produced feedback and oracle labels (C001, C004, C011). Its evidence cannot be substituted for a study of open-ended factual hallucinations; relevance to that assignment is methodological and qualified (C012). No thesis or synthesis is proposed here.

## 10. Questions and Uncertainties

- The official PDF text was available, including tables and appendices. Screenshot calls did not return viewable images; no unlabelled plot heights were estimated. Figure 1 extraction is limited to values and interpretation explicitly stated in the accompanying text (C008).
- The claim table preserves numerical tables over an overbroad reading that every intermediate correction round reduces performance (C005).
- Generalization beyond the sampled tasks, model versions, and tested prompts remains unestablished (C002–C003, C007, C012).
- No conference DOI was confirmed. The arXiv DOI must remain identified as repository-specific.
- Every claim requires an independent verifier's comparison with the original; none is declared VERIFIED here.

## 11. Summary Status

COMPLETE for the assigned publication; pending independent verification. Six key findings and twelve evidence claims (C001–C012), all PENDING_VERIFICATION. Full-text access obtained; no content access blocker remains. Completed 2026-11-13 (UTC). Original text, references, methodology/results, and appendices inspected; no other publications researched and no other agent's files modified.
