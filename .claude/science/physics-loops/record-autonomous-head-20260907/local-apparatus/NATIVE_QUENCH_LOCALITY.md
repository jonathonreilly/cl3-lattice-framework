# Native-CAR local-quench locality: independent review

The root's proposed factorial-tail estimate is valid for the complete RECORD
column on the declared legal source-code domain. It is substantially sharper
than the generic ambient LR constants. The feedback column requires an extra
term: its annihilation/creation factor does not intertwine the surviving
Hamiltonian. Neither result is an unrestricted ambient-operator-norm theorem.
The generic ambient LR memo remains independently valid and is not replaced.

## Exact echo factorization and its orientation

Fix an eligible source fuel mask and one directed live edge e=(v,w). Let

    H0=Hrem+h_e,       Hrem=sum_(other live f) h_f,

suppressing scalar source fuel energy. The same physical Hrem acts on the
source native code and the new Record code. The native physical Q projectors
commute with every surviving hopping, so for the complete two-sign column K,

    Hout K = K Hrem,       K^dagger K=I_source.

This holds for bridges as well as nonbridges. The bridge maps are their actual
parity projectors, without an extra fair-sign factor. Including fuel exactly
once yields

    Y(tau)=exp(i Delta tau) K E(tau),
    E(tau)=exp(-i Hrem tau) exp(i(Hrem+h_e)tau).

Its derivative is

    E'(tau)=i h_e^-(tau) E(tau),
    h_e^-(s)=exp(-i Hrem s) h_e exp(i Hrem s).

Thus the generator uses NEGATIVE ordinary Heisenberg time. Calling it h_e(s)
is fine only with that convention stated. All estimates below depend on |s|,
so reversing the convention consistently does not change their magnitude.

Retain whole physical hopping terms near e, always keeping h_e itself. Write
Hrem,R for this surviving subset and H0,R=Hrem,R+h_e. The same K intertwines
the two truncated sides. Therefore Y_R=exp(i Delta tau)K E_R with the analogous
E_R. Both echoes preserve the legal source code and are unitary there, giving

    ||Y-Y_R|| = ||E-E_R||
       <= integral_0^|tau| ||h_e^-(s)-h_e,R^-(s)|| ds.

For an individual branch only the inequality is needed; the norm equality uses
the complete isometric column. Truncation means omitting couplings, not spending
additional fuels or imposing extra Record constraints.

## One-particle propagation and the exact definition of m

On the source code use the parent's faithful even CAR identification. Then
Hrem=dGamma(h), with h a real signed weighted adjacency matrix of maximum
vertex valence d<=6 and weights bounded by t. The operator bound

    ||h||<=d t,       ||h_R||<=d t

follows from row/column sums and does not contain particle number or volume.
The second-quantized Hamiltonian norm may be extensive; it is NEVER substituted
into the Taylor estimate.

Let O be the set of nonzero hopping edges omitted from h_R. In the full surviving
one-particle graph define

    r = min distance_graph(x,y),
        x in {v,w}, y an endpoint of an edge in O,
    m = r+1.

If no omitted edge is reachable, set m=infinity and the error is zero. The +1
is essential: reaching an endpoint is not yet traversing its omitted hopping.
A length-n walk contributing to h^n|v> or h^n|w> cannot use an omitted hopping
for n<m. Hence those powers agree exactly with h_R^n on both seed vectors.
Cancellations can delay the first nonzero difference, but cannot worsen this
bound. Distances in the full cubic graph may be used instead if a conservative
mask-independent lower bound is wanted.

Define T_m(x)=sum_(n>=m) x^n/n!. Taylor expansion, exact low-order agreement and
the one-particle norm bounds give

    epsilon_v(s)=||(exp(-ihs)-exp(-ih_R s))|v>|| <=2 T_m(dt|s|),
    epsilon_w(s) <=2 T_m(dt|s|).

No rational gap multiplier or large many-body matrix norm enters this proof.

## CAR bilinear estimate and the proposed constant

Write psi_x(s)=exp(-ihs)|x>, with analogous truncated vectors. All have norm1.
The exact quadratic expression is

    h_e^-(s)=a_e[c^dagger(psi_v)c(psi_w)
                       +c^dagger(psi_w)c(psi_v)].

For normalized u,v,u_R,v_R, telescoping a bilinear and using the CAR norm bound
||c(f)||=||f|| gives

    ||c^dagger(u)c(v)-c^dagger(u_R)c(v_R)||
       <= ||u-u_R||+||v-v_R||.

Consequently

    ||h_e^-(s)-h_e,R^-(s)|| <=8t T_m(dt|s|).

Integrating termwise proves precisely the proposed safe bound, for d,t>0:

    delta_R(tau) <= min{2, (8/d) T_(m+1)(dt|tau|)}.       (Q1)

The trivial t=0 case has zero error. The bound starts at order m+1 because the
two echoes have the same initial perturbation h_e. There is no factor N and no
large convolution or geometric LR constant.

This uses odd c(f) only as a norm-estimation device in the faithful Fock
representation. It does NOT assert that odd c_v is a local physical edge-qubit
operator. Restricting an even operator's full-Fock norm to a fixed-N or fixed
component-parity sector cannot increase it. The source connected component
containing e supplies that faithful even representation. At a bridge Hrem
splits it, but remains a quadratic operator on the original source component;
the source code and total/component-source parity remain valid throughout the
virtual echo. K then performs the actual branch projection. Thus neither
bridges nor degeneracies invalidate (Q1).

## Physical whole-hopping geometry

Use the doubled coordinates and ambient l1 metric of ambient-lr-constants.md.
Every native whole-hopping support D_f fits within radius2 of midpoint(f).
Take S to contain D_e and the two endpoint head sites (at most13 sites), even
if a smaller actual Record-only seed would suffice. Let the physical truncated
Hamiltonian retain whole terms D_f contained in B_R(S).

For an n-step graph walk starting at v or w, its first edge midpoint is in D_e
and hence in S. The midpoint of its kth edge is at ambient distance at most
2(k-1) from that first midpoint. Every point of its whole support D_f is thus
at distance at most2k from S. All walk hoppings through order n are retained
whenever2n<=R. A uniform conservative choice is therefore

    m >= floor(R/2)+1.                                  (Q2)

This is for integer R and the distance-to-S ball, not a ball centered only at
midpoint(e). If S contains only the two endpoint vertices, the weaker guaranteed
choice is m>=floor((R+1)/2). If the neighborhood is a radius-R ball centered at
midpoint(e), a safe choice is m>=floor(R/2) for R>=2. These conventions must not
be interchanged. The direct graph definition of m is preferable whenever the
actual omitted edge set is known.

The physical truncated Hamiltonian remains a sum of the same native whole h_f,
so its restriction to the original legal code is exactly dGamma(h_R). Each
retained term preserves the original source code and N. No inferred locality
of an abstract70-dimensional matrix or a Jordan-Wigner string is used.

## Essential modification for occupation feedback

For feedback the branch is K J, where J=c_w^dagger c_v on the source code.
In general [J,Hrem] is not zero, and KJ is a contraction column with effect
J^dagger J rather than a complete isometric column. Its factorization is

    Y_fb(tau)=exp(iDelta tau) K J^-(tau) E(tau),
    J^-(tau)=exp(-iHrem tau)J exp(iHrem tau).

It is NOT exp(iDelta tau)(KJ)E(tau). Applying the same one-particle estimate
to this single bilinear gives

    ||J^-(tau)-J_R^-(tau)|| <=4 T_m(dt|tau|).

Since ||J||,||K||<=1, a valid feedback replacement is

    delta_R,fb(tau)
       <= min{2, 4 T_m(dt|tau|)+(8/d)T_(m+1)(dt|tau|)}.   (Q3)

The extra term generally starts one Taylor order earlier and must be retained.
The resulting fixed-edge maps are CP and trace nonincreasing. This does not
prove identical hazards or a bound for the entire feedback GKSL semigroup.
It does provide a valid local fiber estimate for a separately controlled
single-event comparison, with all rate/conditioning limitations stated.

## Controlled-fuel direct sums, erasure and channel norms

The ambient controlled H is block diagonal in fuel masks. For a fixed eligible
directed edge, each source mask maps to a unique target mask with that edge
spent; distinct masks and old sign sectors remain orthogonal. Each block obeys
the same d<=6 estimate and the same geometric lower bound for m. Operator norm
on their legal direct sum is therefore bounded by the supremum of the block
bounds. This includes arbitrary reference systems and legal-mask coherences;
it does not introduce global history projectors into the physical Hamiltonian.

The explicit CPTP erasure of chronological copies established in the ambient
review transfers the bound to its physical range. It does not identify arbitrary
different physical path-conditioned states and does not recover chronological
observables from the final system. The uniform estimate is restricted to the
legal code/eligibility input domain. Arbitrary ambient edge-qubit states may
lie in different cycle representations, so the native-CAR argument is not a
proof of the same unrestricted ambient operator norm. The generic LR memo
provides that separate ambient route.

For the fixed initial product sine battery, substitute (Q1) or (Q3) into the
localized-lift derivation's delta_R integrals. The record-only local column is
still exactly complete on the legal input; the feedback column is not completed
to an identity-rate law. The matter-plus-Record bound is2 integral p_w delta_R;
the retained-battery bound is2 sqrt(integral p_w delta_R^2). They remain legal-
domain fixed-battery channel norms, not unrestricted matter-battery diamond norms
and not normalized rare-branch bounds.

For an explicit nonoptimized cutoff, take T=m/(2e d t), m>=1. Using
T_n(x)<=x^n/[n!(1-x/(n+1))] and n!>=(n/e)^n gives

    T_m(dtT) <=2^(-m)/(1-1/(2e)),
    T_(m+1)(dtT) <=2^(-(m+1))/(1-1/(2e)).

Thus the short-Fourier-time error decays exponentially in m. When wT>=sqrt(2)pi,
the already derived sine tail is at most32pi/[3(wT)^3]. This turns the short-time
factorial estimate into an explicit radius/battery-width approximation without
the enormous generic LR velocity. It is a proof parameter choice, not tuning
of the frozen physical gamma, packet or trajectories. No favorable small-radius
numerical claim is made.

As before, the truncated lift conserves its truncated total energy rather than
necessarily the full original energy, its original cap support is not automatic,
and applying a fresh product-battery estimate after a correlated retained-battery
event is invalid. Local physical apparatus, entropy, renewal and covariant
one-site admissibility remain supplied or unresolved. The improvement is a
sharper, correctly scoped local-quench approximation theorem.
