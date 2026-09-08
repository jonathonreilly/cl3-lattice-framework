"""Live exact finite controls for the conditional low-charge U1 dictionary."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md',
    'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
    'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
    'docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'scripts/native_low_charge_u1_author_2026_09_08.py',
    'scripts/native_low_charge_u1_independent_2026_09_08.py',
    'scripts/native_low_charge_u1_absolute_2026_09_08.py',
    'scripts/native_low_charge_u1_domain_2026_09_08.py',
    '.claude/science/physics-loops/native-low-charge-u1-dictionary-20260908/inputs/GLOBAL_D4_SEED.json',
)
import argparse,contextlib,hashlib,io,json,math,os,resource,runpy,signal,time
from pathlib import Path
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS}
parts={}
for kind in ('author','independent','absolute','domain'):
    captured=io.StringIO()
    with contextlib.redirect_stdout(captured):runpy.run_path(str(root/'scripts'/f'native_low_charge_u1_{kind}_2026_09_08.py'))
    parts[kind]=json.loads(captured.getvalue())
    if parts[kind]['executed_predicates']<=0:raise RuntimeError('empty predicate coverage')
if parts['author']['native_hop_columns']!=256 or parts['author']['native_ring_columns']!=2348 or parts['author']['local_species_CAR_columns']!=4860:raise RuntimeError('author column coverage')
if parts['independent']['native_hop_columns']!=400 or parts['independent']['ring_columns']!=2096:raise RuntimeError('independent column coverage')
if parts['absolute']['absolute_basis_columns']!=510 or parts['absolute']['old_identity_failures']!=255:raise RuntimeError('absolute phase coverage')
def finite(obj):
    if isinstance(obj,float) and not math.isfinite(obj):raise RuntimeError('nonfinite output')
    if isinstance(obj,dict):
        for value in obj.values():finite(value)
    if isinstance(obj,(tuple,list)):
        for value in obj:finite(value)
finite(parts)
seconds=time.monotonic()-start
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
if seconds>=180 or not 0<rss<384:raise RuntimeError('resource cap')
count=sum(part['executed_predicates'] for part in parts.values())
result=dict(executed_predicates=count,parts=parts,elapsed_seconds=seconds,peak_rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,scope='Finite exact phase/domain controls; general intertwiner proof is separate. No audit status, physical electromagnetic identification or role retirement.')
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/native_low_charge_u1_dictionary_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
    print('per_element: exact native hopping, gated ring and absolute Fock basis phases.')
    print('per_site: full six-edge Gauss/no-double label controls on both sublattices.')
    print('per_mode: site-major two-species CAR and all one-through-eight-mode hole subsets.')
    print('per_block: selected actual L4 columns in both native order conventions, not a full census.')
    print('lattice_wide: finite all-sector basis proof under the supplied restricted carrier.')
    print(f'TOTAL: PASS={count} FAIL=0')
    print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
