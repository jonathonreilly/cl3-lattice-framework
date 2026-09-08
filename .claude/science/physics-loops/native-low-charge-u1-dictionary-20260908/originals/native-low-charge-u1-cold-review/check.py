import itertools,json,pathlib,time,signal,resource,sys
signal.alarm(180);start=time.monotonic();P=pathlib.Path(__file__).parent
checks=0;oldfail=0
# Apply literal rightmost-first electron annihilation to filled Fock bits.
def op(z,k,create):
 if bool(z>>k&1)==create:return None,0
 return z^(1<<k),(-1)**((z&((1<<k)-1)).bit_count())
for m in range(1,9):
 for mask in range(1<<m):
  I=[i for i in range(m) if mask>>i&1];z=(1<<m)-1;s=1
  for i in reversed(I):z,t=op(z,i,False);s*=t
  assert z==((1<<m)-1)^mask and s==(-1)**sum(I)
  oldfail+=s!=(-1)**(sum(I)-len(I)*(len(I)-1)//2);checks+=1
coords=list(itertools.product(range(4),repeat=3));label={v:(13*i+7)%64 for i,v in enumerate(coords)};pos={label[v]:v for v in coords};eps={i:(-1)**sum(v) for i,v in pos.items()};edges=set()
for v in coords:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;edges.add(tuple(sorted((label[v],label[tuple(w)]))))
edges=sorted(edges);ei={e:k for k,e in enumerate(edges)};inc={i:[] for i in range(64)}
for k,(i,j) in enumerate(edges):inc[i].append(k);inc[j].append(k)
order={i:sorted(inc[i],key=lambda e:edges[e][0] if edges[e][1]==i else edges[e][1],reverse=bool(i%2)) for i in inc}
w=[];M=[]
for e,(i,j) in enumerate(edges):
 mask=0
 for v in [i,j]:
  for f in order[v][:order[v].index(e)]:mask^=1<<f
 interval=0
 for v in range(i,j):
  for f in inc[v]:interval^=1<<f
 w.append(mask);M.append(mask^interval)
for e in range(192):
 assert M[e]>>e&1
 for f in range(e):assert (M[e]>>f&1)==(M[f]>>e&1)
def charges(z):return [eps[v]*(sum(z>>e&1 for e in inc[v])-3) for v in range(64)]
def phi(z,q):
 quad=sum((z>>e&1)*((M[e]&z) & ((1<<e)-1)).bit_count() for e in range(192));I=[i for i,v in enumerate(q) if v];D=len(I)
 return (-z.bit_count()+2*(quad+sum(I)+D*(D-1)//2))%4
def fb(q):return sum(1<<(2*i+(s<0)) for i,s in enumerate(q) if s)
seed=0
for e,(i,j) in enumerate(edges):
 v=pos[i];z=pos[j];a=next(a for a in range(3) if v[a]!=z[a]);origin=v if (v[a]+1)%4==z[a] else z
 if origin[a]%2:seed|=1<<e
cases={seed};z=seed;used=set()
for e,(i,j) in enumerate(edges):
 if i not in used and j not in used:
  z^=1<<e;used|={i,j};cases.add(z)
  if len(used)==16:break
for axes in [1,2]:
 z=sum(1<<e for e,(i,j) in enumerate(edges) if next(a for a in range(3) if pos[i][a]!=pos[j][a])<axes);cases.add(z)
cases|={z^((1<<192)-1) for z in list(cases)}
hops=rings=wrong=0;Ds=set()
for z in cases:
 q=charges(z);assert max(map(abs,q))<=1 and sum(q)==0;Ds.add(sum(v*v for v in q));base=phi(z,q)
 for e,(i,j) in enumerate(edges):
  Bi=(-1)**sum(z>>f&1 for f in inc[i]);Bj=(-1)**sum(z>>f&1 for f in inc[j])
  if Bi==Bj:continue
  zz=z^(1<<e);qq=charges(zz)
  if max(map(abs,qq))>1:continue
  src=i if q[i] else j;dst=j if src==i else i;s=q[src];f=fb(q);f,a=op(f,2*src+(s<0),False);f,b=op(f,2*dst+(s<0),True);assert f==fb(qq)
  native=(1+2*((w[e]&z).bit_count()%2)+(2 if Bi-Bj<0 else 0))%4
  wanted=0 if -a*b==1 else 2
  assert (native+phi(zz,qq)-base)%4==wanted
  wrong+=(native+phi(zz,qq)-base)%4!=(0 if a*b==1 else 2)
  black=i if eps[i]==1 else j;assert ((zz>>e&1)-(z>>e&1))==(-s if src==black else s);hops+=1
 for v in coords:
  for a,b in itertools.combinations(range(3),2):
   va=list(v);vb=list(v);vab=list(v);va[a]=(va[a]+1)%4;vb[b]=(vb[b]+1)%4;vab[a]=(vab[a]+1)%4;vab[b]=(vab[b]+1)%4
   C=[label[v],label[tuple(va)],label[tuple(vab)],label[tuple(vb)]];es=[ei[tuple(sorted((C[k],C[(k+1)%4])))] for k in range(4)];bits=[z>>e&1 for e in es]
   if any(bits[k]==bits[(k+1)%4] for k in range(4)):continue
   zz=z;phase=0
   for k in reversed(range(4)):
    e=es[k];phase+=2*((w[e]&zz).bit_count()%2)+2*(C[k]>C[(k+1)%4]);zz^=1<<e
   qq=charges(zz);assert qq==q and (phase+phi(zz,qq)-base)%4==0;rings+=1
assert hops and rings and wrong==hops and oldfail
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
assert rss<384
out=dict(hole_basis_subsets=checks,old_basis_formula_failures=oldfail,relabeled_native_configurations=len(cases),D_sectors=sorted(Ds),native_hop_columns=hops,ring_columns=rings,missing_minus_failures=wrong,seconds=time.monotonic()-start,rss_mib=rss,scope='finite different-order native controls; no full global census')
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
