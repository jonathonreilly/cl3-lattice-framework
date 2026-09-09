# The traveling token-count certificate — W1's matched-parity residual refused — Cycle 731

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle731_token_count_certificate_2026_07_28.py`](../scripts/frontier_cycle731_token_count_certificate_2026_07_28.py)
- [`frontier_cycle731_count_certificate_independent_check_2026_07_28.py`](../scripts/frontier_cycle731_count_certificate_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 730 froze the honest residual of local enforcement: matched-parity
multi-token states satisfy every radius-one row, so local rows enforce
the parity sector, not the token count. This cycle builds the nonlocal
certificate that the W1 ledger line has named open since Cycle 724 — a
**traveling counter**: a supplied clean counter register threaded once
around the ring, a reversible controlled increment at each station
(every gate local to counter + station), an end comparison against the
declared expected count feeding the existing OR-cascade refusal latch,
then exact uncompute. No runtime Python branch survives; the word is
fixed unrolling from `(N, expected_count)`.

- **extended word 112,912 semantic gates** (+13,602 over Cycle 730's
  99,310); the Cycle-730 anchor is regression-pinned unchanged; lawful
  trajectories reproduce Cycle-730 behavior exactly with all registers
  (counter, increment/comparison scratch, refs, `h`, every auxiliary)
  returning clean, and the literal reverse is exact;
- **the frozen residual is now refused**: the exact Cycle-730
  matched-parity witness (tokens at sites 0 and 5, `h = 0`, canonical
  references) is refused with reason `count_mismatch` (station 0,
  observed count 2, expected 1) — and **all 55 two-token placements**
  on ring-11 with `h = 0` are refused, every one;
- **the full enforcement theorem**: over all 8,388,608 rail/`h` cases
  on ring-11, the word passes unmolested **iff** the token count equals
  the declared expected count **and** token parity equals `h`
  (count-pass cases 45,056; full-pass cases 22,528; zero iff
  exceptions; outcome table frozen by sha256);
- **the two laws factor**: the count certificate touches no reference
  bit and never writes `h` (zero touch failures), so count enforcement
  and the Cycle-730 parity law are independent mechanisms — deleting
  either leaves the other's law intact;
- deletion controls (increment gate, comparison gate, uncompute gate)
  are each detected; both the 2-bank and 12-bank physical fixtures pass
  collision-free nearest-neighbor routing with returned work; the
  Cycle-713 pins are byte-unchanged.

With this, `w1_ring11_count_law_enforced: true` and the runner reports
`w1_closed: true` **at bounded scope only**, with the scope key stating
exactly: bounded ring-11 enforcement; no genesis or arbitrary-ring
inventory derivation. W1 as a general wall is not discharged — see Open.

## Supplied / derived / open

### Supplied

- `expected_count = 1`: the same declared one-source-token inventory
  line Cycles 724/730 already carry — the certificate **enforces**
  the declared inventory, it does not derive it;
- the clean counter, increment scratch, comparison scratch, and refusal
  latch genesis; the static reference chain, `h`, ring orientation,
  program content, and clean data genesis; everything the Cycle-719
  controller core declares.

### Derived

- the compiled traveling-counter word and its exact reversibility;
- refusal of the frozen matched-parity witness and of every two-token
  placement; the exhaustive ring-11 count-and-parity iff theorem with
  frozen outcome tables;
- the factorization of the count law from the parity law (structural
  bit-touch audit plus behavioral identity);
- deletion detection; routed physical fixtures; unchanged inherited
  anchors.

### Open

- W1 beyond the fixture: arbitrary ring sizes as a uniform theorem
  family, derivation of the expected-count inventory itself (genesis),
  and any statement not conditioned on the declared supplies;
- everything the landed Cycle-713/719/724/728/730 surfaces leave open
  at their scopes; no time/Record/Born/source content is touched.

## Negative-claim discipline

No negative claim ships. The bounded-scope `w1_closed` flag is a
positive enforcement statement conditioned on declared supplies, with
the remaining gap stated verbatim in the claim boundary.

## Verdict

The W1 ledger line completes its arc at fixture scope: witnessed
(Cycle 724), compressed to one marked-edge bit (Cycle 728), parity
sector enforced (Cycle 730), and now token count enforced by a
traveling certificate whose gates are all local — the nonlocality lives
in the register's walk, not in any gate. The matched-parity blind spot
is refused, prediction-exact, with the count and parity laws provably
independent. What remains of W1 is the inventory itself: deriving, not
declaring, the expected count. Independent audit still required.
