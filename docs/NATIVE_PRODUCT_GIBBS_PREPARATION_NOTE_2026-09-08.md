---
claim_id: native_product_gibbs_preparation_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Conditional on the native finite edge/CAR carrier, product ready preparation, programmed hopping and occupation-difference phase pulses, and Born/Lueders leaf events, a finite path apparatus implements the stated imaginary-time Kraus filter on every ready input. Its selected output on the supplied maximally mixed ready state realizes the full matter Gibbs functional on the even matter algebra. A separate odd three-mode encoding supplies the displayed two-mode hopping/density filter, quadratic on that constrained domain. Every leaf outcome is retained and success probabilities are explicit."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
  - native_edge_record_local_cycle_transport_and_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_product_gibbs_preparation_2026_09_08.py
---

# Product preparation and native leaf Records for finite Gibbs filtering

**Date:** 2026-09-08

**Type:** bounded_theorem

The finite construction replaces a supplied thermal starting state with a specified product ready state and an explicit sequence of native controls and leaf events. The controls and their physical preparation remain supplied. The result is conditional-support; it selects neither a physical Hamiltonian nor a temperature or formation law.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite operator construction with a general path proof, exact dimer evidence and independent noncommuting physical/CAR checks."
trace_class: upstream_support
target_claim_id: native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
target_blocker_text: "Prepare a specified matter background on the native carrier from an explicit nonthermal ready resource."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Supply physical ready preparation and control selection; evaluate the interacting and energy-conserving preparation obligations."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target and obligation graph

**Target.** For every finite matter path of length $m\geq2$, every supplied real symmetric zero-diagonal nearest-neighbor one-particle matrix $h$, and every finite $\beta\geq0$, the apparatus below implements

\[
 K_s=c\exp(-\beta H/2)P_{\rm ready},\qquad
 H=d\Gamma(h),\qquad
 c=\exp\left[-\frac\beta2\sum_{\epsilon_j<0}|\epsilon_j|\right]
\]

as an unnormalized success Kraus map, with a complete physical leaf instrument and the success probability stated below.

| Obligation | Authority and treatment |
|---|---|
| Native edge qubits, even CAR dictionary and recorded-edge signs | Supplied carrier from the linked matter-instrument source; the conditional source theorem is an upstream dependency, not an axiom |
| Tree incidence, parity reservoir and product ready functional | Proved here |
| Native vacant/filled leaf contraction | Proved here using the displayed CAR identities; independently checked as physical matrices |
| Adjacent phase/hopping synthesis of a real mode rotation | Proved here with explicit conjugation and adjacent elimination |
| Full Kraus map, normalization and all-outcome completeness | Proved here |
| Encoded two-mode hopping/density example | Separate finite construction below; its density expression is quadratic on the declared odd three-mode domain |
| Physical selection of preparation, controls, $h,\beta$ and actual event formation | Open; not used as proved premises |

The strongest missing physical obligation is a law supplying the declared ready resources and programmed controls on this carrier. The mathematical target quantifies over those supplied inputs and does not end at a lemma requiring that physical law.

## Supplied inputs and source meaning

The [native edge/CAR source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md) supplies the conditional ordinary tensor composition, ordered Pauli dictionary, Born/Lueders edge event and deletion model. Its real hopping is $T_{ij}=c_i^\dagger c_j+c_j^\dagger c_i$. The [local transport source](NATIVE_EDGE_RECORD_LOCAL_CYCLE_TRANSPORT_AND_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md) explicitly uses the supplied occupation-difference phase $\exp[-i\theta(n_i-n_j)]$. This construction programs arbitrary finite angles of that same control form on adjacent matter modes; such controllability is an explicit apparatus condition, not a theorem inherited from the source's one numerical pulse.

| Input | Role and provenance | Open physical bridge |
|---|---|---|
| Finite tree roles, ordinary tensor product, Pauli frame and native dictionary | Conditional apparatus, as in the linked carrier source | Physical selection and covariance of the apparatus |
| Pure physical leaf Z preparations and maximally mixed remaining qubits | Explicit product preparation defined here | Preparation mechanism; these sharp leaf values are initially **unrecorded** |
| Real hopping pulses and adjacent occupation-difference phases | Supplied native operator forms and programmed angles | Control, timing, interaction and energy supply |
| Real $h$, finite $\beta$, diagonalizing program | Declared mathematical input family | Selection of physical couplings and temperature |
| Leaf events, Born weights, Lueders update and subsequent hopping deletion | Conditional event model of the source | Primitive event formation, rate and permanent physical dynamics |
| Gaussian diagonalization and matrix exponential | Standard finite-dimensional mathematics, reconstructed below | No additional physics supplied |

The primitive registry contains scale reference, kinetic isotropy and realized state; this finite dimensionless calculation makes no missing-premise claim about any of them. The ready state is specified apparatus data, not a selection supplied by the realized-state primitive. No new axiom, primitive, empirical value or fitted coefficient is introduced.

## Literal physical carrier and ready state

Put the $m$ virtual matter vertices at ((j,0,0)), $0\leq j<m$, one sacrificial leaf at ((j,1,0)) for each (j), and one inert reservoir leaf at ((0,0,1)). Join consecutive matter vertices, each matter vertex to its leaf, and the first matter vertex to the reservoir. As in the native source, physical virtual-vertex positions are doubled and each edge qubit occupies the midpoint. The physical qubit coordinates are

\[
 (2j+1,0,0),\quad (2j,1,0),\quad (0,0,1),
\]

with the corresponding path and leaf ranges. There are (2m+1) virtual vertices and (2m) distinct physical $M_2(\mathbb C)$ factors. The graph is a tree, has degree at most three and has no cycle check. Endpoint-star operators have bounded physical support; a strict nearest-neighbor two-qubit gate implementation is outside this construction's declared control model.

For each vertex, $B_v=\prod_{e\ni v} Z_e$ and $n_v=(1-B_v)/2$. The ordered source operators are $A_{ij}=\epsilon_{ij}X_{ij}\prod_{k<_i j}Z_{ik}\prod_{l<_j i}Z_{jl}$ and $T_{ij}=iA_{ij}(B_i-B_j)/2$. On this tree they represent the even CAR sector of all (2m+1) virtual modes. In particular $\prod_v B_v=I$.

Choose an orthonormal eigenbasis of $h$ with eigenvalues $\epsilon_j$. Set sacrificial leaf (j) initially empty if $\epsilon_j\geq0$ and filled if $\epsilon_j<0$. Since a leaf has one edge, these are literal single-qubit Z preparations. Every other physical edge qubit starts maximally mixed. Denote the resulting ready projector by $P_{\rm ready}$; the density is $P_{\rm ready}/2^m$.

The binary incidence map of a tree bijects edge-bit assignments with vertex occupation patterns of even total parity. Fixing the $m$ sacrificial occupations leaves exactly one assignment for each of the $2^m$ matter occupation patterns: the reservoir occupation is fixed by their parity. Thus $P_{\rm ready}$ has rank $2^m$, and its restriction to the represented even matter algebra is the full maximally mixed Fock functional. The reservoir carries the parity correlation. This identifies the even matter functional; odd matter operators are outside that represented observable algebra.

## Leaf filters and mode rotation

For a matter mode (a) and its leaf (b), $T_{ab}^3=T_{ab}$, so a real hopping pulse with cosine $r\in[0,1]$ is

\[
 U_{ab}=I+(r-1)T_{ab}^2-i\sqrt{1-r^2}\,T_{ab}.
\]

It is unitary. Empty and doubly occupied two-mode states are unchanged; on the singly occupied sector this is a two-state rotation. Consequently, projecting the leaf back onto its **initial** occupation gives $r^{n_a}$ for an empty leaf and $r^{1-n_a}$ for a filled leaf. These are full unnormalized operator contractions. The other physical Z outcome is retained as a failure branch.

To synthesize the required real mode rotation, let $D=n_a-n_b$, $T=T_{ab}$ and $J=i(c_a^\dagger c_b-c_b^\dagger c_a)$. With $R=\exp(-i\pi D/4)$, direct CAR multiplication gives $R^\dagger T R=J$. Hence adjacent (J) rotations are products of the supplied adjacent hopping and difference-phase pulses. Sign conventions are fixed by checking $H=V(\sum_j\epsilon_j n_j)V^\dagger$, rather than choosing a convention from a rotation's name.

Change one eigenvector sign if necessary so the real eigenbasis matrix (O) has determinant (+1). Bottom-up adjacent row elimination reduces (O) to a diagonal sign matrix; reversing those Givens rotations reconstructs (O). The final sign matrix has an even number of minus signs. A pair at $a,b$ is represented by $\exp[i\pi(n_a-n_b)]$, and $n_a-n_b=\sum_{j=a}^{b-1}(n_j-n_{j+1})$. Thus every residual pair is a product of allowed adjacent difference phases. Individual onsite phase control is not an extra resource in this compilation. This constructs $V=\Gamma(O)$ on matter and identity on ancillary occupations.

Apply $V^\dagger$, then each leaf pulse with $r_j=\exp(-\beta|\epsilon_j|/2)$ and its physical Z event, then (V). In the successful branch every leaf returns to its initial value. The contractions commute in the modal frame, and

\[
 \prod_{\epsilon_j\geq0}r_j^{n_j}
 \prod_{\epsilon_j<0}r_j^{1-n_j}
 =c\exp\left(-\frac\beta2\sum_j\epsilon_jn_j\right).
\]

Conjugating gives the target $K_s$. Operator equality on the entire ready domain also gives equality when the input is entangled with an arbitrary reference. For arbitrary ready inputs the result is this filter. The Gibbs conclusion uses the particular mixed ready preparation above.

Each pulse followed by its two projectors is a complete instrument; their sequential composition and the final unitary therefore satisfy $\sum_h K_h^\dagger K_h=P_{\rm ready}$. All $2^m$ leaf outcomes are included, even when a branch has zero weight. Final matter rotations commute with every leaf Z. The incident sacrificial hopping term is deleted after its event, and the original recorded sign remains in the source dictionary. Subsequent operations are restricted to those preserving these Records, as in the conditional event model.

## Output, probability and domain

On $P_{\rm ready}/2^m$, the successful represented matter functional is

\[
 \tau_\beta=\frac{\exp(-\beta H)}{Z_\beta},\qquad
 Z_\beta=\prod_j(1+e^{-\beta\epsilon_j}),\qquad
 p_s=\frac{c^2Z_\beta}{2^m}
     =\prod_j\frac{1+e^{-\beta|\epsilon_j|}}2.
\]

Thus $2^{-m}\leq p_s\leq1$. This is the probability of one heralded attempt under the supplied Born instrument. Failures consume their recorded leaf capacity; repeated attempts require fresh capacity. The construction covers disconnected or vanishing hopping coefficients, eigenvalue degeneracy, zero modes and $\beta=0$. It is stated for finite $\beta\geq0$; general interacting path Hamiltonians, negative or infinite beta, continuum limits and a renewal process are outside this theorem's target. The following separate encoded example has its own domain.

## Encoded two-mode hopping and density example

**Finite target.** On the odd three-active-mode ready domain defined here, six physical edge qubits and three native leaf events implement $K=r\exp[-\log(5/3)(T_{01}+2n_0n_1)]P$, with $r=3/5$, on every ready input.

Use active path 0--1--2, vacant sacrificial leaves 3,4,5 attached to 0,1,2, and a filled inert anchor 6 attached to 0. The virtual positions are $(0,0,0),(1,0,0),(2,0,0),(0,1,0),(1,1,0),(2,1,0),(0,0,1)$. The six physical midpoint qubits are distinct. The graph is a degree-three tree in the same native representation. Prepare

\[
 P=(I-n_3)(I-n_4)(I-n_5)n_6.
\]

The four fixed leaf/anchor values are initially unrecorded physical product preparations; the remaining two edge qubits may carry any state. The rank-four domain has odd active parity. Logical occupations are $n_0,n_1$; their compatible third occupation is $n_2=1-[(n_0+n_1)\bmod2]$. Directly on this domain,

\[
 n_0n_1P=\tfrac12(n_0+n_1+n_2-I)P.
\]

This is an identity on the specified encoding, with a parity mode correlated with the logical labels. The ambient density expression and this restricted quadratic expression are different operators outside that domain. The preparation has supplied a physical encoding; it has not supplied a general many-body interaction primitive.

Let $t=T_{01}$, $D=n_0-n_1$, and $W=\exp(-i\pi D/4)\exp(-i\pi t/4)$. The earlier two-mode CAR identity gives $WDW^\dagger=t$. Total active number commutes with $W$, hence

\[
 W(2n_0+n_2)W^\dagger=t+n_0+n_1+n_2,\qquad
 (t+2n_0n_1)P=(t+n_0+n_1+n_2-I)P.
\]

Apply $W^\dagger$, vacant-leaf hopping pulses with respective cosines $r^2,1,r$, their three physical Z events, and $W$. The successful modal contraction is $r^{2n_0+n_2}$, so these identities prove the finite target. The active path remains connected. All eight leaf outcomes, including zero-weight outcomes at the cosine-one leaf, stay in the complete instrument. The final rotation preserves every leaf Record and the inert anchor. The full operator equality extends to arbitrary reference entanglement on this ready domain; it assumes the actual correlated parity encoding rather than independent fermionic ancillas.

On the product ready density $P/4$, the represented two-mode even-algebra functional is the Gibbs functional of $H_{\rm enc}=t+2n_0n_1$, at $\beta=2\log(5/3)$. Its energies are $0,-1,+1,2$. The Kraus amplitudes on those sectors are $r,1,r^2,r^3$. Consequently

\[
 p=\frac{1+r^2+r^4+r^6}{4}=\frac{6001}{15625},\qquad
 \langle H_{\rm enc}\rangle=-\frac{6071}{12002},\qquad
 \langle t\rangle=-\frac{200}{353}.
\]

This provides a concrete two-mode density/hopping filter in a constrained physical encoding. The density term is quadratic on that encoding. General interacting many-mode dynamics, a different recovery domain and physical energy/work implementation remain separate questions.

## Finite evidence and prior work

The [primary runner](../scripts/native_product_gibbs_preparation_2026_09_08.py) imports all three packet computations. The [exact dimer computation](../scripts/native_product_gibbs_dimer_2026_09_08.py) uses four physical qubits, with matter 0,1, empty leaf 2, filled leaf 3 and reservoir 4. At $r=3/5$, $\beta=2\log(5/3)$, $W=\exp(-i\pi D/4)\exp(-i\pi T/4)$ obeys $WDW^\dagger=T$. The complete success operator is $r\exp[-\log(5/3)T]P_{\rm ready}$. Its success probability is (289/625), conditional hopping expectation is (-8/17), and other leaf outcomes 00,10,11 have probabilities $136/625,64/625,136/625$. The 49 exact assertions concern full operators, outcomes, geometry, ready rank and altered controls.

The [physical path computation](../scripts/native_product_gibbs_path_2026_09_08.py) uses 256-dimensional physical matrices for $m=4$, couplings ((1,2,3)) and ((2,1,2)), and beta 0, 0.7, 2. It executes all 16 outcome maps in all six cells, compares the success operator with an independently exponentiated full physical $H$, and tests paired signs directly. Its 148 assertions supplement the general proof. The tested QR decompositions both have trivial residual signs; six explicit pair tests exercise that helper independently of those decompositions. The two computations have 197 executed assertions; repeated executions do not increase that count.

The [encoded example computation](../scripts/native_product_gibbs_encoded_2026_09_08.py) executes 51 exact checks on complete 64-by-4 physical Kraus columns, all eight outcomes, odd ready parity, the restricted quadratic identity, spectrum and final Record support. Its checks overlap in subject with the other fixtures. The packet executes 248 assertions across three fixtures; this is an execution count, not a count of independent physical claims.

Independent campaign checks reconstruct the dimer in CAR matrices, the general tree incidence argument, and all 96 path outcome maps using bit actions, a CAR/native intertwiner and exterior-power minors instead of the author's QR implementation. These are focused mathematical reviews, not independent audit verdicts. The [canonical execution cache](../logs/runner-cache/native_product_gibbs_preparation_2026_09_08.txt) binds the primary, imported computations and declared source inputs.

Generic Gaussian state preparation and Givens synthesis are established quantum-algorithm tools; see [Jiang et al., Phys. Rev. Applied 9, 044036 (2018)](https://arxiv.org/abs/1711.05395). The contribution here is the explicit native physical edge/leaf Record implementation, its nonthermal product ready resource, parity accounting and complete success/failure map. It is not a claim of a new general Gibbs-preparation algorithm.

## Review and delivery record

Focused independent reviews checked the complete canonical general-path proof, actual source authority and portable computations. The source's one numerical phase pulse was explicitly separated from the arbitrary-angle control condition used here. Forty-six fresh exact corner controls checked incidence, all ready leaf patterns for small paths, zero modes and repeated spectra. A separate reviewer checked the new encoded example and primary inclusion, with seven independent four-state exact controls for its restricted identity, Kraus map and energies. These controls supplement the earlier independent CAR/path reconstruction; reused checks are not recounted as new work.

The complete portable primary directly executed all 248 assertions successfully in about 1.14 seconds with a measured peak RSS of 166.6 MiB on this machine. The declared external timeout is 180 seconds; its internal elapsed-time and 384-MiB RSS checks occur after computation. A later resource failure would remain a failure. The primary imports fresh helper result objects; it is not a cached-result or independent schema verifier.

Ten scratch source mutations failed their intended predicates: halve the native hopping amplitude; collide physical midpoints; exchange a ready leaf value; change a unitary attenuation; duplicate a failure projector; reverse the Givens phase conjugation; remove the paired-sign phase; drop the thermal-prefactor half; alter the thermal energy formula; and change the encoded modal attenuation. The canonical helper hashes, exact substitutions and observed failures are recorded in the packet's mutation record. Mutations changed actual model controls or target formula code, rather than adding a stand-alone assertion that a deliberately wrong formula is wrong.

The original path probe's unused paired-sign mutation survived; direct pair tests were subsequently added and the same mutation then failed. The survivor and historical revisions remain in the research checkpoint. No failed physics criterion was changed to obtain the final path checks. The encoded example corrected an exploratory overextension of Gaussian independent-ancilla reasoning: its correlated parity domain is now explicit, and no general interacting-compiler conclusion is carried here.

All three scientific computations are directly imported by the primary, so no helper-registry policy edit is requested. A later integrated landing must regenerate the citation manifest and pass the shared current-main pipeline, strict lint and changed-evidence gates. No effective grade, audit verdict or main landing is assigned by this author packet.
