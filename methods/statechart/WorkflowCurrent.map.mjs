export const readerActions = ["LockExpertRules", "PromoteToRelease"];

export function state(v) {
	if (v.sealed) return "Held-out entry (12 blocked by program)";
	if (v.promoted && v.ginaRules && v.backlogClosed && v.conditionGate) {
		return "Release 0.2 promoted (expert approved + backlog closed)";
	}
	if (v.promoted) return "Promoted early (missing expert sign-off or backlog)";
	if (v.backlogClosed) return "3 paywalled + 336 Kosmos + 168 early records closed";
	if (v.ginaRules) return "Gina locked 4 boundary rules (ready for v4 sweep)";
	if (v.atlasBuilt && v.conditionGate) return "131-protein Atlas built (sample binding checked)";
	if (v.atlasBuilt) return "131-protein Atlas built (upstream sample binding unchecked)";
	if (v.consistencyGate) return "Consistency gate passed (131 pages, 0 leaks, 9 method groups)";
	if (v.conditionGate) return "Single-condition sample gate passed";
	if (v.extracted === "QuoteChecked") return "Verbatim quotes & tables verified (776/776)";
	if (v.extracted === "Drafted") return "Paper JSON drafted (unverified)";
	if (v.staged === "OpenTextReady") return "Open full texts staged (128/131 covered)";
	return "Open RelaxDB entry queued";
}

export function group(v) {
	if (v.sealed) return "Held-out (blocked)";
	if (v.promoted && v.ginaRules && v.backlogClosed && v.conditionGate) return "Release ready";
	if (v.promoted || (v.atlasBuilt && !v.conditionGate)) return "Broken rule (gap today)";
	if (v.ginaRules || v.backlogClosed) return "Expert & v4 closure";
	if (v.consistencyGate || v.conditionGate || v.atlasBuilt) return "Verified draft";
	return "Extraction & checks";
}

export const groupColors = {
	"Held-out (blocked)": "#e5e7eb",
	"Extraction & checks": "#dbeafe",
	"Verified draft": "#e0e7ff",
	"Expert & v4 closure": "#dcfce7",
	"Release ready": "#bbf7d0",
	"Broken rule (gap today)": "#fee2e2",
};

const STEPS = {
	StageOpenTexts: "Stage open full texts [Program: exclude 12 held-out entries]",
	ExtractPaper: "Extract paper into fixed JSON [Reader LLM: verbatim quotes]",
	VerifyQuotesAndTables: "Verify quotes & table rows [Program: 776/776 pass]",
	EnforceConditionGate: "Check 1 condition per sample + closed method enum [v4 Program gate]",
	RunConsistencyGate: "Check links, counts, leaks & diagrams [Program: fixed rules]",
	BuildUnifiedAtlas: "Build 131-protein Atlas & 10-tab workbook [Program]",
	LockExpertRules: "Lock 4 boundary rules [NMR Expert Gina; NOT DONE YET]",
	CloseExternalBacklog: "Close 3 paywalled + 336 Kosmos + 168 re-reads [NOT DONE YET]",
	PromoteToRelease: "Promote draft branch to Release 0.2 [Project lead]",
};

export function step(action) {
	return STEPS[action] ?? action;
}

export function cause(v, facts, invariant) {
	if (invariant === "NoUncheckedSampleBinding") {
		return "Atlas and workbook can be built before an automated upstream check blocks merged multi-condition sample cards (fixed manually for BARSTAR on 19 Nov, not yet blocked in v4 extractor).";
	}
	if (invariant === "NoReleaseWithoutExpertAndBacklog") {
		return "No code gate prevents promoting the draft before Gina locks the 4 boundary rules and before the 3 paywalled PDFs, 336 Kosmos rows, and 168 early re-reads are closed.";
	}
	return null;
}

export const legend = {
	works: "Protected today",
	wrong: "Open gap today (breaks rule)",
	fixed: "Blocked by v4 locked workflow",
};
