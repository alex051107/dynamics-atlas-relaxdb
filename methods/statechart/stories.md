## 1. Quote & table checks passed; Draft workbook built

Rule broken: Invariant 3 (expected broken - Gap 1): Program checks verify quotes, not whether sample solvent/ratio belongs to the measured state.
Why: Workbook builds before sample-condition binding is verified (quote checks pass even when solvent/ratio is swapped).
In the model, one step leads into this bug: "Build merged workbook [Program: does not enforce condition binding]". The steps below are the shortest path that TLC found.

0. Start: Queued open entry
1. Stage local PMC full text [Program: DOI match, exclude 12 held-out entries]. Now: Local full text staged
2. Read full text once [Reader LLM: fixed brief, verbatim quotes]. Now: JSON drafted (unchecked)
3. Check quotes & tables [Program: text match + leakage check; no binding check]. Now: Quote & table checks passed
4. Build merged workbook [Program: does not enforce condition binding]. Now: Quote & table checks passed; Draft workbook built

## 2. Quote & table checks passed; Draft workbook built; Shared for expert review

Rule broken: Invariant 4 (expected broken - Gap 2): Draft can be shared before expert NMR review and before unread full-text sources are integrated.
Why: Draft can be shared while 988 earlier DOIs (244 full text) remain unread and before Gina's expert review.
In the model, one step leads into this bug: "Share draft link with Gina [Project lead]". The steps below are the shortest path that TLC found.

0. Start: Queued open entry
1. Stage local PMC full text [Program: DOI match, exclude 12 held-out entries]. Now: Local full text staged
2. Read full text once [Reader LLM: fixed brief, verbatim quotes]. Now: JSON drafted (unchecked)
3. Check quotes & tables [Program: text match + leakage check; no binding check]. Now: Quote & table checks passed
4. Build merged workbook [Program: does not enforce condition binding]. Now: Quote & table checks passed; Draft workbook built
5. Share draft link with Gina [Project lead]. Now: Quote & table checks passed; Draft workbook built; Shared for expert review
