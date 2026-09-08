---
claim_type: bounded_theorem
actual_current_surface_status: conditional finite tensor-type boundary
claim_scope: One supplied positive rational C4 two-slice Grassmann kernel, its rank-16 OS quotient and exterior coefficients, with separately supplied real-time hopping and pointer writing; I4 and physical time remain open.
---
# C4 Berezin coefficients are Gram data on the supplied two-slice surface

**Date:** 2026-09-08
**Type:** bounded_theorem
**Status:** conditional finite construction; independent final review pending.
**Primary runner:** `scripts/berezin_c4_action_to_fock_record_decision_surface_2026_09_01.py`
**Runner cache:** `logs/runner-cache/berezin_c4_action_to_fock_record_decision_surface_2026_09_01.txt`

The finite kernel below reconstructs CAR fields and an exterior coefficient
matrix. Its coefficient matrix is also the reflected Gram matrix. Raising an
index gives identity, so the two-slice construction supplies no nontrivial OS
time translation. A formal spectral logarithm and an additionally supplied
real-time hopping evolution must be kept separate.

## Premises, inputs and historical boundary

The [current minimal memo](MINIMAL_AXIOMS_2026-06-29.md) supplies no action,
physical matter functional, composite product, time metric, formation law or
Born calibration. The following action, Grassmann product, reflection and
finite occupation carrier are explicit mathematical conditions. I4, that the
framework's physical correlations equal this functional, remains open.

Let A be the four-cycle adjacency, h=-A and g=3I-A. Choose the dimensionless
Euclidean unit delta=log 2 and the exact supplied matrices

```text
B = 2^(-g) = 1/128 [[25,15, 9,15],
                    [15,25,15, 9],
                    [ 9,15,25,15],
                    [15, 9,15,25]],
K = B^2 = 1/4096 [[289,255,225,255],
                  [255,289,255,225],
                  [225,255,289,255],
                  [255,225,255,289]].
```

With 16 Grassmann generators, set
`S=sum_tx bar(chi_tx)chi_tx - sum_xy K_xy bar(chi_0x)chi_1y`.
Use ordered generators indexed `((4t+x)*2+bar)` and the normalized top
coefficient of `exp(-S)` for integration. Reflection reverses product order
and sends `(t,x,bar)` to `(1-t,x,1-bar)`; extend it antilinearly over complex
scalars. The displayed calculations are rational. Selecting these inputs is
not an output of the framework axioms.

The runtime helper is
`scripts/gl_f_identification_bridge_check_2026_06_11.py`: its exact rational
exterior multiplication, Gram, quotient and linear-algebra functions are
called and recomputed. Its guarded main campaign is not executed or accepted.
The two June reconstruction notes and other hash-guarded old notes/runners
are historical definitions/context; their broader physical and audit claims
are not premises licensed here. In particular the July 20 transfer target now
lives at
`archive/notes/docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md`.
Its immutable original Git path/blob is preserved separately from that current
archive path. It supplies historical target context, not a currently accepted
transfer theorem. No obsolete active note is restored.

## Finite reconstruction and coefficient proof

1. A has eigenvalues 2,0,0,-2; thus g has 1,3,3,5 and K has
   `1/4,1/64,1/64,1/1024`. B and K are positive and invariant under all eight
   square frames. B is the unique positive square root after K is supplied.
   Polynomial interpolation on these three distinct K eigenvalues gives
   `g=(131072 K^2-36992 K+1311I)/255`. This inverse identity chooses neither
   K nor a physical action or time scale.

2. Expand `exp(sum_ij bar(eta_i) K_ij xi_j)`. Anticommuting generators make
   each degree-d ordered coefficient equal
   `(-1)^(d(d-1)/2) det K[U,V]`. Removing that declared ordering phase gives
   `Gamma(K)=direct_sum_d wedge^d K`, vacuum coefficient 1. The determinant
   expansion and Cauchy-Binet give `Gamma(I)=I`,
   `Gamma(B)^2=Gamma(K)` and `Tr Gamma(K)=det(I+K)`. The flat 16 by 16
   coefficient array is positive because K is positive.

3. The same normalized functional obeys `Theta(S)=S`. On all 256
   positive-slice monomials its reflected Gram has rank 16 and is positive
   semidefinite. The occupation sub-Gram Gp is positive definite and, in the
   declared occupation order, equals Gamma(K). One can verify the full
   quotient by forming `P=Gp^-1 G_occ,full`: the finite coefficient identities
   give `Gfull=P^T Gp P` and `P M_chi=psi P` for each of the four unbarred
   chi multiplications. Thus null vectors descend for these fields.
   Barred-variable multiplication is not substituted for a Hilbert adjoint;
   that substitution need not descend. The adjoint used is
   `psi^dag=Gp^-1 psi^T Gp` (conjugate transpose over complex scalars).

4. Exact multiplication yields
   `{psi_i,psi_j}=0`, `{psi_i,psi_j^dag}=(K^-1)_ij I`.
   Therefore `f=B psi` satisfies the normalized CAR, using `B^2=K`.
   In occupation coordinates the exterior map `Gamma(B)` gives an explicit
   isometric dictionary to standard ordered CAR, with `S^T S=Gp`, after
   matching occupation ordering. The CAR fields and adjoints generate all
   matrix units: the vacuum projector and creation/annihilation words do so.
   Their commutant is scalar, so the fixed-target dictionary is unique up to
   a scalar. The runner also solves the exact intertwiner equations.
   A hard-core target has nonzero cross anticommutators and admits no invertible
   such dictionary. There is no nonzero singular one either: its kernel would
   be invariant under the full irreducible CAR matrix algebra. This excludes
   that fixed dictionary, not all possible physical matter theories.

5. Write C for the *same* occupation coefficient bilinear. Here `C=Gp` and
   hence `Gp^-1 C=I16`, although C is not the flat identity matrix. The exact
   flat-coordinate identity `Gamma(K)=4^(-dGamma(g))` follows by exterior
   spectral calculus. It intertwines the reconstructed bilinear and the
   standard one and obeys creator covariance. It does not change C's
   covariant index type into a translated correlator. Calling the Riesz
   identity a nontrivial OS evolution would be false.

## Separately supplied real-time and pointer construction

If real-time evolution `exp(-iz dGamma(h))` is additionally supplied, then
`dGamma(g)=dGamma(h)+3Q`; at Q=2 the difference is 6I and affects only a
phase in unitary evolution. The current
`J_xy=i(a_y^dag a_x-a_x^dag a_y)` is the zero-phase derivative of the phased
hopping term, and `i[H,n_x]+sum_y J_xy=0` holds at all four sites.
This algebra gives no analytic-continuation or physical-clock bridge.

For initial1010 and target0101, the Q2 CAR Hamiltonian has
`H(H^2-4I)=0` with the relevant I,H,H^2 entries zero. Its amplitude vanishes
for every real z. The independently supplied hard-core hopping comparison
has `H(H^2-8I)=0` and target amplitude
`(cos(2sqrt(2)z)-1)/2`, equal to -1 at `z*=pi/(2sqrt(2))`.
Hard-core real-time evolution is a hostile comparison, not another transfer
reconstructed from this Grassmann functional.

For the common target projector P and a separate trivially graded pointer,
`V=(I-P) tensor |0>+P tensor |1>` is an isometry. Its channel `rho -> V rho V^dag`
is CPTP and produces pointer weights `(1,0)` and `(0,1)` at the two endpoints.
This coherent channel differs on general superpositions from Block 44's
two-Kraus dephasing channel; their endpoint outputs agree. No equality of the
full two channels is claimed. Under a later matter-only generator tensored
with pointer identity, both written pointer projectors are fixed. Pointer
mixing removes that guarantee. Formation, carrier/readout identification,
future decoupling and any general probability calibration remain supplied.

## Surviving alternatives, evidence and status

A longer temporal extension can provide a translated correlator. For the
explicit symmetric commuting outer links L=I and L=K in a four-slice chain
with central K, block inversion gives one-particle Gram K and translated
bilinear KL. The exterior Riesz maps are Gamma(L), which differ between the
two choices. This shows extra temporal data are needed for this construction.
It is not a theorem for arbitrary noncommuting L or a no-go for OS dynamics.
The independent original review checked these two finite extensions; the
canonical two-slice runner does not execute a four-slice campaign.

The canonical runner retains 13 original certificates and an explicit
120-second timeout. Exact current declarations cover all 17 original mutable
inputs (using the archive alias) plus this note; the imported helper is among
them. Its used functions read no additional files. Historical Git objects,
including original Block 44 comparisons, are fixed provenance, not mutable
worktree inputs or science grades. Current notes/inputs must be frozen before
the genuine cache is generated. The old B45 live path failure and the original
13/0 and 22-mutation prose are preserved; the old counts are not authenticated
by writing this note. Some named mutation flags only enforce wording/custody.
Actual algebraic mutations and cache-input drift controls are separate evidence.

The current result is a finite conditional theorem and a local tensor-type
boundary. I4, action and temporal-extension selection, physical time,
preparation, detector/formation, calibration and global Record compatibility
remain open. There is no independent-wall count, physical no-go, automatic
obligation retirement or new primitive. Old portfolio, novelty and July12
endorsements in the 24 historical packet bodies are historical and unaccepted
here; they are not required for this finite proof. Current recovery follows
the owner-authorized review process. Formal audit waits until a solid TOE;
no audit status or TOE percentage is assigned by this source.
