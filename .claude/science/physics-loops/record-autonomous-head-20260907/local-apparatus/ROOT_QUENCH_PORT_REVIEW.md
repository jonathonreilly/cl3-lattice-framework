# Cold review of root quench port and live comparison

Reviewed primary29996db7e098fd21a0400cdd6ce0554f1485598a7014955a8210dac4fd8e3cab
and helper8b5070cb511dad23814c7b0de65013dd0306f63919df698999d5bc991416ab56.
The reviewer did not author the root full-Fock witness, portable binding or
orbital helper. The SAFE_CAP mathematics was independently derived earlier.
No repository source was edited during this review.

## Science and independence

The portable full-Fock computational body is unchanged from the frozen
/private/tmp/toe-root-local-apparatus-20260907/quench_certificate.py; the diff
adds metadata, live binding, controls and readable output. Fresh frozen/portable
runs have EXACTLY identical cases, CAR checks, residual maximum, physical fixture
and rational certificate. No numerical parameter or tolerance changed.

The helper independently uses6x6 orbital matrices: exterior eigenvalue products
cover all64Fock sectors for the unitary echo norm, while sums of positive/negative
Hermitian eigenvalues give the full-Fock second-quantized energy-defect norm.
It imports no primary functions or saved results. Its binding compares all32
cut/time identities with exact cut/order metadata and finite nonnegative norm
values. Missing/duplicate cases and false norm/type/hash/resource data are checked.
A fresh live run passes at maximum2.22e-15 in0.35s,62.8MiB. Both180MiB/180s
limits remain unchanged. Pure--json output parses successfully.

The live comparison explicitly covers complete echo and global-energy defect
norms, NOT the independently untested feedback norm. The source does not claim
that six-modeCAR matrices reproduce ambient native-code matrices or a48qubit
dynamical simulation. The rational certificate matches SAFE_CAP_FINITE_LADDER:
delta1/320, coefficient221/7, trace221/2240<.1, energy481/51200<.01,
M31040 and15battery qubits. Its48storage-qubit count explicitly excludes the
suppliedMarkov bath and remains conditional on the reviewed theorem/encoding.

## Actionable interface/resource findings

1. Production JSON decoding does not reject duplicate keys. A response with
   source_sha256='WRONG' followed by the correct duplicate key passes compare.
   Use a duplicate-detecting object_pairs_hook and reject nonfinite constants.
2. The top-level payload is not an exact schema and there is no recursive
   finiteness check. Adding an extraNaN field or validation_ok=False passes.
   Require the exact currently emitted top-key set and finite JSON values;
   this avoids silently accepting contradictory status or unaudited metadata.
3. rss_MiB=0 passes although this is not a real measured peakRSS. Require>0
   for RSS while retaining nonnegative elapsed time. The strictinteger resource
   fields already reject bool substitutions correctly.
4. capture_output collects arbitrarily large stdout/stderr before checking
   resource use, unlike the existing bounded-capture ports. Use disk-backed
   capture with an explicit response-size rejection (e.g.2MB) and a remaining
   primary runtime budget. The current top-level180s alarm eventually bounds
   the primary, but the child timeout is independently180s and can outlive the
   parent if it consumes the residual budget. No problem occurred in this run.

These are validation-contract/resource robustness gaps, not a numerical or
scientific discrepancy. A narrow binding-only repair should preserve exact
physics output and add demonstrated decoder/top-schema/RSS mutations. This
review does not authorize self-independent review of a subsequent repair.

Evidence: localized-lift/root-quench-live.json, root-quench-original.json and
review_quench_payload.py under this primary scratch directory. All original
source/artifact bytes remain unchanged.
