---
claim_id: native_record_battery_finite_patch_locality_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional finite-volume tensor-lattice theorem: for a supplied bounded finite-range Hamiltonian, local deletion, and local projective Record isometry commuting termwise with the remaining interactions, a finite-patch spectral battery lift approximates the global lift with explicit volume-uniform instrument-channel bounds. Its exact full-energy intertwining defect is the crossing-energy commutator. For a fixed finite deterministic event schedule and one retained sine-packet battery, the stated joint/channel and unconditional mean-energy bounds hold, including declared free-battery Fourier translations. A cubic boundary-area estimate and the integrable sine Fourier tail give vanishing errors with growing patch radius. Local positive reachable-sector caps are distinguished from a positive global comparison apparatus. Native BKSF placement is supplied; no framework law, spatial battery transport, autonomous implementation, continuum matter or audit status is derived."
upstream_dependencies: []
runner: scripts/native_record_battery_finite_patch_locality_2026_09_07.py
---

# Finite-patch localization of a native Record energy instrument

**Date:** 2026-09-07. **Claim:** conditional mathematical candidate, ready for
independent review after the checks below. No audit verdict is assigned.

The global energy lift for a local Record can be approximated by an instrument
with bounded matter support. The approximation retains the battery between
events and explicitly bounds the energy exchanged across the patch boundary.
Its locality is in a supplied tensor algebra of physical sites. A common
battery accessible at separated events remains a physical communication
resource; this theorem does not construct its transport or an autonomous law.

The framework's current [four axioms](MINIMAL_AXIOMS_2026-06-29.md) and three
approved primitives do not choose the Hamiltonian, ordinary tensor
composition, event instrument, battery preparation or schedule below. These
are conditions of a mathematical model. All conclusions concern that model.
The scale reference, kinetic isotropy and realized-state interface are not
used to supply any of these choices. No parked premise is adopted.

## 1. Exact domain and closest prior result

Let a finite set `Lambda subset Z^3` carry finite-dimensional tensor factors
`H_x`; the native application has `H_x=C^2`. Write

`H = sum_f h_f`, `supp(h_f) subset S_f`, `diam(S_f)<=R`,

with self-adjoint terms, integer `R>=1`, and ambient `l1` distance. Repeated
supports may be treated as separate indexed terms, with their norms all
included in the bounds. Fix `mu>0` and uniform activity controls

`g >= sup_x sum_(f:x in S_f) ||h_f||`,

`kappa >= sup_x sum_(f:x in S_f) ||h_f|| |S_f| exp(mu diam(S_f)) > 0`.       (1)

They must be common across a family of finite volumes. An empty interaction
or zero deleted term is handled directly and gives zero cocycle error.

Delete one named term `h`, set `delta=||h||`, `H'=H-h`, and supply a finite
projective measurement `{Q_z}` supported in a finite nonempty set `X` that
also contains `supp(h)`. The projectors sum to identity, are orthogonal, and
**each `Q_z` commutes with each remaining interaction term separately**.
Commutation with the sum alone would not justify patch truncation. Define the
coherent instrument `W psi = direct_sum_z Q_z psi`; its outcome flag has zero
modeled Hamiltonian. Dephasing the flag gives the ordinary instrument and
cannot increase any channel-distance bound below. The degenerate flag does
not remove its preparation or storage resource.

For an arbitrary patch `P` containing `X`, let `H_P` contain all interaction
terms wholly supported in `P`, including `h`. Put

`H'_P=H_P-h`, `H_ext=H-H_P`,

`B_P=sum_(f:S_f intersects P, S_f not subset P) ||h_f||`.                  (2)

The boundary sum includes terms crossing the patch boundary, even when they
also involve an old recorded site. Terms wholly outside `P` will commute with
all patch operators. For spatial asymptotics use `P=P_r={x:d(x,X)<=r}` within
`Lambda`, integer `r>=R`, and abbreviate `B_r=B_(P_r)`.

All source statements needed for the theorem are given here. Its closest
repository predecessors are the pinned, unmerged native instrument and
shared-battery proposals:

- [PR #7983 source at 4248f6f8a7ffc707d8e4b9bb8f7c0a798eda35c1](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/4248f6f8a7ffc707d8e4b9bb8f7c0a798eda35c1/docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md): native edge instrument and global energy lift.
- [PR #8001 source at 707d7a9c7f929c1c2c16078dfed76acb786e5f3b](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/707d7a9c7f929c1c2c16078dfed76acb786e5f3b/docs/NATIVE_EDGE_RECORD_SHARED_BATTERY_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-07.md): shared battery with nonstationary input, distinct dwell conventions, and a `w^-2` observable bound for a **globally supported** lift.
- The carried finite transport source originated in [PR #7996 at 2ca16ee74d7a19b04b741e83be80434feb1cbe5b](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/2ca16ee74d7a19b04b741e83be80434feb1cbe5b); its schedule and physical margins are not assumptions of this theorem.

The finite-patch approximation and its global-energy boundary estimate are
the new connection proposed here. Global spectral lifting and Lieb-Robinson
localization are established methods, not new principles. The prior
[weighted finite-support LR note](MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
also contains the standard interaction-chain method. Both that note and the
[finite BKSF census](FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-02.md)
are unaudited at frozen main `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`.
They are novelty/comparison sources, not authority for an adopted premise.

## 2. Exact fiber and energy identities

On the comparison battery `L2(R,dE)`, let `E_B` multiply by `E` and
`T_u beta(E)=beta(E-u)`. With Fourier convention

`beta_hat(tau)=(2pi)^(-1/2) integral exp(i tau E) beta(E) dE`,

`E_B=-i d/dtau`. The global energy lift has fiber

`V(tau)=exp(-i tau H') W exp(i tau H) = W C(tau)`,

`C(tau)=exp(-i tau(H-h)) exp(i tau H)`.                                 (3)

Indeed each matrix element from energy `a` to `b` translates the battery by
`a-b`; its outgoing total energy is `b+E+a-b=E+a`. Every fiber is an isometry.
Termwise commutation gives `W H'_P=H'_P W` and `W H_ext=H_ext W` as well.
The localized fiber and its inverse Fourier transform are

`V_P(tau)=W C_P(tau)`, `C_P(tau)=exp(-i tau H'_P) exp(i tau H_P)`,

`Vtilde_P=sum_(a,b) P'_P(b) W P_P(a) tensor T_(a-b)`.                    (4)

Thus (4) acts only on `P`, the battery, and the local outcome register. It is
an isometry, not a truncated series or an unnormalized selected branch.

Differentiating (3), with `alpha_s^A(B)=exp(i s A)B exp(-i s A)`, gives

`C'(tau)=i alpha_(-tau)^(H-h)(h) C(tau)`.                               (5)

The same formula holds with `H_P`. Unitary variation of constants yields

`||C(tau)-C_P(tau)|| <= integral_0^|tau| a_P(s) ds`,

`a_P(s)=max_(sigma=+-1) ||alpha_(sigma s)^(H-h)(h)
                                  -alpha_(sigma s)^(H'_P)(h)||`,       (6)

where both time directions are included explicitly. For general complex
Hermitian interactions their comparison norms need not be equal. A Duhamel comparison of the two Heisenberg
evolutions yields

`a_P(s) <= integral_0^s sum_cross max_(sigma=+-1)
                               ||[h_f,alpha_(sigma u)^(H'_P)(h)]|| du`. (7)

Terms entirely outside `P` commute and are absent from this sum. These are
standard finite-dimensional differentiation identities; no gap is assumed.
Each signed comparison has its own Duhamel estimate; moving the maximum
inside the sum and integral gives (7). The subsequent LR and crude bounds
hold for both signs with the same constants.

The local lift conserves patch energy exactly. Its defect for the **original
full matter energy** is instead

`(H'+E_B)V_P - V_P(H+E_B) = W [H_ext,C_P(tau)]`.                        (8)

To verify the sign, insert
`C'_P=-i H'_P C_P+i C_P H_P` in
`H' C_P-C_P H-i C'_P`; the patch terms cancel and leave the displayed
commutator. Equation (8) holds on the Sobolev domain of `E_B`; bounded finite
matrix coefficients preserve that domain. It includes energy in crossing
terms, rather than redefining that energy as part of a compensating ledger.

For all real `tau`, two elementary estimates already give useful bounds:

`||C-C_P|| <= min(2, delta B_P tau^2)`,

`||[H_ext,C_P]|| <= min(2 B_P, 2 delta B_P |tau|)`.                      (9)

For (7), the commutator sum is at most `2 delta B_P`; integrate twice to get
the first bound. For the second, differentiate `C_P^* H_ext C_P`, use (5),
and integrate the same commutator estimate. The static `2B_P` bound follows
because only crossing terms contribute. If `[H_ext,h]=0`, additionally

`||[H_ext,C_P]|| <= 2 delta B_P ||H'_P|| tau^2`.                         (10)

Here subtract `h` inside `[H_ext,alpha^(H'_P)(h)]` and use
`||alpha_u^(H'_P)(h)-h||<=2||H'_P|| delta |u|`. This stronger premise holds
for the buffers `r>=R`: every crossing support has positive distance from
`X`. Equations (9)-(10) are not exact energy-conservation claims.

## 3. Explicit spatial estimates and the cubic boundary

Put `lambda=2 kappa`. For disjoint supports `X,Y`, the interaction-chain
Lieb-Robinson estimate under (1) is

`||[alpha_s(A_X),B_Y]|| <= 2||A||||B|| |X| exp(-mu d(X,Y))
                          (exp(lambda |s|)-1)`.                       (11)

For completeness, the finite Duhamel recursion bounds its order-`k` term by
`2||A||||B|| (2|s|)^k/k!` times the sum of products of interaction norms
along chains starting at `X`, successive supports intersecting, and ending
at `Y`. The sum of support diameters along such a chain is at least
`d(X,Y)`. Multiply each norm by `exp(mu diam)` and select an intersection
site at every step. Summing backwards, the factor `|S|` in (1) bounds each
continuation by `kappa`, while the first incidence is at most `|X| kappa`.
The chain sum is therefore at most `|X| kappa^k exp(-mu d(X,Y))`.
Summing `k>=1` proves (11); finite-volume iterated-integral remainders vanish
because the factorial dominates the finite interaction count. The final
bound is uniform through (1). This argument does not assume that a pure
exponential spatial weight has a finite convolution constant.

This is the standard LR/Duhamel method. Primary literature checked:
Nachtergaele, Sims and Young, [Quasi-Locality Bounds, Part I](https://arxiv.org/html/1810.02428v2),
Theorems 3.1 and 3.4(ii). Their general interaction-norm formulation supplies
context; (11) states the explicit activity specialization used here.

A crossing support contains a site outside `P_r` and has diameter at most
`R`, so its distance from `X` is strictly greater than `r-R`. Define

`A_r=2 delta |X| B_r exp(-mu(r-R))`,

`F1(u)=(exp(lambda u)-1)/lambda-u`,

`F2(u)=(exp(lambda u)-1)/lambda^2-u/lambda-u^2/2`.                        (12)

They are nonnegative for `u>=0`. Applying (11) to each term in (7) and
integrating proves

`epsilon_r(u)=min(2, delta B_r u^2, A_r F2(u))`,

`b_r(u)=min(2B_r, 2 delta B_r u, A_r F1(u))`,

`||C(tau)-C_r(tau)||<=epsilon_r(|tau|)`,

`||[H_ext,C_r(tau)]||<=b_r(|tau|)`.                                   (13)

Equation (10) can be added to the minimum for `b_r`. Notice the two
integrations in `F2`, compared with the one in `F1`.

The integer `l1` ball in `Z^3` has volume

`V3(r)=(4r^3+6r^2+8r+3)/3`.

Each crossing term touches an inside site whose distance to `X` is greater
than `r-R`. Choose a nearest point of `X` to that site. The site lies in one
of `|X|` annuli, each with at most `V3(r)-V3(r-R)` sites. Summing the local
interaction norm bound `g` over that shell gives

`B_r <= g |X| [V3(r)-V3(r-R)] = O(r^2)` for fixed `R,X,g`.              (14)

Clipping to a finite ambient region can only reduce this upper bound. This
area estimate is a genuine condition of the three-dimensional conclusion;
an uncontrolled boundary size would not give the energy limit below.

## 4. Sine packet: integrable tail and resource price

Supply `w>0`, offset `E_*`, and the real packet

`beta(E)=sqrt(2/w) sin(pi(E-E_*)/w) 1_[E_*,E_*+w](E)`.

Elementary integration gives its even Fourier density

`p_w(tau)=4pi/w^3 * cos^2(w tau/2)/(tau^2-(pi/w)^2)^2`,                 (15)

with removable value `w/(4pi)` at `tau=+-pi/w`. It integrates to one by
unitarity of the Fourier transform. The zero extension is in `H1`, and
Parseval gives

`integral tau^2 p_w(tau) d tau = ||beta'||_2^2 = pi^2/w^2`,

`integral |tau| p_w(tau) d tau <= pi/w`.                              (16)

For `T>=2pi/w`, `tau^2-(pi/w)^2>=3tau^2/4` on the tail. Integrating the
resulting `64pi/(9w^3 tau^4)` upper bound on both half-lines gives

`P_w(|tau|>T) <= q_w(T):=min(1,128pi/(27 w^3 T^3))`.                  (17)

In particular an exponentially growing LR bound must **not** be integrated
against (15) over the entire real line. Nor is the fourth moment finite:
the `tau^-4` oscillatory tail makes it divergent. The cutoff argument below
requires neither that fourth moment nor an exponential moment.

If `m_P=||H_P||+||H'_P||`, every patch spectral shift lies in `[-m_P,m_P]`.
For `K` fixed patch lifts, prepare `E_*>=sum_j m_(P_j)`. Every reachable
prefix battery support then lies inside

`[E_*-sum_j m_(P_j), E_*+w+sum_j m_(P_j)]`.                            (18)

Both allowed dwell conventions preserve support in energy. Taking
`E_*=sum m_(P_j)` gives a positive reachable cap `2 sum m_(P_j)+w` and
initial mean `sum m_(P_j)+w/2`. The theorem is exact on that reachable sector.
A compression to a cap need not be isometric off that sector; a refusal
completion is an additional operation and is not silently included. A finite
energy interval still has infinite-dimensional `L2` Hilbert space.
For a radius-`r` patch, `m_P<=2g|P_r|<=2g|X|V3(r)` is an explicit
volume-independent sufficient allowance, growing cubically with the buffer.

A local cap (18) does **not** necessarily make the global comparator
positive-energy. The comparison (3) is first defined on the full energy
line. If both apparatuses must be cap-safe with the same input, add a global
spectral-shift allowance; it may depend on ambient volume. The local resource
bound and the channel/energy estimates do not assert a uniformly positive
bounded global comparison apparatus.

## 5. Shared-battery theorem, schedules, and quantitative limits

Fix `K<infinity` distinct deletion events and their patches. Event choices,
dwell durations and Hamiltonian coefficients are deterministic supplied
inputs, independent of outcome and battery. Local outcome projectors at
different events commute. Each current event obeys the termwise hypothesis
of section 1 for its remaining Hamiltonian. Previously written projectors
commute with every subsequent Hamiltonian term and event. More general
adaptive schedules require a further proof and are outside this statement.

The initial matter may be in any density operator and entangled with an
arbitrary untouched reference; the initial battery is independently prepared
in `beta`. Keep the same battery throughout. Between events permit either
`exp(-i d_j H_(j-1)) tensor I_B` or the laboratory-free dwell
`exp[-i d_j(H_(j-1)+E_B)]`, for fixed nonnegative `d_j`.

A free-battery dwell acts in Fourier space by `f(tau)->f(tau-d_j)`.
Undoing the final common translation, event `j` is evaluated at `tau+s_j`,
where `s_j` is the sum of free-battery dwell times up to that event. Controlled
matter-only dwells contribute zero. Put `D=max_j s_j`. The remaining matter
unitaries are identical in the two processes being compared and have norm
one. They need not commute with the localized cocycles.

Let `V_K(tau)` and `V_(K,P)(tau)` denote the full instrument fibers after this
change of variable. Telescoping products of isometries gives, for `|tau|<=T`,

`||V_K(tau)-V_(K,P)(tau)|| <= e(T):=min(2,sum_j epsilon_j(T+D))`.         (19)

Each complete instrument is isometric at fixed `tau`, so the full
unconditioned fiber norm remains the original `p_w(tau)`. This statement
keeps matter-battery correlations; it does not reset a reduced channel.
From (17), the joint isometry applied to any matter/reference vector differs
in norm by at most

`eta(T)=sqrt(e(T)^2+4 q_w(T))`, `T>=2pi/w`.                            (20)

Thus the output channel, retaining the battery and Record register if
wanted, has diamond-distance at most `min(2,2eta(T))`. The proof is the pure
state trace-distance bound `|| |a><a|-|b><b| ||_1<=2||a-b||`, also after
adjoining a reference, followed by convexity and partial-trace contraction.

The total-energy operator is unbounded only in the battery coordinate, and
the compact initial energy packet lies in its domain. Apply the exact defect
identity (8) at every event. Identical dwells intertwine the corresponding
total-energy operators; their contribution is zero. Product telescoping and
Cauchy-Schwarz at fixed `tau` therefore bound the **unconditional mean**
full matter-plus-battery energy change of the localized process by

`Eerr(T) <= sum_j b_j(T+D) + 2 sum_j B_j q_w(T)`.                       (21)

This compares its final energy directly with its initial energy, not with a
ledger-defined battery value. Subsequent channel closeness is not used to
bound an extensive global Hamiltonian. A rare normalized outcome history can
reweight the battery density; (20)-(21) apply to the full instrument, including
all history probabilities, and do not promise the same bound on each
normalized branch. Native Record/number preservation below is exact on every
nonzero branch and is a different statement.

There is also an elementary bound useful before a spatial buffer is large.
After tracing the battery, the two complete instrument channels are mixtures
of their fibers with the **same one** density (15). Integrate the trace-norm
bound `2sum_j delta_j B_j (tau+s_j)^2` from (9). Since `p_w` is even,

`||Phi_K-Phi_(K,P)||_diamond
 <= min(2,2sum_j delta_j B_j [pi^2/w^2+s_j^2])`.                       (22)

Likewise (9) and (16) give

`|Delta <H_total>| <= 2sum_j delta_j B_j [pi/w+|s_j|]`.                (23)

When every event has `[H_ext,j,h_j]=0`, (10) strengthens this to

`|Delta <H_total>| <= 2sum_j delta_j B_j ||H'_(P_j)||
                                      [pi^2/w^2+s_j^2]`.             (24)

The `w^-2` controlled-dwell statement (22) is for the reduced instrument;
it is not a `w^-2` norm bound retaining the battery. Free dwell shifts remain
in (22)-(24), so broadening the packet alone does not erase their effect.

For fixed `K,w,D,mu,kappa,R,g,X` and uniformly bounded local data, use equal
buffers `r` and choose

`T=mu(r-R)/(4kappa)-D`, once this is at least `2pi/w`.

Then the LR factors in (13) have net exponential factor
`exp[-mu(r-R)/2]`, multiplied only by the polynomial boundary factor. Equations
(14),(17),(20),(21) consequently prove

`joint channel error = O(r^2 exp(-mu r/2)) + O(w^(-3/2) r^(-3/2))`,

`unconditional mean-energy error = O(r^2 exp(-mu r/2)) + O(w^(-3) r^(-1))`. (25)

The constants are independent of ambient volume; the event count and duration
are fixed. This proves an actual spatial approximation obligation. It is not
an infinite-volume total-energy operator, a hydrodynamic limit, or an unlimited
history theorem. Choosing `r` or `w` to meet a stated error tolerance is an
explicit sufficient resource prescription, not a fit to a physical constant.

## 6. Native edge-qubit specialization

Supply a finite cubic graph of degree at most six. Put the edge `(v,v+e_a)`
qubit at the fine-lattice site `2v+e_a`; other roles are spectators. Vertex
labels, neighbor order and Pauli frames are supplied. In that **physical
site tensor representation**, define

`B_v=product_(e incident v) Z_e`,

`A_ij=epsilon_ij X_ij product_(k<_i j) Z_ik product_(l<_j i) Z_jl`,

`T_ij=(i/2)A_ij(B_i-B_j)`, `h_ij=a_ij T_ij`, `|a_ij|<=t`.

The ordered products omit `ij`; `epsilon_ij` reverses on reversing the edge.
Each `h_e` has norm at most `t`, changes only its own edge in the Z basis,
and has support inside its two endpoint stars. There are at most 11 physical
factors, radius at most two about the edge midpoint and diameter at most four.
A fixed edge qubit can occur in at most the 11 terms sharing either endpoint.
Consequently one valid family bound is

`R=4`, `g=11t`, `kappa=121t exp(4mu)`, `|X|<=11`.                      (26)

Set `Q_(e,z)=(I+zZ_e)/2`. Every other hopping term has only I/Z on `e`, so
the termwise commutation premise is exact. The instrument is supported at the
physical edge qubit; no locality conclusion is transferred from a global CAR
intertwiner.

The number `N=sum_v(1-B_v)/2` commutes with every `h_e` and `Z_e`: only the
two endpoint `B` factors can anticommute with `A_e`, and
`(B_i-B_j)(B_i+B_j)=0` cancels their contribution. All local and global fibers
therefore preserve `N`, as well as old recorded Z values. For the supplied
BKSF cycle code, `S_C=i^length(C) product_(ij in C) A_ij` is central in the
A/B algebra. A hop preserves its current cycle constraints. An edge projection
removes only cycle constraints containing that edge and imposes `Z_e=z`.
On a nonbridge one such cycle anticommutes with `Z_e`, giving
`P Q_(e,z) P=P/2`; on a bridge the relevant boundary product gives its
component parity, including old Z signs. Patch Hamiltonians are sums of the
same code-preserving terms, so these exact Record/code statements survive
the energy localization. The conditional surviving matter state generally
changes; no exact CAR-state identity is claimed for the dressed instrument.

The midpoint roles, ordinary composition and hop Hamiltonian are supplied
carrier/dynamics conditions. Bounded support in (26) does not constitute the
framework's fixed nearest-neighbor Admissibility distribution. The common
battery and outcome register still require a spatial implementation. A
battery reused at separated patches may convey information through its state;
no locality or autonomy theorem for that entire apparatus follows from (25).

## 7. Finite verification and independent-review boundary

The [runner](../scripts/native_record_battery_finite_patch_locality_2026_09_07.py)
imports no parent code and contains two distinct numerical representations:

- Exact spectral-shift formulas for battery overlaps and their first energy
  moments are compared with direct quadrature of the actual joint vector
  `sum_s x_s beta(E-s)` in the battery energy coordinate. This computes battery
  energy directly. Six comparisons, for global/local instruments at widths
  1, 8 and 32, agree in density norm below `7e-16` and battery energy below
  `3e-14` on the declared three-qubit two-event fixture.
- A seven-edge native BKSF ladder uses 128-dimensional physical Pauli matrices.
  Its 15-dimensional `N=2` code spectrum agrees below `4e-15` with a separately
  constructed occupation-sign CAR matrix. Native number, new/old Records and
  bridge boundary parity are checked directly in the physical representation.
  The tested bridge probabilities are approximately `0.717286,0.282714`;
  the runner does not force them to be fair.

The first proper native patch has four edge qubits and one retained hopping
term. At Fourier time `0.3`, cocycle error is `0.106763` and full-energy
intertwining defect is `0.721551`; (8) agrees with direct differentiation.
A patch covering the full ladder gives exactly zero error. This is an explicit
counterexample to treating patch-energy conservation as full-energy
conservation, within this finite construction, not a general impossibility
claim about local apparatuses.

The two-event three-qubit fixture has `sum delta_j B_j=3`. At width 32 its
full-history trace-norm difference is `0.00148598`, below the universal
reduced-channel bound `6pi^2/32^2=0.0578297`. Its actual mean-energy drift is
`-0.0533114`, within (23). At width one the same local process drifts by `-1.5`;
the global lift conserves total energy to below `3e-14` in all three cases.
These unfavorable narrow-packet observations are retained.

In the same fixture, width-one shared-battery histories have probabilities
`(3/8,1/8,1/8,3/8)`, whereas separately reset batteries give `(1/4)^4`.
Their total-variation distance is exactly `1/4`. This independently exposes
why the retained battery must not be replaced by sequential reduced channels.

The explicit native family bounds (26), with `t=1`, `mu=1/4`, one event,
`r=256`, and `w=10^6`, give a joint-channel upper bound `1.474e-6` and an
energy-drift upper bound `3.411e-5`. This is a deliberately loose, finite,
nonvacuous analytical prescription, fixed without optimizing numerical
outcomes. No giant patch or autonomous device was simulated. Its large
coherence width and patch/cap costs are resources, not predictions.
For example the preceding coarse cap prescription uses offset
`5,445,333,234`, initial mean `5,445,833,234` and cap `10,891,666,468` in
these `t=1` units. This poor constant bound demonstrates existence, not
practical resource efficiency or the smallest safe cap.

Additional controls check the two integrations in the LR estimates on a
five-site spin chain, exact small cubic ball counts, the sine Fourier tail
with independently bounded omitted integration tails, and the cumulative
Fourier translation under laboratory-free dwells. Numerical quadrature error
estimates are diagnostic estimates, not interval-certified proof bounds; the
analytic proof supplies the tail and general theorem.

An independent check exposed a time-direction error in the initial (6).
For `h=X_0`, `H'_P=-Z_0 X_1+2Y_1-Z_0 Z_1`, `H_ext=3Z_1 X_2`, and
`Q_z=(I+zZ_0)/2` on a three-site chain with `P={0,1}`, all termwise Record
and buffer conditions hold. At `tau=.4`, the cocycle error is approximately
`0.137722`, exceeding the positive-time-only integral `0.056126`.
The corrected maximum over both time directions in (6)-(7) bounds it.
The runner preserves this counterexample and tests the corrected estimate;
no time-reversal symmetry is now implicitly assumed.

The author runner and proof are not an independent review. Machine outputs,
source hashes, actual mutation failures and execution limits are recorded in
[the scoped packet](../.claude/science/physics-loops/toe-campaign-20260907/matter/WORKLOG.md).
The corrected execution has `TOTAL: PASS=20 FAIL=0`. Four actual
computation mutations are rejected: dropping crossing work, reversing
battery-energy shifts, resetting the shared battery kernel, and halving the
Fourier density. The first and last affect their own single check families;
the reset mutation also fails the independent energy-coordinate comparison.
No full repository pipeline or formal audit is part of this exploratory block.
The coordinator must obtain a focused independent check of (8), (13),
(19)-(25), the cap distinction and native locality before substantial reuse.

The novelty check used the frozen 254-PR inventory, all bodies/discussions and
277 changed science notes. Relevant sources were read rather than inferred
from titles. #8001's separate head/fuel GKSL planning proposal already removes
a supplied event schedule in its own conditional model but explicitly keeps
globally spectral jumps; it does not prove this approximation. No new
framework premise, empirical target, formation law or audit status is supplied
by the present theorem.
