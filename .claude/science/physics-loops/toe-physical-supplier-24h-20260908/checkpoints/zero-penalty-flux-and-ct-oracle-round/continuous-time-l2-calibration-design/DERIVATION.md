# Full-component CT calibration oracle and bounded stationary-start target

This is deterministic design/oracle work only. Root supplied the uniformization route before this derivation. The supplied model is H=(19/20)Nf-A on the864-state L2 seed-reachable component with24 distinct geometric faces. No identification with all zero-flux configurations is used. T denotes total continuous path time: psi=exp(-T H/2)1. Proposed T=1/2 and2 are short calibration times, not ground projections and not the old finite-G tau values.

## Positive uniformization and an explicit truncation bound

With M=24 and G=I-H/M, every entry is nonnegative, row sums lie in[1,21/20], and

 exp(-TH)=exp(-x) sum_k x^k G^k/k!, x=MT.

Under free uniform endpoints, the auxiliary count weight is exp(-x)x^k(1^T G^k1)/k!. It is not an ordinary Poisson law unless those endpoint factors are constant. Since G1>=1, the full normalization Z>=864. Since G1<=(21/20)1, the omitted normalized weight above K is at most

 delta_K <= exp(-x) sum_(k>K) lambda^k/k!
          = exp[x/20] Pr(Poisson(lambda)>K), lambda=21x/20.

The code evaluates a wholly rational upper bound. Let L_J(x)=sum_(j=0)^J x^j/j! <=exp(x), J=ceil(x)+64. For K+2>lambda,

 delta_K <= [lambda^(K+1)/(K+1)!]/[(1-lambda/(K+2)) L_J(x)].

Choose the least K starting at floor(lambda) for which this bound is<=1e-14. The count first-moment tail is bounded by

 eta_K <= lambda [lambda^K/K!]/[(1-lambda/(K+1))L_J(x)].

These are exact Fraction inequalities; no numerical exponential, fitted tolerance or sampled target enters selection. The resulting K are49 at T1/2 and116 at T2; TV upper bounds are2.8000e-15 and9.5806e-15. These bounds apply to conditioning the IDEAL continuous-time augmented law on auxiliary count<=K and then discarding self events. They do NOT prove total-variation accuracy for an actual floating event-time implementation: a finite grid is atomic. Any future implementation must separately disclose/arbitrate floating-time and CDF errors or use exact-real machinery.

## Exact finite-cutoff count and path arithmetic

Put B=480G. Its diagonal is480-19Nf and each allowed face has weight20. Store integer h_k=B^k1 and hN_k=B^kNf. No eigenstate fit or floating matrix power is needed. For the chosen rational times, D=20/T is an integer; a common-denominator count weight is

 w_k = [D^(K-k) K!/k!] sum_x h_k(x).

Normalize these positive integers. Given k, draw the initial state with weight h_k(x); a self or legal face label has weight B_xy h_(remaining-1)(y), normalized by h_remaining(x). The self label is one aggregate diagonal entry. The weights telescope to product B entries divided by1^T B^k1. A BFS witness establishes the chosen initial state lies in the declared component. Count/state choices could use ideal unbiased integer bits, avoiding an unnecessarily rounded discrete CDF; no such random routine has been implemented here.

Given k, sorted ideal independent uniform times on[0,T] and the discrete path yield the truncated augmented law. Discard diagonal self events; every remaining event is a legal face flip. A finite k cutoff is an explicitly bounded approximation, not an exact CT initializer. Uniform-time rounding, collisions and events near T/2 need reviewed handling before real code is called stationary. At the ideal level an exact invariant face-Gibbs kernel cannot amplify the initial TV discrepancy; this does not bound numerical-kernel errors or relaxation of a constant seed start.

## Exact oracle moments for that bounded approximation

All finite-cutoff values in ORACLE.json are exact rational numbers. Let c_k=D^(K-k)K!/k!, Z_K=sum_k c_k sum h_k. A diagonal midpoint insertion F has numerator

 sum_(k<=K) c_k 2^-k sum_(j=0)^k binom(k,j) h_j^T F h_(k-j).

The binomial factor counts how many auxiliary uniform times fall before T/2. An all-time average diagonal insertion instead uses (k+1)^-1 sum_j h_j^T F h_(k-j), because ordered-uniform spacings have equal mean T/(k+1). Endpoint insertions are 1^T F B^k1 and two-endpoint insertions F1^T B^k F1. All24 link-sign endpoint pairs are computed individually for normalized endpoint overlap, with no symmetry reduction.

The literal pooled source is X=sum of six |O_ab(pi)|². With signed bit values z_e=2bit_e-1,

 X=(1/32) sum_(a!=b)[sum_(e=(r,b))(-1)^(sum(r)+r_a) z_e]^2,

so0<=X<=12. The endpoint readout is h=(V-1)Nf=-Nf/20. The retained raw moments are midpoint Nf,X,X²; endpoint average h; h_left h_right; midpoint X times endpoint-average h; time-average Nf; endpoint spin overlap; physical-event count; and normalized temporal Hamming activity=event_count/(6T).

For physical event count, put S_k=sum h_k and F_k=sum_j h_j^T Nf h_(k-j). The weighted nonself-count numerator at k is

 k S_k -480k S_(k-1)+19 F_(k-1).

This follows by inserting B_off=B-diag(480-19Nf) at each of k positions. It counts actual nonself flips, not auxiliary self steps. All computed coefficients are nonnegative.

A bounded observable with range width W has CT expectation discrepancy<=W delta_K. Physical count is unbounded, but its omitted first moment is<=eta_K because it is at most auxiliary k. Hence its expectation discrepancy is<=eta_K+delta_K times its computed finite-cutoff mean. The same bound divided by6T applies to Hamming activity. Every such rational bound is stored explicitly. They are truncation bounds, not Monte Carlo confidence intervals.

## Independent route checks and finite-state source quotients

The supplement forms an independently truncated HALF-time vector using integer powers, squares it and normalizes. The event that either half count exceeds K is a subset of total auxiliary count>K, so its own TV discrepancy is bounded by the same delta_K. Its midpoint Nf and X differ from the total-count oracle by at most twice the appropriate range times delta_K, as verified exactly. This checks a different convolution rather than restating the first formula.

Two bounded order signals are also evaluated through this half-time vector: electric corner intensity sum_a m_a(pi,pi,pi)^2 and face-plane flippability anisotropy. Their exact L2 diagonal numerators are sum_a(sum_edges_axis z_e)^2/256 and(3 sum_plane N_plane²-Nf²)/192, with bounds3/4 and2/3. These are finite-component descriptive observables, not thermodynamic order claims.

The previously reviewed endpoint-residual proof was read in full. Replacing G^m by exp(-TH/2) preserves its symmetry/commutation algebra. At the true CT target, E is the endpoint h expectation, and

 D=(V<Nf>-E)/(2<X>), C=<Xh>/<X>-E, R=D+C

for this q=pi, volume8 six-source normalization. R is relative to E_psi, not the unknown E0. The supplement propagates exact raw truncation intervals through these ratios with a strictly positive denominator lower bound. It does not use the finite-cutoff raw law as an exact Rayleigh state identity. Displayed decimal bounds are rounded; exact rational interval endpoints are retained.

The CT identity E[event_count]=T(V<time-average Nf>-E) is independently checked within the derived truncation bounds. No direct ground-state inference is made from agreement.

## Results and boundary

The main exact oracle passed8643 explicit checks in5.095928s, maximum109.3125MiB, under -OO. It preserves every backward integer column and BFS witness. The completed supplement has875 checks, including the independent half-vector route and all-state bounded order readouts. Original supplemental output before added order readouts/exact interval serialization is preserved; no failure or sampled outcome was hidden.

At T1/2, midpoint X=2.4630667169, D=1.6382568586, C=.0171958600, R=1.6554527186. At T2, X=2.4393503644, D=1.6607045272, C=.0019261787, R=1.6626307058. These are short finite-projector reference values with explicit truncation bounds. No stochastic code or cost profile has run; the design cannot yet claim feasible coverage, equilibration, machine-exact stationary initialization, a gap, a pole, or a phase.
