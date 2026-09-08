"""Live finite controls for the supplied native virtual-pair mechanism."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md',
    'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
    'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'scripts/native_virtual_pair_fourth_2026_09_08.py',
    'scripts/native_virtual_pair_sixth_local_2026_09_08.py',
    'scripts/native_virtual_pair_sixth_global_2026_09_08.py',
    'scripts/native_virtual_pair_full_fourth_2026_09_08.py',
    'scripts/native_virtual_pair_full_sixth_local_2026_09_08.py',
    'scripts/native_virtual_pair_full_sixth_global_2026_09_08.py',
    'scripts/native_virtual_pair_remainder_2026_09_08.py',
    '.claude/science/physics-loops/native-virtual-pair-ring-mechanism-20260908/inputs/FOUR_ICE_BACKGROUNDS.json',
)
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
parts={}
for kind,expected in (('fourth',55576),('sixth_local',456),('sixth_global',182),('remainder',14),('full_fourth',55576),('full_sixth_local',499),('full_sixth_global',186)):
    captured=io.StringIO()
    with contextlib.redirect_stdout(captured):runpy.run_path(str(root/'scripts'/f'native_virtual_pair_{kind}_2026_09_08.py'))
    parts[kind]=json.loads(captured.getvalue())
    if parts[kind]['checks']!=expected:raise RuntimeError('predicate coverage changed')
background_path=root/AUDIT_INPUT_PATHS[-1];background=json.loads(background_path.read_text())
if background!={k:parts['fourth'][k] for k in ('vertices','edges','background_bits')}:raise RuntimeError('actual background input mismatch')
def finite(x):
    if isinstance(x,float) and not math.isfinite(x):raise RuntimeError('nonfinite result')
    if isinstance(x,dict):
        for v in x.values():finite(v)
    if isinstance(x,(list,tuple)):
        for v in x:finite(v)
finite(parts)
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if seconds>=180 or not 0<rss<384:raise RuntimeError('resource cap')
count=sum(p['checks'] for p in parts.values())
result=dict(executed_predicates=count,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Exact finite mechanism controls, not whole-Hilbert enumeration, a phase certificate or audit status.')
(root/'outputs').mkdir(exist_ok=True);(root/'outputs/native_virtual_pair_ring_mechanism_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
    print('per_element: all24 native plaquette orders and repeated-edge diagonal denominators.')
    print('per_site: explicit hard/full-domain comparison and degree-three motif counts.')
    print('per_mode: exact finite forest series and scalar remainder arithmetic; no spectrum census.')
    print('per_block: four literal L4 backgrounds and separately declared finite cluster patterns.')
    print('lattice_wide: finite-volume proofs only; a depends on the total perturbation norm.')
    print(f'TOTAL: PASS={count} FAIL=0')
    print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
