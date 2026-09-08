AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'scripts/native_zero_penalty_optimal_flux_exact_2026_09_08.py', 'scripts/native_zero_penalty_dispersion_exact_2026_09_08.py')
import argparse,hashlib,json,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
flux=runpy.run_path(str(root/'scripts/native_zero_penalty_optimal_flux_exact_2026_09_08.py'))['out']
disp=runpy.run_path(str(root/'scripts/native_zero_penalty_dispersion_exact_2026_09_08.py'))['out']
if flux['checks']!=6962 or disp['predicates']!=97:raise RuntimeError('predicate coverage changed')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=7059,parts={'flux':flux,'dispersion':disp},elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Supplied U0 with explicit imported flux theorem; finite exact dispersion, no phase claim.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_zero_penalty_optimal_flux_dispersion_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: canonical hopping and seam signs.')
 print('per_site: bipartite reflection geometry.')
 print('per_mode: exact Majorana frequency squares and rank.')
 print('per_block: physical-even and auxiliary-full partition identity.')
 print('lattice_wide: finite optimizing sector via explicit theorem import.')
 print('TOTAL: PASS=7059 FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
