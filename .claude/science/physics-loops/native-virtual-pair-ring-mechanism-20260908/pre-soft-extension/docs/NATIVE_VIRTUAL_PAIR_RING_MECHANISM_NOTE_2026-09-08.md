---
claim_id: native_virtual_pair_ring_mechanism_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied finite native low-charge H=UD+g sum lambda_e A_e: exact fourth-order ring/scalar coefficients with orientation and winding factors, constant sixth-order diagonal for uniform magnitudes, and a one-sided finite-volume fourth-order spectral error bound a^6/U^5 when a=|g|sum|lambda_e|<=U/4. No sixth-order off-diagonal calculation, RK-point selection, thermodynamic estimate or electromagnetic identification."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/native_virtual_pair_ring_mechanism_2026_09_08.py
---

# Rings induced by virtual native pairs

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

Virtual pair fluctuations of a supplied native edge perturbation generate an ice ring term at fourth order. Its native signs differ from a bare edge-flip perturbation. The accompanying diagonal is constant through sixth order for uniform coupling magnitudes, so this calculation does not generate the matching RK flippability potential at either order. A separate finite-volume estimate bounds the fourth-order spectral approximation.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite coefficients and bound under supplied Hamiltonian and domain."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Supplied model and native convention

Use the [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), based on the [native instrument algebra](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). These are provisional mathematical dependencies. Fix a periodic cubic graph with all extents even and at least four, full edge carrier, relaxed magnetic-cycle constraint and no fixed winding sector. Let

\[
x_e=(1-Z_e)/2,\quad \epsilon_v=(-1)^{v_1+v_2+v_3},\quad
G_v=\sum_{e\ni v}x_e-3,\quad Q_v=\epsilon_vG_v,\quad D=\sum_vQ_v^2.
\]

Restrict to $|Q_v|\le1$. Write $P$ for the complete ice space $D=0$ and $Q=I-P$ for its complement; this unindexed projector is distinct from $Q_v$. With sorted edge orientation, native Hermitian $A_e$ flips its own edge and distinct generators anticommute precisely when their edges meet. The supplied perturbation is

\[
H(g)=H_0+gV,\qquad H_0=UD,\qquad
V=\sum_e\lambda_e P_{\rm low}A_eP_{\rm low},\qquad U>0,
\]

with fixed real $\lambda_e$ and real strength $g$. Neither this perturbation nor its low-charge penalty is selected by the axioms. Original number-preserving $T$ dynamics is not being substituted for $A$. All intermediate low-support checks and native phases below refer to this actual model.

## Schur reduction and fourth-order normalization

The $Q$ spectrum of $H_0$ starts at $2U$. Since $PVP=0$, eliminating the $Q$ component of an eigenvector gives, whenever the finite inverse exists,

\[
Ep=-g^2PVQ\,[Q(H_0+gV-E)Q]^{-1}QVPp.
\]

Put $R=QH_0^{-1}Q$ and $C=\sum_e\lambda_e^2$. Every single edge flip from ice is low-admissible and creates $D=2$. A two-step ice return repeats that edge, so

\[
PVRVP=\frac{C}{2U}P,\qquad PVR^2VP=\frac{C}{4U^2}P.
\]

Every ice string has $3N/2$ occupied edges, where $N$ is the number of vertices. Each perturbation changes occupied-bit parity. Thus every odd-$V$ word from $P$ to $P$ vanishes, even with intervening $R,Q$ or resolvent powers. Expanding the exact inverse and substituting $E=-g^2C/(2U)+O(g^4)$ yields

\[
H_2=-\frac{C}{2U}P,\qquad
H_4=-PVRVRVRVP+\frac{C^2}{8U^3}P.
\]

The last term is the folded/reducible contribution. Both second-order normalization operators are scalar on $P$, so orthonormalization gives the same fourth-order coefficient. At fixed finite volume the next retained-order error is $O(g^6)$, without a volume-uniform claim; an explicit separate bound appears below.

## Fourth-order diagonal and ring coefficient

A four-step diagonal return uses one edge four times or two edges twice. One edge repeated has an intermediate ice return removed by $R$, leaving only $\lambda_e^4/(8U^3)$ from the folded term. For disjoint edges $e,f$, the four irreducible words have positive amplitude and denominators $2U,4U,2U$. Their sum $-\lambda_e^2\lambda_f^2/(4U^3)$ cancels the folded cross term.

For incident edges with equal initial bits, the second distinct flip violates $|G|\le1$, so all four irreducible words are refused. With opposite initial bits, all four are allowed with denominators $2U,2U,2U$ and amplitudes $-1,+1,+1,-1$. They cancel by native anticommutation. Therefore the entire diagonal is the scalar

\[
H_{4,\rm diag}=\frac1{U^3}\left[
\frac18\sum_e\lambda_e^4+
\frac14\sum_{\{e,f\}\text{ incident}}\lambda_e^2\lambda_f^2
\right]P.
\]

The incident-pair sum is unordered. For uniform $|\lambda_e|=\lambda$, it equals $33N\lambda^4/(8U^3)$. Projected generators were not assumed globally to anticommute: the cancellation is used only where both projected paths are admissible.

A nontrivial four-toggle ice return is an alternating simple four-cycle. Four distinct changed edges must balance their increments at each vertex; on this simple bipartite graph that forces such a cycle. All 24 orders are low-admissible. After the first and third flips $D=2$; after the second it is two for adjacent edges and four for opposite edges. No intermediate state is ice, so the folded term has no off-diagonal contribution.

Relative to the cyclic product of canonically oriented generators, the 16 adjacent-first orders have eight signs of each kind and cancel with denominator $8U^3$. The eight opposite-first orders all have negative relative sign and denominator $16U^3$. Including the Schur minus gives a coefficient $+1/(2U^3)$ multiplying that cyclic product.

For $C=(v_0,v_1,v_2,v_3,v_0)$ define

\[
\eta_C=\prod_{a=0}^3\operatorname{sign}(v_{a+1}-v_a),\qquad
S_C=i^4 A_{v_0v_1}A_{v_1v_2}A_{v_2v_3}A_{v_3v_0}.
\]

Then $S_C$ is $\eta_C$ times the canonical cyclic product, and

\[
H_{4,\rm off}=\sum_{C\text{ unoriented simple four-cycle}}
\frac{\eta_C\prod_{e\in C}\lambda_e}{2U^3}\,F_CS_C.
\]

Each cycle is counted once. $F_C$ projects onto its alternating support on ice. Reversal and cyclic reindexing leave the expression unchanged. Lexicographically labeled elementary plaquettes have $\eta_C=+1$, including seams. Straight winding four-cycles at extent four have $\eta_C=-1$ and contribute at this same order. They cannot be dropped from the finite effective operator. If all extents exceed four, only elementary plaquettes have length four.

Replacing native $A$ by bare $X$ is a different model: its 24 positive amplitudes give $-5\prod\lambda_e/(2U^3)$. Its incident-pair diagonal is $\pm\lambda_e^2\lambda_f^2/(4U^3)$ for equal/opposite bits; at uniform magnitude it sums to $-3N\lambda^4/(8U^3)$, also different from the native result.

For positive canonical $\lambda_e$, the elementary native coefficient is positive relative to the fixed $S_p$, while positive-$J$ RK dynamics uses $-JF_pS_p$. This is not a basis-invariant sign obstruction. A product of physical $Z_e$ flips individual $A_e$ signs, preserves $H_0$ and correspondingly changes cycle signs. For even periods, the coordinate-edge assignment $\sigma_x=(-1)^{y+z}$, $\sigma_y=(-1)^z$, $\sigma_z=1$ has product $-1$ around every elementary plaquette and can be supplied as a coupling sign pattern. No pattern is physically selected here.

Even with the negative ring convention, the scalar diagonal is not $J\sum_pF_p$. The actual four L4 ice backgrounds below have 96, 92, 89 and 86 alternating plaquettes, so this missing potential cannot be absorbed in a scalar. The calculation supplies a leading kinetic-ring mechanism, not the RK equality of its two coefficients.

## Sixth-order diagonal: fixed effective basis

For this section fix the canonical direct-rotation effective Hamiltonian. Let $P(\boldsymbol g)$ be the low spectral projection for independently variable edge couplings, $Q(\boldsymbol g)=I-P(\boldsymbol g)$ and

\[
W(\boldsymbol g)=\big[P(\boldsymbol g)P+Q(\boldsymbol g)Q\big]
\big[I-(P(\boldsymbol g)-P)^2\big]^{-1/2},\qquad
H_{\rm eff}=PW^\dagger HW P.
\]

For a sufficiently small neighborhood at each fixed finite graph, the gapped Riesz projection and inverse square root are analytic and this unitary maps $P$ onto $P(\boldsymbol g)$. An arbitrary additional coupling-dependent unitary within $P$ can change later diagonals; the coefficient here uses this stated convention.

Conjugation by $Z_e$ changes only the sign of its coupling and conjugates $P(\boldsymbol g),W,H_{\rm eff}$ covariantly. Every diagonal matrix element is therefore even in each individual coupling. A degree-six diagonal monomial uses at most three edges, with multiplicities $6$, $4+2$, or $2+2+2$.

Set all other couplings to zero. Exterior bits are conserved by the Hamiltonian, spectral projections and direct rotation. At most three active edges form a forest, and for a fixed exterior ice configuration that forest has exactly one ice state: the degree constraint fixes each leaf edge, then induction removes the leaves. Hence the relevant effective block is one-dimensional and equals the ordinary nondegenerate energy of the active-edge matrix. This proves why small forest energies determine the global coefficient and includes all folded terms.

For vertex-disconnected active sets, the native strings contain no active edge from another component, and the energy penalty and low projector factor. Their finite Hamiltonian is a tensor sum; its energy series is additive, so inclusion-exclusion removes disconnected contributions. Within a forest one may use $A_j=X_j$ times $Z$ on earlier incident active edges: relative toggle phases between this and the original convention are flat on elementary bit-hypercube squares because the incident anticommutators agree. They give a diagonal unitary preserving energy and support. This is not replacement by bare $X$.

Set $U=\lambda=1$ in the local calculation. With intermediate normalization $\psi_0=|0\rangle$, $\langle0|\psi_n\rangle=0$ for $n>0$, the exact recursion is

\[
E_n=\langle0|V\psi_{n-1}\rangle,\qquad
\psi_n=-RQ\left[V\psi_{n-1}-\sum_{j=1}^{n-1}E_j\psi_{n-j}\right].
\]

For one edge, an incident pair or a three-edge star, native anticommutation cancels every admissible distinct two-flip path; refused paths occur in both orders. Thus $V^2|0\rangle=k|0\rangle$ for $k=1,2,3$ and the bright two-dimensional block has energy $1-\sqrt{1+kg^2}$. Its sixth coefficient is $-k^3/16$. After subtracting proper subclusters the one-edge, incident-pair and star contributions are respectively $-1/16,-3/8,-3/8$. The pair contribution includes both degree-six monomials using its two edges at equal magnitudes.

For a simple three-edge path, let $\alpha=1$ for initial patterns 010 or 101 and zero otherwise. The triple toggle is low-admissible exactly when $\alpha=1$, then with $D=2$. The outer-edge double state $|d\rangle$ always has $D=4$. With $|s\rangle=|1\rangle+|2\rangle+|3\rangle$ and $A_1=X_1,A_2=Z_1X_2,A_3=Z_2X_3$,

\[
V|0\rangle=|s\rangle,\quad V|s\rangle=3|0\rangle+2|d\rangle,\quad
E_2=-3/2,\quad\psi_1=-|s\rangle/2,\quad\psi_2=|d\rangle/4,
\]
\[
E_4=7/8,\qquad \langle d|\psi_4\rangle=-(7-\alpha)/32,
\qquad E_6=-(35+\alpha)/32.
\]

The recurrence uses $V|d\rangle=|1\rangle+|3\rangle-\alpha|123\rangle$; the triple-state coefficient in $\psi_3$ is $\alpha/8$. Adjacent-double terms do not enter $\langle s|V\psi_4\rangle=2\langle d|\psi_4\rangle$. Subtracting three one-edge and two incident-pair contributions leaves $-(5+\alpha)/32$. This local coefficient genuinely depends on the bit pattern.

There are $3N$ edges, $15N$ incident pairs, $20N$ stars and $25(3N)=75N$ three-edge paths. A path is uniquely specified by its middle edge and one of five other edges at each endpoint. Bipartiteness prevents the two exterior vertices from coinciding. At each middle edge exactly three choices at each endpoint have bit opposite to that edge, so exactly nine paths per middle edge alternate: $27N$ total in every ice configuration. Thus for uniform magnitudes,

\[
(H_{\rm eff})_{\rm diag}^{(6)}
=-\left[\frac{3N}{16}+\frac{3(15N)}8+\frac{3(20N)}8
 +\frac{5(75N)+27N}{32}\right]\frac{g^6\lambda^6}{U^5}P
=-\frac{207N g^6\lambda^6}{8U^5}P.
\]

It is constant despite the local path dependence. Unequal magnitudes need not give a constant weighted path sum. Sixth-order off-diagonal terms, including longer loops and dressed four-cycles, are not evaluated. Eighth and higher orders remain open. The result does not claim absence of every possible induced potential.

## Rigorous one-sided fourth-order spectral bound

This separate estimate concerns the complete fourth-order operator, including winding loops. Put

\[
B=\sum_e|\lambda_e|,\quad a=|g|B,\quad d=2U,\quad
c=g^2\sum_e\lambda_e^2,\quad
K_4=-\frac{c}{d}P+g^4H_4.
\]

Assume $a\le U/4=d/8$. For every low-cluster eigenvalue $E$ descending from ice,

\[
\operatorname{dist}(E,\operatorname{spec}K_4)\le\frac{a^6}{U^5}.
\]

This is one-sided spectral distance, not individual eigenvalue matching, multiplicity matching, eigenvector control or a thermodynamic bound. At uniform nonzero coupling $B$ grows with the number of edges. The case $a=0$ is exact.

Since $\|gV\|\le a$, Weyl bounds isolate exactly $\dim P$ eigenvalues in $[-a,a]$ and place the rest above $d-a$. Min-max on the entire $P$ trial space gives $E\le0$ throughout the low cluster, because $PHP=0$. The $Q$ block at such $E$ is at least $d-a>0$, and a low eigenvector has nonzero component $p=P\psi$. The exact Schur equation gives

\[
|E|\le e:=\frac{a^2}{d-a}.
\]

Expand the inverse using $R^{1/2}(gQVQ-EQ)R^{1/2}$, whose norm is at most $k=(a+e)/d=a/(d-a)\le1/7$. The retained terms are $-c/d$, $-Ec/d^2$ and $-g^4A_4$, where $A_4=PVRVRVRVP$. Odd-$V$ terms vanish exactly by occupied-bit parity. The remaining inverse terms through order three and the tail satisfy

\[
\mathcal R\le\frac{a^2e^2}{d^3}
 +\frac{a^2(3a^2e+e^3)}{d^4}
 +\frac{a^2}{d}\frac{k^4}{1-k}.
\]

These terms are respectively the two-$E$ word, three placements of two $gV$ factors and one $E$ plus the three-$E$ word, and the complete inverse tail beginning at order four. No commutation of $V$ with resolvents is assumed. Writing $h=c/d^2\ge0$, the equation is

\[
(1+h)Ep=\left[-\frac{c}{d}P-g^4A_4+\text{remainder}\right]p.
\]

Subtracting $K_4$ after scalar normalization gives

\[
\frac{-cP/d-g^4A_4}{1+h}-K_4
=\frac{h g^4A_4-(ch^2/d)P}{1+h},
\]

whose norm is at most $2a^6/d^5$. Therefore the residual for Hermitian $K_4$ is at most $(\mathcal R+2a^6/d^5)\|p\|$. The spectral residual inequality gives the asserted distance without needing a lower bound on $\|p\|$.

For $r=a/d\le1/8$, the error divided by $a^6/d^5$ is bounded by

\[
\frac1{(1-r)^2}+\frac3{1-r}+\frac{r^2}{(1-r)^3}
 +\frac1{(1-r)^3(1-2r)}+2.
\]

Every term is nondecreasing on this interval. At $r=1/8$ their sum is $1286/147<9$, so the error is at most $9a^6/(32U^5)<a^6/U^5$. This conservative estimate controls the actual native operator, not an RK operator with an added diagonal term.

## Evidence, provenance and prior art

The live helpers retain all 24 native phase/denominator orderings, full L4 backgrounds and repeated-edge diagonal coefficients; separate exact forest recursion and original-native background checks cover the sixth-order diagonal. The remainder helper checks rational constants and parity-word bookkeeping only; the operator inequality is proved above. Actual semantic mutants remove native phases, energy feedback, support restrictions or folded terms and fail explicit predicates. None of these finite checks is a whole-Hilbert census or a numerical proof of the spectral bound.

The [packet](../.claude/science/physics-loops/native-virtual-pair-ring-mechanism-20260908/HANDOFF.md) preserves independent fourth- and sixth-order derivations, the root remainder proof and its cold review, contracts, original raw outputs and failures. The optional later floating spectral supplement is archived only and is not executed or relied on here. The fourth-order sign-convention clarification was exposed by root before the author's final proof; independent proofs were frozen before cross-reading.

[Bravyi, DiVincenzo and Loss](https://arxiv.org/abs/1105.0675) provide standard finite-dimensional perturbative-reduction methodology; no new general Schrieffer–Wolff theorem is claimed. The preserved section-specific literature review identifies the cubic spin-half degree-three carrier in [Hermele, Fisher and Balents](https://arxiv.org/abs/cond-mat/0305401), and distinguishes it from coordination-four ice or close-packed dimers. The cubic carrier has twenty local configurations, not the degree-four six-vertex carrier. Narrow-tube studies and near-RK field theory do not supply a rigorous bulk phase result at the pure kinetic point. The earlier supplied near-RK numerical point cannot be relabeled as evidence for this induced model.

The restrictions, penalty and couplings remain supplied; a compatible sign transformation must precede comparisons to a conventional negative-ring model. No local occurrence mechanism, photon, deconfinement, electromagnetic action or physical scale is selected by this result.
