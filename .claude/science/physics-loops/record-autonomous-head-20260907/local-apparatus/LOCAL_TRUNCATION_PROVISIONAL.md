# Local matter-neighborhood approximation of the shared spectral lift

## Result and scope

There is a conditional constructive approximation statement, provided the input
and output Hamiltonians admit bounded finite-range extensions on ONE native
local tensor-product algebra and differ only near the chosen event. Truncating
those Hamiltonians to a ball preserves the complete instrument exactly while
approximating its full shared-battery lift on a fixed product battery input.
For a width-w sine packet, the matter-plus-Record reduced-channel diamond error
has an explicit inverse-cubic radius/width term. Keeping the battery in the
output gives the weaker inverse-three-halves bound from a Stinespring estimate.
Neither result is a global operator-norm approximation uniform over arbitrary
battery states. Neither supplies exact global energy conservation, a finite
battery, one-site operations, or a local physical closed apparatus.

This derivation is independent of any future root memo. No frozen runner was
edited or rerun, and no width/gamma optimization or new fixture was performed.

## Locality assumptions and the flag construction

Work first in a finite physical tensor-product system, not just an abstract
fixed-N matrix dictionary. Let H0=sum_Z Phi0(Z) be a bounded finite-range local
Hamiltonian; assume H1=H0-h_e-Delta I, with h_e supported near e. More generally
it suffices that H1-H0 is supported on a fixed seed S. Native source and target
code sectors must have Hamiltonian extensions of this kind. A faithful CAR
identification by itself does not prove this local extension property. Native
even edge operators in the physical qubit algebra are the intended route to
checking it; unrestricted fermionic tensor-factor identifications must not be
used to declare odd/Jordan-Wigner strings local.

Place an auxiliary flag at the event seed. Set
 Htilde=H0 tensor I_flag -(h_e+Delta I) tensor |1><1|.
For a local branch K, define A=K tensor |1><0|. Direct block multiplication gives
 e^(-i tau Htilde) A e^(+i tau Htilde)
   = [e^(-i tau H1) K e^(+i tau H0)] tensor |1><0|.
Thus the cross-Hamiltonian lift fiber is a block of ordinary Heisenberg evolution
at time -tau. The flag couples only to h_e near the seed; it does not multiply
all distant Hamiltonian terms. The Delta flag term is on-site. In fact its
phase can be factored exactly:
 Y(tau)=e^(+i tau Delta)e^(-i tau(H0-h_e))K e^(+i tau H0).
This common phase does not affect matter-plus-Record reduced output but does
translate the battery and must remain in a retained-battery construction.

For a complete native instrument, package all signs in ONE local column
 W=sum_z |z>_record tensor K_z, so W*W=I and ||W||=1.
The output register is placed at S with degenerate Hamiltonian. It may be
embedded as |z><ready| in a larger register; use the corresponding off-diagonal
flag block above. This avoids paying a separate error per sign or incorrectly
completing each sign. The auxiliary ready/flag/register are mathematical
embeddings/resources, not a demonstrated energy/entropy-free laboratory device.
The locality assumption must include the native K_z on the ambient physical
algebra; a bridge's component-parity formula in a reduced CAR gauge must not
be called a local physical operator without that check.

## A completely specified finite-graph LR constant

One may use the following quoted bounded-interaction theorem; all further
estimates below are derived here. Choose a positive nonincreasing F on graph
distance with finite ||F||=sup_x sum_y F(d(x,y)) and convolution constant C_mu
for F_mu(r)=exp(-mu r)F(r). Define
 J_mu=sup_xy [sum_{Z containing x,y}||Phi(Z)||]/F_mu(d(x,y)),
 v=2 J_mu C_mu/mu.
Theorem3.1/Corollary3.1 of Robert Sims, *Lieb-Robinson Bounds and Quasi-locality
for the Dynamics of Many-Body Quantum Systems* gives, for disjoint supports,
 ||[tau_t(A),B]|| <= (2||A||||B||||F||/C_mu)
                    min(|supp A|,|supp B|) exp[-mu(d-v|t|)].
Source: https://arxiv.org/pdf/1011.4540, Section3, equations18–22.
This applies to bounded interactions on the enlarged native tensor-product
system. Finite-range, bounded-strength interactions satisfy these finite-graph
conditions. Uniform-in-volume constants need a suitable geometry/F assumption;
they do not follow solely from calling a finite cube a lattice.

For an entirely elementary finite-graph choice, take F(r)=1, N=number of sites
INCLUDING local register/flag sites, and C_mu=N. Triangle inequality gives
 sum_z exp[-mu(d(x,z)+d(z,y))] <= N exp[-mu d(x,y)],
so this is a valid (possibly very loose) convolution constant. Then ||F||=N,
J_mu is an explicit finite sum of bounded local interaction norms, and
v=2N J_mu/mu. This supplies valid computable constants without claiming volume
uniformity. For polynomial-growth lattices a decaying summable F can instead
make the constants uniform; that stronger geometry must be separately specified.
No numerical favorable radius is inferred from these intentionally loose bounds.

## Hamiltonian truncation, not an arbitrary conditional expectation

Let B_R be the matter/register/flag ball of radius R around S. Let Htilde_R
retain exactly interactions supported within B_R, and keep the local flag/fuel
term. Let a be the maximum interaction diameter. Require R>a and all of S
inside the truncation. Define W_R(tau) using the input/output diagonal blocks
of Htilde_R and the same W. It acts only on B_R in matter space (and on the
battery through Fourier control).

Let boundary(R) contain omitted interactions whose support meets B_R and its
complement; put b_R=sum_{Z in boundary(R)}||Phi(Z)||. Exterior-only interactions
commute with the truncated evolved A. Duhamel differentiation therefore bounds
the full-minus-truncated evolved operator by the integral of boundary
commutators. Every such Z has d(S,Z)>=R-a (a conservative convention). The
quoted LR estimate applies uniformly to the truncated interaction, whose
J_mu cannot increase. For v>0 define
 C_R=2|S|||F|| b_R/(C_mu mu v).
Then the column fiber error obeys
 delta_R(tau)=||W(tau)-W_R(tau)||
 <= min{2, C_R exp[-mu(R-a)] (exp(mu v|tau|)-1)}
 <= min{2, C_R exp[-mu(R-a-v|tau|)]}.                  (1)
For v=0 use the continuous integral form with |tau| instead of division by v;
if b_R=0 the error is exactly zero. These constants can be replaced by any
sharper valid LR/truncation bound. Boundary growth is explicit in b_R, not
silently absorbed into a radius-independent prefactor.

The tensor extension by an arbitrary reference system does not alter operator
norm (1), so the resulting channel estimates are dimension independent in the
reference dimension. This is important for a genuine diamond-norm statement.

## Exact completeness survives this truncation

Because the same truncated output Hamiltonian acts on all recorded signs,
 sum_z Y_z,R(tau)*Y_z,R(tau)
 = exp(-i tau H0,R) [sum_z K_z*K_z] exp(+i tau H0,R)=I.
Thus the Fourier multiplier column is an isometry on the full-line battery,
and its product-input channel is CPTP. No polar-normalization fix is needed.
An arbitrary local approximation to each branch would not automatically have
this property; truncating the two Hamiltonians coherently is the key choice.
The local fuel phase above is included exactly.

For occupation-directed B_z=K_z c_w†c_v, the sign sum is M_e=n_v(1-n_w),
not I. Both full and truncated columns are contractions for a single edge,
and give CP trace-nonincreasing event maps. The bounds below still apply to
these subnormalized maps with ||W||,||W_R||<=1. Their effects are generally
different conjugates of M_e; do not assert identical hazards or complete them
to an identity-rate jump generator. Summing edges and comparing full GKSL
semigroups needs an additional rate/no-jump error argument; it is NOT proved
by the single-event estimate. Adding an absorbing failure flag can mathematically
complete a one-shot instrument, but would be a separate modeling decision.

## Sine Fourier density and explicit tail

Use the unitary Fourier convention beta_hat(tau)=(2pi)^(-1/2) integral
exp(i tau E)beta(E)dE and beta(E)=sqrt(2/w)sin(pi(E-L)/w)1_[L,L+w].
Elementary integration yields the normalized density
 p_w(tau)=|beta_hat(tau)|²
   = [4pi/w³] cos²(w tau/2)/(tau²-pi²/w²)²,             (2)
with removable values at tau=+/-pi/w. Translation L affects only a phase;
it does not affect p_w. For T>=sqrt(2)pi/w,
 p_w(tau)<=16pi/(w³ tau^4) for |tau|>=T,
 eta_w(T)=integral_|tau|>T p_w(tau)dtau
          <=32pi/[3(wT)^3].                           (3)
Use min(1,the right side) when convenient. The finite tail is not zero. Equations
(2)–(3) are derived by integrating the sine and bounding
(tau²-pi²/w²)²>=tau^4/4; no asymptotic replacement is used in the inequality.

## Two different fixed-battery channel norms

Fix the initial battery to |beta><beta|, uncorrelated with an arbitrary matter
input and an arbitrary reference. This restriction is load-bearing.

1. Discard battery, retain matter and Record register. The channel is
 Phi_beta(rho)=integral p_w(tau)W(tau)rho W(tau)*dtau.
For contractions, the telescoping identity for Kraus products gives
 ||Phi_beta-Phi_beta,R||_diamond <=2 integral p_w delta_R.
Splitting at T and using (1), set
 epsilon_R(T)=C_R exp[-mu(R-a-vT)].
Then
 ||Phi_beta-Phi_beta,R||_diamond
 <= min{2, 2epsilon_R(T)+4eta_w(T)}
 <= min{2, 2epsilon_R(T)+128pi/[3(wT)^3]}.             (4)
This includes recorded outcomes; it does not compare normalized postselected
branches. Conditioning on a very rare outcome can amplify an absolute error.

2. Retain the shared battery in the output. Product-input Stinespring columns
V_beta and V_beta,R differ in operator norm by at most
 sqrt(integral p_w(tau)delta_R(tau)²dtau).
The same telescoping estimate, now before discarding the battery, gives
 ||Psi_beta-Psi_beta,R||_diamond
 <= min{2,2sqrt(epsilon_R(T)²+4eta_w(T))}
 <= min{2,2epsilon_R(T)+4sqrt(32pi/3)(wT)^(-3/2)}.     (5)
The smaller power in (5) is essential: retaining coherent Fourier-tail amplitudes
cannot be bounded by simply averaging the matter-channel distance. These are
norms of maps whose input is matter (and any reference), with the battery fixed
by the definition of the map; not unrestricted diamond norms on matter+battery.

For R>a and v>0, choose T=(R-a)/(2v), provided wT>=sqrt(2)pi. Then the short-time
term is C_R exp[-mu(R-a)/2], while (4) has tail128pi/3 times
[2v/(w(R-a))]^3, and (5) has tail4sqrt(32pi/3) times
[2v/(w(R-a))]^(3/2). The prefactor C_R and velocity geometry must be retained.
This is a bound, not a prescription to tune the frozen scientific packet.

## What the bound does not yet implement

* Arbitrary correlated battery inputs, including states after previous events,
  are outside the single-product-input theorem. A fixed finite sequence can
  sometimes be treated by telescoping its full Fourier column from the ORIGINAL
  product input; simply reapplying (4) after each retained-battery event is invalid.
* Fourier control still involves a continuous battery degree of freedom. Local
  matter support of W_R does not specify a finite-qubit battery or an implementable
  local Hamiltonian coupling. The flag proof is a mathematical embedding, not a
  physical closed-unitary implementation or a preparation/entropy-cost account.
* The truncated lift exactly intertwines H0,R+E_B with H1,R+E_B on the full
  energy line. It generally fails to intertwine the FULL H0+E_B and H1+E_B.
  Thus it does not exactly conserve the original total-energy distribution.
  A small trace/diamond error is not by itself an energy-error bound for an
  unbounded battery observable. One would need support/moment control or a
  bounded capped-energy estimate with quantified leakage.
* The original exact lift has the proven safe cap[0,97] for the frozen packet.
  The approximation need not inherit that safe support. Projecting the approximate
  lift to the cap can destroy completeness; a quantified leakage/failure channel
  is another approximation obligation. No cap-safe truncated apparatus is claimed.
* Local physical Z/Record operations, head/fuel placement, native code constraints,
  and bounded interaction strengths must be checked in the ambient physical
  edge-qubit representation, not inferred from a70d CAR matrix. One-siteZ3-style
  admissibility, memory reset, replenishment and irreversible entropy disposal
  remain separate requirements. No indefinite transport conclusion follows.

## Decision

The route reduces dependence on distant matter terms at the level of a single
fixed-battery event channel with explicit error and exact local-column
completeness. It provides a finite-neighborhood approximation target for a
physical apparatus construction. It does not yet solve the battery realization,
cap, global-energy-conservation or native microscopic implementation residuals.
