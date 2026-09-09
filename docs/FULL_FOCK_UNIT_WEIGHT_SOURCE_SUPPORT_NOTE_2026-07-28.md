# Conditional finite Fock number blocks and unit-weight label diagonals

Date: 2026-07-28; corrected 2026-09-09

**Type:** bounded_theorem

**Status:** conditional finite local algebra; physical auxiliary lift open.

**Primary runner:** `scripts/frontier_full_fock_unit_weight_source_2026_07_28.py`

This result concerns an explicitly supplied finite model. The names matter,
mediator and auxiliary label mathematical components below; they do not supply
new framework structure or establish physical carriers. The current
[framework memo](MINIMAL_AXIOMS_2026-06-29.md) selects neither this source operator
nor its angle. No audit status or physical source/gravity law is claimed.

## Supplied model and exact result

Take six ordered directions `(x,-x,y,-y,z,-z)` and their fermionic occupation
space with basis all 64 masks. Write `n(m)=bit_count(m)`. A local source factor
has seven labels: reservoir `q=0`, and `q=1+d` for direction `d`. Thus its local
space has dimension `64*7=448`. The label `q=1+d` is called a matched pair;
it is **one label**, not a tensor product of independently carried mediator
and auxiliary spaces. The local mask ordering is increasing occupation, then
lexicographic occupied directions, exactly the original finite fixture.

For each occupied `d` whose opposite `bar d=d xor 1` is empty, let
`m'=m minus {d} plus {bar d}`, and let `s(m,d)` be the ordinary ordered CAR
annihilation/creation sign. The real symmetric exchange is

`E = sum_(m,d active) s(m,d) (|m',1+d><m,0| + |m,0><m',1+d|)`.

Use `V(theta)=exp(i theta E)` for real theta. The numerical fixture supplies
`theta=0.8 * 3*tan(0.15)`, retaining the historical `beta=-0.3` and coupling
`0.8`; this parameter value is not a derived physical coupling. Put
`p(m)=sum_(d occupied) e_d`. On a reservoir label define the three vector
diagonals `(P_m,P_F,P_A)=(p(m),0,0)`; on `q=1+d` define
`(p(m),e_d,e_d)`. Consequently `P_F=P_A` as operators, and
`P_total=P_m+P_F+P_A` is exactly the original coefficient-two diagonal.
This equality alone does not create an auxiliary transport mechanism.

For every active channel,

`p(m')-p(m)=-2e_d`, `P_F=e_d`, `P_A=e_d`.

Therefore E commutes with each component of P_total and with the local
number diagonal N. Its exponential does too, by the power series. The supplied
Q in this finite model is the identity; its commutation is a tautological
identity-charge statement, not a new global charge-sector construction.
E is Hermitian and real symmetric, so V is unitary and complex symmetric.
Thus `V_ab=V_ba` in this declared basis. This is the reciprocity used here;
it does not assert physical reciprocity for arbitrary source experiments.

## Number sectors, channel counts and probabilities

The number-n local block has dimension `7*C(6,n)`. For a fixed direction,
occupy d, empty its opposite and choose the other n-1 modes from the remaining
four. The active-channel count is `6*C(4,n-1)` (zero for n=0), hence **0,6,24**
for n=0,1,2, with dimensions **7,42,105**. The vacuum block is identity.
These exact algebraic arguments apply to all six-mode masks; the retained
exhaustive two-cell certificate is restricted to local `n<=2`, and no
untruncated spatial Fock-space theorem is asserted.

Each reservoir is the center of a signed star with k active leaves. A leaf
has exactly one center: its direction and target mask determine the source.
The normalized bright vector is `k^(-1/2) sum_j s_j |leaf_j>`; E acts on
center/bright as `sqrt(k) sigma_x` and vanishes on dark vectors. Thus each
active emitted channel has probability

`sin²(sqrt(k)*theta)/k`.

For n=1, k=1 and the fixture gives approximately `0.12589921612871374`.
For n=2 each active center has k=2 and gives approximately
`0.1204261679086943` per channel; opposite-filled masks have k=0. The six
n=1 rows also agree with the original one-carrier 222-dimensional exchange:
`|d> -> cos(theta)|d> + i sin(theta)|bar d,d,d>`.
The matter vector expectation changes by `-2 sin²(theta)e_d`, with equal
mediator and auxiliary expectations `sin²(theta)e_d`. This is an actual local
operator/component comparison, not evidence of a new physical encoding.

## Two-cell and coherent-state scope

The spectator matter space has all 64 masks. Each endpoint action applies V
to its own local mask and active seven source labels while preserving the
spectator. The original joint ordering has 4096 matter pairs. Testing each
endpoint separately on the 22 allowed masks at both cells and seven active
labels gives `2*22*22*7=6776` endpoint-active columns. The corrected check
examines every numerically nonzero matrix entry, without a support tolerance
that could hide a small cross-sector leak. The independent checker additionally
examines **all** matrix entries between unequal number sectors.

These endpoint tests preserve both local occupation numbers; they do not
construct simultaneous independent source factors or a shared physical
auxiliary lift. Linearity and number-block preservation also retain the
specified coherent n=1/n=2 state, with norm and layer weights unchanged and
inverse recovery. The supplied real reservoir/pair superposition has equal
forward/reverse matrix elements because V is symmetric. This particular check
is not an arbitrary complex-state exchange identity.

The adverse control moves one actual n=2 exchange edge into an n=1 target,
preserving its Hermitian reverse edge. The same number-commutation predicate
then rejects it, with Frobenius residual `sqrt(2)`; this diagnoses the wrong
embedding, not a physical obstruction.

## Parent obligation remains open

The historical Cycle322 “Optimal next campaign” asked for a full-Fock
unit-weight **two-source physical lift** preserving AB/BA physical
intertwining, contact, nonzero two-source response, frames, endpoint reversal,
translations, held sizes and deletions. The local diagonal split and separate
endpoint number blocks do not discharge that obligation. Independent carried
auxiliary transport/catch-up, simultaneous-source sectors, the full physical
update and acceptance tests remain open. Higher spatial/truncation claims,
source preparation, calibrated physical response and gravity remain open.
The old coefficient-two controller replay cannot establish those new claims.
Exact parent notes and their boundaries are recoverable through the
[historical inventory](../.claude/science/physics-loops/full-fock-7871-correction-20260909/RECOVERY.json).

The current token note and both Cycle731 runners are untouched, unrelated
inputs. Their historical broad behavioral iff is not restored or accepted.
All original authored versions, outputs and procedural history are preserved
[outside active discovery](../.claude/science/physics-loops/full-fock-7871-correction-20260909/HISTORY.md).
Historical instructions and old Record-additivity language have no current
premise authority.

## Reproduction and evidence

From the repository root, with NumPy and SciPy available:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/frontier_full_fock_unit_weight_source_2026_07_28.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/frontier_full_fock_independent_check_2026_07_28.py
```

Both entrypoints declare a 30-second budget. The author wrapper enforces that
wall limit and a 2 GiB process-group RSS cap with BLAS threads set to one.
The primary retains all seven original local mathematical checks, using a
provenance-bound extraction of the actual finite definitions. The checker is
an explicitly **standalone** independent arithmetic route: occupied-list CAR
signs and analytic signed-star exponentiation against the actual dense model.
It does not import the primary; it reads primary declarations as data.
Both actual helper APIs discover the imported finite model. No automatic
registration of the standalone checker is claimed. Both caches bind their
own source, this note and all actual local inputs. The primary prints its
machine receipt as `FINAL_JSON`; the receipt field is
`finite_label_algebra_checks_succeeded`, with `physical_auxiliary_lift=open`.
The historical 8/8 primary, 6/6 checker and 20/20 parent-replay credits remain
historical. No parent campaign or child process runs in these entrypoints.
