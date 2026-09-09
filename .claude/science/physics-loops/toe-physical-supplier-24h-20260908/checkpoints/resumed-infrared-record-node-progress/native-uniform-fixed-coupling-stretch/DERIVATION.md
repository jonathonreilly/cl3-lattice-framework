# Fixed-coupling local control and an exact all-ground-state reduction

Research stretch, no physical computation or publication. Uses supplied uniform full native H_U=H0+UD, D=3N/2+V, and H0>=E0+kappa K with commuting bad-face projectors. Canonical uniform stiffness applies on L=4M,M>=32. No active gap is assumed. This document distinguishes an actual symmetric-state consequence from an unproved relative-susceptibility estimate sufficient for every ground state.

## 1. Actual symmetric ground-state local control

The density parent proves, for every finite-volume ground density matrix,

 <K>/N <= min(3,3x/2,75x²), x=U/kappa.

It does not explicitly state the following symmetry consequence. The uniform native Hamiltonian has a face-transitive physical action of the cubic graph automorphisms. Here is a representation-level justification rather than an assumption of bare edge permutation symmetry. Write positive native edge operators A_e=X_e Z^{w_e}. For an edge permutation g induced by a graph automorphism, the difference between the permuted ordered-star rows and the target rows is a symmetric binary matrix with zero diagonal: both row systems have commutation matrix equal to edge incidence adjacency, and neither uses its own edge. A diagonal product of controlled-Z gates realizes this row difference. Composing it with the edge permutation gives a unitary U_g with U_g A_e U_g*=A_{g(e)} and U_g Z_e U_g*=Z_{g(e)}. Thus it preserves sum A and D. No coherent-state invariance under a bare permutation is asserted.

Elementary central face operators map to their geometric images up to a sign. Their GOOD signs are also preserved: otherwise a transformed H0 ground state would have a bad face, contradicting H0>=E0+kappa K and the existence of an H0 ground state. Therefore U_g P_f U_g*=P_{g(f)}. Potential projective composition phases of U_g do not affect the conjugation average; equivalently average over the finite induced automorphism action on the finite-dimensional operator algebra.

Symmetrize any ground density matrix over that action. The result rho_U^sym is still a ground state and every face has the same probability, hence

 Tr rho_U^sym P_f <= b(x):=min(1,x/2,25x²).

For a fixed finite face set C, define good projector G_C=product_{f in C}(1-P_f). Since the projectors commute,

 1-Tr rho_U^sym G_C <= |C| b(x).

This is a union bound on any-defect probability, not an exponential bound on simultaneous defects. If delta=|C|b(x)<1, the normalized locally projected state sigma=G_C rho G_C/Tr(rho G_C) has all these faces good and satisfies ||rho-sigma||_1<=2 sqrt(delta). A purification proof gives that bound: project the purification, whose normalized overlap is sqrt(1-delta), then take partial trace. Thus for any bounded observable A,

 |Tr rho A-Tr sigma A| <=2||A|| sqrt(|C|b(x)).

For a fixed local algebra containing the face supports this gives O(U/kappa) proximity to some locally defect-free state at a coupling interval independent of N. It does NOT identify that state with the canonical vacuum, guarantee uniqueness, or constrain every symmetry-breaking ground state.

Weak-star subsequences of these finite symmetric ground states give infinite-volume ground states of the supplied finite-range interaction, using local commutator positivity. The bounds pass for fixed local projectors/observables. This is existence of symmetry-invariant locally low-defect ground states at fixed U, not the missing all-ground-state theorem. No inference of contour tails from a mean density is made.

## 2. Exact variational reduction for ALL ground states

Fix one face f and 0<s<kappa. Define the local-defect chemical-potential perturbation

 H(U,s)=H0+U V-s P_f,
 E(U,s)=min spec H(U,s),
 Delta(U,s)=E(U,0)-E(U,s)>=0.

The scalar3NU/2 is suppressed and cancels. For ANY ground density matrix rho of H(U,0), its trial energy in H(U,s) gives

 s Tr rho P_f <= Delta(U,s).

This elementary inequality controls all degenerate ground states, not only a Gibbs-selected mixture. At U=0, H0-sP_f>=E0+(kappa-s)P_f+kappa sum_{h!=f}P_h, while an H0 ground state has P_f=0. Hence E(0,s)=E0 and Delta(0,s)=0. The first derivative in U at zero also vanishes for these zero-face ground states because V changes face labels; no ground-space V block remains. A local perturbation bound of the form

 Delta(U,s) <= C s (U/kappa)²

for ONE fixed s, e.g. s=kappa/2, is therefore sufficient for the desired all-ground-state local density bound. It is a relative impurity-energy estimate: extensive vacuum-energy terms cancel BEFORE bounding anything. This avoids the 1/N defect-compression step exactly.

## 3. A concrete connected correlation estimate that would supply it

For finite beta and volume set F_beta(U,s)=-beta^-1 log Tr exp[-beta H(U,s)]. Let

 Chi_beta(U,s)= integral_0^beta <V(tau);V(0)>_{U,s} d tau,

where the connected thermal imaginary-time covariance is defined by the Duhamel derivative. No commutation or positivity of individual spatial contributions is assumed. Exact finite-dimensional differentiation gives partial_U² F_beta=-Chi_beta. With Delta_beta=F_beta(U,0)-F_beta(U,s),

 partial_U² Delta_beta=Chi_beta(U,s)-Chi_beta(U,0).

At U=0, partial_U Delta_beta=0 exactly: both H(0,s) Gibbs operators commute with all faces and V changes their labels. Taylor's integral identity is therefore

 Delta_beta(U,s)=Delta_beta(0,s)+integral_0^U (U-u)[Chi_beta(u,s)-Chi_beta(u,0)]du.

If for 0<=u<=U*, and a fixed s=kappa/2, uniformly in L and all sufficiently large beta,

 Chi_beta(u,s)-Chi_beta(u,0) <= 2 C s/kappa²,

then beta->infinity at each finite L removes Delta_beta(0,s), and gives Delta(U,s)<=C s(U/kappa)², hence p_f<=C(U/kappa)² for EVERY ground state and fixed U<=U*. An absolute bound would suffice but is stronger than necessary. Uniformity in beta is only required for the susceptibility difference, not for an individual extensive susceptibility. This is a precise remaining estimate, not an asserted consequence of quasilocality.

Equivalently one may interpolate s and bound the connected impurity derivative partial_s Chi. It is the spacetime integral of a connected Pf,V,V Duhamel three-point function, including all spatial sums of the electric insertions. Its sign need not be fixed. Establishing a convergent operator-valued/resummed representation for this RELATIVE quantity is a concrete target: disconnected volume terms have already canceled algebraically.

## 4. What the new star results contribute, and what they do not

PR8062/8063 give a quasilocal vacuum creator for one zero-flux star return, a smooth unprojected coefficient symbol, and row-l2 control of its one-particle inverse channel. They give neither the above interacting Duhamel difference at u>0 nor the full operator-valued star return on arbitrary excited states. The local impurity sPf changes the flux penalties but not the reference vacuum at u=0; choosing s<=kappa/2 retains a wrong-face lower bound at least kappa/2 per affected count at that endpoint. This makes an impurity-uniform endpoint expansion plausible without changing its physical reference. It does not justify expanding at arbitrary u without resummation.

The all-order susceptibility-difference estimate is now the sharp remaining task. It is weaker and better localized than bounding all absolute histories or requiring a uniform active gap. The symmetric-state consequence in section1 is established independently of it; the all-ground-state result in sections2–3 is conditional on this explicit operator correlation estimate.

## 5. The relative endpoint curvature has an explicit local bound

The susceptibility target is not arbitrary: its zero-temperature endpoint has an independently controlled local second-order bound. Let P be the complete H0 ground projection. The same P is the H(0,s) ground projection for s<kappa. First-order PVP vanishes. The second-order effective operators on P are

 T_s=-(1/4) sum_j P W_j (H0-E0-sP_f)^(-1) W_j P,

where each inverse is restricted to that pair's nonempty flux sector. Cross j,k terms vanish for j!=k because their exact face labels differ. This is an operator identity on the full degenerate ground space; no spectator state is selected. Terms not flipping f are identical for s and0. On an affected sector of size m, Pf=I and A=H0-E0>=kappa m. Resolvent monotonicity gives

 0 <= (A-s)^(-1)-A^(-1) <= s/[kappa m(kappa m-s)] I.

Therefore 0<=T_0-T_s<=s C(s)P, with

 C(s)=(1/4)[24/(6kappa(6kappa-s))+8/(8kappa(8kappa-s))].

The minimum-eigenvalue variational inequality, valid even when T0 andTs do not commute, implies

 0<=lim_{U->0+} Delta(U,s)/U²<=s C(s).

For s=kappa/2, C(s)=71/(330kappa²); as s decreases to0, C(s)->19/(96kappa²). This is a direct local bound on the second-order relative energy and checks the constants and signs of the proposed response route. It is uniform as a coefficient only. Higher derivatives/remainders and the beta-uniform interacting susceptibility difference are not controlled by this computation.

## 6. Uniform leading joint-event coefficients: an additional exact consequence

There is a useful extension of the local quadratic coefficient to every fixed finite C, still with the order U->0 FIRST. Put m=|C| and r=ceil(m/8). For a finite analytic normalized ground branch write psi(U)=sum_n U^n psi_n. Because each V term toggles at most eight faces, psi_n is supported on face patterns with at most8n bad faces. H0 resolvents and energy counterterms preserve labels, and arbitrary ground-space tangent terms have zero bad faces. Consequently Q_C psi_n=0 for n<r.

At order r, any contributing chain must contain exactly r actual pair insertions. Terms involving an energy counterterm or a higher-order initial ground-space coefficient have fewer pair insertions and cannot cover C. After k insertions, a contributing face pattern has at least m-8(r-k)>0 bad faces: the remaining r-k insertions could add at most8(r-k) of C's required faces. Hence every contributing proper intermediate inverse acts in a strictly wrong-face sector, never in the gapless zero-face sector. Its norm is bounded by

 1/[kappa (m-8(r-k))], k=1,...,r.

Moreover every insertion in such a minimal chain must affect at least one face of C. If one did not, the other r-1 could cover at most8(r-1)<m of C. There are at most32m incident pairs touching C (the exact24+8 count per face, with overcount allowed). This makes the entire leading coefficient a FINITE local sum, without any sum over remote vacuum loops. Triangle inequality therefore gives

 ||Q_C psi_r|| <= (16m)^r / [kappa^r product_{j=0}^{r-1}(m-8j)],

 limsup_{U->0+} p(C)/U^(2r)
 <= (16m)^(2r) / [kappa^(2r) product_{j=0}^{r-1}(m-8j)^2].

The r inverse signs do not affect this upper bound. The same coefficient bound holds over the finite-volume ground branches and their arbitrary mixtures. For r=1 the sharper exact flux-label orthogonality from the prior theorem should be used instead. This construction proves a volume-independent LEADING joint-event coefficient and confirms that the earliest nonzero term has no infrared return problem. It does not control the remainder or fixed-U contour probabilities. The genuinely difficult remote/zero-return contributions enter at later orders; section3's relative-impurity resummation is still needed for a fixed-U all-ground-state result.
