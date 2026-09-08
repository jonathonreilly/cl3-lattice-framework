import itertools,json,pathlib,hashlib
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-rk-mobile-variational');O=pathlib.Path(__file__).parent
# Independent occupation-bit CAR actions; operators act right to left.
def op(state,i,create):
 if bool(state>>i&1)==create:return None,0
 return state^(1<<i),(-1)**((state&((1<<i)-1)).bit_count())
def hole(m,x,y):
 b,s=op((1<<m)-1,y,False);b,t=op(b,x,False);return b,s*t
checks=0
for m in range(3,9):
 for x,y,z in itertools.permutations(range(m),3):
  b,s=hole(m,x,y)
  for old,newholes in ((x,(z,y)),(y,(x,z))):
   # electron z -> old transports hole old -> z.
   c,t=op(b,z,False);c,u=op(c,old,True);d,v=hole(m,*newholes)
   if c!=d or s*t*u!=-v:raise RuntimeError('ordered-hole sign')
   checks+=1
# Geometric premise checked on stated cubic family including length-four wrap exception.
rows=[]
for dims in ((4,4,4),(4,4,6),(6,6,6)):
 vs=list(itertools.product(*(range(L) for L in dims)));nb={}
 for v in vs:
  ns=set()
  for a in range(3):
   for s in (-1,1):
    w=list(v);w[a]=(w[a]+s)%dims[a];ns.add(tuple(w))
  nb[v]=ns
 maxcommon=max(len(nb[x]&nb[y]) for x,y in itertools.combinations(vs,2))
 if maxcommon!=2 or any(nb[x]&nb[y] for x in vs for y in nb[x]):raise RuntimeError('geometry')
 rows.append({'extents':dims,'max_common_neighbors':maxcommon,'triangle_free':True})
out={'CAR_signed_hole_moves':checks,'geometry':rows,'source_sha':hashlib.sha256((P/'DERIVATION.md').read_bytes()).hexdigest(),'scope':'Independent CAR bit actions and finite geometry controls; no import of author checker.'}
(O/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
