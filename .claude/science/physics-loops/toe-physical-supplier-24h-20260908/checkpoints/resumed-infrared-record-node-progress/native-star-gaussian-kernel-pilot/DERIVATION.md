# Fixed L4 Gaussian semigroup kernel comparison

This is a finite normalization and hardware-cost experiment, UNLAUNCHED. It does not evaluate the infinite node scalar, integrate time, certify floating arithmetic, or apply the newly proved infinite h/6 gap to L4.

## Exact reduced carrier

Use hopping t_hop=1, h=2, the 4^3 cubic torus, lexicographic sites, and the directed staggered matrix
K_(r,r+ea)=-2(-1)^(sum_(b<a) r_b), with an additional minus sign on every positive-direction wrap. Reverse entries follow skew symmetry. These are antiperiodic boundary twists in each direction. The magnetic directional differences anticommute. On length four with AP twist, the square of the forward shift plus its inverse square vanishes. Hence K^2=-24 I exactly.

For a pair of disjoint two-edge star subsets A,C, take W=span of the center, their four distinct neighbors, and their K-images. Thus dim_R W<=10. W is K-invariant; both defects have their entire range in W. Its orthogonal complement is an unchanged spectator bath. Choose real orthonormal pairs (a,b), b=-Ka/sqrt(24). Then the restricted reference matrix is the direct sum [[0,sqrt(24)],[-sqrt(24),0]]. With gamma_(2j)=a_j+a_j^dagger and gamma_(2j+1)=i(a_j^dagger-a_j), H=(i/4)gamma^T K gamma has vacuum energy E0=-n sqrt(24)/2, n=dim W/2. The unchanged complement cancels exactly from every shifted semigroup. No parity trace or degeneracy factor is inserted into this vacuum matrix element.

The implemented Gram construction uses floating coordinates but checks orthonormality, invariance, reference orientation, and full defect reconstruction before any kernel evaluation. These residual checks are numerical implementation gates; the preceding span argument is the mathematical reduction.

## Independent Gaussian and Fock routes

For G=exp(-t1 H1)...exp(-tm Hm), coefficient conjugation is
G gamma(c) G^-1=gamma(Rc), R=exp(-it1 K1)...exp(-itm Km).
The transformed annihilator rows are (e_(2j)^T+i e_(2j+1)^T)R^T/2. Writing them as u a+v a^dagger gives the Thouless coefficient Z=-u^-1 v. The unnormalized state is c0 exp(a^dagger Z a^dagger/2)|0>.

The spin lift connected to the identity gives
c0=exp(E0 sum t_j + Tr Log(u)/2)
for the shifted semigroups. This normalization follows by differentiating both expressions using the CAR and matching c0(0)=1; the square-root sign must not be chosen independently at each point. Our entire fixed path lies in ||u-I||<1, so the principal matrix logarithm supplies that continuation. Computing the sum of principal eigenvalue logarithms is equivalent to Tr Log(u) in this chart, even when the determinant's scalar principal square root would select a different branch.

Here ||K_A||<=sqrt(24)+4sqrt(2)<11 and total duration<=1/32. Thus ||R-I||<=exp(11/32)-1<1/2 and ||u-I|| obeys the same bound. The implementation's fixed 3/4 chart gate leaves numerical margin and rejects failure rather than switching charts after seeing an outcome.

Every inserted gamma is moved left through the preceding factors using R. For two resulting coefficient vectors x,y, put ax=x_even-i x_odd, ay=y_even-i y_odd, by=y_even+i y_odd. Wick algebra gives
<0|gamma(x)gamma(y)G|0>=c0[ax.by-ax^T Z ay].
The minus sign follows from <0|a_i a_j exp(a^dagger Z a^dagger/2)|0>=-Z_ij. These are bilinear contractions without complex conjugation.

The reference route independently constructs all 2^n-dimensional Jordan-Wigner gamma matrices, H=(i/2)sum_(a<b)K_ab gamma_a gamma_b, and ordinary Hermitian spectral exponentials. No Gaussian formula supplies its amplitudes.

## Fixed kernels and limitations

For each of the five ordered star-pair orbit representatives, use times (0,0), (1/128,1/64), (1/64,1/64). For each time compare:
1. <E_C(t)E_A(s)>;
2. <E_C(t/2)J_C E_C(t/2)gamma_v E_A(s)>;
3. <E_C(t)gamma_v E_A(s/2)J_A E_A(s/2)>.
Here Delta K_A=v d_A^T-d_A v^T and J_A=i gamma(d_A), as in the reviewed imaginary-time identity. The latter two are fixed midpoint insertion integrands, not quadratures for Z_A. All 45 values and timings are retained. No orbit multiplicity is used to infer an integrated scalar.

The short times guarantee an unambiguous chart and test normalization, ordering, insertion signs, and implementation cost. They do not test long-time conditioning at the infinite tail cutoff, large-carrier scaling, spatial truncation, or a sign of alpha. A successful result is a necessary implementation gate only.
