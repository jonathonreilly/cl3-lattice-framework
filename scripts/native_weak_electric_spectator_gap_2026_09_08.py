"""Portable exact certificate for the supplied finite L4 weak-electric block."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_WEAK_ELECTRIC_SPECTATOR_GAP_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'scripts/native_weak_electric_rational_core_2026_09_08.py',
 'scripts/native_weak_electric_candidate_decoder_2026_09_08.py',
 'scripts/native_weak_electric_rational_replay_2026_09_08.py',
 'scripts/native_weak_electric_magnetic_symmetry_2026_09_08.py',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/INPUT_HASHES.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/FRAME_RESULT.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/PREFIXES.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_0.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_0.npz',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_3.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_3.npz',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_9.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_9.npz',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_12.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_12.npz',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_36.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_36.npz',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_96.json',
 'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/bridge_96.npz',
)
import argparse,hashlib,json,os,resource,runpy,signal,time
from pathlib import Path
from fractions import Fraction

def main():
 start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
 parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
 root=Path(__file__).resolve().parents[1];data=root/'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs'
 sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
 inputs={n:sha(root/n) for n in AUDIT_INPUT_PATHS}
 expected=json.loads((data/'INPUT_HASHES.json').read_text())
 if set(expected)!=set(AUDIT_INPUT_PATHS)-{'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/INPUT_HASHES.json'}:raise RuntimeError('exact input closure')
 for n,h in expected.items():
  if inputs[n]!=h:raise RuntimeError('input hash changed '+n)
 if sorted(p.name for p in data.glob('bridge_*.json'))!=sorted(f'bridge_{b}.json' for b in (0,3,9,12,36,96)) or sorted(p.name for p in data.glob('bridge_*.npz'))!=sorted(f'bridge_{b}.npz' for b in (0,3,9,12,36,96)):raise RuntimeError('candidate membership')
 from native_weak_electric_rational_replay_2026_09_08 import certify
 frame=json.loads((data/'FRAME_RESULT.json').read_text());prefix=json.loads((data/'PREFIXES.json').read_text())
 parts=[certify(data/f'bridge_{b}.json',frame,prefix) for b in (0,3,9,12,36,96)]
 low=sum((Fraction(x['interval'][0]) for x in parts),Fraction(0));high=sum((Fraction(x['interval'][1]) for x in parts),Fraction(0))
 count=sum(len(x['ledger']) for x in parts)
 if count!=2292 or not Fraction(370)<low<=high<Fraction(371):raise RuntimeError('exact coefficient certificate')
 symmetry=runpy.run_path(str(root/'scripts/native_weak_electric_magnetic_symmetry_2026_09_08.py'))['out']
 if symmetry['invariant_dimension']!=1 or [(o['size'],o['forced_zero'],o['distances']) for o in symmetry['orbits']]!=[(192,False,[1]),(384,True,[3]),(256,True,[3]),(192,True,[5])]:raise RuntimeError('magnetic orbit classification')
 seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if os.uname().sysname=='Darwin' else 1024)
 if not 0<rss<384 or seconds>=180:raise RuntimeError('resource cap')
 checks=count+6+1+symmetry['checks']+1+1
 result={'exact_interval':[str(low),str(high)],'coarse_certificate':'370 < c < 371','residual_count':count,'bridge_count':6,'parts':parts,'symmetry':symmetry,'executed_predicates':checks,'predicate_breakdown':{'exact_residual_states':count,'bridge_word_counts':6,'coarse_interval':1,'magnetic_symmetry':symmetry['checks'],'resource_guard':1,'magnetic_classification':1},'elapsed_seconds':seconds,'peak_rss_mib':rss,'source_sha256':sha(Path(__file__)),'input_sha256':inputs,'scope':'Exact supplied L4 adjacent coefficient and magnetic-orbit controls; full finite-gap theorem additionally uses the linked proof and isolation/parity premises.'}
 (root/'outputs/native_weak_electric_spectator_gap_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(json.dumps(result,indent=2,allow_nan=False))
 if not args.json:
  print('per_element: canonical edge signs and strict candidate binary decoding.')
  print('per_site: fixed adjacent centers and magnetic translation orbit.')
  print('per_mode: rational Gram metric and physical even active Fock states.')
  print('per_block: all2292 exact residuals, six bridge closures and coefficient interval.')
  print('lattice_wide: supplied L4 symmetry/isolation premises; no larger-volume inference.')
  print(f'TOTAL: PASS={checks} FAIL=0')
  print(f'Resources: {seconds:.6f}s, {rss:.3f}MiB; timeout180s, RSS384MiB.')
if __name__=='__main__':main()
