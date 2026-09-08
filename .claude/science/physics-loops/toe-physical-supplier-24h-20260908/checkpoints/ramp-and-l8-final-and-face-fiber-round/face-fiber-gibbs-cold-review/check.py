from pathlib import Path
from fractions import Fraction as F
import importlib.util,itertools,json,hashlib,math
P=Path('/private/tmp/toe-24h-probes-20260908/face-fiber-gibbs');spec=importlib.util.spec_from_file_location('subject',P/'core.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
g=c.Geometry(2);checks=0

def req(x):
 global checks
 checks+=1
 if not x:raise RuntimeError('independent fiber check')
def legal(x,face):return tuple((x>>e)&1 for e in face) in ((0,1,0,1),(1,0,1,0))
def wt(x,y,V):
 if x==y:return 1-V*sum(legal(x,f) for f in g.faces)/len(g.faces)
 return F(sum(legal(x,f) and x^sum(1<<e for e in f)==y for f in g.faces),len(g.faces))
x=g.seed;steps=[];states=[x]
for i in range(3):
 p=next(j for j,f in enumerate(g.faces) if legal(x,f));steps.append(p);x^=g.masks[p];states.append(x)
for V in (F(0),F(1,2),F(19,20)):
 for p in range(g.M):
  O=[sorted({x,x^g.masks[p]}) if legal(x,g.faces[p]) else [x] for x in states];mass={}
  for y in itertools.product(*O):
   v=math.prod(wt(a,b,V) for a,b in zip(y,y[1:]))
   if v:mass[y]=v
  req(bool(mass))
  for u in (0.,.1234567,.5,.999999999999):
   uniforms=[u]*4;remaining=mass.copy();expected=[]
   for j in range(4):
    total=sum(remaining.values());target=F(u)*total;cum=F(0)
    for value in sorted({z[j] for z in remaining}):
     cum+=sum(v for z,v in remaining.items() if z[j]==value)
     if target<cum:break
    expected.append(value);remaining={z:v for z,v in remaining.items() if z[j]==value}
   a=c.PackedPath(g,states,V);a.draw(p,uniforms);req(a.states==expected);a.check();req(a.fiber(p)[0]==O)
# Zero-mass CDF alternatives must never be selected at u0.
# Every tested output above is positive under direct enumeration.
out=dict(checks=checks,scope='Exact independent finite conditional enumeration for3V values and fixed variates; no random sampling',core_sha=hashlib.sha256((P/'core.py').read_bytes()).hexdigest());Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
