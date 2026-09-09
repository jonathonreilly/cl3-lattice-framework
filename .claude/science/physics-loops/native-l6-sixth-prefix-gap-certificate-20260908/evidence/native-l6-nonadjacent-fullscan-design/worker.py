import sys,runpy,time,signal,resource,json
from pathlib import Path
C=runpy.run_path(str(Path(__file__).with_name('common.py')));globals().update({k:v for k,v in C.items() if not k.startswith('__')})
start=time.monotonic();signal.alarm(170)
ck(len(sys.argv)==4 and sys.argv[1] in ('produce','replay'),'mode shard output');mode=sys.argv[1];sid=int(sys.argv[2]);out=Path(sys.argv[3]);pin=verify();plan=read(P/'PLAN.json');ck(0<=sid<52,'shard');indices=plan['shards'][sid];target=out/f'{mode}_{sid:02d}.json';ck(not target.exists(),'no replacement');rows=[]
try:
 if mode=='produce':core=load('core');loaded_numpy()
 else:
  core=load('independent');census=read(P/'CENSUS.json');B,R,bi,wi=core.baseline(census);prior=read(out/f'produce_{sid:02d}.json');ck(prior['freeze']==pin,'producer freeze');rowscheck(prior['rows'],indices,plan)
 for pos,i in enumerate(indices):
  case=plan['cases'][i];mask=int(case['mask']);w=case['representative']['white_center']
  if case['singleton'] is not None:
   from math import isqrt
   v=Fraction(2*isqrt(3*10**60),10**30);bits=None
  elif mode=='produce':
   q=core.certify(mask,w,controls=True);v=Fraction(q['gap_lower']);bits=q['max_denominator_bits']
  else:v,bits=core.gap(mask,w,census,B,R,bi,wi)
  row=dict(index=i,case=case,gap_lower=str(v),positive=v>0,denominator_bits=bits);rows.append(row)
  if mode=='replay':ck(row==prior['rows'][pos],'exact independent row')
  ck(time.monotonic()-start<170 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=384*1048576,'resources')
  (out/f'{mode}_{sid:02d}.partial.json').write_text(json.dumps(rows)+'\n')
 rowscheck(rows,indices,plan);target.write_text(json.dumps(dict(freeze=pin,rows=rows,seconds=time.monotonic()-start,rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2)+'\n')
except BaseException as e:
 (out/f'{mode}_{sid:02d}.FAILED.json').write_text(json.dumps(dict(error=repr(e),rows=rows))+'\n');raise
