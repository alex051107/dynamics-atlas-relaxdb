## 1. Scale ~8,000 approved (NOT DONE YET)

Rule broken: Reachability probe (used only with --expect-broken in WorkflowPostAnthropicGoal.cfg): proves broad scaling is reachable.
In the model, one step leads into this bug: "Review QC, sign-off, and cost; approve ~8,000 scale [Lead, judgment, NOT DONE YET]". The steps below are the shortest path that TLC found.

0. Start: Candidate protein enters gate
1. Exclude 12 held-out, stage 12 open proteins + 3 rules [Program, fixed rule, DONE]. Now: TODAY: 12 Batch 1 proteins + 3 rules staged (DONE)
2. Review 3 cases and lock core prompt [Gina, judgment, NOT DONE YET]. Now: Core prompt locked by Gina (NOT DONE YET)
3. Extract 12 open proteins with canonical prompt [Anthropic, fixed prompt, NOT DONE YET]. Now: Batch 1 raw JSON returned (NOT DONE YET)
4. Verify quotes, units, 5-slot match + log cost [Program, fixed rule, NOT DONE YET]. Now: Batch 1 QC + metrics logged (NOT DONE YET)
5. Spot-check Batch 1 cards + resolve abstain [Gina, judgment, NOT DONE YET]. Now: Batch 1 QC + Gina sign-off (NOT DONE YET)
6. Review QC, sign-off, and cost; approve ~8,000 scale [Lead, judgment, NOT DONE YET]. Now: Scale ~8,000 approved (NOT DONE YET)
