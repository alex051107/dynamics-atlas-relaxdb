// Plain-English mapper for WorkflowV3.tla (for collaborator & NMR expert review).
export const readerActions = ["ShareWithExpert", "ExpertReview"];

export function state(v) {
	if (v.sealed) return "Held-out test entry (blocked by program)";
	const parts = [];
	if (v.text === "None") parts.push("Queued open entry");
	else if (v.extracted === "None") parts.push("Local full text staged");
	else if (v.extracted === "Written") parts.push("JSON drafted (unchecked)");
	else parts.push("Quote & table checks passed");
	if (v.blind === "Checked") parts.push("10% blind check adjudicated");
	if (v.coverageComplete) parts.push("Unread full texts integrated");
	if (v.merged) parts.push("Draft workbook built");
	if (v.shared) parts.push("Shared for expert review");
	if (v.gina) parts.push("Expert signed off");
	return parts.join("; ");
}

export function group(v) {
	if (v.sealed) return "Held-out (blocked)";
	if (v.gina) return "Expert approved";
	if (v.shared) return "Gap: shared unreviewed";
	if (v.merged && !v.bindingChecked) return "Gap: sample binding unchecked";
	if (v.blind === "Checked") return "Blind check ran";
	return "Preparing / reading";
}

export const groupColors = {
	"Held-out (blocked)": "#e5e7eb",
	"Preparing / reading": "#dbeafe",
	"Blind check ran": "#e0e7ff",
	"Gap: sample binding unchecked": "#fef3c7",
	"Gap: shared unreviewed": "#fee2e2",
	"Expert approved": "#d1fae5",
};

const STEPS = {
	StageLocalFullText: "Stage local PMC full text [Program: DOI match, exclude 12 held-out entries]",
	ExtractPaper: "Read full text once [Reader LLM: fixed brief, verbatim quotes]",
	ProgramChecks: "Check quotes & tables [Program: text match + leakage check; no binding check]",
	BlindSpotCheck: "Blind-read 10% sample [Second-family LLM + curator adjudication]",
	ResolveUnreadSources: "Read remaining 988 Nov-12 DOIs & Kosmos [NOT DONE YET]",
	BuildWorkbook: "Build merged workbook [Program: does not enforce condition binding]",
	ShareWithExpert: "Share draft link with Gina [Project lead]",
	ExpertReview: "Validate definitions & spots [NMR Expert Gina; NOT DONE YET]",
};

export function step(action) {
	return STEPS[action] ?? action;
}

export function cause(v, facts, invariant) {
	if (invariant === "NoUncheckedConditionBinding") {
		return "Workbook builds before sample-condition binding is verified (quote checks pass even when solvent/ratio is swapped).";
	}
	if (invariant === "NoReleaseWithoutExpertAndCoverage") {
		return "Draft can be shared while 988 earlier DOIs (244 full text) remain unread and before Gina's expert review.";
	}
	return null;
}

export const legend = {
	works: "Protected by current code",
	wrong: "Breaks expert/completeness gate today",
	fixed: "Protected after proposed fix",
};
