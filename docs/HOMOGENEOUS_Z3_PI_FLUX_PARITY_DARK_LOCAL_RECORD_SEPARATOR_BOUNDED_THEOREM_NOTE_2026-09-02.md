# Homogeneous Z3 pi-flux parity-dark local-Record separator

## Status and result

**Date:** 2026-09-02
**Claim type:** bounded theorem
**Surface status:** conditional support
**Audit-status authority:** independent audit only
**TOE accounting:** zero obligation retirement and zero TOE-percentage movement

**Current correction (2026-09-07):** the fixed-generator operator theorem and
its supplied protocol retain their stated scope. The checklist leaves
physical wall implications unresolved. Historical grades and process
directions have no current authority; see the
[correction record](../.claude/science/review-fixes/local-gibbs-z3-record-20260907/CORRECTION.md).
This source correction assigns no audit grade.

For the standard static, simultaneous, unit-hopping staggered signed adjacency
on infinite `Z^3`, the real-time propagator has an exact support selection
rule: from any source, it can reach only sites whose coordinate-parity vector
differs in zero or one positions. Every displacement with two or three odd
coordinates is dark for every real time. In particular, the body-diagonal
target `(1,1,1)` is never reached.

The uniform signed adjacency does reach that same local target. At the common
cadence `t=1/2`, its target occupation probability is `J_1(1)^6`, with the
strict exact bound

```text
(7/16)^6 < J_1(1)^6 < (1/2)^6,
```

while the staggered probability is zero. A target outcome is therefore an
exclusive, one-sided support witness for the uniform branch with every
exterior lattice bond active; finite-cube boundary isolation is unnecessary.
Unlike Block 46, the complement outcome is shared, so perfect single-shot
discrimination does not survive.

This is a homogeneity trade, not an unqualified protocol strengthening, and it
does not select either action. The action, unitary evolution, law-side
preparation, Born evaluation, cadence, identification of the PVM alternatives
with the Admissibility possibility partition, operational Record instrument,
site/probability/rate allocation, and physical permanence mechanism are still
supplied or open. The Record axiom owns that Records form and are permanent;
this block does not construct the production or persistence dynamics. The
physical matter-functional clause `I-4` and the distinct Record-process bridge
remain open.

**Primary runner:**
[`scripts/homogeneous_z3_pi_flux_parity_dark_local_record_separator_2026_09_02.py`](../scripts/homogeneous_z3_pi_flux_parity_dark_local_record_separator_2026_09_02.py)

**Foundation and provenance:** [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[Block 46](STRICT_FREE_STAR_GIBBS_CUBE_RECORD_FLUX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md),
[uniform-walk kernel](../archive/notes/docs/ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
[staggered-kernel component](STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md),
[`I-4` decomposition](GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md),
and [Record-operation normal form](RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md).
The component science sources were top-level/effective `unaudited` in the
pinned `origin/main@2cea9a5` tree; links and blobs establish
dependency/provenance, not grade.

## 1. Supplied objects and physical typing

On `ell^2(Z^3)`, let

```text
T_j |x> = |x+e_j>,      D_j = T_j + T_j^-1,
P_j |x> = (-1)^x_j |x>.
```

Define

```text
H0 = D_1 + D_2 + D_3,
A_1 = D_1,
A_2 = P_1 D_2,
A_3 = P_1 P_2 D_3,
H1 = A_1 + A_2 + A_3.                                  (1)
```

Equivalently, the positive-direction link signs are

```text
eta_1(x)=1,
eta_2(x)=(-1)^x_1,
eta_3(x)=(-1)^(x_1+x_2).                               (2)
```

They are unchanged along their own link direction, so (1) is self-adjoint.
The product around each elementary face is `+1` for `H0` and `-1` for `H1`.
The latter is a uniform pi-flux field in a period-two gauge.

These are one-particle coordinate operators, not three onsite qubits. The
strict-free many-body lift is `dGamma(Hj)` on one CAR mode per physical lattice
site. On its one-particle sector, local occupation at site `y` restricts to
`|y><y|`. The graded composition and this action are supplied; the current
four axioms do not choose either one.

“Strict-free” alone is not a sufficient hypothesis for the darkness theorem:
a quadratic onsite background or longer-range hopping can break it. The
load-bearing surface is the explicit static nearest-neighbor generator (1),
with the limited coefficient/scalar robustness stated after (7).

This is also not a new staggered operator. If
`U|x>=i^(x_1+x_2+x_3)|x>`, direct link-by-link conjugation gives

```text
U [-i sum_j eta_j(x)(T_j-T_j^-1)] U* = H1.              (3)
```

Thus `H1` is the conventional self-adjoint staggered derivative in a diagonal
phase convention. Earlier repository work already owns its folded-cell
Clifford square and dispersion. The new claim below is the real-space
all-time support corollary and its local-Record use.

## 2. Exact square and parity support

`P_j` anticommutes with `D_j` and commutes with `D_k` for `k != j`. It follows
directly from the strings in (1) that

```text
A_i A_j + A_j A_i = 0             (i != j),
A_j^2 = D_j^2.
```

Therefore every mixed two-direction path cancels and

```text
H1^2 = Q := D_1^2+D_2^2+D_3^2
     = 6I + sum_j (T_j^2+T_j^-2).                       (4)
```

`Q` preserves all three coordinate parities. Meanwhile each `A_j` flips the
parity of coordinate `j` and no other coordinate. Hence even powers preserve
all three coordinate parities and odd powers flip exactly one coordinate
parity:

```text
H1^(2n)   = Q^n,
H1^(2n+1) = H1 Q^n.                                     (5)
```

Each `T_j` is unitary and `||H1|| <= 6`, so the exponential power series is
norm-convergent. Equations (4)-(5) can therefore be separated into its even
and odd parts without a formal-series assumption. For every real `t`,

```text
exp(-itH1)
 = sum_n (-1)^n t^(2n) Q^n/(2n)!
   - i H1 sum_n (-1)^n t^(2n+1) Q^n/(2n+1)!.            (6)
```

The first line of (6) connects parity distance zero; the second connects
parity distance one. Thus, for every `x,r in Z^3`,

```text
<x+r|exp(-itH1)|x> = 0                                 (7)
```

whenever the Hamming weight of `r mod 2` is two or three. This includes every
all-odd displacement and, in particular, `r=(1,1,1)`. It is an all-time
operator theorem. The runner's exact integer checks through nine powers are a
sanity check; the load-bearing step is (4)-(6), not a finite truncation.

The same proof survives arbitrary real directional coefficients
`H1(kappa)=sum_j kappa_j A_j`, because its square is
`sum_j kappa_j^2 D_j^2`. Adding a scalar onsite term `mu I` only multiplies
the propagator by a global phase. These are genuine robustness corollaries;
arbitrary non-scalar onsite backgrounds are not included.

## 3. Uniform comparator and an exact fixed-time bound

The three terms of `H0` commute, so its evolution factorizes. The standard
one-dimensional generating function gives, for integer displacement `r`,

```text
<x+r|exp(-itH0)|x>
 = product_j [(-i)^r_j J_(r_j)(2t)].                    (8)
```

This formula is already owned by the repository's uniform cubic-walk result;
it is consumed here, not promoted as new. At the body diagonal,

```text
<x+(1,1,1)|exp(-itH0)|x> = i J_1(2t)^3.                 (9)
```

An independent path count checks the first two nonzero coefficients:

```text
<111|H0^3|000> = 6,       <111|H0^5|000> = 180,

<111|exp(-itH0)|000> = i t^3 - (3i/2)t^5 + O(t^7),      (10)
```

matching the cube of `J_1(2t)=t-t^3/2+t^5/12-...`.

At the preregistered common cadence `t=1/2`,

```text
J_1(1) = 1/2 - 1/16 + 1/384 - ... .                    (11)
```

Successive absolute terms have ratio
`1/[4(m+1)(m+2)]<1`, so the alternating-series theorem gives

```text
7/16 < J_1(1) < 169/384 < 1/2.                          (12)
```

Consequently the same target effect has

```text
p0 = J_1(1)^6 in ((7/16)^6,(1/2)^6),    p1=0.           (13)
```

Unlike the isolated cube, the uniform branch is not perfect transfer. The
strict positivity, not probability one, is the relevant separator.

## 4. Common local-Record protocol with no cut boundary

Use the same supplied unrecorded localized source `|x>`, the same cadence
`t=1/2`, the same local target/complement occupation PVM at
`y=x+(1,1,1)`, the same two-outcome writer, and the same branch-blind
formation-triggered gate (or separately licensed pointer) in both candidates.
Only the final Records are readable. The pre-Record wave function is law-side
predictive machinery, not a framework state silently replacing the axiom's
Record-configuration definition.

Every nearest-neighbor link of infinite `Z^3` remains active during the
evolution. In particular, from a source at a nominal cube corner the links to
`(-1,0,0)`, `(0,-1,0)`, and `(0,0,-1)` are present, as are the links leaving
the opposite corner. The only decoupling occurs after formation, identically
in the two branches, because bare hopping does not commute with target
occupation and so cannot itself implement Record permanence.

Repeated final Records could estimate (13) under supplied stationarity,
reset, and calibration assumptions. No unrecorded alternative is claimed to
be directly observed, and no finite sample proves an exact probability.
A target-occupation Record rules out `H1` under the protocol, but a
complement/no-target outcome is shared by both candidates because `p0<1`.
This is one-sided support separation, not disjoint deterministic transcripts.

Calling the final target/complement outcome a framework Record additionally
requires that this PVM be the relevant partition of the local Qubit
possibility domain and that its Born weights be the Admissibility distribution
for the same neighboring condition. Those identifications are supplied here;
neither `I-4` by itself nor the operator theorem establishes them.

## 5. Gauge-covariant homogeneity and cubic family

The displayed staggered gauge is not invariant under every bare one-site
translation. Directly,

```text
T_1 H1 T_1* = (P_2 P_3) H1 (P_2 P_3),
T_2 H1 T_2* = P_3 H1 P_3,
T_3 H1 T_3* = H1.                                      (14)
```

Thus `T_1` and `T_2` do not commute with `H1`; the magnetic translations
`M_1=(P_2P_3)T_1`, `M_2=P_3T_2`, and `M_3=T_3` do. Calling the displayed
matrix ordinarily translation invariant would be false. Its physical link
field is homogeneous only in the gauge-covariant sense.

Every proper cubic rotation preserves the constant face-flux assignment.
The ratio of a rotated `H1` link field to (2) has trivial plaquette product;
on the simply connected cubical complex of `Z^3`, path products then construct
a diagonal `Z_2` site gauge relating them. The runner enumerates all 24 proper
signed-permutation rotations and independently constructs that gauge on a
finite simply connected witness box. Rotations send `(1,1,1)` to a vector
with three odd coordinates, so (7) and (13) transform as a protocol family.
A single localized source-target instance is not called invariant.

## 6. Sharpness: simultaneous action, not arbitrary controls

The cancellation is specific to static simultaneous evolution under the sum
`H1=A_1+A_2+A_3`. Consider instead the ordered pulse

```text
exp(-itA_3) exp(-itA_2) exp(-itA_1).
```

Its body-diagonal amplitude has leading term

```text
(-it)^3 <111|A_3 A_2 A_1|000> = -i t^3,
```

because the exact path coefficient is `-1`. It is therefore generically
nonzero. The theorem does not say that all `K1`-based controls or
time-dependent dynamics are parity-dark.

A non-scalar onsite field can also escape without changing the hopping links.
For `V=P_1+2P_2`, exact infinite-lattice path algebra gives

```text
<111|(H1+V)^n|000> = 0  for n=1,...,5,
<111|(H1+V)^6|000> = -32.                               (15)
```

Thus neither arbitrary onsite backgrounds nor arbitrary controls are covered.
The runner retains (15) as a hostile sharpness witness.

## 7. Negative-claim discipline

The full committed
[N1-N8 checklist](HOMOGENEOUS_Z3_PI_FLUX_PARITY_DARK_LOCAL_RECORD_SEPARATOR_NO_GO_DISCIPLINE_CHECKLIST_2026-09-02.md)
limits the negative conclusion to the static-`H1` all-time parity-support
boundary. It does not establish independence of the physical obligations in
N2 or a complete wall count. It identifies live positive action-to-functional-
to-Record routes and assigns `partial-narrowing` to broader negative
inferences; an overall N1-N8 pass or broader no-go is not claimed. The new
joined increment is only the position-space all-time parity-support theorem
and its one-sided homogeneous local-Record
application. It is not advertised as a new staggered operator, dispersion,
Bessel identity, action selector, or proof that the missing bridges cannot be
derived.

## 8. Consequence for the TOE program

Block 46's strongest artificial protocol import—finite-cube boundary
isolation—is removed, at the explicit cost of losing its deterministic `1/0`
transcript. Exact `pi/2` perfect-transfer tuning is replaced by a
strict-positive interval certificate at `t=1/2`: the target outcome remains
exclusive to `H0`, but the complement is shared. This is a useful homogeneity
trade and a one-sided conditional experiment, not an unqualified protocol
strengthening. Empirical use additionally supplies reset, stationarity, and
calibration.

They are not TOE closure. Current authority still does not identify `H0` or
`H1` as the physical action, map an action to the physical predictive
functional and event probabilities, select the clock or preparation, allocate
the Record outcome/site/probability/rate, or construct the Record-production
and physical-persistence dynamics. Accordingly this block carries zero obligation retirement, zero
TOE-percentage movement. The original no-standalone-PR recommendation is
historical planning, not a restriction on current source review. Its value is
as a Block 46 strengthening and as a conditional experiment consumed by a future
`I-4`/Record-process bridge.

## Reproduction

```bash
python3 scripts/homogeneous_z3_pi_flux_parity_dark_local_record_separator_2026_09_02.py
```

Finite runner checks use exact integer/Fraction arithmetic. Equations (4)-(6)
are the load-bearing analytic all-time proof; source/protocol custody and the
finite rotation box are explicitly labeled as checks rather than derivations.
The runner terminates with a `TOTAL` line.
