# All-order rectangular area selection and the first two actual spatial loop coefficients

This is a finite-volume Taylor selection theorem for the supplied compact cubic Hamiltonian. It does not by itself give a uniform complex radius, an area law, a temporal string potential, or physical confinement. Root exposed the one-face u/144 candidate before calculation. The two-face candidate below was independently derived and prospectively frozen before exact checks. Root subsequently requested the separately preregistered periodic half-area extension. No coefficient fitting was used.

## 1. Analytic object and its domain

Take a finite open cubic link graph, with any subset of its actual elementary faces retained, and full link Hilbert space. Put u=av and

 h(u)=h0+u V, h0=a sum_e K_e,
 V=sum_f(1-ReTr(U_f)/3).

The constant face count changes eigenvalues, not ground projections, so use instead V_c=-S/6 with S=sum_f(chi_f+bar chi_f). Here chi_f=Tr(U_f) in the fundamental representation. The free vacuum is the normalized constant0, unique on full link space, and h0 has gap at least4. The bounded centered perturbation has norm at most the face count F. A contour about0 of radius smaller than the free gap defines the analytic Riesz projection P(u) for sufficiently small complex u. Its rank remains1. On real u sufficiently close to0 it is the ground projection; the local eigenvalue and eigenvector branches are isolated. The physical Gauss restriction gives the same ground expectation because the vacuum and perturbation are gauge invariant and this simple branch remains physical.

For a bounded loop observable W define the holomorphic expectation

 f_W(u)=Tr(W P(u))/Tr(P(u))=Tr(W P(u)).             (1)

The equality holds because rankP(u)=TrP(u)=1, also for the non-self-adjoint complex projection. Formula(1), rather than a conjugate-u vector norm, is the analytic continuation. A finite-volume radius follows from the bounded resolvent Neumann series but may shrink with F. No volume-independent analyticity is inferred.

A technical trace point matters. Individual free resolvents need not be trace class. Expand each resolvent factor as P0/z plus Q(z-h0)^(-1)Q. The term containing only Q resolvents is holomorphic inside the contour and integrates to zero. Every other term has a P0 factor and is finite rank, so its contour integral and trace against W are well defined. Thus at order n the coefficient is a finite sum of legitimate finite-rank traces, with precisely n factors of V_c and free resolvents/projectors. This justifies the charge argument without illegally tracing a non-trace-class resolvent integrand.

## 2. Independent edge-center selection

For every link e independently, multiply U_e by zeta=exp(2pi i/3). This is a unitary on Haar L2, commutes with h0 and its resolvents, fixes the constant vacuum and commutes with all vertex gauge actions. An oriented fundamental face character transforms by zeta raised to its signed incidence on that link; its conjugate has the opposite charge. The same holds for an oriented loop character.

Resolve each of the n perturbation factors into a character of one oriented face, with sign sigma_j in{+1,-1}; resolve W_C=(chi_C+bar chi_C)/6 into observable sign sigma_C. Conjugating a finite-rank trace term by each link-center unitary shows it is zero unless

 sigma_C C+sum_(j=1)^n sigma_j partial f_j=0 mod3               (2)

as a one-chain on edges. Repeated insertions count with multiplicity n. Resolvents cannot absorb center charge. Scalar perturbation insertions, if one kept the uncentered V, only decrease the number of available charged faces and cannot improve the lower bound.

Let C be the boundary of an R by S planar xy rectangle at fixed z, with R,S positive integers. Project the finite three-dimensional chain onto the infinite xy square lattice: xy faces go to their base-coordinate squares, xz/yz faces go to zero, x/y edges project normally and z edges go to zero. This is a chain map, including for vertical faces whose two horizontal projected edges cancel. The projected two-chain b over F3 therefore satisfies

 partial b=-sigma_C partial I_rect.              (3)

A finitely supported two-cycle on the infinite square plane is zero. Indeed its edge equations equate the coefficients of neighboring squares; a finite-support constant is zero. Hence b=-sigma_C I_rect. Each of the RS interior squares has nonzero coefficient. Each requires at least one inserted xy face above that square. A face contributes to only one projected square, regardless of its height or orientation. Thus n>=RS.

Consequently every Taylor coefficient of f_(W_C)(u) below order RS vanishes. This conclusion is all-order and geometric; it does not rely on a finite census. The independent phases are Z3 center phases, not a fictitious U1 symmetry. Mod3 cancellation, repeated faces and nonplanar fillings are all included by(2)–(3).

## 3. Periodic variant and its necessary qualification

For a cubic torus project onto its Lx by Ly xy torus. Assume the rectangle is nonwrapping and fits strictly inside the periods as a contractible rectangular loop. Two planar solutions of(3) differ by a constant F3 two-cycle. The three possible coefficient supports have sizes

 A=RS, LxLy-A, LxLy.

Thus the same order-n vanishing for n<A follows if A<=LxLy/2. Without that condition the argument only gives n>=min(A,LxLy-A), and the complementary surface can genuinely be smaller. For example a4by4 rectangle on a5by5 torus has area16 but complement9. No unqualified periodic area16 selection is asserted. The leading coefficients in the next sections are for open geometry, not for small periodic boxes where a second minimal filling could contribute.

## 4. Actual single-face coefficient

Use intermediate normalization for the real-u ground vector, writing psi=0+u psi1+u²psi2+..., with <0,psij>=0 for j>=1. Let R0=Q h0^(-1)Q. Since each elementary face character has four nontrivial fundamental links, it is an exact h0 eigenvector with energy16. Haar meanS=0. Therefore

 psi1=-R0 V_c 0=S/96,
 psi2=-R0 V_c psi1=R0 S²/576.                   (4)

For a retained face p, W_p=(chi_p+bar chi_p)/6 has mean0. At first order only p and its conjugate survive edge-center selection. Haar orthogonality gives integral chi_p bar chi_p=1 and integral chi_p²=0. Hence

 f_(W_p)(u)=u [2*(1/6)*(1/96)*2]+O(u²)
           =u/144+O(u²).                       (5)

This agrees with the exposed root candidate but was obtained directly from the actual character eigenstates and Haar contraction. It is independent of other retained faces at this order.

## 5. Actual two-adjacent-face six-link rectangle

Assume the two adjacent planar faces p,q are retained in an open cubic graph. The rectangle has six distinct exterior links, so W_C0 is an exact free eigenvector of energy24. There is only one projected area-two filling. At order2 condition(2) forces the actual p,q at the loop's height, one insertion of each with opposite orientation to the observable; their exterior charged edges exclude displaced-height fillings. There are two orders and two conjugate choices, four terms in total. No other face pair can contribute.

The Haar value of each term is1/3. To see this on the actual seven-link union of p,q, write the shared link as U and the products of the other three edges of each face as A,B, choosing cyclic order so the face characters are Tr(AU),Tr(U†B) and the rectangle is Tr(AB). Fundamental Haar orthogonality gives

 integral_dU Tr(AU)Tr(U†B)=Tr(AB)/3.

Here the coefficient of A_ij B_kl is delta_jk delta_il/3. Integrating the remaining six independent links gives integral|Tr(AB)|²=1, since their product is Haar. Therefore

 I=integral W_C S²=(4/6)*(1/3)=2/9.             (6)

The u² expectation has a middle term and two endpoint terms. From(4), self-adjointness of R0 and the exact energy24 of W_C0,

 <psi1,W_C psi1>=I/96²=1/41472,
 2 Re<0,W_C psi2>=2I/(576*24)=1/31104.

Normalization of the real ground vector contributes nothing at this order because <0,W_C0>=0 and the first-order expectation vanishes. Thus

 f_(W_C)(u)=(7/124416)u²+O(u³).                 (7)

The two free denominators16 and24 are different and load bearing. Replacing the final rectangle energy24 by16 gives a different, incorrect coefficient. This calculation does not approximate the Hamiltonian by commuting classical plaquette fields: the noncommuting free resolvent is explicitly retained. It computes a spatial loop expectation in the supplied ground state, not a temporal transfer or string energy.

## 6. Independent exact checks and preserved defect

The checker constructs the actual two-cube open graph with12 vertices,20 links and11 faces. Order0/1/2 center-charge censuses give0/0/4 survivors for the six-link rectangle, with all four exactly the planar pair. It verifies shared-link Haar index coefficients, rational free denominators, one-face coefficient, two-face coefficient and a wrong-denominator adverse case. Separate planar/periodic chain checks support indexing only; the all-order proof is Sections2–3.

Self-review before result exposure found that the first Haar tensor checker compared the same incorrectly transposed Kronecker indices on both sides and therefore passed spuriously. The original source/raw are preserved. The corrected index formula and an E01/E10 adverse control distinguish the erroneous transpose. The physical Haar identity, analytic candidates and center census did not change. This failure is recorded rather than presented as an independent validation success.

A uniform analytic bound or marked-cluster result could combine with this selection rule to imply controlled area suppression. That extra theorem is not proved here. Finite-volume Taylor vanishing alone does not establish an area law, an infinite-volume analytic radius, physical confinement or a continuum limit.
