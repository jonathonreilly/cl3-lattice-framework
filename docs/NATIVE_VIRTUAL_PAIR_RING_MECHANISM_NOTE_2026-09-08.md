---
claim_id: native_virtual_pair_ring_mechanism_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied full native edge-carrier H=UD+g sum lambda_e A_e, without a hard low-charge projector: exact fourth-order ring/scalar coefficients with orientation and winding factors, constant sixth-order diagonal for uniform magnitudes, and a one-sided finite-volume fourth-order spectral error bound a^6/U^5 when a=|g|sum|lambda_e|<=U/4. No sixth-order off-diagonal calculation, RK-point selection, thermodynamic estimate or electromagnetic identification."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/native_virtual_pair_ring_mechanism_2026_09_08.py
---

# Rings induced by virtual native pairs

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

Virtual pair fluctuations on the full native edge carrier generate an ice ring term at fourth order without an inserted low-charge projector. The supplied energy penalty suppresses charge excitations; it does not remove them from the carrier. Its native signs differ from a bare edge-flip perturbation. The accompanying diagonal is constant through sixth order for uniform coupling magnitudes, so this calculation does not generate the matching RK flippability potential at either order. A separate finite-volume estimate bounds the fourth-order spectral approximation.

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

Retain every edge-bit configuration, including $|Q_v|>1$; here $Q_v$ can range from $-3$ to $3$. Write $P$ for the complete ice space $D=0$ and $Q=I-P$ for its full complement; this unindexed projector is distinct from $Q_v$. With sorted edge orientation, native Hermitian $A_e$ flips its own edge and distinct generators anticommute precisely when their edges meet. The supplied perturbation is

\[
H(g)=H_0+gV,\qquad H_0=UD,\qquad
V=\sum_e\lambda_e A_e,\qquad U>0,
\]

with fixed real $\lambda_e$ and real strength $g$. Neither this perturbation nor its penalty is selected by the axioms. Original number-preserving $T$ dynamics is not being substituted for $A$. All charge states and their actual energy denominators are retained. The earlier hard-projected model is explicitly compared below; its frozen source and outputs are preserved.

## Schur reduction and fourth-order normalization

The $Q$ spectrum of $H_0$ starts at $2U$: signed charges are integers and sum to zero on the closed bipartite graph, so any non-ice configuration has $D\ge2$. Since $PVP=0$, eliminating the $Q$ component of an eigenvector gives, whenever the finite inverse exists,

\[
Ep=-g^2PVQ\,[Q(H_0+gV-E)Q]^{-1}QVPp.
\]

Put $R=QH_0^{-1}Q$ and $C=\sum_e\lambda_e^2$. Every single edge flip from ice creates $D=2$. A two-step ice return repeats that edge, so

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

For incident edges with equal initial bits, the newly retained two-edge state has $D=6$. All four irreducible words have denominators $2U,6U,2U$ and amplitudes $-1,+1,+1,-1$, so they cancel. Opposite initial bits give denominators $2U,2U,2U$ and the same cancellation. These formerly refused high-charge paths do not change the fourth-order coefficient. Therefore the entire diagonal is the scalar

\[
H_{4,\rm diag}=\frac1{U^3}\left[
\frac18\sum_e\lambda_e^4+
\frac14\sum_{\{e,f\}\text{ incident}}\lambda_e^2\lambda_f^2
\right]P.
\]

The incident-pair sum is unordered. For uniform $|\lambda_e|=\lambda$, it equals $33N\lambda^4/(8U^3)$. Here the full native generators obey the stated anticommutation exactly. In the earlier projected model the same result followed from cancellation of admissible paths and paired refusals; no global anticommutation of projected generators was assumed.

A nontrivial four-toggle ice return is an alternating simple four-cycle. Four distinct changed edges must balance their increments at each vertex; on this simple bipartite graph that forces such a cycle. All 24 orders already stay within $|Q_v|\le1$, even though that is no longer imposed. After the first and third flips $D=2$; after the second it is two for adjacent edges and four for opposite edges. No intermediate state is ice, so the folded term has no off-diagonal contribution.

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

Replacing native $A$ by bare $X$ is a different model: its 24 positive alternating-cycle amplitudes give $-5\prod\lambda_e/(2U^3)$. The full native phase information is therefore essential. The earlier hard-projected bare-$X$ diagonal comparison is retained in the historical source; it must not be silently transferred to the new full domain.

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

For vertex-disconnected active sets, the native strings contain no active edge from another component, and the energy penalty factors. Their finite Hamiltonian is a tensor sum; its energy series is additive, so inclusion-exclusion removes disconnected contributions. Within a forest one may use $A_j=X_j$ times $Z$ on earlier incident active edges: relative toggle phases between this and the original convention are flat on elementary bit-hypercube squares because the incident anticommutators agree. They give a diagonal unitary preserving energy and support. Every active bitstring is retained in this full-carrier calculation. This is not replacement by bare $X$.

Set $U=\lambda=1$ in the local calculation. With intermediate normalization $\psi_0=|0\rangle$, $\langle0|\psi_n\rangle=0$ for $n>0$, the exact recursion is

\[
E_n=\langle0|V\psi_{n-1}\rangle,\qquad
\psi_n=-RQ\left[V\psi_{n-1}-\sum_{j=1}^{n-1}E_j\psi_{n-j}\right].
\]

For one edge, an incident pair or a three-edge star, native anticommutation cancels every distinct two-flip path from the bright vector, including the newly retained equal-bit excitations. Thus $V^2|0\rangle=k|0\rangle$ for $k=1,2,3$ and the bright two-dimensional block has energy $1-\sqrt{1+kg^2}$. Its sixth coefficient is $-k^3/16$. After subtracting proper subclusters the one-edge, incident-pair and star contributions are respectively $-1/16,-3/8,-3/8$. The pair contribution includes both degree-six monomials using its two edges at equal magnitudes.

For a simple three-edge path, the triple-toggle state is always retained. Let $m$ count its equal-bit internal junctions. Its energy in $U=1$ units is

\[
d_3=2+4m\in\{2,6,10\}.
\]

The two exterior endpoints contribute one each; every equal-bit internal junction contributes four. The outer-edge double state $|o\rangle$ has $D=4$. With $|s\rangle=|1\rangle+|2\rangle+|3\rangle$ and $A_1=X_1,A_2=Z_1X_2,A_3=Z_2X_3$,

\[
V|0\rangle=|s\rangle,\quad V|s\rangle=3|0\rangle+2|o\rangle,
\quad V|o\rangle=|1\rangle+|3\rangle-|111\rangle.
\]

Adjacent-double contributions cancel before their differing energies enter. The exact recursion gives

\[
E_2=-3/2,\quad E_4=7/8,\quad
\psi_3(111)=\frac1{4d_3},\quad
\langle o|\psi_4\rangle=-\frac7{32}+\frac1{16d_3},\quad
E_6=-\frac{35+2/d_3}{32}.
\]

Subtracting the three single-edge and two incident-pair contributions leaves the connected path coefficient $-(5+2/d_3)/32$: respectively $-3/16,-1/6,-13/80$ for $d_3=2,6,10$. The newly admitted high-charge excursions change this local coefficient.

There are $3N$ edges, $15N$ incident pairs, $20N$ stars and $75N$ three-edge paths. A path is uniquely specified by its middle edge and one of five other edges at each endpoint; bipartiteness prevents coinciding exterior vertices. Each endpoint offers three opposite-bit and two same-bit edges. Thus every middle edge has nine paths with $d_3=2$, twelve with $d_3=6$ and four with $d_3=10$. Their weighted sum is $9+12/3+4/5=69/5$, independently of the ice configuration. For uniform magnitudes,

\[
(H_{\rm eff})_{\rm diag}^{(6)}
=-\left[\frac{3N}{16}+\frac{3(15N)}8+\frac{3(20N)}8
 +\frac{5(75N)+3N(69/5)}{32}\right]\frac{g^6\lambda^6}{U^5}P
=-\frac{1053N g^6\lambda^6}{40U^5}P.
\]

This is still a scalar, not an RK flippability potential. Unequal magnitudes need not give a constant weighted path sum. Sixth-order off-diagonal terms, including longer loops and dressed four-cycles, are not evaluated. Eighth and higher orders remain open.

## Comparison with the preserved hard-projected model

The earlier model used $P_{\rm low}A_eP_{\rm low}$ and omitted states with $|Q_v|>1$. Its fourth-order ring and native diagonal are exactly the same as above: the newly admitted incident equal-bit $D=6$ paths cancel. For the hard model, however, nonalternating triple-path states are refused. Its local path coefficient is $-(5+\alpha)/32$, where $\alpha$ indicates an alternating path. Exactly nine paths per middle edge alternate, giving the earlier sixth diagonal $-207N g^6\lambda^6/(8U^5)$. The full-carrier value differs by $-9N g^6\lambda^6/(20U^5)$. Both derivations and their separate controls remain preserved; this is a genuine domain change, not a silent correction of the old coefficient.

The result removes the hard low-charge projector from this particular virtual-ring mechanism. It does not extend the restricted two-species no-double U1 dictionary to the full carrier: when $|Q_v|>1$, its matter labels and identity $n_c=1-Q_v^2$ fail. Nor is the whole old low-charge subspace an isolated energy band. Many unit defects may cost more than a higher-charge configuration. Only the ice-descended band is isolated by the bound below; the full native CAR/$Z_2$ dictionary remains the exact parent.

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

Every ambient $A_e$ has norm one. Since $\|gV\|\le a$, Weyl bounds isolate exactly $\dim P$ eigenvalues in $[-a,a]$ and place the rest above $d-a$. Min-max on the entire $P$ trial space gives $E\le0$ throughout the low cluster, because $PHP=0$. The $Q$ block at such $E$ is at least $d-a>0$, and a low eigenvector has nonzero component $p=P\psi$. The exact Schur equation gives

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

The live helpers retain all 24 native phase/denominator orderings, full L4 backgrounds and repeated-edge diagonal coefficients for both domains; separate full-carrier forest recursion and original-native background checks cover the new sixth-order diagonal. The old hard-model helpers and outputs remain separately preserved. The remainder helper checks rational constants and parity-word bookkeeping only; the operator inequality is proved above. Actual semantic mutants remove native phases, energy feedback, support restrictions or folded terms and fail explicit predicates. None of these finite checks is a whole-Hilbert census or a numerical proof of the spectral bound.

The [packet](../.claude/science/physics-loops/native-virtual-pair-ring-mechanism-20260908/HANDOFF.md) preserves independent fourth- and sixth-order derivations, the root remainder proof and its cold review, contracts, original raw outputs and failures. The optional later floating spectral supplement is archived only and is not executed or relied on here. The fourth-order sign-convention clarification was exposed by root before the author's final proof; independent proofs were frozen before cross-reading.

[Bravyi, DiVincenzo and Loss](https://arxiv.org/abs/1105.0675) provide standard finite-dimensional perturbative-reduction methodology; no new general Schrieffer–Wolff theorem is claimed. The preserved section-specific literature review identifies the cubic spin-half degree-three carrier in [Hermele, Fisher and Balents](https://arxiv.org/abs/cond-mat/0305401), and distinguishes it from coordination-four ice or close-packed dimers. The cubic carrier has twenty local configurations, not the degree-four six-vertex carrier. Narrow-tube studies and near-RK field theory do not supply a rigorous bulk phase result at the pure kinetic point. The earlier supplied near-RK numerical point cannot be relabeled as evidence for this induced model.

The relaxed magnetic-cycle condition, penalty and couplings remain supplied; a compatible sign transformation must precede comparisons to a conventional negative-ring model. No local occurrence mechanism, photon, deconfinement, electromagnetic action or physical scale is selected by this result.
