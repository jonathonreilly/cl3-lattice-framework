# Fixed quadratic p and new linear q: complete reflected-source closure

Source-only conditional theorem in dimensionless h=1 units. No accepted scalar, moment, trial, geometry or matrix was parsed or evaluated. The native CAR/free symbol and Gaussian determinant-germ imports are pinned. This proposes a new trial/certificate, not a result of the completed quartic estimator. The source counts below do not authorize a runtime.

## 1. Two different reflections, same vacuum subtraction

Let a be the unit center vector, d=d_A a signed neighbor pair with ||d||²=2 and a*d=0. Write g=gamma(a), J=2i gamma(d), B=i gamma(a)gamma(d), D=H0+B, h=iK and H0=Hfree-E0. For any real nonzero v the Majorana reflection is O_v=2vv^T/||v||²-I; quadratic conjugation equivalently uses R_v=-O_v. Therefore

`gamma(v)/||v|| H0 gamma(v)/||v|| = H0 + (i/||v||²) gamma(v)gamma(Kv)`.

The subtraction E0 is unchanged. In particular

`D_d = (gamma(d)/sqrt2) D (gamma(d)/sqrt2) = H0-B+(i/2)gamma(d)gamma(Kd)`,
`D_a = g D g = H0-B+i gamma(a)gamma(Ka)`.

Both are unitarily conjugate to D and inherit D>=delta. There is no extra guessed mean-energy scalar. The exact insertion identity is J*D^kJ=8D_d^k. The center identity needed for the nominal is

`g q(D) J = q(D_a) gJ = q(D_a) 2B`.

Thus a linear q introduces a center-reflected generator in the nominal, whereas the source residual uses the neighbor-reflected generator. Interchanging these two reflections is incorrect.

The one-particle defects relative to h are

`V_d=-V-d(hd)*-(hd)d*`,
`V_a=-V-2a(ha)*-2(ha)a*`.

For nominal source order F=(a,d_A,d_C,ha), V_A has coefficient entries J_A(0,1)=2i and its Hermitian conjugate. V_C uses(0,2). V_a has(0,1)=-2i,(1,0)=2i,(0,3)=(3,0)=-2. These are exact coefficient matrices, not a claim that the four source vectors are independent. No Gram inverse is required.

## 2. Exactly which source moments are new

Fix the SAME already accepted p(x)=p0+p1x+p2x² and put b=Jp(D)Omega. For q(x)=q0+q1x,

`eta²=||(I-Dq(D))b||² = s0-2q0s1+(q0²-2q1)s2+2q0q1s3+q1²s4`,

where s_k=<b,D^k b>. The new trial norm is

`||q(D)b||²=q0²s0+2q0q1s1+q1²s2`.

Accepted s0,s1,s2 depend on p but not on the old constant q; they can be reused under their exact source identity. Only s3,s4 are missing. They follow from

`Z_d(t,s,z)=<Omega,exp(-tD)exp(-zD_d)exp(-sD)Omega>`.

The mask i,j<=2,k<=4 has45 coefficients and total degree8. With coefficient notation [t^i s^j z^k],

`s_k = 8 sum_(i,j=0..2) p_i p_j (-1)^(i+j+k) i!j!k! [t^i s^j z^k] Z_d`.

The underlying jet is independent of p, so each P/O jet can serve both old p modes. The two classes require90 raw jet coefficients. Reconstructing ONLY s3,s4 for both classes and modes requires72 weighted coefficient terms; it does not replay s0..2.

## 3. New nominal, not reuse of the old numerical nominal

For an ordered disjoint pair C,A, the updated nominal contains

`<p_C Omega,p_A Omega> + <p_C Omega, g q_A(D_A) J_A p_A Omega>`.

A single four-variable series supplies it:

`Z_CA(t,s,z,w)=<Omega,exp(-tD_C)exp(-zD_(a,A))exp(2wB_A)exp(-sD_A)Omega>`.

Its relative one-particle product is

`exp((t+s+z)h) exp(-t(h+V_C)) exp(-z(h+V_(a,A))) exp(2wV_A) exp(-s(h+V_A))`.

The mask(t,s,z,w)<=(2,2,1,1) has36 coefficients, total degree6. The base coefficient(z=w=0) has derivative sign(-1)^(i+j). For insertion coefficients w=1,z=k, k=0,1, the sign is(-1)^(i+j+k); the exponential marker already contains2B_A, so there is no additional factor2. Multiplying by p_C,i p_A,j q_A,k i!j!k! gives the inserted term. The old q0-only nominal cannot simply be retained after changing q.

The five signed disjoint-pair signatures are(P,P,o=1):48,(P,P,o=2):12,(P,O,o=0):12,(O,P,o=0):12,(O,O,o=0):6. Their total is90 ordered words. Source tables and defect coefficients agree within each signature, so five complete nominal jets (180 coefficients) suffice for both old modes. With9 base,9 constant-insertion and9 linear-insertion terms per signature/mode,270 weighted terms assemble the two new nominals. Every signature's actual left/right ordering is retained.

## 4. Analytic cancellation and exact radial tables

For each product, the relative free-only coefficients cancel. A trace containing exactly one bounded defect can be moved cyclically past free powers because[P,h]=0, so its contribution is only linear in the time/marker parameters. Every higher-degree one-defect trace must be removed analytically BEFORE acquiring interval table entries. Products of two or more relative coefficients retain their linear sectors. At total order N, every surviving trace has at least two defects and at most N-2 ordinary free powers between them.

For the nominal use the reviewed three-source base(a,d_A,d_C) and source map(0,1,2,0) with endpoint shifts(0,0,0,1). Every ordinary/projected entry of the four-source table is the base entry at power j+shift_i+shift_j. Here j<=4. The signed neighbor radial entry is

`T_AC(j)=shared*R_j+opposite*(R_(j+2)/6-R_j)`.

Ordinary even tables are diagonal in center versus neighbors; ordinary odd center-neighbor entries are-iR_(j+1)/3. Negative-band projected even center-neighbor entries are+iR_(j+1)/6; projected odd diagonal/neighbor entries are minus the odd radial block/2. These signs are imported literally, not inferred from unsigned adjacency.

The nominal's precise parity budget is smaller than an undifferentiated endpoint bound:

* center-center, possibly two ha endpoints: effective power<=6; even radial orders<=6, odd diagonal projected orders<=5;
* center-neighbor, at most one ha endpoint: effective power<=5; its even projected cross uses R<=5 and odd cross uses even R<=6;
* neighbor-neighbor, no shifted endpoint: effective power<=4; projected odd neighbor entries use at most R5 and ordinary/projected even entries at most R6.

Consequently this p2/q1 nominal needs ONLY c,nu,omega5 and exact even R0,R2,R4,R6. No omega7 is required for the nominal. All table entries are radial, so no anisotropic scalar is introduced.

For the inner jet the source order(a,d,hd) has base map(0,1,1), shifts(0,0,1), and j<=6. Its worst neighbor-neighbor projected odd entry reaches fundamental power7 and radial order9; even neighbor entries reach fundamental8 and radial10. Thus omega9 and exact even R10 suffice, together with the already available lower odd moments. The combined p2/q1 route introduces no scalar beyond the accepted omega7/omega9 family. This is a closure claim; it does not assert useful enclosure widths.

The existing quartic first-residual estimate for this unchanged p requires m0..10 and may be reused under exact identity; the older quadratic-majorant estimate needs only m0..8. A different-p bound is never eligible. No additional first-moment supplier is required if the accepted m7..10 certificate is adequate.

The determinant bridge extends here by the same finite number of bounded-defect exponential factors: finite compressions give the CAR determinant germ, each relative factor converges in trace norm, their finite products converge, and analytic convergence near zero identifies each finite mixed derivative. The square-root branch remains1 at zero. This argument introduces no global inverse of the gapless free h, and the finite sources ha/hd converge in norm because h is bounded.

## 5. What q1 can and cannot improve

For a fixed p, the true least-squares inner residual over linear q contains the old constant-q subspace. Its exact infimum cannot be larger. A prospective candidate solves the2x2 normal system with entries(s2,s3;s3,s4) and right side(s1,s2), using fixed bounded dyadic coefficients selected from interval midpoints, then reevaluates the full signed quadratic form. A failed positive pivot or cap must fall back to the old constant candidate. No interval optimization or improvement is automatic.

The new error still satisfies channelwise

`v_A <= sqrt8*u_A/delta + eta_A/delta`.

The first term is untouched by q. Linear q helps only if the old inner residual is an important limitation; it cannot cure a dominant first inverse error. No actual relative sizes were inspected here. Recompute the new q-trial norms and NEW nominal before applying the posterior Ward bound. One may intersect independently valid intervals for the same physical alpha, but cannot splice an old nominal/trial norm into a new-q error certificate.

## 6. Source-only operation and memory bounds

counts.py enumerates only exact formal words and integer mask combinatorics. It performs no Gram lookup. The nominal has348 collected words and a conservative3,098,544 complex-product bound per jet; the inner has2,073 words and6,002,829 products. Five nominal plus two inner jets are bounded by27,498,378 complex products (at most439,974,048 real endpoint multiplications under the existing16-product primitive), before small polynomial assembly and proposal overhead. These intentionally dense source-bank bounds are not elapsed-time forecasts.

The bounds use E_r(d)=r²(d+1)(d+2)/2 for sparse endpoint matrices and the masked log convolution, plus2r^4(N-1)+r² products per formal word for factorization. A matrix-family bound is3,984 nominal or4,725 inner complex boxes. Sequentially processing jets, three families plus temporary matrices have fewer than15,000 boxes; four4,096-bit endpoints per box have under31MB packed payload. Python objects, retained output and formal words add overhead. Future arithmetic may use the reviewed256-grid primitive and its checked4,096-bit stored/8,193-bit multiplication transient bounds, but no such runtime is implemented or priced here.

Missing scientific evaluations are exactly the two reflected inner jets and five four-source nominal jets (with their output enclosures), followed by four bounded q proposals and new signed certificate arithmetic. Reusing old s0..2, p and first bounds requires authenticated identities. The existing three-source multivariate core does NOT yet implement the four-source/mask changes, so this source proof is not a ready native dispatcher.

## 7. Independent small controls

Twenty exact rational four-Majorana controls verify both reflection signs/same E0, J*D^kJ normalization k0..4, the four-source one-particle center defect, the expanded linear-q residual and trial norm, all nine ordered nominal operator identities, and the90-word signature census. They are finite synthetic operator checks, not native expectation values. Separate formal mask controls cancel free words and produce the count ledger. No native run, saved numerical replay or Git edit occurred.
