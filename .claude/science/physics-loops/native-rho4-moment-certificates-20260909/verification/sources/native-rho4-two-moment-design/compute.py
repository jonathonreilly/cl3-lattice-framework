"""New certificate arithmetic only; no executable binder or native input access."""
import json,time
from fractions import Fraction as F
from math import comb
from interval import add,mul,neg
from interval_base import pi_bounds

def moments():
 s=[comb(2*n,n) for n in range(41)]
 two=[sum(comb(n,k)*s[k]*s[n-k] for k in range(n+1)) for n in range(41)]
 return [sum(comb(n,k)*two[k]*s[n-k] for k in range(n+1)) for n in range(41)]

def run(out,catalog):
 start=time.monotonic();stage='initial';current=None;panels=[];totals=[(F(0),F(0)),(F(0),F(0))]
 def save(n,x):(out/n).write_text(json.dumps(x,indent=2)+'\n')
 def partial():save('PARTIAL.json',dict(stage=stage,current=current,panels=panels,sums=[list(map(str,v))for v in totals],seconds=time.monotonic()-start))
 (out/'PANELS').mkdir();partial()
 try:
  if len(catalog)!=1742 or [n['id']for n in catalog]!=list(range(1742)):raise ValueError('node census/order')
  eps=F(1,2**64);first=catalog[0]
  if first['panel']!=-64 or not eps<first['t_interval'][0]<first['t_interval'][1]<2*eps:raise ValueError('low-tail first node')
  lowc=(eps*first['A_interval'][0],eps*(first['A_interval'][1]+3*first['t_interval'][1]));lowm=(eps-F(17,60)*eps**3/3,eps)
  for j in range(-64,3):
   stage='panel';current=j;nodes=[n for n in catalog if n['panel']==j]
   if len(nodes)!=26:raise ValueError('panel census')
   vals=[(F(0),F(0)),(F(0),F(0))]
   for n in nodes:
    vals[0]=add(vals[0],mul(n['weight_interval'],n['A_interval']))
    q=add((F(1),F(1)),neg(mul(mul(n['t_interval'],n['t_interval']),n['A_interval'])))
    vals[1]=add(vals[1],mul(n['weight_interval'],q))
   totals=[add(totals[k],vals[k])for k in range(2)];name=f'PANELS/{j+64:02d}.json';save(name,dict(panel=j,values=[list(map(str,v))for v in vals],cumulatives=[list(map(str,v))for v in totals]));panels.append(name);partial()
  stage='tails';partial();mm=moments();rads=[F(544,45)*F(1,4**52),F(128,3)*F(1,4**52)];lows=[lowc,lowm]
  tails=[sum((F((-1)**n)*mm[n+k]/((2*n+1)*8**(2*n+1))for n in range(40)),F(0))for k in range(2)];rems=[F(12**(40+k),81*8**81)for k in range(2)]
  save('TAILS.json',dict(moments=list(map(str,mm)),high_partials=list(map(str,tails)),high_remainders=list(map(str,rems)),low_intervals=[list(map(str,v))for v in lows],quadrature_radii=list(map(str,rads))))
  pl,pu=pi_bounds();rows=[]
  for k,name in enumerate(['cminus','mu']):
   ans=mul(add(add(totals[k],(tails[k],tails[k]+rems[k])),(lows[k][0]-rads[k],lows[k][1]+rads[k])),(2/pu,2/pl));width=ans[1]-ans[0]
   rows.append(dict(observable=name,interval=list(map(str,ans)),width=str(width),target=str(F(2,10**28)),status='CERTIFIED_TARGET'if width<=F(2,10**28)else'INDETERMINATE'))
  stage='complete';save('RESULT.json',dict(status='COMPLETE_NEW_RHO4_TWO_MOMENT_CERTIFICATE',rows=rows,all_targets_met=all(r['status']=='CERTIFIED_TARGET'for r in rows),panels=67,nodes=1742,tail_terms=40,oracle_calls=0,seconds=time.monotonic()-start));partial()
 except BaseException as e:partial();save('FAILURE.json',dict(stage=stage,current=current,error=repr(e)));raise
