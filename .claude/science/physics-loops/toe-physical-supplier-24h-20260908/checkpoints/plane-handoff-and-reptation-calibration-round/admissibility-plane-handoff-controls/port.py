from pathlib import Path
import shutil
src=Path('/private/tmp/toe-24h-probes-20260908/admissibility-plane-handoff-controls')
w=Path('/private/tmp/toe-admissibility-plane-formation-20260908')
pack=w/'.claude/science/physics-loops/admissibility-plane-formation-20260908'
(pack/'evidence/original').mkdir(parents=True,exist_ok=True)
for n in ['PREREGISTRATION.md','DERIVATION.md','check.py','result.json','HASHES.json','SOURCE_BINDING.md']:shutil.copy2(src/n,pack/'evidence/original'/n)
note='ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md'
runner='admissibility_plane_formation_diagonal_interaction_2026_09_08.py'
parent='ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md'
header=f'''---
claim_id: admissibility_plane_formation_diagonal_interaction_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "For the supplied positive six-state orbit product rule, finite monotone rectangle laws extend consistently to a translation-invariant plane law with explicit axial and diagonal pair interactions. The two diagonal classes differ exactly for nonconstant weights. This is not selection of a physical formation order or identification with a Gaussian instrument."
upstream_dependencies:
  - admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07
runner: scripts/{runner}
---

# The plane formation law and its diagonal interaction

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

The supplied monotone formation rule defines a consistent probability law on the whole plane. Its exact interaction includes a diagonal pair term contributed by the local normalizers. This identifies the resulting classical law, while leaving physical order selection and quantum-instrument identification open.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact conditional probability theorem for the stated positive product-rule family."
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Supply a physical law or instrument identification rather than identifying distinct probability objects by terminology."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and prior work

The [monotone rectangle parent]({parent}), P1–P2 and P7(a), supplies the locally normalized product rule and rectangle density. Its opposite-corner identity is prior work, not a new result here. Labels are the six Bloch-axis menu points; weights are $p$ for identical labels, $q$ for antipodal labels and $r$ otherwise, with $p,q,r>0$. Write $Z=p+q+4r$, $K=\\phi/Z$ and $H=K^2$. No numerical value of these parameters is selected. This note needs no Gaussian-instance premise.

The extension and finite-range conditional arguments use standard probability mathematics. Relevant prior art includes [Pickard (1980)](https://doi.org/10.2307/1426425) and [Champagnat and collaborators](https://pagesperso.ls2n.fr/~idier-j/pub/pubC/Champagnat98C.pdf). These references were supplied as prior-art pointers; their full papers were not read for this proof, and no theorem from them is a load-bearing shortcut. No historical novelty is claimed.

'''
body=(src/'DERIVATION.md').read_text();body=body[body.index('Let K be'):]
body=body.replace('Let K be the positive symmetric stochastic six-state orbit kernel, H=K². Current block05 proves the rectangle density','Let $K$ be the positive symmetric stochastic six-state orbit kernel and $H=K^2$. The parent proves the rectangle density')
body=body.replace('mu_R(x)=(1/6) product_{nearest-neighbor edges in R} K(x_u,x_v) / product_{unit squares in R} H(x_SW,x_NE).',r'\[\mu_R(x)=\frac16\frac{\prod_{\{u,v\}\in E(R)}K(x_u,x_v)}{\prod_{\square\subset R}H(x_{\rm SW},x_{\rm NE})}.\]')
body=body.replace('mu(z | boundary) is proportional to product_{four axial neighbors v} K(z,x_v) / [H(z,x_NE) H(z,x_SW)].',r'\[\mu(z\mid\partial)=\frac1{Z(\partial)}\frac{\prod_{v\text{ axial neighbor}}K(z,x_v)}{H(z,x_{\rm NE})H(z,x_{\rm SW})}.\]')
body=body.replace('This all-parameter extension is analytic and requires independent review; the current parent only asserts its executed distinctness fixtures.','This all-parameter statement extends the parent’s executed distinctness fixtures.')
body=body.replace('Current main','The parent').replace('main.','the parent.')
extra='''
## No-Go Discipline Gate

N1: The affirmative target is the projective plane law and its explicit interaction; the comparison concerns only the supplied product-rule family. N2: No statement excludes other order classes, readouts or instruments. N3: The constant rule is an adverse boundary and gives the uniform law. N4: All local weights are positive, so the conditioning witness has positive probability. N5: Executed resolution classes are printed by the runner; no complete plane census is claimed. N6: Original proof and controls are preserved in the packet. N7: Choosing a different physical formation law remains outside the theorem. N8: The result does not retire the action-identification obligation or select an axiom-level process.

## Verification and imports

The [live exact runner](../scripts/'''+runner+''') uses Python integer and rational arithmetic for all probability calculations. Floating values report resources only. It checks complete 2×3 laws and their subrectangles at three frozen triples, exact six-value center conditionals, and 96 trimming schedules; schedules are not complete 3×3 or 3×4 marginal enumeration. Infinite consistency and the conditional specification rest on the proof above. The sole mathematical source dependency is the linked parent; finite-alphabet extension and conditional-expectation convergence are explicit standard mathematical imports proved applicable above.

[Durable original evidence](../.claude/science/physics-loops/admissibility-plane-formation-20260908/evidence/original/DERIVATION.md) preserves the pre-port derivation and exact read-coverage disclosure. Independent review and adverse executions are recorded in the same packet. No audit verdict is authored here.
'''
(w/'docs'/note).write_text(header+body+extra)
code=(src/'check.py').read_text()
code=code.replace('start=time.monotonic();signal.alarm(180)',f'''AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/{note}', 'docs/{parent}')
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
import argparse
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}}''')
code=code.replace('require(mib<384)','require(0<mib<384 and time.monotonic()-start<180)')
code=code.replace("print(json.dumps(dict(checks=checks,fixtures=out", "result=dict(checks=checks,fixtures=out")
code=code.replace('peak_MiB=mib),indent=2,allow_nan=False))',"peak_MiB=mib, input_sha256=inputs, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())\nprint(json.dumps(result,indent=2,allow_nan=False))\nif not args.json:\n print('per_element: exact six-label probabilities and positive center conditioning.')\n print('per_site: all subrectangle positions of the complete2x3 laws.')\n print('per_mode: no continuum or quantum mode claim; three orbit-weight fixtures.')\n print('per_block: complete46656 configuration laws;96 symbolic trimming schedules.')\n print('lattice_wide: plane extension is analytic, not numerically enumerated.')\n print(f'TOTAL: PASS={checks} FAIL=0')\n print(f'Resources: {result[\"seconds\"]:.6f}s, {mib:.3f}MiB; caps180s384MiB.')")
(w/'scripts'/runner).write_text(code)
(pack/'PORT_SCOPE.md').write_text('Fresh base8257bddfc9. Staging only; root owns commits/publication. No pipeline, strict lint, changed-evidence, graph or authority modifications. Original163-check scientific calculation retained; wrapper adds CLI, source hashes and resource enforcement. Historical handoff four-law statement already corrected on main; no duplicate repair claim.\n')
