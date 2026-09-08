# Prior-art search

Repo-native comparison before implementation:

- `GL_F_FROM_BEREZIN_RP_RECONSTRUCTION...2026-06-10` reconstructs CAR and the
  reflected metric from a supplied Berezin/RP functional, but does not carry a
  plaquette transfer generator into a Record.
- `GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION...2026-06-11` reduces the static
  dictionary to I-4 and proves unique CAR/hard-core nonintertwining at N=2,3;
  it does not close the action-to-Fock operator map.
- `FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY...2026-07-20`
  explicitly supplies the coherent-kernel form and says the action-to-Fock
  identification, kernel normalization, CAR metric, and reflected inner
  product remain open.
- `CORNER_AXIS_FREE_TRANSFER_EXTENSION...2026-06-12` fixes normalization only
  relative to a supplied kernel/trace correspondence.
- Block 44 (`73eccf9394`) proves the exact common-law current/Record
  discriminator but supplies both product representations and the real-time
  action.
- PR #7829 exposes cross-site product as a matter clause; PR #7832 classifies a
  hopping channel but selects no dynamics.  Neither derives the Fock operator
  from a matter action.  PR #7823 owns the gravity pincer and is not duplicated.

External coherent-state/exterior-power identities are standard.  Novelty, if
any, must therefore be program-internal: exact closure of the named finite
action-to-operator prerequisite and its operational consequence, not invention
of fermionic coherent states.

Pinned source blobs are recorded in `SOURCE_BINDING.md` after the
preregistration commit is created.
