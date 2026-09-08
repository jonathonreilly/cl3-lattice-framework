from pathlib import Path
from itertools import product
import json,math,cmath,hashlib,time
p=Path('/private/tmp/toe-24h-probes-20260908/native-3d-chessboard-spectral-design');r=json.loads((p/'COST_RESULT.json').read_text());d=json.loads((p/'INPUTS.json').read_text());checks=0;residuals=[]
def need(x,s):
 global checks
 checks+=1
 if not x:raise ValueError(s)
def mul(A,B):
 rows={}
 for (i,j),v in B.items():rows.setdefault(i,[]).append((j,v))
 C={}
 for (i,j),v in A.items():
  for k,w in rows.get(j,[]):C[i,k]=C.get((i,k),0)+v*w
 return C
expected=[(q,x) for q in (0,1,3,5,10,15) for x in product(range(4),range(2),range(2))]
need(len(r['rows'])==96,'96 rows');need(r['input_sha256']==hashlib.sha256((p/'INPUTS.json').read_bytes()).hexdigest(),'input binding')
for row,(q,x) in zip(r['rows'],expected):
 need((row['rep'],tuple(row['index']))==(q,x),'fixed row membership/order');k=[2*math.pi*(n+.5)/m for n,m in zip(x,(4,2,2))];need(max(abs(a-b) for a,b in zip(k,row['k']))<1e-15,'fixed grid')
 ev=row['eigenvalues'];need(len(ev)==64 and all(math.isfinite(v) for v in ev),'finite spectra');need(ev==sorted(ev),'ordered spectra');need(max(abs(ev[i]+ev[-1-i]) for i in range(32))<1e-11,'bipartite pairing');need(math.isfinite(row['eigvalsh_seconds']) and row['eigvalsh_seconds']>0,'positive cost')
 H={(i,j):s*cmath.exp(1j*sum(a*b for a,b in zip(k,e))) for i,j,e,s in d['rows'][q]['terms']};H2=mul(H,H);H3=mul(H2,H)
 exact=[sum(abs(v)**2 for v in A.values()) for A in (H,H2,H3)]
 errs=[]
 for m,target in zip((2,4,6),exact):
  error=abs(sum(z**m for z in ev)-target);need(error<1e-9*max(1,target),'independent trace moment');errs.append(error)
 residuals.append(errs)
need(0<r['seconds']<30 and 0<r['rss_mib']<384,'internal caps')
root=p.parent/'native-3d-spectral-root-review';o=json.loads((root/'OUTER.json').read_text());need(o['returncode']==0 and o['watchdog_failure'] is None and o['provisional_resource_accept'],'wrapper outcome');need(o['observed_peak_whole_tree_bytes']<384*1048576,'tree RSS')
lines=(root/'SHELL.stderr').read_text().splitlines();wall=[float(x.split()[1]) for x in lines if x.startswith('real ')];rss=[int(x.split()[0]) for x in lines if 'maximum resident set size' in x];need(len(wall)==len(rss)==1 and 0<wall[0]<=30 and 0<rss[0]<=384*1048576,'external full resources')
rough={q:-sum(sum(abs(v) for v in z['eigenvalues']) for z in r['rows'] if z['rep']==q)/(128*16) for q in (0,1,3,5,10,15)}
out=dict(checks=checks,moment_max_errors=[max(x[j] for x in residuals) for j in range(3)],rough_grid_auxiliary_densities=rough,rough_differences={q:v-rough[15] for q,v in rough.items()},external_seconds=wall[0],external_rss_bytes=rss[0],tree_rss_bytes=o['observed_peak_whole_tree_bytes'],source_sha=hashlib.sha256((p/'COST_RESULT.json').read_bytes()).hexdigest(),scope='stored output arithmetic/resource replay; no new eigenvalues and no certified density')
print(json.dumps(out,indent=2))
