# Coordinate-free certificate of the same selected-span leakage

SOURCE-ONLY new certificate method. No history, native Gram, scalar catalog, selected entry or physical action was read/evaluated. Keep the exact physical midpoint family, selected order and original trial domain. Let S=F E have p independent real columns and K be the supplied bounded real skew generator (H=iK). All following bounds scale with h: G is dimensionless, J has units h, D and leakage-square have units h². The target remains delta<=h*1e-6; no threshold is weakened.

## Exact invariant quantity

Set G=S* S>0, J=S* K S (real skew), D=(KS)*KS. The orthogonal projector is P=S G^-1 S*. The residual map B=(I−P)KS obeys

 B*B = L = D+J G^-1 J >=0.

Indeed (KS)*S=−J, so subtracting (KS)*S G^-1 S*KS adds JG^-1J, a negative semidefinite term. For any isometry V onto range S,

 delta²=||(I−P)KV||²=max_(x!=0) (x*Lx)/(x*Gx)
 =||G^-1/2 L G^-1/2||2.

This is independent of orthonormal gauge. It is exactly the leakage entering the existing gap-free propagation theorem. Individual original-family coefficients need not be enclosed to the historical full-width2^-39 gate to establish this scalar assertion. A certificate of delta alone is not a certificate of every coefficient or Gaussian state coordinate; those are separate claims below.

The joint block Gram [[D,−J],[J,G]] is positive semidefinite, and L is its Schur complement. Thus structural PSD of L is a proof premise inherited from the exact action data, not a numerical clipping convention. The formula uses the same correlated G/J/D induced by S and KS; independently admissible entry boxes only provide an over-enclosure and do not redefine the physical family.

## A posteriori rational preconditioning and inverse bound

Choose any exactly represented square candidate T. No floating factorization accuracy is assumed. Form certified enclosures of

 H=T*GT, A=T*JT, C=T*DT.

If a rigorous norm bound e>=||H−I||2 satisfies e<1, then H>=a I with a=1−e>0. This also proves T invertible and G positive definite. The exact residual in these coordinates is N=C+A H^-1 A=T* L T>=0.

Choose any exactly represented symmetric X as an approximate inverse of H. Certify r>=||I−H X||2. Since H^-1−X=H^-1(I−HX),

 ||H^-1−X||2<=epsilon=r/a.

Symmetrizing a nonsymmetric proposal first is harmless provided its residual is recomputed. Neither a matrix solver's nominal accuracy nor a condition-number guess is imported. A trivial X=I yields epsilon<=e/a; higher accuracy may be needed to resolve cancellation. Finite Neumann polynomials or a rational approximate inverse can be checked by the same residual test.

Let b>=||A||2. Let N0 be an exact rational symmetric center for C+A X A and let z bound its matrix arithmetic/input enclosure error in operator norm. Then

 ||N−N0||2<=q=z+b² epsilon.

All quantities H,A,C share the true physical data; interval computation may safely overbound dependency, but no favorable covariance of uncertain entries is assumed without proof. Candidate T, X are exact rational data. Their rounded generation creates no hidden error: verification uses the exact represented candidates.

A directly computable sufficient upper bound is

 delta² <= [max(0,lambda_upper(N0)+q)]/a,

where lambda_upper can be any certified upper spectral bound, e.g. maximum absolute row sum for symmetric N0. The nonnegative maximum uses exact N>=0, not clipping an uncertain Gram pivot. An implementation may more sharply certify N<=d²H by checking a symmetric interval bound on d²H−N; the displayed scalar formula is sufficient and easy to audit. Passing requires the SAME d²=(h*1e-6)².

A useful lower bound needs no eigensolver: for any exact test vector u (including one coordinate), obtain a certified numerator lower ell<=u*N u and positive denominator upper g>=u*H u. Then delta²>=max(0,ell)/g. For u=e_i, ell=N0_ii−q and g any positive upper H_ii. A positive lower bound exceeding the target disproves only that selected span's optional target; it is not a general no-go.

The inverse bound can avoid excessive Frobenius dimension loss by using certified1/infinity matrix norms, their geometric mean, or an exact row sum when symmetric. Frobenius remains safe. The numerical usefulness of a and q must be determined by a new source-bound probe; no native pass is predicted.

## Required native data and operation counts

For k paired selected seeds from the ORIGINAL399-raw family, p=2k and E has at most4k distinct raw/Gamma labels R. The already proved first-action identity K F_R=F_R Lambda+QY uses only the eight real Q labels (center/qA/qC/qD and Gamma partners), hence U=R union Q. The existing3q804 DATA is sufficient for this ORIGINAL-domain certificate. No p=Kq or nu is needed unless q is admitted to the TRIAL domain; doing so requires405/810 DATA and is a different proposal.

Compute G=E* M E, action columns B0=(Lambda E plus the exact rank-two correction), J=E* M B0, D=B0* M B0, using the same physical-inflated principal DATA M and exact source scales. Equivalently exploit the sparse F_R Lambda+QY representation to avoid dense raw contractions. Do not commute the impurity correction through Gamma. The literal minus/plus signs remain those of the reviewed original first-action map.

At k24, |R|<=96 and |U|<=104; a full upper principal DATA block has at most5460 real entries/orbit. For selected G and source blocks ONLY, the selected paired G can use k² real scalars with at most4k²=2304 raw requests/orbit, supplemented by R-Q and Q-Q entries (at most8|R|+36); this reduced count does NOT suffice for D unless an additional closure identity is proved. Lambda E need not remain in range E; Gamma closure is not Lambda closure. Additional M_RR entries for the action are required, and the full5460 principal-block count is the safe acquisition plan. Known/raw cache reuse can reduce duplicates. These are upper acquisition counts, not a measured cost. Products for H,A,C/residual/N are O(p³), p<=48, plus sparse embeddings. Fixed-point or exact rational bit caps and interval endpoint storage must be priced explicitly in a new runtime. Existing4-action output does not automatically provide all24selected R-Q entries.

## Gauge and downstream state obligations

For the exact historical ordered GS frame Vord, the projector is still P and delta is identical; therefore this certificate can establish its leakage without resolving C entrywise. If another exact isometry W=Vord O is used computationally, the compressed generator and all insertion coordinates must transform by the SAME orthogonal O (and its covariance/Fock lift where required). One may not keep old coordinates while substituting W.

A projector/action leakage result supports the gauge-invariant propagation estimate already proved for exact V. To compute a Gaussian amplitude or a state in fixed external coordinates, one still needs certified source projections, compressed generator representation, coefficient/frame or alignment errors, and applicable many-body error propagation. The former full-width2^-39 C gate remains binding for claims that explicitly depend on that coefficient certificate; this method does not relabel its failure as a pass. It establishes a different sufficient certificate for the unchanged leakage target, and may permit downstream projector-based arguments to avoid an unnecessary entrywise interface.

No actual delta, positive lower bound, conditioned inverse, or propagation/state error has been supplied here. Next useful bounded source work is a rational midpoint T/X proposal plus fixed-point certificates for H,A,C and inverse residual, on a frozen selected sequence, with all partials retained. It should first expose a, b²epsilon, z and the cancellation scale separately so a failed result diagnoses information precision versus arithmetic or genuine leakage.
