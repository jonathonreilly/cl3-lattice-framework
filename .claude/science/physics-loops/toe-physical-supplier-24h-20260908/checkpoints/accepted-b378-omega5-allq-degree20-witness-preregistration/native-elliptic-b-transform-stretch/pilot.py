import json,time
from fractions import Fraction as F
from elliptic import oracle,const,add,mul,inv,neg
from highorder import gauss
from interval_base import pi_bounds
from core import integrands,high_tail

def run(out):
 out.mkdir();(out/'ORACLES').mkdir();start=time.monotonic();rows=[];stage='initial';cache={};panels=[]
 def save(name,x):(out/name).write_text(json.dumps(x,indent=2)+'\n')
 def get(x):
  key=str(x)
  if key not in cache:
   t=time.monotonic();row=oracle(x);row['seconds']=time.monotonic()-t;idx=len(cache);cache[key]=row
   save(f'ORACLES/{idx:04d}.json',row)
   save('PARTIAL.json',{'stage':stage,'oracle_count':len(cache),'rows':rows,'panels':panels})
   if max(map(F,row['widths']))>F(1,10**30):raise ValueError('oracle width gate')
  return cache[key]
 def interval(row,key):return tuple(map(F,row[key]))
 save('PARTIAL.json',{'stage':stage,'rows':rows})
 try:
  stage='Gauss';t=time.monotonic();rule=gauss(12);save('GAUSS.json',{'rule':[[[str(z) for z in x],[str(z) for z in w]] for x,w in rule],'seconds':time.monotonic()-t})
  fixed={s:get(s) for s in (F(1),F(2))};sums={s:[const(0),const(0)] for s in fixed}
  for j in range(-28,3):
   stage=f'panel{j}';a0=F(2)**j;panel={s:[const(0),const(0)] for s in fixed};t0=time.monotonic()
   for x,w in rule:
    tl=a0*(x[0]+3)/2;th=a0*(x[1]+3)/2;weight=mul(w,const(a0/2))
    # A decreases, so enclose value at every point of the node bracket.
    rl=get(tl);rh=get(th);at=(F(rh['A'][0]),F(rl['A'][1]))
    for s,row in fixed.items():
     g,h=integrands(s,(tl,th),interval(row,'A'),interval(row,'Aprime'),at)
     panel[s][0]=add(panel[s][0],mul(weight,g));panel[s][1]=add(panel[s][1],mul(weight,h))
   for s in fixed:
    sums[s]=[add(sums[s][k],panel[s][k]) for k in (0,1)]
   panels.append({'j':j,'seconds':time.monotonic()-t0,'panel':{str(s):[[str(z) for z in v] for v in panel[s]] for s in fixed},'cumulative':{str(s):[[str(z) for z in v] for v in sums[s]] for s in fixed}})
   save('PARTIAL.json',{'stage':stage,'oracle_count':len(cache),'rows':rows,'panels':panels})
  radius=F(1000,27)*F(4,25)**12;pl,pu=pi_bounds();factor=(2/pu,2/pl)
  for s,row in fixed.items():
   stage=f'finish{s}';tail=high_tail(s,interval(row,'A'),interval(row,'Aprime'));answers=[]
   for k in (0,1):
    low=F(1,2**28)*(1/(s*s) if k==0 else 2/(s**3))
    v=add(add(sums[s][k],tail[k]),(-radius,radius+low));v=mul(v,factor)
    if k==1:v=neg(v)
    answers.append(v)
   widths=[v[1]-v[0] for v in answers];rows.append({'s':str(s),'B':[str(v) for v in answers[0]],'Bprime':[str(v) for v in answers[1]],'widths':[str(v) for v in widths],'target':'1/1000000','status':'CERTIFIED_TARGET' if max(widths)<=F(1,10**6) else 'INDETERMINATE'})
   save('PARTIAL.json',{'stage':stage,'oracle_count':len(cache),'rows':rows,'panels':panels})
  save('RESULT.json',{'status':'COMPLETE_FIXED_CASES','rows':rows,'oracle_count':len(cache),'panels':panels,'seconds':time.monotonic()-start,'alpha_computed':False,'all_targets_met':all(r['status']=='CERTIFIED_TARGET' for r in rows)})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'rows':rows,'panels':panels,'oracle_count':len(cache),'error':repr(e)});raise
