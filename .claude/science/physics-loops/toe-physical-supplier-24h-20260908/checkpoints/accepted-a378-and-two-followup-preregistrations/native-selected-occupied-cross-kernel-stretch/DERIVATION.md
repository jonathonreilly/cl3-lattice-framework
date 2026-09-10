# Selected-space cross kernels for an occupied-state consumer

Source-only proposal. No actual selected labels, T, history, node bank or native scalar values were read. The completed/frozen A378 acquisition is untouched. Targets tau<=1e-9 and weighted residual squared<=1e-16 are proposed consumer gates, not established outputs.

## One old pole changes the scalar problem

For the canonical spectral measure define B(s)=E[sqrt(X)/(X+s²)]. The positive divided kernel is

 K_B(s,t)=E[sqrt(X)/((X+s²)(X+t²))]=(B(s)-B(t))/(t²-s²).

Confluence is -B'(t)/(2t). Suppose the old selected-family pole t>=1/128. In the low-new-pole region s<=t/2,

 t²-s²>=3t²/4>=3/65536.

Thus independent B radii eta_s,eta_t contribute at most(65536/3)(eta_s+eta_t). Radii1e-29 give entry radius<4.37e-25 before native coefficients and selected-coordinate amplification. This is fundamentally different from subtracting two arbitrary new poles near2^-32. It does not prove the final objective error is small: norms of selected coefficients and weights still multiply it.

The complementary region s>t/2 has s>=1/256. Its only dangerous denominator is near confluence, not the origin. Exact geometry can choose a direct-difference branch when a certified lower denominator is available, and a confluent/jet branch otherwise. This geometry ledger must precede acquisition; approximate pole distances cannot select a certified branch.

## Joint representation without acquiring tiny B independently

Let c=E[X^-1/2], C(s)=E[1/(sqrt(X)(X+s²))]. Then

 K_B(s,t)=[c-B(t)-s²C(s)]/(t²-s²)
         =[t²C(t)-s²C(s)]/(t²-s²).

In the low region the C(s) radius is multiplied by s²/(t²-s²)<=4s²/(3t²), while c and oldB(t) enter with the displayed fixed old-pole denominator. Therefore a uniform1e-20 C target at every tiny s is not necessary solely for this cross kernel. A rigorous coarse C(s) enclosure from the IR proof, C(s)=(1/(2pi²))log(1/s)+[0,1+7/(24pi²)] for s<=1, can be charged with this suppressing s² factor. It is not automatically adequate at the transition s~t/2. A future protocol can freeze a per-pole C tolerance proportional to its required cross-entry tolerance times(t²-s²)/s², and use the coarse enclosure only when it actually meets that gate.

Store common c/B/C dependencies and form the displayed expression once. Independently widening B(s)=c-s²C(s) and then subtracting another correlated quantity can recreate avoidable dependency loss. If only independent oldc and oldB(t) boxes exist, their sum-radius remains a real certified uncertainty; one cannot declare their errors cancel.

## Exact selected projector and affine recentering

Let S be the SAME exact selected seed family, with positive definite G=S*S. Its projector is P=S G^-1 S*. A different invertible coordinate transform T does not change P: with V=S T,H=T*GT, P=V H^-1 V*. This algebraic identity permits new certified coordinates without repeating old pivot recurrence or claiming that an inaccurate approximate basis is exact.

If G=G_c+Delta, certify an inverse candidate Y by ||I-YG||<=e<1. Then ||G^-1-Y||<=||Y||e/(1-e). A posteriori interval bounds on G, including physical scalar radii, must be included in e. Replacing G by G_c without charging Delta changes the projector and is invalid. A positive-definite midpoint alone does not prove this estimate.

For new columns F define J=S*F and K=F*F. The projection-tail Gram is Q=K-J*G^-1J>=0. Given approximations J_c,Y and norm bounds ||J-J_c||<=d, ||J_c||<=j, ||G^-1-Y||<=v, ||G^-1||<=g, one valid operator error bound is

 ||J*G^-1J-J_c*YJ_c|| <=g(2jd+d²)+v j².

Here ||Delta J||<=sqrt(nm)*epsilon_entry is a safe entrywise-to-operator bound. These coefficients must be supplied from actual certified data later. There is no universal inference from a raw1e-29 B radius to a1e-16 squared-residual objective.

A recentering can reduce artificial interval dependency and inverse conditioning, but cannot erase genuine Delta or change the exact selected P. It is a NEW certificate method, not a retry of the old uniform leakage test. The previously excluded uniform leakage remains excluded for the same span; an occupied-state weighted objective is a different, explicitly specified consumer.

## Avoiding a full new-new Gram: what is and is not enough

Cross J alone computes projection coordinates, but not the full tail of a new finite factor: Q also needs K or a certified upper majorant for K. For a factor Dhat=F L F* the nuclear-tail bounds can use a supplied Gram majorant K_up>=K together with lower bounds on J*G^-1J; however crude column norm bounds may be too weak for tau<=1e-9. Do not claim all new-new data unnecessary merely because cross-data are available.

A potentially cheaper sufficient certificate is a low-rank factorization Dhat=U Z V* with independently bounded left norms and directly certified right projection defects. Then ||Dhat(I-P)||1<=||U Z||HS ||(I-P)V||HS. The second factor still requires the trace of the relevant right Gram, but only that trace and selected projections, not every new-new entry. Signed cancellations lost in this bound can make it insufficient. More refined block or weighted trace majorants are legitimate if their PSD order is certified.

For a positive commuting residual majorant W in selected coordinates, the occupied objective uses ||Dhat Y_W||1 plus projector-approximation error times||Y_W||. It can be bounded through cross matrices and factor norm certificates; the approximation error contribution cannot be omitted. The Primary Fock/positive-projection consumer premises remain separate, including initial state tail and CAR insertions.

## New acquisition scope

A naive cross catalog has at most378*66 scalar pole pairs per spatial type (24948); selecting only actually used old poles can reduce it, but that census cannot be asserted before a future bound-label protocol. All low-region comparisons and near-confluence decisions can be certified from the frozen geometry before any scalar call. Existing B(t),c and A(s) may be reused by exact accepted provenance. Missing B(s)/C(s), derivatives, and spatial numerator coefficients must be acquired only if the literal cross formula needs them. The displayed one-measure K_B identity is not a blanket proof for every seven-star spatial numerator; those must be reduced with the actual signed local dictionary.

The next falsifiable gate is to propagate actual authenticated Gram and cross-entry radii through explicit g,j,d,v and factor norms. If those terms alone exceed the objective allowance, a sharper correlation-aware certificate or new physical precision is needed. No target weakening, old uniform-span reinterpretation, or unmeasured precision claim follows from this source design.
