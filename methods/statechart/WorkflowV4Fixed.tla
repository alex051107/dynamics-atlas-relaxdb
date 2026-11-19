---- MODULE WorkflowV4Fixed ----
\* Proposed v4 locked workflow (after Gina signs off on REVIEW_GUIDE.md).
\* Adds upstream EnforceConditionGate before atlas build and guards PromoteToRelease on Gina + backlog closure.

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

StageOpenTexts ==
    /\ ~sealed /\ staged = "None"
    /\ staged' = "OpenTextReady"
    /\ UNCHANGED <<sealed, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

ExtractPaper ==
    /\ ~sealed /\ staged = "OpenTextReady" /\ extracted = "None"
    /\ extracted' = "Drafted"
    /\ UNCHANGED <<sealed, staged, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

VerifyQuotesAndTables ==
    /\ ~sealed /\ extracted = "Drafted"
    /\ extracted' = "QuoteChecked"
    /\ UNCHANGED <<sealed, staged, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

\* NEW v4 gate: rejects any sample card combining two solvents, pH/pD values, temperatures, or ligand ratios + checks closed method enum.
EnforceConditionGate ==
    /\ ~sealed /\ extracted = "QuoteChecked" /\ ~conditionGate
    /\ conditionGate' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, consistencyGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

RunConsistencyGate ==
    /\ ~sealed /\ extracted = "QuoteChecked" /\ conditionGate /\ ~consistencyGate
    /\ consistencyGate' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, atlasBuilt, ginaRules, backlogClosed, promoted>>

BuildUnifiedAtlas ==
    /\ ~sealed /\ extracted = "QuoteChecked" /\ conditionGate /\ consistencyGate /\ ~atlasBuilt
    /\ atlasBuilt' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, ginaRules, backlogClosed, promoted>>

LockExpertRules ==
    /\ ~sealed /\ atlasBuilt /\ ~ginaRules
    /\ ginaRules' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, backlogClosed, promoted>>

CloseExternalBacklog ==
    /\ ~sealed /\ ginaRules /\ ~backlogClosed
    /\ backlogClosed' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, promoted>>

PromoteToRelease ==
    /\ ~sealed /\ atlasBuilt /\ conditionGate /\ ginaRules /\ backlogClosed /\ ~promoted
    /\ promoted' = TRUE
    /\ UNCHANGED <<sealed, staged, extracted, conditionGate, consistencyGate, atlasBuilt, ginaRules, backlogClosed>>

Next ==
    \/ StageOpenTexts
    \/ ExtractPaper
    \/ VerifyQuotesAndTables
    \/ EnforceConditionGate
    \/ RunConsistencyGate
    \/ BuildUnifiedAtlas
    \/ LockExpertRules
    \/ CloseExternalBacklog
    \/ PromoteToRelease

Spec == Init /\ [][Next]_vars

NoSealedEntryRead == sealed => (staged = "None" /\ extracted = "None" /\ ~atlasBuilt /\ ~promoted)
OnlyVerifiedInAtlas == atlasBuilt => (extracted = "QuoteChecked" /\ consistencyGate)
NoUncheckedSampleBinding == atlasBuilt => conditionGate
NoReleaseWithoutExpertAndBacklog == promoted => (ginaRules /\ backlogClosed /\ conditionGate)
====
