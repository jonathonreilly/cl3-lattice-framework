# Uniform global energy-mean defect of the full-line local Record lift

Independent verification of the root conjecture. The stated bound is valid for
the COMPLETE Record column, before cap compression or energy-shift rounding,
with the FULL original total Hamiltonian used for free evolution. It is uniform
in finite lattice volume on the legal one-head domain. This is not exact energy
conservation and not a theorem about an infinite-volume global energy operator.

## 1. Definitions and exact defect identity

In one eligible source fuel/head/native-code sector, let

    Hrem=dGamma(h),       Hrem,R=dGamma(h_R),
    Hext=Hrem-Hrem,R=dGamma(h_ext),       h_ext=h-h_R.

Hrem contains every surviving hopping except the selected h_e; h_R retains a
subset of its WHOLE hoppings near e. The selected h_e itself is kept in both
input comparison Hamiltonians. Source and target full sector energies are
Ain=Hrem+h_e+F Delta and Aout=Hrem,target+(F-1)Delta. The complete native
Record column K obeys K^dagger K=I and intertwines the surviving terms.
Define

    E_R(tau)=exp(-iHrem,R tau) exp(i(Hrem,R+h_e)tau),
    Y_R(tau)=exp(iDelta tau) K E_R(tau).

With the Fourier convention exp(+i tau E), E_B=-i partial_tau. A direct
calculation, using E_R'=i h_e,R^-(tau)E_R, gives

    D_R(tau)
      := [E_B,Y_R]+Aout Y_R-Y_R Ain
       = exp(iDelta tau) K [Hext,E_R(tau)].             (G1)

The fuel Delta terms cancel exactly. Here Hext means the OMITTED surviving
matter Hamiltonian, not the target Hamiltonian. This notation avoids the two
conflicting meanings of Hout in the sketch. If the selected h_e were omitted
from the truncation, (G1) would not be the stated local-quench identity.

The corresponding complete-column adjoint energy-drift fiber is explicitly

    G_R(tau)=Y_R(tau)^dagger D_R(tau)
            =E_R(tau)^dagger Hext E_R(tau)-Hext.         (G2)

It is Hermitian. This identity explains why there is no Cauchy-Schwarz square
root or extra factor two in the expectation estimate below. Norms and identities
refer to the legal source code; the source/target embeddings and the complete
bridge instrument are as established in the ambient and quench reviews.

## 2. Local commutator bound without an extensive many-body norm

Let d<=6 and |a_f|<=t. Because h_ext consists of the omitted adjacency edges,
not an arbitrary difference of matrices, its row/column sums give

    ||h_ext||<=dt,       ||h_R||<=dt.

Let r be the minimum graph distance from {v,w} to an endpoint of any omitted
nonzero hopping, using the full surviving graph; put m=r+1. If no such hopping
is reachable, the commutator is zero. For n<r,

    h_ext h_R^n |v>=h_ext h_R^n |w>=0.

Consequently, for u_R,x(s)=exp(-ih_R s)|x>,

    ||h_ext u_R,x(s)|| <=dt T_r(dt|s|),
    ||h_ext u_R,x(s)|| <=dt,
    T_r(x)=sum_(n>=r) x^n/n!.

The second bound uses normalization and holds for all times. In particular,
when r=0 the first expression has T_0=e^x and is not a locality improvement;
the uniform dt bound should then be used.

The commutator [Hext,h_e,R^-(s)] is an even CAR bilinear with four terms:

    a_e [ c^dagger(h_ext u_v)c(u_w)
          -c^dagger(u_v)c(h_ext u_w)
          +c^dagger(h_ext u_w)c(u_v)
          -c^dagger(u_w)c(h_ext u_v) ].

Applying ||c(f)||=||f|| on the faithful Fock representation gives

    ||[Hext,h_e,R^-(s)]||
        <=4dt^2 min{T_r(dt|s|),1}.                     (G3)

Restriction to fixed N or source-component parity cannot increase the norm.
No estimate of ||dGamma(h_ext)|| by N||h_ext|| is used. The statement therefore
remains independent of N and volume; bridges cause no change in this source-
code argument. Odd creation/annihilation symbols are norm-estimation devices,
not claims of local physical odd operators on the native edge carrier.

Duhamel evolution of [Hext,E_R] with the unitary echo and integration of either
bound in (G3) imply

    ||D_R(tau)|| = ||[Hext,E_R(tau)]|| <= g_R(|tau|),

    g_R(u)=min{4t T_m(dt u), 4dt^2 u}.                  (G4)

This proves the conjectured constants. For r=0, m=1, T_1(x)>=x, so (G4) reduces
to the linear bound. For t=0 the defect is zero. The function g_R is nonnegative
and nondecreasing. With the support-distance ball and seed-star convention of
NATIVE_QUENCH_LOCALITY.md, one may uniformly use m>=floor(R/2)+1.

The finite-volume many-body Hext is of course bounded. Its norm is not used in
the uniform estimate (G4), but its finiteness also removes operator-domain
ambiguities before taking any volume-uniform comparison.

## 3. Complete GKSL energy drift and the one-head rate bound

For a complete source column with jumps sqrt(gamma)Y_R,z, the GKSL adjoint on
full total energy is gamma G_R. The free term contributes zero because it is
constructed with the FULL original Htotal=A+E_B. Globally, each fixed directed
edge has source eligibility

    P_vw=n_v^head q_e,

which commutes with the full Hamiltonian. Both the original and locally
truncated Record columns have effect P_vw. Hence (G2) applies blockwise and

    -g_R(u)P_vw <= G_vw,R(u) <= g_R(u)P_vw.

On the supplied one-head subspace,

    sum_directed_edges P_vw
       =sum_v n_v^head sum_(e incident v)q_e <=d I.

Thus a uniform total rate bound is Lambda=gamma d (or d times the maximum
edge rate). One must NOT replace this by gamma times the total number of lattice
edges. Fixed one-head number is load-bearing; an extensive number of heads would
reintroduce a corresponding extensive factor. Trapped sectors contribute zero.
Source masks/old signs are orthogonal blocks and all obey the same local bound,
so controlled-fuel coherences and the history-erasure channel do not increase it.

For an arbitrary correlated current matter/battery/reference state, let its
positive Fourier-diagonal conditional density have trace p_s(tau). From (G2)
and the operator inequality directly,

    |d/ds <Htotal>_s|
       <=Lambda integral p_s(tau) g_R(|tau|) dtau.       (G5)

No product-state assumption is needed at intermediate times, and no pointwise
Cauchy-Schwarz estimate is needed. The sign of the defect is not fixed.

## 4. Unconditional Fourier marginal under laboratory evolution

Each full-line Y_R is a multiplication operator in tau. At every tau, a complete
GKSL dissipator has zero trace on the diagonal conditional density. The internal
Hamiltonian commutator also has zero trace. E_B=-i partial_tau gives transport
with the sign

    partial_s p_s(tau)=-partial_tau p_s(tau),
    p_s(tau)=p_0(tau-s).                                (G6)

This follows for the UNCONDITIONAL trace over every system sector, including
dark/trapped sectors and retained correlations. A normalized selected trajectory
or postselected event need not have the same marginal. Indeed pointwise trace
cancellation holds for any multiplier GKSL jumps; completeness is specifically
needed for the simpler energy-drift identity (G2), not for the marginal transport
alone.

For the original product sine battery, p_0=|beta_hat|^2. More generally (G6)
uses whatever initial Fourier marginal was actually supplied. Correlations formed
by earlier retained-battery events do not reset or replace this unconditional
marginal.

## 5. Laboratory-time bound and verified tail constants

For laboratory horizon T>=0 and cutoff U>0 define

    eta(U)=integral_(|u|>U) p_0(u)du,
    mu1tail(U)=integral_(|u|>U) |u| p_0(u)du.

On |u|<=U and 0<=s<=T, monotonicity gives g_R(|u+s|)<=g_R(U+T). On the tail
use the global linear part of (G4), 4dt^2(|u|+T). Substituting (G6) into (G5)
and integrating yields exactly the proposed valid bound

    |<Htotal>_T-<Htotal>_0|
       <=Lambda T { g_R(U+T)
                     +4dt^2[mu1tail(U)+T eta(U)] }.    (G7)

Keeping the laboratory-time integration in the last term gives the slightly
sharper optional replacement T eta(U) -> (T/2)eta(U) inside the braces. Neither
bound incurs a volume or N factor.

For a width-w sine packet, the already derived pointwise Fourier bound is
p_0(u)<=16pi/(w^3 u^4) when |u|>=sqrt(2)pi/w. Therefore, for
U>=sqrt(2)pi/w,

    eta(U)<=32pi/(3w^3 U^3),
    mu1tail(U)<=16pi/(w^3 U^2).                         (G8)

Both constants include the two tails and are correct. The inverse-square first
moment tail, rather than the inverse-cubic probability tail alone, is necessary
for this mean-energy estimate.

For example, with fixed laboratory T, choose U=m/(2e dt)-T when it is positive
and satisfies the threshold for (G8). Then the short-time term is bounded by
4t*2^(-m)/(1-1/(2e)), while the dominant tail term in (G7) scales as U^(-2).
This demonstrates a uniform-in-volume vanishing mean defect as the neighborhood
grows. It is a mathematical cutoff choice, not tuning of the physical packet,
gamma or observed trajectories. No favorable small-radius number is asserted.

## 6. Domain and non-transfer conditions

Work in each finite volume with a trace-class initial state of finite absolute
battery-energy first moment and the stated finite Fourier first moment. The
sine packet satisfies both. Local truncated fibers are differentiable with
bounded derivative in each finite volume, so jumps preserve the appropriate
energy form domain. A bounded-rate interaction-picture jump construction gives
well-defined full-line dynamics, despite the unbounded free E_B. Energy identities
can equivalently be obtained first on regular energy-domain vectors and then by
approximation. The volume-uniform integrable majorant is (G4)-(G8).

The conclusion concerns differences of finite-volume GLOBAL energy means with
uniform constants. It does not define a finite global energy expectation for an
infinite lattice with infinitely many particles, and does not assert that its
full-line GKSL generator including free E_B is a bounded generator.

Do not transfer the result without another proof to:

- cap-compressed or cap-completed jumps: energy caps act nonlocally in tau,
  so (G6), completeness and/or the exact echo defect require reanalysis;
- rounded energy shifts: the exact echo/commutator identity (G1) changes,
  even if some Fourier-marginal transport property happens to survive;
- the occupation-filtered feedback column KJ: it is not complete, its J factor
  evolves, and (G2) is not its adjoint drift formula;
- a model whose free Hamiltonian is also changed from the full original one:
  an additional free commutator defect must then be included;
- a fresh product-battery assumption after each selected event, or a claim about
  every conditioned trajectory's energy mean.

The statement controls a signed mean-energy defect. It is neither exact total-
energy-distribution conservation nor a bound on all higher energy moments or
all possible energy readouts. Positive-energy apparatus realization, cap safety,
local reservoir implementation, entropy and renewal remain separate obligations.
