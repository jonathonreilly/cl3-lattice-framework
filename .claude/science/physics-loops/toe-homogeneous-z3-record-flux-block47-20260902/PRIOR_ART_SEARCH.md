# Prior-art search

Authority was refreshed to `origin/main@2cea9a595ee2f0a6c47096de6f821b905182f48c`
before fixing the target. Searches covered homogeneous/infinite cubic signed
walks, all-odd and body-diagonal darkness, parity-sector propagator selection,
Clifford shift cancellation, Bessel kernels, and local occupation Records.

No exact joined duplicate was found. Strong component overlap is explicit:

- `ONSITE_CHARGE_CONSERVING_ENDPOINT_SYMMETRIC_COMMON_HAMILTONIAN_STRICT_QCA_DICHOTOMY...2026-07-12`
  owns the infinite-`Z^3` uniform one-particle Bessel kernel. Its `J=1/2`
  specialization supplies the comparator formula; this block does not claim
  that formula as new.
- `FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL...2026-06-12` and
  `FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY...2026-07-20`
  own related staggered Clifford/two-step kernels, with the action-to-Fock
  kernel identification still supplied. They do not own this real-time
  symmetric signed-adjacency Record protocol.
- `STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION...2026-05-17` owns the
  direction decomposition of the anti-Hermitian-difference staggered Dirac
  operator. The present symmetric signed adjacency is diagonally unitarily
  equivalent to that usual self-adjoint Kogut--Susskind derivative up to the
  conventional scale; neither the operator nor its dispersion is claimed as
  new.
- Block 46 owns the finite isolated-cube identity and explicitly names this
  homogeneous all-odd continuation.
- Open PR `#7832` is the direct interface: it relocates directed cubic
  response to a hopping channel and names site-dependent signs as open.

Novel content, if successful, is narrowly the exact homogeneous parity-sector
kernel theorem joined to one common local target-occupation Record protocol.
It is not the Clifford algebra, uniform Bessel kernel, or a physical action
selection. The standalone-PR value gate is expected to fail unless execution
also closes a physical-functional or Record-process bridge.
