import sys; sys.argv=['x']
exec(open('supervisor_control_block03_certificates_base.py').read().split("T0=time.time(); print(\"c1 multiset")[0])
def nice_mid(a,b):
    k=0
    while True:
        m=F(int(((a+b)/2)*2**k),2**k)
        if a<m<b: return m
        k+=1
def certify_region_nice(line,u,v):
    cache={}
    def c(t):
        if t not in cache: cache[t]=6*c1_multiset(line_tr(line,t))[0]-1
        return cache[t]
    stack=[(u,v)]; n=0; maxden=1
    while stack:
        a,b=stack.pop(); ca,cb=c(a),c(b)
        if ca>=0 or cb>=0: return -1,len(cache),maxden
        if max(ca,cb)+36*(b-a)/a<0: n+=1; continue
        if b-a<F(1,10**40): return -1,len(cache),maxden
        m=nice_mid(a,b); maxden=max(maxden,m.denominator); stack.append((a,m)); stack.append((m,b))
    return n,len(cache),maxden
for name,line in LINES.items():
    ivs={}
    for j in (1,2):
        P=POLYS[(name,j)]; iv=[i for i in P.intervals(eps=sp.Rational(1,10**20)) if i[0][0]>0][0][0]
        ivs[j]=(F(int(iv[0].p),int(iv[0].q)),F(int(iv[1].p),int(iv[1].q)))
    lo=min(ivs[1],ivs[2]); hi=max(ivs[1],ivs[2]); u=lo[1]; v=hi[0]
    T0=time.time(); n,ev,md=certify_region_nice(line,u,v)
    print(f"{name} region certificate on [{float(u):.12f},{float(v):.12f}]: intervals {n}, evaluations {ev}, max dyadic denominator 2^{md.bit_length()-1} [{time.time()-T0:.1f}s]")
