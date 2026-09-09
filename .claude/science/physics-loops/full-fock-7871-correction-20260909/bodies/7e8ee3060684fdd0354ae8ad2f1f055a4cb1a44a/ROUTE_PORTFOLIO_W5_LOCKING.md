# Track B route portfolio — W5 derived write-once locking

## Scope and source discipline

This is a design extraction, not a claim that a W5 lock has already landed.
The authorized sources establish the following useful boundary.

- Cycle 693 supplies a one-site `Record(site, content)` shape and an additive
  trace fixture, but no storage dynamics or permanence.
- Cycle 741 supplies a finite \(3\times303=909\)-site archive, fixed reversible
  words, exact byte checks, returned route work, and active gate-deletion
  controls. Its renewal word nevertheless shifts old slot contents before
  depositing the new image. It is therefore not write-once at fixed sites.
- Cycle 741's fifth full-bank attempt preserves payload bytes, but leaves dirty
  controller/bank rails and fails the decoded clean domain. That is a useful
  refusal precursor, not a clean lock.
- Cycle 742 supplies the junction conventions
  \(b\mapsto(\mathbb{Q}(b),0,0,0)\), sitewise Record granularity, `C_source`,
  collection order, and \(G=(\mathbb Q,+)\), and proves byte preservation
  through readout. It explicitly leaves locking open.

The extraction brief additionally identifies the campaign assets as the
Cycle-723/724/730 refusal cascades, the parameterized Cycle-731 count
certificates, the Cycle-732 genesis words, and deletion-detection patterns.
Those assets are treated here as available design idioms, not re-audited
results: their source files are outside this extraction's read boundary.

## 1. Verbatim obligations from the junction probe

The probe says:

> **Record permanence is not an output of Cycle 693.** In the infinite-content
> countermodel, the records are allowed to “lock those contents, remain
> permanent” before the readout is applied
> (`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:93-103`).
> The additive proof begins with possible record instances and a content map;
> it does not turn a reversible storage site into a permanent Record. A W5
> bridge therefore may not take archive permanence from Cycle 693 as a
> premise.

It requires:

> **A derived persistence/locking certificate, not a Record-permanence
> premise.** Cycle 741 establishes that the final archive is unchanged by one
> tested continuation
> (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:759-762`),
> but its renewal word deliberately moves prior slot contents
> (`scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py:624-637`)
> and the archive is full after the bounded run. A lawful Record claim needs
> an invariant showing that a locked record's content cannot be changed by
> every future lawful evolution in the claimed domain, or an explicit
> write-once locking construction that makes this true.

Its feasibility verdict is:

> **NEEDS-NEW-MECHANISM — a derived write-once Record-locking/persistence
> mechanism (or an invariant subspace theorem showing that locked archive
> contents are untouched by every future lawful evolution in scope).**

What may not be put back in as a premise is also explicit:

> It may **not** say that the archive sites are permanent framework Records, that
> Record derived `C_source`, that the readout family is physically available,
> that `G=C`, that there is a physical event-algebra product, or that storage or
> readout persists through a fourth renewal or unbounded future.

And:

> Calling those sites permanent Records would put the missing conclusion back
> in as a premise, contrary to W5 discipline.

The applicable physical-carrier firewall is:

> The general firewalls are also explicit: no dynamics, probability,
> measurement rule, context selector, or physical carrier identification; no
> identification of local \(M_2(\mathbb C)\) multiplication with multiplication
> of readout rules; and no promotion of the mathematical rule class to a
> physically available observable algebra
> (`docs/PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md:141-150`).

Thus “derived write-once” means a transition-level refusal law plus an
inductive locked-content invariant over a declared lawful evolution domain.
Merely observing unchanged bytes, detecting a later change, declaring inverse
operations unlawful, or calling a bit a lock is insufficient.

## 2. Shared M2-level target

Every binary rail below is a physical \(M_2\) site using Cycle 742's supplied
encoding \(0\mapsto\operatorname{diag}(0,0)\),
\(1\mapsto\operatorname{diag}(1,0)\). A candidate mechanism must provide:

1. a payload row \(D\);
2. lock/certificate rows;
3. an offered-word row \(V\) and an incoming write-request token;
4. accepted and reflected/refused token paths;
5. a fixed local word, compiled from the campaign's reversible gate idiom and
   physically routed with all route work returned; and
6. an exhaustive macro audit showing that every gate path capable of touching
   \(D\) is downstream of the same enforcement result.

The request is not absent when locked. It enters the mechanism and exits on
the `REFUSED` path while \(D\), the lock rows, and returned work are unchanged.
This makes refusal a derived transition, rather than “no overwrite operation
is defined.”

The lawful-domain convention still has to be supplied: the finite forward
macro alphabet, its incoming request sector, initial blank sector, and
physical placement. What must be derived is the truth table of every macro
on that sector and the closure theorem

\[
  \mathrm{LOCKED}(x)\Longrightarrow
  D(M_n\cdots M_1x)=D(x)
\]

for every finite composition of declared lawful macros. Microscopic
reversibility is not denied; a time-reversed boundary sector is not silently
identified with a new forward write request.

## 3. Route 1 — enforced dual-rail lock and refusal cascade

**Physical construction.** For one payload row \(D_0,\ldots,D_{m-1}\), add a
dual-rail lock \((U,L)\), with `UNLOCKED=(1,0)` and `LOCKED=(0,1)`. An offered
word \(V\), incoming request token \(Q_{\rm in}\), and output rails
\(Q_{\rm accept},Q_{\rm refuse}\) complete the interface.

The fixed write word first evaluates the lock row. On `UNLOCKED`, the enable
rail gates every payload-copy macro \(V_j\rightarrow D_j\); after the last
payload gate, the same accepted request moves the one-hot lock token
\(U\rightarrow L\) and routes the request to `ACCEPTED`. Thus the first write
sets the lock itself. On `LOCKED`, the violation rail enters the
Cycle-723/724/730-style enforcement cascade, zeros every payload-write enable,
leaves \((D,U,L)\) fixed, and reflects the request to `REFUSED`. Dirty lock
codewords `(0,0)` and `(1,1)` also take the refusal/fault branch rather than
enabling data gates.

At archive scale, use one enforced lock row per fixed 303-site image slot.
The slot word copies all 303 offered bits and sets its lock last. Later write
requests still traverse the word but are reflected before any payload gate.
Cycle 741's current `shift_oldest + shift_newer` prefix cannot remain in the
post-lock macro alphabet: it changes locked physical sites. The honest
scale-up appends generations into fixed virgin slots; newest-first ordering
becomes supplied decoder metadata (or a separately certified pointer), not a
physical shift of prior Records.

**Supplied versus derived.** Supplied: M2 bit encoding, site layout, initial
blank payload and `UNLOCKED` row, incoming-request convention, fixed macro
alphabet, `C_source`, Record activation rule (`LOCKED` means the site now
contributes a Record), and scalar/readout conventions. Derived: one-hot lock
preservation, first-write acceptance, lock setting by that same write, clean
locked-request refusal, return of all route/work rails, exhaustive control
ancestry for every payload target, and the locked-content invariant under
arbitrary finite macro composition. Record supplies none of these dynamics.

**Cheap counterfactual pass.** Exhaust both offered bits and both valid lock
states. A locked request for both the same value and the opposite value must
return `REFUSED`; the same-value case prevents “unchanged by coincidence”
from counting as refusal. Delete one representative gate from (i) the
violation cascade, (ii) a payload enable, (iii) the lock transfer, and (iv)
the refusal route. As in Cycle 741's deletion controls, each deletion must
break a named output/specification row. Also inject both dirty lock codewords
and require refusal/fault with no payload change. Any locked trace changing
one payload bit, producing `ACCEPTED`, or leaving work dirty falsifies the
route immediately.

**Status: BUILDABLE-NOW at bounded fixture scope.** This is the campaign's
native idiom: permanence is exactly “the lock row is enforced.” The missing
work is a new W5 construction and certificate, not a new conceptual
primitive. It is the only route here that directly converts an overwrite
attempt into clean physical refusal without first requiring a new topological
or irreversible sector.

## 4. Route 2 — monotone accepted-write count with enforced cap one

**Physical construction.** Replace the dual-rail lock by a one-hot unary
accepted-write counter. At cap one the row is simply \((C_0,C_1)\):
`C_0=1` means zero accepted writes and `C_1=1` means one accepted write. The
first accepted write copies \(V\) into \(D\) and moves the count token
\(C_0\rightarrow C_1\). Every later request encounters `C_1`, is routed
through the refusal cascade, and leaves both count and payload unchanged.
For a parameterized certificate, the cap-one transition is the \(n=1\)
instance of the Cycle-731 count pattern.

The count is not merely a report computed after execution. It is an input to
the enforcement word, and `accepted_count <= 1` must be derived from the
literal transition table and macro closure. A count certificate that only
notices a second write after it happened is not a lock.

**Supplied versus derived.** Supplied: unary encoding, cap \(1\), initial
`C_0`, request/macro domain, and the same junction conventions as Route 1.
Derived: one-hot conservation, exactly one `C_0 -> C_1` accepting transition,
no lawful `C_1 -> C_0` transition, clean refusal from `C_1`, and invariance of
\(D\) whenever `C_1` holds. The count's monotonicity must be an output of the
word audit, not an axiom.

**Cheap counterfactual pass.** Enumerate the full cap-one basis table, then
compose two and three write requests. Delete the count-transfer gate, one
count-control gate, and one refusal gate. Try a literal reverse/count-reset
word in the claimed macro domain. Any second `ACCEPTED`, any reachable valid
`C_0` after `C_1`, any locked data change, or any dirty one-hot row falsifies
the route.

**Status: BUILDABLE-NOW only as count plus enforcement.** Cycle 731's
parameterized certificate is a strong audit layer, but refusal still comes
from the same cascade as Route 1. It ranks second because it adds a useful
write census and scales cleanly, while using more state and proving no more
permanence than the enforced lock at cap one.

## 5. Route 3 — consumed genesis token (“reversible fuse”)

**Physical construction.** Give each virgin payload row a certified one-hot
genesis token \((G_{\rm live},G_{\rm spent})=(1,0)\). A write macro can touch
\(D\) only while `G_live=1`. The first accepted write copies \(V\), transfers
the token to `G_spent`, and routes success. Later requests see no live token
and are reflected to `REFUSED`. Cycle 732's genesis-word idiom can certify the
initial word and exact token placement; deletion controls can show that each
token-transfer component is active.

This is only genuinely different from Route 1 if token conservation and
non-return follow from a larger physical invariant. If the literal inverse
write, a genesis-restoration word, or a route carrying the spent token back
is a lawful future evolution, the fuse re-arms and permanence is false.

**Supplied versus derived.** Supplied: the genesis word, unique live-token
sector, request orientation, and finite macro alphabet. Derived: token-number
conservation, consumption on the first write, clean reflection without a live
token, and closure of `G_spent` under every future lawful macro. It is not
enough to supply “spent tokens never return.”

**Cheap counterfactual pass.** Apply the literal reverse of the accepted word
and every genesis/restoration macro named in the claimed domain. Search for a
path `G_spent -> G_live`; delete each token-transfer control in turn. A
reachable re-armed state, accepted second write, payload change, or dirty
return rail falsifies the route.

**Status: NEEDS-MECHANISM.** Genesis-word verification is available, but the
authorized archive construction actively restores operating wires to
genesis. A separate enforced sector theorem is needed to show that the lock
token cannot likewise be restored. Once that theorem is supplied, the route
is essentially a physically interpreted variant of Route 1.

## 6. Route 4 — holonomy-marked write parity

**Physical construction.** Surround the payload site or slot by a small loop
of M2 edge rails \(e_1,\ldots,e_k\) and define a loop mark
\(H=e_1\oplus\cdots\oplus e_k\). The blank sector has \(H=0\). The first
accepted write deposits \(D\) and threads one unit of write flux, giving
\(H=1\). A later incoming write with \(H=1\) excites a violation rail; the
enforcement cascade reflects it to `REFUSED` before payload gates fire.
Ordinary read and route deformations may move edge representatives but must
preserve \(H\).

The attractive possibility is that permanence follows from a derived
Gauss/holonomy sector: local lawful words cannot erase the nontrivial loop
mark. Mod-two parity alone is not sufficient, because an unrefused second
write could toggle \(H\) back to zero. The holonomy conservation theorem and
its coupling to every data-writing macro are both required.

**Supplied versus derived.** Supplied: loop geometry, orientation, parity
decoder, initial trivial sector, and macro domain. Derived: first-write flux
insertion, local-word invariance of nontrivial holonomy, exhaustive coupling
of \(H=1\) to refusal, payload invariance in that sector, and returned route
work. Calling the loop mark “topological” does not supply those results.

**Cheap counterfactual pass.** Enumerate all local loop-word generators and
search for \(H:1\rightarrow0\), then compose two writes. Delete one edge
update, one parity-extraction gate, and one cascade gate. Any local erasure of
the mark, accepted second write, data change at \(H=1\), or parity-dependent
dirty work falsifies the route.

**Status: LIKELY-BLOCKED at present.** None of the authorized W4/W5 surfaces
provides a physical holonomy/Gauss-law sector or proves its conservation.
This could eventually give the strongest mechanism-level permanence, but it
imports substantially more structure than W5 presently needs.

## 7. Cross-route deletion and corruption discipline

Cycle 741's deletion controls are a certification pattern, not themselves a
lock. Apply that pattern to every viable route:

- delete one active gate from deposit, lock/count/token setting, violation
  propagation, refusal routing, and route-work return;
- corrupt one payload bit, one lock/certificate bit, and one request bit
  independently;
- distinguish detection from prevention: a changed checksum or failed
  certificate after payload mutation does not satisfy write-once;
- require a locked same-value request to be refused, even though its payload
  bytes would otherwise compare equal; and
- audit the literal macro inventory so that no unguarded target of \(D\) is
  hidden behind a helper, inverse, restore, or routing word.

This is also why redundant hashes or byte snapshots are not ranked as a
separate route. They make tampering visible but do not make overwrite
`REFUSED`; when upgraded to prevention, they require Route 1's enforcement.

## 8. Ranking

| Rank | Route | Verdict | Reason |
|---:|---|---|---|
| 1 | Enforced dual-rail lock | **BUILDABLE-NOW** | Native refusal-cascade idiom; the first write sets the lock; locked writes remain present and are cleanly reflected. |
| 2 | Monotone accepted-write count | **BUILDABLE-NOW with enforcement** | Adds a parameterized census and cap-one proof, but count-only detection is insufficient and the refusal core is Route 1. |
| 3 | Consumed genesis token | **NEEDS-MECHANISM** | Compact and compatible with genesis-word certificates, but a non-return/closure theorem is needed in a reversible setting. |
| 4 | Holonomy-marked parity | **LIKELY-BLOCKED** | Potentially strongest invariant, but requires a new physical holonomy sector and conservation proof. |

## 9. First cycle: exact smallest honest fixture

The first cycle should prove **one binary Record cell, not a 303-bit slot and
not the 909-site archive**.

- Seven semantic M2 rails form the local fixture:
  payload \(D\), offered bit \(V\), dual lock \(U,L\), and request rails
  \(Q_{\rm in},Q_{\rm accept},Q_{\rm refuse}\). Put them on a fixed
  nearest-neighbor layout; any SWAP/route word must return the layout and
  work exactly.
- Persistent storage begins at \(D=0,(U,L)=(1,0)\). Each interaction supplies
  a forward incoming request packet with \(V\in\{0,1\}\); this is an event
  boundary input, not fresh blank storage.
- The supplied junction convention activates a Cycle-693 singleton Record
  only at `(U,L)=(0,1)`, with
  `Record(site=p_D, content=(Fraction(D),0,0,0))`. `C_source`, equality,
  \(G=(\mathbb Q,+)\), and physical availability remain supplied exactly as
  Cycle 742 says.
- Exhaust both first writes \(V=0,1\). Each must return `ACCEPTED`, set
  `(U,L)=(0,1)`, and store the offered bit. The \(V=0\) row matters because
  “written zero” must differ from blank solely through the lock.
- From each locked result, exhaust both a same-value request and an
  opposite-value request. All four cases must return `REFUSED`, preserve
  \(D,U,L\), and return route/work rails.
- Exhaust `READ` and `IDLE` on both lock sectors, audit every literal target
  of \(D,U,L\), run the gate-deletion and dirty-lock controls, and prove by
  induction over the finite macro truth table that arbitrary finite future
  compositions preserve \(D\) once locked.

The first cycle claims only this one-cell forward interaction sector and its
inductive closure. It does not claim the unchanged Cycle-741 shift word is
write-once, does not claim a locked 303/909-site archive, does not derive
`C_source` or the scalar carrier, and does not claim fourth-renewal or
unbounded storage capacity. A successful next scale step is a fixed
303-payload slot guarded by one enforced lock row and filled by append into a
virgin physical slot, with no post-lock shift.
