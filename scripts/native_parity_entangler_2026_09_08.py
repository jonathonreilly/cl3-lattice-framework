"""Live finite operator evidence for the conditional native parity entangler."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_PARITY_ENTANGLER_AND_CHSH_NOTE_2026-09-08.md',
    'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/native_parity_entangler_numeric_2026_09_08.py',
    'scripts/native_parity_entangler_exact_2026_09_08.py',
)
from pathlib import Path
import os,time,signal,resource,contextlib,io,runpy,json,hashlib,argparse
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[variable]='1'
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1];(root/'outputs').mkdir(exist_ok=True);parts={}
for name in ('numeric','exact'):
    with contextlib.redirect_stdout(io.StringIO()):
        namespace=runpy.run_path(str(root/'scripts'/f'native_parity_entangler_{name}_2026_09_08.py'))
    data=namespace['result']
    if data['status']!='PASS' or not data['checks'] or any(type(v) is not bool or not v for v in data['checks'].values()):
        raise RuntimeError('incomplete live evidence')
    parts[name]=data
seconds=time.monotonic()-start
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=AUDIT_TIMEOUT_SEC:raise RuntimeError('resource contract')
result={'status':'PASS','classification':'conditional-support','parts':parts,'executed_assertions':sum(len(v['checks']) for v in parts.values()),'elapsed_seconds':seconds,'peak_rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite native physical matrix construction; preparation, signed hopping controls, Born Record schedule and CHSH settings supplied. Nonbridge lemma is analytic.'}
(root/'outputs/native_parity_entangler_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
    print('per_element: the middle physical Z event retains both outcomes.')
    print('per_site: supplied edge-midpoint placement; no new one-site primitive.')
    print('per_mode: four modes with even parity, regrouped dual rails.')
    print('per_block: three physical qubits, full four-column success map and local CHSH settings.')
    print('lattice_wide: no scaling, formation-law or universal-gate conclusion.')
    print(f"TOTAL: PASS={result['executed_assertions']} FAIL=0")
    print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
