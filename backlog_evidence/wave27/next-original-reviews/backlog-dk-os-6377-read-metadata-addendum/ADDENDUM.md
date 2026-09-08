# Separate #6377 read-metadata correction

The sealed original packet remains unchanged. Its receipt is `df4f67a1e66fe8173e100ec8aeac5e04c3e549b9ae7f6f349784cbcad0707cbf`; all 336 listed artifacts were reverified byte-for-byte.

Two `range_lines` fields were stale counts of narrower statically identified used ranges, while their `read_ranges` fields already described the larger inspected source spans. The Cycle-704 bridge lists lines 1–115: its read count is **115**, not 24. The projected-trace helper lists its full lines 1–223: its read count is **223**, not 201. The old 24 and 201 remain the correct sizes of the explicitly recorded static used-range sets. They must not label the broader read coverage.

All 64 supplier rows were recomputed. These are the only two discrepancies; total listed read coverage is **4,605 lines**, replacing 4,492 wherever the latter is presented as that read total in the original ledgers, report or receipt. The narrower static used-range total remains 4,492. The corrected ledger supplied here changes only the two counts, the aggregate count and an explanatory metadata field.

Both listed spans were read again from the exact frozen source for this addendum and preserved as source-bound excerpts. The Cycle-704 span covers initialization, dynamic loading and extra endpoint context; it does not claim a full read or acceptance of that 805-line campaign. The projected-trace helper's complete 223 lines supply the already reviewed abstract trace/resource computation. No unread portion of either listed span remains. The original read ledger is the prior read-history evidence; this addendum does not invent a missing terminal transcript or expand acceptance to uncalled supplier campaigns.

No scientific source, listed source range, import closure, finding, claim disposition or verdict changed. There was no scientific execution, guard bypass or repeated primary run. The original **CHANGES REQUIRED** verdict and its seven findings remain bound to the original source trees. This metadata-only addendum is separately sealed and does not replace or modify the original 336-artifact packet.
