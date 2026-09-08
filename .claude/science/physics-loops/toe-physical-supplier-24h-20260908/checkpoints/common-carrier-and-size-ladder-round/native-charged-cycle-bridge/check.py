import itertools,json,hashlib,time
from pathlib import Path
start=time.monotonic()
counts=dict(star_assignments=0,low_active=0,accepted=0,rejected=0,face_patterns=0)
rows=set()
for bits in itertools.product((0,1),repeat=11):
 n=bits[0]; gi=n+sum(bits[1:6])-3; gj=n+sum(bits[6:])-3
 counts['star_assignments']+=1
 if abs(gi)>1 or abs(gj)>1: continue
 bi=(-1)**(gi+3); bj=(-1)**(gj+3)
 assert (1+bi)//2==gi*gi and (1+bj)//2==gj*gj
 if bi==bj: continue
 counts['low_active']+=1
 d=1-2*n; hi,hj=gi+d,gj+d
 if abs(hi)>1 or abs(hj)>1:
  counts['rejected']+=1;continue
 counts['accepted']+=1; rows.add((gi,gj,n,hi,hj))
 for ep in (1,-1):
  q=(ep*gi,-ep*gj); r=(ep*hi,-ep*hj)
  assert sum(q)==sum(r)
  assert sum(x==1 for x in q)==sum(x==1 for x in r)
  assert sum(x==-1 for x in q)==sum(x==-1 for x in r)
  assert sum(x*x for x in q)==sum(x*x for x in r)==1
  assert r[0]-q[0]==ep*d and r[1]-q[1]==-ep*d
for b in itertools.product((0,1),repeat=4):
 counts['face_patterns']+=1
 changes=[2-2*(b[k-1]+b[k]) for k in range(4)]
 alternating=all(b[k]!=b[(k+1)%4] for k in range(4))
 assert (all(x==0 for x in changes))==alternating
assert counts['rejected']>0 and counts['accepted']>0
assert len(rows)==4
out={'counts':counts,'allowed_transitions':sorted(rows),'scope':'Exact diagonal support/charge truth tables, not Pauli phase or statistics verification','seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2,allow_nan=False))
