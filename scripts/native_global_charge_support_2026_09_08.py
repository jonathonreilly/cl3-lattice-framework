"""Live bounded finite controls; the general proofs are in the paired note."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08.md',
    'docs/NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md',
    'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
    'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'scripts/native_global_charge_reachability_2026_09_08.py',
    'scripts/native_global_charge_connectivity_2026_09_08.py',
    'scripts/native_global_charge_exchange_2026_09_08.py',
)
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS}
parts={}
for kind,expected in (('reachability',328177),('connectivity',78),('exchange',102)):
    captured=io.StringIO()
    with contextlib.redirect_stdout(captured):
        runpy.run_path(str(root/'scripts'/f'native_global_charge_{kind}_2026_09_08.py'))
    parts[kind]=json.loads(captured.getvalue())
    if parts[kind]['checks']!=expected:raise RuntimeError('changed finite predicate coverage')
def finite(obj):
    if isinstance(obj,float) and not math.isfinite(obj):raise RuntimeError('nonfinite output')
    if isinstance(obj,dict):
        for value in obj.values():finite(value)
    if isinstance(obj,(tuple,list)):
        for value in obj:finite(value)
finite(parts)
seconds=time.monotonic()-start
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if os.uname().sysname=='Darwin' else 1024)
if seconds>=180 or not 0<rss<384:raise RuntimeError('resource cap')
count=sum(part['checks'] for part in parts.values())
result=dict(executed_assertions=count,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Finite configuration and native-phase controls. No audit status, spectrum census, mixing rate or physical-law selection.')
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/native_global_charge_support_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
    print('per_element: literal native single-edge amplitudes and exact cycle XOR.')
    print('per_site: full degree and signed-charge constraints at every delivered intermediate.')
    print('per_mode: no spectral modes computed; finite Perron consequence is proved separately.')
    print('per_block: three declared exact finite fixtures, with repeated endpoints retained.')
    print('lattice_wide: analytical D2 theorem on finite even cubic tori; no full configuration census.')
    print(f'TOTAL: PASS={count} FAIL=0')
    print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
