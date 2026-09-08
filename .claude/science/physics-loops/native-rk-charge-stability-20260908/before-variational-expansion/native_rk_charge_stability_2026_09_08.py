"""Live finite controls for conditional native RK charge stability."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md',
    'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
    'scripts/native_rk_charge_static_2026_09_08.py',
    'scripts/native_rk_charge_mobile_2026_09_08.py',
)
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS}
parts={}
for kind in ('static','mobile'):
    captured=io.StringIO()
    with contextlib.redirect_stdout(captured):
        namespace=runpy.run_path(str(root/'scripts'/f'native_rk_charge_{kind}_2026_09_08.py'))
    parts[kind]=json.loads(captured.getvalue())
    if kind=='static':
        if parts[kind]['checks']<=0:raise RuntimeError('no static controls')
    else:
        if not parts[kind]['checks'] or not all(parts[kind]['checks'].values()):raise RuntimeError('failed mobile predicate')
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
count=parts['static']['checks']+len(parts['mobile']['checks'])
result=dict(status='PASS',classification='conditional-support',executed_assertions=count,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Finite static support and signed native hopping controls; operator theorem is in the note. No spectral census, physical mass or neutral gap.')
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/native_rk_charge_stability_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
    print('per_element: exact alternating-plaquette matrix and actual native hopping phase conjugation.')
    print('per_site: all thirty charged degree patterns have four possible source edges.')
    print('per_mode: no spectral modes diagonalized; charged-sector estimate follows from the proved operator inequality.')
    print('per_block: declared finite pair-support fixtures and bounded L4 hopping neighborhoods; repeated rows disclosed.')
    print('lattice_wide: proof covers finite even cubic tori with extents at least four and supplied low-charge dynamics.')
    print(f'TOTAL: PASS={count} FAIL=0')
    print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
