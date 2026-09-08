"""Bounded exact controls for local native natural-ring dynamics."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
 'docs/NATIVE_LOCAL_NATURAL_RING_DYNAMICS_NOTE_2026-09-08.md',
 'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
 'scripts/native_local_ring_matrix_2026_09_08.py',
 'scripts/native_local_ring_harmonics_2026_09_08.py',
 'scripts/native_local_ring_constants_2026_09_08.py',
)
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
parts={}
for kind,expected in (('matrix',147),('harmonics',10917),('constants',26)):
 captured=io.StringIO()
 with contextlib.redirect_stdout(captured):runpy.run_path(str(root/'scripts'/f'native_local_ring_{kind}_2026_09_08.py'))
 parts[kind]=json.loads(captured.getvalue())
 if parts[kind]['checks']!=expected:raise RuntimeError('predicate coverage changed')
def finite(x):
 if isinstance(x,float) and not math.isfinite(x):raise RuntimeError('nonfinite output')
 if isinstance(x,dict):
  for v in x.values():finite(v)
 if isinstance(x,(list,tuple)):
  for v in x:finite(v)
finite(parts)
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
count=sum(p['checks'] for p in parts.values())
r=dict(executed_predicates=count,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Exact finite algebra, geometry and constant controls. Not a simulation, phase certificate, global band or audit verdict.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_local_natural_ring_dynamics_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: actual fourteen-step native matrix coefficients and folded ring comparison.')
 print('per_site: all2048 endpoint-star inputs and explicit L4/L6 support geometry.')
 print('per_mode: input-column charge harmonics and charge-conserving effective coefficients.')
 print('per_block: exact finite majorants, analytic radius and two-comparison time powers.')
 print('lattice_wide: uniform local proof only; no global ice-band or phase inference.')
 print(f'TOTAL: PASS={count} FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
