# Concrete occupation-weighted consumer target ledger

Source-only sufficient thresholds, no claim they hold for any current frame. Let Q be the positive mode-weight operator in the actual impurity positive excitation space, M=Tr Q<87/2. P is the ORIGINAL trial projection. Let tau=Tr[(I-P)Q] and let positive Y be the physical commuting residual majorant, so r²=Tr(QY) bounds both time signs uniformly throughout the Poisson integration range. An instantaneous residual is insufficient.

For mode weights w_i and errors e_i, weighted Cauchy gives sum w_i e_i<=sqrt(M)*sqrt(sum w_i e_i²). Thus the initial one-body projection defect contributes sqrt(M*tau), not tau and not merely sqrt(tau). Applying the Hilbert–Schmidt Poisson bound to columns sqrt(w_i)P e_i gives, for0<t<=100/h,

 E_F(t)<=sqrt(M*tau)+sqrt(M)*(t*r/pi)*log(1+(S/t)²)+(4M/pi)*atan(t/S).

The final tail multiplier is M, not sqrt(M), because the weighted input Hilbert–Schmidt norm is at most sqrt(M). Left projection into the exact impurity positive space is required for a legitimate Fock map and cannot enlarge this error. This is the unnormalized exterior-algebra map error on the unit reference vacuum; it does not assert a normalized state, inserted Ward-word error, or mixed-kernel accuracy.

## One conservative explicit sufficient allocation

Choose S=10^8/h, tau<=10^-9, and r²<=10^-16 h². The maximum of t log(1+(S/t)²) on0<t<=100/h occurs at100/h: its derivative is log(1+x²)-2x²/(1+x²)>0 for x>=10^6. Moreover log(1+10^12)<28. Using pi>3, sqrt(M)<7, atan(x)<=x gives

 initial contribution <21/100000,
 residual contribution <(2800/3)*7*10^-8,
 Poisson tail <4*(87/2)*100/(3*10^8).

Their sum is exactly1/3000. Therefore these two physical objectives ensure Fock propagation component error<1/3000 uniformly up to100/h. At t0 the exact propagation difference vanishes, while this projection-based sufficient bound remains conservative.

For total unnormalized accuracy1/1000, separately require all initial finite-state truncation, positive-projector implementation, scalar-shift, arithmetic and other declared approximation contributions to sum at most2/3000. An exact stationary shift Delta>=h/4 multiplies the propagation bound by at most1. A separately approximated shift requires its own t|Delta-Delta_hat|exp[-t min(Delta,Delta_hat)] bound; Delta is not reference c=mu/3. These thresholds do not automatically certify multiple stages or CAR insertions, whose norm products and input-state changes must be charged separately.

## Consequences for the streaming projector supplier

For ||Dhat-(P_A^+-P0^+)||1<=eta, the reviewed polar interface gives

 tau<=eta+||Dhat(I-P)||1,
 r²<=||Dhat Y||1+eta||Y||.

The streaming block trace formulas supply conservative upper bounds on the two nuclear norms. They must include physical interval, selected-inverse and arithmetic errors. A convenient split is eta<=5*10^-10 and tail-nuclear upper<=5*10^-10; and eta||Y||<=5*10^-17 h² and majorant-nuclear upper<=5*10^-17 h².

Consequently eta=10^-12 alone does not establish consumer accuracy. For the displayed residual allocation it additionally needs ||Y||/h²<=5*10^-5, as well as a sufficiently small computed nuclear term. If only ||Y||<=36h² is supplied, the corresponding eta allowance is at most(5/36)*10^-17, about1.39*10^-18. The example36 is a conditional norm bound, not a fact about any implemented majorant. A large commuting majorant can demand even smaller eta. Conversely a much smaller certified objective may permit improved thresholds by optimizing S; the chosen ledger is sufficient, not necessary.

No conclusion follows about current24 spans from their uniform leakage exclusion alone. The selected Gram, actual projector blocks, streaming trace values and a time-invariant Y have not been evaluated here. This ledger identifies the concrete gates a new consumer implementation must meet.
