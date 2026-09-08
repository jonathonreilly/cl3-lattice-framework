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

def candidate(z,e,wrong=False):
 i,j=edges[e];b=i if eps[i]==1 else j;v=j if b==i else i;kappa=1 if b==i else -1
 # Words are written left to right; automatic adjoint reverses and toggles.
 terms=[(1,[(2*b,True),(2*v,False)]),(1,[(2*b+1,False),(2*v+1,True)]),(-1,[(2*b,True),(2*v+1,True)]),(-1,[(2*b+1,False),(2*v,False)])]
 q=charges(z);f=fb(q);out={};bit=z>>e&1
 for coef,word in terms:
  if wrong and coef==-1:coef=1
  fac=-1j*kappa*coef
  if bit:word=[(k,not c) for k,c in reversed(word)];fac=fac.conjugate()
  ff=f
  for k,c in reversed(word):
   ff,s=op(ff,k,c);fac*=s
   if ff is None:break
  if ff is None or any((ff>>(2*k)&3)==3 for k in range(64)):continue
  out[ff]=out.get(ff,0)+fac
 return {f:c for f,c in out.items() if c}
allowed=forbidden=pair=hop=mutant=herm=0;orient=set();sectors=set();witness=None
for z in sorted(cases):
 q=charges(z);D=sum(t*t for t in q);sectors.add(D)
 for e,(i,j) in enumerate(edges):
  zz=z^(1<<e);qq=charges(zz);got=candidate(z,e)
  if max(map(abs,qq))>1:
   assert got=={};forbidden+=1;witness=(z,e);continue
  expected=(1j)**((2*(w[e]&z).bit_count()+phi(zz,qq)-phi(z,q))%4)
  assert got=={fb(qq):expected},(e,q[i],q[j],got,expected)
  back=candidate(zz,e);assert back=={fb(q):expected.conjugate()};herm+=1
  allowed+=1;orient.add(eps[i]);dnew=sum(t*t for t in qq)
  if dnew!=D:
   pair+=1;assert abs(dnew-D)==2;assert candidate(z,e,True)!=got;mutant+=1
  else:hop+=1;assert candidate(z,e,True)==got
assert pair and hop and forbidden and orient=={-1,1} and mutant==pair
# Direct 4-mode local CAR matrix, independent of global graph phase.
def local(f,bit):
 words=[(1,[(0,True),(2,False)]),(1,[(1,False),(3,True)]),(-1,[(0,True),(3,True)]),(-1,[(1,False),(2,False)])];out={}
 for c,word in words:
  a=-1j*c
  if bit:word=[(k,not c) for k,c in reversed(word)];a=a.conjugate()
  ff=f
  for k,c in reversed(word):
   ff,s=op(ff,k,c);a*=s
   if ff is None:break
  if ff is not None and (ff&3)!=3 and (ff>>2&3)!=3:out[(ff,1-bit)]=out.get((ff,1-bit),0)+a
 return {k:v for k,v in out.items() if v}
def gauge(f,bit):
 rb=(f&1)-((f>>1)&1);rw=((f>>2)&1)-((f>>3)&1)
 return (2*bit-1-2*rb,-(2*bit-1)-2*rw)
localcols=0
for f in range(16):
 if f&3==3 or f>>2&3==3:continue
 for bit in [0,1]:
  for (ff,bb),a in local(f,bit).items():
   assert gauge(f,bit)==gauge(ff,bb);assert local(ff,bb).get((f,bit))==a.conjugate()
  localcols+=1
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);assert rss<384
out=dict(configurations=len(cases),D_sectors=sorted(sectors),allowed_columns=allowed,forbidden_columns=forbidden,pair_columns=pair,hop_columns=hop,automatic_adjoint_checks=herm,missing_pair_minus_failures=mutant,local_no_double_columns=localcols,noninvolution_witness=[str(witness[0]),witness[1]],seconds=time.monotonic()-start,rss_mib=rss)
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
