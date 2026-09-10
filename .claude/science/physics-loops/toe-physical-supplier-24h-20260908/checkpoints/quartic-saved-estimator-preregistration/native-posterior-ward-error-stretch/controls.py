"""Finite rational toy controls only; never reads native files."""
from fractions import Fraction as F
from itertools import product
import json

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def l1(a):return sum(map(abs,a),F(0))
def t(a):return(6*a[0],-3*a[1])
def g(a):return(a[1],a[0])
def w(x,v):return dot(x,t(x))-dot(x,t(g(v)))
vectors=[(F(0),F(0)),(F(1),F(0)),(F(-1),F(2)),(F(1,3),F(-2,5))];count=0
for x,v,xh,vh in product(vectors,repeat=4):
 E=l1(sub(x,xh));Fv=l1(sub(v,vh));a=l1(xh);b=l1(vh);X=l1(x);V=l1(v);chi=min(X,a+E);psi=min(V,b+Fv)
 err=6*(E*(a+chi)+min(E*b+chi*Fv,E*psi+a*Fv));assert abs(w(x,v)-w(xh,vh))<=err;count+=1
print(json.dumps({'status':'PASS_RATIONAL_TOY','cases':count,'native_files_read':0,'native_moments':0,'scope':'norm inequality smoke controls; proof is algebraic'}))
