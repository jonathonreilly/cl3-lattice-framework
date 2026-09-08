"""Fresh exact full-carrier eighth diagonal dataflow."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_EIGHTH_DIAGONAL_CYCLE_POTENTIAL_NOTE_2026-09-08.md',
 'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
 'scripts/native_eighth_local_2026_09_08.py',
 'scripts/native_eighth_global_2026_09_08.py',
 'scripts/native_eighth_combined_2026_09_08.py',
 'scripts/native_eighth_witness_2026_09_08.py',
)
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];(root/'outputs').mkdir(exist_ok=True)
inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS};parts={}
for kind,count in [('local',591),('global',541533),('combined',112),('witness',21)]:
 capture=io.StringIO()
 with contextlib.redirect_stdout(capture):runpy.run_path(str(root/f'scripts/native_eighth_{kind}_2026_09_08.py'))
 parts[kind]=json.loads((root/f'outputs/native_eighth_{kind}_2026_09_08.json').read_text())
 if parts[kind]['checks']!=count:raise RuntimeError('changed predicate count '+kind)
# Independent reviewed absolute values bind upstream tables to the final witness.
bindings=0
def need(value,label):
 global bindings
 bindings+=1
 if not value:raise RuntimeError(label)
need(parts['combined']['C_tree']=='3610233/16000','absolute tree scalar')
for word,value in [('0000','-99/1600'),('0001','-10019/108000'),('0011','-11/144'),('0101','5/32')]:
 need(parts['combined']['W'][word]==value,'absolute cycle class '+word)
for row,value in zip(parts['witness']['results'],['-1769/3375','-1769/9000']):
 need(row['determinant']==value,'absolute global determinant')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
r=dict(executed_predicates=sum(v['checks'] for v in parts.values())+bindings,absolute_binding_predicates=bindings,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Exact canonical eighth diagonal, motif reduction and finite same-component witness; not full H8 offdiagonal, phase or audit verdict.')
(root/'outputs/native_eighth_diagonal_cycle_potential_2026_09_08.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n');print(json.dumps(r,indent=2,allow_nan=False))
if not args.json:
 print('per_element: full-carrier native active-cluster eighth-order coefficients.')
 print('per_site: exact degree-three motif counts and full delivered ice states.')
 print('per_mode: rank-two low-band trace and native cycle symmetry.')
 print('per_block: exact scalar, cycle decomposition and affine determinants.')
 print('lattice_wide: finite graph identities; no thermodynamic or phase conclusion.')
 print(f'TOTAL: PASS={r["executed_predicates"]} FAIL=0')
 print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
