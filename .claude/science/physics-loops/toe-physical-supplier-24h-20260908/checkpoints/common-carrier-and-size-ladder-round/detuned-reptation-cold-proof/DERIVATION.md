# Independent lifted-reptation proof and exact controls

The proposed acceptance ratio and reject-only direction flip are correct. The lifted chain has the stated stationary path law. A blanket ergodicity assertion needs qualifications: one-bond paths and constant row sums have two invariant direction classes. None of these finite statements establishes a long-path mixing rate or removes finite-projector bias.

## Target and proposal

Let G be a finite symmetric nonnegative matrix with positive row sums b(x). A path has n>=1 bonds, x=(x0,...,xn), and positive weight w(x)=product_{r=0}^{n−1}G(xr,x(r+1)). Its normalizer is Z_n=1^T G^n 1. Paths are ordered sequences, including repeated configurations; there is no quotient by reversal, cyclic rotation, or repeated vertices. Lift with direction d in {+,-}; the target is pi(x,d)=w(x)/(2Z_n).

For direction + propose y with probability G(xn,y)/b(xn), making x'=(x1,...,xn,y). The corresponding reverse proposal is in direction − at x': it prepends old x0 with probability G(x1,x0)/b(x1). Therefore

 [w(x') q_−(x',x)]/[w(x) q_+(x,x')]=b(xn)/b(x1).

Use a_+(x)=min(1,b(xn)/b(x1)). It is independent of the proposed y. Direction − analogously uses a_−(x)=min(1,b(x0)/b(x(n−1))). On acceptance retain d and shift the path; on Metropolis rejection keep the entire old path and replace d by −d. A sampled G self-transition is a legitimate proposal, not automatically a rejection. Usually it still shifts a nonconstant path. Even when the entire path is constant, its accepted probability remains a same-direction self-transition.

## Stationarity including repeated paths

Write Q_d(x,x') for the accepted proposal kernel, allowing accepted self-transitions. Ordinary Metropolis algebra with the reverse direction yields the skew relation

 w(x) Q_d(x,x') = w(x') Q_(−d)(x',x).

The rejection probability is r_d(x)=1−sum_x' Q_d(x,x'). Incoming accepted mass at (x,d) is pi(x,d)[1−r_(−d)(x)]. Incoming rejection mass from (x,−d) is pi(x,−d) r_(−d)(x). Their sum is exactly pi(x,d). This proof includes self-transitions and imposes no symmetry of the row sums. No population branching/resampling or path-weight reweighting is needed once this target is sampled.

The G entries must be the actual aggregated configuration-transition weights. If several geometric faces lead to the same next configuration, each contributes to G. Sampling a face first is allowed only if its resulting marginal is exactly G(x,y)/b(x). No extra boundary multiplicity belongs in the path law. Uniform boundary trial vectors are load-bearing; nonconstant endpoint trial factors require changed proposal/acceptance bookkeeping.

## Ergodicity boundaries

For n=1, a_+=a_−=1 identically, even if b is nonconstant. Direction never flips. If b is constant, the same is true for all n. Thus the full lifted chain is reducible in these cases; pi/2 remains invariant. With connected G and positive diagonal, each individual direction still has the correct unique base-path stationary law in these special cases: n=1 reduces to a moving edge of the reversible chain G/b, while constant b reduces to a moving fixed-length window of that chain. Initializing only one direction does not make its base-path law wrong, but it does not sample a balanced direction variable.

A useful sufficient condition for full lifted irreducibility is: n>=2, the undirected support of G is connected, every G(x,x)>0, and b is nonconstant. At a fixed direction all allowable append/prepend steps have strictly positive accepted probability. By appending a connecting walk and then any desired path, the base-path support is strongly connected while retaining that direction. There is an adjacent high-b and low-b pair. A path with x1 at the high-b state and xn at the low-b state, padded by self-loops as needed, has positive + rejection; reversal supplies positive − rejection. Both directions therefore communicate. A constant path has a positive accepted self-transition, proving aperiodicity. These are existence arguments, not quantitative mixing bounds; acceptance, persistence, and path autocorrelation still need measurement.

## What distribution and energy are measured

At position k the stationary marginal is exactly

 Prob(xk=z)=[G^k 1](z)[G^(n−k)1](z)/Z_n.

For even n, the midpoint is the normalized square of psi_n=G^(n/2)1. Thus diagonal midpoint observables are pure expectations in this finite projected vector. Endpoints instead have marginal [G^n1](z)/Z_n, generally a different distribution.

If G=I−H/M with real symmetric H, its endpoint local-energy estimator is (H1)(z), since H commutes with G. For even n,

 E_endpoint = [1^T G^n H1]/Z_n
 = [psi_n^T H psi_n]/[psi_n^T psi_n].

This special commutation identity does not turn every endpoint observable into a pure estimator. It also concerns the exact energy of the finite projected vector, not automatically E0.

For the declared ice H=V Nf−A and M=3 Volume, A1=Nf with geometric multiplicity retained. Hence H1=(V−1)Nf and b=1+(1−V)Nf/M. For V<=1, b>=1. The existing uniformly proposed-face kernel, flipping a flippable face with probability 1/b, has off-diagonal weight 1/(Mb) per face and stay weight 1−Nf/(Mb); multiplying by b gives G including its diagonal. These claims were compared to the complete source-energy derivation, which explicitly retains duplicate destinations. This review does not review any newly written stochastic implementation.

If G is primitive, its positive Perron eigenvector is the lowest eigenvector of H, and the finite projected vector converges to it because the uniform vector has positive overlap. The rate depends on all subleading absolute eigenvalue ratios and the initial spectral amplitudes. G may have negative eigenvalues despite nonnegative entries. The path law is an exact discrete-power projector; it is not exp(−tau H) at tau=n/M. No continuous-time or uniform-size convergence theorem follows from the displayed stationarity formula.

## Exact bounded evidence and disposition

The prospective checker uses exact Fractions throughout transition construction, invariant mass, marginal and energy identities. Eleven fixtures cover two asymmetric-row-sum states, a sparse three-state graph, and constant-row controls, with one through four bonds. The largest lifted matrix has198 states. All3435 checks pass in approximately0.036s. No actual ice production or long path was run.

The same fixtures kill three actual transition mutations on every n>=2 nonconstant-row case: inverted acceptance ratio, omitted acceptance, and holding direction on rejection. The one-bond and constant-row controls deliberately retain zero mutation residuals where those distinctions disappear. All raw residuals and reducibility results are preserved rather than counted as false mutant kills.

Disposition: mathematical sampler design PASS under the precise path/row/proposal contract, with the above ergodicity and finite-projector qualifications. Computational usefulness, burn adequacy, ratio precision, long-path mixing and large-volume physics remain untested by these controls.
