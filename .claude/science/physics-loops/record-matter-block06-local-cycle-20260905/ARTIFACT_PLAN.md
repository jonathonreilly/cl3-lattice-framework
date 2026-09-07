# Artifact plan

## Canonical claim

Claim ID: native_edge_record_local_cycle_transport_and_ledger_bounded_theorem_note_2026-09-05
Claim type: bounded_theorem
Current surface: conditional-support
Audit: unset; the independent audit lane owns any verdict.

| Surface | Role |
|---|---|
| docs/NATIVE_EDGE_RECORD_LOCAL_CYCLE_TRANSPORT_AND_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md | Finite theorem/support note and scope boundary |
| scripts/native_edge_record_local_cycle_transport_2026_09_05.py | Primary native-edge runner |
| scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py | Independent fixed-N CAR checker |
| logs/runner-cache/native_edge_record_local_cycle_transport_2026_09_05.txt | Source-pinned primary receipt |
| logs/runner-cache/native_edge_record_local_cycle_transport_independent_check_2026_09_05.txt | Source-pinned checker receipt |
| .claude/science/physics-loops/record-matter-block06-local-cycle-20260905/ | Loop packet and handoff |

## Canonical commands

~~~text
python3 scripts/native_edge_record_local_cycle_transport_2026_09_05.py
python3 scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py
python3 scripts/cached_runner_output.py --refresh scripts/native_edge_record_local_cycle_transport_2026_09_05.py
python3 scripts/cached_runner_output.py --refresh scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py
python3 -m py_compile scripts/native_edge_record_local_cycle_transport_2026_09_05.py scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py
git diff --check
~~~

The primary cache also fingerprints its imported native-edge parent source
through AUDIT_INPUT_PATHS. The checker has no source imports beyond standard
scientific libraries.

## Source and receipt identities

| Artifact | SHA-256 |
|---|---|
| Primary source | 002bf0c89c5a331a9708c0ef5167d7d7d4f611c00c59642dc768f618492a2a0a |
| Independent checker source | 4993a578ad81c6691be2fe105ba3b0d8285f1d78797714d680e1576a95298910 |
| Primary cache | 1e9b8609263dfb03c194f6ea995ead605f5497be417239382f9733c9e083d69c |
| Independent checker cache | 70c70d4e14fb8081a304f474f2a39a7232bfc21c4317dbdf4629ba25228a94bb |

The primary cache header records the imported parent fingerprint
d3219a61403899ffeb29b373bb7321a18042b1c247dec9017d1d65d7c6168538.

No generated audit ledger, queue, status, or verdict is authored by this
block. If the citation graph is regenerated because the new note is a graph
node, only the generated citation manifest may co-land; it is inventory, not
authority.
