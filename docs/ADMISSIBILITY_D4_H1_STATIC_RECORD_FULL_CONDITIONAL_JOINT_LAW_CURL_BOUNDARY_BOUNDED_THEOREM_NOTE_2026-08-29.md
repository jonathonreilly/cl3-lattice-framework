---
claim_id: admissibility_d4_h1_static_record_full_conditional_joint_law_curl_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "For the displayed 24-mask active set, assign common positive odds t to active environments and neutral odds 1 elsewhere. If t is not 1, 4032 of 6144 adjacent-site square conditions fail, in every direction, so this supplied scalar table is not the full-conditional family of a positive static binary joint law. More generally, square-compatible log-odds on all 64 environments are a constant plus three reciprocal-axis count terms; requiring equality on the active set kills all three slopes, leaving a constant law. A nonzero cubic germ only implies t(e) differs from 1 in some sufficiently small punctured neighborhood; it does not prove the condition across the full inherited positivity interval."
upstream_dependencies:
  - admissibility_d4_affine_lineage_binary_record_multi_join_repeatability_selector_boundary_bounded_theorem_note_2026-08-29
runner: scripts/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py
independent_checker: scripts/independent_admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py
status: proposed_retained
actual_current_surface_status: bounded-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Conditional static joint-law curl boundary

**Date:** 2026-08-29
**Corrected:** 2026-09-09
**Type:** `bounded_theorem`
**Standing:** author-side `proposed_retained`; no formal audit has run.

Primary runner:
[`admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py`](../scripts/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py).
Independent checker:
[`independent_admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py`](../scripts/independent_admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py).

## Exact conditional obstruction

Use the explicit active set `A` displayed in the preceding
[affine-lineage note](ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md).
Consider the supplied scalar full-conditional odds table

```text
o(eta)=t  if eta in A,
o(eta)=1  otherwise,                                  (1)
```

with `t>0`. On an edge in direction `d`, compare the two orders of flipping
the endpoint bits while holding the two five-bit exterior environments fixed.
The ratio of the two path products is `t^Delta`, where

```text
Delta = 1_A(x0)+1_A(y1)-1_A(y0)-1_A(x1).              (2)
```

The exact census over six directions and `32*32` exterior pairs per direction
is

```text
Delta=0: 2112;  Delta=1: 1152;  Delta=-1: 1152;
Delta=2: 864;   Delta=-2: 864.                         (3)
```

Therefore, **if and only if the supplied active odds are nonneutral,
`t != 1`**, the 4032 nonzero-Delta squares obstruct a positive static binary
joint law with (1) as its full conditionals. At `t=1` every square closes.

The historical parent supplied a nonzero cubic coefficient in
`t(e)-1`. This block did not recompute that coefficient. Analyticity and a
nonzero leading cubic term imply only that there is an `epsilon>0` such that
`t(e)!=1` for `0<|e|<epsilon`. They do not exclude additional zeros all the
way to the parent's `10^-9` positivity endpoint. The obstruction is thus
stated directly under `t!=1`, with only a sufficiently small punctured germ
following from the supplied cubic datum.

## Compatible extensions

Write an arbitrary log-odds function on the 64 environments in its unique
Boolean multilinear basis. Independence of each bit derivative from the
other five bits kills all 57 coefficients of degree at least two. Equality
of the two endpoint derivatives on each undirected axis adds three independent
relations between the six linear coefficients. The compatible space is

```text
ell(eta)=c + a_x(eta_-x+eta_+x)
             + a_y(eta_-y+eta_+y)
             + a_z(eta_-z+eta_+z).                   (4)
```

The active set realizes six axis-count triples. Their differences have rank
three, so requiring `ell` to have one common value on all active masks forces
`a_x=a_y=a_z=0`. The active-preserving compatible extensions are exactly the
constant laws. This classification includes the neutral case and is not
invalidated when the specific obstruction (1) vanishes.

This is a static scalar compatibility result. Ordered instruments, hidden
states, enlarged carriers, formation hazards, and nonstatic histories remain
open. It gives no physical no-go, axiom defect, gravity result, formal audit
verdict, or TOE movement.

## Reproduction

```bash
python3 scripts/cached_runner_output.py --refresh scripts/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py
python3 scripts/cached_runner_output.py --refresh scripts/independent_admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py
```
