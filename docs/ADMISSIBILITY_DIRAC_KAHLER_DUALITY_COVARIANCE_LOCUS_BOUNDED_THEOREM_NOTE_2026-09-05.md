---
claim_id: admissibility_dirac_kahler_duality_covariance_locus_bounded_theorem_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "Exact finite covariance calculations for the supplied eight-corner cell family under the 24 proper signed cubic rotations: the exterior lift, subgroup census, strict and sign-twisted linear parameter loci, star-line identity, overlap-sum transformation, and named controls. The calculation does not prove that the supplied cell inherits the Admissibility axiom's covariance and selects no cell, subgroup, assembly, parameter, premise, metric, action, spacetime, or dynamics."
depends_on:
  - admissibility_dirac_kahler_duality_parameters_principal_part_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_weighted_kernel_dispersion_bounded_theorem_note_2026-09-05
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py
---

# Proper-cubic covariance loci of the supplied cell form

**Historical block:** 215
**Repair date:** 2026-09-10
**Status:** corrected bounded theorem candidate; fresh execution and audit remain separate gates

**Claim type:** `bounded_theorem`

**Primary runner:**
[`scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py`](../scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py)

**Finite suppliers:** the calculation imports the corrected
[Block 214 principal-part construction](ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md), through it the corrected
[Block 213 finite construction](ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md), and the current
[Block 105 assembly formulas](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md). A dedicated helper supplies only the 24 determinant-one signed permutation matrices. These links identify fixed formulas; they do not adopt the suppliers' broader conclusions or historical parent chain. The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) are authority boundaries only.

The historical packet and cache are preserved byte-for-byte in the dated recovery record. Their old claims that every parent statement stood are historical dispositions. They are not current scientific inputs.

## Scope and result

Let `O` be the 24 determinant-one signed `3 x 3` permutation matrices. The runner builds their exterior action on the eight corners in order
`(empty,y,x,xy,t,ty,tx,txy)`. It checks the representation law, exact orders

```text
order 1: 1, order 2: 9, order 3: 8, order 4: 6,
```

and the complete 30-subgroup census in 11 conjugacy classes. This is a finite group computation.

For a lifted rotation `L` and a corner sign vector `E_R`, covariance means only

```text
(E_R L) H (E_R L)^T = H.
```

The runner solves the resulting linear constraints in the four supplied coordinates `(D07,D16,D25,D34)` at symbolic moduli. It runs both strict `E_R=I` and all 64 sign-twisted cases for each subgroup class. Whether this matrix identity is inherited from the Admissibility rule is an unproved antecedent.

The exterior-star signs are

```text
(+, +, -, +, +, -, +, +),
```

so the grade-one/grade-two star line is

```text
D16 = D34 = -D25,
```

with `D07` free. This is the same linear plane used by corrected Block 214. The overlap fold sees the four parameters through the sum `s=D07+D16+D25+D34`; the runner measures its transformation under the same finite lifts. Positivity and grade parity are reported controls and select no locus.

At the 64 sign cells the finite census finds 16 star-pattern cells; each has one strict `S3_body` subgroup whose shear-alive locus is the star line. It finds no strict tetrahedral shear-alive cell. These statements concern the enumerated cells and the exact covariance equation above.

No action, physical kernel, metric, light cone, continuum symmetry, propagation law, spacetime, or gravity structure is supplied. No subgroup, sign cell, assembly, reading, or parameter value is selected or registered.

## N1–N8 stress record

- **N1, alternative routes:** strict covariance, all sign twists, every subgroup conjugacy class, both supplied assemblies, and the flat/sign-cell controls are enumerated.
- **N2, wall independence:** group construction, exterior intertwining, star signs, and covariance constraints are checked separately. Parent theorem conclusions are not premises.
- **N3, hidden walls:** the moduli and four duality coordinates remain symbolic where claimed. Improper rotations, translations, and continuum rotations are outside scope.
- **N4, residual matching:** every locus is obtained from exact matrix residuals. The named counts and subspaces are compared to literals.
- **N5, rhetoric:** “covariance” always means the displayed finite matrix identity. It does not assert inherited physical covariance.
- **N6, partial closure:** the star line and 16-cell census remain useful even though no assembly or subgroup is chosen.
- **N7, steelman:** a physical interpretation would require an independently justified cell, dynamics, and symmetry action; none is inferred here.
- **N8, cross-cycle echo:** corrected Blocks 213/214 are content-bound as finite suppliers. Superseded historical assurances and the old “symbol never scalar” wording are archived only.

N5: The corrected Block 215 claim is finite exact covariance algebra on one supplied cell family: 24 proper signed rotations, 30 subgroups in 11 conjugacy classes, the exterior-star line D16 = D34 = -D25, strict and sign-twisted linear loci, and a 16-cell star-pattern census. Covariance means only (E_R L) H (E_R L)^T = H. No inheritance from the Admissibility axiom, premise adoption, subgroup selection, assembly choice, physical metric, action, spacetime, continuum, or dynamics is claimed; superseded parent assurances are historical only.
