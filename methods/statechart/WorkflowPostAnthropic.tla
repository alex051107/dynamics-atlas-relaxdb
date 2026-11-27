---- MODULE WorkflowPostAnthropic ----
\* Locked post-Anthropic Dynamics Atlas workflow (27 November 2026).
\* Covers the gate from 12 open Batch 1 proteins to broad ~8,000-protein scaling.
\* Code-enforced gates cite repository files; human/process gates cite project specs (not yet code-locked).

VARIABLES sealed, staged, ruleMode, batch1, signOffLabel, expertReviewed, scaleApproved
vars == <<sealed, staged, ruleMode, batch1, signOffLabel, expertReviewed, scaleApproved>>

TypeOK ==
    /\ sealed \in BOOLEAN
    /\ staged \in BOOLEAN
    /\ ruleMode \in {"None", "GinaLocked", "StrictAbstain"}
    /\ batch1 \in {"None", "Extracted", "Quarantined", "QCPassed"}
    /\ signOffLabel \in {"Unreviewed", "AbstainDefault", "ExpertApproved"}
    /\ expertReviewed \in BOOLEAN
    /\ scaleApproved \in BOOLEAN

Init ==
    /\ sealed \in BOOLEAN
    /\ staged = FALSE
    /\ ruleMode = "None"
    /\ batch1 = "None"
    /\ signOffLabel = "Unreviewed"
    /\ expertReviewed = FALSE
    /\ scaleApproved = FALSE

\* Step 1 (DONE): Exclude 12 held-out entries, stage 12 open Batch 1 proteins, freeze 3 proposed rules.
StageBatch1AndRules ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ ~staged \* methods/check_review_consistency.py:261
    /\ staged' = TRUE
    /\ UNCHANGED <<sealed, ruleMode, batch1, signOffLabel, expertReviewed, scaleApproved>>

\* Step 2A (NOT DONE YET, human gate): NMR expert Gina reviews 3 pilot cases and locks core prompt.
GinaLocksCoreRules ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* PROPOSED_RULES_20261126.md:3
    /\ ruleMode = "None" \* PROPOSED_RULES_20261126.md:5
    /\ ruleMode' = "GinaLocked"
    /\ UNCHANGED <<sealed, staged, batch1, signOffLabel, expertReviewed, scaleApproved>>

\* Step 2B (NOT DONE YET, 1-week timer fallback): Start Batch 1 under strict-abstain defaults, marked abstain.
UseStrictAbstainFallback ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* atlas_pipeline/schema.py:890
    /\ ruleMode = "None" \* PROPOSED_RULES_20261126.md:3
    /\ ruleMode' = "StrictAbstain"
    /\ signOffLabel' = "AbstainDefault"
    /\ UNCHANGED <<sealed, staged, batch1, expertReviewed, scaleApproved>>

\* Step 3 (NOT DONE YET): Anthropic runs Claude over 12 open proteins using the single canonical prompt.
RunAnthropicBatch1 ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* ANTHROPIC_HANDOFF.md:7
    /\ ruleMode \in {"GinaLocked", "StrictAbstain"} \* atlas_pipeline/schema.py:903
    /\ batch1 \in {"None", "Quarantined"}
    /\ batch1' = "Extracted"
    /\ UNCHANGED <<sealed, staged, ruleMode, signOffLabel, expertReviewed, scaleApproved>>

\* Step 4A (Code built; Batch 1 run NOT DONE YET): Deterministic Python QC rejects bad quotes, units, or conditions.
QuarantineFailedQC ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ batch1 = "Extracted" \* atlas_pipeline/schema.py:556
    /\ batch1' = "Quarantined"
    /\ UNCHANGED <<sealed, staged, ruleMode, signOffLabel, expertReviewed, scaleApproved>>

\* Step 4B (Code built; Batch 1 run NOT DONE YET): Deterministic Python QC passes quotes, units, oligomer guard, 5-slot checks, and logs metrics.
PassDeterministicQC ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ batch1 = "Extracted" \* atlas_pipeline/schema.py:831
    /\ batch1' = "QCPassed"
    /\ UNCHANGED <<sealed, staged, ruleMode, signOffLabel, expertReviewed, scaleApproved>>

\* Step 5 (NOT DONE YET, human gate): NMR expert Gina spot-checks Batch 1 cards (and any abstain records) and signs off.
GinaSpotChecksBatch1 ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ batch1 = "QCPassed" \* ANTHROPIC_HANDOFF.md:9
    /\ ~expertReviewed \* PROPOSED_RULES_20261126.md:3
    /\ expertReviewed' = TRUE
    /\ signOffLabel' = "ExpertApproved"
    /\ UNCHANGED <<sealed, staged, ruleMode, batch1, scaleApproved>>

\* Step 6 (NOT DONE YET, human gate): Project lead approves scaling toward ~8,000 candidates after QC and expert sign-off.
ApproveBroadScaling ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* ANTHROPIC_HANDOFF.md:9
    /\ batch1 = "QCPassed" \* atlas_pipeline/schema.py:831
    /\ expertReviewed \* PROPOSED_RULES_20261126.md:3
    /\ signOffLabel = "ExpertApproved" \* PROPOSED_RULES_20261126.md:3
    /\ ~scaleApproved
    /\ scaleApproved' = TRUE
    /\ UNCHANGED <<sealed, staged, ruleMode, batch1, signOffLabel, expertReviewed>>

Next ==
    \/ StageBatch1AndRules
    \/ GinaLocksCoreRules
    \/ UseStrictAbstainFallback
    \/ RunAnthropicBatch1
    \/ QuarantineFailedQC
    \/ PassDeterministicQC
    \/ GinaSpotChecksBatch1
    \/ ApproveBroadScaling

Spec == Init /\ [][Next]_vars

\* The 12 held-out test entries never enter staging, Anthropic extraction, QC, expert review, or broad scaling.
NoHeldOutExposure ==
    sealed => (~staged /\ ruleMode = "None" /\ batch1 = "None" /\ ~expertReviewed /\ ~scaleApproved)

\* Raw Claude output never reaches expert review cards without passing deterministic quote, unit, oligomer, and 5-slot condition checks.
NoUncheckedOutputAccepted ==
    expertReviewed => (batch1 = "QCPassed")

\* Output run under the 1-week strict-abstain fallback stays marked abstain and is never labeled expert-approved before Gina reviews.
NoAbstainLabeledSignedOff ==
    (ruleMode = "StrictAbstain" /\ ~expertReviewed) => (signOffLabel # "ExpertApproved")

\* Scaling toward ~8,000 candidate proteins never starts until Batch 1 runs on open proteins, passes deterministic QC, and receives Gina's expert sign-off.
NoScaleWithoutEvidenceAndExpertCheck ==
    scaleApproved => (~sealed /\ staged /\ batch1 = "QCPassed" /\ expertReviewed /\ signOffLabel = "ExpertApproved")

\* Reachability probe (used only with --expect-broken in WorkflowPostAnthropicGoal.cfg): proves broad scaling is reachable.
GoalNotYetReached == ~scaleApproved
====
