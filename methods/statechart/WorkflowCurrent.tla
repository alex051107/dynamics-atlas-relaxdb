---- MODULE WorkflowCurrent ----
\* Dynamics Atlas Unified 131-Protein Draft workflow (19 November 2026).
\* Models what the repository does today vs WorkflowV4Fixed.tla (proposed v4 gates).
\* Plain-language labels for scientists live in WorkflowCurrent.map.mjs.

VARIABLES sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted
vars == <<sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

TypeOK ==
    /\ sealed \in BOOLEAN
    /\ staged \in {"None", "OpenTextReady"}
    /\ extracted \in {"None", "Drafted", "QuoteChecked"}
    /\ conditionGate \in BOOLEAN
    /\ consistencyGate \in BOOLEAN
    /\ atlasBuilt \in BOOLEAN
    /\ ginaRules \in BOOLEAN
    /\ backlogClosed \in BOOLEAN
    /\ promoted \in BOOLEAN

Init ==
    /\ sealed \in BOOLEAN
    /\ staged = "None"
    /\ extracted = "None"
    /\ conditionGate = FALSE
    /\ consistencyGate = FALSE
    /\ atlasBuilt = FALSE
    /\ ginaRules = FALSE
    /\ backlogClosed = FALSE
    /\ promoted = FALSE

\* Program (identity_preflight / split guard): stages open RelaxDB full texts; 12 held-out entries stay blocked.
StageOpenTexts ==
    /\ ~sealed /\ staged = "None"
    /\ staged' = "OpenTextReady"
    /\ UNCHANGED <<sealed, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

\* Reader LLM (Claude / Gemini): reads full text into fixed JSON template (samples, measurements, states, regions, gaps).
ExtractPaper ==
    /\ ~sealed /\ staged = "OpenTextReady" /\ extracted = "None"
    /\ extracted' = "Drafted"
    /\ UNCHANGED <<sealed, staged, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

\* Program (check_key.py / quote verifier): verifies verbatim quotes, numeric containment, and table accounting (776/776 pass).
VerifyQuotesAndTables ==
    /\ ~sealed /\ extracted = "Drafted"
    /\ extracted' = "QuoteChecked"
    /\ UNCHANGED <<sealed, staged, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

\* Program (check_review_consistency.py): checks 131/131 atlas pages, 0 sealed leaks, 0 broken links, 9 method groups, prose clarity.
RunConsistencyGate ==
    /\ ~sealed /\ extracted = "QuoteChecked" /\ ~consistencyGate
    /\ consistencyGate' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

\* Program (build_atlas_and_workbook): builds 131-protein Atlas + 10-tab workbook.
\* Current gap: does NOT wait for an automated single-condition-per-sample gate on every upstream paper.
BuildUnifiedAtlas ==
    /\ ~sealed /\ extracted = "QuoteChecked" /\ consistencyGate /\ ~atlasBuilt
    /\ atlasBuilt' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, ginaRules, backlogClosed, promoted>>

\* NMR Expert (Gina): reviews ATLAS_131.md, Ets-1 walkthrough, and locks the 4 boundary rules (NOT DONE YET).
LockExpertRules ==
    /\ ~sealed /\ atlasBuilt /\ ~ginaRules
    /\ ginaRules' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, backlogClosed, promoted>>

\* Curator + Program (NOT DONE YET): pulls 3 paywalled PDFs, 336 Kosmos rows, and re-reads 168 early records under locked v4 schema.
CloseExternalBacklog ==
    /\ ~sealed /\ ginaRules /\ ~backlogClosed
    /\ backlogClosed' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, promoted>>

\* Release action: promotes draft branch to Release 0.2.
\* Current gap: no code blocks promotion if Gina has not signed off or backlog is still open.
PromoteToRelease ==
    /\ ~sealed /\ atlasBuilt /\ ~promoted
    /\ promoted' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed>>

Next ==
    \/ StageOpenTexts
    \/ ExtractPaper
    \/ VerifyQuotesAndTables
    \/ RunConsistencyGate
    \/ BuildUnifiedAtlas
    \/ LockExpertRules
    \/ CloseExternalBacklog
    \/ PromoteToRelease

Spec == Init /\ [][Next]_vars

\* Rule 1 (HOLDS today): Held-out test entries never enter staging, extraction, atlas, or release.
NoSealedEntryRead == sealed => (staged = "None" /\ extracted = "None" /\ ~atlasBuilt /\ ~promoted)

\* Rule 2 (HOLDS today): Only quote-checked and consistency-checked records enter the unified 131-protein atlas.
OnlyVerifiedInAtlas == atlasBuilt => (extracted = "QuoteChecked" /\ consistencyGate)

\* Rule 3 (BROKEN today -> FIXED in v4): Upstream single-condition-per-sample gate must pass before building atlas/workbook.
NoUncheckedSampleBinding == atlasBuilt => conditionGate

\* Rule 4 (BROKEN today -> FIXED in v4): Cannot promote to Release 0.2 before Gina locks the 4 rules and closes remaining backlog.
NoReleaseWithoutExpertAndBacklog == promoted => (ginaRules /\ backlogClosed /\ conditionGate)
====
