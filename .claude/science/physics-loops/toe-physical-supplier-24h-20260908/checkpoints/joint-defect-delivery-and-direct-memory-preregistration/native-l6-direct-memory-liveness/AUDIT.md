# Static full-vector liveness: nine-extra-bank pilot is conservative

Source c0195ff5 reviewed read-only: worker, active, resolvent, plane, original real_kernel, transport, formats and norms. No physical array or action was executed. One full real vector V=2^20*8 bytes=8MiB. Bounds below concern live NumPy array payloads; allocator retention, interpreter/library RSS, source hashing and supervisor baseline remain empirical topology-cost obligations.

## Worker-owned baseline

Worst secondO candidate/certificate stage retains firstP, firstO, secondP, vacuum, current b, outer summed and outer y: seven distinct full vectors. The direct candidate adds its copied x, making eight. Input rhs aliases b. The one-stage frame's returned x becomes secondO only after return, so secondO is not an additional live copy. Candidate diagnostics hold small rotation/coefficient lists, not Fock arrays. The cert dictionaries, loop c, discarded `_`, sources and error lists contain scalars; closures alias existing vectors rather than copying them. Small a/b/omega arrays have21 entries.

Candidate active.solve uses one copied x and chunk-bounded plane/denominator scratch, not another full output. First stages retain fewer vectors. At final assembly the persistent first2+second2+vacuum+b baseline is six; previous summed and y can both remain live while the next transport evaluates, giving eight before transport workspace. At the final divide summed, chi and last y coexist: nine including that persistent six. Early assignments deliberately have not been assumed to release old RHS storage before evaluation.

## Action and certificate

Original action may retain four full workspace vectors at once, including old temporaries during rebinding: out,tmp,old term,new multiply/add or next-linear output. Its input is already in the baseline. The secondO fresh action therefore needs at most8+4=12 full payloads plus bounded kernel chunk scratch. After action returns its local temporaries die; certificate y and r add two to baseline8, giving10. Exact norms add only4096-element byte chunks and scalar integer buckets. This is a bound on live references, not whether the allocator returns previously freed pages to the OS.

## Transport transient bound

For ordinary Eg, out is one full copy, two quarter-vector copies plus at most three quarter-vector expression arrays; total at most2.25V beyond the preexisting baseline. Triplet old is one full copy and the assignment RHS at most1/8V: out+old+RHS<=2.125V. The last Eg has out1V, x/y half copies totaling1V, ids1/4V, q and odd together1/8V, and at most3/4V indexed/multiplied expression payload at a time. Hence at most3.125V additional, conservatively round upward to3.25V for small temporary masks. With final-assembly baseline8 this is<=11.25V. Ordinary NumPy arithmetic and fancy-index copies are included; no assumption that transport is in-place is used.

## Saved vector bridge

At worst baseline8, formats.export adds one np.load vector, and whole raw-file read_bytes hashing adds2V. Its loaded a is still live during hashing, so this is11V plus chunk scratch. verify runs afterward with one load, not concurrently with export's load. Worker hashing itself streams1MiB. Candidate checkpoint writes do not append array copies to manifests. At the final write baseline9 and the same3V bridge overhead gives12V, which is tied with fresh-action peak. NPY source hash buffers are streamed by worker; formats' raw hash remains unchanged and explicitly counted.

## Comparison with proposed fixed pilot

Nine additional touched banks plus the pilot's touched input establish10V baseline. Running the unchanged original kernel on that input adds at most4V workspace, giving14V plus the same chunk overhead. This exceeds the worker's maximum12V action/save payload and11.25V transport payload. Pilot plane/norm/save paths also need to retain all nine banks; save must use the same realNPY/raw bridge so its3V transient is present (13V total). Thus nine extra arrays conservatively cover static live payload of this source, provided the input and all banks remain referenced and touched throughout the measured phases and the exact save path is used.

This is NOT proof that384MiB is met. The cost fixture must use the single supervisor+worker architecture and actual imports/hash checks, and its whole-tree sampled/high-water resource result is decisive. No source release optimization or mathematical change is needed merely to justify the nine-bank fixture. Any later implementation change requires a new liveness comparison. The old CG attempt remains closed.
