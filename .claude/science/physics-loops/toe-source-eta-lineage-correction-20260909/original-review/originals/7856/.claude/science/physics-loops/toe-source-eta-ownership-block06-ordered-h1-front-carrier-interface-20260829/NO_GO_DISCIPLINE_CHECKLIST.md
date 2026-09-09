# No-Go Discipline Checklist

## Scope and status

The only negative claim in Block 06 is:

> No CPTP compression to a single two-dimensional quantum carrier can
> intertwine all three actual Block-03 C32 detector generators, every binary
> effect and Lüders root, on every C32 input state.

This is the **all-state full-family M2 intertwiner** claim.  It is not a claim
against a qubit in one chirality sector, a restricted state family, one
detector direction, a qubit plus a classical chirality bit, M4, C32, ordered
histories, the axioms, or a TOE.  Status: `PASS` at this narrow scope.

Skill freshness was checked against `origin/main` at
`004f64e1c87dad696b282cf2b526f3e7312dc82d`; the newer origin version of the
no-go discipline, including the landed-packet and N5-cache requirements, is
the version applied here.

## N1 — Alternative route enumeration

Approach families are normalized by primary object, load-bearing invariant,
and terminal obligation rather than by notation or agent.

| Family | Honesty | Attack on the negative | Exact outcome |
|---|---|---|---|
| unital CP single-M2 sufficient statistic | `ATTEMPTED` | map one output Pauli triple to all three actual `D_i` and intertwine every root | equality in CP Schwarz makes the triple multiplicative; its scalar M2 volume contradicts the actual rank-16/rank-16 central volume |
| one-chirality qubit projection | `ATTEMPTED` | project to `P_+` or `P_-` and use its M2 factor | succeeds inside one sector but is not trace preserving on arbitrary C32 states; the actual zero-source state has weight one half in each sector and nonzero coherence |
| antiunitary sector identification | `ATTEMPTED` | reverse the orientation of one chiral Pauli triple by transpose/conjugation and merge both sectors into one qubit | the required orientation reversal is an anti-automorphism, not a CP all-state channel; it cannot satisfy the root intertwiner |
| restricted-state qubit statistic | `ATTEMPTED` | preserve only `rho0`, one orbit, or only the displayed two-event cylinders | this can evade an all-state obstruction and remains live for a narrower task, but it does not meet the explicitly quantified all-C32-state target |
| one-axis/commuting detector subfamily | `ATTEMPTED` | carry only a selected `D_eta` in one qubit | a qubit carries that binary algebra, but the construction fails the other two anticommuting generators and proper-cubic closure |
| nonunital Heisenberg map | `ATTEMPTED` | avoid the multiplicative-domain step by dropping unitality | the requested Schrödinger compression is trace preserving, so its dual is unital; dropping this changes the CPTP target |
| qutrit carrier | `ATTEMPTED` | encode both sectors in Hilbert dimension three | the generated algebra is two faithful M2 summands; a faithful Hilbert representation needs dimensions `2+2`, so M3 cannot carry both |
| qubit plus classical chirality bit | `ATTEMPTED` | keep one qubit and retain the sector as an orthogonal classical label | succeeds and is exactly the M4 block-diagonal positive repair; it defeats every broader “no qubit content” claim but not the single-M2 claim |
| unchanged C32 carrier | `ATTEMPTED` | skip compression and compose the writer directly | succeeds algebraically but is not minimal; it remains a valid larger-carrier route and corroborates that the negative is compression-local |

The exact evidence for the attempted families lands in the source note's
“Exact detector algebra,” “Why one M2 cannot carry the full instrument,” and
“The exact four-level sufficient channel” sections and in both runners.  No
prior retained theorem is substituted for the current matrix proof.

## N2 — Wall-independence audit

The raw proof ingredients are not advertised as multiple independent walls.

| Raw item A | Raw item B | Does A close B? | Does B close A? | Disposition |
|---|---|---:|---:|---|
| both chiral central projectors are nonzero | the generated algebra has two M2 summands | yes | yes | one algebraic fact, collapsed |
| all-state effect preservation | all-state root/update preservation | no | yes | root intertwining is stronger; the claim uses the stronger item |
| Schrödinger trace preservation | Heisenberg unitality | yes | yes | dual formulations, collapsed |
| Hilbert dimension two | scalar Pauli central volume | yes | yes | one representation-theoretic fact, collapsed |
| proper-cubic three-direction family | one-axis qubit escape | no | no | the latter changes the target, not a second wall |

After collapse there is one load-bearing contradiction: exact full-family
CPTP M2 sufficiency forces scalar central volume, while the actual detector
has two nonzero central-volume sectors.  M4 closes that contradiction.  Open
arbitrary-history, rate, H2, and action questions are downstream obligations,
not extra walls propping up the M2 theorem.

## N3 — Hidden-wall scan

The source note and runner were scanned for the prescribed phrases and close
variants.

| Hit/class | Classification | Resolution |
|---|---|---|
| “preregistered” / “registration” in packet or runner authority text | non-load-bearing provenance | identifies the frozen target only; it supplies no algebra lemma |
| “the actual Block-03” | cited conditional input | exact generators, roots, and state certificate are bound to Block 03 and its runner cache |
| “finite supplied substrate” | explicit condition, not hidden | promoted in the theorem boundary: generated tape, arbitrary history, and rate remain open |
| “equivalently a qubit plus a classical chirality sector” | proved representation statement | equations (2)--(10) display the direct-sum equivalence |

The note does not use “we assume,” “as is standard,” “naturally,” “obviously,”
“standard QFT,” or an uncited “framework provides” step.  The finite substrate,
front token, Block-03 input, and conditional audit status are explicit.

## N4 — Residual matching

| Cited witness | Witness residual | Current residual | Match? / use |
|---|---|---|---|
| `docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md`, detector/writer sections | actual C32 generator, effect, root, state, and Record objects | algebra and carrier classification of those same objects | yes for object identity; it does not supply the new minimality proof |
| `docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md`, lines 42--62 and 228--239 | all-six permanent-Record readiness cannot create an adjacent blank | type the two-event stencil without that overwrite | no for M2 minimality; retained only as stencil-boundary context |
| `docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md`, lines 48--64 and 266--287 | nontrivial scalar static full-conditionals have curl | construct an ordered quantum-instrument history | no for M2 minimality; retained only as route motivation |
| `docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md`, alternating-square construction | a generic M2 three-outcome front can run at arbitrary length | attach the actual binary C32 H1 instrument | no; used as geometry prior art, never as negative evidence |
| `docs/MINIMAL_AXIOMS_2026-06-29.md`, locality/Admissibility/Record sections | nearest-neighbor conditions and permanent realized Records | semantic typing of live inputs versus output Records | yes for terminology only; no carrier theorem is attributed to the axioms |

After dropping the nonmatching prior residuals, the M2 negative still stands on
the current exact central-volume and multiplicative-domain proof.  No static,
readiness, or generic-front result is cited as if it proved carrier minimality.

## N5 — Rhetoric audit

The phrase “one M2 cannot carry the full instrument” is resolved as follows.

| Resolution | Executed? | Exact scope |
|---|---:|---|
| per element | yes | all three actual C32 generators, both central projectors, eight matrix units, both effects and roots |
| per site | yes | both blank targets, six live inputs per event, the carrier update, bridge, and permanent Record codes |
| per mode | yes | all 24 active masks, six directions, both tested sharpness certificates, and 24 proper cubic rotations |
| per block | yes | the all-state CPTP channel, complete instruments, covariance, two-event cylinders, and prefix marginals |
| lattice-wide | no | arbitrary tape generation, unbounded histories, rate/clock, action selection, H2, gravity, and TOE closure were not executed |

The negative is therefore phrased only at the per-block all-state/full-family
carrier resolution.  It is not broadened to lattice-wide physics.  The primary
cached stdout contains substantive `per_element:`, `per_site:`, `per_mode:`,
`per_block:`, and `lattice_wide:` execution-certificate lines.

## N6 — Partial-closure path scan

Several closure paths avoid any new axiom:

| Path | Status | What it closes |
|---|---|---|
| M4 block carrier / qubit plus chirality bit | executed positive theorem in this block | exact full-family all-state detector and root sufficiency |
| unchanged C32 carrier | already supplied conditionally by Block 03 | compression is unnecessary if minimality is not required |
| state-restricted M2 | live narrower route | may compress a chosen orbit or task but cannot be called the all-state theorem |
| one-axis M2 | exact restricted algebra | binary measurement along one frozen direction only |
| finite live-condition tape | executed for two events | avoids the six-permanent-Record readiness trap without an axiom change |

The current primitive registry is not invoked to supply a hidden dynamics or
carrier premise, and the package does not say “no retained primitive supplies
this.”  The minimal axioms already permit live nearest-neighbor conditions and
separate formation content from site/rate.  Therefore no axiom amendment,
labeling ratification, or owner-governance decision is needed for this bounded
repair.  Extending the tape or selecting a rate would require additional
physics, not a relabeling of the M2 result.

## N7 — Steelman

A hostile reviewer should object that the phrase “no qubit carrier” would be
false: the two chiral sectors each are qubits, the actual task might visit only
a restricted family of states, and a classical chirality label can accompany
one qubit at negligible conceptual cost.  The actionable counterconstruction
is to retain the central projector value, partially trace only the multiplicity
space, and evolve the qubit conditionally in that sector.  That is precisely
the M4/block-diagonal channel proved here.  A still narrower state-restricted
channel might compress further and has not been excluded.  This steelman
defeats a broad qubit no-go, so the shipped negative remains only: a *single
M2 with no chirality label* cannot be an exact all-state full-family sufficient
carrier.  The steelman does not defeat that statement because its successful
construction has two orthogonal M2 sectors.

## N8 — Cross-cycle echo

The repo search found three directly relevant echoes.

| Earlier wall | Later mechanism | Applied here? |
|---|---|---:|
| Source/Eta Block 01 left nonlinear/noncentral M2 and a larger compiler carrier live | Blocks 02--03 moved to the actual C32 operator and explicit Record dilation | yes; this block reduces C32 only after classifying its full algebra |
| Source/Eta Block 04 showed the all-six permanent-Record ready set is cleanup-only | replace surrounding Records by live quantum conditions and carry a front token | yes; both targets are blank and all eta inputs are explicitly live |
| Source/Eta Block 05 showed the scalar static full-conditional reading fails | use an ordered quantum instrument with a carried post-measurement state | yes; equations (19)--(22) are the exact two-event ordered repair |

Historical repo negatives that said a carrier or law “requires a new axiom”
were often retired by a richer state, a typed interface, or a convention
separation.  The same lesson is applied rather than ignored: the M2 statement
is narrowed, M4 is constructed immediately, and no axiom-necessity claim is
made.

## Verdict

`PASS` for the narrow all-state full-family M2 intertwiner theorem.

- N1 contains nine materially distinct families and identifies two successful
  larger/narrower counterroutes.
- N2 collapses the proof to one central-volume contradiction.
- N3 exposes the supplied finite substrate and conditional imports.
- N4 drops nonmatching static/readiness/generic-front residuals.
- N5 limits rhetoric to the executed carrier block.
- N6 executes the M4 partial-closure path without an axiom edit.
- N7 defeats every broader “no qubit” wording.
- N8 applies the repo's earlier enlarged-state and ordered-process repairs.

The checklist and the primary runner's five-resolution stdout certificate land
in the same branch as the negative statement.
