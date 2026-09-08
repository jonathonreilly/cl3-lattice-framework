# Full-carrier local charge harmonics and independent theorem check

The supplied model is H=UD+g sum_e lambda_e A_e on the full edge-qubit carrier of even cubic tori with periods at least four. D=sum_v Q_v² and Q_v=epsilon_v(sum_incident x_e-3). All constraints here are energy terms, not deleted states. Native A_e has X on e and only Z on other edges in the two endpoint stars.

For e=(i,j), define r_i=sum_{f incident i,f!=e}x_f and r_j similarly. On a basis column with bit x=x_e, flipping e changes only the two endpoint charge squares. Direct subtraction gives

Delta_e D=2(1-2x)(r_i+r_j-5).

Thus the diagonal local operator M_e=(1-2x_e)(r_i+r_j-5) has integer eigenvalues -5,...,5. Let P_{e,m} be its spectral projector and A_{e,m}=A_e P_{e,m}, with the projector on the input column. Then [D,A_{e,m}]=2m A_{e,m}, A_{e,m}†=A_{e,-m}, ||A_{e,m}||<=1, and sum_m A_{e,m}=A_e. Projector ordering matters. The transformed edge term is exactly sum_m exp(2imUt) A_{e,m}. On ice only m=1 acts: every one-edge flip creates D=2. The m=0 component annihilates ice but is a nonzero resonant transition on the full excited carrier.

The support of every component is contained in S_e=star(i) union star(j), 11 physical edges. It commutes with Q_v² whenever v is not an endpoint. Consequently it is strongly supported on S_e in the sense of Else et al.: it commutes with every charge term whose support is not contained in S_e. Conjugation by exp(itD), averaging and the homological inverse preserve this strong support. Commutators are strongly supported on unions and vanish for disjoint supports. These are operator identities for every volume, rather than observations from the local check.

Global signed neutrality gives D even, since q²=q modulo2 and sum_v Q_v=0. Therefore exp(i pi D)=I, and the interaction-picture perturbation is exactly periodic with period pi/U. This alone does not identify a D-conserving effective Hamiltonian at all orders in an arbitrary Floquet gauge.

For the local tensor product, assign each positive coordinate edge to its tail cubic vertex. There are three qubits per cell. Each 11-edge S_e occupies at most eight connected cells (in fact seven by direct geometric counting). Each physical edge belongs to at most eleven endpoint-star supports; a cell has three assigned edges. Hence for gamma=|g|sup|lambda_e| a conservative interaction norm is j_kappa=33 gamma exp(8 kappa), independent of volume. The finite L4/L6 controls find seven cells and overlap21; the conservative 8/33 bounds suffice and do not depend on those finite observations.

## Exact finite controls

CONTRACT.md was written before execution. The standard-library checker enumerates all2048 endpoint-star bitstrings, literal energy differences, input/output harmonic labels and adjoint phases. It separately constructs L4 and L6 cubic geometry and checks the conservative overlap/support bounds. All10917 explicit predicates pass under Python -OO in .0133s,17.83MiB. Frequency multiplicities are 2,20,90,240,420,504,420,240,90,20,2. These controls are finite and do not prove the prethermal theorem.

## Independent primary-source applicability review

Root read the complete orbital APPLICABILITY.md c85c60a117c889b3bdf605dc25b0db9b7ef0cafb012858ceb66cb9316a7ba3ad, ADHH Sections3.1–3.3,5.3–5.4, and the complete Else–Fendley–Kemp–Nayak AppendixA from the primary PDFs cached with source receipts in the neighboring native-local-prethermal-applicability directory. Public abstract URLs were independently opened:

- https://arxiv.org/abs/1509.05386
- https://arxiv.org/abs/1704.08703

ADHH as originally stated assumes onsite integer N_x; direct application without the extension is not justified. Else et al. AppendixA explicitly extends the averaging/commutator proof using strong support. The preceding exact geometry supplies this requirement for our commuting charge squares. The conservative split bounds ||Vbar||<=j and ||Voff||<=2j yield ADHH scale nu0<=270 pi j/kappa² and sufficient U>=18 pi j/kappa. Choosing the larger conservative nu0 and requiring nstar>=1 gives the orbital exponential remainder bound. Numerical theorem constants are not fitted or claimed known.

The local-dynamics consequence requires a small clarification in its derivation: large UD does not produce a velocity proportional to U because its commuting finite-range evolution enlarges a local observable's support only by a fixed charge-star neighborhood. K commutes with D, so one can factor this rotation from K evolution and apply the Lieb–Robinson estimate to K. Strong-support enlargement changes geometry constants, not volume scaling. The order gamma/U bare-observable dressing correction must remain separate from the small dressed-frame remainder. A polynomial prefactor of degree d+1=4 in time follows from the standard local Duhamel/Lieb–Robinson step, with reduced exponential rate absorbing logarithmic norm-decay factors.

The result is an imported theorem instantiation, not a new general theorem. It controls a high-order quasi-local dressed-D conserving Hamiltonian, not yet the fourth-order ring truncation. The global-norm finite ice spectral bound remains separate; no volume-uniform isolated ice band, bulk phase or physical coupling selection follows.
