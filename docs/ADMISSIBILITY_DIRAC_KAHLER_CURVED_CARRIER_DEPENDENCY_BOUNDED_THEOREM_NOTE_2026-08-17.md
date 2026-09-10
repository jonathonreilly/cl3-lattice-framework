---
claim_id: admissibility_dirac_kahler_curved_carrier_dependency_bounded_theorem_note_2026-08-17
claim_type: bounded_theorem
claim_scope: "On one exact finite Block 105 fixture (time-8 cover, space 4, time-4 antiperiodic quotient, chart origins (1,0) and (1,1), mass 2/7, differential weights 3/5 and 4/5), the two displayed 16x16 chartwise action matrices are unequal with entry difference -89/140 and both have five time bands; their 32x32 alternating forms have spatial-shift commutator rank 32. Eight framed raw distance-two 4x4 action blocks have rank 3 and coordinate kernel e2. These blocks are not Schur complements. Sixteen complete adjacent 8x8 grouped maps have ranks 3 or 4, while the embedded e2 witness fails in six cases, including the exact residual (0,0,0,0,9/80,0,0,0). These finite facts do not establish transition inequivalence, absence of a global action, a unique-evolution no-go, or a universal dependency-order theorem. Common descent, a true elimination, descriptor or enlarged-state evolution, direct-Gram OS, other groupings and other curved fixtures remain open."
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py
---

# Curved-Carrier Finite Matrix Boundary

**Date:** 2026-08-17; corrected 2026-09-10

**Campaign block:** 128

**Type:** `bounded_theorem`

**Audit authority:** none. Formal audit remains deferred.

**Constitutional effect:** none. No action, axiom, premise, or primitive is
adopted.

**TOE accounting:** zero obligation retirement. No TOE percentage moves.
The retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py`](../scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py)

The original PR6844 bodies remain recoverable under
[`released6844-recovery-20260910`](../.claude/science/physics-loops/released6844-recovery-20260910/).
They are historical evidence, not live claim text.

## 1. Result

The question is small: what do two displayed chartwise completions of the
reviewed Block 105 overlap Hodge actually show?

They show four useful finite facts and one failed extrapolation.

1. The two displayed physical action matrices are unequal. At entry
   \((10,11)\),

   \[
   Q_{(1,1)}[10,11]-Q_{(1,0)}[10,11]
   =-\frac{89}{140}.                                      \tag{1}
   \]

   Both cover matrices have time bands
   \((-2,-1,0,1,2)\).

2. If \(A_a\) is the 32-dimensional alternating form built from the
   displayed physical matrix and \(S_x\oplus S_x\) is the doubled spatial
   shift, then

   \[
   \operatorname{rank}[A_a,S_x\oplus S_x]=32              \tag{2}
   \]

   for both displayed origins.

3. Eight framed raw distance-two \(4\times4\) action blocks have rank three.
   In the declared directional slice frame their nullspace is

   \[
   \ker B_{a,\epsilon,j}
   =\operatorname{span}\{e_2\},\qquad
   e_2=(0,1,0,0)^{\mathsf T}.                             \tag{3}
   \]

4. Sixteen complete adjacent \(8\times8\) grouped maps are singular. Twelve
   have rank four and four have rank three. The coordinate witness in
   (3) does not survive all groupings. For origin \((1,0)\), direction
   \(+2\), step \(1\), and the alternative grouping starting at \(1\),

   \[
   G\binom{e_2}{0}
   = (0,0,0,0,9/80,0,0,0)^{\mathsf T}\ne0.               \tag{4}
   \]

The old note called the blocks in (3) “Schur forward coefficients” and
treated their kernel as a regrouping-invariant evolution obstruction. The
runner had only selected a raw cover-action block
\(Q[j,j+\epsilon]\). It had not eliminated any variables, and its grouped
predicate merely found that same subblock inside two larger maps.
Equation (4) is a direct counterexample to the claimed fixed-kernel
regrouping theorem.

The corrected result stops at (1)--(4). It does not establish that the two
matrices are inequivalent under a transition law, that a global action
does not exist, that all forward formulations fail, or that one
construction must precede every curved-OS step.

## 2. Exact displayed domain

The finite domain is part of the theorem:

| object | displayed value |
|---|---|
| cover | time extent \(8\), spatial extent \(4\) |
| quotient | physical time extent \(4\), antiperiodic fold |
| chart origins | \((1,0)\), \((1,1)\) |
| local differential | \(i((3/5)E_x+(4/5)E_t)\) |
| mass | \(2/7\) |
| raw block directions | \(+2\), \(-2\) |
| displayed steps | \(1\), \(3\) |
| full groupings | starts \(j-1\) and \(j\) |
| Block 105 input | reviewed overlap field and overlap Hodge |

The directional slice frame depends on the time coordinate and direction.
It was chosen so that each raw block in (3) has coordinate witness \(e_2\).
The witness is therefore a framed coordinate statement. It is not an
unframed invariant carrier direction.

The doubled alternating form contains one complex Grassmann mode and its
conjugate variable. The second block is not a second physical site mode.

## 3. Inputs and premise boundary

The only imported repository module is the current filesystem copy of the
corrected
[Block 105 runner](../scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py).
The Block 128 runner uses its `EX`, `ET`, `LENGTH`,
`overlap_field`, `shear_hodge`, and `translation_matrix`
definitions and the globals those functions call. These function bodies
are unchanged from the reviewed PR6379 fixture.

The current
[Block 105 note](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
supplies a conditional finite Hodge construction. It leaves the common
nilpotent patch/frame differential or connection residual open. This note
does not turn that open construction into a premise.

[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) and the
[primitive registry](audit/data/axiom_premise_nodes.json) supply no
transition law, curved action, Schur elimination, descriptor evolution,
or reflection-positivity bridge for this fixture.

The exact current citations and hashes are recorded in
[`CITATION_SCOPE.json`](../.claude/science/physics-loops/released6844-recovery-20260910/CITATION_SCOPE.json).
The original citation manifest is archived byte-exactly. It is not copied
onto the live tree; the coordinator owns final manifest regeneration.

Block 127 is not imported and none of its mathematical functions is
evaluated. Its old handoff explains why this calculation was attempted.
The exact dated excerpt and original blob are kept in
[`BLOCK127_ROADMAP_CONTEXT.json`](../.claude/science/physics-loops/released6844-recovery-20260910/BLOCK127_ROADMAP_CONTEXT.json).
That file is roadmap history, not live Block 127 theorem authority.

## 4. Unequal matrices are not an equivalence test

Equation (1) compares two raw matrices in two chosen chart constructions.
It proves inequality in those coordinates. It does not define a transition
map between the charts, test conjugacy, or test descent from a common
operator.

Both displayed matrices are already finite action matrices. The missing
object is a justified chart-independent or transition-compatible action.
This packet establishes no common action, but it also establishes no
global-action no-go.

The five time bands are a support statement. Pentadiagonality neither
identifies coefficients between charts nor supplies a transition law.

## 5. What the commutator establishes

For a unitary shift, its eigenspaces are invariant under an operator
exactly when that operator commutes with the shift. Equation (2) therefore
shows that the eigenspace decomposition of this particular spatial shift
does not reduce either displayed alternating matrix.

This is a precise failure of the spatial-momentum reduction used in the
historical flat program. It is not an absence theorem for all spectral
descriptions, position-space formulations, generalized eigenvalue
problems, or other translations.

## 6. Raw distance-two blocks are not Schur complements

Let

\[
C_a=mH+i(Hd_a+d_a^\dagger H),
\qquad
Q_a=\operatorname{Sel}\,C_a\,\operatorname{Inj},
\]

where \(H\) is the lifted Block 105 Hodge, \(d_a\) is the displayed
chartwise differential, \(m=2/7\), and \(C_a\) is the \(32\times32\)
cover action. The map \(\operatorname{Inj}\) implements the time-four
antiperiodic fold, and \(\operatorname{Sel}\) selects one physical half.
Thus \(Q_a\) is the \(16\times16\) physical action in equation (1). For
any cover-time indices \(s,t\), define the framed slice block

\[
\mathcal B_{a,\epsilon}(s,t)
=R_s^{\mathsf T}C_a[s,t]R_t,
\qquad
B_{a,\epsilon,j}
=\mathcal B_{a,\epsilon}(j,j+\epsilon).                  \tag{5}
\]

Here \(C_a[s,t]\) is the \(4\times4\) block at cover-time row \(s\) and
column \(t\), and \(R_s\) is the declared directional slice frame. No
diagonal block is inverted and no other time slice is eliminated. Thus
\(B_{a,\epsilon,j}\) is a raw distance-two stencil coefficient, not a
Schur complement.

Equation (3) proves that an inverse-based solve using \(B\) alone is
unavailable. It does not supply the three-term recurrence written in the
old note, does not prove that a complete equation has a free next-state
family, and does not exclude a descriptor system, constraints, a
pseudoinverse with compatibility conditions, or an enlarged state.

## 7. The complete grouped control

For each displayed origin, direction, and step, the runner constructs two
complete adjacent maps:

\[
G_{a,\epsilon,j,s}
=
\begin{pmatrix}
\mathcal B_{a,\epsilon}(s,t_0) & \mathcal B_{a,\epsilon}(s,t_1)\\
\mathcal B_{a,\epsilon}(s+1,t_0) & \mathcal B_{a,\epsilon}(s+1,t_1)
\end{pmatrix}.                                             \tag{6}
\]

Here \(t_0,t_1=(s+2,s+3)\) for direction \(+2\), and
\((s-2,s-1)\) for direction \(-2\). Equation (6) is only notation for
that explicit \(8\times8\) assembly; it is not a Schur elimination.

All sixteen displayed \(G\) matrices are singular, with rank census

\[
\#\{\operatorname{rank}G=4\}=12,\qquad
\#\{\operatorname{rank}G=3\}=4.                           \tag{7}
\]

The old test inspected one diagonal \(4\times4\) block twice. The corrected
test multiplies the full \(8\times8\) map by the corresponding embedded
witness. Ten cases annihilate that chosen embedding and six do not.
Equation (4) is an explicit counterexample.

This full-map control is useful, but it is still finite. It does not cover
all blockings or establish a common kernel, a descriptor no-go, or a
universal evolution obstruction.

## 8. Correct finite census

| checked object | result | limit |
|---|---|---|
| displayed physical matrices | unequal; first checked difference \(-89/140\) | no transition-equivalence test |
| cover support | five time bands | no gluing consequence |
| doubled spatial shift | commutator rank \(32\) twice | only this shift reduction |
| eight raw \(4\times4\) blocks | rank \(3\), framed kernel \(e_2\) | no elimination performed |
| sixteen full \(8\times8\) maps | ranks \(3\) or \(4\) | two adjacent groupings only |
| embedded \(e_2\) control | 10 zero, 6 nonzero | disproves universal survival |
| common differential | not constructed | open route |
| transition-compatible action | not constructed or ruled out | open route |
| true Schur/descriptor evolution | not constructed or ruled out | open route |
| reflection positivity | not tested | open route |

There is no universal dependency-order theorem. The common differential is
one natural open construction because Block 105 names it. It is not proved
necessary for every curved formulation.

## 9. No-Go Discipline Gate

The original W1 no-go does not pass this gate. The live result is demoted to
a finite partial narrowing.

### N1 — Alternative routes

| route against the old no-go | honest status | present result |
|---|---|---|
| construct a common differential or connection residual | NOT ATTEMPTED | remains open |
| define and test an actual transition relation between the two matrices | NOT ATTEMPTED | matrix inequality alone is silent |
| derive a true Schur complement or descriptor pencil | NOT ATTEMPTED | raw block singularity does not decide it |
| enlarge or regroup the state | ATTEMPTED only for two adjacent \(8\times8\) assemblies | those maps are singular, but the claimed fixed kernel fails |
| use a companion-free direct Gram OS test | NOT ATTEMPTED | remains open |
| change the curved fixture, chart family, or Hodge | NOT ATTEMPTED | remains open |

Fewer than five route families are attempted or ruled out by prior retained
authority. A universal no-go therefore fails N1. No route family is
manufactured to obtain a packet PASS.

### N2 — Wall relations

The live note declares no independent wall set. Matrix inequality,
noncommutation, raw-block rank, and grouped-map rank concern different
objects, but that difference does not prove logical independence. Closing
one may change the construction in which the others are evaluated.

### N3 — Hidden assumptions

| phrase or construction | classification |
|---|---|
| Block 105 fixture | explicit conditional finite input |
| directional frame | coordinate choice stated in Section 2 |
| antiperiodic quotient | explicit finite fold, checked on the displayed cover |
| “action matrix” | the two finite matrices built by the runner; no global interpretation |
| “momentum” | eigenspaces of the displayed spatial shift only |
| Block 127 | dated roadmap context only |
| “common differential” | open proposed construction, not a premise |

No framework primitive supplies the missing physical or transition
identification.

### N4 — Residual matching

Block 105 supports the finite overlap Hodge and leaves common descent open.
The current residual is exactly that no transition-compatible action has
been constructed for these displayed chart choices. It does not match a
claim that such an action cannot exist.

Block 127's old handoff names a curved-carrier dependency. It does not prove
the flat apparatus, its physical interpretation, or a universal order on
curved constructions. It is kept only as historical routing context.

### N5 — Resolution audit

The runner emits these exact lines:

```text
N5: per_element: checked — two displayed 16x16 physical matrices differ at entry (10,11) by exact -89/140; no transition equivalence is tested
per_site: checked — the doubled alternating form represents one complex Grassmann mode and its conjugate at each of 16 physical sites, not two site modes
per_mode: checked — rank[Q_alt,Sx⊕Sx]=32 for each displayed matrix, so this spatial-shift eigenspace reduction is not invariant; other spectral descriptions are open
per_block: checked — eight raw framed distance-two 4x4 blocks have rank3 and kernel e2; sixteen full adjacent 8x8 maps have ranks3/4, and the embedded e2 witness fails in six
lattice_wide: checked and not executed — no common differential, transition law, true Schur elimination, descriptor evolution, direct Gram OS proof, ADM/history transporter, joint gravity, Records, or TOE closure is constructed
```

These statements distinguish checked finite matrices from unexecuted
lattice-wide constructions.

### N6 — Partial-closure routes

No axiom amendment is needed for the finite identities. A later common
differential or a conventionally specified transition law would be an
explicit extra construction whose hypotheses could be tested. Descriptor,
constraint, enlarged-state, direct-Gram, and alternate-fixture routes also
remain open. No route is rejected merely because it bypasses the historical
program order.

### N7 — Steelman

The strongest objection to the old no-go is constructive. Raw coordinate
matrices from two charts can differ while describing one object after a
nontrivial transition. A singular leading block can define a regular
descriptor system once constraints and the full pencil are included. The
counterexample in (4) already shows that regrouping changes the relevant
kernel. Until a transition, full elimination, or descriptor analysis is
done, neither global-action nonexistence nor universal evolution failure is
available.

This objection is inside the old claimed domain, so the old no-go is
premature. The canonical claim is narrowed accordingly.

### N8 — Cross-cycle echo

The Block 127 handoff and Block 105 next decision are preserved as dated
history. They motivated this computation, but their ordering language does
not become a theorem through repetition. The present correction keeps the
finite matrix data and returns the unexecuted constructions to the open
queue.

**No-Go Discipline verdict:** **FAIL** for the original W1 no-go and its
universal construction order. **PARTIAL NARROWING** for equations (1)--(4)
and the finite census. No no-go packet PASS is claimed.

## 10. Disposition

What survives:

- two exact finite action matrices on the displayed conditional fixture;
- their unequal entry \(-89/140\);
- five time bands;
- two full-rank spatial-shift commutators;
- eight rank-three raw distance-two blocks with a framed \(e_2\) kernel;
- sixteen singular full grouped maps with ranks three or four; and
- an explicit \(9/80\) counterexample to fixed-kernel regrouping.

What is withdrawn:

- calling the raw blocks Schur complements;
- deriving a next-state family from those raw blocks;
- claiming a regrouping-stable coordinate kernel;
- treating unequal matrices as transition inequivalence;
- inferring absence of a global curved action;
- claiming three independent walls or stages;
- claiming the common differential is a proven bottleneck; and
- prescribing a universal curved-construction order.

Historical caches do not certify this corrected source. A fresh bounded
producer run and same-reviewer affected-fix confirmation are required before
landing. Formal audit remains deferred.

## 11. Next decisions

The finite data supports several distinct next questions:

1. define a transition relation and test whether the two chartwise actions
   descend from one operator;
2. derive the actual eliminated or descriptor system before asking for a
   forward evolution map;
3. test other full groupings or an enlarged state if they are scientifically
   motivated;
4. test reflection positivity directly through a finite Gram construction;
   and
5. construct the common differential or connection residual proposed by
   Block 105.

None of these is completed or ruled out here. The scalar quotient,
cross-lane bridge, physical ADM/history transporter, joint gravity, gravity
constraint quotient, Records, retention, and TOE closure remain open.
