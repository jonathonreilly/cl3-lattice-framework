from pathlib import Path
import types,sys,json
from fractions import Fraction as F
p=Path('/private/tmp/toe-24h-probes-20260908/native-scalable-action-bound-design')
for n in ('interval','coefficients','core'):
 m=types.ModuleType(n);sys.modules[n]=m;exec(compile((p/(n+'.py')).read_bytes(),str(p/(n+'.py')),'exec'),m.__dict__)
iv=sys.modules['interval'];c=sys.modules['core'];cf=sys.modules['coefficients'];R=((397,0),(397,1));C=[{R[0]:iv.ONE},{R[1]:iv.ONE}];events=[];calls=[]
def entry(a,b):calls.append((a,b));return iv.ONE if a==b else iv.ZERO
r=c.bound(C,R,[iv.ZERO]*399,entry,[iv.ONE]*66,[iv.ONE]*66,events.append);n=0
def req(x):
 global n
 if not x:raise ValueError(n)
 n+=1
# Independent source image: K xA=qA, K Gamma xA=Gamma qA.
# Both sources orthogonal to V in this formal identity fixture, so Frobenius²=2.
for z in r['results']:
 req(z['a_upper_numerator']==0);u=z['b'][1];req((u-1)**2<2*iv.S**2<=u*u);req(z['pass'] is False)
req(len(calls)==52 and len(set(tuple(sorted(x)) for x in calls))==52)
req([x['candidate'] for x in events if x['stage']=='free_bound']==['zero','dominant_diagonal'])
try:c.bound(C,R,[iv.ZERO]*399,lambda a,b:iv.rational(-1) if a==b==(401,0) else entry(a,b),[iv.ONE]*66,[iv.ONE]*66,events.append)
except cf.Indeterminate:req(True)
else:req(False)
req(5*(36864+3072+6144)==230400)
print(json.dumps({'status':'PASS','predicates':n,'native_calls':0,'scope':'tiny independent xA-pair formal identity fixture, negative PSD adverse'}))
