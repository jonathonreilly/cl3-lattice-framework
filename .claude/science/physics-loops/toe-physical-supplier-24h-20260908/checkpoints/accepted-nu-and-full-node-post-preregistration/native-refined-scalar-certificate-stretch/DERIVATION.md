# Prospective tighter certificates from existing scalar data

SOURCE ONLY, UNREVIEWED. No catalog entries, saved pivot histories, interval scan, integral, or oracle has been evaluated. These are new certificate protocols, not relabelings or reruns of completed protocols. The reviewed rho4 ellipse is reused. Actual accepted scalar intervals are inputs to a future frozen saved-data contraction; nominal precision never replaces their widths.

## Required precision is a conditioning-dependent quantity

The historical fresh-pivot width obstruction concerns the historical recursive interval algorithm. It does not determine a universal scalar precision required for the selected frame. For the new principal certificate let T be a fixed upper triangular candidate, K>=||ET||2, t>=||T||2, and e0>=||T*G0T−I||F. If direct Gram uncertainty is etaG, then e=e0+t² etaG is sufficient. Choose a prescribed d<1 and require

 e<=d,  2K e/(1−d)² + endpoint_rounding_width <= 2^-39.

Thus etaG must not exceed

 [min(d,(2^-39−endpoint_rounding_width)(1−d)²/(2K))−e0]/t².

The right side must be positive. This is a falsifiable sufficient precision requirement, not a claim of necessity or native success. Large T and K can make it much stricter than a scalar's nominal width. Conversely, direct factorization may remove recursive dependency widening without any new oracle.

Suppose each independent selected Gram entry is a linear combination of scalar inputs theta_l with exactly bounded coefficient magnitude a_ij,l, plus separately bounded geometric/rounding error b_ij. With scalar radii eta_l,
 etaG <= sqrt(sum_ij (sum_l a_ij,l eta_l+b_ij)^2).
Use a rational upper bound on this square root or the looser p max_ij radius. This gives an explicit allocation constraint for A,B,cminus,A0 (and any derivative inputs actually used). It requires the actual selected coefficient ledger and T norms; these have NOT been read here. Neither current summaries nor the fresh-r interval alone justify a numerical claim such as '1e-27 will unblock24'.

## Common analytic quadrature improvement

On each [a,2a], rho4 ellipse center3a/2 and axes17a/16,15a/16 lies in Re z>|Im z|. Re z²>0, hence |X+z²|>=X. The Gauss26 analytic radius is (16/3)a M 4^-52. Summing a<8 gives:

 cminus: R_A<=(544/45)4^-52;
 mu: R_mu<=(128/3)4^-52;
 B(s), H(s)=−B'(s): shared R_BH<=128*4^-52,

using A0<=17/60 and the previously reviewed uniform −A'(s)<=3. These are radii before multiplying2/pi. The latter bound is a safe shared envelope, not the optimal individual bound. Even with exact input data this particular analytic estimate contributes a nonzero certified width2R; it is an upper error budget, not a lower bound on the actual quadrature error.

## Direct A-integral and mu contractions using actual widths

Let node t_i have radius d_i, mapped positive weight w_i radius z_i, and accepted A-at-node radius a_i. The latter must include monotone endpoint spread and node displacement exactly once. Work with outward intervals directly; do not regard A and t as independently exact midpoint values.

For cminus integrand A, contribution radius is bounded by w_i^+ a_i + z_i |A_center,i|, with any rounding added. If A interval is assembled at the exact root, no extra derivative inflation is added again. A safe center-free version uses w_i^+ a_i+z_i A_i^+.

For mu integrand1−t²A, a first-order finite-box bound is
 b_i <= (t_i^+)² a_i + [2 t_i^+ A_i^+] d_i,

by the multivariable mean-value theorem (or exact interval multiplication). The weight contribution is w_i^+ b_i+z_i sup|1−t²A|. These formulas retain actual t-dependent amplification rather than imposing64 on every node. Sum these plus fixed arithmetic radii, analytic R and tails; the final pi interval multiplication must be outward. They can be far smaller than uniform worst-case bounds, but that has not been measured.

For cminus low tail epsilon=2^-64, with A0 interval and |A'|<=L, use [epsilon A0_lower−L epsilon²/2,epsilon A0_upper], intersect nonnegative. Its width is epsilon width(A0)+L epsilon²/2. For mu low tail use [epsilon−A0_upper epsilon³/3,epsilon]; stronger cusp information is optional and must be separately pinned.

At t>=8, N even terms give:
 A(t)=sum_(n=0)^(N−1) (−1)^n M_n/t^(2n+2) + positive remainder,
 mu integrand=sum_(n=0)^(N−1) (−1)^n M_(n+1)/t^(2n+2) + positive remainder.

Integrated remainder bounds are respectively M_N/[(2N+1)8^(2N+1)] and M_(N+1)/[(2N+1)8^(2N+1)]. Bound M_j<=12^j if exact moments are not yet formed. N40 already makes these tiny relative to the reviewed uniform input budgets; the new protocol must select N and its exact target before contraction. All moments are finite combinatorial local identities, not new oracle calls.

The existing A catalog itself cannot be tightened by this change of quadrature ellipse: its individual A(s) certificates came from their own oracle. A new cminus/mu integral certificate can use those unchanged A intervals more efficiently. Interval intersections with independently proved Jensen/IR bounds may tighten a particular A interval only if both containments are explicitly proved and applied; no such intersection or achieved improvement occurs here.

## B divided-difference conditioning must be explicit

For exact positive s,t write a=s²,b=t²,d=b−a, As=A(s),At=A(t). The positive integrand is

 G_s(t)=E X/[(X+a)(X+b)]=(b At−a As)/d.

For d!=0, with s,t held exact, scalar-input radii give

 err(G)<= (b etaAt+a etaAs)/|d|.

For H_s(t)=−partial_s G_s(t),
 H=2s[((As+s A'(s)/2)d)−(b At−a As)]/d²,

so a safe independent-box input radius is

 err(H)<=2s[(etaAs+s etaAprime/2)/|d| +(b etaAt+a etaAs)/d²].

These are conservative bounds; shared As should preferably be collected algebraically before interval evaluation. They nevertheless make the denominator problem explicit. If s,t are intervals, use a certified d_min>0 and the full outward rational expression, including numerator coefficient and denominator uncertainties. Plugging midpoint d into these formulas is invalid. All1742 nodes at every requested pole must have a frozen separation ledger, or be assigned a rigorously confluent branch before execution.

At exact coincidence,
 G_s(s)=A(s)+s A'(s)/2,
 H_s(s)=−[3A'(s)+s A''(s)]/4.

A near-coincident branch needs Taylor remainder bounds over the entire interval, including A'' and, for H accuracy, sufficiently high derivatives. An A' value alone does not validate replacing a small nonzero denominator with the coincident formula. One alternative is the positive expectation representation with a separately certified derivative oracle; that is a new supplier, not already available from endpoint A data by assertion.

Consequently the rho4 analytic improvement does not imply B66 can reach the same1e-27 scale as mu. Given requested etaB, the weighted sum of these actual denominator-dependent input errors must fit etaB−analytic−tails−rounding. If it cannot, the honest options are a new sharper A/A' supplier, derivative-based near-coincident certificates, or a correlation-aware analytic representation. Merely rerounding existing intervals to more bits cannot help.

## B and H tails, uniform versus pole-specific

For high t, define J_j(s)=E[X^j/(X+s²)], with J0=As and J_j=M_(j−1)−s² J_(j−1). Then G has N even terms J1..JN divided by t²..t^(2N), and positive integrated remainder <=J_(N+1)/[(2N+1)8^(2N+1)]<=M_N/[(2N+1)8^(2N+1)]. Direct recurrence may suffer cancellation at large s; outward arithmetic and an actual width gate remain mandatory.

For H, coefficients are2s E[X^j/(X+s²)²], j1..N. The positive remainder is bounded by2s E[X^(N+1)/(X+s²)²]/[(2N+1)8^(2N+1)]. A uniform safe bound follows2s/(X+s²)<=1/sqrtX, giving numerator<=E X^(N−1/2); the coarse spectral bound12^(N−1/2) is valid for N>=1. A rational larger bound12^N suffices. This derivation avoids a spurious1/s blowup in the high-tail estimate.

For low t, G_s(0)=As and H_s(0)=−A'(s). Positivity gives integrals in[0,epsilon As] and[0,epsilon(−A')]. These coarse widths may dominate a1e-27 target. A sharper fixed-s bound follows
 0<=G_s(0)−G_s(t)<=t² A0/s²,
 0<=H_s(0)−H_s(t)<=2t² A0/s³.
Integrating gives epsilon³ A0/(3s²),2epsilon³ A0/(3s³), plus endpoint As/A' widths times epsilon. These are useful only when the actual pole lower bound makes them small. At very small s, use a separately proved uniform IR low-tail formula or change the fixed integration splitting under a new protocol. No claim of an adequate uniform low-tail error for all66 poles is made here.

## New-protocol cost and stopping gates

A saved-only direct cminus/mu contraction needs1742 node contributions each,40 or another fixed number of exact moments, and67 retained panel records. B/H66 needs66×1742 divided-difference contributions, with denominator and branch ledgers frozen first; this is not priced by the cheap single scalar contraction. Read/hash/transitive provenance and independent saved reconciliation are part of each new budget. No numerical timing or execution contract is selected here.

Before launch: certify the target Gram allocation above; bind actual unchanged A/A' and weight intervals; calculate only the prospective analytic/conditioning ledger under a separately authorized saved-scalar diagnostic if needed; freeze all tails/branches/counts; then launch a genuinely new certificate once. Failure or insufficient precision preserves the full ledger. No claim that this route unblocks24 is justified until these conditions are met.
