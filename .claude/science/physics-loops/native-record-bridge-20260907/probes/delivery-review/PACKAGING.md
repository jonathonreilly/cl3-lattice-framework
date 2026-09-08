# Historical delivery-review evidence

Top-level review scripts, receipts and stdout/stderr are preserved byte for byte. `mutationrepair/` preserves the actual mutated mathematical sources and logs. `case-inputs/` preserves each disposable case's launcher, manifest and action sources, including the pre-repair baseline. Missing-program history deliberately lacks its removed source.

Repeated whole-packet copies created inside the original disposable cases are omitted to avoid recursively duplicating unrelated evidence. Complete scratch cases remain at `/private/tmp/toe-native-record-probes-20260907/delivery-review/`. Their historical manifests describe those earlier full copies, not the final packet manifest. Reviewer scripts retain historical absolute paths and are execution records, not portable entry points; use the root launcher for current reproduction.

The final packet manifest additionally covers final reviews and this packaging note. Its hash consequently differs from the manifest reviewed before those reviews were written. The launcher and all seven executed scientific source files remain unchanged from the final delivery review.
