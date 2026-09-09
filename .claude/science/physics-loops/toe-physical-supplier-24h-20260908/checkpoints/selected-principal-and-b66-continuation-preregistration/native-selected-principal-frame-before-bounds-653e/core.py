"""Source-only exact rational certificate; no input loader or candidate factorizer."""
from fractions import Fraction as F
from math import isqrt

def sqrt_upper(x,bits=256):
 if x<0:raise ValueError('negative norm square')
 q=1<<bits;n=(x.numerator*q*q)//x.denominator;r=isqrt(n)
 if F(r*r,q*q)<x:r+=1
 return F(r,q)
def transpose(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*B)]for row in A]
def fro(A):return sqrt_upper(sum((x*x for row in A for x in row),F(0)))
def certificate(G0,radii,T,E,persist=lambda stage,data:None):
 p=len(T)
 if not 0<p<=48 or any(len(row)!=p for A in (G0,radii,T) for row in A) or len(G0)!=p or len(radii)!=p:raise ValueError('dimensions')
 if not E or any(len(row)!=p for row in E):raise ValueError('embedding')
 if any(type(x)is not F for A in (G0,radii,T,E)for row in A for x in row):raise ValueError('exact Fraction inputs only')
 if any(T[i][i]<=0 or any(T[i][j] for j in range(i))for i in range(p)):raise ValueError('positive upper candidate')
 if any(radii[i][j]<0 or G0[i][j]!=G0[j][i] or radii[i][j]!=radii[j][i]for i in range(p)for j in range(p)):raise ValueError('symmetric enclosure')
 persist('candidate',{'T':T,'G0':G0,'radii':radii})
 H=mm(transpose(T),mm(G0,T));persist('H_center',H)
 D=[[H[i][j]-F(i==j) for j in range(p)]for i in range(p)]
 # ||T||_2² <= ||T||_F². No floating stability premise.
 eta=fro(radii);t2=sum((x*x for row in T for x in row),F(0));e=fro(D)+t2*eta
 persist('residual',{'D':D,'eta_G':eta,'e':e,'delta':e})
 if e>=1:return {'status':'INDETERMINATE_RESIDUAL','e':e}
 C0=mm(E,T);B=e/(1-e)**2;bc=fro(C0)*B
 persist('coefficient_center_bound',{'C0':C0,'B':B,'entry_radius':bc})
 l1=max(sum(abs(C0[i][j])+bc for i in range(len(E)))for j in range(p))
 return {'status':'CERTIFIED_ENCLOSURE','C0':C0,'entry_radius':bc,'width_pass':2*bc<=F(1,2**39),'l1_pass':l1<=2**40,'l1_upper':l1,'e':e,'same_ordered_frame':True}
