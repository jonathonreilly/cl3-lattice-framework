---
claim_id: record_formation_partial_class_dispersion_and_zero_mode_factorization_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "For the explicitly declared number-conserving bipartite free-fermion Hamiltonian with invertible off-diagonal block Q, half-filled negative-energy Slater state, and projective occupation measurements on an even-sublattice set S that reduces sqrt(Q Q-dagger): the remaining conditional state factors into the complete negative-energy sea of the reduced Hamiltonian and outcome-dependent occupied zero modes. For the separately declared period-two cubic staggered pi-flux Hamiltonian, removing any r of its four even parity classes preserves the nonzero Bloch energies with multiplicity 4-r and supplies r zero bands away from the original node. Finite torus spectra and explicitly supplied propagation probes are numerical checks on their named domains."
upstream_dependencies: []
runner: scripts/record_formation_partial_class_dispersion_2026_09_04.py
---

# Partial parity-class formation: dispersive matter and conditional zero modes

**Date:** 2026-09-04

**Type:** bounded_theorem

**Status:** proposed_retained

**Audit:** unset. This is an author proposal of a bounded mathematical result; an independent audit determines any effective status.

**Primary runner:** [record_formation_partial_class_dispersion_2026_09_04.py](../scripts/record_formation_partial_class_dispersion_2026_09_04.py).

**Independent checker:** [record_formation_partial_class_dispersion_independent_check_2026_09_04.py](../scripts/record_formation_partial_class_dispersion_independent_check_2026_09_04.py).

## Exact target and boundary

The target is to calculate the conditional matter state, complete kinetic spectrum, and propagation on a specified live region after an incomplete sequence of occupation measurements and hopping deletions.

All Hamiltonians, fermion modes, the initial Slater state, projective instruments, and unitary time below are supplied mathematical objects. The formation schedule is a supplied selection of whole parity classes. This note treats occupation outcomes as declared records; the correspondence to the framework's physical edge-qubit records and its nearest-neighbor admissibility is an additional physical question. The following results require no amendment to the framework axioms and make no claim that those axioms select these objects.

The physical lattice/one-site algebra, initial state selection, apparatus, formation rate, energy accounting of the changing Hamiltonian, and subsequent interactions require their own constructions. In particular, the supplied positive-band packet is a propagation probe, rather than a derived preparation protocol. The spectral multiplicities here count bands of this declared operator.

## Supplied objects and proof obligations

| Object or obligation | Definition or role | Treatment here |
|---|---|---|
| Bipartite Hamiltonian | `h = [[0,Q],[Q†,0]]`, square invertible `Q` | Declared finite mathematical domain |
| Initial state | All negative-energy orbitals occupied, all positive-energy orbitals empty | Supplied state, not a vacuum-selection theorem |
| Recorded set | A subset `S` of the first sublattice; its coordinate projector commutes with `K=sqrt(QQ†)` | Explicit hypothesis; established for complete parity classes in the cubic specialization |
| Instrument and continuation | Project occupations on `S`; remove those sites and their incident hopping terms | Declared projective/free-evolution process |
| Conditional-state factorization | Negative sea plus outcome-dependent zero-sector occupation | Proved below by orthogonal fermion pairs |
| Cubic Bloch spectrum | All class subsets and all reduced-zone momenta, with the zero-energy node separately treated | Proved by integer Clifford algebra and rectangular singular values |
| Propagation | Exact propagator and supplied finite packet/local-source calculations | Algebra plus numerical checks on declared fixtures |
| Framework-level record/matter realization | One physical carrier implementing these operations and continued record production | Open physical target; outside the mathematical theorem |

The proof graph runs from polar decomposition and orthogonal occupied orbitals to measurement factorization; independently, Clifford anticommutation gives the cubic reduction condition and explicit spectrum. Both feed the propagation calculation. No terminal lemma is substituted for the full physical target.

## Conditional state and zero modes

Let the two sublattices each have `n` canonical fermion modes, denoted `a` and `b`. Define

\[
K=(QQ^\dagger)^{1/2}>0,\qquad U=K^{-1}Q.
\]

Then `U` is unitary and `Q=KU`. Change the second-sublattice mode basis to `b_tilde=U b`. The Hamiltonian in the `a,b_tilde` basis has the form

\[
h=\begin{pmatrix}0&K\\K&0\end{pmatrix}.
\]

Returning to physical coordinates `(a,b)`, its negative-energy occupied subspace has the orthonormal orbital matrix

\[
F=\frac1{\sqrt2}\begin{pmatrix}I\\-U^\dagger\end{pmatrix}.
\]

Individual columns of `F` need not be energy eigenvectors. Their complete span is the negative spectral subspace, because `K` is positive. Filling that span gives, up to a fixed fermionic ordering convention,

\[
|\Omega\rangle=\prod_{i=1}^n
\frac{a_i^\dagger-\widetilde b_i^\dagger}{\sqrt2}|0\rangle.
\]

Projecting the occupations `n_i` of modes `a_i` for `i` in `S` gives every binary pattern probability `2^{-|S|}`. In each measured pair an occupied `a_i` leaves its partner empty, while an empty `a_i` leaves its partner occupied. Thus the conditional unrecorded occupied space consists of the unmeasured pair orbitals together with the partner orbitals for which `n_i=0`.

Write `T` for the unmeasured first-sublattice sites and assume `[P_S,K]=0`. The Hamiltonian after deleting `S`, in the ordered basis `a_T,b_tilde_T,b_tilde_S`, is exactly

\[
h_R=\begin{pmatrix}
0&K_T&0\\K_T&0&0\\0&0&0
\end{pmatrix},\qquad K_T>0.
\]

In physical coordinates `(a_T,b)`, the same reduced Hamiltonian is `[[0,Q_T],[Q_T†,0]]`, where `Q_T` contains the rows indexed by `T`. In these physical coordinates the conditional state has the occupied projector

\[
C_{S,n}=P_-^{(R)}+
\sum_{i\in S}(1-n_i)|z_i\rangle\langle z_i|,
\qquad z_i=\begin{pmatrix}0_T\\U^\dagger e_i\end{pmatrix}.
\]

Here `P_-^(R)` is the **complete** negative-energy spectral projector of the reduced Hamiltonian. The `z_i` are orthonormal zero modes, perpendicular to it. In the earlier ordered tilde basis they are the corresponding unit vectors in the final `b_tilde_S` block; the factor `U†` belongs only to physical coordinates. In particular,

\[
[C_{S,n},h_R]=0,\quad
\operatorname{rank}(C_{S,n}-P_-^{(R)})=|S|-\sum_{i\in S}n_i.
\]

This is a factorization of the conditional state into the filled negative-energy sea and an explicitly specified zero-mode Slater state. This is an exterior-product factorization up to an overall fermionic-ordering sign. Observables confined to the nonzero-energy mode algebra have the same state for every record pattern. Physical site observables can mix the two sectors and can depend on the pattern. The partner modes `z_i` need not be local in the physical site basis.

The theorem includes `S` empty and `S` the entire first sublattice. The latter leaves only the second sublattice with zero Hamiltonian. The finite theorem assumes invertible `Q`; zero-energy modes in a chosen initial Hamiltonian require a separately supplied occupation prescription and are not covered by its unique negative-sea pairing argument.

## Cubic pi-flux specialization

Declare real nearest-neighbor hopping on cubic sites `x` with unit magnitude and signs

\[
\eta_1(x)=1,\quad\eta_2(x)=(-1)^{x_1},\quad
\eta_3(x)=(-1)^{x_1+x_2},\qquad h_{x,x+e_\mu}=-\eta_\mu(x).
\]

Use the period-two cell `x=2m+a`, `a` in `{0,1}^3`, and physical-position Bloch convention `exp(ik dot x)`. In the reduced zone the internal matrix is

\[
h(k)=-2\sum_{\mu=1}^3\cos(k_\mu)\Gamma_\mu,
\quad
\Gamma_1=X\otimes I\otimes I,\quad
\Gamma_2=Z\otimes X\otimes I,\quad
\Gamma_3=Z\otimes Z\otimes X.
\]

These integer matrices square to identity and anticommute in pairs. They flip the parity of `a_1+a_2+a_3`. Consequently

\[
h(k)^2=\epsilon(k)^2I_8,\qquad
\epsilon(k)=2\sqrt{\sum_\mu\cos^2(k_\mu)}.
\]

The even classes are `000,011,101,110`; the odd classes are `001,010,100,111`. Ordering by these classes writes `h(k)` with off-diagonal block `Q(k)` satisfying `Q(k)Q(k)†=epsilon(k)^2 I_4`. Complete class projectors are independent of momentum, so they reduce `K(k)=epsilon(k) I_4` wherever `epsilon>0`. This verifies the factorization hypothesis for finite periodic fixtures without a zero mode, and pointwise away from the node.

For the finite periodic fixtures, take even extents `L_mu=2N_mu` with the displayed real hopping signs also on wrap bonds. The allowed physical momenta are `k_mu=2 pi j_mu/L_mu`, represented modulo `pi` in the reduced zone. A zero node is present exactly when every extent is divisible by four. The spectral formula includes those tori; the conditional-state theorem on these untwisted tori requires at least one extent congruent to two modulo four. Twisted boundary conditions are not used in the numerical fixtures.

Remove any `r` of the four even classes. The remaining rectangular block `Q_R` has `4-r` orthogonal rows of squared norm `epsilon^2`. For `epsilon>0` the complete spectrum is

\[
\{+\epsilon\}^{4-r}\;\cup\;
\{-\epsilon\}^{4-r}\;\cup\;\{0\}^{r}.
\]

| Removed even classes | Live sites per cell | Multiplicity at each of `+epsilon` and `-epsilon` | Zero bands away from the node |
|---:|---:|---:|---:|
| 0 | 8 | 4 | 0 |
| 1 | 7 | 3 | 1 |
| 2 | 6 | 2 | 2 |
| 3 | 5 | 1 | 3 |
| 4 | 4 | 0 | 4 |

At the original node `epsilon=0`, the complete `(8-r)`-dimensional matrix is zero. This special case must be included separately in finite spectral counting. Near the node, `epsilon=2|q|+O(|q|^3)` for each surviving dispersive branch. The zero bands are additional low-energy spectral content, and are included in every count here.

For context, sublattice imbalance as a source of zero flat bands is established prior mathematics; no novelty claim is made for that rank principle. The framework-specific question investigated here is its conjunction with conditional sea factorization and the supplied formation geometry. [Ramachandran, Andreanov and Flach](https://arxiv.org/abs/1706.02294).

## Propagation between incomplete formation layers

The reduced matrix satisfies `h_R^3=epsilon^2 h_R`. For `epsilon>0` its exact propagator is

\[
e^{-ith_R}=I+\frac{\cos(\epsilon t)-1}{\epsilon^2}h_R^2
-i\frac{\sin(\epsilon t)}\epsilon h_R.
\]

At the node it is identity. The zero projector is `I-h_R^2/epsilon^2`. It annihilates any vector supported on a remaining even class. For `0 <= r < 4`, a supplied positive-band polarization can be chosen as

\[
\xi(k)=\frac1{\sqrt2}\begin{pmatrix}u\\Q_R^\dagger u/\epsilon\end{pmatrix},
\]

where `u` is any unit vector on remaining even classes. A packet in this band evolves with the unchanged phase `exp(-i epsilon t)` and has group velocity

\[
v_\mu(k)=\partial_{k_\mu}\epsilon
=-\frac{4\sin(k_\mu)\cos(k_\mu)}{\epsilon}.
\]

The physical-position Fourier factor includes `exp(ik dot a)` as well as the cell phase. The supplied Gaussian envelope uses `k_0=(pi/4,pi/4,pi/4)`, width `0.20`, and centering phase `exp[-ik dot (2m_0+a_source)]`; the source internal position makes the relative cell-gauge polarization periodic across the reduced-zone seam. Exact zero-node fibers are assigned zero envelope because a positive-band polarization is undefined there. The numerical calculation reports finite periodic-position errors against the analytically calculated, envelope-averaged velocity, without fitting a velocity. The conditioned sea itself is stationary; these packets are separately supplied excitations.

For `r < 4` each such layer therefore leaves explicitly calculable dispersive dynamics in this supplied model. At `r=4`, all remaining odd modes have zero Hamiltonian and there is no positive-band packet. Further layers change the live Hamiltonian; a sequence that eventually records every class has a different endpoint from a fixed incomplete layer. The many-event, spatially local continuation problem remains a subsequent physical target.

## Finite record-law error lemma

The earlier finite pilot also admits a self-contained statement useful for future asynchronous tests. Fix a finite, outcome-independent sequence of shared-basis projective records that ultimately resolves the full basis, and between-event Hamiltonians `H_j` commuting with all earlier record projectors. Its final branch probabilities can be represented as

\[
p_z(\tau)=|[e^{-i\tau H_m}\cdots e^{-i\tau H_1}\psi]_z|^2.
\]

If one diagonal basis phase makes all `H_j` and the initial vector real, complex conjugation makes each probability even in `tau`; mutual commutation of the `H_j` is unnecessary. Put `B=sum_j ||H_j||` and `q=p''(0)/2`. The product rule and Cauchy-Schwarz give `||p''||_1<=4B^2` and `||p''''||_1<=16B^4`, hence

\[
\operatorname{TV}(p(\tau),p(0))\le\min(1,B^2\tau^2),\qquad
\tfrac12\|p(\tau)-p(0)-\tau^2q\|_1\le B^4\tau^4/3.
\]

The bounds concern a finite final record distribution. They grow with the supplied schedule and do not themselves bound the live matter response. The partial-layer calculation above supplies that distinct observable question. The previous pilot's numerical edge-qubit coefficients are not inputs to this note.

## Execution and review record

The primary runner reports **17 PASS, 0 FAIL**; the independent checker reports **13 PASS, 0 FAIL**. Their content-bound execution receipts are [primary cache](../logs/runner-cache/record_formation_partial_class_dispersion_2026_09_04.txt) and [independent cache](../logs/runner-cache/record_formation_partial_class_dispersion_independent_check_2026_09_04.txt).

The primary checks exact integer Clifford identities; all 16 class subsets at five momenta; full real-space/Bloch spectral agreement on periodic cubes of side 4, 6 and 8; all 81 subset/outcome cases on an open cube; and three specified patterns on a 27-site recorded class of a node-free side-6 torus. The side-6 polar kernel is non-flat. A single-site control has commutator norm about `0.205`, explicitly distinguishing it from a complete-class projector. The side-6 pattern check is not an enumeration of all `2^27` outcomes.

The independent implementation builds physical-coordinate nearest-neighbor bonds directly and conditions explicit 256-component fermionic Fock states on the open cube. Across all 81 cases, probability error is below `4e-16`, covariance/projector and stationarity residuals below `3e-15`. Full torus spectral error is below `3e-14`. Mutation controls reject incorrect hopping signs, omitted zero bands, incorrect fermionic reordering and transposed complex covariance. An independent local-source probe on the side-6, one-class-deleted torus has negligible zero-sector weight and nonzero probability away from its source at supplied times `0.2`, `0.5`, and `1`.

For the positive-band packet, the largest two-tick displacement discrepancy in Euclidean norm across `r=0,1,2,3` decreases from about `0.254` to `0.00118` to `9.46e-7` on `8^3`, `12^3`, and `16^3` period-two cells. The largest wrap probability decreases from `0.0623` to `0.000717` to `1.68e-6`. These are finite diagnostics, not asymptotic error bounds; the coarse fixture has appreciable wrap error. Packet norms agree within `2e-12`; zero-sector weights are below `1e-24`.

The primary/checker pairing uses separate contexts of the same model family and distinct construction paths. The checker did not read the primary implementation before completing its independent construction. The supervisor reviewed every line and corrected a commutator diagnostic, packet phase convention and covariance-index convention before the recorded runs. A separate proof review found and prompted explicit physical/rotated-basis labels, the `r<4` propagation restriction, and finite-torus node conditions. These are author-side checks; no effective audit grade is assigned.

The prior-art sweep at main `a1a64d36bc856c3ae330786972d3f2a02b678c52` found the unreduced Clifford spectrum already on main and conditional-subspace/stationarity criteria in prior formation work. The distinct scope here is the explicit polar formula for the complete conditional sea and zero sector, combined with the class-deleted spectrum and supplied propagation probes. There is no general novelty claim for sublattice-imbalance flat bands.

## Status and trace certificate

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
conditional_surface_status: supplied invertible free-fermion Hamiltonian and occupation instrument
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: exact finite conditional-state algebra and cubic spectral specialization on explicitly stated hypotheses; framework realization remains open
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: test the physical edge-qubit star-record instrument against the remaining conditional ground space, then construct continued local formation with live matter
```
