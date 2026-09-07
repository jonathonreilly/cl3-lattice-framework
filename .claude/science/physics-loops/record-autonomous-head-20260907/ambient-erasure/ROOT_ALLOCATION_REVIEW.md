# Root independent allocation review

Reviewed every changed allocation and caller. The single full ambient lift
workspace is consumed before overwrite; saved trajectory matrices are new
matmul outputs and do not alias it. CSR conversion retains all nonzero entries
without a numerical threshold. All source columns remain covered in32-column
blocks; the final density Frobenius norm sums every entry. The417+72 identity
counts, fixture, tolerances and180second/180MiB ceilings are unchanged.

Root additionally made each block residual reject nonfinite values before
Python max can ignore a laterNaN. This is a guard repair, not altered numerical
coverage. Failed191.67MiB original source and receipt remain in historical/.
The final canonical replay is required before marking evidence current.
