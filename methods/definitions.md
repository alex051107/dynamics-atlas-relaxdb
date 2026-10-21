# Definitions

This page defines the words and rules that the atlas uses. The rules apply to slice 1, alternate APO states.

## States

- **Conformation**: the three-dimensional shape of a protein at one moment.
- **State**: a group of similar conformations that the protein visits. A **major state** holds most molecules. A **minor state** holds a small fraction.
- **APO**: the protein binds nothing (no drug, substrate or partner protein). **Holo**: the protein binds something.
- **Alternate APO state**: a minor state of the APO protein.

## Measured quantities

- **kex**: the exchange rate between two states, in s⁻¹.
- **pB**: the population of the minor state.
- **Δω**: the difference between the NMR frequencies of the two states.
- **Rex**: the extra transverse relaxation that exchange adds to a signal. Rex shows that exchange happens, but it does not give kex or pB on its own.

Methods that give kex and pB: CPMG relaxation dispersion, CEST and R1ρ. A second peak set in the spectrum shows a second state directly.

## The reference state

The **reference state** is the RelaxDB entry construct as deposited, free of ligand. Each call is about the reference state. Evidence from mutants, homologs, other constructs or bound samples is kept separate. It never decides the call.

## The call

| Call | Rule |
|---|---|
| yes | A minor state with a measured population and rate (CPMG, CEST, R1ρ), or a second peak set, in the reference state |
| possible | Exchange detected in the reference state, but no population. Or a population only in another condition |
| no_evidence | Measured in a window that could see it, and not seen. The window must be stated |
| unknown | Not measured, or the search was not sufficient |

Three rules refine the call:

1. **Abstracts.** Evidence from an abstract gives at most "unresolved". An abstract does not state the sample conditions or the detection window.
2. **Single-field Rex.** Rex that the authors report from a full-text relaxation analysis counts as exchange detected, so the call is "possible". Each such call carries a fixed caveat: anisotropic tumbling can also produce an apparent Rex. We set this rule on 20 October 2026. Our collaborator has not confirmed it yet.
3. **Other samples.** Exchange that is seen only in a variant or another construct is not exchange in the reference state.

## The strict two-peak reading

The working definition asks for exchange slow enough to show two separate peaks. Exchange is slow when kex is much smaller than Δω (with Δω in rad/s). Each record gives a second, strict reading:

- **qualifies**: the paper states slow exchange or shows two peak sets.
- **does not**: the paper states fast or intermediate exchange.
- **cannot tell**: the paper gives neither.

When a paper prints both kex and Δω, we compute kex/Δω and give the result next to the authors' words. The two can disagree. CheY is an example. Its local fit for D64 gives kex 96 s⁻¹, Δω 9.4 ppm and 20% minor state. So kex/Δω = 0.03 at 600 MHz. That is slow exchange, but the paper reports no second peak.

## Open questions for our collaborator

1. Which reading does the atlas use: any measured minor state, or only a state slow enough for two peaks?
2. Does single-field Rex count as exchange detected?
3. Does a metal-bound state that is coupled to protonation count? Example: azurin His35.
4. Can a near-identical variant stand in for the entry construct? Example: cysteine-free RNase HI.
