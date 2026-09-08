import decimal,itertools,json,math,pathlib,time,signal,resource,sys
from decimal import Decimal as D
import conditional as c
N=0
def need(x,msg):
 global N
 N+=1
 if not x:raise ValueError(msg)
def legal(g,x,p):return tuple((x>>e)&1 for e in g.faces[p]) in ((1,0,1,0),(0,1,0,1))
def nf(g,x):return sum(legal(g,x,p) for p in range(g.M))
def exact_exp(g,O,p,V,T):
 # Independent full-state restricted generator: only this geometric p contributes.
 k=len(O);diag=[-D(str(V))*nf(g,x) for x in O];shift=-min(diag)
 K=[[diag[i]+shift if i==j else D(int(legal(g,O[i],p) and O[i]^g.masks[p]==O[j])) for j in range(k)] for i in range(k)]
 term=[[D(int(i==j)) for j in range(k)] for i in range(k)];S=[z[:] for z in term];t=D(str(T));z=t*max(sum(row) for row in K);tail=None
 for n in range(1,1000):
  term=[[sum(term[i][r]*K[r][j] for r in range(k))*t/n for j in range(k)] for i in range(k)]
  S=[[S[i][j]+term[i][j] for j in range(k)] for i in range(k)]
  if z<D(n+2):
   tail=z**(n+1)/D(math.factorial(n+1))/(1-z/D(n+2))
   if tail<D('1e-65'):break
 else:raise ValueError('oracle series cap')
 factor=(-shift*t).exp();return [[v*factor for v in row] for row in S],str(tail)
def masses(Ds,Cs):
 sizes=[len(d) for d in Ds];raw={}
 for ids in itertools.product(*(range(k) for k in sizes for _ in range(2))):
  w=1
  for i,d in enumerate(Ds):
   w*=d[ids[2*i]][ids[2*i+1]]
   if i<len(Cs):w*=Cs[i][ids[2*i+1]][ids[2*i+2]]
  if w:raw[ids]=w
 Z=sum(raw.values());return {k:v/Z for k,v in raw.items()}
def near(x,y):return abs(float(x)-float(y))<2e-12
def rejects(fn):
 try:fn()
 except ValueError:return True
 return False
def build_fixtures(g):
 fixtures={};x=g.seed;wit=[]
 for step in range(40):
  qs=[q for q in range(g.M) if legal(g,x,q)]
  for q in qs:
   y=x^g.masks[q]
   for p in range(g.M):
    aa=2 if legal(g,x,p) else 1;bb=2 if legal(g,y,p) else 1
    key=(aa,bb)
    if key not in fixtures:fixtures[key]=(c.Trajectory(g,x,[(.4,q)],1.,list(wit)),p)
   if len(fixtures)==4:break
  if len(fixtures)==4:break
  q=qs[(7*step+3)%len(qs)];wit.append(q);x^=g.masks[q]
 return list(fixtures.values())
def main():
 decimal.getcontext().prec=80;allcases=[]
 for L in (2,4):allcases+=build_fixtures(c.Geometry(L))
 g=c.Geometry(2);p=next(p for p in range(g.M) if legal(g,g.seed,p));q=next(q for q in g.by_mask[g.masks[p]] if q!=p)
 alias=(c.Trajectory(g,g.seed,[(.2,p),(.5,q),(.8,p)],1.,[]),p);allcases.append(alias)
 g4=c.Geometry(4);p4=next(p for p in range(g4.M) if legal(g4,g4.seed,p));q4=next(q for q in range(g4.M) if legal(g4,g4.seed,q) and c.strict_distant(g4,p4,q))
 distant=(c.Trajectory(g4,g4.seed,[(.4,q4)],1.,[]),p4);allcases.append(distant)
 categories=set();swaps=0;partial=0;tails=[];raw=[];outputs=0
 for path,p in allcases:
  obj=c.Conditional(path,p,.95);categories.update(map(len,obj.orbits))
  oracle=[]
  for O,t in zip(obj.orbits,obj.durations):
   E,tail=exact_exp(path.g,O,p,.95,t);oracle.append(E);tails.append(tail)
  CC=[[[int(legal(path.g,x,q) and x^path.g.masks[q]==y) for y in obj.orbits[i+1]] for x in obj.orbits[i]] for i,(t,q) in enumerate(obj.retained)]
  need(CC==obj.C,'literal compatibility')
  for C in CC:
   swaps+=int(C==[[0,1],[1,0]]);partial+=int(any(sum(row)==0 for row in C) or any(sum(col)==0 for col in zip(*C)))
  target=masses(oracle,CC);actual=masses(obj.D,obj.C)
  need(set(target)==set(actual),'all boundary support')
  for ids,w in target.items():need(near(w,actual[ids]),'all conditional boundary weights')
  for s in range(len(obj.orbits[0])):need(near(sum(w for ids,w in target.items() if ids[0]==s),obj.h[0][s]/sum(obj.h[0])),'free initial marginal')
  for k in range(4):
   tape=[((13*i+17*k+9)%97+0.25)/98 for i in range(256)]
   out,receipt=c.draw(obj,tape);out.check();outputs+=1
   need([(t,q) for t,q in out.events if q!=p]==obj.retained,'physical skeleton retained')
   need(c.Conditional(out,p,.95).partition_signature()==obj.partition_signature(),'quotient invariant')
   need(all(path.g.flux(x)==path.g.flux(path.g.seed) for O in obj.orbits for x in O),'flux')
   raw.append(dict(L=path.g.L,p=p,events=out.events,initial=out.initial,receipt=receipt))
 need(categories=={1,2} and swaps>0 and partial>0,'singleton double swap partial coverage')
 obj=c.Conditional(*alias,.95) if False else c.Conditional(alias[0],alias[1],.95)
 need(obj.retained==[(.5,q)],'exactly selected label removed')
 wrongD=[c.transfer(g,O,.95,t,2.) for O,t in zip(obj.orbits,obj.durations)]
 need(any(not near(v,masses(wrongD,obj.C).get(k,0)) for k,v in masses(obj.D,obj.C).items()),'alias rate mutation biased')
 wrongC=[[[1 for _ in row] for row in C] for C in obj.C]
 need(masses(obj.D,wrongC)!=masses(obj.D,obj.C),'omit compatibility mutation biased')
 obj=c.Conditional(distant[0],distant[1],.95);unmerged=c.normalize(c.matmul(c.matmul(obj.D[0],obj.C[0]),obj.D[1]));merged=c.merged_pair(obj,0)
 need(all(near(a,b) for row,r in zip(unmerged,merged) for a,b in zip(row,r)),'strict distant merged messages')
 need(obj.retained==distant[0].events,'merge keeps physical event')
 partialobj=next(c.Conditional(path,p,.95) for path,p in allcases if any(any(sum(row)==0 for row in C) or any(sum(col)==0 for col in zip(*C)) for C in c.Conditional(path,p,.95).C))
 need(rejects(lambda:c.merged_pair(partialobj,0)),'partial near event not merged')
 O=sorted([g.seed,g.seed^g.masks[p]])
 need(rejects(lambda:c.interval_events(g,O,.95,1.,0,1,c.Tape([0.]),64,1e-12)),'zero first-event time rejects')
 need(rejects(lambda:c.interval_events(g,O,.95,1.,0,1,c.Tape([.5]),0,1e-12)),'event budget fails whole fixture')
 (pathlib.Path(__file__).parent/'TRAJECTORY_CONTROLS.json').write_text(json.dumps(raw,indent=2))
 return dict(checks=N,fixtures=len(allcases),fixed_tape_outputs=outputs,swap_matrices=swaps,partial_matrices=partial,oracle_positive_series_tail_max=max(map(float,tails)),scope='deterministic short fixtures only; no random sampling or timing profile')
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError()));signal.alarm(180);t=time.monotonic();r=main();r['seconds']=time.monotonic()-t;r['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);need(r['rss_mib']<=384,'RSS');r['checks']=N;print(json.dumps(r,indent=2))
