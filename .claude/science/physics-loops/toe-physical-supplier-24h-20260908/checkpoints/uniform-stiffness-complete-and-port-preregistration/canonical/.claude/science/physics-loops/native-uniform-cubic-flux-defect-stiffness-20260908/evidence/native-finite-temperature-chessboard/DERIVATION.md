# Native annealed reflection positivity and joint defect events

Status: new independent proof candidate, frozen for hard review. Theory only. Supplied uniform U=0 native model, even cubic extents divisible by four, nonzero hopping, exact native/active dictionary, and a uniform fixed-orbit free-energy penalty kappa*k are premises. The last premise remains conditional on the ground-density certificate and temperature/size conditions in the previous finite-temperature packet. No nonzero-U or physical phase claim.

## 1. Why pointwise Cauchy–Schwarz is insufficient

A bound w(l,r)<=sqrt(w(l,l)w(r,r)) alone does not establish positivity of the matrix w, nor a normalized annealed event inequality. Summing that bound produces sums of square roots. The square-root identity between native and auxiliary weights does not solve this problem. Instead we prove positivity directly for the active Majorana trace, then use the exact constant spectator factor.

## 2. Fixing the crossing matching

Take a coordinate reflection between sites, including both opposite cut planes. Half width is at least two. Every boundary vertex belongs to exactly one crossing edge: the crossing edges form a matching. Let its size be c. For each assignment of its signs, use a vertex sign gauge on one endpoint of each matching edge to set every cross term to -i t gamma_L gamma_R, t>0. This is possible independently for all c edges. It bijectively relabels the internal link signs in each half and preserves all gauge-invariant face events wholly within a half.

Consequently the sum over all link fields of such half-factorized events equals 2^c times the sum with fixed crossing signs. There is no discarded flux or winding. Passing from all link fields to gauge orbits divides every sum by the same 2^(N-1), since the connected graph's vertex-gauge action has only the constant-sign kernel. These factors cancel in probabilities. No gauge fixing to a spanning tree is needed.

## 3. Direct active-Majorana positive kernel

Each half has N/2 Majoranas, an even number. Represent left Majoranas by alpha_j tensor I, and right Majoranas by P_L tensor conjugate(alpha_j), after reflecting the right coordinates. Here P_L is left fermion parity. The right reflected internal Hamiltonian is the complex conjugate of the left one. This incorporates the magnetic reflection's reversal of the imaginary hopping coefficient; returning to link coordinates gives canonical crossing fluxes, as in the source dictionary.

For arbitrary left internal field l and right reflected field r, apply a Lie–Trotter product to the internal Hamiltonians and the cross matching. For a time slice of size dt each cross exponential is

    exp(i dt t alpha_j P_L tensor conjugate(alpha_j))
      = cosh(dt t) I + i sinh(dt t) alpha_j P_L tensor conjugate(alpha_j).

The crossing bilinears commute because their endpoints are disjoint; hence each slice expands exactly over subsets, with positive real cosh/sinh weights. A complete expansion history with m selected cross factors has left product containing m parity operators. Move these parities to its right through the odd alpha factors; all internal exponentials are even and commute with parity. The sign is (-1)^(m(m-1)/2). If m is odd, the left trace vanishes by parity, including its final P_L. If m=2k, P_L^m=I and

    i^m (-1)^(m(m-1)/2)=1.

The right trace is the complex conjugate of the corresponding left word evaluated at r, with the same ordered internal exponentials and alpha insertions. Thus at every Trotter depth the kernel is a sum of positive weights times f_history(l) conjugate(f_history(r)). It is positive semidefinite. The finite-dimensional Trotter limit preserves positivity. The spectator factor 2^(N/2-1) is positive and independent of l,r, so the native kernel has the same property. Active zero modes cause no exception.

This gives reflection positivity for arbitrary complex gauge-invariant functions of the internal half-link fields. In particular Cauchy–Schwarz applies after summing those fields, with the exact crossing multiplicity from Section 2. This is a proof of native annealed positivity, not an entrywise-square-root inference.

## 4. Cube-event chessboard estimate

Use the disjoint two-site cubes and the twisted 32-label alphabet of the earlier compatible dissemination proof. Add a wildcard label meaning no condition. For any cube-label assignment let P(q_b) be its normalized native Gibbs event probability. These probabilities are strictly positive for compatible assignments. Reflection positivity gives

    P(q_b)^2 <= P(q_b^+) P(q_b^-).

The normalization is the same full partition function in all three probabilities. Setting f=-log P converts this to exactly the half-reflection inequality used by the finite longest-run chessboard lemma. The wildcard transforms to itself. Applying that finite-alphabet lemma in three directions, with eta_b=(product rho_a^b_a)q_b, gives

    P(q_b) <= product_b P(disseminated eta_b)^(1/B),  B=N/8.

The wildcard disseminated event has probability one. This proof works for arbitrary even block counts; no power-of-two size assumption is introduced. The magnetic reflection exchanges opposite cube faces exactly as before.

## 5. Explicit entropy price and joint defects

Assume each orbit s satisfies F_native(s)-F_native(pi)>=kappa*k(s), kappa>0. A fully disseminated noncanonical cube label q forces B*m(q) defective faces, m(q)>=2. Its internal constraints are five independent cycle constraints per disjoint cube. In the full cycle space of dimension E-N+1=2N+1, they are independent because their internal edges are disjoint. Therefore exactly 2^(2N+1-5B)=2^(11B+1) link gauge orbits realize this label pattern, including all windings and crossing fields.

Since Z_total>=Z_pi,

    P(disseminated q) <= 2^(11B+1) exp(-beta*kappa*B*m(q)).

For any k distinct cubes required to be bad in a fixed partition, sum the chessboard estimate over their 31 noncanonical labels. Thus

    P(all k cubes bad) <= p^k,
    p = min(1,31*2^(11+1/B)*exp(-2 beta kappa)).

When the displayed untruncated factor is below one, this is a joint-event suppression estimate. It retains the explicit gauge/cross-link entropy, and does not pretend the fluxes are independent.

For any prescribed set of m distinct defective elementary faces, one of the eight partitions contains at least m/4 of those faces internally (each face is internal in two partitions). Each cube contains at most six. Hence at least m/24 distinct cubes of that partition must be bad, and

    P(all prescribed m faces defective) <= p^(m/24).

Integer ceilings can strengthen this bound. The partition is selected from the prescribed set, independently of the random configuration.

## 6. Contours and scope

Dual edges corresponding to defective plaquettes form an even-degree graph by cube Bianchi. To obtain a conservative unconditioned connected-set bound, the number of connected m-edge dual sets containing a fixed vertex is at most 6^(2m)=36^m: choose a deterministic doubled-edge traversal of length 2m and encode its six-valued steps. Therefore, if a=36*p^(1/24)<1,

    P(exists a connected defective dual set containing v with size >=ell)
       <= sum_(m>=ell) a^m = a^ell/(1-a).

Finite-volume sums only improve this bound. Winding components are included as connected sets, but pure magnetic winding changes without plaquette defects are not. This is an unconditioned joint-defect/connected-set bound. It is not a uniform exterior-conditioned DLR comparison, a uniqueness theorem, a confinement/deconfinement theorem, or a nonzero-electric stability result. The deliberately large entropy threshold is merely sufficient.

The new load-bearing step is Section 3's native Majorana trace positivity. The old objective inequality alone would not license Sections 4–6. All Hamiltonian and thermal ensemble choices remain supplied.
