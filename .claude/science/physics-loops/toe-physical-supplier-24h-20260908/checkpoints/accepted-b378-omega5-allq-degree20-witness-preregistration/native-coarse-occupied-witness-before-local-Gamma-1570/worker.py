from pathlib import Path
from fractions import Fraction as F
import json,time,os
from interval import const
from binder import load
from adapter import evaluate
from dictionary import pole
PAIRS=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
def save(p,x):
 tmp=p.with_name(p.name+'.tmp')
 with tmp.open('w') as f:json.dump(x,f,default=str);f.write('\n');f.flush();os.fsync(f.fileno())
 os.replace(tmp,p)
def run(out,plan):
 out=Path(out);out.mkdir(exist_ok=False);rows=[];current={};start=time.monotonic()
 def emit(stage,data):
  nonlocal current
  current={'stage':stage,'case':len(rows)}
  save(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
  if stage in ('witness_panel','witness_block'):
   with (out/'BLOCKS.jsonl').open('a') as f:json.dump({'current':current,'data':data},f,default=str);f.write('\n');f.flush();os.fsync(f.fileno())
 try:
  old,new,selected,c,mu,coeffs,pi=load(plan,emit)
  for oi,(A,C) in enumerate(PAIRS):
   sources=[[1,0,0,0,0,0,0]]
   for pair in (A,C):sources.append([0]+[int(j in pair)*((-1)**(j+1)) for j in range(1,7)])
   ids,t=selected[oi]
   for selector,pair in enumerate((A,C),1):
    emit('before_case',{'orbit':oi,'impurity':selector});pole.cache_clear()
    kind='O' if (pair[0]-1)//2==(pair[1]-1)//2 else 'P'
    bank=[dict(r,impurity_selector=selector,positive_imaginary=coeffs[(r['index'],kind)]) for r in new]
    v=[[const(0) for _ in range(7)] for _ in range(7)]
    for j in range(1,7):v[0][j]=const(2*sources[selector][j]);v[j][0]=const(-2*sources[selector][j])
    ans=evaluate(ids,t,sources,old,bank,c,mu,v,pi,emit);ans.update(orbit=oi,impurity=selector)
    save(out/('CASE_%02d.json'%len(rows)),ans);rows.append(ans)
  save(out/'RESULT.json',{'status':'COMPLETE_FIXED_COARSE_WITNESS','rows':rows,'seconds':time.monotonic()-start,'cases':10,'native_Gaussian_solve':False,'fine_consumer_certified':False});emit('complete',{})
 except BaseException as e:
  try:save(out/'FAILURE.json',{'current':current,'completed':len(rows),'error':repr(e)})
  except BaseException as x:e.add_note('retention '+repr(x))
  raise
