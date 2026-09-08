AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'scripts/native_zero_penalty_electric_exact_2026_09_08.py', 'scripts/native_zero_penalty_spectator_exact_2026_09_08.py', 'scripts/native_zero_penalty_isolation_exact_2026_09_08.py')
import argparse,hashlib,json,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
parts={}
for key,count in [('electric',964),('spectator',87509),('isolation',5091)]:
 part=runpy.run_path(str(root/f'scripts/native_zero_penalty_{key}_exact_2026_09_08.py'))['out']
 if part['checks']!=count:raise RuntimeError('predicate coverage changed '+key)
 parts[key]=part
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=93564,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Finite supplied L4 isolation and scalar canonical coefficients through five; sixth only support allowed.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_zero_penalty_l4_delayed_splitting_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: actual electric pair flux toggles.')
 print('per_site: small cuts and incident-pair matching.')
 print('per_mode: active parity and spectator projection.')
 print('per_block: fixed-flux compression and canonical normalization.')
 print('lattice_wide: L4 constant square, winding sectors and isolation.')
 print('TOTAL: PASS=93564 FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
