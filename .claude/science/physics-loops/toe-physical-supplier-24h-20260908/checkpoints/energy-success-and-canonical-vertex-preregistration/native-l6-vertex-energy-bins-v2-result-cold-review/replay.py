from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib
B=Path('/private/tmp/toe-24h-probes-20260908');O=B/'native-l6-vertex-energy-bins-v2-run-4b771';R=B/'native-l6-vertex-energy-bins-v2-root-review';C=B/'native-l6-vertex-energy-bins-v2';checks=0
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def need(v):
 global checks
 if not v:raise ValueError('predicate '+str(checks))
 checks+=1
x=json.loads((O/'RESULT.json').read_text());b=json.loads((O/'BINS.json').read_text());binding=json.loads((R/'BINDING.json').read_text());prod=json.loads(Path(binding['receipts']['production']['path']).read_text());D=2**100;E=F(prod['Echi'])
need(x['bins']==b['bins'] and x['entries']==b['entries']==2**20 and len(x['bins'])==686)
need(x['input_sha256']==binding['raw_sha256'] and x['binding_sha256']==sha(R/'BINDING.json'))
f=json.loads((C/'FREEZE.json').read_text());need(sha(C/'FREEZE.json')==x['source_freeze'])
for p,h in f['inputs'].items():need(sha(Path(p))==h)
for r in binding['receipts'].values():need(sha(Path(r['path']))==r['sha256'])
rows={}
for r in x['bins']:
 c=tuple(r['counts']);need(c not in rows and len(c)==4 and all(type(v)is int and 0<=v<=m for v,m in zip(c,(6,6,6,3))) and sum(c)%2==1)
 n=int(r['numerator']);need(n>=0);rows[c]=F(n,2**2148)
def ceilroot(v):
 q=isqrt(v.numerator*D*D//v.denominator)
 while F(q*q,D*D)<v:q+=1
 need(F((q-1)**2,D*D)<v<=F(q*q,D*D) if v else q==0)
 return F(q,D)
def outward(a,b):return [str(F(a.numerator*D//a.denominator,D)),str(F(-((-b.numerator*D)//b.denominator),D))]
r3=F(isqrt(3*D*D),D);r6=F(isqrt(6*D*D),D)
computed={}
for label in ['one','higher','total']+[str(k) for k in range(1,22,2)]:
 selected=[(c,w) for c,w in rows.items() if label=='total' or (sum(c)==1 if label=='one' else sum(c)>=3 if label=='higher' else sum(c)==int(label))]
 w=sum((w for c,w in selected),F(0));low=F(0);high=F(0)
 for (a,bb,c,d),weight in selected:
  el=(2*a+4*d)*r3+2*bb*r6+6*c;eu=el+F(2*a+4*d+2*bb,D);need(el>0);low+=weight/eu;high+=weight/el
 rt=ceilroot(w);wl=max(F(0),rt-F(1,D)-E)**2;wu=(rt+E)**2
 error=E*(2*rt+E)/((6 if label=='higher' else 2)*r3)
 z={'stored_weight':str(w),'true_weight_interval':outward(wl,wu),'stored_susceptibility_interval':outward(low,high),'quadratic_error':outward(error,error)[1],'true_susceptibility_interval':outward(max(F(0),low-error),high+error)}
 need(z==x['summary'][label]);computed[label]=z
 if label not in ['one','total']:
  key='all_ge3' if label=='higher' else label;need([str(wl),str(wu)]==prod['particle_intervals'][key])
outer=json.loads((R/'OUTER.json').read_text());need(outer['provisional_resource_accept'] and outer['returncode']==0 and outer['failure']is None and 0<outer['seconds']<30 and 0<outer['observed_whole_tree_rss']<=384*2**20)
print(json.dumps({'status':'PASS','checks':checks,'bins':686,'entries':2**20,'higher_interval_display':[float(F(a)) for a in computed['higher']['true_susceptibility_interval']],'one_interval_display':[float(F(a)) for a in computed['one']['true_susceptibility_interval']],'result_sha256':sha(O/'RESULT.json'),'scope':'independent scalar bin reconstruction, no raw vector scan or operator action'},indent=2))
