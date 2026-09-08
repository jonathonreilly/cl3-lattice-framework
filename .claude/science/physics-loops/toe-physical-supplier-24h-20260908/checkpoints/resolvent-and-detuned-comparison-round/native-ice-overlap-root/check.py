"""Independent bit-level native Pauli and incidence controls. Standard library only."""
import collections
import fractions
import hashlib
import itertools
import json
import pathlib
import resource
import time

START = time.monotonic()
checks = 0
def require(p, why):
    global checks
    checks += 1
    if not p:
        raise RuntimeError(why)

def rank(rows):
    piv = {}
    for x in rows:
        while x:
            b = x.bit_length()-1
            if b in piv:
                x ^= piv[b]
            else:
                piv[b] = x
                break
    return len(piv)

def mul(a, b):
    # i^p X^x Z^z, so Z from the left crosses X from the right.
    p,x,z = a
    q,y,w = b
    return ((p+q+2*((z&y).bit_count()%2))%4, x^y, z^w)

def commute(a,b):
    return ((a[1]&b[2]).bit_count()+(a[2]&b[1]).bit_count())%2 == 0

results = []
for L in (4,6,8):
    vertices = list(itertools.product(range(L),repeat=3))
    ids = {r:i for i,r in enumerate(vertices)}
    edges = []
    directional = {}
    for r in vertices:
        for a in range(3):
            t = list(r); t[a]=(t[a]+1)%L
            directional[r,a] = len(edges)
            edges.append((ids[r], ids[tuple(t)]))
    V,E = len(vertices),len(edges)
    require(len(set(tuple(sorted(e)) for e in edges))==E, 'simple graph')
    adjacency = [[] for _ in vertices]
    incidence = [0]*V
    lookup = {}
    for e,(u,v) in enumerate(edges):
        adjacency[u].append((v,e)); adjacency[v].append((u,e))
        incidence[u] |= 1<<e; incidence[v] |= 1<<e
        lookup[min(u,v),max(u,v)] = e
    require(all(x.bit_count()==6 for x in incidence),'degree six')
    require(rank(incidence)==V-1,'incidence rank')
    parent={0:None}; pedge={}; queue=collections.deque([0]); tree=set()
    while queue:
        u=queue.popleft()
        for v,e in adjacency[u]:
            if v not in parent:
                parent[v]=u; pedge[v]=e; tree.add(e); queue.append(v)
    require(len(parent)==V,'connected')
    cycles=[]; paths=[]
    for e,(u,v) in enumerate(edges):
        if e in tree: continue
        pu=[u]; pv=[v]
        while parent[pu[-1]] is not None: pu.append(parent[pu[-1]])
        while parent[pv[-1]] is not None: pv.append(parent[pv[-1]])
        vi={w:i for i,w in enumerate(pv)}
        iu=next(i for i,w in enumerate(pu) if w in vi)
        jv=vi[pu[iu]]
        path=pu[:iu+1]+list(reversed(pv[:jv]))+[u]
        mask=0
        for a,b in zip(path,path[1:]): mask ^= 1<<lookup[min(a,b),max(a,b)]
        require(all((mask & x).bit_count()%2==0 for x in incidence),'cycle boundary')
        cycles.append(mask); paths.append(path)
    require(rank(cycles)==E-V+1,'cycle rank')
    seed=0
    for (r,a),e in directional.items():
        if r[a]%2: seed |= 1<<e
    require(all((seed&x).bit_count()==3 for x in incidence),'ice seed')
    r=(0,0,0); rx=(1,0,0); ry=(0,1,0)
    emptyface=sum(1<<directional[s,a] for s,a in ((r,0),(r,1),(rx,1),(ry,0)))
    require(not(seed&emptyface),'empty face')
    new=seed^emptyface
    require(all((new&x).bit_count()%2==1 for x in incidence),'preserved odd parity')
    degrees=[(new&x).bit_count() for x in incidence]
    require(degrees.count(5)==4 and degrees.count(3)==V-4,'outside ice')
    chosen={ids[r] for r in vertices if all(x%2==0 for x in r)}
    k=len(chosen)
    stars=0
    for u in chosen:
        require(not(stars&incidence[u]),'disjoint stars')
        stars |= incidence[u]
    remaining=((1<<E)-1)^stars
    residual=[x&remaining for u,x in enumerate(incidence) if u not in chosen]
    require(rank(residual)==V-k-1,'connected complement incidence rank')
    completion=remaining.bit_count()-rank(residual)
    require(completion==E-V-5*k+1 and 5*k+completion==E-V+1,'constant completion dimension')
    if L==4:
        As={}
        for e,(u,v) in enumerate(edges):
            z=0
            for target,other in ((u,v),(v,u)):
                for neighbor,f in adjacency[target]:
                    if neighbor<other: z ^= 1<<f
            As[u,v]=(0 if u<v else 2,1<<e,z)
            As[v,u]=(2 if u<v else 0,1<<e,z)
        Bs=[(0,0,x) for x in incidence]
        for (u,v),a in As.items():
            require(mul(a,a)==(0,0,0),'A involution')
            require(all(commute(a,b)==(i not in (u,v)) for i,b in enumerate(Bs)),'A B relation')
        stabilizers=[]
        for path,mask in zip(paths,cycles):
            s=((len(path)-1)%4,0,0)
            for u,v in zip(path,path[1:]): s=mul(s,As[u,v])
            require(s[1]==mask,'cycle X support')
            require(mul(s,s)==(0,0,0),'cycle Hermitian involution')
            require(all(commute(s,a) for a in As.values()),'cycle A centrality')
            require(all(commute(s,b) for b in Bs),'cycle B centrality')
            stabilizers.append(s)
        require(all(commute(s,t) for i,s in enumerate(stabilizers) for t in stabilizers[:i]),'mutual cycle commutation')
        require(rank([s[1]|(s[2]<<E) for s in stabilizers]+[x<<E for x in incidence])==E,'one-dimensional fixed B code block')
    bound=fractions.Fraction(5,8)**k
    results.append(dict(L=L,V=V,E=E,cycle_rank=E-V+1,selected_stars=k,completion_bits=completion,overlap_squared_bound=str(bound),overlap_bound_float=float(bound),native_paulis_checked=L==4))
elapsed=time.monotonic()-START
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2
require(elapsed<180 and rss<384,'resource budget')
out=dict(status='PASS',checks=checks,seconds=elapsed,peak_MiB=rss,results=results,script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
pathlib.Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
