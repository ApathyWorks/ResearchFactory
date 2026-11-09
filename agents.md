
# Academic Research Orchestration

## Purpose

Coordinate specialized Codex agents to support academic research,
evidence verification, synthesis, outlining, and manuscript review.

The human author retains responsibility for:
- Research direction and interpretation
- Thesis selection
- Academic integrity
- Compliance with assignment AI-use policies
- Final writing decisions and submission

Never submit an assignment automatically.

## General Rules

1. Read the assignment requirements before beginning.
2. Follow the assignment's AI-use and academic-integrity rules.
3. Use scholarly, credible, and relevant sources.
4. Never fabricate sources, quotations, citations, or findings.
5. Never treat an AI-generated summary as verified evidence.
6. Preserve source traceability using unique source and claim IDs.
7. Respect copyright, licensing, and access restrictions.
8. Never bypass institutional authentication or paywalls.
9. Do not overwrite existing human edits without approval.
10. Stop and request human input when essential information
    is missing or important decisions cannot be resolved.

## Agent Responsibilities

- researcher: Find and evaluate relevant scholarly publications.
- summarizer: Extract findings from individual publications.
- verifier: Independently verify findings against original sources.
- synthesizer: Compare verified evidence across publications.
- outliner: Develop a structured outline from approved research.
- citation_auditor: Audit manuscript citations and source support.
- peer_reviewer: Critically evaluate argument quality and structure.
- drafter: Write the complete academic manuscript using the approved outline and independently verified evidence.

## File Ownership

All work must remain inside the assigned paper directory.

Specialist agents must write to their designated output files.

The coordinating agent is the only agent permitted to update
the shared evidence-matrix.md.

Agents must not modify another agent's reports.
Integration may read specialist outputs and write a separately owned
consolidated artifact, preserving the input files unchanged. Assign one
writer per output file; existing human edits still require approval.

Use stable identifiers:
- **Source IDs:** `SRC-001`, `SRC-002`, etc.
- **Local claim IDs:** The summarizer assigns `C001`, `C002`, etc.,
  unique within each source's summary.
- **Global claim IDs:** The verifier prefixes the permanent source ID,
  producing IDs such as `SRC-001-C001`. Use these global IDs in verification
  reports, the evidence matrix, synthesis, outlines, and manuscript evidence
  mappings.
- Preserve each claim's local ID and its global mapping through corrections
  and subsequent reviews. Different sources may each contain `C001`;
  their global IDs remain distinct.

Only the coordinating agent may allocate permanent source IDs.
Researchers use temporary candidate IDs: CAND-<report-slug>-001, etc.
The coordinator supplies a unique report slug for each research task.

## Demonstration Workflow Logging

The coordinator alone owns workflow-log.md inside the assigned paper
directory. Create this single chronological Markdown log when the research
workflow begins, not during configuration maintenance.

Record observed task assignments and completions, AI agent contributions,
sources used, verification outcomes, human approvals and interventions,
and outstanding issues. Use timezone-qualified timestamps and these columns:

| Date/time | Actor | Action/contribution | Source/claim IDs | Artifact links | Outcome/outstanding issues |
| --- | --- | --- | --- | --- | --- |

Link to research reports, evidence-matrix.md, and review reports rather than
duplicating their evidence records. The evidence matrix remains the
authoritative evidence index. Specialists supply logging information through
their handoffs and must not edit the shared log.

Preserve earlier entries and human edits; append corrections referencing the
affected entries. Record only observed actions and explicit human decisions;
never infer approvals. Identify unavailable logging details as gaps rather
than inventing history.

---

## Phase 1: Research

1. Read assignment.md and identify:
   - Research questions
   - Required topics
   - Source requirements
   - Citation style
   - Evaluation criteria
   - AI-use restrictions

2. Delegate literature searches to researcher agents.

3. Run independent searches in parallel when beneficial.

4. Search scholarly databases and reputable research sources.

5. Collect bibliographic metadata, DOIs, and accessible
   publications.

6. The coordinator eliminates irrelevant sources and deduplicates candidates
   across research reports and against the existing source register, using
   DOI first, then canonical URL and bibliographic metadata. Ambiguous
   matches remain unresolved until clarified; do not assign them new IDs.

7. The coordinator alone assigns permanent source IDs. Reuse the existing
   ID for a matching publication. For new publications, assign IDs
   sequentially above the highest previously assigned number, starting at
   SRC-001 if none exist. Template examples are not assigned IDs.
   Never renumber existing IDs or recycle an assigned ID for another source.
   Include candidate-to-permanent-ID mappings in delegation handoffs
   without editing researcher reports.

8. Record source access status:
   - FULL_TEXT
   - ABSTRACT_ONLY
   - METADATA_ONLY
   - RESTRICTED

9. Present a research inventory and identify access limitations.

Do not claim full-text access when only an abstract or metadata
is available.

## Phase 2: Evidence Extraction

1. Delegate individual articles to summarizer agents with their
   coordinator-assigned permanent source IDs and bibliographic metadata.

2. Store summaries separately under summaries/.

3. Assign completed summaries to verifier agents.

4. Verifiers must independently inspect original publications.

5. Verify claims, numerical results, quotations, and limitations.

6. Classify findings:
   - VERIFIED
   - PARTIALLY_SUPPORTED
   - UNSUPPORTED
   - UNVERIFIABLE

7. Request corrections for inaccurate summaries.

8. Retry failed verification a maximum of twice.

9. Leave unresolved claims unverified.

10. Have the coordinator update evidence-matrix.md.

Only VERIFIED claims may support the final synthesis,
outline, and manuscript.

If essential source material is inaccessible, request
human assistance rather than inventing findings.

## Phase 3: Synthesis

Delegate synthesis to the synthesizer agent.

For parallel synthesis, assign each specialist a unique
research/synthesis-<topic-slug>.md file. After all reports are stable,
the coordinator creates the consolidated research/synthesis.md using
the required synthesis structure and VERIFIED evidence only. Preserve
the specialist reports unchanged, retain their paths and claim mappings,
and flag unresolved disagreements rather than silently resolving them.
In a single-agent run, the synthesizer owns research/synthesis.md instead;
never assign both ownership modes concurrently.

1. Compare verified findings across publications.
2. Identify agreements and disagreements.
3. Evaluate research quality and methodological limitations.
4. Identify gaps in available evidence.
5. Distinguish established findings from tentative conclusions.
6. Develop possible thesis statements.
7. Explain the evidence supporting each proposed thesis.

Output:
research/synthesis.md

### HUMAN APPROVAL REQUIRED

Present:
- Research findings
- Evidence gaps
- Proposed thesis statements
- Recommended research direction

Wait for approval of the thesis and research direction
before proceeding.

## Phase 4: Organization

Delegate outlining to the outliner agent.

1. Read the approved thesis.
2. Review assignment requirements and rubric.
3. Create a detailed paper outline.
4. Map VERIFIED claims to individual sections.
5. Identify gaps requiring additional research.
6. Check the outline against assignment requirements.
7. Identify expected counterarguments and limitations.

Output:
outline.md

### HUMAN APPROVAL REQUIRED

Present the outline for review.

Wait for approval before beginning drafting assistance.

## Phase 5: Writing

Delegate manuscript creation to the drafter agent.

1. Read the approved thesis and outline.
2. Read assignment requirements and AI-use restrictions.
3. Consult the research synthesis and evidence matrix.
4. Write a complete academic manuscript.
5. Support factual assertions with VERIFIED claims.
6. Include appropriate in-text citations and references.
7. Preserve counterarguments, limitations, and uncertainty.
8. Respect the assignment's word count and citation style.

Output:
draft.md

The Drafter must not modify the evidence matrix or
independent review reports.

Proceed to independent reviews after drafting is complete.

For explicitly requested parallel drafting, assign each drafter a distinct
draft-sections/<section-slug>.md file and only its approved outline sections.
After all sections are stable, one coordinator-designated drafter integrates
them into draft.md, preserving section files unchanged. The integrator checks
the complete manuscript's argument, citations, references, evidence mappings,
and length before review. Approval gates apply equally to section drafting.

## Phase 6: Independent Review

After a stable draft is available:

1. Run citation_auditor against the manuscript and sources.
2. Run peer_reviewer against the manuscript and rubric.
3. Allow independent reviews to run in parallel against the same stable
   manuscript version. Record that version in both reports.
4. Collect both reports. If peer review records the citation audit as PENDING,
   send the completed audit back to the peer reviewer for a follow-up on the
   same manuscript version. The peer reviewer updates only its own report,
   incorporates audit findings, and reassesses its verdict; PASS requires a
   passing citation audit and satisfaction of all peer-review criteria.
5. If the manuscript changed, rerun both reviews on the new stable version
   under the revision-cycle limits. A dependency-only follow-up on an
   unchanged manuscript is part of the same review cycle, not a revision.
6. Consolidate the final reports into a prioritized revision list.

Outputs:
- reviews/citation-audit.md
- reviews/peer-review.md

Review agents must not directly modify the manuscript.

## Phase 7: Revision

1. Review all findings from both auditors.
2. Prioritize BLOCKER and critical issues.
3. Identify changes requiring human decisions.
4. Propose corrections supported by verified evidence.
5. Apply only revisions authorized by the human author
   and permitted by assignment rules.
6. Preserve unresolved concerns in the review reports.
7. Rerun both reviews after substantive revisions.
8. Perform a maximum of two revision-review cycles.

Do not silently downgrade unresolved findings.

If blocking issues remain after two cycles,
stop and request human direction.

### HUMAN APPROVAL REQUIRED

Present the revised manuscript and outstanding issues.

Wait for final human approval.

---

## Completion

Report:

- Total sources collected
- Sources with verified full-text evidence
- Verified and unresolved claim counts
- Evidence gaps and limitations
- Completed research artifacts
- Workflow log path and unresolved logging gaps
- Citation audit outcome
- Peer review outcome
- Outstanding human decisions
- Final manuscript readiness

A completed automated workflow does not mean the
paper is approved for submission.

Never submit the paper automatically.
