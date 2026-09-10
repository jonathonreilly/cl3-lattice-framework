# Precision contract from accepted T norms, without rereading T

Unexecuted saved-scalar certificate proposal. Inputs are the five accepted NORM_i.json records of the new T sensitivity study, its ROOT acceptance/result, and accepted A-only operator approximation. No actual T, native entry or matrix history is needed. The protocol must verify each supplied operator-norm-squared bound u is positive and <=10^8. This last threshold is a prospective exact gate, motivated by the reported maximum below7.32e7, not a substitute for reading/authenticating the record during the future certificate.

Import the independently reviewed companion9932 and accepted operator error<1e-12, hence M=88 bounds ||Dhat||1 from ||D||1<87. Put a=1-8e-6,b=1+8e-6. These constants concern the same selected span; no physical objective is declared small.

## Metric and inverse precision

For a new raw selected Gram enclosure radius rho, delta<=48u rho. With a new inverse candidate residual r0 and delta<=a/2,
 v=||Y-H^-1||<=2r0/a+96u rho/a².

For a nuclear-tail numerical uncertainty allowance z_tau=1e-10, suffice
 v<=z_tau/(88b), r0<=a v/4, rho<=a²v/(192u).

For a residual numerical uncertainty allowance z_r=5e-17 and a fixed exact majorant ||W||<=w>0, suffice
 v<=min(1/a,z_r*a/(264 b w)), with the same r0/rho allocations.

These formulas use actual accepted u records. A concrete conservative optional design with w<=4 and u<=1e8 is rho<=1e-39 and r0<=1e-22. Direct substitution proves both allowances, with substantial margin. w<=4 is a separately required majorant gate, not something computed by this certificate. If w=0 the residual contribution is exactly zero and no division by w is taken. If w>4 use the exact formula, not this advertised fixed threshold.

The existing H uncertainty is not this new rho. Reusing its old enclosure does not meet a new tighter target by assertion. A source-certified recentering/refined physical raw Gram and verified inverse residual must actually be supplied. Higher arithmetic precision alone does not reduce physical scalar uncertainty.

## Cross-entry precision and Holder sensitivity

Let the concatenated cross-coordinate factors D have sum||D_j||F²<159 and coefficient block norms<=3. Suppose each untransformed selected cross entry has radius eta_entry and the concatenated number of right columns is m<=1572. Then after T,
 d=||DeltaD||F<=sqrt(u*48*m) eta_entry <3*10^6 eta_entry

using u<=1e8. With d<=1, the projected trace primitive changes by at most(3/a)(2sqrt(159)d+d²)<81d when using the exact inverse H^-1, with its norm<=1/a, hence less than243000000 eta_entry. This is a sufficient norm estimate; it does not use actual cross norms or assume cancellation.

If a final Holder tail bound uses sqrt of that primitive with prefactor at mostK, its output error is at most K sqrt(243000000 eta_entry). Thus allocate
 eta_entry <= z²/(243000000 K²).

For z=1e-10,K<=1, eta_entry<=1e-29 is sufficient. If K is larger, divide by K²; do not quietly use K=1. For a linear trace consumer the much less stringent eta_entry<=z/243000000 suffices. Distinguish these two interfaces.

If an independently proved literal signed-kernel map has total radius amplification Gamma, require scalar radius eta_scalar<=eta_entry/Gamma. For example Gamma<=2^24 and K<=1 make eta_scalar<=1e-37 sufficient for the displayed Holder allocation. This is a conditional supplier target, not a claim that2^24 has already been proved for all newly requested spatial cross kernels. The exact formula is the contract until that dictionary bound is pinned. It explains a possible1e-35-to1e-37 need without demanding1e-80 universally.

For old-pole t>=1/128 and new s<=t/2, K_B radius<=65536(eta_Bs+eta_Bt)/3. With joint B(s)=c-s²C(s), C's contribution is suppressed by s²; freeze per-node tolerances from the literal weighted formula. Existing independent B radius1e-29, after this amplification alone, is not automatically enough for an eta_entry1e-29 Holder gate. A correlated new certificate or a less pessimistic consumer representation may be needed. The accepted A-only operator construction is unaffected: it does not require this cross Gram.

## New saved-record calculation and scope

The companion script reads only authenticated NORM_i.json after parent preregistration, persists exact u and derived rational thresholds orbit by orbit, and never opens CANDIDATE.json. Its result is a sufficient measurement-precision contract conditional on majorant and kernel-map gates. It does not certify actual tau or residual smallness, create a refined Gram, evaluate C/KB, or alter completed leakage exclusions. Root/output authentication and a bounded20s384MiB runtime are still required before execution. The supplied source is not launched.
