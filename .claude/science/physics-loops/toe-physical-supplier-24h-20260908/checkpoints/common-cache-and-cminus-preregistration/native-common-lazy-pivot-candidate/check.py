import pivot,interval as iv
from fractions import Fraction as F
import json
n=0
def ck(v):
 global n
 if not v:raise ValueError('toy check')
 n+=1
# Literal two-dimensional real CAR complex structure; exact orthonormal columns.
def fetch(i,j):return (iv.ONE if i==j else iv.ZERO,iv.rational(0 if i==j else(-1 if i==0 else 1)))
rows=[];r=pivot.compress(fetch,[1,-1],rows.append);ck(r['status']=='CERTIFIED_COMPRESSION');ck(r['pairs']==1);ck(r['history'][0]['index']==0);ck(r['history'][0]['j'][1]==iv.rational(-1));ck(rows[-1]['original_residual_upper']=='0')
ck(pivot.compress(fetch,[1,-1],lambda _:None,maxpairs=0)['status']=='PAIR_CAP')
ck(pivot.compress(lambda i,j:((-iv.S,iv.S),iv.ZERO),[1],lambda _:None)['status']=='PRECISION_STALL')
try:pivot.compress(lambda i,j:((-2*iv.S,-iv.S),iv.ZERO),[1],lambda _:None)
except ValueError:ck(True)
else:ck(False)
# Half transform of two independent pole columns gives half identity and exact chirality zeros.
def base(i,j,a,b):return (iv.ONE if i==j else iv.ZERO,iv.ZERO)
f=pivot.physical_rows(base,[(0,1,0,1),(0,1,0,-1)],F(0),F(0),F(1));ck(f(0,0)[0]==iv.rational(F(1,2)));ck(f(0,1)[0]==iv.ZERO)
ck(F(1,1000)**2/F(2116)*2==F(1,1058000000))
print(json.dumps({'status':'PASS_TINY_EXACT','predicates':n,'native_calls':0}))
