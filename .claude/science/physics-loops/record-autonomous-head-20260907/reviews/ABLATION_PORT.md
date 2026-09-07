# Cold review of portable ablation port and live binding

Reviewed original portable primary SHA256
4b66eb5e0f4784b9fa5dcf227642666c76ddf066d79679b938b9ab58a66be7c1
and orbital SHA256
dfb36654d1e6918ff04a05d1bc475ae23db190aa683dee65da9c51f2f67f86c6.
The reviewer authored the independent scratch70d route but not either portable
script or its binding. This review concerns the port and interface delta.

No scientific formula drift was found. Fresh portable primary rows have exactly
zero difference from the immutable independent scratch360rows. The orbital
calculation retains its independent8mode covariance/time-quadrature route and
imports no primary implementation. Every360surface and96trajectory is live
computed and keyed-compared. No saved JSON or scratch path is consumed, and
source/dependency hashes are computed from actual current bytes, not literals.
Subprocesses use the current interpreter, single-thread BLAS environment, a
remaining180s timeout, disk-backed capture with2MB stdout rejection, and
independently checked180MiB ceilings. Fresh live comparison maximum6.04e-14,
~2.03s and94.3MiB. Duplicate JSON and nonfinite data fail closed.

Narrow interface findings were reproduced by mutating a checker-shaped live
result: floating rates[3.0], a trajectory edge False in place of0, resource
blas_threads=True, and a contradictory scope string were accepted. Python
numeric equality allowed type substitutions in otherwise exact fields; the
scope string was never compared. These do not change the valid physical
outputs, but they violate the claimed strict schema.

Root explicitly authorized a one-file narrow repair. The reviewer implemented
integer rate/path/resource checks, exact scope validation, and consistent exact
integer aggregate checks, adding the reproduced adversarial cases plus a
floating aggregate count mutation. No numerical formula or parameter changed.
This implementation is NOT represented as independently reviewed by its author;
root will review the final delta. The original cold-port findings remain the
independent review record. The follow-up test compares all physics rows, totals,
trajectories, state residual and support margin exactly against the pre-repair
live result, and checks all9mutations are rejected.

Evidence: portable-ablation-live.json and portable-ablation-fixed.json in the
same parent scratch directory. No canonical receipt or governance file edited.
