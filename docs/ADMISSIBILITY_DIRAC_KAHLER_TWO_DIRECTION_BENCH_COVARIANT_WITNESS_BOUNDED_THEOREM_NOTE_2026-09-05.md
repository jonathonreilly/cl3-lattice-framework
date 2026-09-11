---
claim_id: admissibility_dirac_kahler_two_direction_bench_covariant_witness_bounded_theorem_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "Exact finite calculations on one (4,4,2) periodic bench at the named L+- cell, W1, and flat controls: direct/Bloch characteristic-polynomial agreement, the onsite Bloch/principal-part similarity, the three-point branch ratios at L+-, normalized-spectrum comparison between the pure-t and pure-x W1 blocks, and the overlap fold at the four sampled points. Other cells, extents, momenta, parameter values, universal branch laws, and physical interpretations remain open."
depends_on:
  - admissibility_dirac_kahler_overlap_assembly_covariant_cells_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_covariant_curved_cell_cone_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_duality_covariance_locus_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_duality_parameters_principal_part_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_weighted_kernel_dispersion_bounded_theorem_note_2026-09-05
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py
---

# Two-direction finite bench at the named L+- witness

**Historical block:** 218
**Repair date:** 2026-09-10
**Status:** corrected bounded theorem candidate; fresh execution and audit remain separate gates

**Claim type:** `bounded_theorem`

**Primary runner:**
[`scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py`](../scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py)

**Finite suppliers:** the calculation imports corrected
[Block 217](ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 216](ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 215](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 214](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md), and
[Block 213](ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md), with the current
[Block 105 finite assembly formulas](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md). The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) are context boundaries and supply no scientific premise here.

## Finite bench and onsite identity

The runner constructs the `(4,4,2)` periodic bench with 32 sites. Its Bloch points are

```text
(1,1,1), (1,i,1), (i,1,1), (i,i,1).
```

The last coordinate has extent two and contributes no link. For every declared cell, assembly, and reading, the runner compares the direct degree-32 characteristic polynomial with the product of its four degree-8 Bloch characteristic polynomials. All 20 declared comparisons use exact arithmetic over `QQ(sqrt(6))` and `QQ(sqrt(6),i)`.

At each point the raising block obeys

```text
d_B(z) = sum_mu (z_mu-z_mu^-1)/2 D(e_mu) = i D(kappa_z),
```

and the onsite Hodge block is `Z^-1 H0 Z`. Since the supplied raising matrices square to zero and anticommute, the onsite pencil block has the characteristic polynomial of

```text
(H0^-1 M(kappa_z))^2.
```

This includes `kappa_z=e_t+e_x` at `(i,i,1)`. For the chosen cells `H0` is invertible. With `Z=diag(z^c)`, the onsite Bloch matrix satisfies `Z H_B Z^-1=H0`, while the declared phases give `Z D Z^-1=iD` and `Z D^T Z^-1=-iD^T`. Put `A=H0^-1 D^T H0`. Conjugation sends the pencil operator to `-D+A`; since `D^2=A^2=0`,

```text
-(-D+A)^2 = (D+A)^2 = (H0^-1 M(kappa_z))^2.
```

Thus the similarity is an exact finite statement at the sampled phases, not a continuum or small-momentum limit.

## Named L+- witness

At the named L+- cell and line point, the onsite pencil block has nonzero multisets

```text
pure t:  9/8 x2, 16/11 x2, 18/11 x4
pure x:  9/8 x2, 16/11 x2, 18/11 x4
mixed:   3/2 x2, 64/33 x2, 24/11 x4.
```

Dividing by the supplied quadratic values `Q=(9/8,9/8,3/2)` gives the same normalized multiset

```text
1 x2, 128/99 x2, 16/11 x4
```

at these three points. Polarization gives the sampled cross entry

```text
G1_tx = (3/2-9/8-9/8)/2 = -3/8.
```

This is a result for one named cell at three sampled directions. It does not make the historical parent locus claims universal and supplies no physical branch law.

## Corrected W1 control

For an 8-dimensional monic characteristic polynomial `chi_z(lambda)` and nonzero supplied quadratic value `Q_z`, define its normalized monic spectrum polynomial by

```text
chi_hat_z(u) = Q_z^-8 chi_z(Q_z u).
```

At the pure-t and pure-x W1 points, `Q_t=Q_x=16/15`, while the primitive factor patterns are respectively

```text
(15 lambda-16)^2 P3_t(lambda)^2
(15 lambda-16)^2 (385 lambda-256)^2 P2_x(lambda)^2.
```

Their normalized monic polynomials differ. Therefore these two directions do not share one normalized spectrum on this finite control. This cross-direction comparison is the control result. Irrationality, rationality, or nonmembership in a previously listed witness set at one point cannot by itself establish or refute a direction-independent branch constant.

## Primitive factors and monic polynomials

The runner's `charpoly_shape` returns primitive integer factors and discards the scalar needed to reconstruct the monic characteristic polynomial. The displayed products have these divisors:

| block | primitive product | divisor for the monic polynomial |
| --- | --- | --- |
| L+- onsite form, pure | `P4(lambda)^2` | `55296^2` |
| L+- onsite form, mixed | `P4(lambda)^2` | `864^2` |
| L+- overlap pencil, mixed line | `P2(lambda)^4` | `17837^4` |
| W1 onsite pencil, pure t | `(15 lambda-16)^2 P3(lambda)^2` | `(15*4801335)^2` |
| W1 onsite pencil, pure x | `(15 lambda-16)^2(385 lambda-256)^2P2(lambda)^2` | `(15*385*12471)^2` |
| W1 onsite pencil, mixed | `(5 lambda-8)^2P3(lambda)^2` | `(5*4801335)^2` |

The direct/Bloch equalities use the actual monic polynomials. These primitive products are factorization shapes up to their stated nonzero scalars.

## Overlap fold and scope

At symbolic signs, moduli, and parameters, the overlap fold is parameter-free at the two pure points. At the mixed point its cross-parity block depends on

```text
(-D07-D16+D25+D34)/4.
```

The exact line-versus-zero comparisons and the distinct pure-point overlap multisets are retained as finite matrix facts. They select no assembly, cell, subgroup, reading, or parameter value.

No action, physical kernel, metric, light cone, dispersion law, spacetime, dynamics, gravity structure, continuum limit, or premise is supplied or adopted.

## N1–N8 stress record

- **N1:** direct/Bloch agreement, onsite similarity, witness ratios, W1 normalized-spectrum comparison, and overlap-fold dependence use separate residuals.
- **N2:** the W1 conclusion compares complete normalized monic polynomials across two directions; it does not use one selected root.
- **N3:** the `y` direction, other extents, other cells, other parameter points, and symbolic branch laws remain open.
- **N4:** primitive integer factor shapes are paired with the exact leading-coefficient divisors required for monic polynomials.
- **N5:** “constant times `Q`” is a cross-direction statement only after a common normalized spectrum is tested.
- **N6:** the L+- multisets, cross term, exact onsite identity, and overlap-fold facts survive independently of the W1 control wording.
- **N7:** a physical branch or cone interpretation would require independent dynamics and a supplied reading.
- **N8:** corrected Blocks 213–217 are content-bound finite suppliers; historical universal assurances and checker grades remain archived provenance.

N5: The corrected Block 218 claim is finite. On one (4,4,2) bench at the named L+- witness, the onsite pencil block has the stated three normalized branch constants across the sampled t-x points and the mixed-point identity holds. At W1, the normalized monic characteristic polynomials at the pure-t and pure-x points differ even though Q is 16/15 at both; this cross-direction mismatch, rather than any single irrational or rational eigenvalue, is the control result. Primitive factor products are divided by their recorded leading-coefficient products before being called monic characteristic polynomials. No parent theorem, assembly choice, premise adoption, physical metric, cone, action, spacetime, continuum, dispersion law, or dynamics is claimed.
