# KCPT L=4 full-center unlock and dimension-76 Wedderburn classification

**Type:** bounded_theorem

**Date:** 2026-09-03

**Surface:** periodic `L=4`, `N=64` staggered lattice on the `4^3` torus

**Runner:**
[`scripts/kcpt_l4_full_center_unlock_dim76_wedderburn_2026_09_03.py`](../scripts/kcpt_l4_full_center_unlock_dim76_wedderburn_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/kcpt_l4_full_center_unlock_dim76_wedderburn_2026_09_03.txt`](../logs/runner-cache/kcpt_l4_full_center_unlock_dim76_wedderburn_2026_09_03.txt)

## Claim scope

On the fixed finite KCPT surface inherited from the dependencies, let

```text
A     = Alg_C(D2, J_full, rho(H)),
A_nat = Alg_C(D2, J_full, S_eps),
C_g   = Alg_C(D2, J_full, S_eps, g),  g in G_amb,
```

and let `sep=P_a-P_b` be the difference of the two rank-12 constituent
projectors on the `m=2` shell.  The 768 elements of `G_amb` form 36
`H`-conjugacy classes for this census.

The dependency chain supplies

```text
Z(A)     = C[M] direct-sum span{sep},  dim Z(A)=5,
Z(A_nat) = C[M],                       dim Z(A_nat)=4.
```

Fresh execution of the finite construction gives:

1. `dim(C_g intersection Z(A))` is 4 on 33 classes and 5 on three
   classes.  The three full-center classes are exactly the classes with
   separator reach `omega(g)=1`.
2. One representative suffices in each of those three classes.  Their
   `(class size, dim C_g, order(g))` data are
   `(4,28,4)`, `(64,76,12)`, and `(64,76,12)`.
3. Each of the two 76-dimensional extension algebras has center dimension
   19 and numerically resolves as

   ```text
   C_g isomorphic to M_2(C) direct-sum ... direct-sum M_2(C)
                       (19 summands).
   ```

4. The two non-`H`-conjugate dimension-76 classes have the same abstract
   algebra and representation profile.  Their six rank-4 minimal central
   idempotents on shell `m=2` divide three inside `P_a` and three inside
   `P_b`, so

   ```text
   sep = (e_a1 + e_a2 + e_a3) - (e_b1 + e_b2 + e_b3).
   ```

These are numerical finite-matrix statements at the stated tolerances.  They
do not identify any center element as a physical charge, observable, Record,
or superselection sector.

## 1. Why the center intersection reduces to one question

The four shell projectors `P_0,...,P_3` span `C[M]` and already belong to
every `C_g` because `A_nat` is contained in every extension.  The companion
runner rebuilds

```text
span(P_0,P_1,P_2,P_3,sep)
```

at dimension five and checks that all five directions commute with the
generators of `A`.  The earlier bicommutant theorem supplies the independent
upper bound `dim Z(A)=5`, so those five directions exhaust the full center.

It follows that an intersection can have only two dimensions here:

```text
dim(C_g intersection Z(A)) = 4 + indicator[sep belongs to C_g].
```

The parent census computes the normalized Frobenius projection

```text
omega(g) = ||Pi_Cg(sep)||_F^2 / ||sep||_F^2.
```

Thus `omega=1` is precisely the fifth-center-direction membership test.  The
fresh run separates the three member classes from the other 33 classes by a
wide residual margin: the largest member residual is below `1e-8`, while the
smallest nonmember residual is greater than `0.5`.

The runner's deterministic zero-based enumeration labels the three classes
`14`, `25`, and `27`.  These integers are reproducibility labels, not
class-invariant names.  The invariant metadata are:

| zero-based runner id | class size | `dim C_g` | representative order |
|---:|---:|---:|---:|
| 14 | 4 | 28 | 4 |
| 25 | 64 | 76 | 12 |
| 27 | 64 | 76 | 12 |

Because `A_nat` itself has only the four-dimensional center and one supplied
representative already reaches all five directions, the minimal number of
added elements within each successful class is one.  This is a word-algebra
statement; it does not select one class physically.

## 2. The two larger unlock algebras

The earlier census already measured the two order-12, size-64 routes at
algebra dimension 76 and full separator reach.  Their internal algebra types
were not classified there.  For each class, the new runner:

1. true-closes `C_g` at complex dimension 76;
2. solves the commutant equations inside the closed algebra and finds a
   19-dimensional center;
3. diagonalizes two independently seeded Hermitian center samples;
4. obtains 19 separated minimal central spectral projectors on both seeds;
5. compresses the full algebra into each projector and obtains corner
   dimension four every time; and
6. checks completeness, idempotency, Hermiticity, and centrality directly.

For a finite-dimensional complex `*`-algebra, a minimal central corner of
dimension four is `M_2(C)`.  Nineteen such corners account for the full
dimension `19*4=76`, resolving

```text
C_g isomorphic to M_2(C)^19
```

for both classes at the numerical thresholds.  The largest numerical-null
center singular value is below `4.7e-14`, the smallest kept value is within
roundoff of `2`, and the smallest between-cluster gap across both classes and
both seeds exceeds `1.3e-3`.

## 3. Representation and shell profile

The central-idempotent ranks are

```text
six rank-2 blocks and thirteen rank-4 blocks.
```

Since each algebra block is `M_2(C)`, rank two means representation
multiplicity one and rank four means multiplicity two.  Both dimension-76
classes give the same detailed profile:

| `M` shell | corner dimension | central-idempotent rank | number of blocks |
|---:|---:|---:|---:|
| 0 | 4 | 2 | 2 |
| 0 | 4 | 4 | 1 |
| 1 | 4 | 4 | 6 |
| 2 | 4 | 4 | 6 |
| 3 | 4 | 2 | 4 |

The rank totals are `8,24,24,8` on shells `0,1,2,3`, reproducing the full
64-dimensional carrier.  The profile equality proves abstract isomorphism
and the same represented multiplicities.  It does **not** prove that the two
extensions are conjugate by a transformation outside `H`; they are distinct
`H`-classes by construction.

The six shell-2 atoms are especially informative.  Direct multiplication by
`P_a` and `P_b` assigns all six without remainder: three lie wholly in
`P_a`, three wholly in `P_b`.  Their signed sum reconstructs `sep` with
Frobenius residual below `8e-13` in both classes and both center samples.

This distinguishes the larger routes from the 28-dimensional route:

```text
A_28  isomorphic to M_2(C)^7,
A_76 isomorphic to M_2(C)^19.
```

In `A_28`, `P_a` and `P_b` are themselves minimal central idempotents.  In
either `A_76`, each is refined into three minimal central idempotents.  All
three routes contain the same five-dimensional center of the full algebra
`A`, but their own centers and internal resolutions differ.  In particular,
the extra 14 center directions of `A_76` are central only in that subalgebra;
they are not additional directions in `Z(A)`.

## 4. Executable evidence and controls

The companion runner re-executes the landed 49-gate parent construction in
process, captures its stdout, and refuses to proceed green unless the parent
returns `PASS=49 FAIL=0` and exit code zero.  It then reports
`TOTAL: PASS=23 FAIL=0` for the recovery delta.

The new gates cover:

- the five independent commuting center directions;
- the `{4:33,5:3}` intersection histogram and its residual margin;
- the three full-center class metadata rows and equality with the `omega=1`
  stratum;
- true closure and center dimension 19 for both dimension-76 classes;
- two-seed central clustering, corner dimensions, ranks, and shell profiles;
- the three-plus/three-minus minimal-idempotent decomposition of `sep`; and
- two live controls: deleting `sep` collapses the proposed center basis from
  dimension five to four, while the same block machinery resolves `A_28` as
  seven rather than 19 `M_2(C)` summands.

No cached PASS line is used as evidence.  The original unlanded scratch probe
is unavailable; every number in this note was recomputed from the landed
finite construction on 2026-09-03.

## 5. Boundary and scientific reading

This result is positive structural science on one finite supplied model.  It
shows that full-center word realization is not unique: one short route reaches
the center with a 28-dimensional algebra, while two other one-element routes
reach the same full center and simultaneously resolve a much finer
19-component subalgebra structure.  Center reach alone therefore does not fix
the architecture of the realizing algebra.

The result remains limited to the periodic `L=4`, `N=64` carrier, the stated
KCPT operators, single ambient-element extensions, and numerical rank
thresholds.  It derives no continuum or thermodynamic limit, dynamics,
coupling, Standard-Model generation assignment, measurement rule, or Record
readout.  It adds no axiom and by itself retires no TOE obligation.  Audit
status and retained classification belong exclusively to the independent
audit lane; this source note sets neither.

## Dependencies

- [KCPT Dirac-symmetry algebra bicommutant dimension 992](KCPT_DIRAC_SYMMETRY_ALGEBRA_BICOMMUTANT_DIMENSION_992_BOUNDED_THEOREM_NOTE_2026-07-24.md)
  supplies the full algebra `A`, `dim Z(A)=5`, and its five-block center.
- [KCPT ind12 separator reach census and minimal unlock](KCPT_IND12_SEPARATOR_REACH_QUANTIZED_CENSUS_MINIMAL_UNLOCK_BOUNDED_THEOREM_NOTE_2026-07-25.md)
  supplies the fixed construction, `A_nat`, `sep`, the 36-class census, and
  the 28-dimensional comparison route that the companion runner re-executes.
