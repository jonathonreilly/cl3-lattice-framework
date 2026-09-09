# Finite affine supports and conditional response identities — Cycle 895

Date: 2026-09-09; original note dated 2026-08-04.
Type: bounded_theorem
Authority: none
Audit: unset

This corrects original #5957. The exact finite affine classification survives.
It does not select a physical grading, retire every grading consumer, or close
a research backlog. The state space, source occupancy, grading and response
maps below are supplied mathematical definitions. They are not derived from
the [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

Primary runner: [finite affine runner](../scripts/frontier_cycle895_t_retirement_2026_07_28.py).
Companion: [independent coordinate check](../scripts/frontier_cycle895_t_retirement_independent_check_2026_07_28.py).
The [model](../scripts/affine_5957_model.py) contains the actual finite definitions.
Original bodies, earlier versions, historical inputs and corrections are in
[history](../.claude/science/physics-loops/affine-5957-correction-20260909/HISTORY.md).

## Exact finite domain and affine classification

Let D={+e1,-e1,+e2,-e2,+e3,-e3}. Choose an incoming direction d and three
sector directions m,f,a independently in D, giving 6^4=1,296 labelled supports.
The gauge-fixed grading is w(t)=(1,1+t,1-t), t rational. No positivity condition
on grading components is imposed; the parameter space is a line, not a bounded
segment. Real t gives the same support classification, since every possible
isolated root of the integer affine equations is rational.

The balance residual and unweighted raw sector ledger are

    R(t)=m+(1+t)f+(1-t)a-d=A+tB,
    A=m+f+a-d,  B=f-a,  S=(m-d,f,a).

The sector trace of S is A. For A=B=0 a support is lawful for every t. If
B is nonzero, each nonzero component requires t=-A_i/B_i; these ratios must
agree, and every zero B_i must have A_i=0. Otherwise the support is never
lawful. This finite ratio test exhausts the stated domain without a parameter
grid or approximation. The independent checker solves the original ledger
in the coordinate s=1+t, using m+s f+(2-s)a=d and a separate enumeration.

| Support class | Count | Lawful parameters |
| --- | ---: | --- |
| A=B=0 | 6 | Every t |
| A=0, B nonzero | 84 | t=0 |
| A nonzero, common affine root | 30 | t=-1 |
| A nonzero, common affine root | 30 | t=+1 |
| Inconsistent affine equations | 1,146 | None |

The six always-lawful supports have m=-d and f=a=d. Indeed B=0 gives f=a;
then m+2f=d. Both m and d have unit length, so 1=|m+2f|^2=5+4 m·f forces
m=-f and hence d=f. Conversely these six supports have A=B=0.

At t=0 there are 90 traceless lawful supports. For each fixed d, triples
summing to d consist of three permutations of (d,d,-d) and twelve permutations
of (d,e,-e), where e lies on either of the other two axes. This gives 15 per d.
At any nonzero t, traceless lawfulness requires A=0 and tB=0 and therefore
reduces to the six always-lawful supports. Total lawful counts are 90 at zero,
36 at each of ±1 and six elsewhere. These counts and all individual support
members are emitted by the bounded runner.

## Conditional endpoint response and blind fibre

Use two distinguished endpoints. At each occupied endpoint seat exactly one
source: a lawful support S multiplied by a nonzero weight k in {1,...,6}.
Allow either one occupied endpoint or both occupied endpoints. The zero-source
member is excluded. Different source labels are counted as different members;
this is not a count of independently established physical states.

For a block X with three sectors and three spatial components, let C(X) be
its sector trace, let P_C X repeat C(X)/3 in all three sectors, and define
G_sigma X=X-P_C X+sigma P_C X. Let R exchange the endpoints. Use the six
specified response constructions:

- O1 flattens R G_sigma X.
- O2 flattens G_sigma R R G_sigma X.
- O3 takes the endpoint-resolved sector trace of R G_sigma X.
- O4 is the sum of squared entries of O1.
- O5 is the per-endpoint spatial Gram tensor of R G_sigma X.
- O6 pairs corresponding sector/spatial entries of the two graded endpoints.

The projection identities give C(G_sigma X)=sigma C(X), and hence
O3[e]=sigma C(X)[reversed e]. If C(X)=0 at both endpoints, G_sigma X=X
for all sigma, and all six objects are sigma-independent. If either endpoint
has nonzero trace, O3 distinguishes sigma=+1 from sigma=-1. Thus simultaneous
blindness of this collection is exactly endpoint-wise tracelessness.

Under the stated one-source-per-endpoint and nonzero-weight conditions,
C(kS)=kA vanishes exactly when A=0. Therefore the blind fibre is the fibre
over the traceless lawful supports. For n such supports its labelled count
is 2(6n)+(6n)^2: 1,368 for n=6, and 292,680 for n=90. At t=±1 the entire
lawful fibre has n=36 and 47,088 members, of which 1,368 are blind. The original
1,368 figure is preserved with this exact occupancy convention.

Overlapping sources at one endpoint can cancel traces; zero weights can hide
trace-bearing supports. Summing the two endpoint channels can also hide
opposite nonzero traces. None of those enlarged domains is covered by the
blind-fibre characterization. Eighteen fresh one/two-endpoint fixtures exercise
all six actual response functions, and a trace-bearing lawful support exercises
O3. The general result follows from the projection and occupancy arguments,
not from the number of fixtures. O1 and O3 are affine in sigma; the other four
objects have degree at most two in these supplied constructions.

## Finite selected rows and the missing completeness premise

For a finite family of affine-zero atoms and a finite support set, suppose a
Boolean predicate depends on t only through those atoms and support membership.
The union E of all atom/support roots is finite. Off E the full vector of
Boolean inputs is constant, so the predicate is constant there. Evaluation
at E and one point outside E is then complete. The factor-through-atoms
hypothesis is essential; agreement at one generic point does not establish it.
For example t>1/2 does not factor through the zero atoms t, t-1, t+1.

The model explicitly defines the original 23 selected Boolean rows on the
supplied finite supports. Their parameter dependence is through lawful support
membership, t=0 or t=1, plus identities such as (1+t)+(1-t)=2. Here E={-1,0,1}
is complete by the finite partition and the written formulas. Fifteen rows
hold identically. The eight sensitive rows have these truth sets:

| Selected proposition | Truth set |
| --- | --- |
| Every lawful support is traceless; unqualified O1/O3 sign blindness; unqualified response blindness | All t except ±1 (three rows) |
| Blind fibre equals the carried family; its count equals 1,368 | All t except zero (two rows) |
| Lawful support count equals 90 | {0} |
| Auxiliary-absent coefficient-two support is lawful; its (-2,1,0) ledger witness is on shell | {1} (two rows) |

Uniform rows retain the trace/defect identity, the supplied balance line,
the trace-bearing witness, onset and maximizer statements, grading-independent
raw trace, O3 identity and visibility condition, labelled family count and
blindness, carried-family balance, generic support set and O1/O3 degree bound.
Old row identifiers remain for correspondence; words such as “landed” in those
identifiers grant no status. The (1+t) field contribution of an always-lawful
support varies with t even though its total residual is always zero. Thus
lawfulness independent of t does not imply every observable is independent of t.

The original scanner searched 14,190 files with lexical/AST filters and reported
108 consumers. Those are historical heuristic results, not semantic completeness.
An expression such as `a+(1+t)*b+(1-t)*c` can escape the old vocabulary filters.
No moving-main scan is run here. The historical role choices and weaker
“cofinite means no exact choice” retirement policy do not exhaust other
predicates, research routes or physical conditions. The old 19+10+1 category
counts total **30**, not 29; they combine the selected 23 and seven backlog rows.
Neither those counts nor the 15/8 selected table establishes global retirement.

## Operator nonvanishing and numerical thresholds

Suppose the supplied operators satisfy P_field=P_aux and
[V,P_matter+2 P_field]=0 exactly. Then P(t)=P_matter+2 P_field is independent
of t. Deleting the auxiliary contribution leaves

    [V,P_matter+(1+t)P_field]=(t-1)[V,P_field].

If c=||[V,P_field]|| is positive, this is nonzero exactly for t≠1. A threshold
||commutator||>tau instead requires |t-1| c>tau. For several components the
minimum threshold requires |t-1| min_i c_i>tau; if any c_i=0 it cannot pass.
The pinned Cycle325 field and auxiliary value lists have the same defining
values, so the operator identity has relevant provenance. Its historical
measured >0.7 predicate is not replaced by mere nonvanishing.

The exact independent 2×2 control uses V=X, P_field=P_aux=Z and P_matter=-2Z.
Its full commutator is zero. The deleted commutator has squared Frobenius norm
8(t-1)^2: it exceeds 49/100 at t=0, but equals 1/125000 at t=999/1000, nonzero
and below threshold. This counterexample rejects the old all-t-except-one pricing.

For the auxiliary-absent case one can set P_aux=0; absent vocabulary does not
forbid an affine extension. Write E=[V,P_matter], F=[V,P_field]. The residual
is E+(1+t)F. If E=0 exactly and ||F||>0, nonvanishing holds for t≠-1, but the
threshold is |1+t| ||F||>tau. If only ||E||≤epsilon is known, the norm lies
between max(0,|1+t| ||F||-epsilon) and |1+t| ||F||+epsilon. Degeneracy at -1
cannot then be asserted exactly. Floating thresholds do define truth sets
on rational inputs; missing exact suppliers are a proof obligation, not a
reason such a set cannot exist. Original Cycle316 measured evidence stays
historical. Neither old threshold campaign is rerun or declared closed.

The separate R9 linear statement remains conditional: impose both
-2w_m+w_f+w_a=0 and -2w_m+w_f=0, together with w_m=1. Subtraction gives
w_a=0 and substitution gives (w_m,w_f,w_a)=(1,2,0), i.e. t=1. Selecting both
constraints is an additional supplied condition, not a physical grading derivation.

## Evidence and limits

The two current entrypoints have actual source/input guards and genuine caches.
The checker independently enumerates all supports in s coordinates. Its
receipt controls accept a clean selected-23 summary and reject changes to the
actual state, count and classification operands through the same validator.
The count comparison uses the same 23-row scope throughout. The terminal rule
requires a nonempty set of true checks and no refutations; failed, empty and
refuted cases exercise that actual function. The original ineffective T4/T7
and historical 8/8 output remain unchanged in recovery, with no fresh credit.

The 23-row classifications are compared against exact historical receipt data,
which is declared as an input; no claim of unseen holdout independence is made.
Original eight endpoints, two superseded runners and seventeen historical
input identities are recoverable outside note discovery. Historical scans,
1,108-point hunts, restriction campaigns and prior failures remain historical.
They are not replayed as part of this bounded correction. No physical selector,
backlog closure, retained grade, reserved-scope approval or TOE completion follows.
