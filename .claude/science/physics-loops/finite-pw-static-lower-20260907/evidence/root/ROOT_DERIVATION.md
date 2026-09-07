# Two-sided charged-energy control for the actual finite-PW model

The43 candidate and lower-bound route were shared before completed writeups. Root received native's preliminary confirmation of the imported theorem's dimension-independent hypothesis and its algebraic envelope simplification before writing this full verification; it is not represented as a blind discovery. The result is a cutoff extension and composition of38,34 and42 for a supplied lattice Hamiltonian.

## 1. A separate cutoff argument is necessary

For the full compact Hamiltonian H and cutoff H_R=P_R H P_R, the ordinary variational inequalities E_xy,R>=E_xy and E0_R>=E0 do NOT imply E_xy,R-E0_R>=E_xy-E0. The two subtracted quantities both change. The following lower bound therefore reapplies the quantitative ground-state theorem to H_R itself, rather than transporting an uncut spectral difference by subtraction.

Take a finite cubic link graph with retained elementary faces, complete PW cutoffs p+q<=R, R>=1, and H_R=K_R+sum_f P_R v(1-ReTr U_f/3)P_R. Impose full Gauss transformations at every actual vertex, including boundary vertices. Put u=av and use the same source tensor D=C3 tensor conjugate(C3) of dimension9 as38. Source locations x,y are distinct and connected, with actual graph distance d.

## 2. Uniform cell hypotheses and exact gauge preservation

Complete each outgoing cell with three links as in34/38, using decoupled vacuum ghost links where needed. On a cell put h_z=(a/4)sum_(e tail z)K_e,R. The constant Haar vector is its unique zero state. Every nontrivial retained irrep costs at least4/a, and a fundamental irrep is present for every R>=1, so the normalized onsite gap is exactly1 at every R.

Group at most three centered face perturbations per cell. Their compressed norm is at most r=3u/4, because orthogonal compression never enlarges the multiplication norm. The fixed four-cell interaction range is unchanged. The quantitative perturbative theorem of Yarotsky0411042, in the applicability map already established in34/38, uses a unique local vacuum, a gap lower bound, bounded interaction norm and fixed geometry. It permits arbitrary local Hilbert spaces; its stated smallness and coordinate constants do not depend on their dimensions or on an upper bound on onsite energy. Consequently the same geometric constants c and r_* apply to all R>=1. These are imported existence constants, not a computed physical threshold.

Full-irrep cutoffs commute with both endpoint actions on every link. Local gauge transformations factor over outgoing cells, preserve each cell vacuum and its orthogonal complement, and commute with h_z. The interacting neutral full-carrier ground is unique and has nonzero product-vacuum overlap in the small window. Overlap normalization makes it invariant under all gauge transformations. Its unique creation-log coefficients and the resulting similarity S_R inherit that invariance, just as in38.

## 3. Charged free floor survives the cutoff

In the PW decomposition an occupied link has a nontrivial retained representation. Consider a connected component of occupied links. Apply the SAME central SU3 element at every vertex of that component. Every internal link coefficient has cancelling endpoint center factors, while trivial incident links are unchanged. An isolated external fundamental or antifundamental source would contribute a nontrivial center phase, contradicting combined Gauss invariance. Therefore x and y must lie in the same occupied component.

An occupied component connecting them contains at least d distinct actual links, each of normalized electric energy at least1. Hence the charged free operator H0=(a/4)K_R obeys H0>=d on the combined fixed source sector, regardless of how many additional representations the cutoff retains. This is an all-representation center argument, not a restriction to fundamental path states or a count of occupied cells alone.

The charged sector is nonempty for every R>=1 and every finite coupling: a fundamental transporter on a simple path, acting on the product Haar vacuum, is a nonzero normalized source vector, with every used link in a fundamental or antifundamental summand retained already at R1. This witness is only a nonemptiness proof here; its total potential energy is not used to claim a volume-uniform upper bound.

## 4. Same coordinate-resolvent exclusion, centered on the cutoff vacuum

For the finite-cutoff Hamiltonian itself, the imported creation-log construction gives the similar centered operator

 S_R^-1 [(a/4)(H_R-E0_R)] S_R=H0+F_R.

In the direct sum of cell-excitation coordinates, equip vectors with the sum of their component Hilbert norms. The quantitative column estimate bounds the perturbation by c r times H0 in this norm. Tensoring by D and bounding its9 components by Cauchy–Schwarz costs sqrt9=3, so on the charged source sector

 ||F_R z||_1<=kappa ||H0 z||_1, kappa=3c r.

S_R commutes with the combined gauge projection, so this is the appropriate charged restriction of the centered operator. Every space is finite-dimensional at finite graph and R, and the coordinate norm is equivalent to its Hilbert norm; no hidden closure issue is involved. For real z<d the charged free floor yields

 ||H0(H0-z)^-1||_1<=d/(d-z) for0<=z<d,
 ||H0(H0-z)^-1||_1<=1 for z<0.

If r<r_* and kappa<1, the Neumann inverse therefore exists for every real z<(1-kappa)d. Similarity preserves the spectrum. The lower bound is

 E_xy,R-E0_R >= (4/a)(1-kappa)d,              (1)

uniform in R>=1, graph volume and source separation. In a common smaller window kappa<=1/2 this gives2d/a. The centering is explicitly E0_R, not E0 of the uncut model.

For irregular actual boundaries, include only actual plaquette interactions and decouple padded ghosts. The physical and ghost-vacuum projectors commute with H0, the interacting ground similarity and F_R. Restrict their intersection throughout the argument. The charged free floor then uses actual occupied links and actual d, so a ghost cannot shorten the path. The decoupled ghost ground energy is zero and leaves E0_R unchanged. Dropping boundary Gauss conditions would invalidate the component-center argument and is not permitted.

## 5. Compose with the separate finite-cutoff energy-form upper bound

In the common weak window,42 applies to this same full neutral cutoff ground and gives its local-energy charged trial estimate. Its geometry-only form uses h_R=a e_R=ceil(3R^2/4)+3R and theta=8ud/h_R. For theta<1, combining42 with(1) yields

 1-kappa <= (E_xy,R-E0_R)/(4d/a) <= B(u,d,R),

 B(u,d,R)=[1+sqrt(theta)(1+sqrt(8u)+2u)
                  +2u sqrt(32u/h_R)]/(1-theta).                 (2)

At u=0 the actual charged minimum is exactly4d/a: the free floor and the fundamental path witness coincide. At positive fixed u, for any sequence of finite graphs and source distances with h_R/d tending to infinity, B tends to1. Thus the charged cost per distance stays between a strictly positive lower coefficient and a finite upper coefficient along that controlled cutoff scaling. This does not force a limit of the ratio or identify it with1; the actual charged minimum can lie below the full-unitary trial cost.

At a fixed finite R the lower bound(1) holds for every d, but theta<1 eventually fails as d increases. Neither(2) nor42 supplies a fixed-R uniform all-distance upper bound. R^2/d tending to infinity is a sufficient scaling, not a necessary or optimal hardware cost.

## 6. Optional fixed-R selected infinite representation

Fix one R once and for all. Use the same fixed-interaction, whole-range finite restrictions and neutral infinite ground representation supplied by0411042. The local link algebra is now a matrix algebra, so local normality and continuity of the finite gauge actions are immediate. The ground representation and Hamiltonian carry combined gauge actions after tensoring the external source space. Finite-vertex Haar averaging of bounded local vectors yields a dense charged subspace, as in39.

The finite charged spectral supports lie above L=(4/a)(1-kappa)d for sources fixed in the bulk. Weak-resolvent convergence of the ground representations transfers this support exclusion for fixed local charged test vectors; density gives the same lower bound on the selected charged Hamiltonian. This does not infer convergence of finite charged minima.

For theta=8ud/h_R<1, the local bounded compressed path operator has norm squared at least1-theta in every finite ground. Its local expectation converges, so the infinite trial is nonzero with the same lower norm bound. The42 finite normalized trial spectral measures have first moments bounded by(4d/a)B(u,d,R). Weak convergence and lower semicontinuity of the nonnegative first moment therefore put the infinite trial in the energy form domain and give the same upper bound for the selected charged bottom. There is no claim of an eigenvector at that bottom, representation independence, a joint R/volume limit, or a temporal Wilson-loop potential.

The finite theorem(1)–(2) does not rely on this optional extension. Neither version derives the supplied gauge action, coupling, clock, source meaning or state preparation from the four axioms, and neither describes a qubit implementation of nonunitary postselection.
