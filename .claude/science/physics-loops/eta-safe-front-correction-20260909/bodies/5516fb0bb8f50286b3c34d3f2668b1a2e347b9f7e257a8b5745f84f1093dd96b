# Kinetic-Isotropy Primitive

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-09
**Type:** meta
**Status:** framework primitive declaration. Registered in
`docs/audit/data/axiom_premise_nodes.json` as
`kinetic_isotropy_primitive`. Explicit owner approval is recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.

## What This Declares

The framework takes one structural graining fact: the emergent evolution tick is
grained on the same footing as the spatial lattice edge. Concretely, the matter
kinetic normalization is space-time isotropic,

```text
    c_t = c_s,
```

equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are
computed is hypercubic-symmetric (the Osterwalder-Schrader OS0 kinetic
normalization). One tick is one edge in **form**, not only in spacing.

This is a structural statement about the regulator geometry, the time-direction
analogue of the `LATTICE` axiom's spatial **cubic adjacency** `a_x = a_y = a_z`.
It carries no dimensionless dynamical content: no mass ratio, coupling, mixing
angle, phase, selector, readout bridge, or empirical fit is supplied by it. It
is not a fourth spatial dimension, not a new dynamics, and not a re-axiomatization
of time: the framework's time remains emergent and derived (the single-clock
codimension-1 evolution theorem); this primitive fixes only the one dimensionless
graining ratio relating that emergent time to space.

## Why It Is A Primitive

Within this declaration, `c_t = c_s` is supplied rather than derived. The
Lattice + Qubit + Admissibility + Record baseline, emergent single-clock
evolution, reflection positivity, scale reference, and records' causal order
are not used here as a derivation of that equality. This primitive records the
structural graining choice explicitly; any derivation of it would require a
separate theorem.

The adjacent quantities are *not* supplied here and are recorded only for
contrast:

- the **absolute** scale belongs to the single approved scale-reference primitive
  (`a^{-1} = M_Pl`);
- any **spacing** ratio or reachability claim lives in its own derivation row.

What remains genuinely free is the kinetic **form** ratio `c_t / c_s`. A theory
that grains space but leaves the kinetic form temporally anisotropic is the
lopsided surface relevant to marginal Lorentz-violation naturalness questions.
The primitive chooses the symmetric OS0 kinetic form explicitly. This is the same
broad category of dimensionless **structural** premise the framework already
accepts at axiom grade for space (cubic adjacency), supplied here for the
emergent time direction. Consequences for Collins-style marginal anisotropy,
radiative stability, or full Lorentz restoration remain separate theorem/support
claims; they are not supplied by this primitive declaration.

## What This Does Not Do

- It does not add or amend an axiom. The minimal framework baseline is the four
  named axioms in `MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit,
  Admissibility, and Record.
- It does not re-axiomatize time. The emergent single-clock evolution remains
  derived; this primitive normalizes only the one graining ratio `c_t / c_s`.
- It does not supply any dimensionless dynamical quantity. No mass ratio,
  coupling, mixing angle, phase, or selector is supplied; dimensionless physics
  must derive from retained-grade framework content or remain conditional/open.
- It does not supply the absolute scale (`scale_reference_primitive`) or the
  spacing ratio (derived from the no-diagonal clause); it supplies only the
  kinetic-form isotropy.
- It does not change any audit verdict. Audit status remains set only by the
  independent audit lane.

## Audit-Pipeline Treatment

The machine-readable rule is:

- `docs/audit/data/axiom_premise_nodes.json` lists framework axioms and
  explicitly approved framework primitives. These dependencies chain-satisfy
  without bounding downstream rows.
- no admission registry or third premise class exists. Every other scientific
  dependency must be retained-derived or remain conditional/open.

The structural purity guard `docs/audit/scripts/check_axiom_premise_clean.py`
keeps this source note inside the approved-premise boundary (no framework-rule or
ratification clauses).

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) — the four-axiom
  baseline whose spatial cubic adjacency this primitive parallels in the time
  direction.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the
  sibling primitive supplying the single dimensionful anchor. It supplies units;
  this primitive supplies only the dimensionless kinetic-form ratio.
