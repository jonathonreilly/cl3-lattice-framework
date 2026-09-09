# Independent weighted-projector review

Disposition: PASS as a constructive mathematical reduction with explicitly uncomputed input/error gates. This is not an achieved projector enclosure or an executable pilot authorization.

Reviewed complete DERIVATION.md 4bed5e618135d4c805936cdb86697848de80240c2eb9efeec91650291b2f25e1, UNIFORM_TRANSFORM.md fda1d5bf1e279775c837659327c2a10efdb9086d1a3d3174757de6e612b8592d, check.py, CONTROL_RESULT and FREEZE cba139dcc890158774cbd5222c82843ec3ebe4e2982668873ab08f4099a3419f. Also read the full imported LOW_RANK_PROJECTOR_CERTIFICATE.md. No new physical or synthetic computation was executed in this review. The supplied 105 scalar predicates are supporting controls only.

## Native coefficient and signs

Direct 2x2 multiplication gives I+VG=[[a,−4hsBgeo],[2hsA,a]] and determinant a²+8h²s²ABgeo. Multiplying its inverse by V yields exactly the displayed T+. Woodbury gives −X+T+X−*, and the negative-band projector has factor −1/(2pi) in the positive-s resolvent integral. Both signs therefore cancel as stated. The use of Bgeo, rather than the similarly named square-root Green scalar, is essential and correctly distinguished.

Hermitian block C has absolute value given by the two positive square roots of T+T+* and T+*T+ (including the scalar weight). Thus balancing really moves the physical weights into columns; it does not replace the actual coefficient by an arbitrary contraction. A trace norm of Q alone cannot control the balanced column Gram trace, as the source warns.

The covariance closure gives P0F=FJ0 and, by adjunction, F*P0=J0F*. Consequently M commutes with J0. The chiral pole-pair identity gives complement symmetry for the actual coefficient and commutation for its absolute value. A numerical implementation must preserve these exact transformations or charge their errors. Real rephasing is compatible with h0=iK: imaginary-axis bare resolvent columns are purely imaginary in the real site basis.

## Contour formula and the Gram-null-space issue

Let Rz=(zeta−P)^−1. The finite-rank identity gives

 (I−M r Cbar)^−1=I+F*Rz F Cbar.

It follows either by multiplying the two sides or from F*Rz F=(I−M r Cbar)^−1 M r. The commutation M r=r M, which follows from covariance closure, is necessary here and is available. Its norm is bounded by 1+4||F||²||Cbar||, hence by the stated trace bound. No smallest Gram eigenvalue enters. The circle's distance to the spectrum is at least 1/2−e>1/4; this justifies the physical inverse bound 4.

The contour formula is therefore a valid route even when M is singular. It does not license substituting M+epsilon I as a physical Gram matrix. A future contour implementation still needs verified inverse residuals and an integration remainder, not just existence of this bound.

## Polynomial route

Expanding (P0+FCF*)² and multiplying once more gives exactly D2 and D3 in the source; no inverses or quotient by a null space occur. Since range(F) is invariant under P0, its orthogonal complement is unchanged by every iterate and by spectral rounding. Thus the trace error bound rank(F)e_n is valid.

For either endpoint, the scalar error is at most 3e²+2e³ <=(7/2)e² for e<=1/4, including the outside portions of the two spectral intervals. This produces e_n <=(2/7)(7/8)^(2^n). Both interval components remain on their original side of 1/2. The symmetry f(1−x)=1−f(x) retains the complement symmetry; it does not by itself certify rounding parity or a Fock phase. These additional obligations are not claimed solved here.

## Schedule and uniform transform

The inherited trace error plus 1/200 is exactly the stated approximately 0.2487599, strictly below 1/4. Eleven panels times six nodes gives 66 nodes, 264 balanced columns, and 528 after covariance closure for ONE impurity. Concatenating two impurities can double this count absent a separately proved sharing/reduction. The 1/200 is an allocated operator/trace error budget that must be achieved by the future input/coefficient computation; it is not supplied by the arithmetic inequality itself.

For the transform, rescaling theta by 2/pi and extending the positive integrand to R3 gives −A′<=pi²/32, with no missing octant or measure factor. Maximization of 2y/(1+y²)² gives 9/(8sqrt(3)), so the E0 estimate follows from Cminus<7/15. On the stated ellipse, x²−y² has its minimum at the left real endpoint: its derivative with respect to cos(angle) is positive throughout the interval. Hence Re(z²)>0 and the improved near-zero bound is justified. The whole ellipse lies in the radius-c/2 disk, which supplies the far bound. The dyadic envelope sum 20/9 and resulting (400/27)(4/25)^p follow. Positive moment remainders give the stated uniform high-tail bounds for both G and H.

## Remaining constructive gate

This is a genuine finite-dimensional reduction of the actual weighted projector, rather than a generic coefficient-ball statement. It does not yet provide the 66 pole inputs, certified balancing operations, weighted Gram, purification arithmetic growth, or a cost bound. Existing fixed s=1,2 values cannot fill those gaps. Pole/catalog separation or an implemented confluent formula is mandatory. In a production source closure, the imported low-rank/trace-class and scalar-transform proofs must be pinned along with the local files. The current research freeze pins its local five files only; this is not a full runnable dependency closure. These limitations are consistent with the proof's explicitly prospective scope, and do not invalidate the mathematical reduction.
