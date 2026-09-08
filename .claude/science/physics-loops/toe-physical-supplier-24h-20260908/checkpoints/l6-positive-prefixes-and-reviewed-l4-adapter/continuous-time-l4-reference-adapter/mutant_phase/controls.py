import json,time,resource,signal,tempfile,copy,math,ast
from pathlib import Path
from fractions import Fraction
import adapter,reference_conditional as ref
from reference_runtime import Runtime as OldRuntime
from verified_path import Trajectory
from conditional import Conditional
signal.alarm(180);start=time.monotonic();n=0;cases=0
P=Path(__file__).parent

def ck(c,label):
 global n
 n+=1
 if not c:raise RuntimeError(label)
def fails(fn,label):
 try:fn()
 except (ValueError,AttributeError,TypeError):ck(True,label)
 else:raise RuntimeError(label+' survived')
def literal_sources(g,x):
 out=[]
 for h in ((1,) if g.L==2 else (1,2)):
  total=0
  for a in range(3):
   for b in range(3):
    if a==b:continue
    z=sum((1j)**(4*h*r[a]//g.L)*(-1)**sum(r)*(1 if x>>e&1 else -1) for e,(r,c) in enumerate(g.links) if c==b)
    total+=int(z.real)**2+int(z.imag)**2
  out.append(Fraction(total,4*g.L**3))
 return out
for L in (2,4):
 for T in (.5,2.):
  a=adapter.Adapter(L);g=a.g
  for prepared in (False,True):
   x=g.seed;word=[]
   if prepared:
    p=next(p for p in range(g.M) if g.legal(x,p));word=[p];x^=g.masks[p]
   initial=x;events=[]
   for j in range(12):
    p=next(p for p in [(j*7+k)%g.M for k in range(g.M)] if g.legal(x,p));events.append((T*(j+1)/13,p));x^=g.masks[p]
   path=Trajectory(g,initial,events,T,word)
   for selected in (0,g.M//3,2*g.M//3,g.M-1,1,2):
    reference=ref.Trajectory(g,path.initial,list(path.events),path.T,path.witness)
    tape=[(((i*37+11)%997)+.5)/998 for i in range(4096)]
    expected,er=ref.draw(ref.Conditional(reference,selected,.95),tape,maxevents=4096)
    actual,ar=a.block(path,selected,tape)
    ck(actual.initial==expected.initial and list(actual.events)==expected.events,'identical full conditional trajectory')
    ck(actual.witness==expected.witness and ar==er,'identical witness/receipt')
    ck(actual.full_check()==expected.check(),'full validation')
    ck(actual.check()==expected.check(),'cached endpoint matches')
    ck(path.initial==reference.initial and list(path.events)==reference.events,'old path unchanged')
    for state in (actual.initial,actual.check()):ck(a.sources(state)==literal_sources(g,state),'independent complex sources')
    values=a.measure(actual);ck(all(math.isfinite(v) for v in values.values()),'finite values')
    if L==4:
     def nf(state):return sum([int(state>>e&1) for e in face] in ([1,0,1,0],[0,1,0,1]) for face in g.faces)
     x=actual.initial;mid=x;integral=Fraction(0);last=Fraction(0)
     for t,q in actual.events:
      integral+=(Fraction(t)-last)*nf(x);x^=g.masks[q]
      if t<=T/2:mid=x
      last=Fraction(t)
     integral+=(Fraction(T)-last)*nf(x);v=L**3;s1,s2=literal_sources(g,mid);el=-Fraction(nf(actual.initial),20);er=-Fraction(nf(x),20);em=(el+er)/2
     plane=[sum([int(mid>>e&1) for e in face] in ([1,0,1,0],[0,1,0,1]) for face in g.faces[i*v:(i+1)*v]) for i in range(3)]
     corner=Fraction(sum(sum(1 if mid>>e&1 else -1 for e,(r,b) in enumerate(g.links) if b==a)**2 for a in range(3)),4*v*v)
     literal=[nf(mid),s1,s2,s1*s1,s2*s2,em,el*er,s1*em,s2*em,integral/Fraction(T),1-Fraction(2*(actual.initial^x).bit_count(),g.E),len(actual.events),Fraction(4*len(actual.events),3*v)/Fraction(T),corner,Fraction(3*sum(z*z for z in plane)-nf(mid)**2,3*v*v)]
     for name,target in zip(adapter.NAMES,literal):ck(abs(values[name]-float(target))<1e-12,'literal L4 '+name)
    if L==2:
     old=OldRuntime.measure(type('R',(),{'g':g})(),expected)
     ck(values==old,'all twelve legacy readouts')
    else:
     mid=actual.initial
     for t,p in actual.events:
      if t<=T/2:mid^=g.masks[p]
     src=literal_sources(g,mid);ck(values['mid_X1']==float(src[0]) and values['mid_X2']==float(src[1]),'midpoint complex harmonics')
    ck(a.balance(values,T)==.95*values['time_average_NF']-values['physical_event_count']/T-values['endpoint_h'],'same-time energy balance')
    fails(lambda:setattr(actual,'initial',0),'immutable initial')
    fails(lambda:setattr(g,'M',0),'immutable geometry')
    path=actual;cases+=1
   with tempfile.TemporaryDirectory() as td:
    f=Path(td)/'path.json';a.save(path,f);back=a.load(f)
    ck(back.initial==path.initial and back.events==path.events and back.witness==path.witness and a.measure(back)==a.measure(path),'lossless checkpoint')
    z=json.loads(f.read_text());z['initial']=hex(path.initial^1);f.write_text(json.dumps(z));fails(lambda:a.load(f),'corrupt initial witness')
    z=json.loads(json.dumps({'L':L,'V':'19/20','T':T.hex(),'initial':hex(path.initial),'events':[[t.hex(),p] for t,p in path.events],'witness':path.witness}));z['events']=[[float('nan').hex(),0]];f.write_text(json.dumps(z));fails(lambda:a.load(f),'nonfinite time')
   fails(lambda:Trajectory.from_conditional(path,path.initial,[(T/2, g.M)],0),'invalid label')
   if path.events:
    removed=path.events[0];selected=(removed[1]+1)%g.M
    fails(lambda:Trajectory.from_conditional(path,path.initial,path.events[1:],selected),'deleted retained physical event')
# Deterministic initialization tapes, never a pseudorandom trajectory job.
for L in (2,4):
 a=adapter.Adapter(L);fails(lambda:a.measure(ref.Trajectory(a.g,a.g.seed,[],.5,[])),'unverified mutable path');M=a.g.M;faces=[i%M for i in range(2*M+100)];clocks=[.5]*100
 p,r=a.propagated(.01,faces,clocks,burn_sweeps=2,max_clock_events=100);ck(p.full_check()==p.check(),'propagated full witness');ck(r['rk_proposals']==2*M,'initializer count')
 fails(lambda:a.propagated(.01,faces,[0.],burn_sweeps=2),'zero clock')
 fails(lambda:a.propagated(math.log(2)/M,faces,[.5],burn_sweeps=2),'boundary clock')
 fails(lambda:a.propagated(100.,faces,[.5]*100,burn_sweeps=2,max_clock_events=1),'clock cap')
# Complete conditional arithmetic remains identical except trajectory class and final plumbing.
old=ast.parse((P/'reference_conditional.py').read_text());new=ast.parse((P/'conditional.py').read_text())
for name in ('product','matmul','normalize','orbit','transfer','choose','interval_events','strict_distant','merged_pair'):
 f=lambda t:ast.dump(next(x for x in t.body if isinstance(x,ast.FunctionDef) and x.name==name),include_attributes=False)
 ck(f(old)==f(new),'unchanged '+name)
for name in ('Conditional','Tape'):
 f=lambda t:ast.dump(next(x for x in t.body if isinstance(x,ast.ClassDef) and x.name==name),include_attributes=False)
 ck(f(old)==f(new),'unchanged '+name)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576;ck(rss<384,'resource RSS')
print(json.dumps({'checks':n,'actual_fixed_tape_block_pairs':cases,'seconds':time.monotonic()-start,'rss_mib':rss,'scope':'deterministic supplied tapes/reference comparisons, no sampling profile or production'},indent=2))
