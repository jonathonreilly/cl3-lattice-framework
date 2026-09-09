# Native low-frequency projector tail: better constant and zero-frequency subtraction

Source-only new certificate proposal. No actual scalar, resolvent, matrix, quadrature or old numerical outcome is evaluated. Work in dimensionless hopping units h=1; the frequency variable is s/h and projector errors are dimensionless. The opposite projector convention flips every correction sign, not the error bounds.

## 1. Exact provenance of the existing coarse bound

LOW_RANK_PROJECTOR_CERTIFICATE.md in native-node-stable-imaginary-time-stretch proves, for F(s)=(H_A-is)^-1-(H0-is)^-1 and the NEGATIVE spectral projector,

 D=-(2pi)^-1 integral_0^infinity (F(s)+F(s)*)ds,
 eta <=(357/25)2^-Jlo+2*2^-Jhi+429(4/25)^p.

The first term uses the earlier very loose Woodbury bound C0<1071/25. The second uses ||F(s)||1<=2beta/s², beta<3. The third is trace-norm Gauss approximation on the complex disk/ellipse rho5/2. The scalar rho5 ellipse proof does NOT automatically improve this operator-valued resolvent ellipse.

At the fixed66-node schedule Jlo7,Jhi4,p6, the three rational bounds are357/3200,1/8,429(4/25)^6. A separate1/200 prospective input/arithmetic allocation produces the reviewed<1/4 bound. These are upper bounds, NOT lower floors on actual error. Sharper scalar data can reduce the arithmetic component; they do not by themselves establish a smaller omitted-frequency tail. This note re-proves the low component without changing any completed protocol.

## 2. Exact two-link zero-frequency inverse

Use normalized local columns U=[e0,d/sqrt2]. They are orthonormal. The actual two-link perturbation is U V U*, ||V||=beta=2sqrt2<3. From the native2x2 source formula in native-weighted-impurity-projector-stretch, Dscalar(0)=1/6 gives

 V G(0)=G(0)V=-(2/3)I,  G(s)=U*(H0-is)^-1 U.

Hence K(0)=(I+VG(0))^-1=3I and T(0)=3V. This is an exact rank-two native identity, not a generic impurity assumption. For both geometries, the local inverse columns X0=H0^-1 U exist in l2 and

 ||X_s||HS²<=L²=2a=17/30,  a=17/60,
 ||G(s)-G(0)||<=L² s.

The second estimate is the local resolvent identity followed by the product of the two local-column norms. It requires only those inverse columns, not a bounded H0^-1 operator or a gap.

For0<=s<=epsilon=1/128,

 ||K(s)||<=3/(1-3 beta L² s) <=3840/1229 <25/8.          (1)

Thus ||F(s)||1<=L² beta ||K(s)||<85/16. Merely replacing the old low-frequency constant gives the new safe omitted-low bound85/6144, approximately one eighth of the old357/3200. This alternative needs no new zero-frequency correction and can in principle recertify the same exact66-node candidate, but is a NEW analytic certificate, not an altered original outcome.

## 3. A finite-rank endpoint correction

The source IR derivative bound -A'(s)<=3 for0<s<=1 implies A(0)-A(s)<=3s. For the normalized perpendicular neighbor column Bgeo=A. For the opposite neighbor Bgeo=(1-s²A)/6, its decrease is at mosta s²/6<=3s. By the scalar spectral identity,

 ||X_s-X0||HS² = [A(0)-A(s)]+[Bgeo(0)-Bgeo(s)] <=6s.    (2)

This identity includes both frequency signs. It is a norm-square identity, not a derivative of the Hilbert-space vector at zero.

Woodbury gives F(s)=-X_s T(s) X_-s*, T(s)=K(s)V. Since

 ||T(s)-T(0)||<=3 ||K(s)|| beta² L² s,

three-factor telescoping around F0=-X0(3V)X0* gives

 ||F(s)-F0||1 <=sqrt(6s)L beta(||K(s)||+3)
                       +3||K(s)|| beta² L^4 s
                <=(5439/160)sqrt(s)+(867/32)s.          (3)

The constants use sqrt(17/5)<37/20, beta<3, and(1). F0 is Hermitian. Include the explicit negative-projector low correction

 Q_low=-(epsilon/pi)F0 = +(3epsilon/pi) X0 V X0*.        (4)

Its rank is at most2. The remaining low-tail error is bounded by

 eta_low_new <=(2/9)(5439/160)epsilon^(3/2)
                    +(1/6)(867/32)epsilon²
              <=(2/9)(5439/160)/(128*11)
                    +(1/6)(867/32)/128² <3/500.        (5)

Here sqrt(1/128)<1/11 and pi>3. No A0 numerical value is needed for this bound. Actual coefficients/mixed Gram entries of X0 must still be certified before using(4) numerically.

## 4. What additional columns are required

X0 comprises the inverse-center vector and inverse signed-neighbor vector. The latter is a Ward inverse-column direction; the center inverse is another explicit l2 direction. Their reference-Gamma partners must be included in a physical closure. Being expressible from local seeds does NOT mean those inverse columns already lie in the selected24 trial span. This is a new candidate/bank augmentation proposal. A signed implementation must use the canonical rephasing and exact V; the bound is insensitive to that unitary rephasing, the correction matrix is not.

These two zero-frequency columns are distinct from evaluating an oracle at a smaller positive pole. Their Gram uses the already finite A0-type limits and mixed resolvent identities. A source-bound evaluation/error ledger and resource protocol remain necessary. No exact singular inverse on the whole Hilbert space is proposed.

## 5. Limitation of further Taylor subtraction

At a3D Dirac node, the local inverse column H0^-1 e0 is l2 but H0^-2 e0 is not: the latter norm behaves as integral r²/r^4 dr nearzero. Accordingly the zero-frequency resolvent vector need not have a Hilbert-space derivative. The square-root variation in(2) is the expected threshold behavior. It is not legitimate to subtract a finite rank linear Taylor term in X_s with an unbounded derivative and claim an O(epsilon²) projector error. Further improvement needs an explicit threshold-vector or spectral decomposition, or more low-frequency intervals. Scalar elliptic analyticity alone does not remove this vector-domain obstruction.

The whole revised error is the re-proved low term plus the unchanged quadrature term and a separately proved high term, plus actual input/arithmetic errors. James is independently deriving high moment subtraction. No final practical rank, actual error or alpha benefit is claimed.
