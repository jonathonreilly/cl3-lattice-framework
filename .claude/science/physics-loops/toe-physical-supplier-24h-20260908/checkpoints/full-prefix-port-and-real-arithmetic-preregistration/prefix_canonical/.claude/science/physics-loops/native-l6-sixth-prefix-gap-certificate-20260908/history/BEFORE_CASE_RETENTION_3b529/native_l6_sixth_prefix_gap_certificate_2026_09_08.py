"""Complete exact declared-support certificate replay; no new solves."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_L6_SIXTH_PREFIX_GAP_CERTIFICATE_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md',
 'scripts/native_l6_sixth_prefix_gap_arithmetic_2026_09_08.py',
 'scripts/native_l6_sixth_prefix_gap_geometry_2026_09_08.py',
 '.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908/live_inputs/ADJACENT_CENSUS.json',
 '.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908/live_inputs/NONADJACENT_CENSUS.json',
 '.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908/live_inputs/ADJACENT_COMPLETE.json',
 '.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908/live_inputs/NONADJACENT_ROWS.json',
 '.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908/live_inputs/TARGETS.json',
)
def main():
 import argparse,json,hashlib,runpy,signal,time,resource
 from pathlib import Path
 from fractions import Fraction as F
 from math import isqrt
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args()
 signal.alarm(175);start=time.monotonic();root=Path(__file__).resolve().parents[1];rows=[]
 def guard():
  if time.monotonic()-start>=175 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise RuntimeError('175s384MiB supplemental guard')
 def read(i):return json.loads((root/AUDIT_INPUT_PATHS[i]).read_text())
 try:
  hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
  core=runpy.run_path(str(root/AUDIT_INPUT_PATHS[4]));geom=runpy.run_path(str(root/AUDIT_INPUT_PATHS[5]))
  adj,non,old_adj,old_non,target=[read(i) for i in range(6,11)];cases=target['cases']
  geometry=geom['check'](adj,non,cases,old_adj,old_non);guard()
  B,R,bi,wi=core['baseline'](adj);guard()
  for case in cases:
   if case['singleton'] is not None:gap=F(2*isqrt(3*10**60),10**30);bits=None;method='fixed initial parity singleton'
   else:gap,bits=core['gap'](int(case['mask']),case['center'],adj,B,R,bi,wi);method='exact full-trace Newton/Woodbury'
   equality=gap==F(case['gap_lower']);floor=gap>F(1,3)
   rows.append(dict(mask=case['mask'],center=case['center'],singleton=case['singleton'],gap_lower=str(gap),denominator_bits=bits,equality=equality,above_common_floor=floor,method=method))
   if not equality or not floor:raise ValueError('actual rational source equality/common floor')
   guard()
  if len(rows)!=6489:raise ValueError('full coverage')
  payload=dict(status='PASS',certificate_groups=6489,geometry=geometry,minimum=str(min(F(r['gap_lower']) for r in rows)),common_floor='1/3',native_units='|t|=1; scale gap by |t|, h=2|t|',rows=rows,input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,scope='six declared supports only; no coefficient, all-flux or bulk claim')
  print(json.dumps(payload,indent=2))
 except BaseException as e:
  print(json.dumps(dict(status='FAILED',error=repr(e),completed_or_failed_rows=rows,seconds=time.monotonic()-start)),flush=True);raise
if __name__=='__main__':main()
