# Exact nonnative finite-vector dual identity and sequential proposal controls.
from fractions import Fraction as F
import json
add=lambda a,b:[x+y for x,y in zip(a,b)]
sc=lambda c,a:[c*x for x in a]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
mv=lambda M,a:[dot(r,a)for r in M]
H=[[F(2),F(1)],[F(1),F(3)]];J=[[F(0),F(2)],[F(-2),F(0)]];T=[[F(1),F(1)],[F(1),F(-1)]]
count=0
for n in [1,2,3]:
 x=[F(n),F(-2)];v=[F(1),F(n)];e=[F(1,4),F(n,8)];f=[F(-1,3),F(1,5)]
 u=mv(T,x);w=add(sc(2,mv(T,x)),sc(-1,mv(T,v)));Ju=mv(J,u);Hu=mv(H,u);t=dot(u,Hu)/dot(Hu,Hu);z=sc(-t,u);vv=add(w,sc(-t,Ju));Hvv=mv(H,vv);s=dot(vv,Hvv)/dot(Hvv,Hvv);y=sc(s,vv)
 a=add(add(w,sc(-1,mv(H,y))),mv(J,z));b=add(sc(-1,u),sc(-1,mv(H,z)))
 assert a==add(add(w,sc(-s,mv(H,w))),add(sc(-t,Ju),sc(s*t,mv(H,Ju))));assert b==add(sc(-1,u),sc(t,Hu));count+=2
 r=mv(H,e);ss=add(mv(H,f),mv(J,e));corr=dot(r,y)+dot(ss,z)
 assert corr==s*dot(r,w)-s*t*dot(r,Ju)-t*dot(ss,u);count+=1
 obj=lambda X,V:dot(X,mv(T,X))-dot(X,mv(T,V))
 rem=dot(e,mv(T,e))-dot(e,mv(T,f));assert obj(add(x,e),add(v,f))-obj(x,v)-corr==dot(e,a)+dot(f,b)+rem;count+=1
 assert 0<t<=4 and 0<s<=4;count+=1
print(json.dumps({'checks':count,'native_values':0,'scope':'finite exact dual signs and sequential proposals'}))
