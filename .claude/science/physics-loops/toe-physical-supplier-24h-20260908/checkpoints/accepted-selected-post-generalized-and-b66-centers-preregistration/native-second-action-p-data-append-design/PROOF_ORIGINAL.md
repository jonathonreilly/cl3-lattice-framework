# Enlarging the trial domain by q: three more sources and one extra covariance moment

UNREVIEWED source-only derivation. No native arrays, entries, scalar integral or runtime were evaluated. The current ORIGINAL798-domain theorem and frozen jobs remain unchanged. Assume the supplied infinite native reference, H0=iK, Gamma=i sign(H0), Gamma K=|H0|, and h=1. All vectors are real CAR one-particle columns; J(a,b)=<a,Gamma b>. Opposite parity/sublattice zeros and the seven-star scalar identities are imported from the reviewed common Gram/generator derivation.

## 1. New trial and DATA domains

Original F contains399 raw columns (balanced poles and three Ward insertions). Existing DATA adds qA=dA/2,qC=dC/2,qD=d_all/2, giving402 raw/804 closed. Suppose these q columns are NOW admitted to the trial family F1. This is a new premise/domain, not a reinterpretation of the current certificate. Define p_u=Kq_u, u=A,C,D. Each p is a local white-sublattice vector at graph distance at most2 from the center (including center); Gamma p is not assumed local.

Append pA,pC,pD and their Gamma partners to DATA:405 raw/810 closed columns suffice for the FIRST action on F1, equivalently the next action layer relative to old F. No action on p is asserted. K commutes with Gamma, so the free action of Gamma q is Gamma p. For each impurity

 DeltaK_A=8(x0 qA^T-qA x0^T),
 K_A q_u=p_u+8[x0<qA,q_u>-qA<x0,q_u>].

Here <x0,q_u>=0 and the q self Gram is known. On Gamma q the correction must instead use its actual Gram overlaps; it must NOT be obtained by commuting DeltaK with Gamma. Existing804 Gram already provides those overlaps. Thus the action map on F1 is explicit after adding the p columns, with the same rank-two formula on all columns.

The three p columns are linearly independent: if K(sum a_u q_u)=0, its Fourier transform vanishes off the measure-zero zeros of the canonical dispersion, hence the finite-support vector is zero. The q vectors are independent by disjoint support plus the remaining two neighbors, so a=0. This proves their span dimension3, not independence modulo the old nonlocal trial family.

## 2. All p-to-old-pole entries reduce to existing data

For old z_sigma(v)=sqrt(alpha)y_sigma(v), Ky=sigma*s*y-v and K is skew. Therefore

 G(p_u,z)=−sigma*s G(q_u,z)+sqrt(alpha)<q_u,v>,
 J(p_u,z)=−sigma*s J(q_u,z)+sqrt(alpha)J(q_u,v).

The second formula uses K Gamma=Gamma K and skewness; its sign is the same minus sigma*s. Existing q-to-pole entries already depend only on A,B,mu. Local overlaps are

 <q_u,v>=u^T I v/2,
 J(q_u,v)=−mu u^T T v/12,

with v=e0,dA,dC and q_u=u/2. For v=e0 the first vanishes and u^T T e0 is2,2,6. For neighbor v the J term vanishes. Pole balancing sqrt(alpha) must be retained explicitly.

## 3. p-to-Ward and p-to-q entries

Write original x=(x0,xA,xC) and f=(qD,qA,qC), so Kx_j=f_j. Then

 G(p_u,x_j)=−G(q_u,f_j),
 J(p_u,x_j)=−J(q_u,f_j)=0.

These are exact local rational numbers. In particular G(pA,x0)=G(pC,x0)=−1/2 and G(pD,x0)=−3/2. The sign agrees with p_u's center coefficient−|u-support|/2 and x0=e0/2.

G(p_u,q_v)=0 by opposite sublattices. For J,

 J(p_u,q_v)=−<q_u,Gamma K q_v>=−<q_u,|H0|q_v>.

The local neighbor block of a scalar f(X), X=H0² in folded dispersion variables, is E[f(X)]N−E[X f(X)]O/6, with N=I+O. This follows from cubic symmetry and X=6−2 sum cos(theta), exactly the same local reduction used by A and B; same-direction entries are E f and opposite entries are E f−E(Xf)/6. Taking f=sqrt(X) gives

 J(p_u,q_v)=−mu u^T N v/4+nu u^T O v/24,
 nu=E[X^(3/2)].

For d_all, N d_all=0 and O d_all=−d_all. Consequently

 J(pD,qD)=−nu/4.

This isolates the additional covariance moment directly. The current scalar closure identities do not eliminate nu in favor of A/B/a0/c/mu and integer local moments. This is a precise missing-data obligation, not a theorem that no further identity for this particular dispersion could relate them. A sharp810 Gram needs a nu certificate or another proved enclosure of this same overlap.

## 4. p self Gram requires only exact local moments

G(p_u,p_v)=<q_u,H0²q_v>. The neighbor restriction is M1 N−M2 O/6 with M1=E X=6, M2=E X²=42. Thus

 G(p_u,p_v)=u^T(6I−O)v/4,  J(p_u,p_v)=0.

M2=36+4*(3/2)=42 follows directly from independent uniform torus cosines. pA or pC squared norm is3 for perpendicular pair and7/2 for opposite pair; pD squared norm21/2. The extra CLOSED trace is33,34 or35 according to the two pair types. Thus prior trace<536 becomes<571. This is a norm/count bound, not a complete physical-radius ledger.

All reversed blocks use symmetric G/skew J, and all Gamma copies follow[[G,J],[-J,G]]. p is white like old insertions, whereas q is black. Structural zero tests must reflect that change. No new distance-dependent scalar beyond nu is needed for these first-layer blocks; p-to-p needs no mu or nu.

## 5. A coarse no-new-oracle enclosure and a possible sharp future certificate

Since X≥0, Cauchy–Schwarz gives M1²≤mu*nu and nu²≤M1*M2. Hence

 36/mu ≤nu≤sqrt(252).

A certified positive interval for mu supplies lower36/mu_upper; rational outward sqrt supplies the upper. These inequalities provide immediate coarse containment for new J blocks without any new physical integral. They do NOT imply useful action accuracy; the resulting width is macroscopic relative to tight leakage goals.

For a sharper future integral,

 nu=(2/pi) int_0^infinity E[X²/(X+t²)] dt
    =(2/pi) int_0^infinity (6−t²+t^4 A(t)) dt.

This is a NEW physical integral, even if it reuses the accepted A endpoint catalog. It requires a separately proved quadrature/rounding/cancellation ledger and frozen protocol before evaluation. At large t, N alternating terms use M2 through M_(N+1); after N=26 the positive remainder is bounded by M28/(53*8^53) for the existing cutoff8. This follows from the exact geometric remainder X28/[t52(X+t²)] integrated over t≥8, not an assumed next fitted coefficient. On the same right-half-plane ellipse, |E X²/(X+z²)|≤sec(arg z) E[X²/(X+|z|²)]≤6 sec(arg z), and high-pole bounds use42/(|z|Re z). Whether the old catalog precision and panel order meet any desired nu width remains to be proved; no target or cost is asserted here.

## 6. Cost and scope

For each orbit, p-to-old402 has3*402 entries and upper p self adds6, hence1212 new raw G/J pairs (6060 overfive), before symmetry/zero savings. A prospective stream would have3*(132 pole-sign rows+one Ward row+one q row)+3 self rows=405 rows per orbit,2025 total. No old entries need reevaluation. This is close in entry count to the prior3q append but formulas/cancellation differ, so it is not a timing forecast.

The new action-domain coefficient map on405/810 DATA permits the same exact-isometry leakage algebra for a trial spanning402/804, conditional on all new scalar/Gram/coordinate certificates. Merely appending q to the trial does not guarantee small leakage: its K images p may still have large residual. Repeated further action would introduce another local layer and potentially additional fractional moments. This is a concrete fallback construction and a sharp scalar obligation, not an alteration of the current24-pair original-domain run.

For physical scale h, use dimensionless p=(K/h)q in the frame and restore h multiplying each generator action. mu and nu above are dimensionless E sqrt(X),E X^(3/2); avoid mixing these with dimensional h mu or h³ nu inside dimensionless Gram formulas.
