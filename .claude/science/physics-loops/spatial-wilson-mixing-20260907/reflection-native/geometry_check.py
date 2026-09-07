import itertools,json,hashlib,time
from pathlib import Path
start=time.monotonic();verts=list(itertools.product((0,1),repeat=4));edges=[]
for v in verts:
 for a in range(4):
  if not v[a]:
   w=list(v);w[a]=1;edges.append((v,tuple(w)))
def face(a,b,fixed):
 v=[0]*4
 for j,value in fixed.items():v[j]=value
 p=[tuple(v)];v[a]=1;p.append(tuple(v));v[b]=1;p.append(tuple(v));v[a]=0;p.append(tuple(v))
 return [(u,w) if (u,w) in edges else (w,u) for u,w in zip(p,p[1:]+p[:1])],[1 if (u,w) in edges else -1 for u,w in zip(p,p[1:]+p[:1])]
faces=[]
for a,b in itertools.combinations(range(4),2):
 other=[j for j in range(4) if j not in (a,b)]
 for vals in itertools.product((0,1),repeat=2):
  fixed=dict(zip(other,vals));es,signs=face(a,b,fixed)
  faces.append(dict(axes=(a,b),fixed=fixed,edges=es,signs=signs,weight='t' if b==3 else 'a',omitted=(a,b)==(0,1) and fixed[2]==0))
assert len(edges)==32 and len(faces)==24
active=[f for f in faces if not f['omitted']];assert len(active)==22
cross=[f for f in active if 0 in f['axes']];internal=[f for f in active if 0 not in f['axes']]
assert len(cross)==10 and sum(f['weight']=='a' for f in cross)==6
for f in cross:
 kept=[(e,s) for e,s in zip(f['edges'],f['signs']) if e[0][0]==e[1][0]]
 assert len(kept)==2
 assert kept[0][0][0][1:]==kept[1][0][0][1:] and kept[0][0][1][1:]==kept[1][0][1][1:]
 assert kept[0][1]==-kept[1][1]
left=[f for f in internal if f['fixed'][0]==0];right=[f for f in internal if f['fixed'][0]==1]
assert len(left)==len(right)==6 and sum(f['weight']=='a' for f in left)==2
patterns=[]
for f in left:
 word=[]
 for e,s in zip(f['edges'],f['signs']):
  a=next(j for j in range(4) if e[0][j]!=e[1][j])
  if a==1 and e[0][2]==0:word.append(('U' if e[0][3]==0 else 'V',s))
 patterns.append((f['weight'],word))
assert sorted((w,len(p)) for w,p in patterns)==[('a',1),('a',1),('t',0),('t',0),('t',0),('t',2)]
assert next(p for w,p in patterns if len(p)==2)==[('U',1),('V',-1)]
print(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),vertices=16,edges=32,active_faces=22,cross_faces=cross,half_faces=left,identity_specialization=patterns,seconds=time.monotonic()-start),indent=2))
