# Root selected infinite-volume charged GNS sector

Prospectively contracted before the completed proof. Primary was given the proposed GNS/resolvent route but not this completed derivation; independent proof work is underway. This result imports the neutral thermodynamic ground/GNS dynamics construction and uses block38's uniform finite-volume charged inequality. It defines an energetic charged sector in that selected representation. It does NOT identify its bottom with an unproved limit of finite-volume charged minima.

## Fixed interaction and imported limit

Fix a>0 and v>=0 in block38's sufficiently small regime on the whole infinite cubic lattice, with every elementary plaquette and the supplied compact SU3 link Hilbert spaces. Group three outgoing links per cell. Use the exact finite family in Yarotsky, arXiv:math-ph/0411042: all onsite electric terms in the finite cell set, and precisely those whole interaction-range groups whose support is contained in that set. The interactions are restrictions of ONE fixed infinite interaction. Do not apply its thermodynamic theorem to arbitrary volume-dependent couplings.

The source's Theorems2–3 provide the neutral ground state omega, its GNS representation (H_omega,pi,Omega), and a nonnegative selfadjoint H_infinity annihilating Omega. Its equation6 gives weak resolvent convergence between vectors A Omega_Lambda and B Omega_Lambda for bounded local operators A,B. We use the physical units H_infinity=(4/a)H_infinity,scaled; finite energies are likewise vacuum-subtracted physical energies. These are explicit mathematical imports: https://arxiv.org/pdf/math-ph/0411042 . Block38 gives the same finite-family static-charge lower bound sigma d, where sigma=(4/a)(1-kappa)>0 and kappa=3c(3av/4), and the upper trial energy4d/a.

## Local normality and gauge implementation

Local normality is needed to average the continuous gauge action on arbitrary bounded local operators. Here it follows from a uniform local-energy estimate, rather than being silently assumed. In scaled units set h_z=(a/4)K_cell,z and delta=3av/4. At most four grouped perturbations of norm at mostdelta touch a given cell z. Remove h_z and those touching terms. The remaining operator H_rest acts on the other cells. The variational bound using the cell vacuum times a rest ground state gives E_Lambda<=E_rest+4delta. Conversely the original ground expectation gives E_Lambda>=<h_z>+E_rest-4delta. Hence <h_z><=8delta uniformly in sufficiently large finite volumes (and boundary cells have no larger incidence).

For any finite cell set S, the positive sum of its h_z has compact resolvent: it is a finite product of compact-group electric operators with finite multiplicities. The uniform energy bound8delta|S| makes the reduced finite-volume density matrices tight in trace norm, by projecting below an energy cutoff and bounding the discarded mass. Any weak-star limit on the local bounded-operator algebra is therefore a normal density matrix. Thus omega is locally normal. This argument does not assert a globally trace-class infinite state.

Every finite gauge assignment g acts as an automorphism alpha_g on local link operators and leaves the finite ground states invariant; their limit is invariant. In the GNS space define U_g pi(A)Omega=pi(alpha_g(A))Omega. Invariance makes this well-defined and unitary, with U_g Omega=Omega. For any finite set of gauge vertices, local normality and the strongly continuous compact-group action on finite link Hilbert spaces imply strong continuity of g->U_g on the dense local-vector set and hence on the GNS space.

Finite covariance and the local-vector resolvent limit imply U_g(H_infinity-z)^-1=(H_infinity-z)^-1U_g for nonrealz. Thus each gauge unitary strongly commutes with H_infinity. This also follows from covariance of the selected dynamics, but the resolvent argument binds it directly to the imported construction.

## Charged fixed space and its dense local vectors

Fix distinct lattice vertices x,y and d=|x-y|_1. Adjoin the prescribed endpoint representation D=C3_x tensor conjugate(C3)_y, or its explicitly equivalent dual convention matching the open-line matrix carrier. D has dimension9 and zero Hamiltonian. On H_omega tensor D let V_g=U_g tensor R_xy(g). Define

 H_xy^(omega)=intersection_(finite gauge assignments g) ker(V_g-I).

This is a closed subspace. Since every V_g commutes with H_infinity tensor I_D, their common fixed subspace is reducing, and the restriction H_xy,infinity^(omega) is a nonnegative selfadjoint operator. No charged ground eigenvector is presumed.

Vectors w=sum_(alpha=1)^9 pi(A_alpha)Omega tensor e_alpha with bounded local A_alpha are dense in the full tensor space. For any such tuple, only finitely many vertex gauge factors act nontrivially: endpoints of its operator-support links and x,y. Haar-average the combined gauge action over those vertices. It yields a vector of the same form with bounded local operator coefficients B_alpha, because conjugation preserves the finite link support and source mixing is finite dimensional. The integral exists in the strong/weak operator sense on the finite link carrier and agrees in GNS by local normality. Gauge factors at other vertices already act trivially and commute with the averaged factors. Therefore this finite average equals the full charged-fixed-space orthogonal projection on w.

For a vector already in the fixed space, approximate by local tuples and apply these norm-contracting averages. This proves that exactly covariant bounded-local tuples are dense in H_xy^(omega). In finite volumes containing their link support and source vertices, the same averaged tuple acting on Omega_Lambda belongs exactly to the finite charged sector. There is no approximate Gauss condition or boundary leakage.

## Passing the uniform spectral lower bound

Let w be one of these local charged tuples and w_Lambda its finite-volume counterpart. The source's local-vector weak resolvent convergence, applied to each of the nine diagonal components, gives

 <w_Lambda,(H_Lambda-E_Lambda-z)^-1 w_Lambda>
 -> <w,(H_infinity tensor I_D-z)^-1 w>.

Their squared norms converge as well, by local ground-state convergence. For all sufficiently large volumes the actual graph contains a shortest Manhattan path between the fixed x,y, so its distance isd. Block38 places the spectral measure of every w_Lambda in[sigma d,infinity). The resolvent convergence implies convergence against continuous functions vanishing at infinity; this follows by the resolvent algebra and uniform boundedness of the spectral measures. Any nonnegative continuous compactly supported function below sigma d therefore has zero limiting integral. The limiting spectral measure is also supported in[sigma d,infinity).

This conclusion holds for a dense set of local charged vectors. By continuity of bounded spectral projections it holds on the whole reducing charged space. Hence

 H_xy,infinity^(omega)>=sigma d I.                    (L)

Only spectral support passes through this argument. It does not pass finite-volume lowest eigenvalues through a limit or assume convergence of minimizers.

## Nonempty sector and finite-energy open-line trial

Choose a fixed shortest simple path P from x to y and the nine local matrix coefficients A_ab=(U_P)_ab/sqrt3, with the source convention chosen for combined gauge invariance. The vector

 w_P=sum_ab pi(A_ab)Omega tensor e_ab

is charged and has norm1 because sum_ab A_ab^* A_ab=I pointwise. Its finite counterparts have the same norm. Block38's exact Dirichlet identity gives their vacuum-subtracted energy expectation exactly4d/a for EVERY finite volume containing the path, with the actual nonlinear potential unchanged.

Let mu_Lambda and mu be the spectral measures of these vectors for the nonnegative vacuum-subtracted Hamiltonians. The resolvent limit gives convergence against C0 functions, and both the finite and limiting measures have total mass1. Thus there is no loss of norm/mass at infinity and the probability measures converge weakly. Alternatively their uniform first moment4d/a directly supplies tightness. For the nonnegative energy function, lower semicontinuity (or bounded cutoff approximations) yields

 integral E dmu(E)<=liminf integral E dmu_Lambda(E)=4d/a.

Therefore w_P lies in the quadratic-form domain of the infinite charged operator and has form energy at most4d/a. No unjustified equality of first moments or uniform integrability of energy is asserted. The sector is nonempty and its spectral bottom

 V_omega(x,y):=inf Spec(H_xy,infinity^(omega))

satisfies

 sigma d<=V_omega(x,y)<=4d/a.                           (B)

In the smaller kappa<=1/2 regime this becomes2d/a<=V_omega(x,y)<=4d/a. This is a well-defined sector energy in the supplied neutral ground representation, rather than a claimed limit of finite-volume static potentials.

## Scope and outstanding questions

The construction retains all SU3 link representations, the full nonlinear fixed interaction and exact local Gauss constraints. It proves a nonempty charged sector in the selected infinite neutral-ground representation and bounds its energy bottom linearly in source separation. It does not prove that the bottom is an eigenvalue, that finite-volume charged minima converge to it, independence of every possible boundary-selected representation, a temporal Wilson-loop identity, physical quark dynamics, a numerical coupling threshold or a continuum limit. Static endpoints, Hamiltonian, couplings and units remain supplied inputs. The external neutral-GNS theorem and block38's equivariant coordinate argument are load-bearing premises, not axiom consequences.
