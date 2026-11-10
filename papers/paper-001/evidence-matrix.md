# Academic Paper Evidence Matrix

> Reusable template. Replace the bracketed fields for each paper. This file is the **shared evidence index**, not a substitute for the original publications or independent verification reports.

## Paper information

| Field | Value |
| --- | --- |
| Paper title | [Title] |
| Course / assignment | [Course and assignment] |
| Research question | [Question] |
| Assignment file | `assignment.md` |
| Citation style | [APA 7 / other] |
| Last review date | [YYYY-MM-DD] |
| Matrix owner | Coordinating agent (human approval required for the paper) |

## Candidate-screening ledger

The coordinator alone maintains this ledger. Retain one row per candidate ID
from researcher reports, including rejected and duplicate records. Revising a
candidate does not create a new candidate ID. Template examples are not data.

| Candidate ID | Canonical publication identity (DOI, URL, bibliographic metadata) | Deduplication status | Duplicate of (candidate or existing source ID) | Screening decision | Reason / unresolved question | Research report link | Permanent source ID when assigned |
| --- | --- | --- | --- | --- | --- | --- | --- |

Deduplication statuses: UNIQUE, DUPLICATE, UNRESOLVED. Match DOI first, then
canonical URL and bibliographic metadata. For duplicates, point to one
representative candidate or an existing source ID; keep all original report
links and candidate IDs. Ambiguous matches remain UNRESOLVED and must not
receive new permanent IDs or be silently counted as unique publications.

Screening decisions: PENDING, ACCEPTED, REJECTED. Record a reason for every
decision. Screening and deduplication are separate: several candidate records
can refer to one accepted publication, which counts only once. Count raw
discoveries by distinct candidate IDs, confirmed unique discoveries by resolved
publication groups, and unresolved matches separately.

Use UNASSIGNED when no permanent source ID has been allocated. Rejected
candidates remain traceable here without receiving new permanent IDs. If a
publication already has a permanent ID, retain it even if later rejected;
never recycle or renumber it. For accepted publications, the coordinator
assigns or reuses IDs under AGENTS.md and records the mapping here and in
delegation handoffs without editing researcher reports.

Record screening changes and their reasons in the review and change log below.
The coordinator preserves measurement snapshots before changes so historical
screening totals remain traceable in workflow-metrics.md.

## 1. Source register

Add one row per unique publication. **Source IDs are permanent** once assigned. A DOI is preferred but may be unavailable for some legitimate sources. `FULL_TEXT` refers to permitted, accessible full text—not merely a publisher abstract.

| Source ID | Authors (year) | Article title | Journal / conference | DOI or canonical URL | Local full-text path | Access status | Peer-review status | Research relevance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

<!-- Example shape (do not treat as a real source): SRC-001 | [authors] ([year]) | [title] | [venue] | [DOI/URL] | sources/SRC-001.pdf | FULL_TEXT | Confirmed | [why relevant] -->

Allowed access statuses: `FULL_TEXT`, `ABSTRACT_ONLY`, `METADATA_ONLY`, `RESTRICTED`.

Allowed peer-review statuses: `CONFIRMED`, `NOT_PEER_REVIEWED`, `UNKNOWN`.

## 2. Claim-level evidence ledger

The Summarizer's local ID `C001` becomes the globally unique ID **`SRC-001-C001`**. Keep this ID stable through summarization, verification, synthesis, outlining, and citation audits. Record paraphrases in your own words; do not paste lengthy excerpts from copyrighted articles.

| Global Claim ID | Source ID | Claim (accurate paraphrase) | Original source locator | Evidence type | Critical qualifications | Verification status | Verification report | Intended paper section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

<!-- Example shape (not a real finding): SRC-001-C001 | SRC-001 | [claim] | Printed p. 6, Table 2 (PDF p. 8) | Experimental result | [conditions] | PENDING_VERIFICATION | reviews/verification/SRC-001.md | [section] -->

### Verification status definitions

| Status | Meaning | Eligible to support a draft claim? |
| --- | --- | --- |
| `PENDING_VERIFICATION` | Extracted by the Summarizer but not independently checked. | No |
| `VERIFIED` | Verifier inspected permitted full text and found direct support, including material qualifications. | Yes, subject to author review and proper citation |
| `PARTIALLY_SUPPORTED` | Evidence exists, but the claim or its qualifications need correction. | No, not until corrected and reverified |
| `UNSUPPORTED` | Original full text does not support the assertion as written. | No |
| `UNVERIFIABLE` | Source is inaccessible, illegible, insufficient, or the claim cannot be located reliably. | No |

**Rules for advancing claims:**

1. A summarization result enters the ledger as `PENDING_VERIFICATION`.
2. The Verifier writes a per-source report at `reviews/verification/SRC-###.md` and proposes status changes. It must not edit this matrix directly.
3. The coordinating agent merges statuses and corrected wording, retaining claim IDs and the report path.
4. Corrected claims that materially change meaning return to `PENDING_VERIFICATION` until independently rechecked.
5. Only `VERIFIED` claims may be proposed as evidence for the outline or manuscript. Verification still does not establish that a citation is formatted correctly or that the author's argument is sound.
6. Never convert `UNVERIFIABLE` into `UNSUPPORTED` simply because a document could not be accessed.

## 3. Cross-source synthesis

Record relationships *after* individual claims have been verified. Do not mistake multiple claims from the same study for independent corroboration.

| Theme or research question | Supporting global claim IDs | Contradicting or qualifying claim IDs | Evidence strength / caveats | Gap or next research action |
| --- | --- | --- | --- | --- |

## 4. Draft claim and citation mapping

This section is used by the Outliner, Writing Assistant (if permitted), and Citation Auditor. It links draft statements back to verified evidence rather than relying on plausible-sounding citations.

| Draft section | Draft assertion or intended argument | Supporting global claim IDs | Intended citation(s) | Citation audit status | Notes |
| --- | --- | --- | --- | --- | --- |

Citation audit statuses: `NOT_CHECKED`, `CHECKED`, `NEEDS_CORRECTION`, `NOT_APPLICABLE`.

## 5. Outstanding issues and manual access requests

| Issue ID | Related source / claim IDs | Problem | Owner | Next action | Status |
| --- | --- | --- | --- | --- | --- |

Possible issue statuses: `OPEN`, `IN_PROGRESS`, `RESOLVED`, `BLOCKED`.

Examples of issues to track: missing full text, a conflicting result, ambiguous PDF page numbering, a source's licensing restrictions, or a verifier's request for a better scan.

## 6. Review and change log

| Date (YYYY-MM-DD) | Agent / reviewer | Source or claim IDs affected | Change made | Supporting report or rationale |
| --- | --- | --- | --- | --- |

## Working conventions

- The **Researcher** creates source candidates and metadata; the coordinator adds approved sources to the register.
- The **Summarizer** writes `summaries/SRC-###.md` and extracts local claim IDs (`C001`, `C002`, ...).
- The **Verifier** independently checks the original source and writes `reviews/verification/SRC-###.md`.
- The **coordinating agent alone** merges verified records into this shared matrix to avoid concurrent edits.
- The **Synthesizer** works primarily from `VERIFIED` claims but can identify gaps and contradictions to investigate.
- The **Outliner** links sections to verified claim IDs; the **Citation Auditor** checks the eventual draft against the original publications and reference list.
- Human review is required before the thesis, interpretation, and final paper are accepted. Follow the specific course's policy on AI assistance.
- Follow publication licenses and access conditions. In particular, do not upload or process subscription-protected documents with AI when those terms prohibit it.
