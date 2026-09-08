# An energy-dependent three-insertion native vertex

Status: independent structural derivation, pending review. No new physical linear solve, spectrum or integral. Sources read: native-zero-penalty-sixth-spectator-coefficient/DESIGN.md, native-l6-sixth-factorization/DERIVATION.md, native-sixth-full-operator-support-root/DERIVATION.md and the local native Gauss convention recorded there. The exact Hamiltonian and isolated canonical flux orbit are supplied. This is not a globally gapped all-active Schrieffer–Wolff block.

## Energy-window Feshbach formulation

Let P denote the full canonical-flux physical sector, retaining all active states and spectators. Let Q contain the other flux sectors. Subtract the scalar first-order piece of D and write the remaining perturbation as V=(1/2)sum Z_e Z_f over distinct incident edge pairs. At U=0 let E0 be the canonical ground energy and Delta_flux the positive finite-volume separation to the lowest other-flux energy. For real z<E0+Delta_flux,

    R_Q(z)=(z-QH0Q)^(-1)

exists, even though the spectra of PH0P and QH0Q overlap at high energies. The Feshbach operator is

    P(H0+uV)P + u^2 PVQ[z-Q(H0+uV)Q]^(-1)QVP.

Its expansion is norm-convergent when |u| ||QVQ|| < E0+Delta_flux-z. This is a finite global sufficient window, not uniform in volume. Retaining all active states in P is therefore legitimate for this energy-dependent resolvent description, without claiming a block spectral gap or an energy-independent local SW theorem.

## Exact third-order star operator

A three-insertion word toggles at most six edges. On the stated cubic geometry its only nonempty returning cut is a singleton star. Zero-toggle returning words also exist and contribute a separate even-active, spectator-scalar part of Sigma_3; the following formula isolates the singleton vertex and does not discard that part. Each of the star's six edges occurs once, and all three pairs are centered at that vertex: neighboring outer endpoints are mutually nonadjacent, so they do not provide other pairings. There are15 partitions into three pairs and6 orders, hence90 words. No nonempty prefix of one or two such pairs is a gauge cut. All their resolvents belong to Q.

Fix a vertex v and write A,C for disjoint two-edge subsets of its six incident edges; the remaining two edges form the middle insertion. Let H_A be the active Hamiltonian with the two links in A reversed, and R_A(z)=(z-H_A)^(-1), with the unchanged-bath energy included. The Gauss closure is the native parity operator

    P_v = -i gamma_v beta_v.

This sign uses beta=i(c†-c), so P_v=1-2n_v. A convention using the negative beta changes the displayed sign, not the physical operator.

Complementing a star toggles its vertex gauge, hence H_(star\C)=gamma_v H_C gamma_v and R_(star\C)=gamma_v R_C gamma_v. Closing the three-link-pair word back into the canonical representative therefore gives exactly

    Sigma_3,v(z) = -i O_v(z) beta_v,
    O_v(z) = (1/8) sum_(A,C disjoint pairs) R_C(z) gamma_v R_A(z).       (1)

There are90 summands in (1). This follows directly from the chronological prefix product R_(A union B) R_A and the final Gauss closure; it does not replace native A/B phases by bare link flips. Spectators commute with every even resolvent. Since A,C exchange permutes the sum and the resolvents are Hermitian for real z below the Q spectrum, O_v is Hermitian and odd. Therefore -i O_v beta_v is Hermitian and preserves physical total parity.

Equation (1) is an actual order-u^3 active/spectator vertex in the energy-dependent Feshbach operator. It is not generally a quadratic hybridization m gamma_v beta_v: an inverse many-body quadratic Hamiltonian is not itself quadratic or Gaussian, and products in (1) may contain odd Clifford degrees beyond one. No claim that those terms cancel is made.

## Vacuum transition state and a smaller computational target

The physically relevant transition state is chi_v=O_v(E0)|Omega>. It has odd active parity. Decompose it into one-, three-, five-, ... quasiparticle sectors of canonical H0. The one-particle amplitudes <a|chi_v> define the linear vertex seen from the vacuum; they do not establish equality of O_v to that linear operator on all active states.

Equation (1) allows30 resolvent applications instead of90 two-step words: first compute x_A=R_A|Omega> for all15 pairs; for each C form b_C=gamma_v sum_(A disjoint C)x_A (six terms) and compute y_C=R_C b_C. Then chi_v=(1/8)sum_C y_C. First solves have even active parity, second odd parity. Each H_C is a genuinely wrong flux, so its all-parity energy gap applies; singleton-cut zero vacuum denominators have been removed by the exact gauge conversion. The support is the one-star endpoint-generated invariant active space, with its unchanged bath vacuum offset. On the reviewed L4 flat problem that space has12 real Majoranas, so each solve can use a32-dimensional parity block. No such solves were executed here. A future L6 dimension/cost must be derived separately, not inherited from L4.

This is a concrete lower-cost target: certify chi_v and its particle-number weights, including whether the one-particle part is nonzero and whether the multiparticle remainder is small. Until measured/certified, neither property is asserted. It may illuminate the infrared structure without computing every sixth-order word, but it does not replace the full coefficient calculation.

## What integrating the retained active sector reproduces

At E0, the singleton-middle contribution to the vacuum effective operator is the second-order elimination of the third-order vertices through the odd active excited sector:

    P0 Sigma_3 R_active,exc Sigma_3 P0,
    R_active,exc=(E0-H0)^(-1) on odd active states.

All signs are retained by this operator expression. Its diagonal quadratic form is negative semidefinite, but an individual spectator bilinear extracted from cross terms need not have a definite sign. For the full sum of vertex-created states, the spectral decomposition weights an odd excitation of energy E_a-E0 by its negative reciprocal. On L4 these denominators are n*sqrt24|t| for odd n; the one-particle channel has the smallest denominator. On a general finite torus they are sums of canonical positive frequencies. A bound by inverse minimum active gap is available, but divergence of that bound does not prove a divergent amplitude; the numerator can vanish or scale with the gap.

For two disjoint six-edge stars, each fixed six-pair set has720 orders. Exactly72 have a complete star as the first three insertions (2*3!*3!), while648 have mixed middle flux. Thus the vertex integration accounts for the singleton-middle family and does not account for the mixed-middle sixth-order Feshbach self-energy. The latter must be retained, along with the standard canonical normalization/folded analysis when changing from the energy-dependent operator to the canonical vacuum effective Hamiltonian. The reviewed scalar-through-five theorem licenses the nonscalar raw-chain identification only after that analysis; it does not license discarding648 orders.

## Diagnostic dispersion, not a proved native replacement

If an independently justified quadratic approximation had active/spectator skew block [[K,mI],[-mI,0]], a singular active frequency omega would yield frequencies (sqrt(omega^2+4m^2)±omega)/2. Thus the small branch is approximately m^2/omega at fixed positive omega and |m| at omega=0. Taking m proportional u^3 would suggest u^6 versus u^3 scales. This is an exactly solvable diagnostic matrix only. The actual O_v(z), its momentum dependence, higher odd components, mixed-middle terms, energy dependence and error control have not been replaced by this ansatz. No Dirac mass, thermodynamic gap, resonance-free all-active block or phase follows.
