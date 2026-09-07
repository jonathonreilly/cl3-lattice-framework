"""Reproduce both paths and mutate only scratch copies of the source runners."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

PACK = Path(__file__).resolve().parent
ROOT = PACK.parents[4]
PRIMARY = ROOT/'scripts/spin_half_cartesian_plaquette_source_2026_09_07.py'
INDEPENDENT = ROOT/'scripts/spin_half_cartesian_plaquette_source_independent_check_2026_09_07.py'
ENV = dict(os.environ, OPENBLAS_NUM_THREADS='1')
results = {}
for name, source in [('primary', PRIMARY), ('independent', INDEPENDENT)]:
    command = [sys.executable, str(source), '--json', str(PACK/f'{name}.json')]
    run = subprocess.run(command, cwd=ROOT, env=ENV, text=True, capture_output=True, timeout=60)
    (PACK/f'{name}.log').write_text(run.stdout+run.stderr)
    if run.returncode:
        raise RuntimeError(f'{name} baseline failed: {run.returncode}')
    results[name] = dict(command=command, returncode=run.returncode,
                         sha256=hashlib.sha256(source.read_bytes()).hexdigest())
p = json.loads((PACK/'primary.json').read_text())
i = json.loads((PACK/'independent.json').read_text())
max_difference = max(abs(row['curvature']-i['curvatures'][f"{row['source']}_V{row['V']:.2f}"]['K'])
                     for row in p['curvatures'])
trace_derivatives = {name: -sum(int(power)**2*coefficient for power, coefficient in polynomial.items())
                     for name, polynomial in i['trace_H4_V1'].items()}
if max_difference >= 1e-10 or trace_derivatives != p['trace_H4_second_derivatives']:
    raise RuntimeError('Independent response/trace comparison failed')
results['cross_check'] = dict(max_curvature_difference=max_difference,
                              trace_H4_second_derivatives=trace_derivatives)
mutations = [
    ('primary_drop_source_parity', PRIMARY,
     '"cartesian_curl": epsilon * signs * target', '"cartesian_curl": signs * target'),
    ('primary_drop_general_source_parity', PRIMARY,
     'phases = epsilon * signs * np.asarray(face_source)[face_ids]',
     'phases = signs * np.asarray(face_source)[face_ids]'),
    ('primary_reverse_one_boundary_edge', PRIMARY,
     'BOUNDARY = np.array([1, 1, -1, -1]', 'BOUNDARY = np.array([1, 1, -1, 1]'),
    ('primary_omit_full_flux_seam', PRIMARY,
     'flux_a[i] = -theta_quantum * 2 * root[1]', 'flux_a[i] = 0.'),
    ('primary_wrong_response_relaxation_sign', PRIMARY,
     'curvature = bare - relaxation', 'curvature = bare + relaxation'),
    ('independent_drop_source_parity', INDEPENDENT,
     'cartesian.append(eps(r)*s if (a,b)==(0,1) else 0)',
     'cartesian.append(s if (a,b)==(0,1) else 0)'),
    ('independent_omit_full_flux_seam', INDEPENDENT,
     'link_a[k]=-tquant*L*r[1]', 'link_a[k]=0.'),
]
mutant_dir = PACK/'mutants'
mutant_dir.mkdir(exist_ok=True)
results['mutations'] = []
for name, source, old, new in mutations:
    text = source.read_text()
    if text.count(old) != 1:
        raise RuntimeError(f'{name}: mutation target count {text.count(old)}')
    target = mutant_dir/f'{name}.py'
    target.write_text(text.replace(old, new))
    command = [sys.executable, str(target)]
    run = subprocess.run(command, cwd=ROOT, env=ENV, text=True, capture_output=True, timeout=60)
    (mutant_dir/f'{name}.log').write_text(run.stdout+run.stderr)
    failures = [line for line in run.stdout.splitlines() if line.startswith('[FAIL]')]
    detected = run.returncode != 0 and bool(failures)
    results['mutations'].append(dict(name=name, returncode=run.returncode, detected=detected,
                                     failure_labels=failures, command=command))
    if not detected:
        raise RuntimeError(f'{name}: mutation did not produce a scientific check failure')
(PACK/'verification.json').write_text(json.dumps(results, indent=2)+'\n')
print('Cross-method curvature maximum difference:', max_difference)
print('Exact independent trace derivatives:', trace_derivatives)
print('Detected scientific mutations:', len(mutations))
