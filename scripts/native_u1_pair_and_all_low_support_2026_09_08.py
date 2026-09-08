"""Exact finite pair-phase and constructive support controls."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_U1_PAIR_OPERATOR_AND_ALL_LOW_SUPPORT_NOTE_2026-09-08.md', 'docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md', 'scripts/native_u1_pair_support_pair_author_2026_09_08.py', 'scripts/native_u1_pair_support_pair_independent_2026_09_08.py', 'scripts/native_u1_pair_support_support_author_2026_09_08.py', 'scripts/native_u1_pair_support_support_independent_2026_09_08.py', '.claude/science/physics-loops/native-u1-pair-and-all-sector-support-20260908/inputs/GLOBAL_D4_SEED.json')
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS}
parts={}
for kind in ('pair_author','pair_independent','support_author','support_independent'):
 captured=io.StringIO()
 with contextlib.redirect_stdout(captured):runpy.run_path(str(root/'scripts'/f'native_u1_pair_support_{kind}_2026_09_08.py'))
 parts[kind]=json.loads(captured.getvalue())
 if parts[kind]['executed_predicates']<=0:raise RuntimeError('empty helper predicates')
if parts['pair_author']['nonbacktracking_two_edge_paths']!=24596:raise RuntimeError('pair composition coverage')
if parts['pair_independent']['pair_columns']!=3292 or parts['pair_independent']['forbidden_columns']!=532:raise RuntimeError('independent pair coverage')
if parts['support_author']['A_exchange_phase']!=-1 or parts['support_independent']['phase']!=-1:raise RuntimeError('closed phase')
if len(parts['support_independent']['all_ordered_pair_routes'])!=100:raise RuntimeError('independent route coverage')
def finite(x):
 if isinstance(x,float) and not math.isfinite(x):raise RuntimeError('nonfinite output')
 if isinstance(x,dict):
  for v in x.values():finite(v)
 if isinstance(x,(list,tuple)):
  for v in x:finite(v)
finite(parts)
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
count=sum(x['executed_predicates'] for x in parts.values())
out=dict(executed_predicates=count,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Selected exact operator columns and constructive routes; general proofs conditional, no physics selection or audit verdict.')
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/native_u1_pair_and_all_low_support_2026_09_08.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
print(json.dumps(out,indent=2,allow_nan=False))
if not args.json:
 print('per_element: oriented native A and signed pair/hopping CAR columns, including forbidden toggles.')
 print('per_site: no-double and integer Gauss support on both sublattices.')
 print('per_mode: explicit two-species adjoint and off-D block-phase comparisons.')
 print('per_block: actual L4 composed paths and independent relabeled native columns.')
 print('lattice_wide: constructive low-domain paths on L4 and K6,6, with closed minus witnesses.')
 print(f'TOTAL: PASS={count} FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s RSS384MiB.')
