---
claim_id: diagonal_lattice_scoping_note_2026-06-04
claim_type_author_hint: meta
---

# Diagonal-Lattice Adjacency — Scoping Note (Thought-Experiment Surface)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (scoping / thought-experiment surface)
**Status:** source-note proposal awaiting independent audit handling. This note
defines a thought-experiment surface; it does **not** change axioms and does
**not** assert a derived theorem.
**Status authority:** independent audit lane only. This note does not set or
predict an audit outcome.
**Primary runner:**
[`scripts/diagonal_lattice_scoping_enumerator.py`](../scripts/diagonal_lattice_scoping_enumerator.py)
**Cached log:**
[`logs/runner-cache/diagonal_lattice_scoping_enumerator.txt`](../logs/runner-cache/diagonal_lattice_scoping_enumerator.txt)

## 0. Purpose and what this note is not

This note opens a scoped thought experiment: *what changes if the lattice
adjacency primitive is enlarged from cubic nearest-neighbor (NN) to
"NN + face-diagonal + body-diagonal", with diagonal links allowed to carry
their own qubit-link connections?*

It is a **surface definition only**. Concretely:

- It does **not** edit [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
  or any other parent note.
- It does **not** assert a derived theorem, a closure, or a status.
- It does **not** import any external comparator or new physics framing beyond
  the three explicitly named commitment levels (L1/L2/L3) below, which are the
  user-authorized framing for this exploration.
- It fixes vocabulary and enumeration so the downstream phase notes
  (L1 negative, L2 dimension audit, gate tests, synthesis) have one precise
  reference for "which diagonals, named how".

## 1. The current cubic-NN adjacency (precise statement)

The Lattice axiom states (verbatim):

> The site set is `Z^3` with standard translation action and nearest-neighbor
> cubic adjacency. Finite-range locality means finite support or finite
> graph-distance range with respect to this lattice when a local expression is
> specified.

So the baseline adjacency relation is

```text
x ~ y   iff   x - y in { ±e_1, ±e_2, ±e_3 }              (cubic NN, ⟨100⟩)
```

with `e_i` the standard basis of `Z^3`. The coordination number is `6`; the
displacement set is the 6-vector `⟨100⟩` family. This adjacency is part of the
axiom: it is the reference for "finite-range locality". Enlarging it is an
axiom-content question, not a free relabeling (see §5).

## 2. Three commitment levels

The thought experiment is graded by how much new structure a diagonal link is
allowed to carry.

- **L1 (free, derived).** A diagonal link is a **Wilson-line composite** of NN
  connections along a chosen NN path. It carries no independent degree of
  freedom: its holonomy is the ordered product of NN link variables along the
  path. The existing framework Wilson-loop machinery already contains this
  implicitly. **Governance cost: none.** (Tested in the L1 negative note.)

- **L2 (convention/primitive extension).** Each diagonal link carries its
  **own independent** qubit-link `u(2)` connection (cf.
  [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)).
  The adjacency primitive grows from cubic NN to cubic + diagonal, and the
  diagonal connection variables are new dynamical data not fixed by the NN
  variables. **Governance cost: primitive/axiom-level** (see §5). (Tested in
  the L2 dimension audit.)

- **L3 (genuine new physics).** Distance-weighted, site-dependent connections
  in which the connection between far sites depends on intervening sites' qubit
  content; the connection class becomes non-local but causality-respecting
  (Lieb-Robinson-compatible). **Governance cost: import requiring explicit user
  approval.** The L3 *framing* is user-authorized for this exploration only;
  adopting it into the framework would require a separate import petition.
  (Tested as speculative territory in the r=1/2 gate note.)

## 3. Enumeration of diagonals

Two distinct objects must not be conflated.

### 3a. Per-unit-cube segments (8 vertices `{0,1}^3`, `C(8,2)=28` pairs)

Graded by Hamming distance `h` (= squared Euclidean length on `{0,1}^3`):

| class | `h` | Euclid. length | count | O_h-orbit? |
|---|---|---|---|---|
| cube edge (NN)   | 1 | `1`   | **12** | one orbit, stab order 4 |
| face-diagonal    | 2 | `√2`  | **12** | one orbit, stab order 4 |
| body-diagonal    | 3 | `√3`  | **4**  | one orbit, stab order 12 |

`12 + 12 + 4 = 28 = C(8,2)`. The **12 face-diagonals** are the two diagonals
of each of the 6 cube faces; the **4 body-diagonals** join antipodal vertices
through the cube center. Orbit-stabilizer: `|O_h| = 48`, and
`12·4 = 12·4 = 4·12 = 48`.

Explicit face-diagonals (named by endpoints, `xyz` bit strings):

```text
z=0 face: 000-110, 100-010      z=1 face: 001-111, 101-011
y=0 face: 000-101, 100-001      y=1 face: 010-111, 110-011
x=0 face: 000-011, 010-001      x=1 face: 100-111, 110-101
```

Explicit body-diagonals:

```text
000-111, 100-011, 010-101, 001-110
```

### 3b. Per-site displacement families (Moore neighborhood of one site)

The directed displacement vectors to the 26 sites of the surrounding `3×3×3`
shell partition into three cubic-symmetry (`O_h`) orbits:

| family | representatives | count | coordination after adding |
|---|---|---|---|
| `⟨100⟩` (NN)            | `(±1,0,0)` & perms | **6**  | 6 (baseline) |
| `⟨110⟩` (face-diagonal) | `(±1,±1,0)` & perms | **12** | 6+12 = 18 |
| `⟨111⟩` (body-diagonal) | `(±1,±1,±1)`        | **8**  | 18+8 = 26 (full Moore) |

`6 + 12 + 8 = 26`. Note the body-diagonal count differs between the two
readings (**4** undirected cube body-diagonals vs **8** directed `⟨111⟩`
displacements) because each cube has 4 body-diagonals but a central site sees 8
corner-directions. The enumerator runner verifies both counts and their
`O_h`-orbit/stabilizer arithmetic.

## 4. Cross-reference to the three open gates

The thought experiment is motivated by three high-leverage open gates. Each
later phase note tests one against the diagonal extension; this note only
records the targets.

- **GATE-COLOR** — where does `SU(3)` come from? It is dimension-obstructed on
  a single qubit fiber (`dim end_R(C^2)=4 < 8 = dim su(3)`), per
  [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md).
  *Tested under L2.*

- **GATE-CHIRALITY** — the `C_3`-orbit-splitting chiral grading
  `Γ_χ = (2/3)J − I` on the hw=1 generation `R^3` factor. A retained bounded
  identity says it cannot be built from `C_3`-equivariant comm/anticomm on the
  generation factor:
  [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md).
  The hw=1 triplet is the BZ-corner orbit of
  [`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md).
  *Tested under L2/L3.*

- **GATE-R-HALF** — the charged-lepton Brannen-circulant modulus
  `r = |b|^2/a^2 = 1/2`, currently admitted as the Tier-A input `AC_φλ`:
  [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md),
  with the circulant form `Y_e = A_e + B_e C` of
  [`CHARGED_LEPTON_TWO_HIGGS_CANONICAL_REDUCTION_NOTE.md`](CHARGED_LEPTON_TWO_HIGGS_CANONICAL_REDUCTION_NOTE.md).
  *Tested under L3 (weighted paths).*

## 5. Governance placement (no decision made here)

Per [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md):
axioms and approved primitives are tracked in
`docs/audit/data/axiom_premise_nodes.json` and may not be added or amended
"without explicit owner approval", recorded in the policy and registry before
chain-satisfying downstream claims.

- **L1** changes nothing — diagonals are derived composites; no governance step.
- **L2** posits *new independent connection degrees of freedom* on diagonal
  links. The graph-relabeling part is quasi-isometric to NN (a face-diagonal is
  2 NN steps, so finite-range locality is unchanged), which is convention-like
  and could in principle follow the radian-style adoption precedent
  ([`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md`](RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md):
  `meta` source-note + paired-runner + cached-log + audit-lane review). **But**
  the independent-connection *content* adds dynamical data not derivable from
  the three axioms, which is a primitive-level addition requiring owner
  approval. This note does **not** request that approval; it only records that
  the question lives at the primitive level.
- **L3** is a new connection class = an import, requiring explicit user
  authorization beyond this exploration.

The point of the later phase notes is to determine **whether any gate actually
closes** under L2/L3, i.e. whether the governance cost would buy anything,
before any adoption is contemplated.

## 6. Explicit disclaimers

- **This note does not change axioms.** The Lattice axiom remains cubic NN.
- **This note proposes a thought-experiment surface, not a derived theorem.**
  No closure, no status, no promotion is asserted.
- Status is owned by the independent audit lane.

## 7. Runner certificate

[`scripts/diagonal_lattice_scoping_enumerator.py`](../scripts/diagonal_lattice_scoping_enumerator.py)
exhibits the enumeration explicitly and verifies:

1. `{0,1}^3` has 8 vertices and `C(8,2)=28` undirected pairs;
2. the Hamming-distance grading gives counts `(12, 12, 4)` for
   `(edge, face-diagonal, body-diagonal)` summing to 28;
3. the per-site Moore displacement families have sizes `(6, 12, 8)` summing
   to 26, with coordination numbers `6 → 18 → 26`;
4. each family is a single `O_h` orbit with the stated stabilizer order
   (orbit-stabilizer product `= 48`);
5. the explicit face-diagonal and body-diagonal endpoint lists are correct and
   disjoint;
6. the hw=1 generation triplet `{100, 010, 001}` is pairwise face-diagonal
   (Hamming distance 2) and forms one `S_3`/`C_3` orbit — the bridge used by
   the chirality-gate note;
7. the source note keeps "no axiom change" / "thought-experiment surface"
   firewalls in scope.

Run:

```text
python3 scripts/diagonal_lattice_scoping_enumerator.py
```

Expected:

```text
SUMMARY: PASS=30 FAIL=0
```
