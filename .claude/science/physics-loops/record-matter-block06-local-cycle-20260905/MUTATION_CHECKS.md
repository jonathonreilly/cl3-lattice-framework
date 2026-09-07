# Mutation checks

These are small integrity checks for the already completed finite probe. They
do not add a scientific result. Each temporary mutation is expected to make a
runner exit nonzero by crossing an existing declared gate.

The final record is filled after canonical source-bound runs:

| Mutation | Expected guard | Result |
|---|---|---|
| Replace one edge in the primary EDGE_ORDER with 1 | L0 endpoint-star scheduler | exit 1; the temporary runner raised before certification |
| Raise the primary CURRENT_FLOOR to 9.0 | L4 transport-support guard | exit 1; TOTAL PASS=7 FAIL=1 |
| Replace the independent checker EXPECTED_ORDER with 1 | C0 independent front | exit 1; TOTAL PASS=3 FAIL=2 |
| Flip the independent checker ledger sign | C3 persistent ledger | exit 1; TOTAL PASS=4 FAIL=1 |

Temporary mutation copies are outside the repository and are not PR
artifacts. A mutation is counted only when it exits nonzero; no mutation result
is used as a physics input.
