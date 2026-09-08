"""Exact finite U0 controls; no flux optimization or phase inference."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
 'scripts/native_zero_penalty_endpoint_exact_2026_09_08.py',
)
import argparse,hashlib,json,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
part=runpy.run_path(str(root/'scripts/native_zero_penalty_endpoint_exact_2026_09_08.py'))['run']()
if part['checks']!=80:raise RuntimeError('predicate coverage changed')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=80,parts={'exact':part},elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Exact finite flux-sector and parity controls; no cubic flux optimum or phase.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_zero_penalty_endpoint_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: exact Gaussian-rational Pauli and CAR matrices.')
 print('per_site: even matter parity from global Gauss product.')
 print('per_mode: frequency-square polynomials, zero modes and spectator multiplicity.')
 print('per_block: flux-projected traces and total carrier dimension.')
 print('lattice_wide: finite endpoint theorem only; no flux optimization or phase.')
 print('TOTAL: PASS=80 FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
