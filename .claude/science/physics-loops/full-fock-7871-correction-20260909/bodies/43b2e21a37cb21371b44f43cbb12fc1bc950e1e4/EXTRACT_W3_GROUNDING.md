# W3 formation/admission grounding — Cycle 719 time lane

This is a bounded extraction from the five authorized files.  The two no-go
notes do not contain a literal `claim_scope` field, so the verbatim blocks below
are their own scoped no-go statements.  Line references name the landed source
lines.  The imported `EventChain` implementation is outside the authorized
corpus; consequently, the four field meanings below are operational
forcing targets inferred from their call site and names, not a claim about
unread implementation internals.

## 1. The two no-gos and their daylight

### Record-formation non-supply no-go

**Verbatim scoped claim** (`docs/ACPHILAMBDA_R_ETA_RECORD_FORMATION_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:56-61`):

> Within the current axiom/primitive surface, Record formation does not force
> R-eta. It supplies existence of formed records, not the occurrence/rate law or
> readout-context theorem that would select the direct density-as-angle member.
> Selecting R-eta still requires a separate inhomogeneous readout theorem,
> occurrence-lane event-rate theorem, physical action/source bridge, or
> approved primitive with the exact declared scope.

**What it forecloses.**  It forecloses the inference from the bare axiom
sentence “Records form” to the specific R-eta direct-density-as-angle selector.
Its finite witness holds the formed records fixed while allowing incompatible
per-record scalars and totals, so formation existence alone cannot be that
selector (`...RECORD_FORMATION...md:38-52`).  It does **not** foreclose all
formation, admission, occurrence, or readout constructions; the note expressly
does not claim all future occurrence-lane or readout-context routes are closed
(`...RECORD_FORMATION...md:6-10`).

**Uncovered premises / precise daylight.**  The note explicitly leaves out a
formation rule, event rate, site distribution, record-production process, time
metric, weight, and physical-observable bridge
(`...RECORD_FORMATION...md:30-34`).  It leaves live an inhomogeneous readout
theorem, an occurrence-lane event-rate theorem, a physical action/source
bridge, or an exactly scoped approved primitive (`...RECORD_FORMATION...md:56-61,
102-112`).  A W3 candidate may therefore add an objective event-to-record
formation/binding dynamics, an epoch occurrence selector, or a physical
admission predicate.  It may not relabel the generic fact that records form as
one of those missing rules.

### Record-outcome/orbit-occupancy non-supply no-go

**Verbatim scoped claim**
(`docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:19-22`):

> Grant an auxiliary invertible complex block carrier. Even with that grant, the
> four axioms do not entail whether an additive,
> K-even determinant readout uses one complex determinant grain or the
> realified two-power grain.

The note immediately fixes the outer boundary verbatim
(`...ORBIT_OCCUPANCY...md:47-48`):

> This is a current-surface non-entailment result. It does not rule against a
> future physical CAR/action theorem that derives a specific Gaussian measure.

**What it forecloses.**  On the granted auxiliary finite complex carrier, the
current four-axiom surface plus additivity, similarity invariance, K-evenness,
and pointwise realized-state evaluation does not select raw complex
determinant power one over the realified power two
(`...ORBIT_OCCUPANCY...md:24-45, 134-143`).  More narrowly, Record additivity
does not choose that raw determinant power (`...ORBIT_OCCUPANCY...md:123-128`).
It is not a generic no-go for event formation, objective occurrence, or
admission.

**Uncovered premises / precise daylight.**  A physical matter action, Berezin
measure, K/CPT structure, determinant line, polarization, orbit quotient, and
physical record-to-action map are not derived
(`...ORBIT_OCCUPANCY...md:108-121`).  A future action-native CAR/Berezin
theorem, real/Majorana action theorem, or physical carrier theorem remains
outside the claim (`...ORBIT_OCCUPANCY...md:177-195`).  Thus an action-derived
admission or formation law is not contradicted, but merely adding Record
additivity or an auxiliary determinant readout is foreclosed as its selector.

**No-go discipline conclusion.**  New-premise candidates for W3 must lie in
objective occurrence/selection, local formation/binding dynamics,
state-dependent admissibility, or a physical law-domain/action bridge.  Neither
bare formation existence nor Record additivity/determinant normalization is
daylight.

## 2. `BINDER/ACTUAL/ADMISS/LAW` supply-site census

The primary controller imports the two-rail core
(`scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py:23-29`)
and inventories the aggregate `BINDER/ACTUAL/ADMISS/LAW acceptance inputs` as
supplied (`...recurrent_matter_history_controller...py:1436-1440`).  It separately
keeps “objective actuality/admissibility rather than supplied flags” open
(`...recurrent_matter_history_controller...py:1451-1455`).  In the two selected
scripts, the only concrete consumption site is the two-rail core:

```text
scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py:244-249
status = coarse.admit(
    tick_id=event,
    orientation=1 if direction == (1, 0) else -1,
    certificate=1, binder=1, actuality=1, admissibility=1, law_domain=1,
)
logical += status != "admitted" or B.cell_rows(decoded) != B.cell_rows(coarse)
```

The `BINDER/ACTUAL/ADMISS/LAW` inventory names map respectively to the
`binder`, `actuality`, `admissibility`, and `law_domain` keyword arguments.
`certificate=1` is a fifth, separately named input and is not part of W3's
four-name inventory.  The call is made once inside
`for event in range(2 * bank_count)` (`...two_rail...py:226-248`), while the
program-station count and event count are separately reported
(`...two_rail...py:259-264`).  Therefore the landed shape is four scalar integer
`1` values acting as Boolean acceptance flags **per event**.  They are neither
a four-column lookup table nor values attached to each controller-program
station.  The 130 applications are circuit ordinals, not physical time
(`docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md:187-188`).

| input | landed consumption and shape | what “derived” would mean operationally |
|---|---|---|
| `BINDER` → `binder` | Scalar `1` passed to `EventChain.admit` for every event (`...two_rail...py:232-248`). | Replace the literal by a deterministic value forced from an upstream physical event-to-record relation: the decoded pre/poststate and a local formation surface must determine whether this event is bound to this record/cell. “Records form” alone is insufficient. |
| `ACTUAL` → `actuality` | Scalar `1` at the same per-event call site; it is not the word “actual” used elsewhere for an executed circuit (`...two_rail...py:244-249`). | Replace the literal by the output of an objective occurrence/realized-member rule on the epoch's physical alternatives, so the state/history structure fixes which event, if any, has actuality. |
| `ADMISS` → `admissibility` | Scalar `1` at the same per-event call site (`...two_rail...py:244-249`). | Replace the literal by a locally evaluated admissibility predicate forced by the event state, conserved/enforced sector, and declared candidate relation. Domain enforcement counts only if a theorem identifies that domain predicate with admission of this event. |
| `LAW` → `law_domain` | Scalar `1` at the same per-event call site (`...two_rail...py:244-249`). | Replace the literal by membership in a physically derived law domain, computed from upstream invariants/constraints for this event. This is the admission harness's `law_domain` bit, not by itself the separate Born/history law left open in W6. |

The two-rail report calls clean genesis and event predicates supplied and
autonomous occurrence/admission open (`...two_rail...py:554-572`).  The 719
note likewise says that accepted-event flags are supplied and that the law
domain is conditional on supplied acceptance and genesis inputs
(`docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md:313-323`).
So a computed replacement is not “derived” merely because it is written as a
function: its value must be forced by upstream physical structure already
independent of the acceptance verdict.

## 3. W3 wall statement and recorded pair implications

**N2 wall statement verbatim**
(`docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md:264-277`):

> The raw open list is collapsed into seven residual classes:
>
> - `W1`: autonomous local enforcement/preparation of the declared controller,
>   code, bank/link/route, and clean-syndrome domain;
> - `W2`: retirement of the source boundary, finite oriented program geometry,
>   supplied program content/order, and passive-only controller covariance;
> - `W3`: objective formation/admission values replacing supplied
>   `BINDER/ACTUAL/ADMISS/LAW` inputs;
> - `W4`: post-capacity renewal and separated multi-source composition;
> - `W5`: a physical bridge from reversible packets to the axiomatically named
>   permanent Record, not Record permanence as a new premise;
> - `W6`: Born weighting and realized-history selection; and
> - `W7`: source/gravity meaning, reciprocal response, and a no-refit prediction
>   attachment.

N2 warns that “not established” is not an independence theorem
(`...CYCLE719...md:279-281`) and records every W3 pair as follows, verbatim
(`...CYCLE719...md:286,291,296-299`):

| pair | first closes second? | second closes first? | skill classification | evidence disposition |
|---|---|---|---|---|
| W1/W3 | not established | not established | operationally separate here; no independence theorem | controller-domain checks do not derive admission; supplied admission does not prepare the controller sector |
| W2/W3 | not established | not established | operationally separate here; no independence theorem | boundary-free geometry does not select occurrence; admission bits do not remove a program ring |
| W3/W4 | not established | not established | operationally separate here; no independence theorem | an admitted event can still exhaust finite capacity; renewal does not determine which event occurs |
| W3/W5 | not established | not established | operationally separate here; no independence theorem | Cycle 332 supplies a conditional occurrence witness without permanence; the Record axiom supplies no formation rule |
| W3/W6 | not established | not established | operationally separate here; no independence theorem | occurrence/admission does not set weights, while weights do not choose the realized admitted member |
| W3/W7 | not established | not established | operationally separate here; no independence theorem | source meaning does not by itself produce objective admission, or conversely |

## 4. Route candidates

| route | uncovered premise used | classification | why |
|---|---|---|---|
| **Epoch occurrence pullback for `ACTUAL`, then `ADMISS`.**  Evaluate the unchanged 719 physical word inside an objective occurrence structure for the epoch and pull its selected member back to per-event bits. | An objective occurrence/selection rule on the epoch's physical alternatives, including boundary/selection preparation rather than a supplied chosen branch. | **Needs-mechanism.** | The 719 note reports bounded transition-occurrence and protected-recurrence routes, but their boundary-pair preparation, selection, and realized-history selection remain supplied (`...CYCLE719...md:378-387`); W2/W3 and W3/W6 record no automatic implication. |
| **Enforcement-cascade pullback for `LAW`, with a possible structural `ADMISS`.**  Feed a derived charge/count-sector predicate into `law_domain`, and into `admissibility` only if admission is proved equivalent to that predicate. | An exact identification theorem mapping the derived charge/count law's per-event state predicate to the `EventChain` law domain and, separately, to admission eligibility. | **Buildable-now for the `LAW` plumbing; needs-mechanism for scientific W3 closure.** | The user-supplied post-730 fact makes a nonconstant `LAW` adapter plausible now, but the authorized 719 evidence says controller-domain checks do not derive admission (`...CYCLE719...md:286`) and the law domain remains conditional on supplied acceptance (`...CYCLE719...md:322-323`). Thus derived enforcement does **not automatically** change either landed supply status: `LAW` changes only after exact composition/identification, and `ADMISS` needs an additional equivalence or occurrence theorem. |
| **Local record-formation surface for `BINDER`.**  Determine binding from the event's physical pre/poststate and a local record-production transition, at the formation-rule/site-distribution scopes excluded by the R-eta no-go. | A local event-to-record formation/binding dynamics fixing site, content, and association; not the generic existence statement “Records form.” | **Needs-mechanism.** | This lies exactly in the first no-go's daylight (`...RECORD_FORMATION...md:30-34,97-110`), while the 719 note says the minimal axioms grant no formation dynamics (`...CYCLE719...md:325-330`). |
| **One composed occurrence-to-record interface for all four bits.**  After W1/W2 closure, feed the same 719 physical word unchanged into occurrence/Record interfaces, derive `ACTUAL/ADMISS` from occurrence, `BINDER` from formation, and `LAW` from the verified domain. | A commuting physical interface theorem from the 719 event state to occurrence, formation/binding, and law-domain predicates, with no selected boundary or flag supplied. | **Needs-mechanism; strongest integrated route.** | The 719 note itself prescribes feeding the same word into the Cycle-332/335 occurrence/Record interfaces only after W1/W2 closure (`...CYCLE719...md:403-409`), so the integration target is concrete but not presently certified. |
| **Exactly scoped four-value premise.**  Grant the missing values as an approved primitive if constructive routes all fail. | A state-indexed formation/admission functional with exact scope and no claim to derive Born weights, permanence, or determinant normalization. | **Likely-blocked as a derivation route.** | It would be governance rather than derivation, exactly as the record-formation note says for a narrow selection primitive (`...RECORD_FORMATION...md:102-112`), and the 719 note requests no axiom or registry change (`...CYCLE719...md:403-409`). |

**Top route.**  The best Track-A route is the composed
epoch-occurrence-to-record interface: first force `ACTUAL/ADMISS` from the
epoch's occurrence structure, then force `BINDER` from the local formation
surface, while importing a genuinely derived enforcement predicate only for
`LAW`.  It uses three separately uncovered premises and respects the recorded
non-implications rather than pretending one closes the others.

## 5. Forcing-classification stakes

If every constructive route fails, the minimal-missing-content candidates are:

- **`BINDER`:** “For every candidate physical event and record cell, a
  state-local binding predicate is fixed, and `BINDER=1` exactly when that event
  physically forms or updates that cell's record.”
- **`ACTUAL`:** “For each epoch's physically available alternatives, an
  objective occurrence rule fixes the realized member, and `ACTUAL=1` exactly
  for that member.”
- **`ADMISS`:** “For every candidate event, a state-dependent admissibility
  predicate is fixed independently of the acceptance call, and `ADMISS` equals
  that predicate.”
- **`LAW`:** “For every candidate event, membership in the applicable physical
  law domain is fixed by the event state and the derived enforcement laws, and
  `LAW` equals that membership predicate.”

These are deliberately four separate minimal-content sentences.  The N2 pair
table supplies no license to merge W3 with genesis/enforcement, geometry,
renewal, Record permanence, Born selection, or source meaning; nor does it
prove that such a merger is impossible.
