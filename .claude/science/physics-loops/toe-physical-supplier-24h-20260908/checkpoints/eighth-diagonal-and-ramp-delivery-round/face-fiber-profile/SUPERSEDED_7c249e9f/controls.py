import pathlib,json,random,hashlib,struct,shutil,resource,sys,time,signal
import reference,factory,checkpoint,guarded
from measure import measure
B=pathlib.Path(__file__).resolve().parent
N=0
def need(c,msg):
 global N
 N+=1
 if not c:raise ValueError(msg)
def rejects(fn):
 try:fn()
 except (ValueError,TypeError):return True
 return False
def literal(g,n,V,rng,rk):
 x=g.seed;w=[]
 for _ in range(rk*g.M):
  p=rng.randrange(g.M)
  if reference.Geometry.legal(g,x,p):x^=g.masks[p];w.append(p)
 states=[x]
 for _ in range(n):
  k=g.nf(x);u=rng.random()*(g.M+(1-V)*k);p=int(u) if u<g.M else -1
  if p>=0 and g.legal(x,p):x^=g.masks[p]
  states.append(x)
 return reference.PackedPath(g,states,V,w),w

def main():
 root=B/'CONTROL_FILES';root.mkdir(exist_ok=False);case=0
 for L in (2,4):
  for n in (4,16):
   for V in (0.,.95):
    g=factory.Geometry(L);a,meta=factory.initialize(g,n,V,random.Random(9100+case),2);r,w=literal(g,n,V,random.Random(9100+case),2)
    need(a.states==r.states and a.nf==r.nf and list(a.witness)==w,'initializer exact trajectory');a.check()
    need(measure(a)==measure(r),'initial measurements')
    for j,p in enumerate((0,g.L**3,2*g.L**3)):
     us=[((17*i+13*j+7)%103)/103 for i in range(n+1)]
     r.draw(p,us);factory.draw(a,p,us);a.check()
     need(a.states==r.states and a.nf==r.nf,'guarded DP unchanged');need(measure(a)==measure(r),'draw measurements')
     certified=reference.PackedPath(g,a.states,V,list(a.witness));need(certified.nf==a.nf,'witness after endpoint update')
    folder=root/str(case);checkpoint.save(a,folder);b=checkpoint.load(g,folder,(L,n,V));need(a.states==b.states and a.nf==b.nf and a.witness==b.witness,'file roundtrip')
    us=[((29*i+5)%107)/107 for i in range(n+1)];factory.draw(a,0,us);factory.draw(b,0,us);need(a.states==b.states and a.nf==b.nf and a.witness==b.witness,'continuation');case+=1
 # Real corruptions with recomputed payload SHA.
 origin=root/'0';g=factory.Geometry(2)
 for name,mutate in [('bad_nf',lambda raw:struct.pack('<H',struct.unpack('<H',raw[:2])[0]+1)+raw[2:]),('bad_state',lambda raw:b'\xff'*3+raw[3:])]:
  folder=root/name;shutil.copytree(origin,folder);file='nf.bin' if name=='bad_nf' else 'states.bin';p=folder/file;p.write_bytes(mutate(p.read_bytes()));m=json.loads((folder/'meta.json').read_text());m['files'][file]=checkpoint.sha(p);(folder/'meta.json').write_text(json.dumps(m))
  need(rejects(lambda:checkpoint.load(g,folder,(2,4,0.))),name+' updated hash rejected')
 need(rejects(lambda:checkpoint.load(g,origin,(2,4,.95))),'wrong V')
 saved=checkpoint.load(g,origin,(2,4,0.))
 # A deliberately false witness endpoint must reject, irrespective of binary format integrity.
 y=g.seed^g.masks[next(p for p in range(g.M) if g.legal(g.seed,p))]
 need(rejects(lambda:factory.reconstruct(g,[y,y],[g.nf(y)]*2,0.,[],2*g.nf(y))),'missing witness')
 for t,h in [(float('nan'),1.),(1.,float('inf')),(1e-300,1e-300),(-1.,1.)]:need(rejects(lambda:guarded.guarded_product(t,h)),'DP numeric guard')
 need(guarded.guarded_product(0.,1.)==0. and guarded.guarded_product(1.,0.)==0.,'structural zeros allowed')
 return dict(checks=N,cases=case,scope='reduced deterministic controls only; profile unlaunched')
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError()));signal.alarm(180);t=time.monotonic();r=main();r['seconds']=time.monotonic()-t;r['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);need(r['rss_mib']<=384,'RSS');r['checks']=N;print(json.dumps(r,indent=2))
