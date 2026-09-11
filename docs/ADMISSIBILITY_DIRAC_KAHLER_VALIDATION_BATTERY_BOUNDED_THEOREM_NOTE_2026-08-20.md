---
claim_id: admissibility_dirac_kahler_validation_battery_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "the specified even-column pullback, its exact kernel, a balanced curved carrier, a real-weight sufficient annihilation scope, and a 41-point rational interpolation grid"
depends_on:
  - admissibility_dirac_kahler_exchange_condition_contract_bounded_theorem_note_2026-08-20
runner: scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A Specified Quotient Pullback and Curved Carrier

**Type:** `bounded_theorem`

**Campaign block:** 161. **Status:** corrected bounded theorem; formal audit is
deferred. Original note, primary, cache, ledger, and manifest bodies are in the
released-7315-B recovery packet.

The [primary](../scripts/admissibility_dirac_kahler_validation_battery_2026_08_20.py)
uses corrected [Block 160](ADMISSIBILITY_DIRAC_KAHLER_EXCHANGE_CONDITION_CONTRACT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 159 finite supplier](ADMISSIBILITY_DIRAC_KAHLER_LINK_CURVATURE_SCOUT_BOUNDED_THEOREM_NOTE_2026-08-20.md),
the [Block 105 fixture](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md),
and the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Exact pullback and kernel

For edge \((2,2)\), retain only the eight temporal hops on even spatial
columns. On the flat carrier the displayed reflected half form is

\[
P=\operatorname{diag}(4/5,0,4/5,0,4/5,0,4/5,0)
 =Q^{\mathsf T}(4I_4/5)Q,
\]

where \(Q\) selects half slots \(0,2,4,6\). Its kernel is exactly the span of
the other four coordinate vectors. This proves a pullback through that
specified quotient. It does not show that the full carrier has no other
sector, no connection content, or no physical interpretation.

The distinction matters because the carrier chart still contains

\[
a=\frac{\nu}{1-\sigma^2},\qquad
b=-\frac{\nu\sigma}{1-\sigma^2}.
\]

The full quotient action contains both kinds of moduli. Removing the named
odd-column directions from \(P\) therefore does not remove all dependence on
the magnitude of the shear.

## Curved mass-survival counterexample

Set the even-time even-column shears to zero and use the balanced odd-time
profile

\[
(1/3,1/3,-1/3,-1/3)
\]

on each odd time row, with unit volumes. Its quotient Hodge matrix is
non-diagonal. Nevertheless the same deleted edge gives

\[
P=\operatorname{diag}(33/40,0,33/40,0,33/40,0,33/40,0)
\]

at \(m=0,1/10,1,5\). This exact carrier refutes Block 160's historical
“only-flat” upgrade and is retained as a counterexample, without upgrading four
mass values to a universal mass theorem.

## Weight and interpolation results

At identity Hodge, arbitrary real healing weights annihilate all sixteen
theta-prime forms. Complex-weight controls produce nonzero theta-prime forms.
The real-weight result is a sufficient mechanism. The source does not solve the
full general-carrier vanishing equations and therefore states no necessity or
global iff.

For the displayed even/odd-column interpolation, the exact grid
\(\lambda=k/20\), \(-20\le k\le20\), contains a PSD point only at
\(\lambda=1\), at masses zero and one. This is a 41-point grid result. It is
not a statement about every real or complex \(\lambda\).

The even-column and odd-column endpoint forms have inertias \((4,4,0)\) and
\((2,4,2)\), in positive-zero-negative order. Since unitary congruence is an
invertible congruence and preserves inertia, this does prove that these two
displayed forms are not unitarily congruent. The historical criticism of that
inertia argument is withdrawn.

## Disposition

The specified quotient, exact kernel, curved mass-survival counterexample at
four masses,
real-weight sufficient mechanism, finite lambda grid, and inertia distinction
are retained. Absence of any physical sector or connection, global iff, and
continuum interpolation claims are withdrawn.
