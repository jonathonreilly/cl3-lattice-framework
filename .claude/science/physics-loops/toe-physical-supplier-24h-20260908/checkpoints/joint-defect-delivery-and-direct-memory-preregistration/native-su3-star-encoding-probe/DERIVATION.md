# A six-edge Clifford encoding: constructive local algebra, failed native gauge continuation

Work on the full native edge-qubit carrier. Fix a vertex and order its six incident edge operators A1,...,A6 into three declared pairs. Each Ai is a Hermitian involution and distinct incident operators anticommute. This is an exact Cl6 representation; its complex algebra is Mat8, represented with a multiplicity factor in the full carrier. The choice of pairs/colour labels is supplied, not selected by the native Hamiltonian.

Define f_a=(A_(2a-1)+i A_(2a))/2, a=1,2,3. They satisfy exact CAR. The operators G(T)=sum_ab f_a† T_ab f_b for traceless Hermitian3x3 T obey the su3 commutator algebra. They are native even Clifford bilinears (the trace constant cancels). Let n=sum f†f and P=n(3-n)/2. Then P is the rank-six projector per irreducible spinor copy onto n=1 or2, excluding vacuum and full occupation. No original ice/low-charge/electric interpretation is assigned to this new n.

## Exact representation and its mismatch with the new-main rishon

Choose |a>=f_a†|0> and |bar a>=(1/2)sum_bc epsilon_abc f_b†f_c†|0>. In increasing occupation order these have phases |bar1>=|23>, |bar2>=-|13>, |bar3>=|12>. Direct CAR gives

    G(T)|_(n=1)=T,       G(T)|_(n=2)=-T^T.

Thus the selected six-dimensional representation is3⊕bar3. Its centre acts as omega on n=1 and omega² on n=2. The new-main one-rishon link instead has endpoint basis |i,a>,|j,a> and two independent endpoint su3 actions E_i(T)=diag(T,0), E_j(T)=diag(0,T). Under their diagonal subgroup it is3⊕3, with centre omega I6. There is no unitary intertwiner between this diagonal action and the single native bilinear G(T) action: their central spectra differ. At one endpoint alone the supplied link is3⊕three singlets, also not3⊕bar3. Calling the spinor subspace that same rishon without changing generators would be incorrect.

A precise supplied local encoding of the six-state *link algebra* nevertheless exists if higher-degree projected operators are allowed. Let P1,P2 be the spectral projectors of n onto1,2. Under |i,a>→|a>, |j,a>→|bar a>, define

    E_i(T)=P1 G(T) P1,
    E_j(T)=P2 G(-T^T) P2,
    U^{ab}=-|bar b><a|.

The outer-conjugated argument on P2 makes its matrix exactly T, and the disjoint blocks commute. The nilpotent U matrix units can be written explicitly in CAR:

    U^{ab}=-(1/2)sum_cd epsilon_bcd f_c† f_d† P0 f_a,
    P0=product_a(1-f_a†f_a).

They obey U^{ab}U^{cd}=0 and the same finite endpoint covariance as the supplied link. These are exact projected polynomials in the six native A's, with an explicit phase dictionary. They are not the original eight bilinear G generators, not native single-edge hopping, and not an enforced physical six-state role. This construction only prices a local algebraic encoding; no physical preparation or dynamics is supplied by it.

## The original native Hamiltonian does not preserve P

Write B_a=i A_(2a-1)A_(2a), so n=(3+sum B_a)/2 and

    P=3I/4-(B1B2+B1B3+B2B3)/4.

Thus P has only the identity and four-star-edge toggle masks. A nonzero real star term h=sum_r lambda_r A_r leaks between n=0,3 and n=1,2: h|0> is a nonzero one-particle vector for every nonzero real coefficient vector. Therefore [P,h]≠0. Equivalently each commutator term has a distinct three-star-edge toggle mask, so the nonzero coefficients cannot cancel.

This survives in the actual full uniform hopping Hamiltonian H_U=UD+g sum_e lambda_e A_e when any star coefficient is nonzero. Terms from edges outside the star, when commuted with P, have a toggle mask including that outside edge, hence cannot cancel the three-star-edge components. D is diagonal in the actual edge occupation basis; [D,P] has four-star-edge masks and likewise cannot cancel them. Distinct toggle masks are linearly independent operator sectors on the full ambient edge space. Consequently the selected six-state subspace is not invariant under the original H_U for nonzero uniform hopping. Projecting the Hamiltonian or adding a penalty would be new supplied dynamics. Relaxing an old fixed-cycle code does not repair this separate noninvariance.

## Spatial gauge commutation: adjacent centres commute, but distance-two centres fail

Even star Clifford bilinears at nearest-neighbour vertices commute on a triangle-free cubic graph. If both terms contain the shared edge, their remaining edges are disjoint, and the two anticommutations cancel. If only one contains it, that shared edge anticommutes with both edges of the other bilinear, again giving even parity. If neither contains it, no endpoint is shared. Therefore the bilinear su3 algebras at adjacent centres do commute. This is a useful exact positive observation, not enough for a vertex gauge family.

At distinct centres separated by two steps, the algebras need not commute. On L=6 take v=(0,0,0), w=(2,0,0), pair each vertex's +/-x, +/-y, +/-z edges, and take its Cartan generator n_x-n_y. The x bilinear at v and the x bilinear at w each has an edge incident at (1,0,0); exactly one cross edge pair meets. All other cross pairings in those two Cartans have no shared endpoints. The two x bilinears anticommute, so the Cartan commutator is nonzero, with a unique four-edge toggle support. No cross-term cancellation occurs. Thus [G_v,G_w]=0 for all distinct vertices—the required local gauge condition—fails for this proposed star assignment. A claim only about nearest neighbours would miss the obstruction.

This counterexample concerns the actual chosen star encoding, not all encoded SU3 constructions. The adjusted endpoint operators above also have no proved mutually commuting global vertex realization, and their selected sectors are not proved simultaneously enforceable. The exact local Clifford/representation bridge is valid; a native gauge theory with these roles and the original dynamics is not obtained.

## Consequence for the queue

The useful result is an explicit native polynomial realization of one supplied six-state algebra, with pairing, projector, phase and outer-conjugation choices exposed. The decisive missing steps are simultaneous spatial gauge locality and invariant/enforced subspaces under declared dynamics. Enlarging a matrix census or identifying triality with the old native signed defect would not close either gap. No generic SU3 no-go, colour selection, formation law or confinement statement follows.
