# Canonical whole-carrier dictionary port review

Scientific disposition: PASS for the complete canonical note3d61dfac1a844364b98c731efca34b27b3c8dac1a3049d519f26d97b1db12715 and the unchanged finite calculations. One narrow timeout-wrapper repair is requested below. This is a canonical portability/source-delta review reusing the prior independently reviewed general proofs, not a new independent proof count or formal audit verdict.

Read the full note, primarye8911bf3cc1647e3637c6b277ee9da82bb6b05f0be0ffe11e3590697a0c8cb60, every line of all three helpers, their complete diffs against the preserved originals, the original full dictionary proof and completed common-carrier review, input closure, port receipt and actual outputs. READ_HASHES.json binds all canonical source inputs. The original review442e3b3e covered the dictionary, charged and exchange mathematics; my prior projected-ice work is reused where relevant, not recounted as a fresh proof.

## Quantified source and signs

The canonical theorem retains a finite connected simple loopless graph, specified vertex/neighbor orders and the full2^E carrier. It explicitly drops the old simultaneous fixed-cycle state constraint, rather than claiming that native hopping dynamically releases it. Every right-hand operator is restricted to the all-positive Gauss subspace. The enlarged Fock/link tensor product is mathematical redundancy, not added physical roles or an independently accessible matter factor.

The phase direction is correct: a_e(x)d(x xor e)=d(x)b_e(x). For reverse toggles (-i)^|x| gives+i, compensated by M_ee=1; the symmetric off-diagonal quadratic mask supplies the other signs. The increasing-order Majorana interval includes i and excludes j. On every oriented simple cycle the adjacent Majoranas cancel in their existing order, including descending edges through antisymmetry, and i^r(-i)^r=1. Odd cycles and the hexagon therefore keep the necessary native phase. The hopping sign is the positive CAR hopping times link X with the stated T convention. The all-m Gauss census and even total parity are explicit; no odd sector or independent two-species factor is inferred.

Ice gating is restricted to even periodic cubic L>=4, excluding the small periodic multigraph ambiguity. The corner degree criterion gives the two alternating patterns; F_p commutes with the toggle and its Pauli dressing. W removes the native cycle phase while retaining all electric functions. The note does not identify ungated S with ice-preserving dynamics or derive the ring Hamiltonian from the vanishing ice-sector T.

The low-charge identities require |G|<=1, and are not asserted for the entire edge carrier. Bipartite staggering preserves signed charge under the projected hop. The Hamiltonian, local gates, relaxed state space and couplings remain supplied. The three-hop identity retains both complete support and intermediate-path conditions; reversing three incident A factors gives minus one. This supports an exchange algebra, not deconfined particles, relativistic statistics or U1 dynamics. The note explicitly distinguishes the old additional-U1-link model and does not close its physical supplier premise.

## Actual execution and port deltas

All scientific bodies are preserved. The author helper only adds wrappers and exposes its result; the independent helper replaces scratch output writing with result; the exchange helper additionally converts two assert statements to explicit failures, preserving their predicates under optimized Python. Runtime imports contain no scratch modules. All three local helpers are named in AUDIT_INPUT_PATHS and actually invoked through runpy. The two upstream science notes and the U1 comparison note are source-bound; source hashes are evidence identity, not proof of their contents.

A fresh isolated copy of the exact primary and all declared inputs was run with PYTHONOPTIMIZE=1 --json. It executed7919 assertions in0.145seconds at42.875MiB. Its payload and input hashes equal the stored canonical output after removing measured timing/RSS only. The two resource-independent scientific counts6712+17+1190 are honest:15 matrix groups plus two guards in the independent helper,1188 representatives plus two guards in exchange. Local boundary representatives are not represented as a global low-charge-state census. LIVE.json and PAYLOAD_COMPARISON.json preserve the run.

## Narrow wrapper correction

Every helper currently executes signal.alarm(180) unconditionally at top level. Since the primary runs them in its own process through runpy, each resets the primary's absolute alarm. The primary final elapsed check will reject an overlong completed run, and the external cache timeout protects the reviewed cache invocation, but the standalone primary's signal timeout is sliding rather than a single180-second deadline. Guard each helper's alarm with __name__=='__main__' so the primary owns the alarm during runpy. This is a resource-interface correction only; no mathematical input, count or scope changes are requested.

No other blocking correction was found. No full pipeline, audit, queue mutation, or source edit was performed by this reviewer. Final timeout-delta confirmation should bind the repaired runner/helper hashes while preserving this original review.
