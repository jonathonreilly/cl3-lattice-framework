# Narrow scanner readiness repair: PASS

Reviewed a5852e65a14b6dcd962e62ed891481920ab79505be4ac6fafd4b92354f6b1d0e source binding, actual driver prefix, readiness wrapper, protocol and retained failure receipts. All1885 declared input hashes match. This review is the startup/runtime delta only; root's independent scanner arithmetic and6155 small checks are reused, not claimed as newly performed here.

The driver explicitly requires isolated, no-site and dont-write-bytecode flags. Its actual loaded-module guard checks both origin and hash before fixture creation and after scanner loading. The readiness source executes that same prefix and imports the scanner without calling scan or generating a fixture. Its preserved result reports exactly that scope. Top-level executable/directory membership is checked; the preserved failure directory is historical and not added to import search paths. The runtime boundary correctly excludes the OS shared-cache libSystem bytes rather than pretending to hash them.

The original failed startup on unbound_distutils_hack remains visible, with no completed fixture or scan claimed. The new-S contract prevents site injection rather than weakening the origin guard. It explicitly charges0.14 seconds prior cost and leaves29.86 seconds for the separate attempt under the shared30-second envelope. The internal29-second alarm is supplementary; root must bind the new external watchdog to29.86, fresh output and current source before launch. An abrupt timeout can bypass Python failure JSON, so outer receipts remain authoritative.

No full scan or fixture generation was performed in this review. No source blocker found for this new readiness contract; this is not permission to retry the old source or a new arithmetic certification verdict.
