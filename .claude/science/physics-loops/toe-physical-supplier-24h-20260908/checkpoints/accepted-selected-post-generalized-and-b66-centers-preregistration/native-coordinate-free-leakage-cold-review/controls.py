from fractions import Fraction as F
import json
n=0
def req(x):
 global n
 if not x:raise ValueError('independent exact identity')
 n+=1
def mat(x):return [[F(v)for v in r]for r in x]
def tr(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum((x*y for x,y in zip(r,c)),F(0))for c in zip(*b)]for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)]for r,s in zip(a,b)]
def scale(a,c):return [[x*c for x in r]for r in a]
S=mat([[1,1],[0,2],[0,0]]);K=mat([[0,-2,-1],[2,0,-3],[1,3,0]]);T=mat([[1,F(-1,2)],[0,F(1,2)]])
G=mul(tr(S),S);J=mul(mul(tr(S),K),S);KS=mul(K,S);D=mul(tr(KS),KS);Gi=mat([[F(5,4),F(-1,4)],[F(-1,4),F(1,4)]])
L=add(D,mul(mul(J,Gi),J));req(L==mat([[1,7],[7,49]]));req(J==scale(tr(J),-1))
P=mul(mul(S,Gi),tr(S));req(mul(P,P)==P);req(P==mat([[1,0,0],[0,1,0],[0,0,0]]))
H=mul(mul(tr(T),G),T);A=mul(mul(tr(T),J),T);C=mul(mul(tr(T),D),T);N=add(C,mul(A,A));req(H==mat([[1,0],[0,1]]));req(N==mat([[1,3],[3,9]]));req(N==mul(mul(tr(T),L),T));req(N[0][0]+N[1][1]==10);req(N[0][0]*N[1][1]-N[0][1]**2==0)
# Test vector attaining generalized quotient10: T*(1,3).
x=mul(T,mat([[1],[3]]));num=mul(mul(tr(x),L),x)[0][0];den=mul(mul(tr(x),G),x)[0][0];req(num/den==10)
for eps in [F(1,100),F(1,1000000)]:
 X=scale(H,1-eps);N0=add(C,mul(mul(A,X),A));req(add(N0,scale(N,-1))==scale(H,4*eps));q=4*eps
 req(max(sum(abs(v)for v in r)for r in N0)+q>=10);req((N0[0][0]-q)/H[0][0]<=10)
print(json.dumps({'status':'PASS','checks':n,'scope':'independent finite skew generator and nonorthogonal trial seeds; no native data'},indent=2))
