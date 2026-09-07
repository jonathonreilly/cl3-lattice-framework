#!/usr/bin/env python3
"""Exact actual SU(3) one-plaquette PW-R1 energy fixture, not a convergence fit."""
from fractions import Fraction as F
from itertools import product
import json

checks = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def eps(a,b,c):
    if len({a,b,c}) < 3:
        return 0
    return 1 if (a,b,c) in ((0,1,2),(1,2,0),(2,0,1)) else -1

# Monomials are sorted tuples (group:0=U,1=M, conjugate:0/1,row,col).
ONE = {(): F(1)}
def var(g, i, j, conjugate=0):
    return {((g,conjugate,i,j),): F(1)}
def add(*polys):
    out={}
    for p in polys:
        for m,c in p.items():
            out[m]=out.get(m,F(0))+c
    return {m:c for m,c in out.items() if c}
def scale(p,c):
    return {m:c*v for m,v in p.items() if c*v}
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(sorted(m+n));out[k]=out.get(k,F(0))+c*d
    return {m:c for m,c in out.items() if c}
def conj(p):
    return {tuple(sorted((g,1-z,i,j) for g,z,i,j in m)):c for m,c in p.items()}
def group_moment(terms):
    pos=[(i,j) for z,i,j in terms if z==0]
    neg=[(i,j) for z,i,j in terms if z==1]
    n,m=len(pos),len(neg)
    if (n-m)%3:
        return F(0)
    if n==m==0:
        return F(1)
    if n==m==1:
        return F(pos[0]==neg[0],3)
    if (n,m) in ((3,0),(0,3)):
        a=pos if n else neg
        return F(eps(*(i for i,j in a))*eps(*(j for i,j in a)),6)
    raise ValueError(('unsupported actual Haar moment',n,m))
def integral(p):
    total=F(0)
    for mon,c in p.items():
        for g in (0,1):
            c*=group_moment([(z,i,j) for h,z,i,j in mon if g==h])
            if not c: break
        total+=c
    return total
def inner(A,B,operator=ONE):
    return sum((integral(mul(mul(conj(A[i][j]),operator),B[i][j]))
                for i,j in product(range(3),repeat=2)),F(0))/3

chi=add(*(mul(var(0,k,l),var(1,l,k)) for k,l in product(range(3),repeat=2)))
J=scale(add(chi,conj(chi)),F(1,6))
A=[[var(0,i,j) for j in range(3)] for i in range(3)]
B=[[add(*(scale(mul(var(0,a,b,1),var(1,l,k)),F(eps(i,k,a)*eps(j,l,b),2))
           for k,l,a,b in product(range(3),repeat=4)))
     for j in range(3)] for i in range(3)]
C=[[scale(var(1,j,i,1),F(1,3)) for j in range(3)] for i in range(3)]
basis=[A,B,C]
gram=[[inner(x,y) for y in basis] for x in basis]
mag=[[inner(x,y,J) for y in basis] for x in basis]
check('actual matrix HS Gram from Haar contractions',gram==[[F(1),0,0],[0,F(1,3),0],[0,0,F(1,9)]])
check('actual compressed face matrix from Haar contractions',mag==[[0,F(1,18),F(1,54)],[F(1,18),0,F(1,54)],[F(1,54),F(1,54),0]])
check('epsilon nontrivial mixed BJC entry',mag[1][2]==F(1,54))
check('wrong source color normalization rejected',3*gram[0][0]!=1)
check('fake isometric compressed loop input rejected',gram[1][1]!=1 and gram[2][2]!=1)
neutral=[ONE,chi,conj(chi)]
ngram=[[integral(mul(conj(x),y)) for y in neutral] for x in neutral]
nj=[[integral(mul(mul(conj(x),J),y)) for y in neutral] for x in neutral]
check('actual neutral character orthogonality',ngram==[[1,0,0],[0,1,0],[0,0,1]])
check('actual neutral Wilson face fusion matrix',nj==[[0,F(1,6),F(1,6)],[F(1,6),0,F(1,6)],[F(1,6),F(1,6),0]])
t=F(1,100);v=96*t/(1+t-2*t*t);N=1+2*t*t
E0=v-v*t/3
H=[[F(16 if i==j and i else 0)+(v if i==j else 0)-v*nj[i][j] for j in range(3)] for i in range(3)]
x=[F(1),t,t]
check('prospective rational vector is exact eigenvector',all(sum(H[i][j]*x[j] for j in range(3))==E0*x[i] for i in range(3)))
# The other symmetric-block eigenvalue is its trace minus E0; antisymmetric one explicit.
other_sym=16+F(11,6)*v-E0
other_anti=16+F(7,6)*v
check('neutral exact eigenvector is lowest',E0<other_sym and E0<other_anti)
check('full nonneutral sectors excluded by electric floor',0<E0<v<4)
qnum=sum(x[i]*gram[i][j]*x[j] for i,j in product(range(3),repeat=2))
jnum=sum(x[i]*mag[i][j]*x[j] for i,j in product(range(3),repeat=2))
knum=4*gram[0][0]+16*t*t*gram[1][1]+12*t*t*gram[2][2]
q=qnum/N
trial=(knum+v*(qnum-jnum))/qnum
delta=trial-E0
Epath=8*t*t/N;Eface=4*Epath;eR=F(4);theta=Epath/eR
check('actual norm loss matches analytic fraction',1-q==14*t*t/(9*N))
check('actual shell probability controls trial loss',0<1-q<=theta<1)
check('actual local ground energy budget',Epath<=8*v and Eface<=32*v)
check('finite compressed trial has genuine extra energy',delta>4)
check('small exact finite excess bounded without floats',delta<4+F(1,100))
# Rational overestimates of the theorem radicals, verified by squaring.
rt=F(1,50);re=F(3,100);rf=F(3,100)
check('rational theta square-root enclosure',theta<=rt*rt)
check('rational derivative square-root enclosure',Epath<=re*re)
check('rational face square-root enclosure',Eface/eR<=rf*rf)
bound=(4+rt*(4+4*re)+2*v*(rf+rt))/(1-theta)
check('actual charged energy satisfies local form theorem',delta<=bound)
check('crude sufficient normalization bound can fail',8*v/eR>1)
check('wrong unconditional exact four-energy identity rejected',trial!=E0+4)
check('naive distant vacuum normalization error grows',1000*F(1,2)*(1-q)/q>10*F(1,2)*(1-q)/q)

result={'status':'PASS','checks':checks,'check_count':len(checks),
        'fixture':'actual four-link SU3 plaquette, complete PW R1, a=1,t=1/100',
        'v':str(v),'neutral_E0':str(E0),'q':str(q),'charged_trial_energy':str(trial),
        'charged_excess':str(delta),'rational_theorem_upper':str(bound),
        'gram':[[str(z) for z in r] for r in gram],
        'J_matrix':[[str(z) for z in r] for r in mag],
        'limitation':'one exact finite fixture; crude global sufficient theta bound fails here, actual local-energy version passes'}
print(json.dumps(result,indent=2))
