# Constructive common impurity basis from certified local Grams

New bounded analytic design. No physical scalar integral, Gram matrix, compression rank, or native kernel has been computed. The objective is an a posteriori finite-excitation basis, not a claim that the previous worst-case rank is attained or can already be reduced.

## 1. Exact shared symmetry blocks

Use the seven source vectors center and +/- coordinate neighbors, and the matrices N=I+O,T of the local Green derivation. Define normalized neighbor combinations
s_a=(e_(+a)+e_(-a))/sqrt(2), w_a=(e_(+a)-e_(-a))/sqrt(2),
w0=(w_x+w_y+w_z)/sqrt(3).
Let E be the two-dimensional orthogonal complement of w0 within span(w_x,w_y,w_z). The matrices I,O,T simultaneously preserve:

* the coupled two-dimensional space span(center,w0), where T_(center,w0)=-sqrt(6);
* three identical one-dimensional s_a channels;
* two identical one-dimensional E channels.

Indeed O is +1 on s_a, -1 on w_a, zero on the center, and T couples only center to w0. Every full and P0-projected local resolvent Gram is a linear combination of these matrices, so this decomposition holds for ALL pole pairs and their confluent limits, not just for one sampled Gram. If q pole/sign labels are retained, the common data consist of one 2q block and two scalar q blocks, reused with multiplicities three and two. This reduces repeated matrix construction and exposes exact degeneracies; it is not an a priori truncation.

For this paragraph only define unnormalized bars: bar_s_a=e_(+a)+e_(-a), bar_w_a=e_(+a)-e_(-a). For the actual defect d_A/(2h), an opposite pair is bar_w_a. A perpendicular pair (sigma a,tau b) is (sigma bar_s_a+bar_w_a+tau bar_s_b+bar_w_b)/2. Applying this to the five ordered pair representatives gives the following neighbor-channel ranks for their shared span:

| pair class | symmetric rank | E rank |
| opposite/opposite |0|2|
| opposite/perpendicular |1|1|
| perpendicular/opposite |1|1|
| opposite-sign perpendicular pairs on same axes |1|1|
| remaining perpendicular pair class |2|2|

The center/w0 block is common. Completing by these channels gives at most four q channels in the first four cases and six q channels in the fifth. It may overcomplete the original source span; no smaller exact physical rank is claimed. Crucially all five geometries use one common pole convention and the same covariance matrices, so cross-impurity phases are not lost in separate normalizations.

## 2. Balance the finite-rank operator before compressing columns

The stationary quadrature gives a Hermitian finite-rank Q=V C V^dagger approximating P_A-P0. Bare columns are resolvents at both signs of the imaginary poles. For one node, F(is)=-X_+ T_s X_-^dagger; adding its adjoint gives an off-diagonal Hermitian coefficient block. Its absolute value is block diagonal with the two square roots of T_s T_s^dagger and T_s^dagger T_s. Thus a balanced representation

 Q=Y J Y^dagger, Y=V |C|^(1/2), ||J||<=1

uses only two-by-two coefficient factorizations per node. A common union of the balanced columns for both impurities must be used. The matrix G=Y^dagger Y is the weighted Gram, not the unweighted Gram of many nearly identical low-frequency columns.

This matters because Tr G is bounded using the same factor-norm majorants that bound the quadrature contributions: each node contributes Tr(|C| V^dagger V), bounded by ||C|| times the squared Hilbert-Schmidt column norm. A bound solely on the trace norm of the summed Q does NOT bound Tr G, because cancellations can reduce Q. Any numerical stopping rule must use an actual certified Tr G or a valid factor-norm majorant, rather than reuse 87 without proving that stronger bound. Low-pole weights shrink with their dyadic interval. It does not remove all conditioning: the columns still become nearly dependent as poles approach zero.

If Pi is a subspace projection, put r=Tr[Y^dagger(I-Pi)Y]. Schatten Cauchy-Schwarz gives

 ||Q-Pi Q Pi||_1 <=2 sqrt(Tr G) sqrt(r).                 (1)

Proof: expand the difference as (I-Pi)Y J Y^dagger+Pi Y J Y^dagger(I-Pi), and apply the Hilbert-Schmidt product bound to both terms. A certified upper bound on r and on Tr G therefore supplies an actual stopping certificate. It does not require guessing a numerical singular-value threshold.

For a target epsilon, the sufficient residual is r<=epsilon²/(4 Tr G). This may require very accurate Gram inputs. For example, if a factor-norm bound near87 were established and epsilon=10^-6 demands a residual of order10^-15. The current width1/32 Green pilot cannot certify that. No claim of practical high-precision compression is made before actual interval costs and a posteriori residuals are known.

## 3. Close under the reference covariance and use paired pivots

In a real CAR representation let Gamma0²=-I be the pure reference covariance. The bare resolvent columns can be rephased to real columns; retain the corresponding imaginary skew coefficient in Q. Let

 G=Y^T Y, J0=Y^T Gamma0 Y.

These are obtained from the full and projected Gram matrices by
Y^dagger P0 Y=(G+i J0)/2.
The enlarged span of Y and Gamma0 Y is Gamma0-invariant and has Gram
[[G,J0],[-J0,G]]. Its reference Gaussian state is PURE. This closure is specific to this finite-excitation construction and does not justify replacing a generic Krylov restriction by sign(K_m).

Construct an invariant basis greedily in pairs. For a residual column y_i with r_i=G_ii>0, choose a=y_i/sqrt(r_i), b=Gamma0 a. They are orthonormal, and the reference covariance on (a,b) is [[0,-1],[1,0]]. Project all columns off both directions. If g=G_(i,:) and j=(J0)_(i,:), the exact residual recurrences are

 G_new=G-(g^T g+j^T j)/r_i,
 J0_new=J0-(g^T j-j^T g)/r_i.                           (2)

No large Gram inverse is needed. Each pivot normalizes one positive scalar. The pair orientation b=Gamma0 a fixes the CAR covariance convention; choosing it independently for each impurity would lose shared signs. The source can store each basis pair as coefficients in the original columns and their Gamma0 images, without any infinite ambient vector.

With interval inputs, choose a pivot only when its lower bound is strictly positive. If its interval includes zero while the residual bound is still too large, request higher precision from the original moment evaluator; do not clip it positive or declare it negligible. Outward interval evaluation of (2) gives a valid, possibly pessimistic residual upper bound. A deterministic pivot rule, precision escalation rule and complete retained history would need a new protocol before physical Gram work.

The final basis is shared across both impurities, central gamma and J insertions, with all their signed cross contractions. The reference vacuum then has the fixed standard covariance in this basis. Spin phases of the subsequent dynamics still require their own continuous lift; a Gram basis alone does not determine a quench overlap sign.

## 4. What a useful next finite test would establish

At modest error first, evaluate certified local scalars at a fixed small pole set; assemble all three symmetry blocks and their cross-impurity coefficients; run paired interval pivots and report r and Tr G after each pair. A small residual would certify useful compression. An interval stall would identify the needed scalar precision, and a slowly decreasing residual would falsify the hoped-for small rank at that pole set. None of these outcomes can be inferred from the existence bound or the five-mode L4 fixture.

Only exact synthetic algebra controls accompany this design. No new physical job or cost run is proposed for execution here.

## 5. Supporting controls and present cost boundary

The accompanying standard-library exact rational check verifies 125 predicates: paired updates against ambient projections, covariance invariance, complete exhaustion of a synthetic eight-dimensional space, and the seven-source symmetry blocks. Dropping the covariance partner or reversing the skew update sign actually disagrees with the ambient calculation. These are direct algebraic adverse controls, not isolated mutated-process tests.

The completed separate Green pilot at s=1,2 achieved width 1/32 for eight scalar quantities in four jobs; root reports external 0.63 seconds and 66,895,872-byte whole-tree peak. Its hardest B job used 2,234 leaves. This provides a coarse starting cost only. It does not price the much narrower enclosures, divided differences, or near-zero poles needed for a successful compression certificate. No physical Gram has been assembled here. The next genuine gate is a fixed modest-error pole set with certified factor-balanced trace and residual, including an explicit INDETERMINATE outcome for interval pivot stalls.
