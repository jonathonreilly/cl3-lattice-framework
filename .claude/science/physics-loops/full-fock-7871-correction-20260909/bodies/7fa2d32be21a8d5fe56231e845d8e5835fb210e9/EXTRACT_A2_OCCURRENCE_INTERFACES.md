# Track A cycle-2 extraction: Cycle-332/335 occurrence interfaces

## Scope and bottom line

This extraction uses only the two named runners and the Cycle-719 `N6 — partial-closure paths` prescription. The runners provide reusable bounded mechanics, but neither accepts a Cycle-719 “physical word” object directly. Cycle 332 can derive conditional transition/close bits after boundary and matcher inputs are fixed. Cycle 335 can move protected candidate triples through recurrent/export/append structures, but it has **no actual-member selector output**. Therefore a first composition can honestly establish only conditional same-word interface compatibility; it cannot establish realized-history selection or a permanent typed Record.

## 1. Input surfaces: state, consumption, derivation, and supply

### Cycle 332: transition occurrence and close

The file describes its own scope as starting from the Cycle-314 event stream and Cycle-329 matcher/readiness, while keeping the two boundary registers supplied and refusing to promote a candidate to Record (`scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py:2-8`).

| Surface | Exact input/state shape | What it consumes and returns | Derived here | Still supplied or conventional |
|---|---|---|---|---|
| `TransitionProgram` / `compile_transition_program` | Frozen state with `length: int`, opaque `sidecar: object`, and three arrays: `active_rows`, `nonvacuum`, `truth` (`:91-98`). Constructor inputs are `length` and `deleted=False`; only `L=3,6` are admitted (`:100-112`). `truth` is an `ambient * ambient` bit array indexed by `(pre, post)` (`:104-112`). | Builds the event sidecar from the fixed Cycle-314 code, identifies active/nonvacuum rows, and marks the fixed stream-map transitions when not deleted (`:103-112`). | The transition truth table and reversible full mapping (`:115-120`); the controls check 1,020 ambient rows, 508 nonvacuum transitions, no false positives/negatives, and no permutation/involution failures (`:179-216`). | The fixed Cycle-314 code/stream program, the choice `L=3` or `L=6`, and whether the transition stage is deleted. There is no Cycle-719-word decoder on this surface. |
| `transition_witness` | `(program, pre: int, post: int, witness: bit = 0) -> bit` (`:123-133`). `pre` and `post` must be ambient-row labels. | XORs the supplied witness ancilla with `program.truth[pre,post]` (`:129-133`). | A conditional occurrence witness for the supplied boundary pair. | Both boundary labels and their preparation; optionally the witness ancilla convention. The runner itself chooses a first active nonvacuum `pre` and its stream-mapped `post` in its positive fixture (`:267-270`). |
| `boundary_certificate` | Five bits `(pre_code, transition, post_code, match, ready)` plus optional `deleted_stage` (`:245-258`). | Passes the five-bit tuple to the fixed Cycle-329 causal certificate against `(1,1,1,1,1)` and returns its first bit (`:254-258`). | A relational close bit once all five inputs are fixed. The positive fixture gives witness = certificate = 1 and receiver `(0,1)`; readiness alone, false boundaries, anti-splices, and every stage deletion fail (`:271-311`, `:357-374`). | `pre_code`, `post_code`, matcher result, readiness result, their physical preparation, and the fixed comparator/certificate convention. In the tournament, boundary code bits are literally supplied as `1`, while matcher/readiness come from a constructed Cycle-329 fixture (`:265-272`). |
| `protect_candidate` / `protected_closed_flag` | Candidate bit plus optional deletion index; returns `(protected_triple, inverse_recovered_triple)` (`:379-394`). The flag consumes a three-bit tuple and equality-tests it against `(1,1,1)` (`:397-398`). | Fan-outs candidate `1` into `(1,1,1)`, then reversibly uncomputes to `(1,0,0)`; equality provides a closed flag. | Protected candidate redundancy and an identity-checked predecessor-ready route. Fault, fanout-deletion, identity-splice, and false-boundary controls are rejected (`:401-520`). | The initial prior candidate is manufactured by calling the local-close receiver with **all five semantic inputs set to `1`** (`:404-410`). Fresh replica/history capacity and the meaning of “candidate” remain supplied. |

Cycle 332 gives the most explicit derived/supplied inventory. It derives “conditional Cycle-314 stream-transition witness,” “two-boundary close certificate,” and “identity-checked predecessor readiness from protected candidates”; it leaves supplied/open the two boundary registers and preparation, actual-member selection, fixed transition/comparator programs, fresh capacity, Record typing, permanence, and clock matcher/calibration (`scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py:594-609`). Its terminal claim is only three bounded transition-sensitive routes “without promoting a witness or candidate to selected Record history” (`:622-640`).

### Cycle 335: protected recurrence, export, and append

Cycle 335 composes Cycle-332 protected candidates into three pieces of apparatus and says at file scope that the broad registration negative is blocked (`scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py:2-8`). Its candidate alphabet is hard-coded as `ZERO=(0,0,0)` and `ONE=(1,1,1)` (`:48-51`).

| Surface | Exact input/state shape | What it consumes and returns | Derived here | Still supplied or conventional |
|---|---|---|---|---|
| Ring rotation and invariants | `rotate_right(slots: tuple[triple,...], deleted_swap=None)` and inverse `rotate_left(slots)` (`:227-248`); `candidate_invariants(slots, identities)` consumes a same-length identity tuple (`:251-268`). | Permutes whole protected triples. The invariant summarizes occupancy, triple weights, identities, cyclic adjacent views, and occupancy counts. | For the hard-coded four-slot ring `(ONE,ONE,ONE,ZERO)`, four distinct phases recur exactly, inverse restores the initial ring, the blank visits indices `(3,0,1,2)`, and swap deletion is detected (`:271-306`). | Initial slot contents, identity labels `(1,1,1,0)`, ring size, and selector phase. The source explicitly says candidate-only invariants “ignore supplied phase” and records only the tautological distinction `0 != 1` as `selector_phase_distinguishes` (`:281-303`). |
| `ExportState` / export | Frozen state `incoming: triple`, `slots: tuple[triple,...]`, `exported: triple` (`:310-315`). `export_step(state, deleted_swap=None)` and `export_inverse(state)` return the same shape (`:317-332`). | A reversible swap chain moves one triple across the bounded window. | On the internal fixtures `ExportState(ONE, (ONE,)*L, ZERO)`, the final `.exported` is `ONE`, the existing blank relocates to `.incoming`, inverse is exact, and deletions fail (`:335-367`). | Initial incoming/slots/exported contents, `L=3` or `6`, and—critically—the semantic convention that the triple crossing `.exported` is an “actual” member. The code derives transport, not that meaning. |
| `append_step` | `(slots: tuple[triple,...], phase: int, incoming: triple=ONE, deleted=False) -> (new_slots, output_triple)` (`:370-384`). It requires `slots[phase] == ZERO` and `incoming == ONE`. | Swaps the protected candidate into the specifically indexed blank slot. | A finite append prefix, exhaustion rejection, explicit reverse unwind, and deletion sensitivity for `L=3,6` (`:387-438`). | The write phase, protected incoming candidate, blank initialization, window length, and any rule that interprets a written slot as the realized member. |
| Identity/frame/fault controls | No external constructor; internal fixtures use Cycle-329 words and Cycle-332 `protect_candidate(1)` (`:441-468`). | Checks 48 `(L, frame)` cases plus identity splices, replica faults, and invalid-domain calls (`:469-495`). | Bounded covariance/identity/fault compatibility. | The underlying fixed fixture, candidate value `1`, and the semantic mapping from the Cycle-719 word into this fixture. |

The no-argument tournament drivers (`protected_recurrence_controls`, `moving_export_controls`, and `append_window_controls`) build their own fixtures; they are certificates/test surfaces, not general constructors for a Cycle-719 word. Cycle 335’s semantic firewall states exactly that it derives “bounded protected recurrence/export/append mechanics” and does **not** derive “actual member, Record typing, permanence, time” (`scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py:498-511`). Its final result likewise says `member_selection_no_go: "not shipped"` (`:525-537`).

## 2. Cycle-719 prescription and its W1/W2 preconditions

The relevant Cycle-719 section first inventories the two interfaces:

- Cycle 332 has three bounded positive transition-occurrence/close routes, but “boundary-pair preparation and selection remain supplied” (`docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md:378-382`).
- Cycle 335 has positive recurrence/export/window mechanics, but “realized-history selection and phase/boundary roles remain supplied” (`:383-387`).

The feed-after-W1/W2 prescription is verbatim:

> Within Cycle 719, the strongest next closure is literal local enforcement of  
> the one-token/clean-work sector around the actual controller macros.  The  
> already-positive refusal circuit is a finite starting primitive.  Parallel  
> routes are a local Gauss/charge-sector construction and a boundary-free paired  
> controller excitation.  Only after W1/W2 closure should the same physical word  
> be fed unchanged into the Cycle-332/335 occurrence/Record interfaces.  No  
> axiom or registry change is requested.

Evidence: `docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md:403-409`.

The demanded precondition artifacts, using only this prescription’s own text, are:

1. **W1-side closure:** literal local enforcement of the one-token/clean-work sector around the actual controller macros. The already-positive refusal circuit is named only as a “finite starting primitive”; the local Gauss/charge-sector construction is named as a live route to the demanded enforcement.
2. **W2-side closure:** a boundary-free paired controller excitation.
3. **Then, and only then:** an unchanged instance of the same physical word must feed both the Cycle-332 and Cycle-335 views.

These preconditions are **not shown as met in the allowed scope**. The phrases “strongest next closure,” “starting primitive,” “parallel routes,” and “only after W1/W2 closure” describe unfinished prerequisites, not completed certificates (`:403-409`). No evidence in either allowed interface runner supplies those Cycle-719 closures. Thus this extraction must not infer that later, out-of-scope artifacts have met W1/W2.

## 3. Honest `ACTUAL` / `ADMISS` binding shape

There is no callable `ACTUAL(word)` or `ADMISS(word)` interface in either runner, and neither runner accepts a common physical-word state. A first composed harness would need read-only projections from the unchanged word into the existing primitive shapes:

```text
P332(word) -> (TransitionProgram, pre, post, pre_code, post_code, match, ready)
P335(word) -> (protected triples, identities, phase, incoming/slots/exported)
```

The mechanically available 332 chain is:

```text
t = transition_witness(program, pre, post)                   # conditional bit
c = boundary_certificate(pre_code, t, post_code, match, ready)
r = run_local_close(..., occurrence=t, close_law=c)          # positive fixture: (0, 1)
```

This is supported by `scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py:245-258` and `:305-325`. Therefore the most faithful `ADMISS` binding is not an unconditional physical predicate but the **tuple of conditional verdicts** `(t, c, r)`. If a one-bit API is required, a supplied convention could define `ADMISS(word) := r[1]`; that convention is valid only after the word projections, boundary preparation, fixed comparator, and matcher/readiness semantics are independently justified. Cycle 332 itself does not perform that justification.

Cycle 335 has **no selection output to bind to `ACTUAL`**. Its returned details expose ring mechanics, final `ExportState`, or append states, while its firewall explicitly says actual-member selection is not derived (`scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py:498-511`). The closest mechanically precise candidate is:

```text
next_state = export_step(state)
candidate  = next_state.exported          # a protected triple
ACTUAL(word) := candidate                 # only under a supplied export=actual convention
```

Alternatively, a supplied selector phase can choose one ring/window slot. Both are imported selection rules, not Cycle-335 outputs. Calling `.exported == ONE` a selected actual history would overstate the source, which proves only transport (`:335-367`) and explicitly leaves member selection unshipped (`:525-537`).

The conventions that remain supplied in a first composition are therefore:

- the read-only projections of the unchanged Cycle-719 word into Cycle-332 boundary rows/codes and Cycle-335 protected triples;
- synchronization showing that both projections refer to the same physical word and same transition;
- the two boundary registers and their physical preparation;
- fixed transition, comparator, matcher, and readiness semantics;
- the selector tag/phase or the rule “exported means actual”;
- candidate/blank/identity encoding, initial ring/window state, and fresh capacity;
- Record typing, permanence, time/clock interpretation, and calibration.

**Honest first-cycle claim ceiling:** a bounded, conditional **same-word interface-compatibility certificate** at the declared `L=3,6` fixtures (including the existing frame, deletion, inverse, fault, and capacity checks). It may say: *given W1/W2 closure and the listed supplied projections/conventions, one unchanged word produces a Cycle-332 conditional occurrence/close candidate and a Cycle-335 reversibly transported protected candidate.* It may not say that the dynamics selected the actual member, formed a typed permanent Record, or derived time.

## 4. Feasibility verdict

### BUILDABLE-NOW — bounded certificates already present

- Cycle 332: reversible two-boundary conditional transition witness with exact false-event/deletion controls (`scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py:136-220`); relational close certificate with no readiness-only, anti-splice, or stage-deletion survivors (`:261-376`); protected predecessor-candidate route with replica/fanout/splice faults rejected (`:401-520`); held `L=6`, 24-frame, and domain controls (`:544-591`). Reported support/capacity figures include witness support `M2=91` (`:197-215`), close-chain `M2=720` (`:352-374`), and protected-history chain `M2=1198` with fresh-replica `M2=6` (`:489-519`).
- Cycle 335: exact four-phase protected recurrence with recurring blank and inverse (`scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py:271-307`); exact moving export/inverse (`:310-367`); finite append/exhaustion/reverse unwind (`:370-438`); identity, 24-frame, fault, and lawful-domain controls (`:441-495`). Reported ring apparatus is `M2=16`, and each route reports maximum primitive support `M2=6` (`:283-304`, `:367`, `:438`).
- Buildable composition artifact: a narrow adapter/harness that evaluates both families from supplied projections of one immutable word and reports the full conditional result tuple. This is software plumbing, not a new physical-selection theorem.

### NEEDS-MECHANISM — overall verdict

The overall same-word physical claim is **NEEDS-MECHANISM**:

1. a **Cycle-719-to-332/335 projection/decoder** that identifies the physical word’s pre/post boundaries, match/readiness inputs, protected candidate triples, identities, and phase without changing the word; and
2. a **physical actual-member/phase-retirement mechanism** that derives which protected candidate is realized instead of importing a selector phase or the convention “exported means actual.”

The prescription additionally requires prior W1 one-token/clean-work enforcement and W2 boundary-free paired excitation. Those are prerequisite mechanisms/certificates, not supplied by these interface runners.

### BLOCKED — ceiling wall

A composed **realized, typed, permanent Record** theorem is blocked by the **W1/W2-plus-selection wall**: the Cycle-719 prescription does not permit feeding until W1/W2 close (`Cycle719:403-409`), Cycle 332 leaves boundary preparation and selection supplied (`Cycle719:378-382`; `Cycle332:594-609`), and Cycle 335 has no selector output and leaves realized-history selection plus phase/boundary roles supplied (`Cycle719:383-387`; `Cycle335:498-511`). Record typing, permanence, and time are further independent walls. The conservative verdict is thus: mechanics/certificates are reusable now; conditional adapter composition needs an explicit decoder; `ACTUAL`/permanent-Record closure remains blocked pending a genuine physical selection mechanism and the prescribed W1/W2 certificates.
