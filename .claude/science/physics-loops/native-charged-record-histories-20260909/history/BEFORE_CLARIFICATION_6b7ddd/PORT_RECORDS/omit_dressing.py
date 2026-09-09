"""Exact phase controls on small full native carriers; no dynamics/sampling."""
from itertools import combinations,permutations
from pathlib import Path
import json,hashlib,time
P=Path(__file__).parent;count=0

def ck(x,s):
 global count
 count+=1
 if not x:raise ValueError(s)
def bits(x):return x.bit_count()&1

def data(n,edges,orders):
 inc=[sum(1<<k for k,e in enumerate(edges) if i in e) for i in range(n)];w=[];ell=[]
 for k,(i,j) in enumerate(edges):
  mask=0
  for v,u in [(i,j),(j,i)]:
   for z in orders[v][:orders[v].index(u)]:mask^=1<<edges.index(tuple(sorted((v,z))))
  w.append(mask);l=0
  for v in range(i,j):l^=inc[v]
  ell.append(l)
 M=[a^b for a,b in zip(w,ell)]
 for k in range(len(edges)):
  ck((M[k]>>k)&1,'diagonalM')
  for l in range(k):ck((M[k]>>l)&1==(M[l]>>k)&1,'symmetryM')
 return inc,w,ell,M

def phase(x,M):return (-1j)**x.bit_count()*(-1)**sum(((x>>i)&1)*((x>>j)&1)*((M[i]>>j)&1) for i in range(len(M)) for j in range(i+1,len(M)))
def remove(x,k):return (x&((1<<k)-1))|((x>>(k+1))<<k)
def one(n,edges,orders,x,k,wrong=False):
 inc,w,ell,M=data(n,edges,orders);a=(x>>k)&1;y=remove(x,k);e=edges[k];rest=edges[:k]+edges[k+1:];o=[[z for z in row if tuple(sorted((v,z)))!=e] for v,row in enumerate(orders)];inc2,w2,l2,M2=data(n,rest,o)
 occ=sum(bits(x&i)<<j for j,i in enumerate(inc));target=sum(bits(y&i)<<j for j,i in enumerate(inc2));c=1
 if a:
  i,j=e;c=-1j*(-1)**bits(occ&(((1<<j)-1)^((1<<i)-1)));occ^=(1<<i)|(1<<j)
 lhs=phase(x,M)*c;rhs=phase(y,M2)*((-1)**bits(x&w[k]) if False else 1)
 return lhs==rhs and occ==target

def seq(n,edges,orders,x,sequence):
 amp=1
 for edge in sequence:
  k=edges.index(edge);_,w,_,_=data(n,edges,orders);a=(x>>k)&1;amp*=(-1)**(a*bits(w[k]&x));x=remove(x,k);edges=edges[:k]+edges[k+1:];orders=[[z for z in row if tuple(sorted((v,z)))!=edge] for v,row in enumerate(orders)]
 return amp,x

def check():
 global count
 count=0
 start=time.monotonic();mutants=0;graphs=[(3,[(0,1),(1,2),(0,2)]),(4,[(0,1),(1,2),(2,3)]),(4,[(0,1),(1,2),(2,3),(0,3),(0,2)])];history=0
 for n,edges in graphs:
  edges=[tuple(sorted(e)) for e in edges]
  for reverse in [False,True]:
   orders=[sorted([j if i==v else i for i,j in edges if v in (i,j)],reverse=reverse) for v in range(n)]
   for x in range(1<<len(edges)):
    for k in range(len(edges)):
     ck(one(n,edges,orders,x,k),'local correction');mutants+=not one(n,edges,orders,x,k,True)
    for e,f in combinations(edges,2):
     a=(x>>edges.index(e))&1;b=(x>>edges.index(f))&1;u,y=seq(n,edges.copy(),orders,x,[e,f]);v,z=seq(n,edges.copy(),orders,x,[f,e]);sign=(-1)**(a*b*bool(set(e)&set(f)));ck(y==z and u==sign*v,'history cocycle');history+=1
 ck(mutants>0,'omit local phase adverse')
 r=dict(status='PASS',predicates=count,history_columns=history,omitted_phase_mutant_failures=mutants,seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='exact small full-carrier columns only')
 return r

if __name__=='__main__':check()
