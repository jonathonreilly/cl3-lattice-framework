# Diagonal adjacency: finite geometry and separate model choices

**Date:** 2026-06-04; source correction 2026-09-09
**Type:** meta
**Scope:** supplied finite mathematics; no physical selection or audit verdict.
**Primary runner:** [diagonal_lattice_scoping_enumerator.py](../scripts/diagonal_lattice_scoping_enumerator.py)
**Cached output:** [diagonal_lattice_scoping_enumerator.txt](../logs/runner-cache/diagonal_lattice_scoping_enumerator.txt)
**Original history:** [exact original and correction record](../.claude/science/physics-loops/diagonal-adjacency-7870-correction-20260909/CORRECTION_HISTORY.md).

What changes when diagonals are allowed? First specify what a diagonal is.
A segment in a cube, a spatial displacement, and a matrix element between
three abstract labels are different objects. This note is a
thought-experiment surface, not a derived theorem about a physical lattice.
Its enumeration statements below are exact finite combinatorics.

## Finite geometry

On `{0,1}^3`, the 28 unordered distinct vertex pairs partition by Hamming
distance into 12 edges, 12 face diagonals, and 4 body diagonals. The latter
four pairs are `000–111`, `100–011`, `010–101`, and `001–110`.
The twelve face diagonals are the two diagonals of each of the six faces:

| fixed coordinate | two pairs on its zero face | two pairs on its one face |
|---|---|---|
| z | 000–110, 100–010 | 001–111, 101–011 |
| y | 000–101, 100–001 | 010–111, 110–011 |
| x | 000–011, 010–001 | 100–111, 110–101 |

For the per-site Moore neighborhood on the separately supplied `Z^3`, the
nonzero displacements in `{-1,0,1}^3` partition into 6 vectors of squared
length 1, 12 of squared length 2, and 8 of squared length 3. Including the
successive families gives coordination counts 6, 18, and 26. These are not
the counts of unordered segments in one cube.
On the infinite spatial lattice, NN graph distance is the l1 norm and full
Moore graph distance is the infinity norm: `d_Moore <= d_NN <= 3 d_Moore`.
Thus the two metrics define the same class of finite-range supports, with
different range bounds. This finite-range comparison does not select an
interaction, dynamics, or an amendment to the lattice axiom.

The signed-permutation group is `(Z_2)^3 semidirect S_3`, of order 48.
On cube vertices its sign flips act around the cube center (bit complements).
On displacement vectors they act around the origin. Its finite orbits are:

| object | orbit size | stabilizer order |
|---|---:|---:|
| cube edge | 12 | 4 |
| cube face diagonal | 12 | 4 |
| cube body diagonal | 4 | 12 |
| displacement `<100>` | 6 | 8 |
| displacement `<110>` | 12 | 4 |
| displacement `<111>` | 8 | 6 |

Each row has orbit size times stabilizer order 48. The runner enumerates
the complete sets, explicit diagonal lists and actions.

## The three-label model and the spatial model

The abstract weight-one set `T={100,010,001}` has pairwise Hamming distance
2. Coordinate permutations preserve it and act transitively; a cyclic
permutation already cycles all three points. This agrees with the bare
finite-set scope of the
[Hamming-orbit note](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md).
It supplies no physical generation or Brillouin-zone realization.

In particular, a spatial face-diagonal hopping term need not mix momentum
corners. For a translation-invariant operator
`(H psi)(x)=sum_d t_d psi(x+d)` on a periodic lattice, a character
`psi_k(x)=exp(i k.x)` has eigenvalue `sum_d t_d exp(i k.d)`.
Thus it remains diagonal in momentum even when `d` includes diagonals.
An operator on the abstract three labels requires a separate supplied map
before it can be interpreted as a spatial or momentum-space operator.

## Three choices retained for comparison

- L1: define a diagonal transporter as a fixed ordered word in supplied NN
  link variables. This adds no independent connection variable, but a new
  action term using that word may still change dynamics.
- L2: supply extra variables or operators on a chosen carrier. The two
  matrix-generator families tested in the L2 note are examples; they do not
  exhaust connections, carriers, or dynamics.
- L3: choose weights for a three-label circulant matrix. Counting paths or
  geometric distances does not by itself prescribe those weights.

This note does not change axioms. The [current four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) governs
framework interpretation; it is not a derivation of any of these extra
choices. Physical carrier, connection, action, clock, Born/readout law and
permanent Record formation are unproved suppliers here. No current primitive
or admission selects these models. Formal audit is deferred; status authority
remains the independent audit lane only. Historical schedules and pass counts
in the preserved originals have no present authority.
