---
claim_id: when_the_odds_are_an_energy_rank_one_detailed_balance_tests
claim_type: bounded_theorem
claim_scope: "Finite supplied classical pattern chains on the L=8 cubic torus; exact attained proposal census and rational rectangular extensions, bounded cycle and stationary diagnostics, dimensionless break-channel formulas. Rectangular ranks are not observed partial-table ranks and do not derive physical energy or temperature."
upstream_dependencies: []
runner: scripts/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.py
---

# Attainable proposal odds, rectangular factorization and finite reversibility checks

**Type:** bounded_theorem

Original date: 2026-09-03. Correction: 2026-09-09.
**Author status:** conditional finite support; no audit grade.
**Audit:** formal audit deferred by the owner.
[Primary runner](../scripts/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.py) · [current cache](../logs/runner-cache/when_the_odds_are_an_energy_rank_one_detailed_balance_check_2026_09_03.txt)

```yaml
actual_current_surface_status: conditional-support
trace_class: frontier_discovery
artifact_role: theorem
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Supplied model

The L=8 periodic cubic graph has 512 sites and six ordered neighbours
(+x,-x,+y,-y,+z,-z). A configuration S has n<=3 occupied sites, one particle
per site. A(S) counts adjacent pairs; B(S)=(n-1)-A(S) is the supplied cost
coordinate. A proposal chooses a particle with probability 1/n and a direction.
Blocked targets give a null step; otherwise acceptance is min(1,exp(-w)).
The source has m_s other neighbours and the target m_t, giving
D=B(new)-B(old)=m_s-m_t. The direction sign s is +1/-1 for ±x and 0 otherwise;
a is the source parity. Constants g0=1, mu=1/2, nu=1/4 are supplied.

| Table | w | Direction proposal |
| --- | --- | --- |
| A | (1+mu m_t)(1+nu a)D | 1/6 |
| B | gD | exp(h[d=+x])/(5+exp(h)) |
| C | gD+kappa D²1[m_t>=1]+hs | 1/6 |
| C′ | gD+kappa D²1[m_s>=2]+hs | 1/6 |

These are classical shifting-pattern models. Permanent physical Records do
not thereby move or change value. No formation clause, physical Hamiltonian,
clock, energy unit or temperature calibration is supplied. The prior PR 7899
formulas are rederived as table B mathematics below, not imported authority.

## A/T1: actual proposal support and a declared rectangular extension

The dimer census contains 18 occurring (m_t,s,a,D) tuples over 12240 proposals.
The trimer census contains 36 over 4672620 proposals, enumerating 130305
translation representatives {0,x,y}, both parities, all movers and directions.
For a cubic nearest-neighbour hop the source and target other-neighbour sets
are disjoint. With two other particles m_s+m_t<=2; D=m_s-m_t.
The runner checks that the enumerated domain has precisely the six possible
(m_s,m_t) pairs with this bound, crossed with three s and two a values.

At g=1,h=0,kappa=1/2, **B and C have identical acceptance at every attainable
trimer proposal**. If D>0 then m_t=0; if D<0 the C cost remains nonpositive;
D=0 gives zero cost. The exact actual-tuple control checks this directly.
Thus no B/C rebinding signature exists in this experiment at those parameters.

`odds_matrix` separately projects condition coordinates and D values and
fills their Cartesian product. It intentionally remains a **supplied extension**:
18 conditions times 5 D values=90 cells, only 36 of which occur. Its gauge is
M_rel(c,D)=max(0,w(c,D))-max(0,w(c,0)). A D=0 baseline is not necessarily
observed at fixed c. The full condition including both m_s and m_t already
fixes D. No missing cell is imputed as measured history.
For example m_t=1,D=2 implies m_s=3 and is unavailable; its B/C costs 2/4
supply part of the extended rank separation. The runner checks its absence.

On these rectangles, exact Fraction elimination retains the original ranks:
A and B have rank 1 for both group rectangles at h=0,1; C has dimer rank 1
and trimer rank 2 at h=0, rank 4 at h=1. C′ has trimer rank 2 at kappa=1/2,1
and rank 4 at h=1. The respective second/first singular ratios are
C: .03411710 (residual .03409726), .1426295 at h=1;
C′: .05018675, .1304845, .2224582 at h=1.
The exact reciprocal factor ladder for A is 2/5,1/2,8/15,2/3,4/5,1;
B has reciprocal factor 1/g. All nine factorizations found use the gauge
E(+1)=1 and give E(D)=max(0,D). The dimer C rectangle has reciprocal factors
2/3,1. Adding its raw proposal log cost produces singular ratio .04032337.
These are algebraic factors, not identified physical energies or temperatures.
The transformation E->cE, beta->beta/c leaves their product unchanged.
Dimer insufficiency here concerns this tested C rectangle and parameter point,
not every dimer law. The chosen gauge is a convention, not a universal remedy.

## B/T2: actual graphs, cycles and stationary distributions

The supplied dimer relative chain has 511 states r=v-u and applies only when
the table is translation covariant; A is not. The parity-resolved chain has
1022 states (p,r) and aggregates transition rates after quotient by even
translations. Results concern these actual chains; no blanket correspondence
between all quotient and absolute cycles is assumed. The runner enumerates
56454 distinct four-cycles there,1524 in the relative chain, and 504 listed
length 8 +x winding paths. The trimer calculation covers 1620 four-cycles
based at the bent trimer {(0,0,0),(1,0,0),(1,1,0)} or its one-step successors.

At g=1,kappa=1/2: A has maximum log cycle defect .25 in the tested dimer
and trimer cycles, zero on the winding paths within numerical tolerance;
its stationary vector differs from normalized exp(-gB) by relative maximum
.1199957. B at h=0 has negligible tested defects and agrees with that vector.
B at h=1 still agrees with exp(-gB) in the tested dimer chain, while its
four-cycle and winding defects are 4 and 8. The relative and restricted trimer
cycle tests miss those defects. C at h=0 agrees with B on the attained domain;
its agreement is **not** a general cancellation of a symmetric barrier.
The target-keyed kappa term is not generally invariant under reversal.
C′ has maximum defect 4kappa on the declared trimer cycles at kappa 0,1/4,1/2,1
and g=1, with the g=2,kappa=1/2 comparison also giving 2.
These defects and stationary solves are floating evaluations with printed
thresholds; rational rank and combinatorial count statements are exact.

Kolmogorov's criterion establishes reversibility when *all* graph cycles
satisfy it (with positive reverse rates). A failed cycle disproves reversibility;
a clean bounded census alone is not a generating-cycle proof. For table B at
h=0, symmetric proposals and the Metropolis ratio directly give detailed
balance for exp(-gB), independently of the rectangular activation rank.
A positive stationary pi can always be written exp(-E)/Z with E=-log(pi),
without implying reversibility, locality or physical thermodynamics. A's
failure to match the particular exp(-gB) vector does not exclude every such
representation. Parity dependence alone also does not exclude reversibility:
two parity states with rates 1/3 and 2/3 and weights 2/3 and 1/3 have equal flux 2/9.
The exact rational control retains this counterexample.

## C/T3 and D/T4: dimensionless channel and lifetime identities

The bent trimer has 18 proposals:4 blocked,2 at D=0,8 at D=1 and 4 at D=2.
Define a(D)=-log(mean acceptance in channel D). B gives a(D)/D=g at g=1,2,4.
For C′ the end breaks have (m_s,m_t)=(1,0) and the central breaks(2,0), so

    a(1)=g,  a(2)=2g+4kappa,  a(2)/2-a(1)=2kappa.
    tau=18/(8 exp(-g)+4 exp(-2g-4kappa)).

At kappa=1/2 the lifetimes at g=1,2,4 are 5.967579958344,
16.474505674194,122.693773845084. The B values are 5.165916817967,
15.571677528219,121.731046628774. The tested C′ cycle defect equals twice
the channel gap on the stated parameter grid. Its rectangular rank residual
is a separate off-support algebraic diagnostic. C's breaking channels equal
B for any kappa because all 12 targets have m_t=0; this does not locate a
rebinding signature. The runner retains kappa 0,1/2,1 for that break check.
These formulas measure supplied-model step counts and log costs. An Arrhenius
or van't Hoff temperature interpretation requires a separate identification.

For table B's dimer, the aligned and transverse first-break lifetimes are
2 exp(g)(5+exp(h))/(9+exp(h)) and exp(g)(5+exp(h))/(4+exp(h)).
Both become(6/5)exp(g) at h=0. The stationary intact fraction in the tested
relative chain is 6/(6+505 exp(-g)). The runner checks g=1,2,4 and h=0,1;
the supplied relative-rate symmetry explains the stationary expression.
No arbitrary-h numerical sweep is claimed. Table B's bent-trimer expression
is 18/(8 exp(-g)+4 exp(-2g)), checked at g=1,2,4.

## Inputs and scope

All scientific definitions and functions are inline. The only runtime file
input is this exact note, declared and hash-verified by the runner. Current
caches are actual source/input-bound executions; historical numerical cache
residuals are not copied as fresh measurements. All 21 original predicates
remain, with truthful labels, plus the two decisive domain/parity controls.
The full trimer graph, other cycle lengths, larger groups, other acceptance
rules, local thermodynamic representations and physical formation remain open.
[Original six-body recovery and finding dispositions](../archive/backlog/readout-7901-7969/HISTORY.md).
