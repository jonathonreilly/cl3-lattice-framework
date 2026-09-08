from itertools import product
from pathlib import Path
import json,hashlib
checks=0;examples=[]
for n in [2,4,8]:
 for pattern in product([False,True],repeat=12):
  tags=[('old',j) for j in range(n+1)];u=hi=lo=0;d=1;run=0;runs=[];hist=[]
  for t,accept in enumerate(pattern):
   if accept:
    if d==1:tags=tags[1:]+[('new',t)]
    else:tags=[('new',t)]+tags[:-1]
    u+=d;run+=1
   else:runs.append(run);run=0;d=-d
   hi=max(hi,u);lo=min(lo,u)
   original={z[1] for z in tags if z[0]=='old'};expected=set(range(hi,n+lo+1))
   if original!=expected:raise RuntimeError('interval')
   if (tags[n//2][0]=='old')!=(hi<=u+n//2<=n+lo):raise RuntimeError('midpoint')
   hist.append((u,hi,lo));checks+=1
  # Reconstruct exact attempt-time path from runlengths, retaining rejected attempts.
  got=[];uu=hh=ll=0;dd=1
  for rr in runs:
   for _ in range(rr):uu+=dd;hh=max(hh,uu);ll=min(ll,uu);got.append((uu,hh,ll))
   got.append((uu,hh,ll));dd=-dd
  for _ in range(run):uu+=dd;hh=max(hh,uu);ll=min(ll,uu);got.append((uu,hh,ll))
  if got!=hist:raise RuntimeError('run reconstruction')
  checks+=1
# Actual wrong formula using only current displacement fails after an excursion and reversal.
tags=[('old',j) for j in range(5)]
for t,d in enumerate([1,1,-1,-1]):tags=tags[1:]+[('new',t)] if d==1 else [('new',t)]+tags[:-1]
if {z[1] for z in tags if z[0]=='old'}==set(range(5)):raise RuntimeError('mutation inert')
print(json.dumps({'checks':checks,'histories':3*2**12,'each_history_attempts':12,'n':[2,4,8],'current_displacement_only_mutant_failed':True,'scope':'tagged deterministic histories; not actual production-chain bias estimate','source_sha':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
