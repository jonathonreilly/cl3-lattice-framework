# Original PR #6000 bounded correction report

The corrected surface retains the exact finite eight-row station identities
and narrowly scoped detector facts. It removes the old causal,
global-arithmetic, physical-time, Record, and RC-3/TOE conclusions.

The primary is self-contained. Its first and only current run passed 11/11
predicates in 0.08 seconds under a 30-second runner limit and a 2-GiB
process-group watchdog, peaking at 48,922,624 bytes RSS. The independent
checker pins the exact primary source and cache. Its first and only current run
passed 9/9 predicates in 0.04 seconds, peaking at 47,546,368 bytes RSS. Both
runner stderr sections were empty. Each outer wrapper stderr contains only its
normal cache-refresh notice.

The original reviewer found that attempt 1 named the checker in the note and
inventory but omitted it from both actual audit-packet helper registries. The
superseding correction adds one literal claim-scoped registration to each
consumer. Both APIs now return exactly the independent checker. The registry
files compile, and all 32 standard-library fingerprint tests pass. No note,
primary, checker, cache, or numerical receipt changed, and no numerical runner
was repeated. The complete attempt-1 packet remains immutable under
`backlog-third-pair-6000-fixes/attempt1`.

The current results are: the full-domain affine station proof with its parity
exception; a 253-cell implementation regression; a concrete distinction
between last-clean and supplied-stretch endpoints; explicit `[1,1]` rejected
and `[1,2]` accepted detector-domain masks; complete periodic-run translation;
and a real widened-only `t1+4` control. The old `t1+3` extension is preserved
as the true/true counter-control.

All 181 receipt-bound review artifacts, eight original endpoint bodies, three
earlier runner bodies, and four raw commit patches remain byte exact. The
458.2-second and 678.2-second historical controllers were not replayed. Full
base-to-head diff checking passes, and the 195-path repair has no intersection
with main changes since the author base at final sealing.

No formal audit was run under the owner-selected deferral. This author packet
is ready for the original same-session reviewer; it assigns no science grade
and mutates no main, GitHub, shared planning, or audit state.
