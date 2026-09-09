# I1 Supplied Quadratic Static-Source Complete-Square Bridge

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py`](../scripts/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py)
**Cached log:**
[`logs/runner-cache/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.txt`](../logs/runner-cache/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.txt)

## Statement

On a finite periodic `Z^3` lattice with the zero mode projected out, given the
source-normalized leading quadratic action

```text
S[phi; J] = (1/(2 g^2)) <d phi, d phi> - <J, phi>,
```

and the graph Laplacian identity `<d phi, d phi> = <phi, L phi>`, completing
the square gives

```text
L phi_* = g^2 J,
S_eff[J] = -(g^2/2) <J, L^+ J>.
```

For two static source records with channel signs `s_1, s_2`, the
separation-dependent cross term is therefore

```text
V_cross(r) = -g^2 s_1 s_2 G(r),
```

where `G = L^+` is the zero-mean lattice Green kernel. With the existing
Green-kernel authority for `G(r) -> 1/(4 pi r)`, this supplied quadratic
substep yields the `-g^2 G(r)` scaling used in the I1 relocation discussion.

## What this establishes

- The stationary equation for the supplied action is `L phi = g^2 J`.
- The completed-square effective action is
  `S_eff[J] = -(g^2/2) <J, L^+ J>`.
- The two-source cross term is `V_cross(r) = -g^2 s_1 s_2 G(r)`.
- Source-amplitude scaling is quadratic and coupling scaling is exactly `g^2`
  inside this finite-lattice model.
- The graph-Laplacian small-`k` symbol has the native normalization leading to
  the continuum inverse-Laplacian coefficient `1/(4 pi)`.

## Boundary

This is a complete-square theorem for a supplied leading quadratic source
action. It does not derive the physical source-coupling normalization, the
gauge action, the general energy-readout bridge, a Wilson-loop transfer
statement, a Casimir assignment, a hierarchy magnitude, `u_0`, or any
phenomenological value. It adds no axiom, primitive, admitted input, or audit
verdict.

## Relation to I1

The I1 relocation row had a native-field-integration half and a general
energy-readout half. This bridge narrows the native-field-integration half:
once the leading source-normalized quadratic action is supplied, the
finite-lattice algebra gives the `-g^2 G(r)` cross term directly.

The general energy-readout bridge remains open. The physical source-coupling
normalization also remains an explicit premise of this finite calculation, not
a conclusion derived here.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the
  `Z^3` lattice background only.
- [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
  for the `Z^3` Green-kernel asymptotic `G(r) -> 1/(4 pi r)`.

The source-normalized quadratic action itself is the stated input of this
bounded theorem.

## Forbidden-imports check

No PDG value, fitted selector, observed hierarchy value, Planck-scale input, or
literature numerical comparator is consumed. The runner verifies only finite
matrix/FFT identities and the analytic inverse-Laplacian coefficient.

## Validation

Run:

```bash
python3 scripts/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
