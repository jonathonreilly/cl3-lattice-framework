import itertools,json,math,pathlib,hashlib,importlib.util,signal,resource,sys,time
from fractions import Fraction as F
import core
B=pathlib.Path(__file__).resolve().parent
checks=0

def require(c,msg):
 global checks
 checks+=1
 if not c:raise ValueError(msg)

def literal_nf(g,x):
 return sum([((x>>f[0])&1,(x>>f[1])&1,(x>>f[2])&1,(x>>f[3])&1)] in ([(1,0,1,0)],[(0,1,0,1)]) for f in g.faces)
def w(g,x,y,V):
 if x==y:return 1-V*literal_nf(g,x)/g.M
 return F(sum(x^sum(1<<e for e in f)==y and tuple((x>>e)&1 for e in f) in ((1,0,1,0),(0,1,0,1)) for f in g.faces),g.M)
def enumerated(g,states,p,V):
 O=[sorted({x,x^g.masks[p]}) if tuple((x>>e)&1 for e in g.faces[p]) in ((1,0,1,0),(0,1,0,1)) else [x] for x in states]
 masses={}
 for ys in itertools.product(*O):
  mass=F(1)
  for a,b in zip(ys,ys[1:]):mass*=w(g,a,b,V)
  if mass:masses[ys]=mass
 Z=sum(masses.values());return O,{ys:v/Z for ys,v in masses.items()}
def inverse(masses,uniforms):
 remaining=masses;out=[]
 for i,u in enumerate(uniforms):
  vals=sorted({y[i] for y in remaining});weights=[sum(v for y,v in remaining.items() if y[i]==z) for z in vals]
  target=F(u)*sum(weights);cum=F(0)
  for z,v in zip(vals,weights):
   cum+=v
   if target<cum:break
  out.append(z);remaining={y:v for y,v in remaining.items() if y[i]==z}
 return tuple(out)
def matrix_mass(O,T):
 d={}
 for ids in itertools.product(*(range(len(z)) for z in O)):
  a=F(1)
  for i in range(len(T)):a*=T[i][ids[i]][ids[i+1]]
  if a:d[tuple(O[i][j] for i,j in enumerate(ids))]=a
 Z=sum(d.values());return {y:v/Z for y,v in d.items()}
def reject(fn):
 try:fn()
 except (ValueError,TypeError):return True
 return False

def main():
 g=core.Geometry(2);V=F(19,20);fixtures=[];x=g.seed
 # Fixed deterministic legal paths, not Monte Carlo samples.
 for k in range(12):
  path=[g.seed];x=g.seed
  for j in range(4):
   legal=[p for p in range(g.M) if g.legal(x,p)]
   if (k+j)%3:x^=g.masks[legal[(k+3*j)%len(legal)]]
   path.append(x)
  fixtures.append(path)
 fixtures.insert(0,[g.seed]*5)
 exact_cases=0;changed_other=False
 for states in fixtures:
  for p in range(g.M):
   a=core.PackedPath(g,states,V);O,N,T=a.fiber(p);OO,masses=enumerated(g,states,p,V)
   require(O==OO,'orbit');require(matrix_mass(O,T)==masses,'all exact weights')
   require(all(k==literal_nf(g,x) for row,ns in zip(O,N) for x,k in zip(row,ns)),'all Nf cache')
   for ys,mass in masses.items():
    require(all(g.flux(y)==g.flux(g.seed) for y in ys),'flux')
    for y in ys:g.validate(y)
    # The partition and conditional must be identical from every positive output.
    oo,other=enumerated(g,ys,p,V);require(oo==O and other==masses,'fiber partition and detailed balance')
    for i in range(4):
     old=states[i]^states[i+1];new=ys[i]^ys[i+1]
     if old and old!=g.masks[p] and new!=old:changed_other=True
   for k in range(5):
    us=[((37*k+11*i+7)%101)/101 for i in range(5)]
    a=core.PackedPath(g,states,V);a.draw(p,us);a.check()
    require(tuple(a.states)==inverse(masses,us),'literal exact inverse CDF')
    require(a.nf==[literal_nf(g,x) for x in a.states],'draw Nf')
   exact_cases+=1
 # A block can birth a separated flip interval on a constant original path.
 p=next(p for p in range(g.M) if g.legal(g.seed,p));_,m=enumerated(g,[g.seed]*5,p,V)
 y=g.seed^g.masks[p]
 require(m.get((g.seed,y,y,y,g.seed),0)>0,'separated birth')
 # Other-face labels need not change; their fixed-label assumption is tested directly below.
 # Changing a face column may turn a self bond into a p bond; retaining ALL old labels is invalid.
 require(any(tuple(g.seed for _ in range(5))!=ys for ys in m),'fixed old label mutant witness')
 bad=core.PackedPath(g,[g.seed]*5,V);bad.nf[0]+=1
 require(reject(bad.check),'bad cache')
 require(reject(lambda:core.PackedPath(g,[-1,g.seed],V)),'negative state')
 require(reject(lambda:core.PackedPath(g,[y,y],V)),'missing component witness')
 require(core.PackedPath(g,[y,y],V,[p]).states==[y,y],'valid component witness')
 require(reject(lambda:core.PackedPath(g,[g.seed]*2,1)),'V1 excluded')
 require(reject(lambda:core.PackedPath(g,[g.seed]*2,V).draw(p,[float('nan'),.2])),'NaN')
 # Literal single-slice birth has aggregated L2 multiplicity, not naive N/M^2.
 sq=sum(w(g,g.seed,z,V)**2 for z in {g.seed^g.masks[q] for q in range(g.M) if g.legal(g.seed,q)})
 birth=sq/(w(g,g.seed,g.seed,V)**2+sq)
 require(0<birth<1,'birth probability')
 # Actual source mutants, imported separately. They must fail mathematical equality.
 src=(B/'core.py').read_text();mutants={
  'wrong_matrix':src.replace('Fraction(sum(self.legal(x,p) for p in self.by_mask.get(x^y,())),self.M)','Fraction(2*sum(self.legal(x,p) for p in self.by_mask.get(x^y,())),self.M)'),
  'pinned_endpoint':src.replace('for i in range(len(T)-1,-1,-1):','h[-1]=[1.]+[0.]*(len(O[-1])-1)\n  for i in range(len(T)-1,-1,-1):')}
 kills={}
 for name,source in mutants.items():
  require(source!=src,'mutation applied');path=B/(name+'.py');path.write_text(source)
  spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
  obj=mod.PackedPath(g,[g.seed]*5,V)
  if name=='wrong_matrix':
   # Geometry carries the modified transition function as well.
   gm=mod.Geometry(2);obj=mod.PackedPath(gm,[gm.seed]*5,V);o,ns,t=obj.fiber(p)
   killed=matrix_mass(o,t)!=m
  else:
   killed=False
   for k in range(20):
    us=[((17*k+13*i+3)%103)/103 for i in range(5)];obj=mod.PackedPath(g,[g.seed]*5,V);obj.draw(p,us)
    if tuple(obj.states)!=inverse(m,us):killed=True;break
  require(killed,'actual mutant escaped '+name);kills[name]=killed
 return {'checks':checks,'exact_fibers':exact_cases,'fixture_paths':len(fixtures),'mutants':kills,'single_slice_birth':str(birth),'other_nonself_label_changed_observed':changed_other,'scope':'deterministic controls only; no stochastic sampling or performance/mixing test'}
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('180s')));signal.alarm(180);t=time.monotonic();r=main();r['elapsed']=time.monotonic()-t;r['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);require(r['rss_mib']<=384,'RSS');r['checks']=checks;print(json.dumps(r,indent=2))
