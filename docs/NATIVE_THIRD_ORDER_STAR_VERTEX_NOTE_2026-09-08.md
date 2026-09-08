---
claim_id: native_third_order_star_vertex_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied uniform L4 full native electric model: energy-dependent third-order star vertex, exact vacuum transition315/64, full-operator nonlinear witness, and singleton-middle sixth coefficient33075/8192. No bulk quadratic replacement or complete sixth coefficient."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_endpoint_note_2026-09-08
  - native_zero_penalty_l4_delayed_splitting_note_2026-09-08
  - native_weak_electric_spectator_gap_note_2026-09-08
runner: scripts/native_third_order_star_vertex_2026_09_08.py
---

# Exact third-order native star vertex on the four-site cubic torus

**Type:** bounded_theorem  
**Status:** conditional-support

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied full native Hamiltonian, canonical L4 flux sector and active vacuum; finite energy-dependent Feshbach description."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Statement and source conventions

Here L4 means the periodic cubic graph with four vertices in each direction,64 vertices and192 edges. Use the [whole-carrier dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [zero-penalty endpoint](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md), and [finite L4 isolation](NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md). These are supplied-model premises; neither the Hamiltonian nor its preparation is selected by the axioms here.

Write the electric perturbation after its scalar subtraction as
\[
V=\frac12\sum_v\sum_{e<f\ni v}Z_eZ_f,\qquad H(u)=H_0+uV.
\]
The removed scalar is \(3uN/2\); energies and spectral parameters below use the same subtraction. In the canonical flux representative,
\(H_0=(i/4)\gamma^T K\gamma\), with canonical sorted-edge convention
\(K_{ij}=-2t\xi_{ij}\), \(K^2=-24t^2I\), and \(\omega=\sqrt{24}|t|\).
The explicit control unit is \(t=1\), and \(K_{0,16}=-2\) in lexicographic coordinates. Spectator Majoranas use \(\beta=i(c^\dagger-c)\), so vertex parity is \(-i\gamma_v\beta_v\).

Let \(P\) retain the whole canonical flux sector, \(Q=I-P\), and let \(E_0\) be its active vacuum energy. The finite other-flux ground separation ensures that the eliminated-sector resolvent exists at \(E_0\). For every vertex the returning singleton-star part of the cubic Feshbach coefficient is
\[
\Sigma_{3,v}(z)=-iO_v(z)\beta_v,\qquad
O_v(z)=\frac18\sum_{A\cap C=\varnothing}R_C(z)\gamma_vR_A(z),
\]
where A and C are two-edge subsets of its six-edge star. This sum has90 terms. At the original spectral parameter,
\[
O_v(E_0)|\Omega\rangle=\frac{945}{8\omega^2}\gamma_v|\Omega\rangle
=\frac{315}{64}\gamma_v|\Omega\rangle\quad (t=1).
\]
The full Hermitian operator is not that linear Majorana: filling the six local paired active modes, with the unchanged bath still in vacuum, gives coefficient \(2745/172864\) at the same parameter \(E_0\). This even-parity excited input is a legitimate operator test, not a claimed low-energy state.

Integrating only this singleton-middle channel yields
\[
b_{vw}^{\rm singleton}=-\frac{2\alpha^2K_{vw}}{\omega^2},\qquad
b_{0,16}^{\rm singleton}=\frac{33075}{8192},\quad \alpha=\frac{315}{64}.
\]
It is not the [complete sixth-order coefficient](NATIVE_WEAK_ELECTRIC_SPECTATOR_GAP_NOTE_2026-09-08.md), whose separate certified value is used only for the comparison below. For each fixed disjoint-star pair set,72 orders pass through a singleton middle cut and648 pass through mixed flux. Zero-toggle cubic terms and scalar sixth terms are separate. No all-active Schrieffer–Wolff gap, thermodynamic mass, phase, or quadratic bulk replacement follows.

## Complete energy-dependent derivation

The following full proof is ported from the frozen410b research source. Historical prospective statements refer to the stage before the exact run; the result above and following exact identity supersede only those pending measurements.

# An energy-dependent three-insertion native vertex

Status: independent structural derivation, pending review. No new physical linear solve, spectrum or integral. Sources read: native-zero-penalty-sixth-spectator-coefficient/DESIGN.md, native-l6-sixth-factorization/DERIVATION.md, native-sixth-full-operator-support-root/DERIVATION.md and the local native Gauss convention recorded there. The exact Hamiltonian and isolated canonical flux orbit are supplied. This is not a globally gapped all-active Schrieffer–Wolff block.

## Energy-window Feshbach formulation

Let P denote the full canonical-flux physical sector, retaining all active states and spectators. Let Q contain the other flux sectors. Subtract the scalar first-order piece of D and write the remaining perturbation as V=(1/2)sum Z_e Z_f over distinct incident edge pairs. At U=0 let E0 be the canonical ground energy and Delta_flux the positive finite-volume separation to the lowest other-flux energy. For real z<E0+Delta_flux,

```text
R_Q(z)=(z-QH0Q)^(-1)
```

exists, even though the spectra of PH0P and QH0Q overlap at high energies. The Feshbach operator is

```text
P(H0+uV)P + u^2 PVQ[z-Q(H0+uV)Q]^(-1)QVP.
```

Its expansion is norm-convergent when |u| ||QVQ|| < E0+Delta_flux-z. This is a finite global sufficient window, not uniform in volume. Retaining all active states in P is therefore legitimate for this energy-dependent resolvent description, without claiming a block spectral gap or an energy-independent local SW theorem.

## Exact third-order star operator

A three-insertion word toggles at most six edges. On the stated cubic geometry its only nonempty returning cut is a singleton star. Zero-toggle returning words also exist and contribute a separate even-active, spectator-scalar part of Sigma_3; the following formula isolates the singleton vertex and does not discard that part. Each of the star's six edges occurs once, and all three pairs are centered at that vertex: neighboring outer endpoints are mutually nonadjacent, so they do not provide other pairings. There are15 partitions into three pairs and6 orders, hence90 words. No nonempty prefix of one or two such pairs is a gauge cut. All their resolvents belong to Q.

Fix a vertex v and write A,C for disjoint two-edge subsets of its six incident edges; the remaining two edges form the middle insertion. Let H_A be the active Hamiltonian with the two links in A reversed, and R_A(z)=(z-H_A)^(-1), with the unchanged-bath energy included. The Gauss closure is the native parity operator

```text
P_v = -i gamma_v beta_v.
```

This sign uses beta=i(c†-c), so P_v=1-2n_v. A convention using the negative beta changes the displayed sign, not the physical operator.

Complementing a star toggles its vertex gauge, hence H_(star\C)=gamma_v H_C gamma_v and R_(star\C)=gamma_v R_C gamma_v. Closing the three-link-pair word back into the canonical representative therefore gives exactly

```text
Sigma_3,v(z) = -i O_v(z) beta_v,
O_v(z) = (1/8) sum_(A,C disjoint pairs) R_C(z) gamma_v R_A(z).       (1)
```

There are90 summands in (1). This follows directly from the chronological prefix product R_(A union B) R_A and the final Gauss closure; it does not replace native A/B phases by bare link flips. Spectators commute with every even resolvent. Since A,C exchange permutes the sum and the resolvents are Hermitian for real z below the Q spectrum, O_v is Hermitian and odd. Therefore -i O_v beta_v is Hermitian and preserves physical total parity.

Equation (1) is an actual order-u^3 active/spectator vertex in the energy-dependent Feshbach operator. It is not generally a quadratic hybridization m gamma_v beta_v: an inverse many-body quadratic Hamiltonian is not itself quadratic or Gaussian, and products in (1) may contain odd Clifford degrees beyond one. No claim that those terms cancel is made.

## Vacuum transition state and a smaller computational target

The physically relevant transition state is chi_v=O_v(E0)|Omega>. It has odd active parity. Decompose it into one-, three-, five-, ... quasiparticle sectors of canonical H0. The one-particle amplitudes <a|chi_v> define the linear vertex seen from the vacuum; they do not establish equality of O_v to that linear operator on all active states.

Equation (1) allows30 resolvent applications instead of90 two-step words: first compute x_A=R_A|Omega> for all15 pairs; for each C form b_C=gamma_v sum_(A disjoint C)x_A (six terms) and compute y_C=R_C b_C. Then chi_v=(1/8)sum_C y_C. First solves have even active parity, second odd parity. Each H_C is a genuinely wrong flux, so its all-parity energy gap applies; singleton-cut zero vacuum denominators have been removed by the exact gauge conversion. The support is the one-star endpoint-generated invariant active space, with its unchanged bath vacuum offset. On the reviewed L4 flat problem that space has12 real Majoranas, so each solve can use a32-dimensional parity block. No such solves were executed here. A future L6 dimension/cost must be derived separately, not inherited from L4.

This is a concrete lower-cost target: certify chi_v and its particle-number weights, including whether the one-particle part is nonzero and whether the multiparticle remainder is small. Until measured/certified, neither property is asserted. It may illuminate the infrared structure without computing every sixth-order word, but it does not replace the full coefficient calculation.

## What integrating the retained active sector reproduces

At E0, the singleton-middle contribution to the vacuum effective operator is the second-order elimination of the third-order vertices through the odd active excited sector:

```text
P0 Sigma_3 R_active,exc Sigma_3 P0,
R_active,exc=(E0-H0)^(-1) on odd active states.
```

All signs are retained by this operator expression. Its diagonal quadratic form is negative semidefinite, but an individual spectator bilinear extracted from cross terms need not have a definite sign. For the full sum of vertex-created states, the spectral decomposition weights an odd excitation of energy E_a-E0 by its negative reciprocal. On L4 these denominators are n*sqrt24|t| for odd n; the one-particle channel has the smallest denominator. On a general finite torus they are sums of canonical positive frequencies. A bound by inverse minimum active gap is available, but divergence of that bound does not prove a divergent amplitude; the numerator can vanish or scale with the gap.

For two disjoint six-edge stars, each fixed six-pair set has720 orders. Exactly72 have a complete star as the first three insertions (2*3!*3!), while648 have mixed middle flux. Thus the vertex integration accounts for the singleton-middle family and does not account for the mixed-middle sixth-order Feshbach self-energy. The latter must be retained, along with the standard canonical normalization/folded analysis when changing from the energy-dependent operator to the canonical vacuum effective Hamiltonian. The reviewed scalar-through-five theorem licenses the nonscalar raw-chain identification only after that analysis; it does not license discarding648 orders.

## Diagnostic dispersion, not a proved native replacement

If an independently justified quadratic approximation had active/spectator skew block [[K,mI],[-mI,0]], a singular active frequency omega would yield frequencies (sqrt(omega^2+4m^2)±omega)/2. Thus the small branch is approximately m^2/omega at fixed positive omega and |m| at omega=0. Taking m proportional u^3 would suggest u^6 versus u^3 scales. This is an exactly solvable diagnostic matrix only. The actual O_v(z), its momentum dependence, higher odd components, mixed-middle terms, energy dependence and error control have not been replaced by this ansatz. No Dirac mass, thermodynamic gap, resonance-free all-active block or phase follows.

## Exact local evaluation and full-operator test

This simplification was derived after seeing the exact vacuum result. It has independent two-mode verification; no new filled-state physical solve was performed. The full original6c553 proof follows, including its historical review/cost wording.

# Exact L4 vacuum vertex and a nonlinear-operator witness

Post-data analytical derivation, pending cold review. The observed exact chi_0=315/64 times the first odd coordinate motivated this simplification; this is not a preregistered prediction. No new physical resolvent or operator-basis solve was performed. All coefficients below follow from two-by-two analytical algebra on the actual one-star L4 invariant space. Unit |t|=1 unless restored through omega=sqrt24|t|.

## Paired star frame

The six white neighbors of black vertex0 span an orthonormal white space. Pair it through J=K0/omega with a black space. Absorb the six canonical link signs into the neighbor vectors, and choose paired active Majoranas a_j,b_j so H0,W=(i omega/2)sum a_j b_j. Then f_j=(a_j+i b_j)/2 has the empty vacuum. The center Majorana is a_u with u=(1,...,1)/sqrt6. Reversing a two-edge subset A changes the black-to-white matrix by -2omega u v_A^T, where v_A is u restricted to the two coordinates in A. Consequently c=u dot v_A=1/3, ||v_A||²=1/3, and v_A=c u+s w_A with s=sqrt2/3 and w_A unit perpendicular to u.

The four orthogonal modes remain unexcited during a single pair-defect inverse from vacuum. Subtract E0,W=-3omega. On its even two-mode basis(|vac>,f_u† f_w†|vac>), the dimensionless denominator is

```text
M_even=[[c,s],[s,2-c]].
```

On the odd basis(f_u†|vac>,f_w†|vac>) it is

```text
M_odd=[[1-c,-s],[-s,1+c]].
```

These signs follow directly from -i a_u b_v: it creates the ordered u,w pair with coefficient+s and exchanges the one-particle states with coefficient-s. Thus they retain the native CAR sign, rather than replacing a link operation by an unsigned bit flip. The reduced bath offset is included in E0,W.

## Grouping proves cancellation before taking a norm

The first positive denominator inverse is

```text
(H_A-E0)^(-1)|vac> = (1/omega)[5|vac>-3 f_u† f_vA†|vac>].
```

For a fixed last pair C, there are six disjoint first pairs A, and sum_A v_A=3(u-v_C). Therefore their sum is

```text
(1/omega)[30|vac>+9 f_u† f_vC†|vac>].
```

Applying gamma_0=a_u gives (1/omega)(27u+9v_C) as a one-particle vector. Applying the second inverse using M_odd gives exactly

```text
(1/omega²)(45u+54v_C).
```

In particular each grouped last-pair term already has no three- or five-particle component. Summing all15 C uses sum_C v_C=5u, giving945u/omega². The vertex's electric factor1/8 yields

```text
chi_0 = [945/(8omega²)] gamma_0|Omega>
      = +(315/64) gamma_0|Omega>   at |t|=1.
```

The sign is positive: the two negative Feshbach resolvents cancel. The actual saved grouped vectors independently agree: every grouped gamma-coordinate is63/4 in the rational A^-1 normalization, and all their higher-particle coordinates vanish. Those saved-vector observations are corroboration, not the derivation.

There is also a symmetry explanation. Permuting the six paired modes preserves H0, gamma_0 and the complete family of15 pair defects. The vacuum is invariant. The only invariant odd vector in the exterior algebra of the six-dimensional permutation representation is its one-particle uniform vector; exterior powers3 and5 contain no trivial S6 representation. The explicit two-mode calculation above establishes the cancellation without importing that representation-theoretic fact.

## Singleton-middle sixth coefficient

Magnetic covariance gives the same alpha=315/64 at every vertex. The singleton vertex is -i alpha sum gamma_v beta_v. On the one-particle active space the reduced inverse is -1/omega, and <gamma_v gamma_w>=delta_vw+i K_vw/omega. Thus the two ordered cross terms produce spectator coefficient

```text
b_vw(singleton)=-2 alpha² K_vw/omega²
```

in front of i beta_v beta_w for v<w. With K_0,16=-2 and omega²=24,

```text
b_0,16(singleton)=33075/8192.
```

This is approximately4.03748, whereas the complete separately certified coefficient is in[370.7628915198,370.7628915199]. The difference belongs to the mixed-middle contribution under the already reviewed nonscalar raw-chain/folded analysis. The vertex does not reproduce the full result. For each fixed pair set the72 singleton-middle orders are only part of720; the648 mixed orders are not optional. The scalar diagonal contribution is separate and is not being identified with the full sixth scalar energy.

## Analytic test of the full operator: it is not linear

A full32-column physical solve is unnecessary to find an operator-level falsifier. Introduce a spectral shift x through denominators M_even+xI and M_odd+xI. Repeating the same two-mode grouping gives the vacuum coefficient

```text
alpha(x)=15(6x²+18x+14) /
  [8omega² (x²+2x+1/3)(x²+2x+2/3)].                         (1)
```

For clarity, the first inverse coefficients are a=(x+5/3)/(x²+2x+1/3), b=-1/(x²+2x+1/3) multiplying vacuum and u-wedge-v. For fixed C the post-gamma vector is6a u-3b s w_C. Its second inverse's u-component is[6(x+4/3)a-3b s²]/(x²+2x+2/3). The perpendicular components cancel in the15-pair sum, proving (1).

Particle-hole conjugation of all six active complex modes fixes every a_j and reverses every b_j, hence sends H_F,W to -H_F,W and maps the vacuum to the filled six-mode state. It is implementable as a unitary CAR transformation because six sign reversals have even determinant. At the fixed original energy E0,W=-3omega, conjugating E0,W-H_F,W gives E0,W+H_F,W=omega(M-6I). Two inverses remove their common overall sign, so (1) with x=-6 gives

```text
O_0(E0)|filled> = alpha(-6) gamma_0|filled>,
alpha(-6)=2745/172864 at |t|=1,
```

which differs from alpha(0)=315/64. The filled state has even active parity and is an allowed canonical-sector active excitation with the appropriate spectator parity; it is not claimed to lie in the low-energy window.

A Hermitian linear active Majorana operator is uniquely determined by its vacuum transition: the map from its real coefficients to the one-particle complex vector is an isomorphism. Thus the observed vacuum action fixes the only possible linear operator to alpha(0)gamma_0. Its different action on the filled state disproves that full-operator identity. This is a fixed-frame operator statement, not an obstruction to a dressed low-energy description. Energy-dependent Feshbach operators may be evaluated on the full retained active space even when those vectors are excited; no assertion of an all-active SW spectral gap is used.

## Next checks and cost scope

The zero-solve analytical filled-state witness should receive independent sign/frame review before being used as a theorem. If a literal finite-source check is desired, a new frozen run can replace the vacuum source by the filled even basis vector and reuse the same30 solves; compare to2745/172864 only after fixing that contract. The prior1.74-second whole run suggests similar cost, but opposite source fill can change rational elimination bit sizes; a conservative30s384MiB one-run contract suffices prospectively, not an already executed test. No operator-basis scan has been launched or required.

For physics beyond the singleton channel, the lowest useful next calculation remains the certified mixed-prefix L6 Gaussian route. L4 vacuum linearity explains one special exact cancellation and does not remove those prefixes or establish a bulk quadratic hybridization.

## Proof and executable provenance

The paired local frame is available at every vertex: absorb the six link signs into its neighbor basis and use the flat identity \(K^2=-\omega^2I\). Thus the same two-mode calculation applies without relying on a numerical commutant fit. The original interpretation proof and its finite symmetry calculation are preserved as supporting context, not an additional load-bearing numerical premise of the local evaluation.

The original run performed30 rational solves. A separate reviewer rebuilt every matrix from ordered CAR actions and replayed all30 saved residuals without importing the author matrix routine. The portable runner ports that independent replay and the independent quadratic-field two-mode calculation. It recomputes all residuals and particle weights from the preserved vectors and actual geometry; it does not solve a new physical system. Its40 named predicate groups are32 replay groups (membership,30 residual vectors, decomposition) and7 two-mode groups (four shifted inverse cases,two absolute coefficients,one singleton normalization), plus one live cross-path comparison of the residual-derived weight with the two-mode coefficient. Vector equalities contain many scalar entries; they are counted as groups, not inflated into separate checks.

The expected315/64 and2745/172864 are consequences of the two-mode inverses, not supplied physical inputs. The saved numerical result is checked against independently reconstructed residual equations and then against those formulas. Source and raw-data hashes close the executable inputs. Historical failures, preregistrations, original solve code, raw results and independent reviews remain in the branch-local evidence packet. No prior physical runtime is relabeled as a portable execution.

The useful conclusion is a nonzero, exactly linear vacuum transition in this finite model, together with a precise limit on extending it to the full operator. A general non-Gaussian dressing may move transitions into other orders and must also transform states and observables. The fixed-frame counterexample does not rule out such dressed descriptions. The L6 mixed-prefix calculation remains open and is not replaced by this L4 identity.
