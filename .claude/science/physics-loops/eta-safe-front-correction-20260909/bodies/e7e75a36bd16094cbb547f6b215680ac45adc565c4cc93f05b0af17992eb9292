# Scale-Reference Primitive

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta
**Status:** framework primitive declaration. Registered in
`docs/audit/data/axiom_premise_nodes.json` as
`scale_reference_primitive`. Explicit owner approval is recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.

## What This Declares

The framework takes exactly one dimensionful reference: a scale that converts
the framework's lattice-natural units to physical units. The chosen reference
is the Planck mass scale, `a^{-1} = M_Pl`.

This is a units conversion, not a physics axiom. It carries zero dimensionless
content: no mass ratio, coupling, mixing angle, phase, selector, readout
bridge, or empirical fit is supplied by it. A row whose only otherwise
non-retained dependency is this scale-reference primitive should not become
`retained_bounded` merely for using a ruler.

## Why It Is A Primitive

This declaration supplies the units conversion that the Lattice + Qubit +
Admissibility + Record baseline does not itself specify. Quantities on the
structural surface remain dimensionless or carry a power of the lattice
spacing `[a]^n` until that reference is supplied. No derivation of the chosen
physical scale is claimed here. The units reference is an approved primitive,
so it does not bound lanes whose dimensionless content is otherwise closed.

## What This Does Not Do

- It does not add or amend an axiom. The minimal framework baseline is the
  [four named axioms](MINIMAL_AXIOMS_2026-06-29.md): Lattice, Qubit,
  Admissibility, and Record.
- It does not assert `a/l_P = 1` as a derived theorem. The self-consistency
  question that the framework's natural unit equals the Planck length remains
  a separate open gravity derivation.
- It does not supply any dimensionless quantity. Dimensionless physics must
  derive from retained-grade framework content or remain conditional/open.
- It does not change any audit verdict. Audit status remains set only by the
  independent audit lane.

## Audit-Pipeline Treatment

The machine-readable rule is:

- `docs/audit/data/axiom_premise_nodes.json` lists framework axioms and
  explicitly approved framework primitives. These dependencies chain-satisfy
  without bounding downstream rows.
- no admission registry or third premise class exists. Every other scientific
  dependency must be retained-derived or remain conditional/open.

The scale-reference primitive belongs to the sole foundation registry.
