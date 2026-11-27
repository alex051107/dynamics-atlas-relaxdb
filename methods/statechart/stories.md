## 1. Scaled early (missing Batch 1 QC or sign-off)

Rule broken: Scaling toward ~8,000 candidate proteins never starts until Batch 1 runs on open proteins, passes deterministic QC, and receives Gina's expert sign-off.
Why: No code lock prevents launching broad ~8,000-protein scaling in Slack before Batch 1 deterministic QC and Gina's spot-check finish.
In the model, one step leads into this bug: "Review QC, sign-off, and cost; approve ~8,000 scale [Lead, judgment, NOT DONE YET]". The steps below are the shortest path that TLC found.

0. Start: Candidate protein enters gate
1. Exclude 12 held-out, stage 12 open proteins + 3 rules [Program, fixed rule, DONE]. Now: TODAY: 12 Batch 1 proteins + 3 rules staged (DONE)
2. Review 3 cases and lock core prompt [Gina, judgment, NOT DONE YET]. Now: Core prompt locked by Gina (NOT DONE YET)
3. Review QC, sign-off, and cost; approve ~8,000 scale [Lead, judgment, NOT DONE YET]. Now: Scaled early (missing Batch 1 QC or sign-off)

With locked workflow, step 3 (Review QC, sign-off, and cost; approve ~8,000 scale [Lead, judgment, NOT DONE YET]) cannot happen, so you stay at: Core prompt locked by Gina (NOT DONE YET).

## 2. Abstain batch mislabeled expert-approved

Rule broken: Output run under the 1-week strict-abstain fallback stays marked abstain and is never labeled expert-approved before Gina reviews.
Why: No code lock prevents marking a 1-week strict-abstain Batch 1 output as expert-approved before Gina reviews it.
In the model, one step leads into this bug: "Mark abstain batch expert-approved without Gina [Unguarded shortcut]". The steps below are the shortest path that TLC found.

0. Start: Candidate protein enters gate
1. Exclude 12 held-out, stage 12 open proteins + 3 rules [Program, fixed rule, DONE]. Now: TODAY: 12 Batch 1 proteins + 3 rules staged (DONE)
2. No ruling after 1 week: strict-abstain default [Fixed rule, NOT DONE YET]. Now: 1-week strict-abstain active (NOT DONE YET)
3. Extract 12 open proteins with canonical prompt [Anthropic, fixed prompt, NOT DONE YET]. Now: Batch 1 JSON, abstain (NOT DONE YET)
4. Verify quotes, units, 5-slot match + log cost [Program, fixed rule, NOT DONE YET]. Now: Batch 1 QC passed, abstain (NOT DONE YET)
5. Mark abstain batch expert-approved without Gina [Unguarded shortcut]. Now: Abstain batch mislabeled expert-approved

With locked workflow, step 5 (Mark abstain batch expert-approved without Gina [Unguarded shortcut]) cannot happen, so you stay at: Batch 1 QC passed, abstain (NOT DONE YET).
