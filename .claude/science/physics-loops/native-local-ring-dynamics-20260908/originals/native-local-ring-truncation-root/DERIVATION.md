# A constructive finite local ring truncation bound

Independent root proof, frozen before reading the parallel native agent's proof. This is an intentionally very conservative existence bound, not a useful numerical coupling threshold. Supplied full edge carrier, even cubic torus with all extents at least four, native local A, H=UD+g sum lambda_e A_e. No hard low-charge projection.

## Norm and local algebra

Store three positive-direction edge qubits at each cubic cell. For a strong-support potential B=sum_S B_S define ||B||_k=sup_x sum_{S containing x} exp(k|S|)||B_S||. Use connected supports and the torus graph metric. D=sum Q_v² has four-cell charge-star terms, norm at k=1 at most36e^4<2916=:d. Each native edge term is strongly supported on at most8 cells, with at most33 such terms covering any cell. Normalize V=sum b_e A_e with |b_e|<=1; its norm at1 is at most33e^8<216513=:v. If max|lambda|=0 the result is exact; otherwise set z=g max|lambda|/U and b_e=lambda_e/max|lambda|, so H/U=D+zV.

For 0<k'<k, the potential commutator satisfies

||[A,B]||_{k'} <= 4/[e(k-k')] ||A||_k ||B||_k.

Proof: use the representation [A_S,B_T] on S union T, only overlapping pairs. Split a marked cell x between S and T. For the first part, sum T through an intersection point in S, producing |S| times the local B norm, and absorb |S| with |S|exp(-(k-k')|S|)<=1/[e(k-k')]. The second part exchanges S,T. The operator commutator norm contributes2. This also proves the bound for strong supports since commutators are strongly supported on their union.

For any m>=1, distributing the loss delta=k-k' equally over m brackets gives ||ad_S^m B||_{k'} <= (4m/(e delta))^m ||S||_k^m ||B||_k. Since m! >= (m/e)^m, the Lie series is bounded by the geometric series with ratio4||S||_k/delta. In particular exp(ad_S) is analytic in local norm and has norm at most2 on B whenever ||S||_k<=delta/8.

Averaging A(B)=(1/2pi) integral_0^{2pi} exp(itD)Bexp(-itD)dt is norm contractive. The homological inverse

I(B)=(1/2pi) integral_0^{2pi} i(t-pi) exp(itD)Bexp(-itD)dt

has [D,I(B)]=B-A(B), norm <=(pi/2)||B||<4||B||, and is anti-Hermitian when B is Hermitian. This follows termwise from integer D frequencies; the zero frequency integrates to zero. Both operations preserve each strong support. No onsite-only theorem is being assumed.

## Five formal elimination steps and explicit constants

Choose k_j=1-j/12 for j=0,...,5. Construct S(z)=sum_{j=1}^5 z^j S_j. At step j, let R_j be the coefficient of z^j in exp(ad_{sum_{i<j}z^i S_i})(D+zV). Set S_j=I(R_j) and K_j=A(R_j). The new coefficient is R_j+[S_j,D]=K_j and commutes with D. Lower coefficients are unchanged. Every real-z S_j is anti-Hermitian. All objects are connected strong-support potentials with volume-independent norms.

Here is an explicit recursive majorant requiring no unknown theorem constants. Starting with no s_i, define C_j=48j and

r_j = d [z^j] exp(C_j sum_{i<j}s_i z^i) + v [z^{j-1}] exp(C_j sum_{i<j}s_i z^i),
s_j=4r_j.

All coefficients in this scalar expression are nonnegative. The previous commutator estimate with at most j nested brackets and loss1/12 bounds ||R_j||_{k_j}<=r_j and ||S_j||_{k_j}<=s_j. The d term bounds the D input directly; no cancellation is needed for the bound. These are finite rational numbers computed only for j<=5, independent of the lattice volume and the signs of b_e.

Set delta=1/12, r=min(1,delta/(8 sum_{j=1}^5 s_j)), and M=2(d+v). On the complex disk |z|<=r, ||S(z)||_{7/12}<=delta/8. The exact transformed Hamiltonian F(z)=exp(S(z))(D+zV)exp(-S(z)) therefore has ||F(z)||_{1/2}<=M. Its Taylor polynomial through degree5 is D+sum_{j=1}^5 z^jK_j. Cauchy's bound in the local potential Banach space and geometric summation imply, for |z|<=r/2,

exp(S) H exp(-S)=UD+U sum_{j=1}^5 z^j K_j + E,
||E||_{1/2} <= 2 M U (|z|/r)^6.

Equivalently ||E||_{1/2}<=C gamma^6/U^5, C=2M/r^6, gamma=|g|max|lambda|. This constant is extremely large and the sufficient regime extremely small. It proves a uniform local asymptotic statement; it is not a realistic parameter estimate. The finite-volume unitary is exact, while its local bounds are uniform in volume.

## Ice restriction and fourth-order gauge

Let P be the full D=0 space. F_bit=product_e Z_e commutes with D and anticommutes with V. Averaging and I commute with its conjugation. Thus S_j and K_j have parity(-1)^j. Every ice state has exactly3N/2 occupied edges, so F_bit is scalar on P and P K_j P=0 for odd j. Also PVP=0, the second coefficient is the scalar -sum b_e²/2, and the fourth coefficient equals the canonical direct-rotation H4 in U=1 normalization.

For the last claim, at each fixed finite volume compare the formal block diagonalization with the canonical direct rotation for P. Both block diagonalize through order5 and their effective ice Hamiltonians differ by a formal unitary within P through this order. The lower ice terms are zero or scalar, so conjugation cannot change the fourth coefficient. This does not transfer the canonical sixth-order diagonal into this different gauge. Such a sixth-order claim would require additional work.

Consequently the approximate Hamiltonian UD+U sum_{j<=5}z^jK_j preserves ice exactly and restricts there to the known scalar second/fourth terms plus the actual fourth-order rings, including length-four winding rings. Its fourth ring coefficient is the source-proved eta_C product lambda_e/(2U^3), multiplied by g^4. The bound compares the full model with this charge-conserving finite-order effective model in local norm, not with an added RK potential.

## Dynamics and interpretation

For a fixed local observable in the transformed frame, Duhamel plus a local Lieb–Robinson estimate gives a bound proportional to ||E|| times a polynomial of degree4 in time in three dimensions, with constants depending on the observable, the fixed norm convention and the approximate K interaction strength, but independent of volume. Large UD does not force an O(U) propagation speed: [D,K]=0 and the commuting finite-range D evolution enlarges a local observable support by a fixed neighborhood only; the K evolution supplies the propagating light cone. This is a polynomial truncation-timescale statement, separate from optimal quasi-exponential prethermal normal forms.

Laboratory initial states and observables must be transformed consistently by exp(S). To use an ice-sector ring dynamics statement, prepare a dressed ice state exp(-S)|ice> and dress measured observables, or explicitly bound the local dressing error. Bare ice has perturbative dressing corrections. Local bounds do not imply that the probability of any defect anywhere is small at arbitrary volume. No uniform isolated global ice band, phase, photon, temperature, or physical coupling selection is claimed.
