"""Exact local native ring controls; theorem and scope are in the paired note."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_LOCAL_NATURAL_RING_DYNAMICS_NOTE_2026-09-08.md', 'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md')
import argparse
if __name__=="__main__":
 import signal
 signal.alarm(AUDIT_TIMEOUT_SEC)
 parser=argparse.ArgumentParser();parser.add_argument("--json",action="store_true");parser.parse_args()
from fractions import Fraction as F
import json,math,time,resource,sys,hashlib
from pathlib import Path
import signal

start=time.monotonic();checks=0
N=16;order=14
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
def add(a,b,scale=F(1)):
 c=a.copy()
 for k,v in b.items():
  c[k]=c.get(k,F(0))+scale*v
  if c[k]==0:del c[k]
 return c
def mul(a,b):
 c={};rows={}
 for (k,j),v in b.items():rows.setdefault(k,[]).append((j,v))
 for (i,k),u in a.items():
  for j,v in rows.get(k,[]):c[(i,j)]=c.get((i,j),F(0))+u*v
 return {k:v for k,v in c.items() if v}
def pcomm(a,b):
 c=[{} for _ in range(order+1)]
 for n in range(order+1):
  for i in range(n+1):c[n]=add(c[n],add(mul(a[i],b[n-i]),mul(b[n-i],a[i]),F(-1)))
 return c
def transformed(s,h):
 out=[d.copy() for d in h];term=h
 for k in range(1,order+1):
  term=pcomm(s,term)
  for n in range(order+1):out[n]=add(out[n],term[n],F(1,math.factorial(k)))
 return out
bits=(0,1,0,1);inc=((0,3),(0,1),(1,2),(2,3));masks=(0,0,0,0)
energy=[]
for m in range(N):
 delta=[(bits[e]^(m>>e&1))-bits[e] for e in range(4)]
 energy.append(sum((delta[a]+delta[b])**2 for a,b in inc))
ice=[m for m,d in enumerate(energy) if d==0];req(ice==[0,15],'rank two ice')
d={(i,i):F(e) for i,e in enumerate(energy) if e};v={}
for m in range(N):
 for e in range(4):v[(m^(1<<e),m)]=F((-1)**((m&masks[e]).bit_count()))
h=[d,v]+[{} for _ in range(order-1)];s=[{} for _ in range(order+1)];coeff=[]
for j in range(1,order+1):
 r=transformed(s,h)[j]
 s[j]={(a,b):value/(energy[a]-energy[b]) for (a,b),value in r.items() if energy[a]!=energy[b]}
 req(all(s[j].get((b,a),F(0))==-value for (a,b),value in s[j].items()),'antihermitian generator')
 full=transformed(s,h)
 for n in range(1,j+1):req(all(energy[a]==energy[b] for a,b in full[n]),'all D-offdiagonal cancelled')
 coeff.append(full[j])
def restrict(a):return {(i,j):value for (i,j),value in a.items() if i in ice and j in ice}
p={(i,i):F(1) for i in ice};r={(i,i):F(1,e) for i,e in enumerate(energy) if e}
second=mul(mul(mul(p,v),r),mul(v,p));req(restrict(coeff[1])=={k:-val for k,val in second.items()},'second resolvent coefficient')
word=p
for mat in (v,r,v,r,v,r,v,p):word=mul(word,mat)
reference=add({k:-val for k,val in word.items()},p,F(2))
req(restrict(coeff[3])==reference,'fourth folded resolvent coefficient')
req(reference=={(0,0):F(3,2),(15,15):F(3,2),(0,15):F(1,2),(15,0):F(1,2)},'absolute native fourth matrix')
for j in range(0,order,2):req(restrict(coeff[j])=={},'odd ice vanishes')
req(restrict(coeff[3])!={k:-val for k,val in word.items()},'missing folded actual negative control')
swrong=[{} for _ in range(order+1)];swrong[1]={k:-val for k,val in s[1].items()};wrong=transformed(swrong,h)
req(any(energy[a]!=energy[b] for a,b in wrong[1]),'wrong inverse sign actual negative control')
# Slow local extension agrees only on ice, up to scalar terms.
for j in range(1,order+1):
 lj=coeff[j-1] if j>=6 else (add(reference,p,F(-3,2)) if j==4 else {})
 scalar=F(-2) if j==2 else (F(3,2) if j==4 else F(0))
 req(restrict(add(coeff[j-1],lj,F(-1)))=={k:scalar*val for k,val in p.items() if scalar*val},'slow extension ice restriction')
req(bool(coeff[0]) and not restrict(coeff[0]),'fast excited sector remains nonzero')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
req(time.monotonic()-start<180 and 0<rss<384,'resources')
print(json.dumps(dict(checks=checks,order=order,ice=ice,ice_fourth={str(k):str(val) for k,val in reference.items()},coefficients=[{str(k):str(v) for k,v in c.items()} for c in coeff],seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
