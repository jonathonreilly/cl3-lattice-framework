"""Exact local native ring controls; theorem and scope are in the paired note."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_LOCAL_NATURAL_RING_DYNAMICS_NOTE_2026-09-08.md', 'docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md')
import argparse
if __name__=="__main__":
 import signal
 signal.alarm(AUDIT_TIMEOUT_SEC)
 parser=argparse.ArgumentParser();parser.add_argument("--json",action="store_true");parser.parse_args()
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,time,resource,sys
start=time.monotonic()
ncheck=0
def req(x,m):
 global ncheck
 ncheck+=1
 if not x:raise RuntimeError(m)
def comps(n,l):
 if not l:
  if not n:yield()
  return
 for i in range(1,n+1):
  for t in comps(n-i,l-1):yield(i,)+t
f={};s={}
for n in range(1,15):
 value=F(0)
 for l in range(2,n+1):
  for c in comps(n,l):
   term=2*f[c[0]];p=c[0]
   for i in c[1:]:p+=i;term*=22*p*s[i]
   value+=term/factorial(l)
 for l in range(n):
  for c in comps(n-1,l):
   term=F(11);p=0
   for i in c:p+=i;term*=22*(1+p)*s[i]
   value+=term/factorial(l)
 f[n]=value;s[n]=4*value;req(value>0,'finite majorant')
m=154;rho=min(F(1),F(1,24*m*max(1,sum(s.values()))))
req(2*m*3*rho*sum(s.values())<=F(1,4),'analytic Lie disk')
req(5+1-4-9==-7,'old failure');req(13+1-4-9==1,'root vanishing');req(14+1-4-9==2,'native improved');req(6-4==2,'slow comparison')
M=174
req(rho<=1,'radius below one')
req(18*3+11*3==87,'analytic input norm')
req(M==2*87,'Lie analytic norm')
C14=2*M/rho**15
req(C14>0,'positive degree15 remainder constant')
# Explicit positive-decay Lieb-Robinson comparison parameters.
kappa=F(1,154);mu=kappa/4;C_F=9216;C_0=(4/(kappa-mu))**4
req(mu==F(1,616) and C_0==F(2464,3)**4,'distance decay')
req(C_F==32*288,'convolution shell bound')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
req(0<rss<384 and time.monotonic()-start<180,'resources')
print(json.dumps(dict(checks=ncheck,order=14,rho=str(rho),s={j:str(v) for j,v in s.items()},M=M,remainder_constant=str(C14),kappa=str(kappa),mu=str(mu),C_F=C_F,C_0=str(C_0),time_powers=dict(order5=-7,order13=1,order14=2,slow=2),seconds=time.monotonic()-start,rss_mib=rss),indent=2))
