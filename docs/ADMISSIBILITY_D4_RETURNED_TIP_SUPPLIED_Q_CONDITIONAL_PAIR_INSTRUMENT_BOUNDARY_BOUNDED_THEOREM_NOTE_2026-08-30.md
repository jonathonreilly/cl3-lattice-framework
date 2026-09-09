# Two supplied joint exit tables give conditional Record instruments

**Date:** 2026-08-30; correction 2026-09-09.
**Campaign block:** Source/Eta 28.
**Type:** bounded_theorem
**Standing:** conditional mathematical result; physical suppliers remain open.

Descriptions below of exhaustive runner checks refer to the archived original
controller unless named in the current evidence section. The displayed proofs
remain; the current entrypoint does not relabel old executions as fresh.

**Primary runner:** [`admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py`](../scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py).
**Current bounded cache:** [execution](../logs/runner-cache/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.txt).

Current framework boundary: [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

[Exact original bodies, versions and earlier evidence](../.claude/science/physics-loops/eta-pair-process-correction-20260909/HISTORY.md).

## Supplied local definitions and conditional factor lemma

The necessary Block22/23/24 definitions are stated here. Their exact callable
implementations are the two source-only helpers linked below; their wider
historical campaigns are not premises. Let the six live sites be
`n=epsilon e_j`, the fourteen outcomes be the six signed axes and eight signed
corners, and `tau=1/24`. Define the commuting six-qubit effect
`E_b=a_b I + sum_n w_(b,n) dot sigma^(n)` as follows:

- For an axial outcome on axis `k`, `a_b=1/12` and
  `w_(b,epsilon e_j)=(tau/4) epsilon (delta_kj-1/3)e_j`.
- For a corner `b`, `a_b=1/16`, the `j` component of
  `w_(b,epsilon e_j)` is zero and its `k != j` component is
  `(3 tau/32) epsilon b_j b_k`.

All local Pauli terms commute because they occupy distinct sites. Their
joint eigenvalues are `a_b+sum_n z_n |w_(b,n)|`, with six independent signs.
The minima are `1/18` for axes and `1/16-3 sqrt(2)/128>0` for corners.
Summing the fourteen effects gives identity: their constants sum to one and
the signed coefficient sums vanish. The positive root is therefore the
explicit spectral sum over all 64 sign sectors, with coefficient the positive
square root of that sector eigenvalue. Its square is exactly `E_b`.

For a source outcome `s`, put `u_s=s/|s|`, `Q_s=u_s u_s^T-I/3`, and prepare
at live site `n` the pure Bloch vector `v_(s,n)=Q_s n/|Q_s n|`.
These denominators are nonzero for all fourteen supplied outcomes and six
sites. The actual local transition is
`T(b|s)=a_b+sum_n w_(b,n) dot v_(s,n)`.
Positivity and row normalization follow from the positive effects and their
identity sum; the runner retains the literal spectral contraction, not just
this scalar formula.

The pointer sites are the six front sites `+-2e_j`, six axial outcome sites
`+-3e_j`, eight corner slots `2b`, and six STATUS sites `+-4e_j`, disjoint
from the six live sites. At relative site `r`, bit `q` is the projector
`(I+(-1)^q rhat dot sigma)/2`. Blank has all pointer bits zero and the six
outward radial live vectors. Ready_f has only its front bit at `2f` set.
Locked_(f,b) also sets all six STATUS bits and its geometric outcome slot.
At a supplied isolated anchor these complete product words are orthogonal;
packet grouping and radial frames are construction inputs. A bit is not a
context-free scalar: `P_0(r)=P_1(-r)`.

An append at anchor `x` reads the complete Locked_(f,s) word and selects target
`x+9f`; a turn selects `x+9g` with `g dot f=0`. It applies the rank-one live
preparation from the complete Blank live state to `v_s`, the Blank-to-Ready
pointer map, the positive root `sqrt(E_b)`, and Ready-to-Locked_(g,b) writer.
The old pointer projector and all old live identities remain, every unused
spectator site has identity, and the outside carrier has identity. Contracting
this literal sequence gives `T(b|s)` times its complete current/Blank input
projector. Distinct input words are orthogonal; summing targets and adding the
orthogonal complement STOP gives the conditional channel identity. This
proves QND for the old commuting pointer algebra, not nondisturbance of an
arbitrary noncommuting live state.

Translations transport the anchors. Proper cubic rotations transport the
site vectors, outcome labels, radial projectors and Pauli coefficients.
Functional calculus then transports the positive roots, and tensor products
transport every listed preparation, writer, control and identity factor.
This proves covariance of the supplied oriented family; no autonomous
invocation or global carrier formation follows.

Source-only definitions:
[local effects and pointer code](../scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py),
[append factors](../scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py).

## Exact target, inputs, and proof obligations

**Exact target.**  On the declared supplied returned-tip pair sector, construct
two full-space conditional CPTP instruments with the same literal carrier,
strictly positive joint exit support, uniform one-tip marginals, covariant QND
Record output, and different probabilities for one event decoded from Record
content.

| obligation | disposition in this note |
|---|---|
| literal local transition and writer factors | defined by the local factor lemma below and reconstructed by the source-only helpers |
| ten-block pair geometry and complete controls | proved by exact finite support and projector checks here |
| normalization, support, marginals, and covariance of both supplied joint tables | proved by exact symbolic algebra here |
| guarded Kraus contraction and full-space trace preservation | proved here for every source-pair control plus the complement STOP |
| arbitrary-reference extension | proved here from the same explicit complete Kraus family |
| readable distinction of the two instruments | proved here after decoding complete output Record configurations |
| singleton-compatible repeated process, autonomous invocation, and resource renewal | open; neither assumed nor concluded |

The later Block30 and Block33 notes analyze supplied two-use and cause architectures.
Their finite conclusions do not establish autonomous invocation or physical renewal.

The scientific inputs are separated as follows:

- the minimal axioms supply the Lattice, Qubit, Admissibility, and Record
  premises, but no displayed joint probability values or production process;
- the Block23/24 factors are explicit conditional definitions given below;
- the returned-tip carrier, eight Blank blocks, external invocation, and the
  two `q` tables are explicit supplied construction data; and
- no scale-reference, kinetic-isotropy, or realized-state primitive is used.

There is no observational or fitted input.  Exact symbolic arithmetic is a
proof tool, not an additional physics premise.

## Result up front

Two positive finite-sector instruments survive exact execution.

The carrier contains two existing current Records and the eight mutually
disjoint lateral Blank blocks available to the two inward-facing returned
tips.  For each pair of old Record outcomes there is one exact ten-atom
control: two complete Locked pointer projectors and all eight complete Blank
block projectors.  The `14 x 14 = 196` controls are pairwise orthogonal.

On every control, the left and right tips each have four lateral exit
directions.  Two supplied joint exit tables give complete compound Kraus
families.  Both tables are positive on all `16` exit pairs and give each tip
the same uniform exit marginal `1/4`.  The old Records remain QND, the selected
new target blocks become distinct Locked Records, all unused target blocks
remain Blank, and the complement of the `196` active controls carries one
common STOP.

The two instruments are physically distinguishable by Record content.  Let
`D` be the event that the two decoded new exit directions agree.  The exact
conditional probabilities are

\[
   \Pr_0(D)=\frac14,
   \qquad
   \Pr_{1/2}(D)=\frac58.                                  \tag{1}
\]

This is a meaningful positive bridge, not yet two physical process laws.  The
joint tables, pair carrier, Blank resources, and invocation are supplied.
The runner does not show that either instrument is reachable from the same
singleton process, remains consistent under repeated use, renews its finite
resources, or is selected by Admissibility, action, source, or gravity.

## The two supplied joint tables

Let `G` be the four lateral directions perpendicular to the incoming front.
For `g,h in G`, define

\[
 q_\lambda(g,h)=
 \begin{cases}
  (1+3\lambda)/16, & g=h,\\
  (1-\lambda)/16, & g\ne h.
 \end{cases}                                               \tag{2}
\]

The runner uses only the two supplied choices

\[
 \lambda=0,
 \qquad
 \lambda=\frac12.                                         \tag{3}
\]

For either choice, every entry is strictly positive,

\[
 \sum_{g,h}q_\lambda(g,h)=1,
 \qquad
 \sum_hq_\lambda(g,h)=\sum_gq_\lambda(g,h)=\frac14.       \tag{4}
\]

Equation (2) is invariant under the proper-cubic actions that transport the
oriented pair, including the eight-element unordered-pair stabilizer.  It is
a constructed downstream ansatz, not a value derived from the minimal axioms
or the parent factors.

## Guarded compound Kraus family

For one source-pair control `P_(s,t)`, one exit pair `(g,h)`, and one pair of
new outcomes `(c,d)`, the success descriptor has the structural form

\[
 K^{(\lambda)}_{s,t;g,h;c,d}
 =\sqrt{q_\lambda(g,h)}\,
   L^L_{s;g,c}\,L^R_{t;h,d}\,P_{s,t}.                    \tag{5}
\]

The displayed product is shorthand for the explicit factorization in the
runner.  `P_(s,t)` retains all ten control atoms.  Each `L` contains the
literal current identity/projector factors, preparation maps, positive root,
writer maps, spectator identities, and outside-carrier identity inherited
from the conditional Block23/24 construction.  The six unselected Blank
blocks are not dropped during contraction.

If `T(c|s)` is the exact source-derived local transition factor, the branch
Gram is

\[
 K^{(\lambda)\dagger}_{s,t;g,h;c,d}
 K^{(\lambda)}_{s,t;g,h;c,d}
 =q_\lambda(g,h)T(c\mid s)T(d\mid t)P_{s,t}.              \tag{6}
\]

Every target axis is reconstructed from all `14` literal branches, so

\[
 \sum_{g,h,c,d}
 K^{(\lambda)\dagger}_{s,t;g,h;c,d}
 K^{(\lambda)}_{s,t;g,h;c,d}
 =P_{s,t}.                                                 \tag{7}
\]

The `196` source-pair controls are orthogonal and idempotent.  With

\[
 P_{\mathrm{active}}=\sum_{s,t}P_{s,t},
 \qquad
 K_{\mathrm{STOP}}=I-P_{\mathrm{active}},                \tag{8}
\]

equations (7)--(8) give full-space trace preservation.  Tensoring every
success branch and STOP with an arbitrary untouched reference identity leaves
the same Gram identity.  Complete positivity is explicit from the Kraus
form.

The controls are rank-one on their ten pointer/Blank control atoms; the map
acts as identity on the current-live degrees of freedom.  No stronger
full-carrier rank statement is intended.

## Covariance and readable Record event

The runner transports every literal turn factor through all `24` proper cubic
frames, verifies symbolic translations of the complete carrier, transports
the ten-atom controls and output Locked words, and checks the unordered-pair
stabilizer including the side-exchanging action.  The two instruments are
therefore covariant as a family of oriented finite carriers.

Each tip has `4 x 14 = 56` possible new Locked labels.  The compound output
stores the two selected Locked blocks together with the six remaining Blank
blocks.  All `56^2 = 3,136` complete pointer configurations are distinct and
decode back to their exit/outcome labels before the event `D` is evaluated.

There are four diagonal cells in (2), so the guarded branch sum gives

\[
 \Pr_\lambda(D)=4\frac{1+3\lambda}{16}
                =\frac{1+3\lambda}{4}.                   \tag{9}
\]

Substituting (3) yields equation (1).  The difference is therefore a readable
Record statistic, not an unregistered internal label.

## Exact boundary and next discriminator

The positive terminal does not classify the complete returned-tip process-law
image.  In particular, it does not prove:

- exact singleton reduction to the parent append channel;
- closure of the reachable sectors under repeated application;
- cylinder/prefix consistency for repeated returned-pair histories;
- one state-derived eligibility and invocation rule;
- finite Blank, retry, entropy, and renewal accounting;
- a nearest-neighbor microscopic factorization;
- a normalized cadence or rate;
- a conserved directed Record source/current; or
- an action-response or gravity coupling.

The next campaign should isolate the coupling-specific layer before adding
the common clock, all-time renewal, and gravity obligations.  The exact joint
matrix has nonnegative rank one for `lambda=0` and four for `lambda=1/2`.
Therefore the first common-extension stage should classify a physical
four-valued Locked-Record cause and an exact depth-two cylinder under one
shared architecture.  Its outcome has a sharp routing meaning:

1. if both pass depth two, continue to autonomous reuse and test
   selector/source only if both survive that later stage;
2. if exactly one passes, record only a scoped depth-two consistency selector
   between these two supplied couplings, then test its reuse;
3. if neither extends through one exact local-factor obstruction, dispatch
   that factor to a targeted `M_2(C)` compiler;
4. if a proved auxiliary-state lower bound grows with event count, dispatch to
   extensive causal Record history; and
5. if the search is incomplete or times out, make no physics inference.

An immediate gravity join would be premature.  The live gravity/action branch
contains fixed-placement conditional response coefficients, not the missing
occurrence, normalized cadence, conserved Record current, or debit-continuity
law.  Those coefficients may not be reused as branch probabilities, hazards,
or rates.

## Evidence scope after correction

Current named science checks:

- `local_positive_roots_rows_and_actual_writer_deletion`
- `ten_block_geometry`
- `3136_actual_record_configurations`
- `two_q_tables_and_changed_weight`


The original Block28 numerical definitions and conditional argument are
preserved. The current entrypoint executes the checks it names, with current
source, own-note and actual input identities. Its terminal covers those
bounded checks only. It does not replay or newly certify the original long
controller, original mutation census, or historical custody/status checks.
The complete original execution output and all earlier source versions remain
in the linked recovery inventory, including any earlier failures. Mathematical
claims beyond the named fresh checks retain their displayed proof and the
explicitly historical computation; old outputs are not presented as fresh.
No formal audit verdict or physical TOE closure is asserted.
