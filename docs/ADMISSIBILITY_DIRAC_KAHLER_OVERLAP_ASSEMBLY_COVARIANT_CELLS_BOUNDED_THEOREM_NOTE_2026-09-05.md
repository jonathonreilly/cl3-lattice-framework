---
claim_id: admissibility_dirac_kahler_overlap_assembly_covariant_cells_bounded_theorem_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "Exact finite overlap-assembly calculations at eight transported curve witnesses plus W1 and flat controls: fold dependence on s, strict and sign-twisted stabilizers, finite union-locus certificates from a univariate coefficient gcd and square-free part, the s=0 two-quadric factorization, generic joint factorization in (s,kappa), and a (4,2,2) bench with monic characteristic-polynomial normalization. Exceptional nonzero-s specializations, other cells or benches, assembly selection, and physical interpretations remain open."
depends_on:
  - admissibility_dirac_kahler_covariant_curved_cell_cone_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_duality_covariance_locus_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_duality_parameters_principal_part_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_weighted_kernel_dispersion_bounded_theorem_note_2026-09-05
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py
---

# Overlap assembly at the covariant finite cells and bench

**Historical block:** 217
**Repair date:** 2026-09-10
**Status:** corrected bounded theorem candidate; fresh execution and audit remain separate gates

**Claim type:** `bounded_theorem`

**Primary runner:**
[`scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py`](../scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py)

**Finite suppliers:** the live calculation uses corrected
[Block 216](ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 215](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md),
[Block 214](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md), and
[Block 213](ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md), with the current
[Block 105 finite assembly formulas](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md). The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) are context boundaries only.

## Fold and finite locus

At symbolic face signs and moduli, the overlap fold depends on the four duality coordinates only through

```text
s = D07 + D16 + D25 + D34.
```

Its cross-parity block is `(s/4) P111`; at `s=0` its remaining off-diagonal entries are the twelve measured two-flip couplings. The flat control is `I+(s/4)P111`.

At each of the eight rule-A curve witnesses plus the all-plus W1 and flat controls, the runner computes the nonzero `kappa` coefficients of

```text
det M(s,kappa) - det(B(kappa))^2.
```

Those coefficients are univariate polynomials in `s`. Their monic gcd over `QQ[s]` or `QQ(sqrt(6))[s]` is `s^2`; its square-free part is `s`. This PID calculation proves the union locus `s=0` at these **ten witnesses**. It replaces the invalid historical practice of collecting irreducible factors from separate ideal generators. No all-moduli or all-cell locus follows.

The finite stabilizer calculation reports a trivial strict overlap stabilizer and a sign-twisted `D4_face` at the eight curve witnesses. It also retains the W1 and flat controls and the explicitly measured shear relations. These are exact identities for the supplied matrices and select no assembly.

## Factorization scope

At `s=0`, `det M=det(B)^2`. At the eight curve witnesses, `det B=Q_+Q_-` with two distinct rational quadrics. They differ only in the sign of the `kt ky` coefficient; they are not related by a coordinate sign flip and neither is proportional to the onsite supplied quadric.

Factoring `det M` jointly in `(s,kt,kx,ky)` gives one factor of degree two in `s` and four in `kappa`, squared, over the stated coefficient field. This is a **generic polynomial factorization statement**. It does not prove that every specialization at `s != 0` remains irreducible, nor does it exclude every exceptional single-quadric specialization.

## The finite `(4,2,2)` bench

The runner retains all 16 exact direct/Bloch characteristic-polynomial comparisons at the named witness and controls. The displayed integer factor shapes must be normalized to describe the monic characteristic polynomials:

| row | primitive product | monic divisor |
| --- | --- | --- |
| L+- onsite form | `lambda^8 P4(lambda)^2` | `55296^2` |
| W1 onsite form | `lambda^8 P4(lambda)^2` | `129600^2` |
| W1 onsite pencil | `lambda^8 (15 lambda-16)^2 P3(lambda)^2` | `(15*4801335)^2` |
| flat onsite form | `lambda^8 (4 lambda^2-9 lambda+4)^2 (16 lambda^2-33 lambda+16)^2` | `(4*16)^2` |

The runner's direct-versus-Bloch and principal-symbol comparisons already use the actual monic polynomials. The L+- onsite pencil multiset is

```text
0 x8, 9/8 x2, 16/11 x2, 18/11 x4.
```

The overlap bench at the named nonzero Bloch point is parameter-free in this finite construction. No continuum or small-momentum limit is taken.

No action, physical kernel, metric, light cone, dispersion law, spacetime, dynamics, gravity structure, cell, subgroup, assembly, reading, or parameter value is supplied or selected.

## N1–N8 stress record

- **N1:** fold, stabilizer, univariate-locus, `s=0` factorization, generic joint factorization, bench, and principal-symbol checks use separate residuals.
- **N2:** the union locus uses an actual gcd and square-free part, independent of the generic factorization claim.
- **N3:** exceptional specialized values of `s`, other cells, other benches, and other extents remain open.
- **N4:** primitive factor shapes and monic characteristic polynomials are explicitly separated by their leading-coefficient divisors.
- **N5:** “generic irreducible factor” never means every nonzero specialization.
- **N6:** the `s=0` pair, finite stabilizers, bench multisets, and exact Bloch/direct identities survive without the stronger specialization claim.
- **N7:** a physical cone or assembly decision would need independent dynamics and interpretation.
- **N8:** parent corrections are content-bound as finite suppliers; historical ledger assurances and caches remain archived provenance.

N5: The corrected Block 217 claim is finite. At eight curve witnesses plus W1 and flat controls, the univariate coefficient gcd is s^2 and its square-free part is s, certifying the locus s = 0 only at those ten witnesses. The joint factorization in (s,kappa) is generic and does not imply irreducibility at every nonzero-s specialization. Primitive bench factor shapes are divided by their stated leading-coefficient squares to obtain monic characteristic polynomials. No assembly selection, premise adoption, physical cone, action, spacetime, continuum, dispersion law, or dynamics is claimed.
