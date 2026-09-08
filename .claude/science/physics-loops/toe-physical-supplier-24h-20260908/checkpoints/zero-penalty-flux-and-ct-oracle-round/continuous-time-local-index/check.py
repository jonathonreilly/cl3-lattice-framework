import json,math,pathlib,time,resource,sys,signal
import index as ix
import conditional_reference as c
N=0
def need(v,msg):
 global N
 N+=1
 if not v:raise ValueError(msg)
def gated(g,x,p):return x^g.masks[p] if g.legal(x,p) else x
def full_transfer(path,p):
 a=c.Conditional(path,p,.95);v=a.D[0]
 for i,C in enumerate(a.C):v=c.normalize(c.matmul(c.matmul(v,C),a.D[i+1]))
 return c.normalize(v)
def near(A,B):return len(A)==len(B) and all(abs(x-y)<2e-12 for row,r in zip(A,B) for x,y in zip(row,r))
def state(path,t):
 x=path.initial
 for u,p in path.events:
  if u<t:x^=path.g.masks[p]
 return x
def integral(path):
 x=path.initial;last=0.;total=0.
 for t,p in path.events:total+=(t-last)*path.g.nf(x);x^=path.g.masks[p];last=t
 return total+(path.T-last)*path.g.nf(x)
def main():
 g=c.Geometry(4);p=next(p for p in range(g.M) if g.legal(g.seed,p));q=next(q for q in range(g.M) if g.legal(g.seed,q) and gated(g,gated(g,g.seed,p),q)!=gated(g,gated(g,g.seed,q),p));far=next(q for q in range(g.M) if g.legal(g.seed,q) and c.strict_distant(g,p,q))
 need(not set(g.faces[p]).isdisjoint(g.faces[q]),'overlapping gated noncommutativity')
 base=c.Trajectory(g,g.seed,[(.05,p),(.1,p),(.6,q)],1.,[]);expanded=c.Trajectory(g,g.seed,sorted(base.events+[(.2+j*.01,far) for j in range(20)]),1.,[])
 I=ix.Index(base);J=ix.Index(expanded);li=ix.local_messages(I,p,.95);lj=ix.local_messages(J,p,.95)
 need(li['local_event_count']==lj['local_event_count']==3,'distant events not scanned locally')
 need(li['index_entry_visits']==lj['index_entry_visits']<=12,'bounded local incidence visits')
 need(near(li['total'],full_transfer(base,p)) and near(lj['total'],full_transfer(expanded,p)),'full/local message equality')
 need(near(li['total'],lj['total']),'distant transport cancels common NF')
 need(len(list(ix.events(J.global_root)))==23,'distant physical events retained')
 outputs=[]
 for k in range(6):
  path=expanded if k%2 else base;obj=c.Conditional(path,p,.95);out,receipt=c.draw(obj,[((17*j+13*k+9)%103+.25)/104 for j in range(512)])
  index=ix.Index(path);oldroot=index.global_root;newtimes=[t for t,q0 in out.events if q0==p];initial_flip=out.initial!=path.initial
  change=ix.integral_delta(index,p,newtimes,initial_flip)
  need(abs(change-(integral(out)-integral(path)))<1e-10,'local integral NF delta')
  oldcount,newcount=index.splice(p,newtimes,initial_flip);rebuilt=index.trajectory();rebuilt.check()
  need(rebuilt.initial==out.initial and rebuilt.events==out.events,'persistent splice physical output')
  need(list(ix.events(oldroot))==list(ix.events(ix.Index(path).global_root)),'old persistent root unchanged')
  need(sum(ix.sz(r) for r in index.edge.values())==4*ix.sz(index.global_root),'worldline count invariant')
  for root in [index.global_root]+list(index.edge.values())+list(index.face.values()):ix.audit(root)
  need(list(ix.events(index.global_root))==sorted(ix.events(index.global_root),key=ix.key),'AVL key ordering')
  for t in (0.,.06,.11,.3,.59,.61,.99,1.):
   x=index.state(t);a=state(path,t);need(x==state(out,t),'all-edge prefix reconstruction');need(x^a in (0,g.masks[p]),'only selected support changes')
   need(g.nf(x)-g.nf(a)==(ix.dnf(g,a,p) if x!=a else 0),'fixed-time NF local update')
  outputs.append(dict(selected=p,near=q,far=far,old_events=len(path.events),new_events=len(out.events),local_events=3,integral_NF_change=change,receipt=receipt))
 # Collision at an ignored distant event must still be caught by global logarithmic lookup.
 index=ix.Index(expanded);root=index.global_root
 try:index.splice(p,[.2,.3],False)
 except ValueError as e:need('global event collision' in str(e),'distant collision reason')
 else:need(False,'collision accepted')
 need(index.global_root is root,'failed splice atomic')
 try:index.splice(p,[.2],False)
 except ValueError as e:need('legality' in str(e),'near gated incompatibility reason')
 else:need(False,'gated invalid proposal accepted')
 need(index.global_root is root,'invalid proposal atomic')
 (pathlib.Path(__file__).parent/'FIXTURES.json').write_text(json.dumps(outputs,indent=2))
 return dict(checks=N,local_events=3,expanded_physical_events=23,prefix_convention='strictly before t (left limit)',scope='deterministic data-structure controls only; no profile/sampling')
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError()));signal.alarm(180);t=time.monotonic();r=main();r['seconds']=time.monotonic()-t;r['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);need(r['rss_mib']<=384,'RSS');r['checks']=N;print(json.dumps(r,indent=2))
