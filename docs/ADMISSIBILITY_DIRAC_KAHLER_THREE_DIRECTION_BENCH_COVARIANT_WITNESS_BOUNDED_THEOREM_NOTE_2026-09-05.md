---
claim_id: admissibility_dirac_kahler_three_direction_bench_covariant_witness_bounded_theorem_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "Exact finite calculations on one (4,4,4) periodic bench at the named L+- cell, two named rescalings, W1, and flat controls: declared direct/Bloch characteristic-polynomial comparisons, onsite Bloch/principal-part similarity, seven-point L+- branch ratios and quadratic read-off, normalized-spectrum comparison between pure-t and pure-x W1 blocks, and overlap-fold dependence. Other cells, extents, parameter values, universal branch laws, and physical interpretations remain open."
depends_on:
  - admissibility_dirac_kahler_two_direction_bench_covariant_witness_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_overlap_assembly_covariant_cells_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_covariant_curved_cell_cone_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_duality_covariance_locus_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_duality_parameters_principal_part_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_weighted_kernel_dispersion_bounded_theorem_note_2026-09-05
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_three_direction_bench_covariant_witness_2026_09_05.py
---

# Three-direction finite bench at the named L+- witness

**Historical block:** 219
**Repair date:** 2026-09-10
**Status:** corrected bounded theorem candidate; fresh execution and audit remain separate gates

**Claim type:** `bounded_theorem`

**Primary runner:**
[`scripts/admissibility_dirac_kahler_three_direction_bench_covariant_witness_2026_09_05.py`](../scripts/admissibility_dirac_kahler_three_direction_bench_covariant_witness_2026_09_05.py)

**Finite suppliers:** the calculation imports corrected
[Block 218](ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 217](ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 216](ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 215](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 214](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md), and
[Block 213](ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md), with the current
[Block 105 finite assembly formulas](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md). The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) supply no scientific premise here.

## Finite bench and onsite identity

The `(4,4,4)` bench has 64 sites and the eight Bloch points in `{1,i}^3`. For the 14 declared constructions, the Bloch products have degree 64; the nine declared direct characteristic polynomials are compared exactly with those products. The zero point contributes eight zeros.

The raising block obeys

```text
d_B(z) = sum_mu (z_mu-z_mu^-1)/2 D(e_mu) = i D(kappa_z)
```

at all eight points, including `kappa_z=e_t+e_x+e_y`. For the chosen cells `H0` is invertible. With `Z=diag(z^c)`, the onsite Bloch matrix satisfies `Z H_B Z^-1=H0`, while the sampled phases give `Z D Z^-1=iD` and `Z D^T Z^-1=-iD^T`. Put `A=H0^-1 D^T H0`. Conjugation sends the pencil operator to `-D+A`; since `D^2=A^2=0`,

```text
-(-D+A)^2 = (D+A)^2 = (H0^-1 M(kappa_z))^2.
```

This proves the finite similarity identity at the sampled phases.

## Named L+- witness and rescalings

At the line point, the nonzero onsite-pencil multisets are

```text
pure t, x, y and triply mixed:  9/8 x2, 16/11 x2, 18/11 x4
doubly mixed tx, ty, xy:         3/2 x2, 64/33 x2, 24/11 x4.
```

Dividing by the seven supplied values of `Q=kappa^T G1 kappa` gives the common normalized multiset

```text
1 x2, 128/99 x2, 16/11 x4.
```

The three pure and three doubly mixed values read the six entries

```text
G1_tt=G1_xx=G1_yy=9/8,
G1_tx=G1_ty=G1_xy=-3/8.
```

The triply mixed value is the finite consistency check `3(9/8)+6(-3/8)=9/8`.

Two named rescalings are retained. At line parameter `lambda=1/2`, the normalized constants are `{1 x2,16/9 x2,2 x4}`. At `D07=1/4`, they are `{128/119 x2,128/99 x2,16/11 x4}`. The runner checks the stated leading minors before using the first point. These are results at named points, not a universal parameter theorem.

## Corrected W1 control

For each nonzero W1 point define

```text
chi_hat_z(u) = Q_z^-8 chi_z(Q_z u),
```

where `chi_z` is the monic degree-8 onsite-pencil characteristic polynomial. At pure t and pure x, `Q_t=Q_x=16/15`, but their normalized monic characteristic polynomials have different factor-degree patterns: the former contains an irreducible cubic, while the latter contains an additional linear factor and an irreducible quadratic. Hence no one normalized spectrum covers even those two sampled directions.

At the triply mixed point the primitive factor product is

```text
(5 lambda-8)^2 (165 lambda-256)^2
(4157 lambda^2-26952 lambda+43008)^2.
```

Its monic divisor is `(5*165*4157)^2`. The ratio `(256/165)/(8/5)=32/33` is a constant and is not a counterexample to proportionality at a single point. The valid control conclusion comes from comparing complete normalized monic polynomials across directions.

## Overlap fold and finite scope

The overlap fold is parameter-free at the three pure points and the triply mixed point. At the three doubly mixed points its cross-parity block depends respectively on

```text
(-D07-D16+D25+D34)/4,
(-D07+D16-D25+D34)/4,
(-D07+D16+D25-D34)/4.
```

The line-versus-zero comparisons and the recorded overlap multisets remain finite matrix facts. They select no assembly, cell, subgroup, reading, or parameter value.

No action, physical kernel, metric, light cone, dispersion law, spacetime, dynamics, gravity structure, continuum limit, or premise is supplied or adopted.

## N1–N8 stress record

- **N1:** direct/Bloch comparisons, onsite similarity, seven-point ratios, rescalings, W1 normalized-spectrum comparison, and overlap-fold dependence use separate residuals.
- **N2:** the W1 negative result compares complete normalized monic polynomials across pure t and pure x.
- **N3:** other cells, extents, momenta, rescalings, parameter values, and symbolic branch laws remain open.
- **N4:** primitive products are kept distinct from monic characteristic polynomials; the triply mixed divisor is explicit.
- **N5:** a value at one nonzero `Q` point always has some pointwise ratio to `Q`; a branch-constant claim requires cross-direction coherence.
- **N6:** the L+- ratios, quadratic read-off, rescalings, onsite identity, and overlap-fold facts survive independently of the corrected W1 argument.
- **N7:** a physical metric or propagation interpretation would require independent dynamics and a supplied reading.
- **N8:** corrected Blocks 213–218 are content-bound finite suppliers; historical “all STAND” and universal narratives remain archived provenance.

N5: The corrected Block 219 claim is finite. On one (4,4,4) bench at the named L+- witness, the seven sampled onsite-pencil blocks have the stated normalized branch multiset, the six quadratic entries and triply mixed consistency check, and the two named rescalings. At W1, pure-t and pure-x have different normalized monic characteristic polynomials even though Q is 16/15 at both; this cross-direction mismatch is the control result. The triply mixed ratio 32/33 is a constant and is not used as a pointwise counterexample. Primitive products are divided by their recorded leading-coefficient products before being called monic characteristic polynomials. No parent theorem, assembly choice, premise adoption, physical metric, cone, action, spacetime, continuum, dispersion law, or dynamics is claimed.
