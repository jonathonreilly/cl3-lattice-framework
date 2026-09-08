# Independent cold review: native parity reservoir

Disposition: PASS for the finite algebra and the stated conditional architecture/measure boundary. No physical measure selection, AC closure, or general no-go is established. The degeneracy qualification below should accompany any proposed q-identification experiment; it does not contradict the frozen nondegenerate fixture.

## Exact coverage

Complete reads: RESULT_MEMO.md, check_square_frozen.py, check_reservoir.py, results.json, reservoir_results.json, both preregistrations and SHA256.json in the author action-measure directory. The declared hashes all match actual bytes. The principal memo SHA is89edc7d06cf34fac0edde6ad979c812c8b2bd292181a7f78b8536f91589176ce; square source ce8d3fb9142e7e540897cf7ac0d157d1b5eb2948133af2c31f5b548863634bd3; reservoir source79f7701bab7d24f1ff3bfe1113877bfb63db4b77c31812d059147552c6e9723f. Both executables were run read-only, with stdout written only in this review folder: their entire parsed payloads equal frozen raw,17 and7 assertions respectively.

Source binding: main47da12268436ee1843e822386477aa2c829d95a9, native edge-instrument physical placement paragraph and Theorem1 equations2–4 were read directly. The main axiom and local Gibbs/parity limitations were also read in the preceding source-map task. This review does not independently reverify all open-PR head/provenance assertions listed in the author's memo; they remain its supplied source inventory, not added proof authority here.

## Independent general derivation

Let V be an m-dimensional one-particle space, m>=1, and A any linear map. On full Fock space F(V)=direct_sum_n wedge^n V, Gamma(A)=direct_sum_n wedge^n A. The polynomial identity

    det(I+zA)=sum_n z^n Tr(wedge^n A)

holds for all A: prove for diagonalizable A by eigenvalue products and extend as a polynomial identity. It does not require A Hermitian or a thermal interpretation. With D_plus=det(I+A), D_minus=det(I-A), the even and odd traces are E=(D_plus+D_minus)/2 and O=(D_plus-D_minus)/2.

Append one inert one-particle mode r with transfer eigenvalue1. The total-even Fock space is the direct sum

    [F_even(V) tensor |0>_r] direct_sum [F_odd(V) tensor |1>_r].

Gamma(A direct_sum1) acts by Gamma(A) on both summands. A diagonal boundary weight W_q=|0><0|+q|1><1| therefore gives exactly

    Z_q=E+qO=[(1+q)D_plus+(1-q)D_minus]/2.

This derivation uses exterior algebra, not the author's Pauli implementation. q>=0 makes W_q positive; the polynomial identity itself also holds for arbitrary scalar q. At q=1 the trace is D_plus. This is one matter Fock copy with a parity register, not a second conjugate matter copy and not |det|^2. Fixing the reservoir occupation gives E or O instead; normalization of a prepared reservoir state and tracing an unnormalized boundary weight are different operations.

At A=I, E=O=2^(m-1). Dividing by the zero-transfer weighted dimension gives

    F_q(A)=Z_q/[2^(m-1)(1+q)]
          =[D_plus+r_q D_minus]/2^m,
    r_q=(1-q)/(1+q), q>=0.

Thus F_q-F_1=r_q D_minus/2^m. If D_minus!=0, this normalized observable distinguishes every distinct finite q>=0. If D_minus=0 it distinguishes NONE: any A with eigenvalue1 is such a degeneracy. In a thermal family A(t)=exp(-t h), an inert matter zero mode makes the degeneracy persist for every t. At t=0 all models are necessarily degenerate. A proposed q-identification family must contain at least one member with D_minus!=0. The author's square has D_minus=1/4 and meets this condition.

For positive-definite A, O>0, so the unnormalized Z_q changes with q even in some normalized-degenerate cases. Calling that an identifiable physical difference additionally requires an independently fixed overall normalization. For completely general A, even the unnormalized coefficient O can vanish, e.g. A=0. These are mathematical distinctions, not alternative physical trace selectors.

## Native carrier and exact fixture

The square has M=4,L=4,c=1, one independent cycle check, physical Hilbert dimension16 and code dimension2^(M-c)=8. The native source explicitly represents only total-even CAR on this connected code. Four mode full Fock has dimension16 and cannot simply be identified with that eight-dimensional code.

Adding a leaf gives M=5,L=5,c=1, again one cycle check: physical dimension32, code dimension16. It is an actual additional edge-qubit site, not an M4 local-site substitution. For an explicit virtual Z3 embedding choose vertices0=(0,0,0),1=(1,0,0),2=(1,1,0),3=(0,1,0),4=(-1,0,0); source physical edge centers are (1,0,0),(0,1,0),(-1,0,0),(2,1,0),(1,2,0). The added mode has zero hopping/energy but the graph/code remains connected because the zero-coefficient edge is retained. Deleting that edge as a Record event would be a different code-sector problem.

The enlarged code need not be viewed as the old even-code tensor an independently prepared qubit; its useful decomposition includes both matter parities tied to the added mode. The source faithful dictionary licenses the total-even algebra. No physical preparation of the needed full-trace boundary contraction follows from the dimension count.

For the opposite dimers, h has eigenvalues+1,-1,+1,-1. At t=log2, A has eigenvalues2,1/2,2,1/2; the exterior layers are [1,5,33/4,5,1]. Independently E=41/4, O=10, D_plus=81/4, D_minus=1/4. E/8=41/32 differs from D_plus/16=81/64. At q=2, Z=121/4 and F_2=121/96 differs from F_1=81/64 by -1/192. These values agree with both literal native matrix programs and raw files.

The source uses exp(-log2 T)=I-3T/4+T^2/4, correctly obtained from the eigenvalues0,+/-1. The two disjoint hoppings commute. The square cycle phase i^4=1 is correct for this geometry, but its script should not be generalized to arbitrary cycle lengths without restoring the source i^length factor.

## Controls and limits of evidence

Ten independent review assertions passed: exterior layers, normalized mismatch, q2 exact value and mismatch, zero-mode E=O and q invisibility, nondegenerate q injectivity on four rational controls, two whole-payload live comparisons, and all declared source hashes. They are recorded in INDEPENDENT_CONTROLS.json. No random or fitted result was used.

The author's reservoir check named normalized_full is algebraically redundant with native_full_trace: both divide the same equality by16. It is not an additional independent normalization experiment. This is a check-description limitation, not a false assertion; the memo's nontrivial q2 normalization comparison is valid and independently checked here.

Holding CAR and matter H fixed while changing q changes the closure/boundary weight. One may equivalently encode q as a reservoir chemical-potential boundary factor; that does not make it an unchanged FULL action-and-measure experiment. The memo correctly claims only unchanged matter hopping/algebra. A chosen trace fixes q=1 mathematically; no inference from zero energy to a physically equiprobable ensemble is warranted.

The positive result is therefore a native finite parity-reservoir realization of a chosen full-Fock contraction. Its exact remaining physical premise is which preparation/sewing/readout mechanism selects that contraction on a nondegenerate family. Passing at a stipulated q=1 or programming an intensity from Z_q would not supply this premise. The existing AC action, charged-lepton sector and grain/readout identifications remain separate unclosed obligations.
