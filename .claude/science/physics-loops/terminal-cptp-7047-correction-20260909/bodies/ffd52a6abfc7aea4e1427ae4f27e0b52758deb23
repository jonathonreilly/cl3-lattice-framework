---
claim_id: fixed_carrier_presence_separated_nondemolition_record_update_boundary_bounded_theorem_note_2026-08-20
claim_type: bounded_theorem
claim_scope: "For the exact supplied Block-7 A/B qubit instruments, the original terminal path word 000 coincides with the all-blank three-memory sector, so it cannot distinguish absence of a Record from the nonzero outcome-0 range. Reusing the existing flag qubit as an all-branch completion flag repairs that exact carrier defect with blank 000, pending 100, and terminal words 010, 110, 111. On the connected four-site Z3 path F--M1--S--M2, exact 16-by-16 unitary extensions map every blank-memory/live-system input to the repaired path isometry and reproduce all three flat Kraus blocks and central masses. The input-to-terminal-path cq channel Gamma_c has Kraus rank three and therefore needs a pure environment of dimension at least three; a two-qubit environment and explicit export realize it, while four environment codes also realize the full-carrier Q_perp/Q0/Q1/Q2 pinching of rank four. A separately supplied future update fixes the terminal logical algebra pointwise while changing live-system states, giving an exact nondemolition/permanence realization criterion. In finite dimension, no one reversible update can both carry a nonzero subspace orthogonal to the terminal sector into that sector and leave the terminal sector forward invariant; scheduled future updates, nonunitary sinks, infinite or increasing archives, and complete post-formation commutant restrictions remain live. The coherent carrier, regional pointer algebra, central restriction, framework site Record, Admissibility law, and actual terminal atom remain distinct. No axiom amendment, audit verdict, obligation retirement, or TOE percentage movement is claimed."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - fresh_ancilla_staged_cq_record_intertwiner_conditional_completion_bounded_theorem_note_2026-08-20
runner: scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20.py
---

# Fixed-Carrier Presence-Separated Nondemolition Record-Update Boundary

**Date:** 2026-08-20
**Type:** bounded theorem
**Status authority:** independent audit only. This proposal applies no verdict,
changes no axiom, and retires no obligation.

Primary runner:
[`scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20.py`](../scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20.py)

Independent runner:
[`scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_independent_check_2026_08_20.py`](../scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_independent_check_2026_08_20.py)

## 1. Result Up Front

[Block 7](FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md)
exactly solved the finite staged-to-flat cq channel problem. Its
physical Record interpretation nevertheless encounters a sharper carrier
defect before any permanence theorem can begin: the all-blank three-memory
word and the terminal outcome-0 word are both `000`.

Let

\[
 \mathcal B=|000\rangle\otimes\mathbb C^2_S,
 \qquad
 \mathcal R_0=|000\rangle\otimes\operatorname{ran}K_0.
                                                               \tag{1}
\]

The exact fixture has \(\operatorname{rank}K_0=1\), hence
\(0\ne\mathcal R_0\subset\mathcal B\). No presence projector can annihilate
every all-blank/live-system input and simultaneously certify every nonzero
outcome-0 vector. This does not damage the Block-7 channel identity; it shows
only that the word `000` cannot do double duty as physical **absence** and
formed outcome 0.

The same three memory qubits have enough unused capacity to repair the defect:

```text
blank       000
pending B   100
terminal 0  010
terminal 1  110
terminal 2  111.
```

Thus the existing `F` bit is promoted from a residual-only occupancy marker to
an all-branch **completion flag**. The old `B` prefix and both residual words
remain literal; only terminal outcome 0 moves from `000` to `010`.

For each context \(c=A,B\), the corrected coherent path isometry is

\[
 \widehat W_c|\psi\rangle=
 |010\rangle K_0|\psi\rangle+
 |110\rangle K_{c1}|\psi\rangle+
 |111\rangle K_{c2}|\psi\rangle .                    \tag{2}
\]

The runner constructs an exact \(16\times16\) unitary \(U_c\) such that

\[
 U_c\bigl(|000\rangle\otimes|\psi\rangle\bigr)
   =\widehat W_c|\psi\rangle                           \tag{3}
\]

for every live-system input. The unitary acts on one fixed connected four-site
carrier. No extra Stinespring pointer or export sink is needed for the
**coherent** form (2). Dephasing it or treating it as one actual history would
be an additional operation.

The terminal logical algebra has atoms

\[
 Q_0=|010\rangle\!\langle010|\otimes I_S,\quad
 Q_1=|110\rangle\!\langle110|\otimes I_S,\quad
 Q_2=|111\rangle\!\langle111|\otimes I_S.             \tag{4}
\]

A declared later unitary is exactly nondemolishing for this algebra when it
fixes each \(Q_j\), equivalently when it commutes with every \(Q_j\). The
runner gives a nontrivial branch-controlled example that changes the live
system while preserving every terminal content and central mass, plus a
unitary `110`/`111` swap that preserves occupancy and the terminal set but
fails pointwise permanence.

The fixture-specific boundary is finite and exact, and instantiates a prior
repository theorem rather than claiming abstract novelty. If a nonzero blank subspace
\(B\) is orthogonal to a terminal sector \(T\), no single finite-dimensional
unitary can satisfy both

\[
 U(B)\subseteq T,
 \qquad U(T)\subseteq T.                               \tag{5}
\]

Finite-dimensional unitarity turns the second inclusion into \(U(T)=T\),
while preservation of orthogonality forces \(U(B)\perp U(T)=T\), contradicting
the first inclusion. Thus an autonomous fixed-carrier **absorbing** write
cannot be obtained by simply repeating one reversible step. The exact writer's
inverse demonstrably returns its coherent written image to blank.

This is not a universal Record no-go. A scheduled switch to a different
nondemolition update succeeds conditionally; so can a nonunitary channel, an
infinite or increasing archive, a superselection/allowed-operation
restriction, a stochastic append law, or another actualization dynamics.
Those route prices are the scientific result.

## 2. Authority And Complete Resource Ledger

The load-bearing inputs are:

1. the exact Block-7 A/B post-contact Kraus programs, their common binary
   front, and their exact residual factorization;
2. ordinary finite-dimensional Hilbert-space and unitary algebra;
3. four fixed qubit sites at
   `F=(-1,0,0)`, `M1=(0,0,0)`, `S=(1,0,0)`, and `M2=(2,0,0)`, so
   `F--M1--S--M2` is a connected nearest-neighbour path in `Z3`;
4. the initial memory word `000`, the externally selected context `A` or `B`,
   and a supplied order: front interaction, completion interaction, then a
   switch to a declared future-update family;
5. exact full-domain unitary extensions on every unused or malformed carrier
   subspace; and
6. the logical terminal algebra (4) as a mathematical pointer algebra.

The exact **coherent** writer uses only those four carriers. If the terminal-
path cq output is dephased, the complete ledger additionally contains two
blank environment qubits (or another pure environment of dimension at least
three), a terminal-label copy, and an exported/sunk environment. One pure
environment qubit is insufficient.

No additional pointer or sink is hidden in (2)-(3), because the memory qubits
are the coherent pointers and nothing is traced out. Conversely, the result
does **not** claim a dephased cq output, collapse, an observed branch, a
nearest-neighbour two-qubit gate compilation, or one autonomous repeated
update. The four-site unitary is an exact connected-cluster extension. The
context, blank preparation, two-step circuit order, post-write update switch,
and apparatus are supplied. A physical formation site/rate and physical time
remain open rather than supplied by the construction.

The [current Record axiom](MINIMAL_AXIOMS_2026-06-29.md#record--fixed-reality)
says that Records form, lock one admissible local possibility, and are
permanent. It also permits **at most** one Record per site (including no
Record) and requires content-alone readout. The
same memo expressly withholds record-production and physical persistence
dynamics. It therefore constrains any successful physical carrier but does not
register (4) as a site Record or select the update family used here.

The historical context files
`docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`
and
`docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`
are source-matched warnings, not upstream retained authority: reusing a
coherent copy can erase it, and reversible access alone does not give absolute
permanence.
The current runner rebuilds the exact obstruction on the A/B fixture and
supplies the missing presence-separated control.

## 3. Exact Presence Collision And Repair

In Block 7 the terminal path projectors were attached to
`000`, `110`, and `111`. With the live system included, the nominal blank
sector is

\[
 P_{\rm blank}=|000\rangle\!\langle000|\otimes I_S.    \tag{6}
\]

The old outcome-0 projector is literally the same matrix. Worse, the exact
outcome-0 range is nonzero and sits inside that sector by (1). Suppose a
putative presence projector \(N\) satisfied

\[
 N|_{\mathcal B}=0,\qquad N|_{\mathcal R_0}=I.
\]

Every vector in \(\mathcal R_0\) would then have to be sent both to zero and
to itself. This is impossible. The argument does not depend on a probability
rule, a tolerance, or a chosen input state.

For the repaired code let

\[
 P_b=P_{000},\quad P_p=P_{100},\quad
 T=P_{010}+P_{110}+P_{111}.                            \tag{7}
\]

All five word sectors are pairwise orthogonal and \(P_bT=0\). The terminal
presence projector is \(T\), while \(P_p\) is explicitly nonterminal. The
repair uses no additional qubit. It changes the semantics of `F`: `F=1` now
means that the staged program has completed on every terminal branch, not
that a framework Record has formed.

This distinction matters. Occupancy alone does not determine content, and a
completion bit is not automatically a Record. Setwise stability of the three
terminal atoms also permits their permutation; permanence requires pointwise
fixing.

## 4. Exact Fixed-Carrier Unitary

For either binary Kraus pair \((L_0,L_1)\), the stacked map

\[
 V_L=\begin{pmatrix}L_0\\L_1\end{pmatrix}:
 \mathbb C^2\longrightarrow\mathbb C^2_P\otimes\mathbb C^2_S
                                                               \tag{8}
\]

is an isometry. Complete its two columns by exact Gram--Schmidt in the
orthogonal complement to obtain a four-by-four unitary \(\widetilde U_L\)
whose action on a blank pointer is \(V_L\). The runner performs this completion
symbolically for the common front and both A/B residual pairs and checks
\(\widetilde U_L^\dagger\widetilde U_L=I\) exactly.

Embed the front completion on `M1,S` and leave `F,M2` fixed. Acting on blank
memory it gives

\[
 |000\rangle K_0|\psi\rangle+|100\rangle B|\psi\rangle,             \tag{9}
\]

so the continuation branch has the exact pending word `100`.

Let \(\widetilde U_{J_c}\) be the residual completion on `M2,S`. Define the
four-site completion step, in logical order `M1,F,M2,S`, by

\[
 C_c=
 |0\rangle\!\langle0|_{M_1}\otimes X_F\otimes I_{M_2S}
 +|1\rangle\!\langle1|_{M_1}\otimes X_F\otimes
       \widetilde U_{J_c}.                            \tag{10}
\]

The two summands have orthogonal controls, so \(C_c\) is unitary. With
\(U_c=C_c\widetilde U_{\rm front}\), equations (2)-(3) follow exactly because

\[
 J_{c1}B=K_{c1},\qquad J_{c2}B=K_{c2}.                \tag{11}
\]

The runner verifies every matrix entry, both contexts, and arbitrary live
inputs through the two-column operator identity. This is stronger than a
state-specific numerical preparation check.

The exact geometry is a connected four-site path. Equation (10) is a
connected-cluster unitary, not a displayed decomposition into pairwise
nearest-neighbour gates. General compilation is not used as hidden evidence.
More importantly, even a successful pair-gate compilation would retain the
supplied schedule and would not evade the reversible absorbing-sector theorem
in Section 7.

## 5. Terminal Center And The Unchanged cq Channel

The repaired path decoder is

\[
 d(010)=0,\qquad d(110)=1,qquad d(111)=2.             \tag{12}
\]

Therefore restricting \(\widehat W_c\rho\widehat W_c^\dagger\) to the
commutative algebra generated by (4) gives

\[
 \operatorname{Tr}\!\left(
 Q_j\widehat W_c\rho\widehat W_c^\dagger\right)
 =\operatorname{Tr}(K_{cj}\rho K_{cj}^\dagger).       \tag{13}
\]

Dephasing between the three word sectors gives the same flat cq blocks as
Block 7. At \(\rho_*=\operatorname{diag}(3/5,2/5)\), the exact masses remain

```text
A: (3/10, 19/50, 8/25)
B: (3/10,  7/20, 7/20).
```

Presence repair does not change the channel or insert branch probabilities.
It also does not make the coherent state one terminal atom. Dephasing is a
channel operation, not a sampler, and restriction to a commutative algebra is
not actual-member selection.

The three branch operators

\[
 A_{cj}=|t_j\rangle K_{cj}:\mathbb C^2_S
       \longrightarrow\mathbb C^8_M\otimes\mathbb C^2_S
\]

are nonzero and have mutually orthogonal memory ranges. They are therefore
linearly independent, so the exact input-to-terminal-path channel

\[
 \Gamma_c(\rho)=\sum_{j=0}^2 A_{cj}\rho A_{cj}^\dagger
\]

has Kraus/Choi rank three. A pure Stinespring environment for \(\Gamma_c\)
must have dimension at least three. The runner constructs a full permutation
that assigns four distinct two-qubit environment codes to
\(Q_\perp,Q_0,Q_1,Q_2\). Tracing that environment realizes the full-carrier
four-atom pinching map, of Kraus rank four; restricted to the terminal path
output it gives \(\Gamma_c\)'s exact three-sector dephasing. The primary and
independent checks use four Hermitian inputs spanning \(M_2\), including the
Y-direction input, for both contexts. Thus one pure environment qubit is
insufficient for \(\Gamma_c\), while two qubit sites suffice for it and for
the stronger four-atom full-carrier pinching. This does not exclude a mixed
environment, classical randomization, approximation, or a restricted input
family. The export sink remains mandatory for the cq claim and still does not
select an atom.

## 6. Nondemolition And Permanence Criterion

Let

\[
 \mathcal Z_T=\operatorname{span}\{Q_0,Q_1,Q_2\}
\]

in the terminal corner, or adjoin \(Q_\perp=I-T\) for a unital full-carrier
algebra. For any declared post-formation unitary \(V\), the following are
equivalent for each terminal atom:

\[
 V^\dagger Q_jV=Q_j
 \quad\Longleftrightarrow\quad
 [V,Q_j]=0.                                           \tag{14}
\]

Thus exact all-state content permanence for an arbitrary finite sequence of
declared later steps follows when every step lies in \(\mathcal Z_T'\). Such a
step can have the form

\[
 V=\sum_{j=0}^2 |t_j\rangle\!\langle t_j|\otimes V_j
       \oplus V_\perp,                                \tag{15}
\]

so the live system need not freeze. The runner uses different exact Pauli or
Hadamard updates in the three sectors and verifies that all four tomographic
inputs retain every label mass.

For a declared CPTP update \(\Lambda\), the representation-independent
condition is

\[
 \Lambda^\dagger(Q_j)=Q_j\qquad(j=0,1,2).             \tag{16}
\]

For the complete partition including \(Q_\perp\), these fixed projections lie
in the multiplicative domain of the unital Heisenberg map. Equivalently, the
map is bimodular over the declared logical algebra and admits a block-
preserving Kraus representation. For continuous unitary flow the corresponding
condition is \([H,Q_j]=0\); a Markov generator must satisfy
\(\mathcal L^\dagger(Q_j)=0\).

The quantifier matters. A globally noncommuting update can agree with a QND
map on a restricted reachable corner. Equation (14) is an all-state statement
for the declared logical projectors, not a necessity theorem for every
microscopic representation.

Setwise invariance

\[
 V^\dagger\mathcal Z_TV=\mathcal Z_T
\]

is too weak: it allows a permutation of terminal contents. The exact hostile
swaps `110` and `111`. It keeps the terminal set and completion occupancy but
fails (14). Conversely, rotations on unused words pass logical stability even
though they do not preserve the full raw eight-word diagonal algebra. The
right object is the declared terminal logical algebra, not every computational
bit projector.

Equation (14) is a **realization criterion** for the permanence already named
by Record. It does not prove that (4) is a framework Record, select the future
update family, or form any atom. The identity and environment-blind commuting
updates satisfy (14) while writing nothing.

## 7. Finite Reversible Absorption Boundary

Let \(\mathcal H\) be finite-dimensional, let \(B,T\subset\mathcal H\) be
nonzero orthogonal subspaces, and let \(U\) be unitary. Suppose a repeated
fixed-carrier update is asked both to form a terminal code and preserve it:

\[
 U(B)\subseteq T,\qquad U(T)\subseteq T.              \tag{17}
\]

Since \(U|_T\) is injective and \(T\) is finite-dimensional,
\(\dim U(T)=\dim T\); hence the second inclusion gives \(U(T)=T\). Since
\(B\perp T\) and \(U\) preserves inner products,
\(U(B)\perp U(T)=T\). The first inclusion then forces \(U(B)=\{0\}\), contrary
to unitarity and \(B\ne0\). This proves the bounded theorem.

For the repaired fixture, \(\dim B=2\), \(\dim T=6\), and the exact writer
does satisfy \(U_c(B)\subset T\). It therefore cannot also preserve all of
\(T\). The runner verifies that it does not, and verifies directly that

\[
 U_c^\dagger\widehat W_c=|000\rangle\otimes I_S.      \tag{18}
\]

If the inverse is an allowed later update, the coherent write is erasable.
Applying either exact A/B writer a second time sends its entire two-dimensional
written image into the terminal complement, with unit leak Gram. Thus the
failure is visible without choosing an arbitrary hostile unitary: host-blind
double use of the writer itself violates permanence.

The conclusion is deliberately narrow:

> A nonzero disjoint blank-to-terminal transition cannot be an absorbing
> transition of the same finite-dimensional reversible update.

It does **not** exclude:

- one write unitary followed by a different QND future update;
- a finite nonunitary CPTP append/reset channel with an explicit environment;
- an infinite bilateral-shift archive or an ever-growing fresh archive;
- a superselection or allowed-operation restriction under which **every**
  physically allowed post-formation operation fixes, equivalently commutes
  with, each terminal atom \(Q_j\) (merely excluding the writer inverse is
  insufficient because a terminal-label swap also violates permanence);
- an append-only stochastic Record-configuration law;
- objective-collapse, hidden-variable, branching-relative, or other
  actualization mechanisms; or
- access-relative rather than absolute permanence.

Those are live constructive routes, not rhetorical footnotes.

Two escape witnesses are explicit. On a two-level blank/terminal toy carrier,

\[
 L_0=|1\rangle\!\langle0|,\qquad
 L_1=|1\rangle\!\langle1|                              \tag{19}
\]

define a trace-preserving two-Kraus channel that maps blank to terminal and
fixes terminal. It is finite and absorbing because it is irreversible. On
\(\ell^2(\mathbb Z)\), the bilateral shift
\(S|n\rangle=|n+1\rangle\), with
\(B=\operatorname{span}\{|0\rangle\}\) and
\(T=\overline{\operatorname{span}}\{|n\rangle:n\ge1\}\), is unitary and obeys
\(S(B)\subset T\), \(S(T)\subset T\). It evades exactly the finite-dimension
step. The runner checks (19); the infinite shift is an elementary basis proof.

## 8. Regional Pointer Algebra Versus Framework Record

The repaired terminal words provide a faithful **regional pointer algebra**
with an empty sector. That is materially closer to Record typing than the old
collision, but it is not a framework site Record. A retained bridge must still
specify:

1. which site or sites carry the Record and how each \(Q_j\) maps to admissible
   local `M2(C)` possibilities;
2. whether the code is one distributed logical Record or a configuration of
   several site-local Records;
3. how blank/no-Record and value-zero semantics are represented at each site;
4. at-most-one-Record-per-site consistency, including lawful no-Record sites;
5. a readout that factors through Record content alone; and
6. admissibility of each locked possibility under the actual nearest-neighbour
   condition.

The completion flag certifies execution in the supplied circuit. It cannot by
itself distinguish the three contents, register a formation event, or prove
content-alone readability. The live system remains part of the cq payload and
must not become a hidden second readout input.

If \(\iota\) is established as a **single-site event map**, or if a separate
retained joint-regional Admissibility law is supplied, the probability-law
datum would be

\[
 \mu_{\rm Adm}\!\left(\iota(Q_j)\mid
       \text{neighbours, formation}\right)
 =\operatorname{Tr}\!\left[
       Q_j\widehat W_c\rho\widehat W_c^\dagger\right]. \tag{20}
\]

Equation (20) is therefore a typed target, not an available equality. The
current per-site Admissibility distribution does not by itself assign a
probability to a distributed regional atom \(\iota(Q_j)\). This is the same
**central-restriction compatibility** isolated in Block 7, with an additional
single-site-event or joint-regional-law typing obligation made explicit.
Nondemolition can preserve an equality already established by (20); it cannot
establish its initial physical truth. A support-identical Admissibility law
with different weights remains compatible with the pointer algebra and its
permanence criterion.

Finally, neither (2), dephasing, (14), nor (20) supplies the separate
**actual-member correlation** between one formed Record atom and the
pointwise realized history. The
[realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md#the-primitive)
names the target type but provides no selection rule.

The exact dynamics-side interface exposed by this block is a checklist, not a
standalone physical law:

> **Carrier registration and post-formation compatibility.** Conditional on
> the existing Record axiom, a declared empty/terminal logical algebra is a
> candidate physical carrier only after the carrier sites and their local
> typing are specified; no-Record is distinguished from recorded value zero
> at every site; the typing obeys at most one Record per site (or explicitly
> declares one distributed Record); blank and pending sectors yield no content
> readout; every terminal readout factors through carrier content alone;
> every terminal value is admissible under the actual local condition; each
> selective branch of a declared formation instrument lands in one terminal
> atom; and the complete physically allowed future update law fixes that atom.

The selective-branch clause types the target of each instrument branch. It
does not assert that one branch is realized; the nonselective coherent or cq
state can still contain all three terminal sectors.

This is sufficient interface wording only for the carrier-registration and
post-formation-compatibility claim, not for central compatibility, actuality,
or a complete theory. It is not a demonstrated necessary/minimal new axiom.
The current Record axiom already states formation and permanence abstractly.
Microscopic carrier registration, a nonunitary or increasing-archive law, and
an admissible-update restriction are still live downstream derivation routes.
No axiom amendment is justified or authorized here.

## 9. No-Go Discipline Gate

The no-go discipline covers every negative statement in this note, not only
Section 7. The complete negative-claim inventory is:

| ID | exact negative target | resolution and surviving route |
|---|---|---|
| `C_P` | on the old exact code, no projector can annihilate the full blank sector and certify the nonzero outcome-0 range | direct inclusion `R_0 subset B`; the repaired `010` code succeeds, so no general presence no-go ships |
| `C_E` | no **pure** one-qubit environment realizes the exact input-to-terminal-path channel `Gamma_c` | its Choi rank is three; a qutrit is minimal and the displayed two-qubit environment succeeds; mixed, randomized, approximate, and restricted-input routes remain live |
| `C_Q` | terminal-set/occupancy invariance does not imply pointwise content permanence | the exact `110`/`111` swap is a counterexample; the atomwise commutant criterion succeeds |
| `C_A` | one **single finite-dimensional reversible update** cannot map a nonzero subspace disjoint from the terminal sector into that sector while leaving the terminal sector forward invariant | equation (17); scheduled, irreversible, infinite, restricted-operation, and stochastic routes survive |

Universal measurement or Record impossibility, failure of local instruments,
failure of infinite archives, impossibility with a mixed environment, axiom
necessity, and TOE closure are `FAIL / DO NOT SHIP`.

### N1 — Alternative-route enumeration

For `C_A`, the alternatives are normalized by physical mechanism rather than
by wording variants:

| normalized route family | exact attempt and outcome | direct locator / status | marker |
|---|---|---|---|
| direct repeated finite writer | both exact repaired `U_c` form from blank, but a second use sends the **entire** written two-dimensional image into `T_perp` with unit leak Gram; each inverse erases the coherent image | equations (2), (18); primary and independent executable | **ATTEMPTED** |
| terminal-commutant/QND-first unitary | the exact nontrivial future family fixes every `Q_j`, but then `P_T U P_B=0` for disjoint blank | equations (14)-(17); primary and independent executable | **ATTEMPTED** |
| fresh-environment reachable-corner dilation | the four-code copy realizes the channel from a blank environment corner, but repetition needs explicit export/reblanking and is not one closed same update | Section 5; primary and independent executable | **ATTEMPTED** |
| scheduled reversible write/future pair | `U_c` writes, then a distinct terminal-commutant unitary preserves every atom | Section 6; primary and independent executable; physical switch remains supplied | **ATTEMPTED** |
| finite irreversible instrument | the exact two-Kraus reset (19) maps disjoint blank to terminal and fixes terminal | Section 7; primary and independent executable | **ATTEMPTED** |
| finite program/clock/catalytic enlargement | enlarge the carrier by any finite stage/fuel register and repeat one closed unitary | equation (17) applies to the enlarged finite `B,T`; a globally absorbing terminal sector still cannot receive its disjoint blank | **ATTEMPTED** |
| infinite/increasing archive | the explicit bilateral shift on `ell^2(Z)` has a proper forward-invariant terminal half-space | equation (19) discussion and prior infinite-QCA context; exact basis construction | **ATTEMPTED** |

The runner's `n1_route` resolution lines authenticate the five current
executable mechanisms; the two analytic routes have direct proofs. For the
other inventory targets, the repaired code is the positive `C_P` route, the
qutrit/two-qubit dilation is the positive `C_E` route, and the atomwise
commutant is the positive `C_Q` route. None supports a broader no-go.

### N2 — Wall-Independence Audit

The exact theorem has four load-bearing walls:

- `W_F`: the carrier and terminal sector are finite-dimensional;
- `W_R`: the repeated update is reversible/unitary; and
- `W_S`: the same update both writes from blank and must preserve the terminal
  sector, rather than a scheduled write/future pair; and
- `W_D`: the nonzero blank and terminal sectors are disjoint (orthogonal), as
  required for presence to differ from an already recorded value.

Each wall can be relaxed while retaining the other three:

| relaxed wall | exact counterroute with the other three retained | price |
|---|---|---|
| `W_F` | bilateral shift with disjoint `B=span{|0>}` and `T=span{|n>:n>=1}` | infinite no-return capacity |
| `W_R` | finite two-Kraus reset with disjoint blank/terminal sectors | irreversible channel/export |
| `W_S` | finite unitary `U_write` followed by a distinct finite unitary `U_QND` | physical stage/switch law |
| `W_D` | finite identity update with `B=T` | destroys the no-Record/recorded-value distinction |

| pair | relaxing first while keeping second | relaxing second while keeping first | independent? |
|---|---|---|---:|
| `W_F`, `W_R` | an infinite bilateral shift is unitary and has a forward-invariant terminal half-space | a finite irreversible append channel has an absorbing terminal sector | yes |
| `W_F`, `W_S` | one infinite shift can both enter and preserve the half-space | finite scheduled `U_write` then `U_QND` succeeds | yes |
| `W_F`, `W_D` | the infinite shift keeps blank and terminal disjoint | finite `B=T`, `U=I` removes disjointness | yes |
| `W_R`, `W_S` | one finite nonunitary append channel can absorb | finite reversible scheduled write/future updates succeed | yes |
| `W_R`, `W_D` | the finite reset keeps blank and terminal disjoint | finite `B=T`, `U=I` remains reversible | yes |
| `W_S`, `W_D` | the finite scheduled pair keeps blank and terminal disjoint | finite `B=T`, `U=I` uses one update | yes |

Thus disjointness is an explicit theorem premise and an independently
relaxable wall. Its relaxation is mathematically a counterroute but physically
recovers the old `000` collision and loses Record-presence certification.

`U(T) subset T` is a full-sector/all-state condition. The theorem does not
silently replace it by a handpicked reachable-corner test. If a separately
defined nonzero reachable subspace `R subset T` is disjoint from `B`, receives
`U(B)`, and is itself forward invariant under the same finite unitary, the same
proof applies with `R` in place of `T`. A finite-duration or scheduled-corner
claim is weaker and remains outside the theorem. For this exact fixture the
double-use executable proves the stronger immediate fact
`T U_c W_hat_c=0` and unit leak Gram for both contexts.

### N3 — Hidden-Wall Scan

The phrase scan covers “we assume,” “by construction,” “as is standard,” “the
framework provides,” “background,” “naturally,” “obviously,” “standard QFT,”
“bridge context,” “registered,” and “canonical.” The exact programs, context,
memory blank, connected carrier, unitary extensions, two-step order, future-
update switch, logical algebra, and finite-dimensional quantifier are
declared. “Context” denotes either the externally selected A/B menu or a
historical-source context; it never supplies a physical bridge. “Registered”
occurs only in the N5 negation that the regional code is **not** silently
registered, and the retained-bridge wording names an open target. “Canonical”
does not occur as load-bearing evidence. The unitary extension is a
mathematical existence/construction, not a framework-selected law.

The optional dephasing environment and sink are explicit; no reset stream is
hidden. No global clock, pair-gate compiler, physical formation site/rate or
time, sampler, collapse, Admissibility values, site-Record map, or actual atom
is supplied by the construction. “Completion flag” means circuit completion
only.

### N4 — Per-Citation Residual Matching

| cited witness (path, line) | residual there | residual used here | match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:55-90,116-145,161-170` | local distribution and abstract fixed Records; dynamics, central sectors, and physical persistence withheld | authority boundary for carrier registration, update selection, central compatibility, and time | yes — current axiom authority only |
| `docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md:27-97,186-219` | exact `000/110/111` cq path and explicit non-Record flag boundary | presence collision, corrected code, and unchanged cq decoder | yes — exact proposal fixture, locally recomputed |
| `docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md:65-121` | all-state QND condition plus same-fragment reuse erasure | exact logical-algebra QND criterion and fresh/scheduled escape | yes — historical unaudited warning, theorem reproved |
| `docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md:161-182` | reversible CNOT access does not yield absolute permanence | finite reversible absorbing-sector boundary and named escapes | yes — historical unaudited route map, theorem reproved |
| `docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md:149-179` | exact finite same-carrier formation/permanence obstruction and environment/infinite escapes | abstract theorem provenance; current A/B fixture instantiation only | yes — historical proposal context, not upstream authority |
| `docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md:54-177,299-347` | exact infinite reversible export steelman, finite recurrence boundary, inverse/collision/blank-tape residuals | strongest positive infinite escape and its resource price | yes — authority-free context, not a retained dependency |

No cited row supplies the physical carrier registration, future update family,
central law, or actual member.

### N5 — Resolution And Rhetoric

The primary runner emits these exact resolution lines:

```text
per_element: checked — blank 000, pending 100, corrected outcome-0 word 010, residual words 110/111, Kraus blocks, and terminal projectors remain separately typed
per_site: checked — the fixed F--M1--S--M2 path is a connected four-site Z3 carrier, while its regional logical code is not silently registered as one framework site Record
per_mode: checked — coherent unitary write, terminal-center restriction, optional dephasing, QND future update, Admissibility distribution, and actual terminal atom remain distinct
per_block: checked — exact A/B front and residual unitaries compose from blank through pending to the presence-separated terminal code and reproduce every flat Kraus block
lattice_wide: checked and not executed — the finite scheduled carrier exposes the reversible absorption wall; increasing archives, nonunitary sinks, overlap arbitration, and physical time remain open
```

It also emits one certificate line for each executable normalized N1 route:

```text
n1_route: direct_repeated_finite_writer — executed for A and B; first use maps the full blank input into T, while second use maps the entire written image into T_perp with unit leak Gram
n1_route: terminal_commutant_qnd_first — executed; the nontrivial future unitary fixes every Q_j and therefore has zero disjoint blank-to-terminal formation block
n1_route: fresh_environment_reachable_corner — executed; four environment codes realize Q_perp/Q0/Q1/Q2 pinching from a blank corner, with export and reblanking explicit
n1_route: scheduled_write_future_pair — executed for A and B; U_c forms the terminal path and a distinct terminal-commutant unitary preserves every terminal atom
n1_route: finite_irreversible_instrument — executed; the two-Kraus reset maps a disjoint blank atom into an absorbing terminal atom while violating reversibility
```

`C_A` is always qualified by “single,” “finite-dimensional,” “reversible,”
“same update,” “disjoint blank,” and “forward-invariant terminal sector.”
`C_P` is old-code-specific, `C_E` is exact-channel/pure-environment-specific,
and `C_Q` rejects only the implication from setwise to atomwise permanence.
Universal impossibility and axiom necessity are `FAIL / DO NOT SHIP`.

### N6 — Partial-Closure Path Scan

| route | positive closure now | exact residual |
|---|---|---|
| presence code | blank, pending, and every terminal outcome are orthogonal on the same three memories | regional code is not a site Record |
| fixed carrier | exact four-site A/B unitaries reproduce every flat Kraus block | context, blank preparation, and circuit order/switch are supplied; physical formation site/rate/time are open |
| exact cq export | terminal-path Kraus rank three and full-carrier pinching rank four are realized with two pure-environment qubits | export/sink is explicit and produces no actual atom |
| terminal logical algebra | exact pointwise QND criterion and nontrivial stable future family | physical future-update law is supplied |
| central restriction | exact Block-7 A/B masses survive re-encoding and QND future updates | equality with Admissibility is underived |
| finite reversible boundary | exact reason one repeated fixed unitary cannot be absorbing | scheduled, irreversible, infinite, restricted-operation, and stochastic routes survive |
| Record semantics | presence collision is removed and required registration fields are enumerated | site map, content-only readout, formation event, and actual member remain open |

The partial closures sharpen a dynamics/registration target; they do not force
an axiom amendment.

### N7 — Strongest Steelman

The strongest counterroute, already explored in the prior authority-free
infinite-QCA cycle, is an autonomous local dynamics on an increasing archive.
A fixed translation-covariant unitary can shift completed information
outward into fresh sites, leaving an increasing commutative history algebra
whose already-written atoms are never revisited by the local future light
cone. An explicit irreversible local instrument or a superselection rule can
achieve the same operational end on a finite observed subsystem. Neither route
is excluded by Section 7.

The strongest case against new axiom text is that Record already declares
formation and permanence. A microscopic theory may register the regional
pointer algebra, derive the allowed future-update restriction, and prove
central compatibility as consequences of its local law. The strongest case
for an explicit interface is only conditional: if no such law is supplied,
“permanent” has no operator-level realization criterion and the same fixed
carrier admits exact erasing updates. This block names the criterion but does
not establish necessity or owner-approved wording.

### N8 — Cross-Cycle Echo

The June pointer-conservation cycle already found that reusing one coherent
fragment can erase its imprint. The July extensional-rule cycle found that a
reversible CNOT or QCA requires a future-invariant algebra, increasing archive,
or allowed-operation restriction. The July context file
`docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md`
already proved the exact finite same-carrier invariant-subspace theorem and
the formation/leakage Frobenius-norm identity. The authority-free
`docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md`
already stated the finite invariant-subspace obstruction and exhibited the
infinite-shift escape, while retaining blank-tape, no-return, inverse-precursor,
collision, renewal, and actuality residuals. The separate authority-free
`docs/work_history/repo/review_feedback/DYNAMIC_RECORD_BOUNDARY_INDEX_QCA_STEELMAN_NOTE_2026-07-14.md`
also preserved an infinite no-return/index route but did not retain a theorem
or supply occurrence, metric rate, finite recurrence removal, or actuality.
Block 7 then separated its occupancy flag from Record formation.

Accordingly, this block does **not** claim the abstract finite obstruction as
new and does not count these repeated warnings as independent walls. Its new
work is fixture-specific: it exposes the exact blank/outcome-0 collision,
repairs the carrier code without changing the cq channel, gives the exact
four-site writer and rank-three export ledger, and instantiates the old
finite boundary on the repaired A/B carrier at full subspace resolution.

**No-Go Discipline Gate Status: PASS.** This status applies only to the four
bounded targets `C_P`, `C_E`, `C_Q`, and `C_A` under their stated quantifiers.
Every universal widening, axiom-necessity claim, and TOE-closure claim remains
`FAIL / DO NOT SHIP`.

## 10. Axiom And TOE Decision

No axiom amendment is mature. The Record axiom already supplies abstract
formation, one-value locking, permanence, and content-only readout. What is
missing is a retained dynamics/carrier bridge or a physical law that:

```text
registers empty and terminal logical sectors as site Record semantics
  -> enters exactly one admissible content sector at formation
  -> restricts every later physical update to fix that content
  -> identifies the predictive state on that center with Admissibility
  -> separately correlates the formed atom with realized history.
```

The first three lines may be derivable through an irreversible or increasing-
archive local dynamics. The fourth is central-restriction compatibility. The
fifth remains the actual-member seam. Bundling them into one axiom would hide
their independence.

Audit status: none.
Retained status: none.
Obligation retirement: zero.
TOE percentage movement: zero.

The frozen lane map remains:

| lane | repo science | physical M2 bridge | autonomous closure | evidence ceiling |
|---|---:|---:|---:|---:|
| operational quantum / Records | 95% | 92% | 50% | 99% |
| causal / time | 76% | 72% | 41% | 99% |
| inertia / matter | 95% | 96% | 75% | 99% |
| gravity / source / resources | 70% | 45% | 29% | 94% |
| Born / probability / realized history | 84% | 63% | 34% | 99% |

Science significance without score inflation:

1. the Block-7 path is upgraded from a label channel to a carrier with an
   exact empty/terminal distinction;
2. the repaired coherent writer is one exact fixed-carrier unitary, while the
   separately claimed dephased cq channel has a sharp two-environment-qubit
   resource ledger and explicit export sink;
3. logical-algebra permanence is characterized exactly and distinguished from
   occupancy, setwise stability, and total dynamical freezing;
4. the fixed-carrier autonomous route now has a proved failure mechanism, not
   a vague “needs irreversibility” slogan; and
5. the next positive route is localized to an increasing archive or explicit
   irreversible local instrument plus site-Record registration, followed by
   central compatibility and, separately, actual-history correlation.

The next portfolio test should compare those two surviving physical routes.
Kill any route that hides fresh capacity, an environment sink, a clock/switch,
the site-Record map, or a sampler. Re-run the five-role panel before calling
either route a closure or proposing axiom text.

## 11. Verification

```text
python3 -m py_compile scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20.py
python3 scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20.py
python3 -m py_compile scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_independent_check_2026_08_20.py
python3 scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_independent_check_2026_08_20.py
```

The executables are evidence for a proposal only. Independent audit controls
retention.
