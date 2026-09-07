# Volume-uniform finite-PW charged trial upper bound

2026-09-07. Root's proposed formula was exposed before the prospective contract. This derivation was written without reading a completed root proof. It repairs the specific missing form-energy bridge in block41, for the supplied finite Peter–Weyl Hamiltonian; it does not derive a hardware compiler or a physical coupling.

## 1. Model and the necessary full-carrier ground premise

Take a finite ordinary cubic link graph, at most four plaquettes incident to each link. The link Hilbert space is the complete Peter–Weyl sum p+q<=R, R>=1. Let P be its tensor product projection from the full Haar link Hilbert space. Put

 H_R=P(K+V)P on Ran P, K=sum_e K_e,
 K_e=-(3/(2a)) sum_A D_eA^2, V=sum_f V_f,
 V_f=v(1-ReTr U_f/3), 0<=V_f<=2v.

Haar is normalized, a>0,v>=0, and Hermitian generators satisfy Tr(T_A T_B)=delta_AB, sum_A T_A^2=(8/3)I. Full-irrep projection preserves both endpoint actions and commutes with K. Let Omega be a normalized ground vector of H_R on the FULL finite tensor carrier, of ground energy E_0. Assume Omega is neutral physical. The small-av regime of the reviewed uniform-gap theorem supplies a unique full-carrier ground, hence this physical premise. We do not replace minimization on the full carrier by minimization only in an arbitrarily constrained Gauss subspace.

Replace one link in |Omega><Omega| by its normalized Haar vacuum and retain the reduced density matrix on every other link. This is a legitimate mixed trial on the full finite carrier. All other kinetic terms and all nonincident face expectations are unchanged. Its link kinetic energy is zero. Each of at most four changed compressed positive face terms has expectation between0 and2v. Ground minimality therefore gives

 E_e:=<Omega,K_e Omega> <=8v.                 (1)

Thus E_path<=8vd for d distinct path links, and E_face<=32v for a four-link face. No ambient-volume norm appears. The replacement need not itself be gauge invariant; that is harmless precisely because Omega minimizes on the full carrier. At v=0 a restricted subspace excluding the vacuum would invalidate this inference: a positive-energy eigenstate can minimize there, showing why the premise matters.

## 2. Accepted charged trial and exact Rayleigh commutator

Let W be the ordered full fundamental transporter along a path with d distinct links, with inverse factors for reverse orientations. Regard W Omega as a matrix-valued function with Hilbert–Schmidt color norm Tr/3; this is the standard normalized external-source singlet contraction. Define C=P W P. Block41's exact distinct-link projection identity identifies C with the product of the compressed link transporters. Its exact endpoint covariance makes C Omega a vector in the external fundamental/antifundamental charged sector.

For e_R=[R^2-floor(R^2/4)+3R]/a, define

 theta=E_path/e_R, q=||C Omega||^2.

The shell/union bound gives 1-q<=theta. In particular theta<1 suffices for a nonzero charged trial. The charged variational energy excess satisfies

 Delta_R <= <C Omega,(H_R-E_0)C Omega>/q
          = <C Omega,[H_R,C]Omega>/q.         (2)

Every inner product here includes normalized color trace. H_R Omega=E_0 Omega holds in each color column. No derivative of a normalized, postselected output is inferred from a state-norm bound; we estimate the actual commutator in (2).

## 3. Kinetic contribution and its domain

All finite PW functions are smooth on a finite compact product group. Multiplication by the finite path word remains smooth. Therefore all kinetic and commutator expressions below are in their classical operator domains; there is no unbounded-operator limit interchange.

Since P commutes with K,

 [K,C]Omega=P[K,W]Omega.

Consequently its contribution differs from the full path identity by exactly

 <C Omega,[K,C]Omega>
 =<W Omega,[K,W]Omega>-<QW Omega,[K,W]Omega>, Q=I-P.

For each used link, sum_A D_eA^2 W=-(8/3)W. The cross term in the normalized trace of W^*(D_eA W) is zero, because it is a conjugate of plus or minus iT_A. Hence, even for complex scalar Omega,

 <W Omega,[K,W]Omega>=4d/a.                  (3)

The product rule is

 [K,W]Omega=(4d/a)W Omega
             -(3/a)sum_(e,A)(D_eA W)(D_eA Omega).

At each configuration the row operator with entries D_eA W has square

 sum_(e,A)(D_eA W)(D_eA W)^*=(8d/3)I.

Indeed each derivative is a unitary left/right product around plus or minus iT_A. The same identity holds for reverse orientation. Operator Cauchy–Schwarz, also on Hilbert–Schmidt color matrices, and the kinetic quadratic form give

 ||sum_(e,A)(D_eA W)(D_eA Omega)||
 <=sqrt((8d/3) sum_(e,A)||D_eA Omega||^2)
 =sqrt((8d/3)(2a/3)E_path).

Therefore

 ||[K,W]Omega|| <=4d/a+4sqrt(d E_path/a),

and using ||QW Omega||<=sqrt(theta),

 <C Omega,[K,C]Omega>
 <=4d/a+sqrt(theta)[4d/a+4sqrt(d E_path/a)].  (4)

Taking the real part if necessary is implicit in the upper estimate; the total Rayleigh numerator is real. The exact scalar/color-trace identity (3), not an operator identity on arbitrary color states, is the reason the full kinetic cost is exactly4d/a.

## 4. Only incident magnetic faces contribute

Write V_f^R=P V_f P. If f has no link in common with the path, its compressed operator commutes with C: it acts on disjoint link variables and is scalar in the shared color. Such faces contribute zero, exactly.

For a touching face, full scalar multiplication commutes with W. Inserting I=P+Q gives the exact compressed commutator

 [V_f^R,C]=P W Q V_f P-P V_f Q W P.          (5)

Let T_e=P_(R,e)-P_(R-1,e), and let T_f be the projection that at least one of the four face links lies in its top shell. Fundamental or antifundamental multiplication on each face link raises p+q by at most one. Thus Q V_f annihilates the subspace where all four face links are interior, and

 ||Q V_f Omega|| <=||V_f|| ||T_f Omega||
 <=2v sqrt(sum_(e in f)<T_e>)
 <=2v sqrt(E_face/e_R).                      (6)

The scalar part of V_f causes no leakage. This argument uses the actual face word, not arbitrary bounded potentials. In addition ||Q W Omega||<=sqrt(theta), ||P W||<=1 and ||C Omega||<=1. Equation(5) therefore yields

 |<C Omega,[V_f^R,C]Omega>|
 <=2v[sqrt(E_face/e_R)+sqrt(theta)].          (7)

There are at most4d distinct touching faces; double-counting them only weakens the bound. Neither (6) nor (7) uses a total-volume magnetic norm.

## 5. Explicit volume-independent result

Combining (2), (4), (7), for theta<1,

 Delta_R <= {4d/a
 +sqrt(theta)[4d/a+4sqrt(d E_path/a)]
 +sum_(f touching path)2v[sqrt(E_face/e_R)+sqrt(theta)]}/(1-theta). (8)

This is exactly a finite charged trial energy bound, not merely a vector approximation. A completely explicit sufficient version follows from (1). Put h_R=a e_R and theta_0=8avd/h_R. If theta_0<1, then

 a Delta_R <= {4d
 +sqrt(theta_0)[4d+4d sqrt(8av)]
 +8avd[sqrt(32av/h_R)+sqrt(theta_0)]}/(1-theta_0). (9)

For every fixed path and fixed a,v in the stated physical-ground regime, this tends to4d/a as R grows, uniformly over finite ambient graphs containing that path. At v=0 the bound is exactly4d/a already for every R>=1. For growing d at fixed av, h_R/d tending to infinity is sufficient for the relative correction to vanish; h_R grows quadratically in R. No specific numerical weak-coupling threshold is inferred.

The charged sector is nonempty when the trial is nonzero. The weak-regime full neutral ground premise implies a nonnegative charged excess, but no new charged lower bound is derived here. Unused-qubit sectors, a physical implementation of C, repeated-link paths, time evolution or infinite-volume convergence of charged minima remain separate questions. The input is the actual full finite ground, not the projection of an assumed untruncated ground. The result therefore repairs precisely the missing finite-carrier upper-trial bridge while retaining the model and preparation assumptions.
