"""Unlaunched cost gate; full replay deliberately disabled in this design."""
from pathlib import Path
from fractions import Fraction
from math import isqrt
import sys,json,hashlib,signal,time,resource,importlib.util
P=Path(__file__).resolve().parent
def require(c,m):
 if not c:raise ValueError(m)
def main():
 require(sys.flags.isolated and sys.dont_write_bytecode,'-I -B required')
 require(len(sys.argv)==3 and sys.argv[1]=='cost','cost FRESH_OUTPUT only; full run unlaunched')
 start=time.monotonic();signal.alarm(29)
 spec=importlib.util.spec_from_file_location('bound_verify',P/'verify.py');guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard);freeze=guard.verify()
 out=Path(sys.argv[2]).resolve();require(not out.exists() and out!=P and P not in out.parents,'fresh external output');out.mkdir(parents=True)
 rows=[];io_seconds=0.0
 try:
  spec=importlib.util.spec_from_file_location('replay_core',P/'replay_core.py');core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
  guard.verify_loaded(freeze)
  census=json.loads((P/'ADJACENT_CENSUS.json').read_text());plan=json.loads((P/'COST_PLAN.json').read_text());require(len(plan['cases'])==25,'25 cases')
  t=time.monotonic();B,R,bi,wi=core.baseline(census);baseline=time.monotonic()-t
  for case in plan['cases']:
   t=time.monotonic();gap,bits=core.gap(int(case['mask']),case['center'],census,B,R,bi,wi);elapsed=time.monotonic()-t
   require(gap==Fraction(case['gap_lower']),'source equality');require(gap>Fraction(1,3),'fixed common floor')
   rows.append(dict(case=case,gap_lower=str(gap),denominator_bits=bits,seconds=elapsed));tio=time.monotonic();(out/'PARTIAL.json').write_text(json.dumps(rows));io_seconds+=time.monotonic()-tio
   require(time.monotonic()-start<29 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<384*1048576,'resource')
  guard.verify_loaded(freeze)
  (out/'RESULT.json').write_text(json.dumps(dict(status='COMPLETE',baseline_seconds=baseline,partial_io_seconds=io_seconds,rows=rows,seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,scope='cost-only exact25-case gate; not full replay'),indent=2))
 except BaseException as e:
  (out/'FAILURE.json').write_text(json.dumps(dict(error=repr(e),rows=rows,seconds=time.monotonic()-start)));raise
if __name__=='__main__':main()
