# Finite eight-row station identities and detector endpoint distinctions

Date: 2026-07-28 (corrected 2026-09-09 after focused review of original PR
6000)

**Authority:** none

**Audit:** unset

**Type:** bounded_theorem

**Status:** proposed_retained

**Primary runner:**
[`frontier_cycle930_third_pair_rc3_2026_07_28.py`](../scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py)

**Independent check:**
[`frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py`](../scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py)

**Execution evidence:**

- primary cache: `logs/runner-cache/frontier_cycle930_third_pair_rc3_2026_07_28.txt`
- primary receipt: `outputs/third_pair_rc3_cycle930_receipt_2026_07_28.json`
- checker cache: `logs/runner-cache/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.txt`
- checker receipt: `outputs/third_pair_rc3_independent_check_cycle930_receipt_2026_07_28.json`
- current ship receipt: `outputs/third_pair_rc3_block_cycle930_ship_receipt_2026_07_28.json`

The primary is self-contained and has no external scientific input. The checker
reads only the frozen primary source and its fresh cache, both by exact
SHA-256. Neither current runner imports the old controller stack or executes
the historical long census.

## Supplied station family

Let `B` and `b` be integers with

`B >= 3`, `1 <= b <= B-2`, `N = 8B-5`, and `P = 8(B-1-b)`.

This result concerns the following supplied, unpadded affine station family:

| Row | Station value |
|---|---:|
| `hf(b-1)` | `5b-3` |
| `f(b-1)` | `5b-1` |
| `hf(b)` | `5b+2` |
| `f(b)` | `5b+4` |
| `r(b)` | `8B-9-3b` |
| `hr(b)` | `8B-7-3b` |
| `r(b-1)` | `8B-6-3b` |
| `hr(b-1)` | `8B-4-3b` |

The rows appear in exactly that increasing order. The only inequalities that
are not immediate fixed gaps are

`r(b)-f(b) = 8(B-b)-13 >= 3`

and the cyclic closing gap

`N+hf(b-1)-hr(b-1) = 8b-4 >= 4`.

The eight cyclic gaps are therefore

`2, 3, 2, 8(B-b)-13, 2, 1, 2, 8b-4`.

The sole unit gap is `hr(b) -> r(b-1)`. This is an ordinal fact about the
supplied rows.

Three ordered pairs have ordinary difference `P`:

- `f(b-1) -> r(b)`;
- `f(b) -> hr(b-1)`;
- `hf(b) -> r(b-1)`.

Consequently, precisely the third listed terminal has another supplied row at
its immediately preceding ordinal, while none of the three first stations
does. Also

`hr(b)-P = 5b+1`,

which lies strictly between `f(b-1)=5b-1` and `hf(b)=5b+2` and is absent from
the eight-row set.

## All P-shift rows and the parity exception

For completeness, solve `x+P=y (mod N)` over all 64 ordered pairs of supplied
rows. Because `0 <= x,y < N` and `0 < P < N`, only
`y-x-P=0` and `y-x-P=-N` can occur.

In the non-wrapping case, the three identities above are the only identities.
The other low-to-high equations reduce to nonzero constants. The nonconstant
same-group equations have the form `8(B-b)=c` with `c<16`, and the
high-to-low equations have the form `16(B-b)=c` with `c<32`; these are
incompatible with `B-b>=2`.

In the wrapping case, the only integral in-domain equations are

- `r(b-1)+P=f(b-1) (mod N)` when `B` is odd and `b=(B-1)/2`;
- `r(b)+P=f(b) (mod N)` when `B` is even and `b=(B-2)/2`.

The other wrapped high-to-low equations have the form
`-8B+16b+c=0` with `c` not divisible by `8`. Wrapped low-to-high equations
have the form `8B+c=0` and force `B<3` or a noninteger value; wrapped
same-group equations have the form `8b+c=0` and force `b<1` or a noninteger
value. Thus the three pair starts are the P-shift rows in every cell, with
exactly one additional reverse row at
`b=floor((B-1)/2)`: `r(b-1)` for odd `B`, and `r(b)` for even `B`.

This is a proof on the full stated integer domain. Both runners also check all
253 originally advertised cells `3 <= B <= 24` as a finite regression. That
regression is evidence against an implementation error; it is not the reason
the general affine statement holds.

## Two different detector endpoints

The historical detector takes a clean-tick bit mask `S` and ends its periodic
suffix at

`last_clean = S.bit_length()-1`.

The historical predictor called `tail_window_P_exact` instead ended its window
at `length-1`, the boundary of the supplied stretch. These are different
observables when a stretch ends with dirty ticks.

The exact witness has supplied length 18, period 2, and clean ticks

`0,2,4,6,8,10,12,14`.

The last-clean detector ends at tick 14 and accepts period 2 with transient 0,
eight clean events, and one occupied residue. The whole-stretch feature ends
at tick 17 and fails because bits 14 and 16 differ. The historical F1 score
`0.1347` and recall `0.5311` therefore belong to the whole-stretch feature;
they are not scores for the detector's last-clean prerequisite.

The primary includes two additional synthetic detector-domain witnesses:

- with `P=4`, equal-width dirty runs of widths `[1,1]` are followed by a tail
  disturbance and the detector rejects;
- with `P=5`, an earlier P-separated pair has widths `[1,2]`, while a later
  periodic suffix makes the detector accept.

These masks show that equality of one selected pair is neither sufficient nor
necessary for this finite detector. They are not asserted to arise in the old
bank controller or in a physical system.

## Periodic regions and run widths

If a binary region obeys `S(t+P)=S(t)`, translation by `P` maps any complete
maximal run, including both of its boundary transitions, to a run of the same
width whenever the translated run also lies inside the region. A run clipped
by an endpoint lacks one boundary and need not have the visible width of an
interior image. For example, a finite slice of a period-five pattern with
three consecutive dirty residues has visible widths `[2,3,2]` at its clipped
left boundary, interior, and clipped right boundary.

The runners exhaust every binary base word for periods 2 through 8 over five
repeats and compare every complete interior translation. This finite check
supports the implementation. The equality itself follows directly from the
translation of the run and its two boundary bits.

## Correct widened-pair control

The widened definition accepts any two dirty-run starts separated by `P`; the
strict definition additionally requires the two starts to be consecutive in
the ordered run-start list. On the historical `B=5`, `b=3`, `N=35`, `P=8`
fixture, the target run-start pair `(18,26)` corresponds for token position
zero to station pair `(17,25)`.

Adding tick `t1+3=21` to a dirty run already occupying ticks 18 through 20 only
extends that run. Its start list remains `(18,26)`, so both definitions see the
target. This was the original defective tooth.

Adding a separated dirty tick at `t1+4=22` instead gives start list
`(18,22,26)`. The widened definition still sees `(18,26)`, while the strict
definition does not. The current predicate requires this `true/false` result,
so replacing the widened test with the strict test fails the control.

## Historical finite evidence

The following values are preserved from the original source, caches, and
receipts. They were not regenerated by the corrected runners and have no
current input-validity claim:

| Historical quantity | Preserved value | Exact operand or limit |
|---|---:|---|
| third-pair register occurrences | 2,698 | original primary, `B=4..8` |
| third-pair full configurations | 34 | original primary finite corpus |
| detected third-pair episodes | 0 | original strict finite hunt |
| widened pair occurrences | 4,576 | original checker tiers, including exposed `B=9` |
| accepted unequal-only cases | 156 | original finite stretch population |
| refusal shape incidences | ACCEPT 3,311; last-clean-tail 3,328; short 252; all-residues 98 | incidences, not a partition of unique stretches |
| best of six tested features | `both_widths_le_3`, F1 `0.5642` | finite historical candidate list |
| equal-width feature | F1 `0.5574` | finite historical candidate list |
| whole-stretch tail feature | F1 `0.1347`, recall `0.5311` | ends at `length-1` |

These rows report a historical experiment on its actual finite operands. Six
features do not classify all possible arithmetic or width statistics. A
finite zero count and the unique unit gap do not identify a cause. The original
seal was written after `B=8` and `B=9` results were already visible, and no
`B>=10` controller corpus was built.

## Scientific boundary

The current theorem establishes affine identities in a supplied row family,
finite detector counterexamples, and a corrected distinction between widened
and consecutive run-start searches. It supplies no controller dynamics, bank
state, physical clock, physical time, Record formation/readout, station-to-site
map, or causal mechanism. It does not promote the historical census, seal,
feature ranking, or zero episode count to current evidence.

The broader questions remain unresolved: which additional variables determine
an episode in the historical controller; whether a useful arithmetic selector
exists; whether any controller observable maps to physical time or Record; and
whether a later physical construction makes the detector relevant. No unique
successor, new axiom, physical prediction, RC-3 closure, or TOE closure follows.

## Source custody and reproduction

The exact eight original endpoint bodies, all three earlier runner bodies, all
four raw commit patches, and the complete 181-artifact focused review packet
are preserved under
`.claude/science/physics-loops/third-pair-6000-correction-20260909/review-packet/`.
`SOURCE_PRESERVATION.json` verifies their hashes and sizes. The historical
458.2-second primary and 678.2-second checker were not replayed. The original
reviewer's 30-second component control remains preserved with its actual
identity and does not stand in for a current producer run.

Run the primary and then the checker under their declared 30-second limits and
the recorded 2-GiB process-group watchdog. Both emit predicate-derived
`TOTAL: PASS=<n> FAIL=<n>` lines. The checker independently recomputes the
load-bearing finite facts and fails closed if either declared input drifts.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "exact affine station identities and synthetic finite detector-domain distinctions on the declared definitions"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "a full-domain affine proof with finite regression, explicit counterexamples, and an independent implementation route"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

No formal audit has run. Audit status remains unset under the owner-selected
campaign policy to defer formal audit until a solid TOE candidate exists.
