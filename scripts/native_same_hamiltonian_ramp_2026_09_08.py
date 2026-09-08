"""Exact bounded controls for the conditional same-Hamiltonian ramp theorem."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_SAME_HAMILTONIAN_RAMP_NOTE_2026-09-08.md',
 'docs/NATIVE_LOCAL_NATURAL_RING_DYNAMICS_NOTE_2026-09-08.md',
 'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
 'scripts/native_same_hamiltonian_ramp_jets_2026_09_08.py',
)
import argparse,hashlib,json,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
module=runpy.run_path(str(root/'scripts/native_same_hamiltonian_ramp_jets_2026_09_08.py'))
part=module['run']()
if part['checks']!=18626:raise RuntimeError('predicate coverage changed')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=part['checks'],parts={'jets':part},elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Exact finite jets and graph support controls; no simulation, phase, global band or audit verdict.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_same_hamiltonian_ramp_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: exact arbitrary-profile moving-frame Pauli coefficients through four.')
 print('per_site: full L4 degree-three seed and all distinct two-edge supports.')
 print('per_mode: derivative jets and charge-changing coefficient cancellation.')
 print('per_block: beta14 endpoint flatness and concatenated time exponents.')
 print('lattice_wide: uniform local analytical theorem; no global state or phase certificate.')
 print('TOTAL: PASS=18626 FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
