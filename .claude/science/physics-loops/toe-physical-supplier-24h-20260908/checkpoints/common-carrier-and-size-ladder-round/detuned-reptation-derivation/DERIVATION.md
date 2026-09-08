# Exact finite-projector reptation: balance, targets and limits

Root supplied the candidate before this derivation. This is a conditional Monte Carlo construction for the existing finite ice Hamiltonian, not a derivation of its physical law or equilibrium preparation. Fix one finite connected move component, M geometric plaquettes, D(x)=Nf(x), adjacency A including any move multiplicities, H=V D-A, and delta=1-V>=0. The RK proposal P=I-(D-A)/M is symmetric stochastic. Thus G=I-H/M=P+delta D/M is symmetric nonnegative, with b(x)=sum_yG(x,y)=1+delta D(x)/M>=1 and Q(x,y)=G(x,y)/b(x). Uniform-face proposal plus flip acceptance1/b implements Q, including self probability1-D/(M b). This statement is about the actual binary kernel; no enumerated-state oracle is needed for an implementation.

## Fixed-length path and reversible shift

Fix integer n>=1. On paths x=(x0,...,xn) with nonzero weight, set pi_n(x)=Z_n^-1 product_{i=0}^{n-1}G(xi,xi+1), Z_n=1^T G^n1. Uniform trial endpoints are load-bearing; nonuniform trials introduce endpoint factors. Choose a direction with probability1/2. The positive proposal appends z drawn from Q(xn,z) and removes x0, giving y=(x1,...,xn,z). The reverse negative proposal prepends x0 to y with probabilityQ(x1,x0). Symmetry of G gives exactly

 pi_n(y)Q(x1,x0)/(pi_n(x)Q(xn,z))=b(xn)/b(x1).

Consequently positive acceptance is min(1,b(xn)/b(x1)); negative acceptance is min(1,b(x0)/b(x(n-1))). Rejection leaves the path unchanged. This proves ordinary detailed balance after equal random direction choice. Self moves and identical resulting paths do not invalidate the paired-flux proof: sum the individual directional proposal channels. The n=0 case needs a separately defined single-state update and is not covered by the x1 formula.

The denominator is the retained endpoint x1, not the discarded endpoint x0. Replacing it by b(x0) generally violates stationarity. If G is nonsymmetric, an uncancelled forward/reverse edge ratio remains; the displayed rule is then false.

## Persistent direction and rejection flips

Enlarge to (x,s), s=+ or -, with target pi_n(x)/2. In direction s propose the corresponding shift and use the same acceptance, retaining s on acceptance. On rejection retain x and flip s. Let K_s(x,y) denote accepted directional transitions, including accepted self transitions, and a_s(x)=sum_yK_s(x,y). The preceding identity gives skew detailed balance

 pi_n(x)K_+(x,y)=pi_n(y)K_-(y,x).

Incoming probability into (x,+) is pi_n(x)a_-(x)/2 from accepted positive transitions plus pi_n(x)(1-a_-(x))/2 from rejected negative transitions. It equals pi_n(x)/2; the other sign is identical. Thus the rejection-flip lift is exactly stationary. It is generally not ordinary reversible dynamics. This proof does not establish faster mixing, irreducibility of every lifted class or a central limit theorem. Optional random direction refresh preserves the target but changes the frozen algorithm and must be specified prospectively.

At RK b=1, every proposal accepts, so the persistent direction never flips. Each sign sector separately has the stationary sliding-window distribution of the ordinary P chain. This reducibility of the auxiliary sign does not bias path observables when that sector has equilibrated, but forbids claiming unique lifted stationary distribution from the balance proof. Equal random ends at RK are also stationary, with possible diffusive window refresh. Persistent direction can refresh a length-n window in n accepted moves, but strong autocorrelation of endpoints/midpoints and slow physical modes remain; no universal cost gain follows.

## Exact finite-projector observables

The marginal at path position k is proportional [G^k1](x)[G^(n-k)1](x). For even n=2m the midpoint law is exactly psi_m(x)^2/||psi_m||², psi_m=G^m1. Endpoint law is proportional(G^n1)(x). Since H1=(V-1)D and H commutes with G, the endpoint average

 E_n=(V-1)<D>endpoint = 1^T H G^n1/Z_n

is, for even n, exactly the Rayleigh energy <psi_m,H psi_m>/||psi_m||². The same identity holds for either endpoint; averaging endpoints is legitimate and its covariance must be retained. At odd n the quotient remains exact but is not the displayed squared-state Rayleigh expression. Midpoint D and S are pure finite-projection expectations, without population branching or forward genealogy bias. Finite path length and Markov sampling bias have not disappeared.

For the sum-six staggered-electric source, the local double-commutator identity gives the finite-state Dirichlet quotient qhat²(V<D>mid-E_n)/(Volume*S_mid). This follows from the kinetic expectation <A>=V<D>-E_n and the summed flip increments. However, for a nonground psi_m the energy-weighted O psi_m spectral measure includes a residual term involving (H-E_n)psi_m. Thus calling this quotient the ground spectral centroid or applying the ground supported-gap bound still needs projection control. It is not enough that endpoint energy is measured exactly for the finite projector.

Ground projection requires the Perron eigenvalue of G to dominate all other absolute eigenvalues on the supplied component. Nonnegative irreducibility alone permits periodicity; positive diagonal somewhere makes the component primitive. The actual component has an RK seed self-loop and retains it for delta>=0, so this condition holds, subject to the reviewed connectivity/component premise. G^m is a discrete polynomial projector. Assigning beta=n/M is only a heuristic first-order correspondence to exp(-beta H): exact finite-n targets must use G, not silently continuous time. At V>1 this proposal's positivity/row-sum argument must be rechecked rather than imported.

## Memory and implementation obligations

An exact path can be stored as a circular buffer of n elementary state changes (face index or self sentinel) plus head, tail and midpoint configurations. A shift updates each stored configuration by its adjacent involutive face move, and modifies one buffer entry. Self-transition multiplicities must be summed in Q; storing the resulting self move is sufficient, whereas treating proposal labels as the target path variables changes the measure unless their weights are included. Rejected moves change neither buffer nor configurations, only the lifted direction. Independent direct reconstruction checks are needed to rule out buffer/midpoint errors.

The algorithm removes branching-population bias only if it correctly samples the stated path measure. It substitutes path-chain equilibration/autocorrelation and finite-projector error. Proposed actual L2 oracle: independently enumerate the existing864-state component once, form exact sparse G at V=.95 and RK, compare normalized G^m1 midpoint moments and endpoint E_n for predeclared m (e.g24,96,384). Then test a binary-state circular-buffer implementation against direct path reconstruction, small exact transition balance and independent-chain Monte Carlo. No such stochastic production is authorized here. Projection-length, direction refresh, burn and independent replicas must be frozen before any calibration; stationary balance alone is not calibration.

## Explicit time and move-label clarification after root review

n above is the TOTAL number of projector bonds. The one-sided projection time convention is tau=n/(2M), because the midpoint amplitude is G^(n/2)1; n/M is the two-sided total, not the one-sided time. Neither convention replaces the exact finite-G formulas by exponential propagation.

For implementation with geometric move multiplicities, retaining a face-index buffer means sampling a labeled path. For each legal face use labeled g_face=1/M and the inverse transition uses the SAME face label; the single self label has aggregated g_self=1-V*Nf/M. Their sum is b. Q_label=g_label/b makes the identical row-sum cancellation valid on labeled paths; marginalizing labels recovers the state path G with its multiplicities. All failed nonflippable proposals and extra diagonal weight must collapse to that aggregated self label, not be counted as independent unit-weight paths. A path filled with self labels at the seed is admissible when g_self>0 but not equilibrated. These clarifications leave the state-path and lifted balance proofs unchanged and do not add an ergodicity claim, including one-bond/constant-b cases.
