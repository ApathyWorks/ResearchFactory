# Research candidates: Independent verification and self-correction limitations

## Scope and procedure

Phase 1 only, for the research question and constraints in [assignment.md](../../assignment.md): a 1,200-word, APA 7 demonstration comparing consistency checking, independent verification, and evidence-based fact-checking. Sources must be scholarly and peer reviewed; limitations and opposing findings matter. No publication-date cutoff is specified. The assignment permits the AI-generated demonstration subject to the enclosing assignment's rules. No substantive evidence has been extracted or independently verified here.

Owner: researcher agent `/root/independent_verification`. Report slug: `independent-verification`. All permanent source IDs remain UNASSIGNED for coordinator allocation. This report evaluates discovery relevance and bibliographic/access information, not the validity of experimental findings.

## Searches and sources

Searches on 2026-11-10 included:

- `site.aclanthology.org "Chain-of-Verification Reduces Hallucination"` (initial query used this literal spelling; direct official record subsequently opened).
- `site:openreview.net "Large Language Models Cannot Self-Correct Reasoning Yet"`
- `site:aclanthology.org "Intrinsic Self-Correction" language models`
- `site:openreview.net/forum "Large Language Models Cannot Self-Correct Reasoning Yet"`
- `"Large Language Models Cannot Self-Correct Reasoning Yet" arxiv DOI`
- `site:proceedings.iclr.cc "Large Language Models Cannot Self-Correct Reasoning Yet"`

Primary records inspected: ACL Anthology publisher pages and PDFs, ICLR proceedings and PDF, arXiv metadata, and indexed OpenReview acceptance metadata. Search-result mirrors and general websites were not used as bibliographic authorities. Moral self-correction/detoxification hits were not promoted to candidates because they address a different outcome from factual hallucination. No duplicate publication was retained within this three-candidate report; preprint and conference versions are treated as versions of the same work.

## Candidate publications

### CAND-independent-verification-001

- Existing Source ID: UNASSIGNED
- Title: Chain-of-Verification Reduces Hallucination in Large Language Models
- Authors: Shehzaad Dhuliawala; Mojtaba Komeili; Jing Xu; Roberta Raileanu; Xian Li; Asli Celikyilmaz; Jason Weston
- Publication year: 2024
- Venue: Findings of the Association for Computational Linguistics: ACL 2024, pp. 3563–3578; Association for Computational Linguistics
- DOI: [10.18653/v1/2024.findings-acl.212](https://doi.org/10.18653/v1/2024.findings-acl.212)
- Publisher URL: [ACL record](https://aclanthology.org/2024.findings-acl.212/)
- Open-access URL: [Publisher PDF](https://aclanthology.org/2024.findings-acl.212.pdf)
- Publication type: Original conference findings paper
- Peer-reviewed status: CONFIRMED; published in ACL Findings proceedings
- Access status: FULL_TEXT; publisher PDF successfully opened, 16 pages, title/authors and proceedings header inspected
- Relevance score: High
- Research relevance: Directly addresses the assignment's independent-verification category. It is a suitable anchor for assessing the suggested publication rather than assuming its title establishes effectiveness.
- Potential contribution: A method-specific comparator for later evidence extraction.
- Limitations: Context-separated model answers must not automatically be equated with independent external evidence. Methodological quality and numerical results remain unverified.
- Bibliographic verification: Title, author order, year, venue and pagination match publisher page/PDF; DOI appears in publisher metadata. Use the 2024 publication rather than counting the 2023 preprint separately.

### CAND-independent-verification-002

- Existing Source ID: UNASSIGNED
- Title: Large Language Models Cannot Self-Correct Reasoning Yet
- Authors: Jie Huang; Xinyun Chen; Swaroop Mishra; Huaixiu Steven Zheng; Adams Wei Yu; Xinying Song; Denny Zhou (PDF form)
- Publication year: 2024
- Venue: International Conference on Learning Representations (ICLR 2024)
- Pages: Proceedings page range not supplied; accessible paper has 17 internally numbered pages
- DOI: No conference DOI located in inspected primary records. [10.48550/arXiv.2310.01798](https://doi.org/10.48550/arXiv.2310.01798) is explicitly the arXiv-issued DOI, not a conference DOI.
- Publisher URL: [ICLR record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html)
- Open-access URL: [ICLR PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)
- Publication type: Original conference research/critical analysis
- Peer-reviewed status: CONFIRMED; ICLR proceedings, with [OpenReview acceptance record](https://openreview.net/forum?id=IkmD3fKBPQ) indexed as accepted poster
- Access status: FULL_TEXT; ICLR PDF opened successfully
- Relevance score: High
- Research relevance: Offers a critical comparison for self-correction assumptions. Its reasoning focus requires caution when applying it to factual hallucination.
- Potential contribution: Counterevidence and evaluation-design questions for later reading.
- Limitations: OpenReview direct access encountered a browser challenge; no bypass attempted. Public ICLR access succeeded.
- Bibliographic verification: Title/year/venue/authors checked against proceedings/PDF; [arXiv](https://arxiv.org/abs/2310.01798) verifies repository DOI. Proceedings HTML abbreviates Adams Wei Yu to Adams Yu; preserve PDF form and flag discrepancy for citation review.

### CAND-independent-verification-003

- Existing Source ID: UNASSIGNED
- Title: Understanding the Dark Side of LLMs’ Intrinsic Self-Correction
- Authors: Qingjie Zhang; Di Wang; Haoting Qian; Yiming Li; Tianwei Zhang; Minlie Huang; Ke Xu; Hewu Li; Yan Liu; Han Qiu (PDF form)
- Publication year: 2025
- Venue: Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 27066–27101; Association for Computational Linguistics
- DOI: [10.18653/v1/2025.acl-long.1314](https://doi.org/10.18653/v1/2025.acl-long.1314)
- Publisher URL: [ACL record](https://aclanthology.org/2025.acl-long.1314/)
- Open-access URL: [Publisher PDF](https://aclanthology.org/2025.acl-long.1314.pdf)
- Publication type: Original conference research paper
- Peer-reviewed status: CONFIRMED; ACL main-conference long paper
- Access status: FULL_TEXT; publisher PDF opened successfully, 36 pages
- Relevance score: High
- Research relevance: Provides a newer candidate addressing intrinsic self-correction failure cases. It can broaden the limitations discussion beyond one critical publication.
- Potential contribution: Alternative explanations and boundary conditions for later assessment.
- Limitations: No result-level verification performed. Bibliographic author discrepancy needs preservation.
- Bibliographic verification: Title/year/venue/pages/DOI checked against publisher record and PDF header. HTML/BibTeX list ninth author as Liu Yan (BibTeX `Yan, Liu`), whereas PDF says Yan Liu. ACL explicitly treats PDFs as authoritative; use PDF display form provisionally and recheck family-name parsing before APA references.

## Ranked recommendations and screening handoff

1. CAND-independent-verification-001: Recommend acceptance as the directly relevant suggested publication, using its peer-reviewed 2024 version.
2. CAND-independent-verification-002: Recommend acceptance as a critical comparator; retain the reasoning-versus-factuality scope qualification and distinguish its repository DOI.
3. CAND-independent-verification-003: Recommend acceptance as a newer limitations candidate, with the author metadata discrepancy carried forward.

These are research recommendations, not an approved thesis or evidence synthesis. All three are unique within this report; the coordinator must deduplicate against other research reports before source-ID assignment.

## Access limitations, gaps, and logging handoff

- Candidate publications: 3; recommended: 3; accessible full text: 3; requiring manual full-text access: 0. No local PDFs downloaded; the linked publisher PDFs were opened through the web tool.
- OpenReview browser challenge was respected. ICLR's independently public proceedings copy supplied full text without authentication.
- DOI gaps: no conference DOI found for candidate 002; repository DOI verified and clearly labeled. A missing conference DOI is not evidence that one cannot exist.
- Metadata discrepancies: candidate 002 middle name abbreviation; candidate 003 ninth-author name order. Neither prevents publication identity matching, but neither should be silently discarded.
- This targeted search is not a systematic review or an exhaustive search through 2026. Evidence-based external fact-checking is delegated elsewhere; candidate selection does not establish whether methods work.
- No detailed summaries, extracted claims, verification reports, synthesis, outline, or draft were created. No claims have VERIFIED status.
- Observation timestamps: work was underway by 2026-11-10T19:00:48Z (clock observation); report preparation began by 2026-11-10T19:01:14Z. Exact task-start timestamp is NOT_RECORDED here; the coordinator may use its observed delegation time. Final handoff timestamp should be recorded by the coordinator on receipt.
