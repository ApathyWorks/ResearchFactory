# Academic Article Summary

## 1. Bibliographic Information
- Source ID: SRC-011
- Title: RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models
- Authors: Cheng Niu, Yuanhao Wu, Juno Zhu, Siliang Xu, Kashun Shum, Randy Zhong, Juntong Song, and Tong Zhang. The inventory notes the publisher capitalization variant KaShun Shum.
- Publication Year: 2024
- Journal or Conference: Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 10862–10878.
- DOI: https://doi.org/10.18653/v1/2024.acl-long.585
- Original Publication URL: https://aclanthology.org/2024.acl-long.585/ ; full text: https://aclanthology.org/2024.acl-long.585.pdf
- Local Document Path: None used; original publisher PDF inspected online.
- Access Status: FULL_TEXT. Publisher PDF contains 17 pages, including appendices A–D. ACL's copyright policy states that ACL works from 2016 onward use CC BY 4.0: https://aclanthology.org/faq/copyright/ . No applicable prohibition on this processing was identified.

## 2. Research Overview
The authors construct an annotated corpus of naturally generated responses to reference-grounded tasks and evaluate hallucination detectors and detector-guided response selection (C001–C005, C009). The relevant outcome is fidelity to the supplied context: unsupported content may receive a hallucination label even if it is true outside that context (C001). Fine-tuning a smaller model produces stronger aggregate detection F1 than the tested prompting and consistency baselines, while detection remains imperfect (C007–C008). Filtering can reduce the hallucination rate among retained responses, with a coverage tradeoff (C010–C011).

## 3. Research Questions
The following are paraphrased research objectives, not verbatim formal hypotheses:

- Build a corpus with response-level and span-level human annotations for grounded generation (C001–C004).
- Compare prompting, sampled-output consistency, cross-examination, and supervised fine-tuning for detecting context-unfaithful content (C005–C008).
- Test whether detector-guided selection between candidate outputs reduces labeled hallucinations (C009–C011).

Formal null/alternative hypotheses: Not reported in the relevant methods and experiments. The broader motivation is operationalized by these corpus and evaluation objectives; no final assignment thesis is proposed here.

## 4. Methodology
The corpus covers question answering using MS MARCO passages, data-to-text writing using Yelp business information and reviews, and news summarization using CNN/DailyMail and recent news. Six models produce a response to each input; the Llama-2-70B model uses 4-bit quantization (C002). Human annotators label hallucinations with a four-part taxonomy; two annotators initially assess each response and a third reviews substantial disagreements (C001, C004).

The test split contains 450 inputs, 150 per task, with remaining inputs used for training. Evaluations compare prompt-based GPT detectors, SelfCheckGPT with three additional outputs and a GPT-3.5 evaluator, LMvLM cross-examination, and fully fine-tuned Llama-2-13B (C005). Response-level precision, recall, and F1 measure detection; span-level metrics use character overlap rather than exact-span matching (C006). A separate experiment selects between two candidate responses according to predicted spans, including a policy that may return no response (C009).

Confidence intervals and repeated-run uncertainty for the principal Tables 5–7 results: Not reported in those tables. No causal or deployment-wide effectiveness claim is inferred from this evaluation.

## 5. Key Findings
1. Context-relative annotation matters: an unsupported but potentially true statement can be labeled a hallucination; special labels retain that distinction (C001; printed pp. 10864–10866).
2. The corpus contains 17,790 responses and 14,289 labeled spans; 7,664 responses contain hallucinations under this policy (C003; Table 2, p. 10867).
3. Annotation agreement is higher at response level than span level: 91.8% versus 78.8% (C004; p. 10865).
4. Fine-tuned Llama-2-13B has aggregate response F1 78.7, compared with 63.4 for prompted GPT-4-turbo and 58.8 for the evaluated SelfCheckGPT implementation. GPT-4-turbo has higher recall, so the advantage is not uniform across metrics (C007; Table 5, p. 10868).
5. Fine-tuned Llama-2-13B also has higher aggregate character-overlap span F1, 52.7 versus 28.3 for prompted GPT-4-turbo, while its recall is lower (C008; Table 6, p. 10868).
6. For the Llama-2-7B/Mistral-7B candidate pair, selecting fewer predicted spans reduces the hallucination rate from the random-selection baseline of 52.4% to 41.1%; zero-span filtering reduces it to 19.3% while retaining only 328 of 450 responses (C010; Table 7, p. 10869).
7. For the GPT-3.5/GPT-4 pair, the corresponding rates are 9.8%, 5.6%, and 4.8%, with the zero-span policy retaining 448 of 450 responses (C011; Table 7, p. 10869).

## 6. Evidence Table
Local claim IDs below map to global IDs by prefixing SRC-011-, for example C001 becomes SRC-011-C001. PDF page numbers are one-based; printed page 10862 is PDF page 1.

| Claim ID | Claim | Source Location | Evidence Type | Qualifications | Verification Status |
| --- | --- | --- | --- | --- | --- |
| C001 | The annotation scheme distinguishes evident/subtle conflict and evident/subtle introduction of baseless information. Its strict reference-grounding policy can label potentially true unsupported content as hallucinated, preserving an implicit_true flag; treating JSON null as false is tagged due_to_null. | Printed pp. 10864–10866, sections 3.1 and 3.4 (PDF pp. 3–5); Appendix A/Table 8 p. 10874 (PDF p. 13); Appendix C/Table 10 p. 10877 and Appendix D/Table 11 p. 10878 (PDF pp. 16–17). | Dataset definition and annotation policy | Labels concern support in the supplied material, not necessarily external factual falsity. Null represents missing information, not negation. | PENDING_VERIFICATION |
| C002 | Inputs comprise daily-life QA sampled from MS MARCO training data with three retrieved passages, Yelp restaurant/nightlife business data with up to three reviews, and CNN/DailyMail training plus recent-news summarization. One response per input is obtained from GPT-3.5-turbo-0613, GPT-4-0613, Mistral-7B-Instruct, and Llama-2-7B/13B/70B-chat; the 70B model is 4-bit quantized. | Printed pp. 10864–10865, section 3.2 (PDF pp. 3–4); generation prompts Appendix B/Table 9 p. 10875 (PDF p. 14). | Dataset construction and experimental setup | Task/model selection constrains generalizability; generation prompts are adapted slightly across models. Quantization qualifies comparisons involving the 70B model. | PENDING_VERIFICATION |
| C003 | Table 2 reports 2,965 inputs, 17,790 responses, 7,664 hallucinated responses (43.1%), and 14,289 spans. Task response counts/rates are QA 5,934/29.1%, data-to-text 6,198/68.6%, CNN/DailyMail 3,768/30.9%, and recent news 1,890/27.6%. | Printed pp. 10866–10867, section 4.1 and Table 2 (PDF pp. 5–6). | Descriptive corpus statistics | Percentages use the paper's annotation policy; they are not estimates of all RAG deployment error rates. Data-to-text is highest within these sampled tasks. | PENDING_VERIFICATION |
| C004 | Each response is independently assessed by two professional annotators; a third reviews substantial disagreement. Reported agreement is 91.8% at response level and 78.8% at span level. | Printed p. 10865, section 3.3 (PDF p. 4). | Annotation methodology and reliability result | These are the paper's agreement percentages, not chance-corrected kappa values. Agreement does not establish infallible ground truth. | PENDING_VERIFICATION |
| C005 | Detectors include prompted GPT-3.5-turbo/GPT-4-turbo, SelfCheckGPT using three additional same-model responses and GPT-3.5 consistency evaluation, LMvLM cross-examination, and fully fine-tuned Llama-2-13B. The test split uses 450 randomly chosen inputs, 150 per task; remaining inputs train the model, with learning rate 2e-5 for one epoch on four A100 GPUs. | Printed pp. 10867–10868, sections 5.1–5.2 (PDF pp. 6–7); Appendix D/Table 11 p. 10878 (PDF p. 17). | Experimental methodology | These are this paper's implementations and split; supervised fine-tuning has labeled training data unavailable to the prompting baselines. SelfCheckGPT sentence decisions are aggregated for response evaluation. | PENDING_VERIFICATION |
| C006 | Response detection is evaluated with precision, recall, and F1; span evaluation uses overlap of characters in predicted and annotated hallucination spans. | Printed p. 10868, section 5.3, Tables 5–6 and Table 6 caption (PDF p. 7). | Evaluation definition | Span F1 is not exact-span-match accuracy. Response and span measures answer different questions. | PENDING_VERIFICATION |
| C007 | Overall response precision/recall/F1 are 76.9/80.7/78.7 for fine-tuned Llama-2-13B, 46.9/97.9/63.4 for prompted GPT-4-turbo, 37.1/92.3/52.9 for prompted GPT-3.5-turbo, 49.7/71.9/58.8 for SelfCheckGPT, and 36.2/77.8/49.4 for LMvLM. | Printed p. 10868, Table 5 (PDF p. 7). | Experimental result | Values are percentage-scale metrics for this test split. Fine-tuning has the highest aggregate F1 among these methods, but GPT-4 prompting has higher recall. No uncertainty interval is supplied in the table. | PENDING_VERIFICATION |
| C008 | Overall character-overlap span precision/recall/F1 are 55.6/50.2/52.7 for fine-tuned Llama-2-13B, 18.4/60.9/28.3 for prompted GPT-4-turbo, and 7.8/35.3/12.8 for prompted GPT-3.5-turbo. | Printed p. 10868, Table 6 (PDF p. 7). | Experimental result | Fine-tuning improves aggregate F1 and precision over these baselines, but not recall over GPT-4-turbo. Substantial detection errors remain; no exact-span accuracy claim follows. | PENDING_VERIFICATION |
| C009 | Suppression experiments choose between two model responses using the fine-tuned detector: select fewer predicted hallucinated spans or accept only a response with no predicted spans; ties are random, and zero-span selection can reject both responses. | Printed p. 10869, sections 6.1–6.2 and Table 7 (PDF p. 8). | Mitigation procedure | This is candidate selection/filtering, not rewriting or proof that retained responses are correct. Coverage changes under rejection. | PENDING_VERIFICATION |
| C010 | For Llama-2-7B/Mistral-7B candidates, random selection yields 450 responses at 52.4% hallucination; fewer-span selection yields 450 at 41.1%; zero-span selection yields 328 at 19.3%. The table reports relative reductions of 21.6% and 63.2% against random selection. | Printed p. 10869, Table 7, Group 1 (PDF p. 8). | Experimental mitigation result | Reductions are relative percentages, not percentage-point changes. The 19.3% rate is conditional on the 328 retained responses, not all 450 inputs. | PENDING_VERIFICATION |
| C011 | For GPT-3.5/GPT-4 candidates, random selection yields 450 responses at 9.8% hallucination; fewer-span selection yields 450 at 5.6%; zero-span selection yields 448 at 4.8%. Reported relative reductions are 42.9% and 51.0%. | Printed p. 10869, Table 7, Group 2 (PDF p. 8). | Experimental mitigation result | Test-subset rates differ from full-corpus counts. Relative reductions and retained-response denominators must be preserved; hallucinations are not eliminated. | PENDING_VERIFICATION |
| C012 | The authors identify generalization to other datasets and contexts as requiring further benchmarking and propose evaluating manual versus synthetic annotation and their combination. | Printed p. 10870, section 8, Limitations (PDF p. 9). | Author-reported limitation and future work | Cross-domain superiority and the relative value of alternative annotation mixtures are not established by the present experiments. | PENDING_VERIFICATION |

## 7. Author Conclusions
The authors interpret the detection experiments as evidence that this manually annotated corpus can support an effective smaller fine-tuned detector; the reported aggregate F1 comparisons support that claim for the evaluated setup (C007–C008). Their selection experiments show lower labeled hallucination rates among selected outputs, subject to the stated coverage conditions (C009–C011). Broader transfer and annotation-mixture benefits remain future evaluation questions, not established results (C012).

## 8. Research Limitations
**AUTHOR_REPORTED_LIMITATIONS:** Broader generalization requires benchmarking; comparative evaluation of manual and synthetic annotations and their combination remains open (C012).

**ADDITIONAL_OBSERVATIONS:** These are summarizer interpretations, not attributed to the authors: the annotation policy makes source faithfulness distinct from real-world truth (C001); finite task/model coverage limits extrapolation (C002); span disagreement and imperfect detector precision/recall caution against treating automated checking as conclusive (C004, C007–C008); filtering changes the population on which success is measured (C010–C011). The supervised-versus-prompted comparison does not isolate architecture or model size as the causal source of the F1 difference (C005).

## 9. Relevance to Assignment
The paper provides within-study comparisons of sampled-output consistency, cross-examination, and reference-grounded detection (C005–C008), relevant to the assignment's comparison of hallucination-reduction strategies. It also supplies a concrete mitigation example with both rate and coverage information (C009–C011). It should not be used as evidence that every independent verifier or every evidence-checking system achieves these results. The context-faithfulness distinction and remaining false detections offer qualifications for later analysis; this summary does not select a thesis.

## 10. Questions and Uncertainties
- Verification should check every compound numerical row against the original tables, especially metric order and filtering denominators.
- The broad cross-model wording in section 4.2 should not be converted into an unqualified claim that GPT-4 has the lowest count by every metric. No such claim is extracted here; the principal results selected are Tables 5–7.
- Original PDF text and tabular contents were readable. A PDF screenshot request returned no inspectable image; precise plot estimates and image-only interface details are therefore not extracted. Relevant appendix text, taxonomy examples, prompts, and label statistics were inspected.
- Independent verification is outstanding. All evidence records remain pending, including methodological and limitation records.

## 11. Summary Status
COMPLETE for the selected substantive evidence: 7 key findings and 12 evidence claims (C001–C012), all PENDING_VERIFICATION. Full-text access available; no source-content access barrier was encountered. Independent verifier review is required before any claim advances. Only this assigned summary file was created.
