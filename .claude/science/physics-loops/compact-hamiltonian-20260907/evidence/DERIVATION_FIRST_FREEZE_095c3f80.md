# Actual compact SU(3) Hamiltonian limit on the full finite cube

Independent derivation following PREREGISTRATION.md SHA002cfcef29b3a496b98041d1b97128328c6ddcb009145ecf12e6f31a823ef065. No root new proof or result was read. This is a new explicitly supplied anisotropic scaling of the FULL24-face transfer, not the earlier boundary-state Gaussian localization. Parameters a>0 and v>=0 and mathematical time t remain supplied. The potential is kept as the exact compact plaquette function.

## 1. Hilbert space, normalization and generator conventions

Let G=SU3^12 with normalized product Haar, Hlink=L2(G), and Hphys its subspace invariant under the eight vertex gauge transformations. The previously proved full-transfer reduction and gluing apply to arbitrary positive spatial/temporal couplings. Write J(U)=ReTr(U)/3 and

 V(U)=v sum_(six spatial faces)(1-J(U_face)),
 p_s(g)=exp(sJ(g))/c0(s),  c0(s)=integral exp(sJ(g))dg.

V is bounded, smooth, gauge invariant and nonnegative. In particular V<=12v is a sufficient conservative bound because |J|<=1. For h>0 define B_h=exp(-hV/2), and

 C_h=(convolution by p_(a/h))^tensor12,
 F(h)=B_h C_h B_h.

Each convolution is a contraction on L2 by averaging unitary translations; inversion invariance makes it selfadjoint. Wilson character positivity also makes it positive. B_h is a positive contraction, so F(h) is a positive selfadjoint contraction. All factors commute with the vertex gauge projection. F(h) is the actual full Wilson transfer at spatial coupling hv and temporal coupling a/h, multiplied by the scalar exp(-6hv)c0(a/h)^(-12). These scalars are stated, not an implicit division by the largest transfer eigenvalue. The potential therefore includes its specified constant term6v; no ground-energy subtraction is performed.

Choose Hermitian traceless generators Ta with Tr(TaTb)=delta_ab. Let D_a be the skew-adjoint generator of f(g)->f(exp(-itTa)g), and let Delta=sum_a D_a², nonpositive. For12 links set Delta_tot=sum_e Delta_e and L=-Delta_tot>=0. On a fundamental matrix coefficient, -Delta=sum_a Ta²=(8/3)I: conjugation invariance makes the sum scalar and its trace is8. Thus the candidate kinetic coefficient kappa=3/(2a) gives fundamental kinetic energy4/a. This checks the factor-two convention relative to generators normalized with trace1/2; no representation normalization is silently swapped.

## 2. Normalized actual Wilson moments

There is a small Ad-invariant, inversion-symmetric exponential ball g=exp(iX), X=sum x_a Ta, on which Haar is j(X)dX with j positive smooth and even. Write Q=TrX²=|x|². The exact one-link Wilson deficit E=1-J satisfies

 E(X)=Q/6+O(|X|4),  E(-X)=E(X),
 j(X)=j0+O(|X|²), j0>0.

The absence of a cubic term is exact for this single exponential real trace; no multiple-source conditional cancellation is used. E has a unique minimum at g=I. On a sufficiently small chart E>=c|X|², and on its compact complement E>=g0>0. Standard finite Taylor remainder estimates here can be obtained directly by differentiating chi(epsilon y)j(epsilon y)exp[-E(epsilon y)/epsilon²] on nested symmetric charts: its first derivative at epsilon0 vanishes, its second derivative is bounded by a fixed polynomial times exp(-c|y|²). This gives O(epsilon²) weighted L1 errors for every fixed polynomial weight. The compact complement is exponentially small after normalization.

With s large and epsilon=s^-1/2, let Z_s=integral exp(-sE)dg. Direct scaling yields

 Z_s=s^-4[j0(6pi)^4+O(s^-1)],
 integral_chart x_a x_b exp(-sE)dg
       =s^-5[3 j0(6pi)^4 delta_ab+O(s^-1)].

Consequently the UNCONDITIONALLY normalized, chart-truncated logarithm moments obey

 integral_chart x_a x_b p_s(g)dg=3 delta_ab/s+O(s^-2),
 integral_chart |X|4 p_s(g)dg=O(s^-2),
 integral_chart x_(a1)...x_(a_(2r+1)) p_s(g)dg=0.

The last identity is exact by inversion and the symmetric chart. Chart truncation is not silently renormalized. The omitted mass is at most C exp(-c s), absorbing the harmless s4 partition prefactor into a smaller exponential. In particular zeroth-order mass outside the chart contributes at most2C exp(-cs)||f||2 when comparing convolution to identity.

For12 independent links, the product chart has total logarithm vector X in R96. Its second moments have the same diagonal leading coefficient3/s, cross-link moments vanish, its fourth norm moment is O(s^-2), and its complement has exponential mass. Constants depend on the fixed12-link graph, not on a Sobolev embedding dimension argument. Putting s=a/h gives covariance3h/a plusO_a(h²).

## 3. L2 Taylor estimate without pointwise regularity

Define the graph Sobolev space H4=D((I+L)^2) with norm ||f||H4=||(I+L)^2 f||2. On a smooth vector let D_X=sum_(e,a) x_(e,a) D_(e,a). It generates a unitary one-parameter translation and commutes with L because the group Laplacians are bi-invariant Casimirs. The energy identity gives

 ||D_X f||2 <= |X| ||L^(1/2)f||2,
 ||D_X^r f||2 <= |X|^r ||L^(r/2)f||2.

The first inequality is Cauchy-Schwarz over the generator family and sum||D_(e,a)f||²=<f,Lf>; iteration uses commutation with L. Thus Taylor's integral remainder in the UNITARY group on L2 gives

 ||exp(D_X)f-sum_(r=0)^3 D_X^r f/r!||2
       <= |X|4 ||L²f||2/24.

Average over the product chart. The linear and cubic terms cancel exactly, the quadratic term is(3h/(2a))Delta_tot f plusO_a(h²)||f||H4, and the remainder is bounded by the fourth moment. Add the exponentially small outside-chart contribution. Extending from smooth vectors by graph-norm density proves

 ||C_h f-f-kappa h Delta_tot f||2 <= C_a h² ||f||H4

for0<h<=h0(a), kappa=3/(2a). This is an H4-to-L2 bound, not operator-norm differentiability on allL2. No pointwise Taylor bound, supremum norm or Sobolev embedding was used.

## 4. Compact potential and selfadjoint interacting Hamiltonian

Multiplication by any fixed smooth function on the compact product group is bounded on H4 (and H2), by iterated invariant-derivative Leibniz rules. Derivative graph norms through order4 are equivalent to the stated elliptic Laplacian graph norm on this finite compact group; one can use the derivative norm throughout instead. The constants depend on finitely many derivatives of V. In particular ||B_h||H4->H4 is uniformly bounded for0<h<=h0, and ||B_h-I||H2->H2<=C h.

Define H=kappa L+V on D(L)=H2. Bounded real multiplication is a bounded selfadjoint perturbation, so H is selfadjoint and H>=0. Its restriction to Hphys is also selfadjoint because the gauge projection commutes with L and V. H4 lies in D(H²), and ||H² f||2<=C||f||H4 follows by expanding kappa²L²+kappa LV+kappa VL+V² and the H2 multiplication bound.

Let S(t)=exp(-tH). It is an L2 contraction. The free heat semigroup exp(-kappa tL) is an H4 contraction by the spectral definition. The bounded-perturbation Dyson series on H4 with multiplication by V therefore gives

 ||S(t)||H4->H4 <= exp(C_V t).

The series agrees with the L2 semigroup by the same Duhamel equation and uniqueness; there is no need to presume H and L commute. This establishes the regularity estimate used later on S(jh)f.

## 5. One-step and n-step bounds

Use the established C_h expansion on B_h f and multiply on the left by the L2 contraction B_h:

 F(h)f = B_h² f +kappa h B_h Delta_tot B_h f +O(h²)||f||H4.

The bounded potential expansion gives B_h²=I-hV+O(h²) on L2. Moreover

 B_h Delta B_h-Delta
   =(B_h-I)Delta+B_h Delta(B_h-I)

has H2-to-L2 norm O(h), by smooth multiplication. Hence

 ||F(h)f-f+hHf||2 <= C h²||f||H4.

For f in H4 subsetD(H²), the spectral integral remainder for S(h) yields

 ||S(h)f-f+hHf||2 <= h²||H²f||2/2.

Consequently ||(F(h)-S(h))f||2<=C h²||f||H4. At fixed0<t<=T, h=t/n, the exact telescoping identity is

 F(h)^n-S(t)=sum_(j=0)^(n-1) F(h)^(n-1-j)(F(h)-S(h))S(jh).

Its left factors are L2 contractions and its right semigroup factors obey the H4 stability bound. For n sufficiently large that h<=h0,

 ||F(t/n)^n f-S(t)f||2 <= C_(a,v,T) n^-1 ||f||H4.

This holds on the full compact link Hilbert space and its physical gauge-invariant subspace. Smooth invariant vectors are dense: average smooth approximations with the gauge projector, which commutes with L. Since both families are contractions, approximation by H4 vectors proves strong convergence on EVERY f in Hphys (indeed every link-L2 vector). No rate depending only on ||f||2, no allL2 operator-norm rate, and no finite-dimensional spectral truncation is asserted.

The powers are genuine full Wilson slab powers up to the declared scalar factors. Internal spatial halfweights glue to exp(-hV), and all intermediate physical degrees of freedom are integrated. There is no source/reset projection. Boundary states need not be supported near the identity: only the small temporal increment distribution is localized. The limiting compact plaquette multiplication V retains its full nonquadratic dependence on all four links of every face.

## 6. Adverse boundaries and provenance

For every fixed h>0 the smooth convolution kernel on the compact group is compact, so C_h cannot tend to identity in operator norm as h->0 on the infinite-dimensional space: ||I-C_h||>=1 by its vanishing high-frequency eigenvalues. This explains why a naive bounded-generator/one-step operator-norm Taylor argument would fail. It does not disprove any possible operator-norm convergence of the n-step family at a fixed positive time; that stronger question is simply not proved here.

The argument is a source-specific quantitative finite-cube realization of the standard Wilson-to-Hamiltonian construction, not discovery of Hamiltonian lattice gauge theory. Primary historical provenance: John Kogut and Leonard Susskind, “Hamiltonian formulation of Wilson's lattice gauge theories,” Phys. Rev. D11,395–408 (1975), https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.395. The paper explicitly presents Wilson's lattice gauge model as a canonical Hamiltonian theory. Its result is credited as provenance; the local normalized moments, exact trace convention, H4 consistency and rate above are derived here rather than imported as an unexplained theorem.

This removes Gaussian boundary-state localization from this NEW supplied scaling, not the action/time supplier. It does not select a, v, physical units, continuum space, thermodynamic limit or a physical Yang–Mills gap. It is not a correction to the prior beta_n=n204 Gaussian-state regime: the spatial coupling is now hv and temporal coupling a/h. Independent cold review is required before any canonical theorem claim.
