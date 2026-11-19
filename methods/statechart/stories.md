## 1. 131-protein Atlas built (upstream sample binding unchecked)

Rule broken: Rule 3 (BROKEN today -> FIXED in v4): Upstream single-condition-per-sample gate must pass before building atlas/workbook.
Why: Atlas and workbook can be built before an automated upstream check blocks merged multi-condition sample cards (fixed manually for BARSTAR on 19 Nov, not yet blocked in v4 extractor).
In the model, one step leads into this bug: "Build 131-protein Atlas & 10-tab workbook [Program]".

0. Start: Open RelaxDB entry queued
1. Stage open full texts [Program: exclude 12 held-out entries]. Now: Open full texts staged (128/131 covered)
2. Extract paper into fixed JSON [Reader LLM: verbatim quotes]. Now: Paper JSON drafted (unverified)
3. Verify quotes & table rows [Program: 776/776 pass]. Now: Verbatim quotes & tables verified (776/776)
4. Check links, counts, leaks & diagrams [Program: fixed rules]. Now: Consistency gate passed (131 pages, 0 leaks, 9 method groups)
5. Build 131-protein Atlas & 10-tab workbook [Program]. Now: 131-protein Atlas built (upstream sample binding unchecked)

With v4 locked workflow, step 4 (Check links, counts, leaks & diagrams [Program: fixed rules]) cannot happen, so you stay at: Verbatim quotes & tables verified (776/776).

## 2. Promoted early (missing expert sign-off or backlog)

Rule broken: Rule 4 (BROKEN today -> FIXED in v4): Cannot promote to Release 0.2 before Gina locks the 4 rules and closes remaining backlog.
Why: No code gate prevents promoting the draft before Gina locks the 4 boundary rules and before the 3 paywalled PDFs, 336 Kosmos rows, and 168 early re-reads are closed.
In the model, one step leads into this bug: "Promote draft branch to Release 0.2 [Project lead]". The steps below are the shortest path that TLC found.

0. Start: Open RelaxDB entry queued
1. Stage open full texts [Program: exclude 12 held-out entries]. Now: Open full texts staged (128/131 covered)
2. Extract paper into fixed JSON [Reader LLM: verbatim quotes]. Now: Paper JSON drafted (unverified)
3. Verify quotes & table rows [Program: 776/776 pass]. Now: Verbatim quotes & tables verified (776/776)
4. Check links, counts, leaks & diagrams [Program: fixed rules]. Now: Consistency gate passed (131 pages, 0 leaks, 9 method groups)
5. Build 131-protein Atlas & 10-tab workbook [Program]. Now: 131-protein Atlas built (upstream sample binding unchecked)
6. Promote draft branch to Release 0.2 [Project lead]. Now: Promoted early (missing expert sign-off or backlog)

With v4 locked workflow, step 4 (Check links, counts, leaks & diagrams [Program: fixed rules]) cannot happen, so you stay at: Verbatim quotes & tables verified (776/776).
