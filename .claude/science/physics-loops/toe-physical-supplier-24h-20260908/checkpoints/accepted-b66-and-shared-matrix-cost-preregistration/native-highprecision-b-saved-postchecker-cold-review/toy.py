"""Synthetic interval/recurrence controls only; main/moment never invoked."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/native-highprecision-b-saved-postchecker/check.py');ns={'__name__':'definitions_only'};exec(compile(p.read_bytes(),str(p),'exec'),ns);count=0

def encl(a,x):
 global count
 if not a[0]<=x<=a[1]:raise ValueError('enclosure')
 count+=1
for x in [F(-2,7),F(0),F(3,11)]:
 for y in [F(-5,9),F(1,13)]:
  encl(ns['add'](ns['rnd'](x,x),ns['rnd'](y,y)),x+y);encl(ns['mul'](ns['rnd'](x,x),ns['rnd'](y,y)),x*y)
for s in [F(1,2),F(3,2)]:
 x=F(5);a=ns['rnd'](1/(x+s*s),1/(x+s*s));da=ns['rnd'](-2*s/(x+s*s)**2,-2*s/(x+s*s)**2);si=(s,s);ss=ns['mul'](si,si);c=ns['add']((F(1),F(1)),ns['neg'](ns['mul'](a,ss)));e=ns['add'](ns['scale'](ns['mul'](si,a),2),ns['mul'](da,ss))
 for n in range(26):
  encl(c,x**(n+1)/(x+s*s));encl(e,2*s*x**(n+1)/(x+s*s)**2)
  c,e=ns['add']((x**(n+1),x**(n+1)),ns['neg'](ns['mul'](c,ss))),ns['add'](ns['scale'](ns['mul'](si,c),2),ns['neg'](ns['mul'](e,ss)))
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':count,'physical_moment_calls':0,'integrand_calls':0,'oracle_calls':0,'reviewed_source':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
