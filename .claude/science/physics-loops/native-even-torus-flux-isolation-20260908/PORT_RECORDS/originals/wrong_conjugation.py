"""Exact finite controls of analytical lemmas, not a proof by finite census."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse,json,hashlib,signal,time,resource,sys
class Q:
 def __init__(self,r=0,i=0):self.r=F(r);self.i=F(i)
 def __add__(self,b):
  b=q(b);return Q(self.r+b.r,self.i+b.i)
 __radd__=__add__
 def __neg__(self):return Q(-self.r,-self.i)
 def __sub__(self,b):return self+-q(b)
 def __mul__(self,b):
  b=q(b);return Q(self.r*b.r-self.i*b.i,self.r*b.i+self.i*b.r)
 __rmul__=__mul__
 def conj(self):return Q(self.r,-self.i)
 def __truediv__(self,b):
  b=q(b);v=self*b.conj();d=b.r*b.r+b.i*b.i;return Q(v.r/d,v.i/d)
 def __eq__(self,b):b=q(b);return self.r==b.r and self.i==b.i
 def norm(self):return self.r*self.r+self.i*self.i
def q(a):return a if isinstance(a,Q) else Q(a)
def mat(a):return [[q(v) for v in r] for r in a]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def adj(a):return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]
def bar(a):return [[x.conj() for x in row] for row in a]
def trans(a):return list(map(list,zip(*a)))
def tr(a):return sum(a[i][i] for i in range(len(a)))
def energy(A,B,C,X):
 Xd=adj(X);v=tr(mul(Xd,mul(A,X)))+tr(mul(Xd,mul(X,trans(B))))
 for c in C:v-=tr(mul(Xd,mul(mul(c,X),trans(c))))
 return v
count=0
def ck(c,label):
 global count;count+=1
 if not c:raise ValueError(label)
def run():
 I=mat([[1,0],[0,1]]);a=mat([[0,1],[0,0]]);C=[a,adj(a)]
 ck(all(any(c==adj(d) for d in C) for c in C),'paired channels')
 U=mat([[F(3,5),Q(0,F(4,5))],[Q(0,F(4,5)),F(3,5)]]);V=mat([[Q(0,F(5,13)),Q(0,F(12,13))],[-F(12,13),F(5,13)]])
 ck(mul(adj(U),U)==I and mul(adj(V),V)==I,'unitary complex frames')
 for s in (1,2,3):
  D=mat([[1,0],[0,s]]);X=mul(mul(U,D),adj(V));Y=mul(mul(U,D),adj(U));Z=mul(mul(V,D),adj(V))
  A=mat([[2,Q(F(2,3),F(3,7))],[Q(F(2,3),-F(3,7)),-1]]);B=mat([[3,Q(-F(1,5),F(4,9))],[Q(-F(1,5),-F(4,9)),4]])
  defect=energy(A,B,C,X)-(energy(A,A,C,Y)+energy(bar(B),B,C,Z))/2
  square=F(0)
  for c in C:
   aa=mul(mul(adj(U),c),U);bb=mul(mul(adj(V),c),V)
   square+=sum(F((1,s)[i]*(1,s)[j],2)*(aa[i][j]-bb[i][j]).norm() for i in range(2) for j in range(2))
  ck(defect==square,'complex reflected weighted square')
 # Kernel fixture: v=e1, X=|0><0|. Paired channel positivity excludes it.
 X=mat([[1,0],[0,0]]);total=sum(mul(mul(c,X),adj(c))[1][1] for c in C)
 ck(total==1,'kernel paired positivity');ck(mul(mul(a,X),adj(a))[1][1]==0,'unpaired adverse kernel')
 ck(energy(mat([[F(1,2),0],[0,F(1,2)]]),mat([[F(1,2),0],[0,F(1,2)]]),C,I)==0,'faithful PSD ground eigenenergy')
 phases=[Q(1),Q(-1),Q(0,1),Q(0,-1),Q(F(3,5),F(4,5))]
 for width in range(2,9):
  vertices=list(product(range(width),range(4),range(6)));known={v:Q(1) for v in vertices if v[0] in (0,width-1)};g={v:(Q(1) if v in known else phases[(v[0]+2*v[1]+3*v[2])%5]) for v in vertices};A={}
  for v in vertices:
   for axis in range(3):
    w=list(v);w[axis]+=1
    if axis==0 and w[0]==width:continue
    if axis:w[axis]%= (4 if axis==1 else 6)
    w=tuple(w)
    if (v,w) in A:continue
    value=phases[(sum(v)+axis)%5]*F(1+axis,2);A[v,w]=value;A[w,v]=value.conj()
  H={(v,w):g[v].conj()*a*g[w] for (v,w),a in A.items()}
  while len(known)<len(vertices):
   new={}
   for v in list(known):
    unknown=[w for x,w in A if x==v and w not in known]
    if len(unknown)!=1:continue
    w=unknown[0];z=H[v,w]/(known[v].conj()*A[v,w]);ck(z.norm()==1,'phase norm');ck(z==g[w],'recovered phase')
    if w in new:ck(new[w]==z,'opposite frontier consistency')
    new[w]=z
   ck(bool(new),'layer progress');known.update(new)
  ck(len(known)==len(vertices),'full CAR generation support')
  for (v,w),a in A.items():ck(H[v,w]==known[v].conj()*a*known[w],'all hopping coefficients')
 return count
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args();signal.alarm(180);t=time.monotonic();n=run();rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
 ck(time.monotonic()-t<180 and 0<rss<384,'resources');print(json.dumps(dict(checks=count,seconds=time.monotonic()-t,rss_mib=rss,scope='exact finite lemma controls; analytical all-even proof separate')))
