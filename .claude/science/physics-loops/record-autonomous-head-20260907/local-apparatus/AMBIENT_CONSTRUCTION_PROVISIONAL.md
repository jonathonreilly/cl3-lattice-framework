# Independent ambient native-generator construction review

Read the native parent's physical A/B/T and cycle definitions, native Q instrument,
code update, and whole-hopping support/number identities. This is an independent
operator argument, not a numerical implementation review. No source edits.

## Verdict and exact scope

YES: global projectors onto complete chronological histories are unnecessary for
these two supplied Markov laws. There is an explicit common physical ambient
Hamiltonian and local bare seed, and an explicit CPTP erasure channel intertwines
the history-labelled and ambient GKSL generators on their legal sectors. This
preserves the initial definite-sector unraveling, including every classical
edge/sign/time record and each path-conditioned physical observable.

NO: erasing history does not preserve every observable of the history register
as a physical system observable. Order must remain available in the environmental
trajectory record if it is to be read later. Nor does the construction make the
exact spectrally lifted jump spatially local. It supplies the missing ambient
local-Hamiltonian setting for a Lieb-Robinson truncation argument, with the
Fourier-time range and battery-tail problem still explicit.

## 1. Concrete ambient operators

Use the native edge-qubit space, one fuel qubit at each edge, and one head qubit
at each vertex. Write q_e=|1><1| for live fuel and f_e=|0><1| for fuel lowering.
For head qubits use d_v=|0><1| and M_vw=d_w^dagger d_v. Restrict initial head
preparation to one excitation. This subspace is invariant under all these head
moves; no global one-hot projector is needed in the dynamics. Head qubits are
not fermions and introduce no Jordan-Wigner or fermionic exchange sign.

On the ENTIRE tensor product define

    H = sum_e q_e (h_e + Delta I),     h_e=a_e T_e.

The head Hamiltonian is zero. Every term includes the WHOLE native hopping,
not a selected Pauli summand. Fuels commute with native matter, so the parent's
[N,h_e]=0 implies [N,H]=0 also for quantum superpositions of fuel masks.
Moreover [H,q_e]=0. For Delta>=t, each q_e(Delta+h_e) is positive and bounded
by Delta+t, giving 0<=H<=L(Delta+t) on the full ambient space, not only its code.

For the original Record-only law define the directed-edge/sign seed

    B_vw,z = M_vw f_e Q_e,z q_e,       Q_e,z=(I+z Z_e)/2.

For occupation-following feedback use

    J_vw = T_e n_v(1-n_w),     n_v=(I-B_v)/2,
    B_vw,z = M_vw f_e Q_e,z J_vw q_e.

The native identities imply J_vw=c_w^dagger c_v on each faithful source CAR
code and, already as an ambient identity,

    J_vw^dagger J_vw = n_v(1-n_w),     [N,J_vw]=0.

Indeed T_e swaps the two single-occupation projectors and
T_e^2=(I-B_v B_w)/2. This gives an explicit native realization of J without
importing an extra globally defined odd CAR operator or dividing by a possibly
zero hopping coefficient a_e.

The product order is essential: Q_e,z acts AFTER J_vw. Since Z_e anticommutes
with J_vw, reversing their order swaps the newly written sign:
J_vw Q_e,z=Q_e,-z J_vw. At a bridge this changes the parity-conditioned branch;
it cannot be dismissed as a harmless fair-sign convention. No extra1/sqrt(2)
is included: native Q itself gives fair nonbridge branches and the complete
state-dependent bridge instrument.

On the one-head sector, summing signs gives respectively

    sum_z B_vw,z^dagger B_vw,z = n_v^head q_e,
    sum_z B_vw,z^dagger B_vw,z = n_v^head q_e n_v(1-n_w).

Thus legality of the bare transition uses only the incident fuel and head,
plus the specified local native occupation filter. It does not inspect history.

## 2. Code invariance, including the anticommutator issue

Let alpha=(live mask R, head v, old signs z_Rc). Its native code P_alpha is
exactly the parent's projector: old Z values and the cycle checks of the live
graph. It depends on this present data, not on the order that produced it.
In the fixed fuel block the ambient H restricts to H_R+|R|Delta. The parent's
cycle operators commute with every native A/B and hence every h_f and J_e.
For old recorded r, all live h_f and J_e have X/Y support only on their own
live edges and commute with Z_r. Consequently H and J_e preserve the source
code. Q_e,z maps that code into the correct new code, including bridges.

An important point: an INDIVIDUAL Q_e,z^dagger Q_e,z need not preserve the
old code. It would be wrong to infer full GKSL code invariance only from
forward branch invariance. What is required is invariance of the SIGN-SUMMED
loss operator. For the unlifted seeds this follows from the two identities
above: the sign sum removes Q, and J^dagger J belongs to the source algebra.

The same holds after the global lift and a common battery cap. Write H_in and
H_out for the ambient matter/fuel operators in the source/target fuel blocks.
Both commute with P_alpha; so does J (or J=I). H_out also commutes with Z_e,
because its q_e=0 removes precisely that hopping. In the capped pullback
sum_z S_z^dagger S_z, the sum has the form

    sum_(a,a',b) Pi_in(a) J^dagger Pi_out(b) J Pi_in(a')
                         tensor [capped translated-battery product],

with head/fuel eligibility factors. The Q projectors disappeared because
sum_z Q_z Pi_out(b) Q_z=Pi_out(b). Every native factor in this expression
commutes with P_alpha. Thus the sign-summed loss operator preserves each
source code, even when an individual pullback does not. It also preserves
old signs, fuel mask and source head. This closes the nontrivial no-jump part
of the invariant-code argument; it is not merely an on-jump assertion.

Old Record preservation can also be stated ambiently: once q_r=0,
[(1-q_r)Z_r,H]=0, and jumps at other live edges commute with that old guarded
Record. The jump at r has zero eligibility once its fuel is spent. The new
Record has the announced z because Q acts last and the target Hamiltonian
commutes with it. Total native N and the one-head number are preserved.

## 3. Global energy lift and cap

Using the single ambient H, define the full-line battery lift of each bare B:

    V = sum_(a,b) Pi_H(b) B Pi_H(a) tensor T_(a-b).

Since H is block diagonal in all fuels and has zero head energy, V has exactly
the same source/target fuel-mask and head routing as B. The lift does not
create transitions between unrelated masks. Spectral restriction to a legal
code gives precisely the old sector-wise lift. It commutes with modeled total
energy and is bounded, as is clear from Fourier fibers
exp(-i tau H) B exp(i tau H). Caps commute with total energy.

For feedback, set L=sqrt(gamma) Pcap V Pcap and use the ordinary GKSL loss term.
No identity refusal is required for trace preservation, and adding one would
change the law. On the invariant safe domain this is the supplied full-line
feedback generator. Off that domain cap compression changes the rates; it
matches a history model using the same compressed seeds, not a claim that
unsafe cap crossings are somehow still implemented.

For the Record-only law, if exact matching includes its absorbing refusal,
use ONE complement per directed edge of

    F_vw = [E_vw - sum_z S_vw,z^dagger S_vw,z]^(1/2),
    E_vw = n_v^head q_e tensor I_capped-battery,

on the one-head sector. The full-line sign column has squared norm E_vw,
because E_vw commutes with H. Hence the bracket is positive. This is NOT the
identity on ineligible sectors. Embed F into one additional absorbing flag
copy with the same H, and guard successful/refusal jumps by the active flag.
No per-history refusal memory is needed. The sign-sum argument above makes
F preserve every legal source code, so it agrees with the old sector
complements. The absorbing flag and reservoir remain apparatus premises.

The cap makes the total Hamiltonian bounded. Finite graph, finitely many
oriented edge/sign seeds and bounded complements then give a bounded GKSL
construction. Every jump intertwines total energy, including the matched
refusal, so every bounded Borel function of total energy is conserved.

## 4. Explicit CPTP intertwiner

Take the old history Hilbert space to be the direct sum over s of copies of
its actual native code (with the same battery). Let W_s embed that code into
the common native edge space with its physical fuel mask, head, old signs,
and active/refused flag. Distinct orders reaching the same alpha may have
identical overlapping embeddings W_s; that is allowed.

Define Kraus operators E_s=W_s P_s^hist and the erasure channel

    C(rho)=sum_s W_s rho_ss W_s^dagger.

Each W_s is an isometry on its source copy, so sum_s E_s^dagger E_s=I_hist.
Thus C is explicitly CPTP. It removes cross-history coherences; starting from
the declared definite sector, the old separately labelled GKSL jumps never
create those coherences anyway.

For each history transition s->t of label (v,w,z), native operator restriction
and the common H give

    W_t L_s,vw,z = L_vw,z W_s.

For the summed loss, the code-invariance argument in section2 gives
D_ambient W_s=W_s D_s, where D=sum L^dagger L. Likewise H W_s=W_s H_s.
Summing the jump terms and using these loss/free identities proves

    C o L_history = L_ambient o C.

It also proves intertwining separately for the no-jump semigroup and each
edge/sign jump instrument (sum old source-history labels for the same edge/sign).
Therefore every timed jump-record probability and the corresponding normalized
physical conditional state agree. Keeping the edge/sign/time labels in the
standard environmental unraveling gives the same classical-quantum trajectory
instrument; different past orders remain separate classical alternatives there.

No coherent interference is added when two histories reach one physical sector:
C sums their density matrices. Future ambient jumps act linearly on that sum
and depend only on the present physical state. An amplitude sum over such
histories would be a different, unjustified construction.

Canonical physical embeddings also settle dictionary holonomy. The code is
fixed by present mask/sign data, and the bare operators are fixed physical
Paulis/products. Different dictionary phase choices merely change W_s and the
corresponding matrix representation consistently. Noncommuting feedback
products can produce different physical states for different orders; C retains
both states in the mixture. They are not replaced by a common state based only
on mask. For Record-only zero-dwell products, the actual Q operators commute,
so there is no additional untracked operator holonomy to postulate.

## 5. Precise counterexample to "all observables" after erasure

On cube square0-1-3-2-0, the two four-edge orders [0,3,5,1] and [1,5,3,0]
return the head to0 and spend the same fuels. Fix the same four Record signs.
For the Record-only law their zero-dwell physical Q products coincide; with
the same accumulated time, the retained lift and final free evolution also
coincide. These histories nevertheless occupy distinct old history-register
sectors. The old observable "the order was [0,3,5,1]" distinguishes them;
no final physical-system observable can do so for identical physical states.

Thus C is not reversible and cannot preserve arbitrary history-register
observables as system observables. The correct equivalence is all physical
observables and the full ENVIRONMENTALLY RECORDED unraveling. It removes the
need for a separate degenerate chronological register in the system generator;
it does not remove the supplied reservoir's record/entropy obligations or the
fuel/head/Record storage already present.

## 6. Ambient locality and what LR now does and does not establish

With fuels placed at their edge sites and head qubits at vertices, q_e h_e
has the parent's whole-hopping endpoint-star support plus its colocated fuel.
J_e, Q_e,z, fuel lowering and M_vw likewise have uniformly bounded support.
For a bounded-degree graph family these supports have bounded diameter/cardinality,
and the term norms are bounded by t and Delta. In the midpoint placement the
parent gives radius2/diameter4 for h_e; adding the colocated fuel does not enlarge
that range. The two endpoint head sites are also within a fixed-radius seed ball.

This is a genuine finite-range ambient interaction, without a hidden global
history or code projector multiplying its terms. The usual iterated Duhamel
commutator expansion now consists of chains of overlapping bounded supports.
A chain connecting X to Y needs at least d(X,Y)/D links, where D bounds term
diameter, and bounded degree gives an exponentially bounded number/weight of
such chains. The factorial time denominator therefore yields a uniform bound
of the form C|X||Y| ||O_X|| ||O_Y|| exp(v|tau|-mu d(X,Y)), with C,v depending only
on the range, degree and interaction-strength bounds. Equivalently,
H restricted to terms contained in a neighborhood approximates the conjugated
local seed for a bounded Fourier-time window, with an exponentially small
boundary-distance error. Keeping WHOLE controlled hopping terms also preserves
native N under that truncation.

This argument is available uniformly only for a family with the stated bounded
geometry and strengths, not from an isolated finite-cube calculation alone.
More importantly, the EXACT energy lift uses all Fourier times. A local H and
bare B do not turn its spectral lift into a finite-support operator, nor do they
by themselves give a uniformly small operator-norm truncation for arbitrary
battery states. A tau cutoff and a justified state/battery Fourier-tail bound,
or another explicit approximation norm and domain, remain necessary. Cap
compression and refusal can be nonlocal too.

Accordingly: global chronological projectors can be removed exactly; a usable
ambient LR premise can be proved from the native controlled-hopping algebra;
a spatially local bath implementation, one-site/covariant admissibility,
physical preparation, entropy accounting and renewal are still unproved.
