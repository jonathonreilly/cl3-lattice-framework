---
claim_id: admissibility_dirac_kahler_covariant_curved_cell_cone_bounded_theorem_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "Exact finite onsite-assembly calculations for 16 star-pattern cells and 26 named positive zero-parameter witnesses: universal star-line sufficiency from the symbolic odd-odd block, finite witness necessity from coefficient-ideal containment plus powers of both line generators, the coincidence-cell census, eight curve witnesses, and named branch and symmetry data. Necessity at arbitrary symbolic moduli, a selected cell or assembly, and any physical metric, cone, action, spacetime, continuum, or dynamics remain unclaimed."
depends_on:
  - admissibility_dirac_kahler_duality_covariance_locus_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_duality_parameters_principal_part_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_weighted_kernel_dispersion_bounded_theorem_note_2026-09-05
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py
---

# Covariant curved-cell finite cone calculations

**Historical block:** 216
**Repair date:** 2026-09-10
**Status:** corrected bounded theorem candidate; fresh execution and audit remain separate gates

**Claim type:** `bounded_theorem`

**Primary runner:**
[`scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py`](../scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py)

**Finite suppliers:** this runner imports the corrected
[Block 215 covariance construction](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md), the corrected
[Block 214 principal part](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md), the corrected
[Block 213 finite cell machinery](ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md), and the current
[Block 105 assembly formulas](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md). The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) supply no scientific premise.

## Corrected locus statement

For the onsite principal part `M=H0 D + D^T H0`, the odd-odd block at symbolic face signs and moduli contains exactly

```text
(D16 + D25) kt,
-(D16 - D34) kx,
-(D25 + D34) ky,
```

and its remaining row and column vanish. Therefore on

```text
D16 = D34 = -D25
```

that block vanishes at every supplied cell. The exact block determinant identity

```text
det [[A,B],[B^T,0]] = det(B)^2
```

then proves **sufficiency at symbolic moduli for every cell**.

Necessity is a finite witness result. The runner evaluates 26 positive zero-parameter witnesses: W1 moduli at the 16 star-pattern cells and all-plus control, the flat control, and the two transported curve classes across the eight rule-A cells. At each witness it forms every nonzero `kappa` coefficient of

```text
det M - det(B)^2.
```

All coefficients vanish after the star-line substitution, so the coefficient ideal is contained in the line ideal. The coefficient list also contains a nonzero scalar multiple of each square

```text
(D16-D34)^2, (D25+D34)^2.
```

These two containments prove that the radical is the star-line ideal at those 26 witnesses. The runner does not collect individual factors of arbitrary ideal generators and does not claim necessity at unsampled symbolic moduli.

The M-odd-block line itself is checked by linear rank/nullspace, not by the invalid historical factor-collection shortcut.

## Cell census and finite witnesses

The 16 star masks are

```text
2, 5, 11, 12, 16, 23, 25, 30, 33, 38, 40, 47, 51, 52, 58, 61.
```

They coincide with the corrected Block 213 coincidence-curve cells. The eight positive rule-A masks are

```text
2, 11, 16, 25, 38, 47, 52, 61.
```

At each rule-A mask the transported named curve point is positive definite and has one strict `S3_body` stabilizer in the finite covariance sense. The Hodge readings are proportional with ratios `32/27` or `27/32`; on the star line the determinant is the fourth power of the corresponding supplied quadric times `64/81` or `9/16`. “One metric's cone” is only shorthand for this polynomial proportionality and names no physical metric or light cone.

## Branch values

At the named `lambda=1/4`, `D07=0` points, the squared-pencil eigenvalues are `Q(kappa)` times these normalized branch-constant multisets (away from `Q=0`; the polynomial identity extends through `Q=0`):

```text
L+-:  1 x2, 128/99 x2, 16/11 x4
L-+:  1 x2, 108/119 x2, 144/119 x4
```

Thus there are four branch slots counted with their transverse repetition and **three distinct values** at each displayed point. The runner does not assert three distinct values at every specialization; crossings remain possible. With `D07=1/4` the separately measured values are retained. The line rescaling and positivity bounds are conditional on the named curve construction: `lambda^2 < v0 v1` and `D07^2 < v0/v1`.

No result here selects the onsite assembly, cell, subgroup, parameter value, or reading. No action, physical kernel, spacetime cone, propagation law, continuum, dynamics, or gravity structure is supplied.

## N1–N8 stress record

- **N1:** sufficiency and necessity use different routes; the latter is run at all 26 declared witnesses.
- **N2:** the symbolic odd-odd-block lemma, generic block identity, finite certificate, cell census, positivity, stabilizers, branches, and symbol tests are separate gates.
- **N3:** symbolic-moduli necessity is explicitly left open; positivity bounds delimit the branch formulas.
- **N4:** each finite radical claim requires coefficient containment and a power of each line generator. Mere factor collection is forbidden.
- **N5:** exact-locus rhetoric always names the 26 witnesses unless the statement is the universal sufficiency lemma.
- **N6:** the universal sufficiency line, finite witness census, branch ranks, multiplicities, and symmetry data remain useful without a universal locus theorem.
- **N7:** a stronger physical or global theorem would require an independent construction and all-moduli proof.
- **N8:** superseded parent assurances and historical cache grades are archived; corrected Blocks 213–215 are content-bound only for the definitions actually used.

N5: The corrected Block 216 claim separates universal sufficiency from finite necessity. The symbolic odd-odd block and the generic block determinant identity prove star-line sufficiency at every supplied cell. Necessity is certified only at 26 named positive zero-parameter witnesses by coefficient-ideal containment plus nonzero multiples of both line-generator squares. The displayed squared-pencil rows have four branch slots counted with repetition and three distinct values at the named D07 = 0 points. No all-moduli necessity, cell or assembly selection, premise adoption, physical metric, light cone, action, spacetime, continuum, or dynamics is claimed.
