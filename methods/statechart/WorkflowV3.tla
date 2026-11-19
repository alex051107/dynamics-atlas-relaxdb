---- MODULE WorkflowV3 ----
\* Dynamics Atlas v3 literature-curation workflow (18 November 2026 state).
\* Plain-language English labels live in WorkflowV3.map.mjs.

VARIABLES sealed, text, extracted, blind, bindingChecked, coverageComplete, merged, shared, gina
vars == <<sealed, text, extracted, blind, bindingChecked, coverageComplete, merged, shared, gina>>

TypeOK ==
    /\ sealed \in BOOLEAN
    /\ text \in {"None", "StagedFull"}
    /\ extracted \in {"None", "Written", "Checked"}
    /\ blind \in {"NotRun", "Checked"}
    /\ bindingChecked \in BOOLEAN
    /\ coverageComplete \in BOOLEAN
    /\ merged \in BOOLEAN
    /\ shared \in BOOLEAN
    /\ gina \in BOOLEAN

Init ==
    /\ sealed \in BOOLEAN
    /\ text = "None"
    /\ extracted = "None"
    /\ blind = "NotRun"
    /\ bindingChecked = FALSE
    /\ coverageComplete = FALSE
    /\ merged = FALSE
    /\ shared = FALSE
    /\ gina = FALSE

\* Program: resolves open RelaxDB entry DOIs to local PMC XML full text; held-out entries are excluded.
StageLocalFullText ==
    /\ ~sealed /\ text = "None"
    /\ text' = "StagedFull"
    /\ UNCHANGED <<sealed, extracted, blind, bindingChecked, coverageComplete, merged, shared, gina>>

\* Reader LLM (Claude Sonnet on 466 records; Gemini Pro/Flash on 305 B5 records): reads paper once into fixed v3 JSON.
ExtractPaper ==
    /\ ~sealed /\ text = "StagedFull" /\ extracted = "None"
    /\ extracted' = "Written"
    /\ UNCHANGED <<sealed, text, blind, bindingChecked, coverageComplete, merged, shared, gina>>

\* Program: checks verbatim quotes, value inside quote, table accounting, zero sealed or path leaks. Does NOT check sample binding.
ProgramChecks ==
    /\ ~sealed /\ extracted = "Written"
    /\ extracted' = "Checked"
    /\ UNCHANGED <<sealed, text, blind, bindingChecked, coverageComplete, merged, shared, gina>>

\* Second-family LLM: blind-reads a 10% stratified sample (30 papers) and curator adjudicates diffs against source text.
BlindSpotCheck ==
    /\ ~sealed /\ extracted = "Checked" /\ blind = "NotRun"
    /\ blind' = "Checked"
    /\ UNCHANGED <<sealed, text, extracted, bindingChecked, coverageComplete, merged, shared, gina>>

\* Missing gate in v3 (proposed for v4): resolve 988 unread Nov-12 DOIs (244 full text), Kosmos ZIP, and 22 zero-paper entries.
ResolveUnreadSources ==
    /\ ~sealed /\ ~coverageComplete
    /\ coverageComplete' = TRUE
    /\ UNCHANGED <<sealed, text, extracted, blind, bindingChecked, merged, shared, gina>>

\* Program: builds merged draft Excel workbook once deterministic quote/table checks pass. Does not wait for blind check or condition-binding gate.
BuildWorkbook ==
    /\ ~sealed /\ extracted = "Checked" /\ ~merged
    /\ merged' = TRUE
    /\ UNCHANGED <<sealed, text, extracted, blind, bindingChecked, coverageComplete, shared, gina>>

\* Person: shares GitHub overview and draft workbook link with Gina and Soojung.
ShareWithExpert ==
    /\ ~sealed /\ merged /\ ~shared
    /\ shared' = TRUE
    /\ UNCHANGED <<sealed, text, extracted, blind, bindingChecked, coverageComplete, merged, gina>>

\* NMR Expert (Gina): reviews worked protein cards, validates sample conditions and inclusion cutoff (NOT DONE YET).
ExpertReview ==
    /\ ~sealed /\ shared /\ ~gina
    /\ gina' = TRUE
    /\ UNCHANGED <<sealed, text, extracted, blind, bindingChecked, coverageComplete, merged, shared>>

Next ==
    \/ StageLocalFullText
    \/ ExtractPaper
    \/ ProgramChecks
    \/ BlindSpotCheck
    \/ ResolveUnreadSources
    \/ BuildWorkbook
    \/ ShareWithExpert
    \/ ExpertReview

Spec == Init /\ [][Next]_vars

\* Invariant 1 (holds): Held-out evaluation entries never enter extraction or workbook.
NoSealedEntryRead == sealed => (text = "None" /\ extracted = "None" /\ ~merged)

\* Invariant 2 (holds): No unverified extraction row enters the draft workbook.
OnlyQuoteCheckedInWorkbook == merged => extracted = "Checked"

\* Invariant 3 (expected broken - Gap 1): Program checks verify quotes, not whether sample solvent/ratio belongs to the measured state.
NoUncheckedConditionBinding == merged => bindingChecked

\* Invariant 4 (expected broken - Gap 2): Draft can be shared before expert NMR review and before unread full-text sources are integrated.
NoReleaseWithoutExpertAndCoverage == shared => (gina /\ coverageComplete)
====
