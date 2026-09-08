---
claim_id: terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "The exact supplied Block-7 A/B ternary qubit instruments admit one fixed supplied program-controlled, freshness-flag, four-sector Hilbert CPTP channel. On each definite program P_c, blank register, fresh flag, and arbitrary system input rho, it reproduces the canonical label-retaining ternary cq instrument; one complementary hold Kraus operator fixes the complete 28-dimensional inactive Hilbert subspace and its 784-dimensional operator algebra, plus the complete terminal algebra. The channel is total and idempotent on this finite factor model and makes each terminal atom subharmonic with incoming effect K_j^dagger K_j. Its total Kraus/Choi rank is four, while its active blank formation corner has rank three; two pure-environment qubits suffice for either, and no export/no-return transport is derived. The program, four-sector register, system, freshness flag, and two environment qubits use seven qubit tensor factors, but no spatial placement, edge-gate compiler, or lattice-wide overlap law is claimed. One ordinary qubit cannot host blank plus three nonzero pairwise-orthogonal perfectly readable sectors because their ranks sum to at least four. For the specified forgetful map identifying (absent,beta) and (present,beta), a tagged transition assigning different successors on that fibre cannot factor through bare M2; support-restricted sentinel encodings are not excluded. This narrow Hilbert/type boundary does not constrain the framework's non-Hilbert Record ontology: three distinct M2(C) content candidates have positive support in an explicitly supplied uniform site menu, but no quantum-to-Record formation kernel is constructed. Conditional on target-site formation, law-admissible membership, and the stipulated diagonal table, only terminal atom Q_j paired with content kappa(j) has support; an explicit off-diagonal table has the same two marginals but nonzero mismatch. Equality of the actual site Admissibility marginal with the instrument central marginal, target formation, candidate calibration, lattice-wide overlap-safe autonomy, and unbounded resource renewal remain separately supplied inputs grouped into the three interfaces audited below. The block neither constructs a total homogeneous nearest-neighbour Record dynamics nor derives Born weights, and it makes no axiom amendment, audit verdict, obligation retirement, or TOE-percentage change."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_bounded_theorem_note_2026-08-20
  - fixed_carrier_presence_separated_nondemolition_record_update_boundary_bounded_theorem_note_2026-08-20
runner: scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_2026_08_20.py
---

# Terminal-Center Site-Record Diagonal Commit And Minimal-Carrier Boundary

**Date:** 2026-08-20

**Type:** bounded theorem with a narrow Hilbert-sector boundary

**Authority:** proposal only; independent audit controls retention
**Review mode:** direct author, independent executable, periodic independent
physics panel, and no-go discipline; review-loop was not used

**Primary runner:**
[`scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_2026_08_20.py`](../scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_2026_08_20.py)

**Independent reconstruction:**
[`scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20.py`](../scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20.py)

**Canonical caches:**
[primary](../logs/runner-cache/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_2026_08_20.txt) and
[independent](../logs/runner-cache/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20.txt)

**Exact source packet:** the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
the [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md),
[Block 6](INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md),
[Block 7](FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md),
and [Block 8](FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md).

## 1. Result Up Front

Block 8 left one tempting but ill-typed shortcut: call its three terminal
projectors one framework site Record. This block replaces that shortcut with
an exact type discriminator and the smallest fixed-carrier endomorphic
register for one blank plus three orthogonal terminal statuses. Typed
external-input or non-endomorphic routes can use smaller output spaces and are
not excluded.

Let a four-dimensional output register have basis

```text
|b>, |0>, |1>, |2>,
```

where `b` is blank and the remaining vectors are terminal labels. For either
exact A/B ternary instrument, with Kraus operators `K_cj`, define

\[
 W_{c j}=|j\rangle\langle b|\otimes K_{c j},\qquad
 H=T\otimes I_2,qquad
 T=\sum_{j=0}^2|j\rangle\langle j| .                 \tag{1}
\]

The four Kraus operators `(W_c0,W_c1,W_c2,H)` define a total CPTP channel
`Lambda_c`. On a blank register and arbitrary live-system input `rho`,

\[
 \Lambda_c(|b\rangle\langle b|\otimes\rho)
 =\sum_j |j\rangle\langle j|\otimes K_{c j}\rho K_{c j}^\dagger . \tag{2}
\]

Equation (2) is exactly the Block-7 label-retaining cq instrument, without an
input probability table. Every terminal-supported operator is fixed, and
`Lambda_c^2=Lambda_c`; thus the complete declared finite channel forms from
the blank corner and is absorbing thereafter. In the Heisenberg picture,

\[
 \Lambda_c^*(Q_j\otimes I)
 =Q_j\otimes I+|b\rangle\langle b|\otimes E_{c j}
 \ge Q_j\otimes I,
 \quad E_{c j}=K_{c j}^\dagger K_{c j}.              \tag{3}
\]

The inequality, rather than equality, is the correct permanence condition:
it preserves already terminal atoms while allowing probability to flow into
them from blank.

This is the positive finite answer that the Block-8 reversible boundary left
open. It is not a lattice-wide autonomous nearest-neighbour law. The context,
register placement, one-shot application, candidate-content calibration, and
fresh environment are supplied.

There is also one stronger **conditional Hilbert-factor** form with no
host-selected A/B channel call.
Add a supplied program qubit `P` with atoms `P_A,P_B` and a supplied one-shot
freshness flag `F` with `|fresh>` and `|spent>`. On tensor order `P,R,S,F`, set

\[
 A_j=\sum_{c=A,B}P_c\otimes|j\rangle\langle b|\otimes K_{c j}
                 \otimes|spent\rangle\langle fresh|,
\quad G=I_P\otimes|b\rangle\langle b|\otimes I_S\otimes P_{fresh},
\quad H_{\rm int}=I-G .                              \tag{1a}
\]

The one fixed channel with Kraus operators `(A_0,A_1,A_2,H_int)` reads its program
factor, flips the freshness flag, and needs neither a host-selected A/B channel call
nor a post-write switch. On a **definite** `P_c`, blank `R`, fresh `F`, and
arbitrary system input it returns the exact context-`c` cq output. A coherent
program input instead retains a supplied coherent A/B Kraus alignment and is
not interpreted as classical program selection. The channel is identity on the full 28-dimensional
inactive Hilbert subspace, including terminal, spent-flag, and other nonactive
sectors; active/inactive coherences are discarded. The runner checks the
projector identities covering all `28^2=784` inactive matrix units.

Program, freshness flag, and environment are not thereby framework Records or
licensed complete-state variables. In particular the flag changes from fresh
to spent and cannot be a permanent Record. Their preparation, target placement, invocation,
Record-configuration typing, and renewal remain supplied. This construction
removes only the host A/B call and the separate post-write future map inside
the finite Hilbert model.

For the integrated channel `Phi`, define

\[
 O_j=I_P\otimes Q_j\otimes I_S\otimes I_F .
\]

Its atomwise permanence statement is exactly

\[
 \Phi^*(O_j)=O_j+
 \sum_{c=A,B}P_c\otimes |b\rangle\langle b|\otimes E_{cj}
                         \otimes P_{\rm fresh}\ge O_j .          \tag{1b}
\]

This is permanence under repeated application of the isolated reduced
channel. It is not permanence under interleaved lattice updates or reversal
of a unitary dilation.

The type discriminator is equally exact. One ordinary qubit cannot host blank
plus three nonzero pairwise-orthogonal readable sectors: four nonzero
orthogonal support projectors have rank sum at least four, while `C^2` has
dimension two. A four-sector register is minimal and Hilbert-isomorphic to a
supplied `C^2 tensor C^2` factorization. This is not a spatial placement. Four
nonorthogonal qubit POVM effects exist, but they are not four perfectly
readable absorbing status sectors.

That rank statement is deliberately not promoted into a Record no-go. A
framework site Record locks one **admissible** possibility in `M_2(C)`; Record
does not say that absence and its readable contents are orthogonal
density-operator sectors inside the same `C^2`. Three distinct matrices can
therefore serve as candidate contents. The runner supplies a uniform site menu
with all three candidates at positive mass, establishing support compatibility
for that menu only. Use as contents of the actual framework law remains
conditional on

\[
 \kappa(j)\in\operatorname{supp}
 \mu_{\mathrm{Adm},x}(\cdot\mid\eta,\mathrm{formation})             \tag{3a}
\]

for every positive branch. The four-sector register is not one framework site
Record.

Finally, a stipulated diagonal table is the candidate relation needed to join
the two types, conditional on target formation, equation (3a), and
law-admissible membership:

\[
 \Pr(Q_j, R_x=\kappa(j)\mid\rho,c,F_x,\eta)
 =\operatorname{Tr}(E_{c j}\rho),\qquad
 \Pr(Q_j,R_x=\kappa(k)\mid\rho,c,F_x,\eta)=0\quad(j\ne k),       \tag{4}
\]

where `F_x` denotes the separately supplied event that target `x` forms under
shell `eta`, and equation (3a) is required. Equation (4) is a hypothetical
joint table, not a derived conditional distribution of the current framework.

For any separately supplied law-admissible realized pair in this table's
support, the candidate content decodes the same label as the carrier atom.
This is a conditional diagonal support correlation. The table is not a
quantum-to-Record channel, site-formation kernel, realized pair, or draw. An
explicit off-diagonal table preserves both marginals while carrying positive
mismatch mass, so equal marginals do not force diagonal support.

The strongest remaining numerical datum is still

\[
 \mu_{\mathrm{Adm},x}(\kappa(j)\mid\eta,\text{formation})
 =\operatorname{Tr}(E_{c j}\rho_\eta),               \tag{5}
\]

with the preparation/effect registration typed physically. Admissibility
marginal equality remains supplied. Neither the channel algebra nor the
candidate codes derive (5), target formation, or membership of the supplied
realized state in equation (4).

This is significant route clarification, not retained TOE closure. Audit
status is unset. Retained status is unset. Zero obligation retirement. TOE
percentage movement is zero. No axiom amendment is mature.

For machine-facing scope checks, the exact conclusions are repeated plainly.
One ordinary qubit cannot host blank plus three nonzero pairwise-orthogonal
readable sectors. Equal marginals do not force the diagonal coupling.
Admissibility marginal equality remains supplied. The finite four-sector
register uses a separately supplied classical calibration and is not a
lattice-wide autonomous nearest-neighbour law. Formation site, rate, overlap
arbitration, and unbounded environment renewal remain open. No axiom amendment is
mature. No-Go Discipline Gate: PASS.

## 2. Three Types, Kept Separate

The proof uses three different state spaces.

| object | mathematical type | what it supplies | what it does not supply |
|---|---|---|---|
| four-sector commit register | `C^4 tensor C^2` density operators | blank/terminal orthogonality, cq output, absorbing CPTP update | framework site presence or Record content |
| one-site content candidate | partial-map status `absent` or one supported content in `M_2(C)` | a possible at-most-one/content-only Record interface once an actual law forms it | admissibility in the actual shell, formation, a density operator, Hilbert inner product, or CPTP writer |
| joint coupling candidate | probability table on `(Q_j,candidate content)` | conditional diagonal support correlation | formation, law-admissible realized membership, or equality to Admissibility |

For a concrete one-site content calibration use

\[
 \kappa(j)=i(j+1)I_2,\qquad
 d(\kappa(j))={1\over2}\operatorname{Im}\operatorname{Tr}\kappa(j)-1=j.
                                                               \tag{6}
\]

The three matrices are distinct and invariant under simultaneous unitary
conjugation. The decoder is a partial function defined only on present declared
contents and depends on content alone. `absent` is outside its domain, not a
fourth matrix or sentinel readout. In the candidate map, blank `000` and
pending `100` leave the target absent, while the corrected Block-8
outcome-zero word `010` maps to the nonblank candidate `kappa(0)`. Conditional
on equation (3a) and target formation, that candidate can be locked as a
Record. No Record is never used as recorded zero.

Equation (6) is a calibration candidate, not a quantum-state encoding. The
codes are anti-Hermitian central possibilities, not density operators. The
current Qubit axiom permits them in the possibility domain, but the current
axioms do not select this menu, the output site, or its formation law.

The external-tag factorization boundary has a self-contained two-point
witness. Let `q` forget the presence tag, let `beta=I_2/2`, and specify the
tagged transition `D` on one fibre by

\[
 q(\mathrm{absent},\beta)=q(\mathrm{present},\beta)=\beta,
\quad D(\mathrm{absent},\beta)=(\mathrm{present},\kappa(0)),
\quad D(\mathrm{present},\beta)=(\mathrm{present},\beta).          \tag{6a}
\]

Because `kappa(0)=i I_2` differs from `beta`, the two successors differ. If
\(D=f\circ q\) for any tag-blind map `f` on bare `M_2`, they would have to agree,
a contradiction. This proves only nonfactorization of this specified tagged
transition through this forgetful map. It does not exclude tagged kernels or
support-restricted sentinel encodings whose bare matrices already distinguish
their statuses.

## 3. Exact Total Absorbing Channel

The ternary normalization identity gives

\[
 \sum_j W_{c j}^\dagger W_{c j}
 =|b\rangle\langle b|\otimes I_2,
 \qquad H^\dagger H=T\otimes I_2.                   \tag{7}
\]

The sum is the identity on the complete eight-dimensional register-system
space. The channel is therefore defined on blank, terminal, coherent,
off-code, and mixed inputs; no reachable-corner partial map is being called
CPTP.

After one application every output lies in the terminal face. On that face,
`W_cj` vanishes and `H` is the identity. Therefore the channel fixes every
terminal population, every within-terminal coherence, and every correlated
terminal-system operator. It also follows immediately that it is idempotent.

For each terminal atom, equation (3) gives exact subharmonicity. A future
label-swap unitary fails it atomwise and is rejected. Permanence here is under
repeated application of this one declared finite-cell channel `Lambda_c`, not
under every imaginable quantum operation or every update of a future global
law. Treating a label-mixing map as physically allowed would change the law
and destroy the result.

This totality is finite-register totality only. It does not cover a global
lattice with competing apparatuses, overlapping cells, depleted resources, or
multiple contexts. Those cases belong to the global trajectory law that this
block does not claim to construct.

## 4. Environment And Resource Ledger

The three writers and terminal hold have mutually distinct register source or
target support and are linearly independent for both exact A/B programs. The
total channel's Kraus/Choi rank is therefore four. A pure Stinespring
environment for the total endomorphic channel has dimension at least four; a
two-qubit environment suffices. Restricted to the active blank formation
corner, only the three writers occur and the rank is three. A qutrit is minimal
there, also fitting in two qubits.

The runner constructs the exact isometry

\[
 V_c=\sum_{a=0}^{3}|a\rangle_E\otimes L_{c a},
 \quad (L_{c0},L_{c1},L_{c2},L_{c3})
 =(W_{c0},W_{c1},W_{c2},H),                         \tag{8}
\]

checks `V_c^dagger V_c=I`, and traces the environment to recover `Lambda_c`.
On blank input only the three outcome codes occur. The fourth code is the
terminal-hold route needed for a total absorbing channel.

This is an output branch environment in a Stinespring representation. The
runner does not place it on the lattice or prove export, no-return transport,
or reblanking. If an ordinary pure dilation is used, one active application
needs a fresh environment of dimension at least three; one pure dilation of
the total endomorphic channel needs dimension four. An unbounded sequence of distinct
target commits would need a physical fresh/renewal or archive law, or would
have to take the nonunitary channel itself as fundamental. This block supplies
none of those global resource mechanisms.

## 5. Diagonal Coupling And The Marginal Trap

At `rho*=diag(3/5,2/5)`, the exact central weights are

```text
A: (3/10, 19/50, 8/25)
B: (3/10,  7/20, 7/20).
```

For either vector `p`, equation (4) is the diagonal matrix `diag(p)`. Its row
marginal is the quantum terminal label distribution and its column marginal
is the candidate site-content distribution. Every positive cell has matching
labels. Therefore any separately supplied law-admissible realized pair in its
support has equal decoded and carrier labels.

This conditional statement uses the realized-state primitive only for
pointwise evaluation after law-admissible membership is separately supplied.
The primitive does not supply target formation, membership in equation (4), a
state, sample, measure, probability, or value.

Marginal equality is weaker. For any
`0<epsilon<=min(p0,p1)`, replace the upper-left two-by-two diagonal block by

\[
 \begin{pmatrix}p_0-\epsilon&\epsilon\\
                 \epsilon&p_1-\epsilon\end{pmatrix}.              \tag{9}
\]

Both marginals remain exactly `p`, but the mismatch probability is
`2 epsilon`. The runner uses `epsilon=1/10` in both contexts. Consequently,
neither a shared probability vector nor equality of the two marginal laws
derives diagonal support. The diagonal relation must be supplied or derived as
part of the physical bridge.

Conversely, a supplied normalized uniform site menu gives every candidate
positive support but differs from the exact quantum marginal. Support legality
does not derive the weights. Three obligations are distinct:

1. **conditional coupling:** support only on `(Q_j,kappa(j))` after formation;
2. **central marginal compatibility:** the common marginal is the
   Admissibility distribution and equals the instrument central restriction;
   and
3. **formation/realized membership:** the declared target forms and the
   supplied law-admissible realized pair belongs to that coupling.

Block 9 writes and validates the first as a stipulated finite table. It does
not turn that table into a site formation kernel. The second is the minimum
numerical law datum; the third belongs to the trajectory/resource law and
contingent history.

## 6. Why This Is Not Another Generic Markov Law

Block 6 already supplies total Borel nearest-neighbour Record kernels with
occupied-site absorption, malformed-shell fallback, and a finite path
extension. The June Markov boundary already separates a discrete production
kernel from a continuous-time generator and rate. The July full-Z3 campaign
already constructs homogeneous append fronts and prices scheduling,
occurrence, and finite capacity.

Repeating those objects would not advance the live seam. The new content here
is instead a type-level coupling **discriminator** on the exact Block-8
terminal center, together with a total absorbing quantum counterroute and its
minimal factor/environment-rank ledger. A physical site coupling remains open.
The old rank observations are direct prior art; no novelty is claimed for rank
additivity itself.

The finite channel still does not satisfy the stronger Block-9 candidate
contract for one homogeneous global law. In particular it has a supplied
program value/genesis, target placement, and invocation; no covariant event
guard, overlap arbitration, formation rate/order, or unbounded resource
renewal. It is a killable bounded discriminator, not a disguised
arbitrary-horizon closure.

## 7. Exact Boundary And Next Discriminator

What is now exact:

- the smallest ordinary Hilbert register for blank plus three orthogonal
  terminal atoms has dimension four;
- a total finite nonunitary channel maps the blank corner to the exact A/B cq
  instrument and fixes the terminal face;
- atomwise subharmonicity gives the correct inflow-compatible permanence
  condition;
- the total channel uses a minimal four-dimensional pure environment;
- a supplied uniform site menu can give all three content candidates positive
  support, without selecting the actual Admissibility law; and
- a stipulated diagonal table gives conditional support agreement, while
  equal marginals alone do not.

What remains open:

- derive or physically select the quantum-to-Record calibration;
- derive equation (5), including the preparation/effect quotient;
- choose a formation site and rate through the same local law;
- compile one translation/proper-cubic-covariant strict-nearest-neighbour
  trajectory law, total on malformed inputs and overlaps;
- supply program/freshness/environment typing and genesis, plus environment
  renewal or an increasing archive; and
- obtain independent audit retention and obligation retirement.

The next high-leverage test is not another pointer. It is a central-law
discriminator on the candidate-typed event: require a single local site event map
and test whether operational preparation/effect equivalence plus affine
randomization forces equation (5), or leaves an exact wrong-effect law alive.
If a wrong-effect law survives the complete physical equivalence class, the
missing law datum is isolated enough for an owner-facing constitutional
decision. If equivalence forces the trace form, the Born/Record lane advances
without an axiom edit.

## 8. No-Go Discipline Gate

**Gate status: PASS.** **No-Go Discipline Gate: PASS.** Four insufficiency
statements are narrowly typed: one ordinary `C^2` Hilbert output cannot contain
four nonzero mutually orthogonal status sectors; a specified tagged transition
that differs on `(absent,beta)` and `(present,beta)` cannot factor through the
forgetful map that identifies their bare `M_2` value; equal marginals do not
force diagonal support; and positive support on all three candidates does not
fix their weights. None is a no-go for site Records, support-restricted sentinel
encodings, tagged extensional kernels, stochastic formation, general POVMs,
two-qubit carriers, nonunitary channels, or increasing archives.

### N1 — Alternative route enumeration

| route | marker | attempted attack | exact disposition | authority / executable artifact |
|---|---|---|---|---|
| four ordinary orthogonal sectors in `C2` | `ATTEMPTED` | use one nonzero support projector for blank and each of three outcomes | rank sum is at least four and exceeds dimension two | retained type premise `MINIMAL_AXIOMS_2026-06-29.md:43-53`; current rank proof and primary check `single-m2-four-sector-rank-boundary`; direct prior-art echo `FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md:311` |
| nonorthogonal four-effect POVM | `ATTEMPTED` | replace output sectors by four normalized positive effects | the effects exist, but overlap and do not give four perfectly readable absorbing statuses | retained type/readout premises `MINIMAL_AXIOMS_2026-06-29.md:43-53,75-83`; current primary check `nonorthogonal-povm-route-does-not-meet-status-target` |
| arbitrary/non-Hermitian `M2` Record contents | `ATTEMPTED` | use three algebraically distinct contents plus external absence | this succeeds as a candidate calibration/menu and therefore blocks every broader Record no-go; it is not four Hilbert sectors | retained type/Record premises `MINIMAL_AXIOMS_2026-06-29.md:43-53,75-83`; current equation (6) and primary check `one-site-record-code` |
| `C4` or supplied `C2 tensor C2` factorization | `ATTEMPTED` | enlarge the ordinary output space to four orthogonal atoms | this succeeds exactly and is the minimal dimensional escape, without supplying spatial placement | retained one-site type premise `MINIMAL_AXIOMS_2026-06-29.md:43-53`; current equations (1)-(3) and primary checks `minimal-four-sector-counterroute`, `total-cptp-terminal-commit` |
| irreversible stochastic/CPTP commit | `ATTEMPTED` | relax Block 8's reversible-update condition | equation (1) succeeds, so no irreversible or universal measurement no-go survives | retained formation/permanence target `MINIMAL_AXIOMS_2026-06-29.md:75-83`; current equations (1)-(3) and primary check `idempotent-absorbing-future-law` |
| same-marginal non-diagonal coupling | `ATTEMPTED` | infer actual correlation from equality of the Record and carrier marginals | equation (9) survives with mismatch, so diagonal support must be supplied or derived separately | retained distribution/support distinction `MINIMAL_AXIOMS_2026-06-29.md:55-73`; current equation (9) and primary check `same-marginal-off-diagonal-hostile` |
| positive-support free-weight menu | `ATTEMPTED` | infer the central weights from legality/support of all three contents | a normalized uniform menu keeps every candidate supported but differs from both A/B trace marginals | retained distribution/support distinction `MINIMAL_AXIOMS_2026-06-29.md:55-73`; current primary check `admissibility-marginal-free-law-control`; prior exact echo `INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md:409-446` |
| tag-blind single-site factorization | `ATTEMPTED` | make one map on bare `M2` distinguish `(absent,beta)` from `(present,beta)` | the specified forgetful map identifies the two inputs while the tested tagged transition assigns different successors; tagged kernels and support-restricted sentinel encodings survive outside the claim | retained Record/readout premise `MINIMAL_AXIOMS_2026-06-29.md:75-83`; current equation (6a) and primary check `external-presence-tag-collision` |

These are eight distinct mechanism families: projection geometry, generalized
measurement, Record ontology/calibration, carrier enlargement, irreversible
dynamics, probabilistic coupling, support-versus-weight freedom, and
external-tag factorization. No route is counted by changing notation or
reviewer.

Authority note: every row is marked `ATTEMPTED`, not `RULED OUT BY PRIOR`.
Each row cites the retained minimal-axiom premise that defines its framework
type or target; the cited current equations and two executables then supply
the new self-contained witness. The current witnesses are proposal evidence,
not mislabeled retained conclusions, and the prior rows in N4 are provenance
only. Thus gate `PASS` records completion and honest scoping of the stress
test, not audit retention of the new theorem.

### N2 — Wall-independence audit

The remaining TOE interfaces collapse to three walls:

- `W_C`: classical quantum-to-Record content/diagonal-commit calibration;
- `W_M`: equality of the site Admissibility marginal with the physical
  instrument central marginal; and
- `W_L`: one lattice-wide autonomous local trajectory/resource law.

`W_L` is one deliberately conjunctive terminal contract: target-site
formation/rate, overlap-safe global dynamics, and resource genesis/renewal
must coexist in that law. This note does not assert that those internal
subconditions are independent walls. N2 tests independence only among the
three interfaces `W_C`, `W_M`, and conjunctive `W_L`.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `W_C`,`W_M` | no: matching labels does not fix weights | no: equal marginals allow equation (9) | yes |
| `W_C`,`W_L` | no: one finite calibration gives no global guard/resource law | no: a global law may use another content interface | yes |
| `W_M`,`W_L` | no: one equality gives no formation site/rate or renewal | no: a complete trajectory can carry wrong-effect weights | yes |

Environment freshness is not counted as a fourth independent wall: for a pure
dilation it is part of `W_L`'s resource boundary. Conditional realized-pair
correlation is not a fourth independent wall, but it does **not** follow from
`W_C` alone: it requires diagonal calibration in `W_C`, formation/site and
resource membership from `W_L`, Admissibility legality/identification from
`W_M`, and only then pointwise evaluation at the separately supplied
law-admissible realized state.

### N3 — Hidden-wall scan

The note and runner were scanned for the required phrases and close variants.

| phrase family | classification |
|---|---|
| “we assume” | absent outside this checklist description |
| “by construction” | absent; equations (1), (4), and (8) are explicitly defined supplied objects |
| “as is standard”, “naturally”, “obviously”, “standard QFT” | absent |
| “the framework provides” | absent; exact axiom and primitive content is quoted by linked source instead |
| “bridge context”, “background” | absent as load-bearing prose |
| “registered” / “canonical” | `canonical cq` names Block 7's explicitly defined direct-sum object; `registration` names an open interface, not retained authority |

No hidden condition was promoted after the scan; the three-wall count above
stands.

### N4 — Residual matching

| source | source residual | present residual | match? / use |
|---|---|---|---|
| `docs/FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md:390` | one finite reversible update cannot both enter and preserve a disjoint terminal sector | dimension of one ordinary `C2` blank-plus-ternary output | **no**; context only, not a witness |
| `docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md:258` | faithful complex-linear/full-cq one-site algebra representation | four orthogonal status supports including blank | **no**; context only, not a witness |
| `docs/work_history/repo/review_feedback/FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md:311` and `scripts/full_z3_causal_front_sampled_instrument_law_probe_2026_07_14.py:636` | too many nonzero orthogonal status sectors for one `M2` Hilbert carrier | same rank-sum status-sector residual, now with blank plus three outcomes | **yes, direct prior art**; current proof is self-contained and claims only exact-fixture absorbing-channel/coupling integration |
| `docs/work_history/repo/review_feedback/FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md:300` | `OPEN` is absence from the Record map, so status is additional to the bare density matrix | the specified transition in equation (6a) cannot factor through the tag-forgetting map | **no, mechanism-level echo only**; the prior note motivates the tag, but does not prove this transition-factorization residual and is not witness support |
| `docs/INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md:409` | trace-matched and free-weight laws share typed support while their weights differ | positive support for all three candidate contents does not determine the trace marginal | **yes, direct prior art**; the current uniform menu is an exact one-site instantiation |
| `docs/INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md:497` | a deterministic affine map cannot choose nonconstant definite sectors | output-register dimension and diagonal joint coupling | **no**; not used as no-go support |
| `docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md:80` | binary fresh-fragment write isometry | ternary absorbing commit and site calibration | **no**; positive analogy only |

The two exact matching historical echoes are not needed for the proof. Nonmatching
citations are explicitly excluded from witness support.

### N5 — Rhetoric audit

The four narrow negative/insufficiency facts are resolution-scoped as follows:

| resolution | executed? | exact conclusion |
|---|---|---|
| per element | yes | four nonzero mutually orthogonal support projectors require total rank at least four |
| per site | yes, ordinary Hilbert/tag-forgetting reading only | an ordinary `C2` output cannot host those four sectors, and bare `M2` cannot recover a forgotten presence tag; a framework Record with external status and supported content is not excluded |
| per mode | yes | nonorthogonal POVM, classical calibration, `C4`, irreversible commit, diagonal/off-diagonal couplings, and support/free-weight modes are tested and remain distinct |
| per block | yes | exact A/B programs both admit the positive total `C4` commit channel |
| lattice wide | no | no lattice-wide impossibility is asserted; a global overlap-safe law remains open |

The primary cached stdout lands one substantive certificate line for each
resolution.

### N6 — Partial-closure path scan

No new axiom is required by the bounded result. Existing partial closures are:

| path | status | what it closes |
|---|---|---|
| one-site `M2` candidate content code/menu, equation (6) | supplied bounded construction here | label capacity and content-only decoder without Hilbert orthogonality |
| four-sector absorbing channel, equation (1) | supplied bounded construction here | finite quantum commit, terminal absorption, and environment-rank/factor ledger |
| Block 6 total Record kernel | proposal, audit unset | site append/support/path extension after its law values are supplied |
| realized-state primitive | approved primitive | pointwise evaluation at actual Record content, never its value or probability |
| controlled-copy/fresh-fragment route | prior bounded theorem | binary orthogonal write inside an explicit fresh-fragment model |

These are import-and-bound-theorem routes, not constitutional amendments.
An owner-facing axiom proposal would be premature until `W_C`, `W_M`, and
`W_L` are attacked by complete physical law candidates and independent audit.

### N7 — Steelman against the no-go

A hostile reviewer should reject any broad conclusion immediately: Record is
not defined as an orthogonal density sector in one site Hilbert space. The
Qubit axiom supplies `M_2(C)` as a possibility domain
(`docs/MINIMAL_AXIOMS_2026-06-29.md:43-53`), while Record adds presence,
content locking, and content-only readout
(`docs/MINIMAL_AXIOMS_2026-06-29.md:75-83`). Three distinct matrices such as
equation (6) therefore fit one site without four orthogonal vectors.
Block 6 already shows a total local classical kernel can append such contents.
The actionable route is to derive a physical diagonal calibration from the
four-sector cq carrier into that site-level law and then prove its
Admissibility marginal. This steelman defeats a broad site-Record no-go. The
shipped negatives remain only the ordinary-Hilbert-sector rank bound and the
specified tag-forgetting factorization bound; the coupling and support
controls are insufficiency witnesses, not universal no-gos. The positive
physical-law route is the next campaign target.

### N8 — Cross-cycle echo

Four similar walls were searched and their repair mechanisms were applied:

1. The July full-Z3 carrier work found that several orthogonal status sectors
   exceed one qubit, then escaped through distributed relational binary
   Records. This block keeps multisite and arbitrary-content routes live.
2. Block 7's panel rejected a broad one-site information no-go after an
   injective real-affine non-Hermitian `M2` code survived. This block again
   separates algebraic Record content from faithful Hilbert/*-algebra storage.
3. Block 8's reversible absorber boundary retained nonunitary and increasing
   archive escapes. Equation (1) executes the nonunitary finite escape and
   names environment renewal or increasing archive as the remaining global
   resource problem.
4. Block 6 executes a total tagged Record kernel and, separately, a
   support-identical free-weight law (`INSTRUMENT_PORT_TYPED_RECORD_COMPILER_`
   `CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md:409-446`). Those
   repairs are applied here by keeping tagged kernels live and treating
   candidate support as weaker than trace-weight identification.

No structurally similar repair was ignored. The cross-cycle history is why
this note ships a positive finite channel plus a narrow type boundary, not a
universal no-go.

## 9. Verification And Status

Run:

```text
python3 scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_2026_08_20.py
python3 scripts/terminal_center_site_record_diagonal_commit_minimal_carrier_boundary_independent_check_2026_08_20.py
```

The primary executable checks exact source needles, one-site code/absence
typing, the rank boundary and `C4` escape, A/B CPTP completeness, arbitrary
input totality, all-basis idempotence, terminal-face identity, atomwise
subharmonicity, the rank-four Stinespring ledger, diagonal and hostile
couplings, tomography marginals, and the no-go resolution certificate.
The independent executable rebuilds the effects and Kraus programs without
importing Block 9, then separately checks the simple and integrated channels,
dual identities, total/active ranks, type boundaries, and hostile couplings.
At source stabilization the primary result is `19/19` and the independent
result is `14/14`; the content-pinned caches above are the canonical evidence.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_narrowing
reachability_to_target: advances
conditional_surface_status: "exact finite absorbing Hilbert channel plus a stipulated candidate-content diagonal table, conditional on target formation, actual Admissibility compatibility, and separately supplied law-admissible realized membership"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
obligation_retirement: zero
toe_percentage_movement: zero
```
