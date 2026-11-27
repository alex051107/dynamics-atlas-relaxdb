export const readerActions = ["GinaLocksCoreRules", "GinaSpotChecksBatch1", "ApproveBroadScaling"];

export function state(v) {
	if (v.sealed) {
		return "Held-out test entry (12 physically blocked)";
	}
	if (v.scaleApproved && v.batch1 === "QCPassed" && v.expertReviewed && v.signOffLabel === "ExpertApproved") {
		return "Scale ~8,000 approved (NOT DONE YET)";
	}
	if (v.scaleApproved) {
		return "Scaled early (missing Batch 1 QC or sign-off)";
	}
	if (v.ruleMode === "StrictAbstain" && !v.expertReviewed && v.signOffLabel === "ExpertApproved") {
		return "Abstain batch mislabeled expert-approved";
	}
	if (v.expertReviewed && v.batch1 === "QCPassed") {
		return "Batch 1 QC + Gina sign-off (NOT DONE YET)";
	}
	if (v.batch1 === "QCPassed" && v.ruleMode === "StrictAbstain") {
		return "Batch 1 QC passed, abstain (NOT DONE YET)";
	}
	if (v.batch1 === "QCPassed") {
		return "Batch 1 QC + metrics logged (NOT DONE YET)";
	}
	if (v.batch1 === "Quarantined" && v.ruleMode === "StrictAbstain") {
		return "QC failed, abstain repair (NOT DONE YET)";
	}
	if (v.batch1 === "Quarantined") {
		return "QC failed, repair needed (NOT DONE YET)";
	}
	if (v.batch1 === "Extracted" && v.ruleMode === "StrictAbstain") {
		return "Batch 1 JSON, abstain (NOT DONE YET)";
	}
	if (v.batch1 === "Extracted") {
		return "Batch 1 raw JSON returned (NOT DONE YET)";
	}
	if (v.ruleMode === "GinaLocked") {
		return "Core prompt locked by Gina (NOT DONE YET)";
	}
	if (v.ruleMode === "StrictAbstain") {
		return "1-week strict-abstain active (NOT DONE YET)";
	}
	if (v.staged) {
		return "TODAY: 12 Batch 1 proteins + 3 rules staged (DONE)";
	}
	return "Candidate protein enters gate";
}

export function group(v) {
	if (v.sealed) return "Program: held-out block";
	if (v.scaleApproved && v.batch1 === "QCPassed" && v.expertReviewed && v.signOffLabel === "ExpertApproved") {
		return "Lead: go/no-go";
	}
	if (v.scaleApproved || (v.ruleMode === "StrictAbstain" && !v.expertReviewed && v.signOffLabel === "ExpertApproved")) {
		return "Unguarded shortcut";
	}
	if (v.expertReviewed || (v.ruleMode === "GinaLocked" && v.batch1 === "None")) {
		return "Gina: NMR judgment";
	}
	if (v.ruleMode === "StrictAbstain" && v.batch1 === "None") {
		return "1-week fallback";
	}
	if (v.batch1 === "Extracted") {
		return "Anthropic: Claude";
	}
	return "Program: fixed QC";
}

export const groupColors = {
	"Program: held-out block": "#e5e7eb",
	"Program: fixed QC": "#ccfbf1",
	"Gina: NMR judgment": "#fef3c7",
	"1-week fallback": "#ffedd5",
	"Anthropic: Claude": "#dbeafe",
	"Lead: go/no-go": "#dcfce7",
	"Unguarded shortcut": "#fee2e2",
};

const STEPS = {
	StageBatch1AndRules: "Exclude 12 held-out, stage 12 open proteins + 3 rules [Program, fixed rule, DONE]",
	GinaLocksCoreRules: "Review 3 cases and lock core prompt [Gina, judgment, NOT DONE YET]",
	UseStrictAbstainFallback: "No ruling after 1 week: strict-abstain default [Fixed rule, NOT DONE YET]",
	RunAnthropicBatch1: "Extract 12 open proteins with canonical prompt [Anthropic, fixed prompt, NOT DONE YET]",
	QuarantineFailedQC: "Reject bad quote, unit, oligomer, or condition [Program, fixed rule, NOT DONE YET]",
	PassDeterministicQC: "Verify quotes, units, 5-slot match + log cost [Program, fixed rule, NOT DONE YET]",
	GinaSpotChecksBatch1: "Spot-check Batch 1 cards + resolve abstain [Gina, judgment, NOT DONE YET]",
	MarkAbstainApprovedEarly: "Mark abstain batch expert-approved without Gina [Unguarded shortcut]",
	ApproveBroadScaling: "Review QC, sign-off, and cost; approve ~8,000 scale [Lead, judgment, NOT DONE YET]",
};

export function step(action) {
	return STEPS[action] ?? action;
}

export function cause(v, facts, invariant) {
	if (invariant === "NoAbstainLabeledSignedOff") {
		return "No code lock prevents marking a 1-week strict-abstain Batch 1 output as expert-approved before Gina reviews it.";
	}
	if (invariant === "NoScaleWithoutEvidenceAndExpertCheck") {
		return "No code lock prevents launching broad ~8,000-protein scaling in Slack before Batch 1 deterministic QC and Gina's spot-check finish.";
	}
	return null;
}

export const legend = {
	works: "Allowed state",
	wrong: "Breaks safety rule",
	fixed: "Blocked by locked workflow",
};
