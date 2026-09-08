"""Fresh bounded exact sixth-order coefficients and full-carrier sign witnesses."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_SIXTH_OFFDIAGONAL_SIGN_OBSTRUCTION_NOTE_2026-09-08.md',
 'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
 'scripts/native_sixth_coefficients_2026_09_08.py',
 'scripts/native_sixth_normalization_2026_09_08.py',
 'scripts/native_sixth_l4_2026_09_08.py',
 'scripts/native_sixth_l6_2026_09_08.py',
)
import argparse,contextlib,hashlib,io,json,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];(root/'outputs').mkdir(exist_ok=True)
inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS};parts={}
for kind,count in [('coefficients',3653),('normalization',4),('l4',9),('l6',9)]:
 with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(root/f'scripts/native_sixth_{kind}_2026_09_08.py'))
 parts[kind]=json.loads((root/f'outputs/native_sixth_{kind}_2026_09_08.json').read_text())
 if parts[kind]['checks']!=count:raise RuntimeError('predicate count '+kind)
bindings=0
def need(v,m):
 global bindings
 bindings+=1
 if not v:raise RuntimeError(m)
for row,value in zip(parts['coefficients']['rows'],['-3/2','-89/48','-89/48']):need(row['H']['6'][0][1]==value,'absolute canonical coefficient')
need(parts['coefficients']['six_cycle_amplitude']=='-3/8','absolute sixth cycle')
need(parts['normalization']['forward4']==[['2','5/8'],['5/8','1/4']],'absolute metric normalization')
for kind in ['l4','l6']:need(parts[kind]['witness']['effective_edge_signs']==[-1,1,1,1],'actual signed history')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=sum(v['checks'] for v in parts.values())+bindings,absolute_binding_predicates=bindings,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Exact finite canonical H6 and diagonal-phase obstruction; no arbitrary basis, phase, thermodynamic radius or audit verdict.')
(root/'outputs/native_sixth_offdiagonal_sign_obstruction_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: exact canonical rank-two sixth coefficients and all720 cycle orders.')
 print('per_site: all delivered L4/L6 ice states and local face supports.')
 print('per_mode: wave-operator metric and generic noncommuting normalization.')
 print('per_block: full signed histories and negative four-step product.')
 print('lattice_wide: fixed finite analytic diagonal-gauge obstruction only.')
 print(f'TOTAL: PASS={r["executed_predicates"]} FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
