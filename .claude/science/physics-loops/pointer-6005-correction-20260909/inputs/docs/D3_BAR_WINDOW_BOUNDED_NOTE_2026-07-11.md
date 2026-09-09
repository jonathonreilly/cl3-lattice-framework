# Finite-Ladder Transverse-Field Comparator: Bounded Measured Support

**Date:** 2026-07-11
**Type:** bounded_theorem
**Status authority:** independent audit lane only; this note sets no audit status.
**Scope:** a post-specified descriptive measurement on one finite, declared
transverse-field Ising comparator. It is not a framework threshold derivation.

The measurement follows the historical frozen protocol in
[`D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md`](D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md),
which inherits the declared geometry, Hamiltonian, preparation, fragment
partition, pointer convention, and observable definitions from
[`D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md`](D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md).
Those memos are protocol records, not retained authorities. Their original
`BAR-*` verdict names are not adopted as scientific grades here.

The paired reporter is
[`d3_bar_window_measurement_2026_07_11.py`](../scripts/d3_bar_window_measurement_2026_07_11.py).
Its committed evidence consists of five JSONL streams, the preflight record,
and a compact provenance/completion manifest in
[`d3_bar_window_checkpoints/`](../logs/runner-cache/d3_bar_window_checkpoints/).
In a clean checkout,
`python3 scripts/d3_bar_window_measurement_2026_07_11.py --report` authenticates
those files and the exact generation/reporter source hashes, recomputes the
finite summaries, and emits `TOTAL BOUNDED-MEASURED-SUPPORT`.

## Bounded result

Conditional on the declared comparator and gates, the committed finite ladder
`lambda in {0.02, 0.05, 0.10, 0.20}` has

- `W_full = {0.02, 0.05, 0.10}` under the memo's all-tolerances,
  by-`Jt=1`, persistent-headline definition;
- headline first-hit values
  `theta* = 0.500104157943, 0.500751527281, 0.504730776866`, with
  median `0.500751527281` and range width `0.004626618923`;
- tolerance factor `1.000890303705` and field-ladder factor
  `1.009251310652` under the declared `< 1.5` descriptive gates; and
- a change in the Boolean certification outcome between the adjacent
  commissioned field values `lambda=0.10` and `lambda=0.20`.

Only the `lambda=0.02` trace is new relative to the inspected predecessor
data. The shared `lambda=0.05, 0.10, 0.20` observables are the predecessor
values, and the minimum-window rule was introduced after those values had been
seen. Therefore `W_full` and the `(0.10,0.20)` pair are post-specified
descriptive support, not a blind certification, fit, interpolation, confidence
interval, monotonicity theorem, or physical threshold estimate.

At `lambda=0.20` and headline tolerance `delta=0.10`, the two closed-five
fragments meet the singleton content gate at `Jt=0.7`, while their conditional
dependence is `0.0603948 > 0.02` bits, so the declared independent-pair gate
does not form. The broader `W_full` condition has another distinct failure:
at strict tolerance `delta=0.05`, the content threshold is not reached by the
deadline. The endpoint is thus not an exactly-one-wall result.

The `lambda=0.02` headline event has all six declared fragments in an
independent subset under the supplied `0.02`-bit gate; the maximum of the 15
stored pair values is `0.00113269541329` bits. The `lambda=0.05` and `0.10`
headline subsets have size two. These are finite, partition-specific outcomes,
not a statement about all fragmentations or volumes.

The `dt=0.05` comparison at `lambda=0.10` moves the first hit by `0.05` in
`Jt` and changes `theta*` by `0.1718%` relative to the coarse trace. This is
one deterministic sensitivity comparison, not a numerical uncertainty model.

## What is and is not measured

`lambda` multiplies a coherent `sum_i X_i` term in a closed deterministic
Hamiltonian. No stochastic noise, disorder ensemble, environment, decoherence
channel, repeated-sample variance, or error distribution is present. The
finite-ladder outcome may be described as a transverse-field or coherent-field
comparator bracket only. It does not establish what physical noise destroys.

The reported
`theta = (1/6) sum_a (1 - Tr(rho_{Sa}^2) - baseline_a)` is an unnormalized,
declared comparator observable. No reviewed theorem maps its value near `0.50`
to a deposition threshold, a gravity parameter, or a comparator-independent
normalization. This note makes none of those comparisons and closes no
registration, deposition, or gravity chain.

The mixed ground doublet is a stationary control and diagnostic, never the
gate baseline. Its finite residual, normalization, orthogonality, stationary
event, and commutator summaries are authenticated by the compact manifest.
They support machinery integrity only.

## Import and selection inventory

The following are supplied inputs rather than derived conclusions:

- the open `3 x 3 x 3` volume and transverse-field Ising Hamiltonian;
- the class-uniform preparation, `Z` pointer, and basis privilege;
- the six-fragment partition and pair subgrid;
- the Holevo and conditional-mutual-information readout convention;
- the numerical content, independence, drift, persistence, and deadline gates;
- the `R >= 2` rule and all-tolerances definition of `W_full`;
- the theta observable and its `0.20` declared comparison floor; and
- first-sampled-hit selection, the four-point field ladder, and one
  time-step-halving comparison.

The repository's `docs/MINIMAL_AXIOMS_2026-06-29.md` is context only:
its Record clause does not supply quantum Darwinism, Holevo information,
conditional mutual information, this pointer basis, `R >= 2`, any numerical
gate, or the finite-time persistence surrogate. Nothing here is claimed to be
derived from that clause.

## Proof-obligation boundary

The finite arithmetic obligation is closed conditional on the committed
streams and declared definitions: exhaustive subset selection reproduces the
stored event ledger, and the clean-checkout reporter authenticates and
recomputes the summaries. The physical-threshold obligation is not attempted.
No lemma connects this comparator observable or four-point field ladder to a
universal record, noise, deposition, or gravity threshold. Accordingly the
strongest supported class is bounded measured support under explicit premises.

## Reproducibility and boundaries

The compact manifest records exact hashes for the historical generation
runner, both imported engine helpers, both frozen protocol memos, the current
reporter, the five committed streams, the preflight record, and the discarded
state-checkpoint identities. State-vector NPZ checkpoints are not required for
reporting and are not repository artifacts.

This note is not basis-neutral, makes no formation claim, performs no fit,
asserts no monotonic or continuum extension, and sets no audit verdict.
