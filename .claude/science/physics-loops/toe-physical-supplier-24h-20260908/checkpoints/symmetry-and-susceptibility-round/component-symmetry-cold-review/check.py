from pathlib import Path
import itertools,json,numpy as np,hashlib
p=Path(__file__).resolve().parent;rows=[];checks=0
def ck(x):
 global checks
 if not bool(x):raise AssertionError('independent component control')
 checks+=1
def face(L,r,a,b):
 ra=list(r);rb=list(r);ra[a]=(ra[a]+1)%L;rb[b]=(rb[b]+1)%L
 return [(r,a),(tuple(ra),b),(tuple(rb),a),(r,b)]
def legal(x,f):
 z=[x[r+(a,)] for r,a in f];return z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]
def reflected(x,j):
 L=len(x);out=np.empty_like(x)
 for r in np.ndindex(L,L,L):
  for b in range(3):
   q=list(r);q[j]=(-q[j]-(b==j))%L;out[r+(b,)]=x[tuple(q)+(b,)]
 return out
def O(x,a,b,h):
 L=len(x);return sum((-1)**sum(r)*np.exp(2j*np.pi*h*r[a]/L)*(float(x[r+(b,)])-.5) for r in np.ndindex(L,L,L))/L**1.5
for L in [2,4,6,8]:
 seed=np.empty((L,L,L,3),np.uint8)
 for r in np.ndindex(L,L,L):
  for d in range(3):seed[r+(d,)]=r[d]%2
 for j in range(3):
  k=(j+1)%3;l=(j+2)%3;x=seed.copy();n=0
  for jp,lp in [(0,0),(0,1),(1,0),(1,1)]:
   layer=[]
   for r in np.ndindex(L,L,L):
    if r[j]%2==jp and r[k]%2==1 and r[l]%2==lp:layer.append(face(L,r,j,k))
   entries=[v for f in layer for v in f];ck(len(entries)==len(set(entries)))
   for f in layer:
    ck(legal(x,f))
    for r,a in f:x[r+(a,)]^=1
    n+=1
   # Full intermediate layer boundary is2-periodic.
   for axis in range(3):ck(np.array_equal(x,np.roll(x,2,axis=axis)))
  ck(n==L**3//2);ck(np.array_equal(x,np.roll(seed,1,axis=j)));ck(np.array_equal(reflected(seed,j),x))
  degree=np.zeros((L,L,L),int)
  for axis in range(3):degree+=x[:,:,:,axis]+np.roll(x[:,:,:,axis],1,axis=axis)
  ck(np.all(degree==3))
  for axis in range(3):ck(sum((-1)**sum(r)*(2*int(x[r+(axis,)])-1) for r in np.ndindex(L,L,L) if r[axis]==0)==0)
  rows.append({'L':L,'axis':j,'moves':n})
 # Generate fixed legal path snapshots without component enumeration, then test symmetry operator equations.
 x=seed.copy();rng=np.random.default_rng(5700000+L)
 for _ in range(100):
  r=tuple(rng.integers(L,size=3));a,b=sorted(rng.choice(3,2,replace=False));f=face(L,r,a,b)
  if legal(x,f):
   for z,d in f:x[z+(d,)]^=1
 for a,b in itertools.permutations(range(3),2):
  for h in [0,1,L//2]:
   old=O(x,a,b,h)
   for j in range(3):
    ck(abs(O(np.roll(x,1,axis=j),a,b,h)+np.exp(2j*np.pi*h/L*(a==j))*old)<1e-11)
    target=(-1 if b==j else 1)*(old.conjugate() if a==j else old)
    ck(abs(O(reflected(x,j),a,b,h)-target)<1e-11)
# Algebraic adverse: at qpi longitudinal character is+1, transverse is-1.
ck(abs(-np.exp(1j*np.pi)-1)<1e-14);ck(any(abs(O(x,a,b,L//2))>1e-8 for a,b in itertools.permutations(range(3),2)))
s=p.parent/'component-symmetry';out={'actual_check_calls':checks,'all_pass':True,'constructive_rows':rows,'no_L4_or_larger_enumeration':True,'author_derivation_sha256':hashlib.sha256((s/'DERIVATION.md').read_bytes()).hexdigest(),'author_helper_sha256':hashlib.sha256((s/'check.py').read_bytes()).hexdigest()};(p/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
