# Finite-order local ring approximation on the full native carrier

Conditional finite-volume theorem, with constants independent of volume. This proof was developed without reading root's new finite-order proof. The completed applicability note and the canonical full-carrier coefficient calculation are inputs. No optimal-prethermal theorem is used below.

## 1. Model, norm, and strong support

Take even periodic cubic extents at least four, edge qubits, H=UD+g sum_e lambda_e A_e, U>0, D=sum_v Q_v², full carrier and relaxed cycle constraints. Let lambda_* = sup|lambda_e|, x=g lambda_*/U, and H/U=D+x V, with V=sum_e(lambda_e/lambda_*)A_e; the zero-coupling case is exact. Signs are allowed. The geometry, penalty and couplings are supplied, not selected.

Use physical edges as tensor sites, with adjacency when they share a cubic vertex. Assign A_e the complete union of its two endpoint stars S_e, size11. It is strongly supported: [A_e,Q_v²]=0 whenever star(v) is not contained in S_e. Strong support is preserved by sums, charge averaging, and commutators (on the union); disjoint supports commute. In particular [B_S,D] is supported on S, not an enlarged neighborhood. These statements follow directly because the charge-star terms commute. All supports constructed below are connected, since only overlapping commutators survive.

For a specified potential Phi=(Phi_S), set ||Phi||_k=sup_i sum_{S containing i} e^{k|S|}||Phi_S||. The potential is part of the construction; this is not a claim about a unique interaction decomposition. At k=0, ||D||_0<=18 (two stars of norm9 per edge) and ||V||_0<=11 (an edge belongs to at most11 endpoint-star unions). At k=1 these are bounded by18e^6 and11e^11. Periodic identifications do not increase either bound.

If potentials B,C have maximum support sizes b,c, assigning commutators to unions gives

  ||[B,C]||_k <= 2(b+c)||B||_k||C||_k.                 (1)

Proof: for a fixed site i, split overlapping pairs according to i in the first or second support. Sum the partner using an intersection site, costing at most b or c; e^{|S union T|}<=e^{|S|}e^{|T|}. No volume factor appears.

## 2. Support-preserving inverse and a completely explicit recursion

For a strongly supported term B define

  P_D B=(2pi)^-1 integral_0^{2pi} e^{itD}B e^{-itD} dt,
  Gamma B=(2pi)^-1 integral_0^{2pi} i(t-pi)e^{itD}B e^{-itD} dt.

Integer D makes the average the exact D-conserving part. On energy difference m nonzero, Gamma multiplies by1/m, hence [Gamma B,D]=-(B-P_D B). Gamma takes Hermitian B to anti-Hermitian operators and has norm <=pi/2, so <=4 is a safe bound. Both maps preserve the assigned strong support. Averaging has norm<=1. These facts hold for the overlapping stars; no onsite hypothesis is being substituted.

Construct S(x)=sum_{j=1}^5 x^j S_j recursively. Let F_n be the coefficient of x^n in exp(ad(sum_{j<n}x^jS_j))(D+xV). Set

  S_n=Gamma F_n,       K_n=P_D F_n.                   (2)

The x^n coefficient after adding S_n is exactly F_n+[S_n,D]=K_n. Every assigned K_n term commutes with D. Inductively S_n,F_n,K_n have connected support size<=11n: the innermost commutator with D does not enlarge strong support, and all other supports add. S(x) is anti-Hermitian for real x; Y=exp(S(x)) is an actual finite-volume unitary, not a formal similarity only.

Here is an explicit rational majorant, so the smallness statement below is not hiding a volume-dependent coefficient. Write s_n=4 f_n. For n=1,...,5, using previously determined s_i, define f_n as follows. Sum over ordered positive compositions (i_1,...,i_l), with i_j<n; let p_j=i_1+...+i_j. The D contribution has total n and l>=2 and is

  18 sum [ product_{j=1}^l (2(6+11p_j)s_{i_j}) ] / l!.

The V contribution has total n-1 and l>=0 and is

  11 sum [ product_{j=1}^l (22(1+p_j)s_{i_j}) ] / l!.

The empty composition contributes11 only for n=1. These bounds apply (1) to nested commutators from the inside outward, allowing an unnecessary extra six sites for the D term. They imply ||F_n||_0<=f_n and ||S_n||_0<=s_n. The omitted l=1 D term would be S_n itself and is precisely what (2) solves. This finite recursion involves only rational arithmetic and fixed n<=5.

Put s=sum_{n=1}^5 s_n and define the explicit constants

  rho=1/[440*3^55*max(1,s)],
  M=2(18*3^6+11*3^11),       C_R=2M/rho^6.           (3)

These constants are extremely conservative, not accuracy estimates for useful laboratory couplings.

## 3. Convergent Lie series, exact remainder, and local regime

For complex |x|<=rho, S has maximum support55 and ||S(x)||_1<=3^55 |x|s<=1/440. For a potential B of support size b, repeated (1) yields

  ||ad_S^l B||_1/l! <= ||B||_1 (110||S||_1)^l
                         product_{j=1}^l(j+b/55)/l!.

The sum is (1-110||S||_1)^(-1-b/55). For b=6 or11 it is less than2 at110||S||_1<=1/4. Therefore the exact transformed interaction exp(ad_S)(D+xV) is analytic in this disk, has norm<=M, and agrees with the unitary conjugation for real x. The interaction series converges uniformly independent of volume. Complex x is used solely to estimate coefficients, not to claim a physical nonunitary evolution.

Cauchy's estimate in this potential norm bounds every coefficient by M/rho^n. The recursion has removed its off-diagonal coefficients through degree5. For |x|<=rho/2,

  Y H Y† = UD + K + R,
  K=U sum_{n=1}^5 x^n K_n,       [K,D]=0,
  ||R||_1 <= C_R U |x|^6 = C_R gamma^6/U^5,          (4)

where gamma=|g|lambda_*. This is an exact decomposition with a quasi-local remainder, not equality modulo a formal series. Also ||K||_1<=2M gamma/rho. R is a sum of connected strongly supported terms. The sufficient regime gamma/U<=rho/2 and every constant in (3) are independent of volume. We claim no optimal constants or exponential-time approximation by K4 alone.

## 4. Which ice Hamiltonian is obtained?

The global bit-parity operator Z_all commutes with D and negates V. The recursion preserves the degree grading: Z_all S_n Z_all=(-1)^n S_n and likewise K_n. Every ice basis vector has3N/2 occupied bits, so Z_all is scalar on the whole ice space P. Consequently P K_1 P=P K_3 P=P K_5 P=0. The second coefficient is the scalar -sum(lambda_e/lambda_*)²/(2) times P.

The fourth coefficient agrees with the already fixed canonical direct-rotation H4, not merely up to an unspecified fourth-order ice gauge. To see this, fix any one finite volume and take a sufficiently small neighborhood where its Riesz ice projection exists. This temporary neighborhood may shrink with volume; it is used only for coefficient identification. Since YHY† is D-block-diagonal through degree5, a further near-identity correction starting at order6 maps the exact ice projection to P. Compare that exact map with canonical direct rotation: their restrictions differ by a near-identity unitary on P. Conjugating an effective series whose terms below degree4 are zero or scalar cannot alter its degree4 coefficient. This algebraic coefficient identity therefore holds at every volume, independently of that auxiliary spectral neighborhood. It is not a uniform global band theorem.

Thus, on P, K is exactly the second scalar plus the complete fourth operator:

  P K P= -g² sum lambda_e²/(2U) P + g^4 H4,

with the canonical full-carrier diagonal scalar and coefficients eta_C product(lambda_e)/(2U³) F_C S_C. Extent-four winding four-cycles must be retained. The fourth scalar also drops from dynamics. After the stated physical Zpi conjugation, comparisons with a negative-ring model must transform states and off-diagonal observables too. No RK flippability potential has appeared.

## 5. Local dynamics and dressing, without a speed proportional to U

A standard finite-range commutator estimate can be derived directly here. For connected potentials of norm||K||_1, the iterated commutator expansion connects an initial support X to an interaction support Z by a chain of overlapping supports. Allocate half the e^{|S|} weight to intersection counting and half to distance. Summing these chains bounds the commutator by an exponential light cone with speed v=C_geom||K||_1 and exponentially decaying distance tail, capped by2||O||||B_Z||. C_geom is a fixed finite geometric constant: it can be chosen from the convolution sums of exp(-dist/4)/(1+dist)^4 on the edge-adjacency cubic graph. More explicitly take F(r)=exp(-r/4)/(1+r)^4, S_poly=sup_x sum_y(1+dist(x,y))^-4<infinity, and C_F=32 S_poly. The convolution sum of F(x,z)F(z,y) is at most C_F F(x,y): split according to which distance is at least half dist(x,y), use the triangle inequality for the exponent, and sum the remaining fourth-power denominator. Also C_0=sup_{m>=1}(1+m)^4 exp(-3m/4)<infinity gives the pair interaction F-norm at most C_0||K||_1, since connected support diameter is at most its cardinality. Iterating the Duhamel commutator inequality sums the convolution chains with their time simplex factor t^n/n!, yielding an exponential factor exp(2 C_F C_0||K||_1 |t|). These definitions specify finite volume-independent constants rather than a fitted velocity. In summing over R supports, min(1,sum_{z in Z}a_z)<=sum_{z in Z}min(1,a_z) allows anchoring every term at z and using ||R||_0; no number-of-supports or volume factor remains. The polynomial growth bound |ball(r)|<=C(1+r)^3 is uniform on all these tori.

For completeness, the consequence needed here is

  sum_Z ||[R_Z, alpha_s^K(O_X)]||
       <= C_X ||O_X|| ||R||_1 (1+v|s|)^3.           (5)

It follows by summing the capped light-cone estimate: inside radius v|s| the number of anchors is O((1+v|s|)^3); outside, sum the exponential shell tail. The extra |Z| and intersection factors are absorbed by the reserved exponential support weight. C_X is finite and depends on the fixed support X and geometry, not total volume. This argument is valid for time-dependent R_Z(s) with the same support/norm bound. It is the usual elementary Lieb-Robinson/Duhamel proof, not a new general locality theorem or an imported prethermal estimate.

Now remove UD in the interaction picture. Every K_n term commutes with D. Every R_Z is strongly supported, so e^{itUD}R_Ze^{-itUD} remains on Z and its norm is unchanged. Thus (5), followed by Duhamel and unitary norm preservation of the outer full evolution, gives for any dressed-frame local observable O_X

 ||alpha_t^{YHY†}(O_X)-alpha_t^{UD+K}(O_X)||
   <= C'_X ||O_X|| C_R gamma^6/U^5 |t|(1+v|t|)^3. (6)

For an O not commuting with D, its final free-D rotation has support enlarged only by the charge stars meeting X: all charge-star terms commute, so there is no cascading spread. This enlargement has at most11|X| edge sites and bounded radius, independently of U t. Apply (5) to that enlarged support. This proves why v can be bounded in terms of gamma, not U. The constants are geometry/support constants in addition to the explicit algebraic constants(3); they do not depend on volume or t.

In laboratory variables the directly controlled comparison uses observable Y†O_XY, or equivalently dresses a supplied laboratory observable by Y. A local observable changes under this dressing by at most C_X'' gamma/U times its norm. This follows from the same convergent nested-commutator series for S, with ||S||_1<=3^55 s gamma/U; its quasi-local tail permits applying(6) termwise. This bound is not an extensive/global norm estimate for Y-I.

For any ice-supported density matrix rho, prepare the laboratory state Y†rho Y. With laboratory observable Y†O_XY, its exact expectation differs by(6) from the expectation under the fourth-order ring Hamiltonian on ice. UD and the second/fourth scalar terms act trivially there; K preserves P exactly. No global-norm closeness of bare ice and dressed ice is assumed. Bare ice initialization may not be replaced by this preparation without its own error estimate; local dressing is not a theorem that the probability of any defect in a whole large volume is small.

The useful guaranteed time regime is the explicit polynomial condition (gamma^6/U^5)|t|(1+C_geom(2M/rho)gamma|t|)^3 small, multiplied by the stated constants. This is a finite-order local approximation, not quasi-exponential ring-only accuracy, a thermodynamic phase result, or a selected physical action.
