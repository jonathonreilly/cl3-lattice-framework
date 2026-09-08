"""Portable exact saved-residual and two-mode checks; no physical solves."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_THIRD_ORDER_STAR_VERTEX_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md',
 'scripts/native_third_order_star_vertex_replay_2026_09_08.py',
 'scripts/native_third_order_star_vertex_two_mode_2026_09_08.py',
 '.claude/science/physics-loops/native-third-order-star-vertex-20260908/evidence/native-l4-third-vertex-post-review/INPUTS.json',
 '.claude/science/physics-loops/native-third-order-star-vertex-20260908/evidence/native-l4-third-vertex-run-1085/RESULT.json',
 '.claude/science/physics-loops/native-third-order-star-vertex-20260908/evidence/native-l4-third-vertex-run-1085/SOLVE_VECTORS.json',
)
def main():
 import argparse,json,hashlib,runpy,signal,time,resource
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');p.parse_args()
 signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
 replay=runpy.run_path(str(root/AUDIT_INPUT_PATHS[4]))['check'](root)
 two=runpy.run_path(str(root/AUDIT_INPUT_PATHS[5]))['check']()
 if replay['checks']!=32 or two['checks']!=7:raise ValueError('predicate group coverage')
 # Live cross-path comparison: direct CAR residual-derived weight vs two-mode inverse.
 from fractions import Fraction
 alpha=Fraction(two['direct_two_mode_cases'][0]['alpha'])
 if Fraction(replay['particle_weights']['1'])!=alpha*alpha or any(Fraction(replay['particle_weights'][str(k)]) for k in (3,5)):raise ValueError('independent vertex equality')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss>384*1048576:raise RuntimeError('384MiB RSS')
 print(json.dumps(dict(status='PASS',checks=40,replay=replay,two_mode=two,input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_bytes=rss,scope='39 helper predicate groups plus1 cross-path comparison; no new physical solve, bulk or full-sixth inference'),indent=2))
if __name__=='__main__':main()
