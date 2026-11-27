---- MODULE WorkflowPostAnthropicRisk ----
\* Today's unguarded process shortcuts (27 November 2026) compared against the locked workflow.
\* Code enforces held-out exclusion and deterministic QC before review cards; abstain labeling and ~8,000 scaling remain human/process gates today.

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

StageBatch1AndRules ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ ~staged \* methods/check_review_consistency.py:261
    /\ staged' = TRUE
    /\ UNCHANGED <<sealed, ruleMode, batch1, signOffLabel, expertReviewed, scaleApproved>>

GinaLocksCoreRules ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* PROPOSED_RULES_20261126.md:3
    /\ ruleMode = "None" \* PROPOSED_RULES_20261126.md:5
    /\ ruleMode' = "GinaLocked"
    /\ UNCHANGED <<sealed, staged, batch1, signOffLabel, expertReviewed, scaleApproved>>

UseStrictAbstainFallback ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* atlas_pipeline/schema.py:890
    /\ ruleMode = "None" \* PROPOSED_RULES_20261126.md:3
    /\ ruleMode' = "StrictAbstain"
    /\ signOffLabel' = "AbstainDefault"
    /\ UNCHANGED <<sealed, staged, batch1, expertReviewed, scaleApproved>>

RunAnthropicBatch1 ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* ANTHROPIC_HANDOFF.md:7
    /\ ruleMode \in {"GinaLocked", "StrictAbstain"} \* atlas_pipeline/schema.py:903
    /\ batch1 \in {"None", "Quarantined"}
    /\ batch1' = "Extracted"
    /\ UNCHANGED <<sealed, staged, ruleMode, signOffLabel, expertReviewed, scaleApproved>>

QuarantineFailedQC ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ batch1 = "Extracted" \* atlas_pipeline/schema.py:556
    /\ batch1' = "Quarantined"
    /\ UNCHANGED <<sealed, staged, ruleMode, signOffLabel, expertReviewed, scaleApproved>>

PassDeterministicQC ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ batch1 = "Extracted" \* atlas_pipeline/schema.py:831
    /\ batch1' = "QCPassed"
    /\ UNCHANGED <<sealed, staged, ruleMode, signOffLabel, expertReviewed, scaleApproved>>

GinaSpotChecksBatch1 ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ batch1 = "QCPassed" \* ANTHROPIC_HANDOFF.md:9
    /\ ~expertReviewed \* PROPOSED_RULES_20261126.md:3
    /\ expertReviewed' = TRUE
    /\ signOffLabel' = "ExpertApproved"
    /\ UNCHANGED <<sealed, staged, ruleMode, batch1, scaleApproved>>

\* Unguarded shortcut 1 today: no code lock prevents labeling strict-abstain Batch 1 output as expert-approved before Gina reviews.
MarkAbstainApprovedEarly ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ ruleMode = "StrictAbstain" \* atlas_pipeline/schema.py:890
    /\ batch1 = "QCPassed" \* atlas_pipeline/schema.py:831
    /\ ~expertReviewed \* PROPOSED_RULES_20261126.md:3
    /\ signOffLabel = "AbstainDefault"
    /\ signOffLabel' = "ExpertApproved"
    /\ UNCHANGED <<sealed, staged, ruleMode, batch1, expertReviewed, scaleApproved>>

\* Unguarded shortcut 2 today: no code lock prevents launching ~8,000-protein scaling in Slack before Batch 1 QC and expert spot-check finish.
ApproveBroadScaling ==
    /\ ~sealed \* atlas_pipeline/schema.py:61
    /\ staged \* ANTHROPIC_HANDOFF.md:7
    /\ ruleMode \in {"GinaLocked", "StrictAbstain"} \* PROPOSED_RULES_20261126.md:3
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
    \/ MarkAbstainApprovedEarly
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
====
