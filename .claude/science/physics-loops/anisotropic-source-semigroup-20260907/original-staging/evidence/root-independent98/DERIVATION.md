# Root independent simultaneous anisotropic source-operator limit

Provisional analytical proof for independent review. This is a conditional result for repeated powers of the supplied finite bare central source operator. It is not a theorem that a longer full microscopic Wilson slab equals these powers: (I* T I)^n need not equal I* T^n I. Repeated source compression/environment reinsertion is a supplied composition rule. No physical time, coupling or large spatial volume is selected.

## 1. Model and exact Gaussian parameters

Keep the same open four-cube, 17 gauge chords and two literal source chords. The action deficit is E_k=E_spatial+k E_temporal, with ten spatial halfweights and twelve temporal weights k>=1. All deficits are nonnegative, so E_k>=E_1. The unique gauged minimum, exact normalized-Haar coordinates and all source-compression identities are unchanged. Its Hessian H_k is positive. Exact independent calculations give

    det H_k=k^7(k+1)^2(2k+3)(4k^2+6k+1)/8,
    C_plus=10,
    C_minus=2(4k+5)/(4k^2+6k+1),
    Sigma_plus=30,
    Sigma_minus=6(4k+5)/(4k^2+6k+1).

For k>=1, det H_k is bounded above and below by positive fixed constants times k^12. The eight-color Gaussian partition coefficient therefore lies between fixed constants times k^-48. The source Gaussian precision has a fixed positive lower bound because Sigma_plus=30 and 0<Sigma_minus<=Sigma_minus(1)<30. Its density is not uniformly bounded as k grows; the crude estimates below do not silently assume that.

Set omega_k=(Sigma_plus Sigma_minus)^-1/2, r_k=sqrt(Sigma_minus/Sigma_plus), theta_k=(1-r_k)/(1+r_k). The independently averaged source Gaussian K_k is positive and has ground value

    lambda_k=1/[pi^4 j0 (sqrt(Sigma_plus)+sqrt(Sigma_minus))^8]
            =16sqrt3*pi/(sqrt(Sigma_plus)+sqrt(Sigma_minus))^8.

This follows directly by integrating its normalized Gaussian against exp(-omega_k |X|^2/2). Since Sigma_minus decreases from its k1 value to0, lambda_k is bounded above and below by fixed positive constants for k>=1. With the unitary coordinate change w=sqrt(omega_k) X, the operator K_k/lambda_k is exactly theta_k^N on Ad-invariant functions, N=(-Delta+|w|^2-8)/2. The fixed central oscillator eigenvalues of N are 2a+3b.

## 2. Uniform local Taylor estimate

Choose once and for all nested star-shaped product exponential balls around the identity on all17 groups. They are independent of k. On the larger compact local ball, E_1(w)>=c|w|^2, hence E_k(w)>=c|w|^2 for every k>=1. On the complement of any fixed smaller neighborhood, compactness and the unique E_1 minimum give a uniform positive gap. Every derivative of E_k through any fixed finite order on this compact chart is bounded by C k: the action has finitely many fixed analytic words and depends affinely on k. Product normalized Haar J is independent of k, smooth and even under simultaneous inversion.

For epsilon=beta^-1/2, let

    F_e,k(z)=chi(e z) exp[-E_k(e z)/e^2] J(e z),

with smooth cutoff supported in the larger product ball and equal1 on the smaller product ball. At e=0 use its continuous Gaussian value. Star-shapedness ensures the Hessian integral formula is valid at every intermediate parameter. Differentiating that formula gives

    |d_e(E_k(ez)/e^2)|<=C k |z|^3,
    |d_e^2(E_k(ez)/e^2)|<=C k |z|^4.

The exponential remains at most exp(-c|z|^2), uniformly in k and e on support. Differentiating J and chi adds only fixed polynomials; thus for some fixed polynomial P,

    |d_e^2 F_e,k(z)|<= C k^2 P(|z|) exp(-c'|z|^2).

The cutoff can be smoothly extended by zero. Derivatives on its support boundary vanish as required; its annular terms obey the same polynomial-Gaussian estimate. Constants in this paragraph are independent of k>=1 and sufficiently small e.

The first e derivative at0 is -j0^17 E3,k exp(-Q2,k). Its full integral vanishes by parity. More strongly, its integral over the15 nuisance Lie-algebra variables is identically zero for every pair of fixed source vectors. The already reviewed two-source f-tensor cancellation applies for every k: each color covariance remains a scalar edge covariance times delta_color, and conditional means span the two fixed source vectors. The coefficients may depend on k; the cancellation itself is exact.

Integrating Taylor's remainder over all136 variables therefore gives partition coefficient error <=C k^2/beta. Integrating only the120 nuisance variables gives an unnormalized source-marginal error <=C k^2/beta times a fixed polynomial-Gaussian envelope in the16 source coordinates. These bounds apply to the cutoff model with respect to rescaled Lebesgue coordinates.

## 3. Uniform partition lower bound and normalization loss

Let D_beta,k=beta^68 Z_beta,k, where Z uses the actual product Haar and deficit action. Let D0,k=j0^17 (2pi)^68 det(H_k/3)^-4. The discarded global contribution is at most beta^68 exp(-c beta), with c independent of k>=1, because E_k>=E_1. For all sufficiently large beta this is bounded by C/beta, hence

    |D_beta,k-D0,k|<=C k^2/beta,
    c0 k^-48<=D0,k<=C0 k^-48.

Consequently D_beta,k>=D0,k/2>=c1 k^-48 whenever beta>=C1 k^50, where C1 is a finite model-dependent constant. No numerical C1 or onset is claimed.

Write M_beta,k for the corresponding unnormalized rescaled source marginal and M0,k for its full Gaussian counterpart. The local estimate gives a polynomial-Gaussian bound C k^2/beta for their difference. To remove the nuisance cutoff on the source chart, its contribution is bounded by C beta^60 exp(-c beta). Since |x|^2+|y|^2<=2delta^2 beta inside this chart, an exponential fraction absorbs the source radius and any beta polynomial. This yields C/beta times a fixed weaker source-Gaussian envelope, uniformly in k. The full Gaussian contribution outside the nuisance cutoff has the same estimate, using Q2,k>=Q2,1. Thus

    |M_beta,k-M0,k|<=C k^2/beta P(R) exp(-c2 R^2),
    M0,k<=C exp(-c2 R^2),
    R^2=|x|^2+|y|^2.

The second bound is for the UNNORMALIZED nuisance Gaussian integral and is uniform; it follows from Q2,k>=Q2,1. Normalization now yields

    |p_beta,k-p0,k|
      <= |M_beta,k-M0,k|/D_beta,k
         +M0,k |D_beta,k-D0,k|/(D_beta,k D0,k)
      <= C/beta [k^50+k^98] P(R) exp(-c3 R^2).

The k98 exponent is deliberately crude: two inverse partition factors cost k96 and the Taylor remainder costs k2. There is no assumption that the normalized Gaussian has a uniform peak. Thus both weighted L1 and L2 source-density errors are <=C k98/beta on the expanding chart. Outside that chart the limiting Gaussian has an exponentially small tail times at most k48 (using p0=M0/D0); it fits the same estimate under beta>=C1 k50.

## 4. Actual operator and norm normalization

The one-source Haar half-density denominator is positive and uniformly bounded on the fixed chart, independently of k. Its difference from j0 is <=C beta^-1 R^2. Multiplying p0<=C k48 exp(-cR^2) adds at most C k48/beta in weighted L2, which is dominated by k98/beta. Independent source conjugation averaging contracts L2.

Let U_beta be the previously defined chart partial isometry and P its source projector. Then

    || beta^-4 U_beta P A_beta,k P U_beta* - K_k ||_HS
       <= C k98/beta

for beta>=C1 k50 and sufficiently large beta. The actual source-chart complement has kernel amplitude <=C beta68 k48 exp(-c beta), so

    beta^-4 ||A_beta,k-P A_beta,k P||_HS
       <= C beta64 k48 exp(-c beta)
       <= C k98/beta.

The last inequality follows from a uniform finite supremum of beta65 exp(-c beta), and k>=1. Thus actual scaled norm differs from lambda_k by <=C k98/beta, without identifying operators on different Hilbert spaces incorrectly.

Because lambda_k has a fixed positive lower bound, for beta>=C2 k98 the actual positive norm-scaled operator C_beta,k=A_beta,k/||A_beta,k|| is a contraction and its dilated chart compression differs from K_k/lambda_k by <=C k98/beta in operator norm. After the k-dependent oscillator coordinate unitary W_k,

    ||B_beta,k-exp(-t_k N)|| <= C k98/beta,
    t_k=-log theta_k,
    B_beta,k=W_k U_beta P C_beta,k P U_beta* W_k*.

B_beta,k, extended by zero on the complement of the chart image, is a positive contraction. The transformed exact oscillator semigroup acts on the same Ad-invariant L2 space. The complement tail also bounds C_beta,k-P C_beta,k P by the same error.

## 5. Simultaneous n-step limit

Fix t>0 and k_n=4n^2/(5t^2), restricted to n large enough that k_n>=1. Set beta_n=n^200. These are sufficient supplied parameter schedules, not an optimized or physically selected scaling. Eventually beta_n>=C2 k_n98, since the right side grows like n196.

Elementary expansion of the exact rational r_k gives

    r_k=(5k)^-1/2+O(k^-3/2),
    t_k=2/(sqrt(5k))+O(k^-3/2),
    n t_(k_n)=t+O(n^-2).

A telescope between positive contractions gives

    ||B_(beta_n,k_n)^n-exp[-n t_(k_n) N]||
       <= C n k_n98/beta_n = O(n^-3).

Since n t_(k_n) stays bounded away from0, the spectral theorem gives

    ||exp[-n t_(k_n)N]-exp(-tN)||=O(n^-2),

using sup_(x>=0) x exp(-a x)=1/(e a) for a>0. This is operator-norm convergence, including all central oscillator modes, not merely fixed eigenvalues.

The same limit holds for the chart-compressed ACTUAL n-th power

    W_kn U_betan P C_(betan,kn)^n P U_betan* W_kn*,

because ||C^n-(PCP)^n||<=n||C-PCP|| and the same off-chart estimate is O(n^-3). This step distinguishes taking actual powers from repeatedly inserting the chart cutoff. It does NOT remove the physical source-compression/reset premise built into A itself.

Therefore the simultaneous schedule yields exp(-tN) with an asymptotic norm error O(n^-2), with unspecified finite constants and onset depending on t and the fixed supplied model. The exponent200 is a sufficient analytic construction; it is enormous and offers no usable finite-resource accuracy claim. A smaller exponent would require sharper bounds, not a parameter fit.

## 6. Ground-transformed invariant dynamics

The oscillator ground function is proportional to exp(-|w|^2/2). Its unitary ground-state transform yields the Ornstein–Uhlenbeck Markov generator L=(1/2)Delta-w·grad in invariant Gaussian L2 with density proportional to exp(-|w|^2). For q=Tr w^2 and c=Tr w^3,

    L=2q d_qq+6c d_qc+(3q^2/4)d_cc+(8-2q)d_q-3c d_c,
    q>=0, c^2<=q^3/6.

The identities are grad q=2w, grad c=3(w^2-qI/3), Trw^4=q^2/2, Delta q=16, Delta c=0. Thus gradq·gradc=6c and |gradc|^2=3q^2/2, giving the displayed mixed coefficient. The discriminant domain is the image of traceless Hermitian matrices. The inherited ambient invariant semigroup defines its boundary behavior; this proof does not independently assert uniqueness for an arbitrarily prescribed singular two-variable boundary PDE.

This supplies conditional smooth reduced dynamics for a family of repeated finite source operators. It leaves the microscopic composition law, physical parameter/time selection and spatial thermodynamic limit open.
