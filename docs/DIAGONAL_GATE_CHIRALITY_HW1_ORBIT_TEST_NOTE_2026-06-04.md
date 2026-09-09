# Three-label anticommutation: real and complex domains

**Date:** 2026-06-04; source correction 2026-09-09
**Type:** bounded_theorem
**Scope:** supplied finite mathematics; no physical selection or audit verdict.
**Primary runner:** [diagonal_gate_chirality_hw1_orbit_test.py](../scripts/diagonal_gate_chirality_hw1_orbit_test.py)
**Cached output:** [diagonal_gate_chirality_hw1_orbit_test.txt](../logs/runner-cache/diagonal_gate_chirality_hw1_orbit_test.txt)
**Original history:** [exact original and correction record](../.claude/science/physics-loops/diagonal-adjacency-7870-correction-20260909/CORRECTION_HISTORY.md).

Supply a cyclic 3×3 shift R and `Gamma=(2/3)J-I`, where J is the all-ones
matrix. Then `Gamma^2=I` with eigenvalues `+1,-1,-1`, and
`Gamma=(-1/3)I+(2/3)(R+R^2)`. This is a chosen grading on a three-label
space. Physical chirality and a physical generation carrier are not supplied.

## Simultaneous equivariance and anticommutation

For any real or complex matrix H, `[H,R]=0` implies `[H,Gamma]=0`, because
Gamma is a polynomial in R. If also `{H,Gamma}=0`, then `2H Gamma=0` and,
since Gamma is invertible, H=0. This proof does not require Hermiticity.
It recovers the finite identity in the
[equivariant-anticommuting note](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
without importing that note's historical status or other physical discussion.

## Real symmetric restriction

Let `u=(1,1,1)`. Gamma is +1 on span(u) and -1 on its orthogonal complement.
A real symmetric anticommuting matrix has only off-diagonal blocks between
these eigenspaces. Therefore it is exactly

```
H = u v^T + v u^T,       v in R^3, u.v=0.
```

This family has real dimension 2. Its coordinate diagonal is `2v`, so a
zero-diagonal real symmetric member is zero. The numerical runner checks
this zero slice with a required equality, not a branch accepting either
answer. Each nonzero member breaks C3-equivariance by the preceding proof;
testing representatives alone would not establish that universal statement.
The equal-weight real hopping matrix `R+R^2=J-I` is nonzero and commutes
with R, so it cannot anticommute with Gamma.

## Complex Hermitian counterexample

The zero-diagonal conclusion does not extend to all complex Hermitian hops.
Take `v=(1,-1,0)` and

```
H = i(u v^T - v u^T)
  = i [[0,-2,-1],[2,0,1],[1,-1,0]].
```

H is nonzero, Hermitian, and has zero diagonal. Since Gamma u=u and
Gamma v=-v, its anticommutator with Gamma vanishes exactly. It breaks C3.
Thus complex phases permit a pure off-diagonal anticommuting matrix while
leaving the simultaneous equivariance theorem intact. The old assertion
that every inter-label hop requires on-site terms is withdrawn. The actual
matrix, Hermiticity, diagonal, anticommutator and broken equivariance are
checked in the corrected runner.

## Different factors and remaining scope

On `C^3 tensor C^2`, `Gamma tensor I_2` and `I_3 tensor sigma_z` are different
commuting gradings. `I_3 tensor sigma_x` anticommutes with the second and
not the first. A separate-factor construction therefore has a different
hypothesis; neither a physical realization nor its exclusion follows here.
Likewise changing equivariance, the grading, phases or the carrier changes
the problem. No global chirality no-go, unique escape, or exhaustive route
list is claimed. Spatial diagonal motion and BZ-corner mixing have not been
identified with these matrix entries.

This note does not change axioms. The [current four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is the
current interpretation boundary. These are finite supplied matrices, not a
physical carrier, clock, readout law or permanent Record formation derivation.
