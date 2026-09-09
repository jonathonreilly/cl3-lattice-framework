from fractions import Fraction as F
import importlib.util,json
from pathlib import Path
p=Path(__file__).with_name('ledger.py');sp=importlib.util.spec_from_file_location('width_ledger',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
n=0
def req(x):
 global n
 if not x:raise ValueError('tiny budget identity')
 n+=1
# Synthetic scalar intervals only, no file inputs other than formula source.
s=F(1);t=F(2);x=F(4);As=1/(x+s*s);At=1/(x+t*t);Ap=-2*s/(x+s*s)**2
r,_=m.node(s,(t,t),(At,At),(As,As),(Ap,Ap),(F(1),F(1)));req(r==(0,0))
e=F(1,10**30);r,_=m.node(s,(t,t),(At-e,At+e),(As,As),(Ap,Ap),(F(1),F(1)));req(r[0]==F(4,3)*e);req(r[1]==F(8,9)*e)
try:m.node(s,(s,s),(At,At),(As,As),(Ap,Ap),(F(1),F(1)))
except ValueError:req(True)
else:req(False)
# Symbolic finite-N tail dependency verified through two arbitrary As values.
for N in [2,4]:
 def part(aa):
  c=1-s*s*aa;z=F(0)
  for j in range(N):
   z+=(-1)**j*c/F((2*j+1)*8**(2*j+1));c=x**(j+1)-s*s*c
  return z
 k=sum(s**(2*j+2)/F((2*j+1)*8**(2*j+1))for j in range(N))
 req(part(As+e)-part(As)==-k*e)
req(128*F(1,4**52)<F(1,10**28))
print(json.dumps({'status':'PASS','checks':n,'scope':'synthetic width and finite-series identities; no66pole/catalog/tail40 scan'},indent=2))
