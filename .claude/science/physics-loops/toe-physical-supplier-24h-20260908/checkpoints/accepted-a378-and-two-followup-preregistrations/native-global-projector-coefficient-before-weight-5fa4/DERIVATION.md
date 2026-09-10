# Prospective A-only physical-column projector coefficients

Status: source-only candidate, NOT_READY for execution. No actual acquisition values, native columns, moments, Gram or operator evaluated. This code defines an operator by exact physical column descriptors. It does not produce a numerical wavefunction basis or certify a Gaussian consumer.

## Convention and exact assembly

Use dimensionless H0=iK0, U=[e0,d], ||d||²=2, V=2i[[0,1],[-1,0]]. For each positive midpoint s, G=U*R0(is)U=iM with M=[[sA,-2D],[2D,2sBgeo]], D=(1-s²A)/6, Bgeo=A for P and D for O. Set a=1-4D, d=a²+8s²ABgeo. Then T=(I+VG)^-1V=iQ with

 Q=d^-1[[-8sBgeo,2a],[-2a,-4sA]].

The source computes this from the exact rational midpoint of the A enclosure intersected with [0,1/s²] and checks (I-NM)Q=N exactly, N=V/i. It refuses an empty spectral intersection or nonpositive computed determinant. In the intersection, D>=0 and a>=1/3, so both classes have determinant>=1/9. Enclosure of the actual A(midpoint), and the uniform inverse estimates, are supplied by the bound acquisition and input-budget proof; positivity of an arbitrary supplied scalar alone does not establish a physical resolvent.

With X±=R0(±is)U, RA(is)-R0(is)=-X+ T X-* and the conjugate is its adjoint. Thus the positive-band difference has coefficient -w/(2pi)[[0,T],[T*,0]] in [X+,X-]. The negative-band difference is its negative. core.block_imaginary returns the real skew matrix whose product by i is that Hermitian coefficient. No unannounced rephasing or half-seed normalization is applied.

## Rounding and numerical error

Each real component of Q is rounded to the nearest2^-84 dyadic, ties upward. Error per entry is <=2^-85, so the2x2 operator error is <=2^-84, below the required2^-80. The implementation also computes the actual error and gates twice its largest entry. Final multiplication by exact rational midpoint weights and midpoint reciprocal pi is exact; it introduces no further rounding.

The imported budget is Einput<=2^27 epsA+2^42 rhos+2^13 rhow+5 epsT+2^12 rhopi. Each radius is an absolute radius, not a full width. The planned acquisition supplies fullwidth A<=1e-30 and geometry radii<=2^-160. The separate reciprocal-pi enclosure must have radius<=2^-180. core.reciprocal_pi_box supplies it from pi=16 atan(1/5)-4 atan(1/239), with40 and12 alternating terms. Each alternating tail lies between zero and its signed next term; positive reciprocal reverses the resulting endpoints. The exact radius gate passes in a pure rational control. Future runtime must bind this generator output, rather than accepting an arbitrary narrow box as proof of1/pi.

The function checks exactly378 ordered, separated positive root boxes in [2^-32,16], positive weights, midpoint weight sum<=17, literal integer IDs and declared shapes. This does not prove those roots and weights are the18-panel Gauss21 rule; the future authenticated loader must bind that producer certificate. Both classes use the same A data. No A' is required.

The analytic contribution is the sum of the reviewed low corrected remainder, high N15 remainder and ratio4 p21 quadrature bound. core.analytic_budget implements their exact rational constants. The final ledger is retained before the strict total<1e-12 gate. This bound holds separately for each impurity; it is not a joint sum over both impurity operators.

## Low and high descriptors

For the positive projector, the low approximation is -(epsilon/pi) X0(3V)X0*, X0=H0^-1U and epsilon=2^-32. The stored imaginary2x2 coefficient is therefore [[0,-6epsilon/pi],[6epsilon/pi,0]]. The inverse columns exist by the imported three-dimensional local resolvent estimate. They are exact descriptors, not computed entries.

The high correction is (1/pi) sum n=0..14 (-1)^n (HA^(2n+1)-H0^(2n+1))/((2n+1)16^(2n+1)). Every coefficient is explicit. The polynomial difference has the reviewed finite bare-Krylov representation of degree28/rank<=58; this source records the polynomial operator rather than performing a Gram calculation. Exact rational scalar arithmetic introduces no moment acquisition. These corrections and the node terms use the same positive-band convention and h=1 scaling; restore Hphys=hHbar and dimensionless frequencies consistently with SCALING_BRIDGE.

## Retention, cost and remaining closure

The retain callback must serialize durably before returning; it must not retain mutable Python references. Current inputs, exact/rounded Q, each4x4 imaginary coefficient, and final ledger are emitted. A future dispatcher must retain failures, verify all immutable input/source bytes and close resources. No dispatcher or accepted-input binder exists here.

Fixed work:378 nodes,7562x2 solves,756 residual checks and756 coefficient blocks. It uses no dense matrix larger than4x4. Streaming output contains these coefficients plus15 high coefficients and one low block per class; physical descriptors are symbolic. MAX_BITS32768 bounds stored rational components. Intermediate Fraction products/sums can exceed that before validation (a bounded2x2 sum has a conservative few-times32768 transient bit length); there is no current RSS/time contract. Input parsing and resource guards remain future runtime obligations. No timing forecast is claimed from the synthetic controls.

Fifty original synthetic checks use a deliberately nonnative one-atom scalar law, alternate determinant inversion, polarization/skew adjoints, signed dyadic rounding, malformed input refusal and the exact rational error budget. They are algebraic supporting controls, not an acquired projector certificate. No full378-row synthetic or native assembly ran.

The original1b8c source is preserved in the sibling before-spectral folder. Three additional nonphysical controls confirm the Machin radius, a boundary-straddling valid spectral intersection, and refusal of an empty intersection. Full original controls were not repeated.
