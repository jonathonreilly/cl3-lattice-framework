---
claim_id: native_zero_penalty_l4_delayed_splitting_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied uniform full-native L4 endpoint: unique minimizing flux orbit, full ground isolation at least |t|/432 and 2^31 ground dimension; positive-overlap canonical electric-penalty effective Hamiltonian is scalar through order five. Sixth order is only support-allowed, with no coefficient or radius claimed."
upstream_dependencies:
  - native_zero_penalty_endpoint_note_2026-09-08
runner: scripts/native_zero_penalty_l4_delayed_splitting_2026_09_08.py
---

# Finite L4 isolation and delayed spectator splitting

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

For the supplied uniform full native Hamiltonian on the $4\times4\times4$ torus, the zero-penalty ground space has dimension $2^{31}$ in one magnetic flux orbit and is isolated from all other states. Adding a small electric penalty gives a canonical effective Hamiltonian scalar through fifth order. This establishes delayed perturbative splitting, not a nonzero sixth-order splitting or a phase.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied finite full-carrier Hamiltonian and exact dictionary."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Premises and actual L4 theorem

Use the [exact endpoint](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md), [full Gauss dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), and [native algebra](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). Retain the entire edge carrier, with no low-charge projection. Set

\[
H(u)=H_0+uD,\quad H_0=t\sum_e A_e,\quad t\ne0,\qquad
D=\sum_v Q_v^2=\frac{3N}{2}+\frac12\sum_v\sum_{e<f\ni v}Z_eZ_f.
\]

Here $u$ is the small electric-penalty parameter near zero, not the inverse large-penalty expansion. For the actual uniform L4 graph, $N=64$. The unique minimizing flux orbit has square Wilson products $-1$ and straight winding products $+1$. Its ground energy, ground dimension and conservative full-space separation are

\[
E_0=-\frac{64\sqrt{24}}4|t|,\qquad
\dim P=2^{31},\qquad \operatorname{gap}(H_0;P)\ge |t|/432.
\]

For the positive-overlap canonical effective Hamiltonian on $P$,

\[
H_{\rm eff}(u)=E_0P+\sum_{j=1}^{5}c_j u^jP+O(u^6),\qquad c_1=96.
\]

The scalar coefficients beyond first order are not evaluated here. Analyticity is finite-volume near zero; no explicit radius is asserted. Order six is the first support-allowed nonscalar order, not a proved nonzero coefficient. Uniqueness refers to the magnetic orbit, not a unique ground vector. The proof uses elementary constant-square/concavity arguments, not an external flux-minimization theorem.

## First-order flux selection

Root supplied the candidate; this derivation verifies it. On the full cubic edge carrier, with degree6 and Q_v=epsilon_v(deg_x(v)-3),

 Q_v²=(1/4)(sum_(e incident v) Z_e)²=3/2+(1/2)sum_(e<f incident v)Z_e Z_f.

Thus D=3N/2+(1/2)sum_v sum_(e<f incident v) Z_e Z_f. No low-charge projection is present. The sign epsilon_v squares away. In a general simple graph the centered penalty (deg_x(v)-d_v/2)² has scalar sum_v d_v/4=E/2 and the same pair sum; that is not automatically the original cubic charge definition on a different graph.

In the full dictionary, Z_e is Z_e^g. Magnetic flux sectors are the orbits of link-X signs under vertex-star flips. An electric product Z_F toggles exactly the subset F of link-X signs and therefore sends flux character phi_C to (-1)^|F intersect C| phi_C for every cycle. It stays within a fixed flux sector if and only if F is a cut (mod2 coboundary). This is the standard cycle/cut orthogonality, also seen directly because a sign assignment is gauge equivalent to its toggled assignment exactly when the changed signs form a product of stars.

For the pair terms of D, F consists of two distinct incident edges. A connected cubic periodic graph with all even extents>=4 has no nonempty cuts of size1 or2 (proved below). Consequently every pair term maps to a distinct flux sector and

 Pi_phi D Pi_phi=(3N/2)Pi_phi

on the ENTIRE fixed-flux even-Fock sector, not just its U0 ground states. Distinct pair terms may reach the same other sector and interfere there; this does not affect the diagonal compression. It does not say D is scalar on the full carrier. Since D vanishes on actual ice states while its trace average is3N/2, it is manifestly not globally scalar.

A direct elementary proof of the needed no2-edge-cut fact avoids any external graph theorem. Given an edge in direction a, there are four length-three square detours between its endpoints, obtained by displacement +b,-b,+c,-c along the two other axes. For extents>=4 these detours are pairwise edge-disjoint and avoid the original edge. Any cut containing that edge must meet each detour, so it contains at least five edges. This lower bound suffices; claiming the sharper connectivity6 is unnecessary to this proof. Periodic seams do not change the distinctness of these translated detours.

For a general connected graph the precise exception is a pair of incident edges that itself forms a cut. Merely having some2-edge cut is not sufficient if its two edges are disjoint and never occur in the penalty sum. If F=delta(S), then on Gauss-invariant vectors product_(e in F)Z_e^g=product_(v in S)P_v^f. Hence its within-sector contribution is a generally nonscalar even matter-parity operator. S and its complement give the same operator because total matter parity is even. A bridge alone does not occur as a linear term in this centered-square penalty, although sums of two bridges can be an incident cut and contribute. Parallel-edge/L2 geometries require their actual incidence and cycle space; the simple cubic argument must not be transferred by collapsing labels.

For perturbation theory, let H0 denote the U0 Hamiltonian at fixed nonzero supplied g and coefficients, and let an eigenspace P_* lie wholly in one flux sector with eigenvalue E_*. If E_* is isolated from ALL other eigenvalues of the full finite H0 by a positive gap, then first-order degenerate perturbation by U D is scalar3NU/2 on P_*. Degeneracy within that flux eigenspace, including spectator degeneracy, is not split at first order. This requires excluding coincident-energy states in other flux sectors; if they exist, the full degenerate eigenspace can have nonzero off-flux D matrix elements at first order. Even with isolation, second and higher orders can couple virtual other-flux states. There is no claim of a cubic optimal flux, a uniform gap, nonzero-U solvability, or scalar correction on the globally degenerate ground manifold without those extra hypotheses.

## Exact bounded controls

The independent standard-library control checks all960 incident edge-pair removals on the actual L4 degree6 graph; each remaining graph is connected, so every term changes a magnetic flux. Small-graph fixed-flux gauge-parity compressions distinguish the hypothesis: on K4 (using its degree-centered penalty) the compression is3I but12 pair terms leave the sector; the full penalty is not scalar, since the all-zero electric state has value9. On a square, the incident pairs are cuts and the even-Fock diagonal values are4,2,2,2,2,2,2,0, a direct nonscalar exception. These are not cubic phase controls. The run passed964 predicates in0.028s, with no sampling or author imports. The general result rests on the cut selection rule and four disjoint detours, not the finite census.

## General delayed-splitting theorem under extra spectral hypotheses

Conditional theorem. Let the finite graph be a rectangular cubic torus with all three extents even and at least four. Use the full native dictionary, with no low-charge projection. Let H0 be the supplied U=0 Majorana hopping Hamiltonian. Assume an eigenvalue E0 of the FULL H0 has eigenspace P contained in one magnetic flux orbit and, in that orbit, consists of a unique full-rank active Majorana vacuum tensored with its allowed spectator parity space. Assume E0 is isolated from every other full-H0 eigenvalue. These are additional spectral hypotheses; flux optimization does not establish them. The small parameter here multiplies D and is not the large-charge-penalty expansion.

Under these hypotheses, the positive-overlap canonical effective Hamiltonian of H0+uD on P is scalar through order FIVE in u. In particular it is scalar through orders two, three and four requested initially. Order six is the first order at which the elementary support and parity rules permit a non-scalar contribution. No nonzero sixth-order coefficient or actual lifting is proved.

## Operator selection rule

In the full dictionary, D=3N/2+(1/2) sum_v sum_{e<f incident v} Ze^g Zf^g. Each nonconstant insertion toggles exactly two incident link-X signs and leaves the matter state unchanged before returning to a chosen gauge representative. H0 and all its resolvents are block diagonal in link-X configurations and involve only even products of active gamma Majoranas.

Take an ordered perturbation word, allowing reduced resolvents, unperturbed spectral projectors and powers thereof between insertions. Its final link toggle F is the mod-two sum of its electric pairs. Returning to the original magnetic orbit is equivalent to F=delta S for a vertex subset S. This equivalence uses the complete cycle fluxes: orthogonality to every cycle is exactly the cut space over F2.

Use an unreduced link-X representative along the word. No intermediate gauge choices are needed. On closing the orbit, the Gauss relation identifies the toggle delta S with the matter operator P_S=product_{v in S} P_v. Each P_v is, up to the fixed convention sign, i gamma_v bar-gamma_v. Therefore a returning word has spectator factor product_{v in S} bar-gamma_v and active factor comprising product_{v in S} gamma_v and even active resolvent functions. The active parity of this factor is |S| modulo two. Since the active vacuum has definite parity, every odd-|S| contribution vanishes after projection onto it. This conclusion does not require Gaussian factorization of a many-point correlator.

If S is empty, the projected active matrix element is a scalar and the spectator factor is identity. If S is the full vertex set, total physical matter parity is +1, so it is the same identity action. Complementary cuts give the same physical result. For other even S a spectator operator is permitted but its coefficient is not determined by this selection rule.

Reduced resolvents introduce no extra spectator operation. Within the starting orbit, the removed projector is the active vacuum projector extended by the identity on spectators and then restricted to even total matter parity. In other link sectors, the resolvent remains a function of an even active quadratic Hamiltonian. The argument thus also covers returns to the starting orbit in the middle of a word.

## Elementary small-cut classification

For a subset S write m_a for the number of coordinate-a circular lines containing both S and its complement. Each such line contributes at least two boundary edges, hence |delta S| >= 2(m_1+m_2+m_3).

Suppose |delta S| <= 10 and S is proper and nonempty. No m_a can be zero. Indeed, if m_a=0, S descends to a nonconstant binary function on the other two-coordinate torus. Such a function has at least two mixed coordinate lines in total: if only one direction varies, at least four parallel lines are mixed; otherwise each direction contributes one. Lifting multiplies this number by L_a>=4, contradicting sum m <=5.

Consequently all three m_a are positive, their sum is at most five, each is at most three, and at least one, say m_a, equals one. Slice in a different coordinate b, with remaining coordinate c. A nonconstant (a,c) slice must contain a mixed a-line: otherwise it is constant along a and any c variation would generate at least L_a>=4 mixed c-lines, exceeding m_c<=3. There is therefore exactly one nonconstant slice. There must be at least one because otherwise a nontrivial stack of constant slices gives m_b=L_a L_c>=16.

All constant slices have the same value; two opposite constant slices would again make every b-line mixed. Let T be the sites in the exceptional slice differing from that common value. Exactly those b-lines are mixed, so |T|=m_b<=3. Thus S or its complement has at most three vertices. A three-vertex subset has at most two internal edges (the graph is simple and triangle-free), and hence boundary at least 18-4=14. A two-vertex subset has boundary 12 unless adjacent, in which case it is 10. A singleton has boundary six.

This proves: every nontrivial cut of size at most ten is a singleton/complement cut or an adjacent-pair/complement cut. In particular every nontrivial even-cardinality cut has size at least ten. This proof does not use an assumed isoperimetric classification or a small-subset census in place of the arbitrary-subset argument.

## Orders and the fifth-order obstruction

At n insertions the toggle support has at most 2n edges. For n<=4, the small-cut classification leaves only empty/full S (scalar) or singleton/complement S (odd and vanishing). At n=5 the only additional possibility is the boundary of adjacent vertices v,w, containing ten edges.

To reach a ten-edge support in five two-edge insertions, every boundary edge must occur exactly once, with no repeated or internal edge. The ten boundary edges form two disjoint five-edge stars for purposes of incidence matching: no edge from one star shares an endpoint with an edge from the other, since adjacent vertices have no common neighbor in this triangle-free graph. Five edges at either star cannot be partitioned into incident pairs. Thus five allowed D insertions cannot realize this cut at all.

At six insertions this particular combinatorial obstruction disappears. At v pair the internal edge vw with one of its five external edges, and pair the other four external edges among themselves. Do the same at w. The six allowed electric pairs toggle all ten boundary edges once and the internal edge twice, giving delta{v,w}. The corresponding spectator factor is a bilinear and active parity is even. This establishes only an allowed support, not a surviving sum over resolvents or a nonzero coefficient.

## Canonical normalization and limitations

Finite isolated spectral perturbation theory supplies the contour projector Pi(u). Let A=P Pi(u) P and B=P (H0+uD) Pi(u) P. The positive-overlap canonical Hamiltonian is A^(-1/2) B A^(-1/2). Every coefficient of A and B is a finite sum of the words considered above. Up to degree five each is scalar on P. Formal power series multiplication and the analytic inverse-square-root expansion therefore remain scalar through degree five. Folded terms and normalization cannot manufacture an earlier spectator splitting. The scalar constant in D does not alter this conclusion.

This general theorem alone does not establish the isolated-eigenspace hypothesis for a flux-minimizing cubic model; the separate L4 proof below does so on its specific finite domain. A degenerate energy shared by distinct flux orbits requires including all those orbits in P; inter-orbit matrix elements are then not constrained to returning cuts, and the present theorem does not apply. Active zero modes likewise invalidate the unique-active-vacuum premise. No radius, coefficient, thermodynamic stability, spectator gap or phase is asserted.

## Actual L4 isolation supplies those hypotheses

Root supplied the proposed constant-square and quantitative Jensen route. The following derivation and integer checks were completed independently of any new author proof. Domain: the actual simple 4x4x4 periodic cubic graph, N=64, uniform real t=g lambda !=0, full native carrier, H0=t sum_e A_e. The full Gauss/CAR fixed-flux dictionary remains an input. This is an exact finite endpoint theorem, not a phase or a volume-uniform assertion.

## Constant square and its equality characterization

In a flux representative xi, set h=iK, K_ij=-2t xi_ij for i<j. The native ground energy in that sector is

E(xi)=-(1/4) Tr sqrt(h^2).

Every row of h has six entries of modulus 2|t|. Thus A=h^2 has A_ii=24t^2 and Tr A=24Nt^2. The row-sum bound gives ||h||<=12|t|, so every eigenvalue of A lies in [0,144t^2].

On the L4 graph any two distinct vertices joined by a two-step walk have EXACTLY two intermediate vertices. For displacement along two different axes these two paths bound an elementary square. For displacement two units along one axis, they are the two halves of a straight winding four-cycle. These exhaust the possibilities. There are no other off-diagonal A entries. The two path amplitudes each have modulus 4t^2. Their ratio is the hopping holonomy of their closed four-cycle. Consequently they cancel if and only if that hopping holonomy is -1.

Hence A=24t^2 I if and only if all elementary square and all straight winding hopping holonomies are -1. These cycles generate the integral cycle space of the torus, so their flux values determine the U(1) gauge orbit; within the sign-valued family they also determine exactly one Z2 gauge orbit. One can see the latter directly by fixing a spanning tree: trivial holonomy of the ratio of two assignments fixes every remaining chord sign.

The representative xi_(r,a)=(-1)^(sum_{b<a}r_b) exists periodically. Its native square holonomies are -1 and its straight winding holonomies are +1. In passing to h, the vertex-order orientation factor is +1 around a square and -1 around a straight winding; the factor (-i)^4 is +1. Thus every one of the corresponding hopping holonomies is -1, including seam squares and all three winding directions. The required constant square is attained. This proof does not import a flux-optimization theorem.

## Strict minimizer and an explicit separation

Scalar concavity gives

Tr sqrt(A) <= N sqrt(24)|t|,

with equality only if all eigenvalues equal 24t^2. For Hermitian A this means A=24t^2 I. Therefore the specified orbit is the unique minimizing magnetic flux orbit, and its ground energy is -N sqrt(24)|t|/4. This is uniqueness of the orbit, not of the many-body ground vector.

For a wrong sign-valued flux orbit, at least one off-diagonal A_ij is nonzero. Its two path contributions are equal instead of cancelling, so A_ij is +8t^2 or -8t^2. Hermiticity gives the symmetric entry as well. Therefore

sum_j (lambda_j(A)-24t^2)^2 = Tr(A-24t^2 I)^2 >= 128t^4.

For f(x)=sqrt(x) on (0,M], f''(x)<=-1/(4M^(3/2)). The tangent bound at mu=24t^2, extended continuously to x=0, is

sqrt(x) <= sqrt(mu)+(x-mu)/(2sqrt(mu))-(x-mu)^2/(8M^(3/2)).

Set M=144t^2 and sum; the linear term vanishes. The trace slack is at least

128t^4/[8(144t^2)^(3/2)] = |t|/108.

Multiplying by the native energy factor 1/4 proves every other flux-sector ground energy is at least |t|/432 above the minimizing sector ground. This is a conservative bound, not the exact sector gap.

In the minimizing orbit all positive active frequencies equal sqrt(24)|t|. K is full rank, and the active vacuum is unique. The spectator constraint allows each active occupation pattern with its corresponding spectator parity, so the first active excitation has energy sqrt(24)|t|. Thus the FULL H0 ground eigenspace is isolated by a gap at least |t|/432, is contained in the single minimizing flux orbit, and has dimension 2^(N/2-1)=2^31. Every state outside that eigenspace belongs either to an excited active pattern in that orbit or to another flux orbit, both already bounded.

## Consequence for small electric penalty

The hypotheses of the previously frozen spectator-selection theorem b1561c3326a62a6a9d045c0380e93bd3eff5c7f22b1bef63238c4ef46487d9b1 now hold for this actual finite uniform L4 model. Therefore the positive-overlap canonical effective Hamiltonian on this 2^31-dimensional unperturbed ground eigenspace, for H0+uD, is scalar through order five in u. This uses the proved small-cut and incident-pair selection argument; it does not compute the first surviving coefficient. Sixth order is only the first support-allowed order. Finite isolation ensures analytic perturbation theory near zero, but no explicit radius or splitting coefficient is asserted here.

At t=0 this argument does not apply. No result for larger tori, inhomogeneous magnitudes, nonzero-u ground-state phase, thermodynamic flux gap or preparation follows. In particular the uniqueness above does not remove the exact spectator ground degeneracy at u=0.

## Finite controls and limits

check.py has no author imports or eigensolver. It constructs the actual 64x64 integer square matrix at t=1, confirms the constant square and all 240 basic-cycle phases, and checks all coordinate-pair path multiplicities. Four single-edge mutations and three winding-only twists yield nonzero square entries and the variance floor. The winding twists preserve every plaquette phase and demonstrate why plaquettes alone would be insufficient. Exact rational arithmetic checks the 1/108 and 1/432 factors. 5091 predicates passed in 0.134 seconds with 16.234375MiB reported RSS. These controls support the literal finite geometry; the all-flux conclusion follows from the two-path/equality proof, not an unperformed enumeration of 2^129 flux sectors.


## Evidence and restrictions

Live portable controls retain964 first-order,87509 cut/Clifford and5091 L4 isolation predicates, total93564. Complex entries in the small Clifford control are exact dyadic Gaussian values; no floating eigensolver or tolerance-based eigenvalue conclusion is used. Independent review controls are archived separately and not added to the live count. The failed reviewer mixed-line bound is preserved with its correction; it was not a defect in the source theorem.

Actual isolated mutants remove the final active-vacuum projection, treat off-flux terms as within-sector identity, and omit winding circuits from the isolation characterization. They must fail actual operator or geometry predicates. Finite controls support the general cut proof and equality characterization; they do not enumerate all flux sectors or compute the sixth-order coefficient.

All Hamiltonian choices remain supplied. The general theorem requires its full-isolation and unique-active-vacuum premises; the L4 proof supplies them only for the stated uniform finite model. No larger-volume isolation, thermal state, radius, spectator gap at nonzero penalty, phase or physical selection is established. The [packet](../.claude/science/physics-loops/native-zero-penalty-l4-delayed-splitting-20260908/HANDOFF.md) preserves complete proofs, failures, source hashes, review and fresh execution receipts. No external flux-optimization result is needed in this block.
