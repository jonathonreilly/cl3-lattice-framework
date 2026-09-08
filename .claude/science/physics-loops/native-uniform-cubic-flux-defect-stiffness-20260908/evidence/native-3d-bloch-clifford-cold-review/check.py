"""Independent coordinate-action check, no author functions or eigensolver."""
import json,itertools,signal,time
from pathlib import Path
signal.alarm(180);start=time.monotonic();n=0
D=json.loads(Path('/private/tmp/toe-24h-probes-20260908/native-3d-chessboard-spectral-design/INPUTS.json').read_text());V=[tuple(r) for r in D['site_order']];ix={r:i for i,r in enumerate(V)}
def ck(c,s):
 global n;n+=1
 if not c:raise RuntimeError(s)
def square(H):
 out={};rows={}
 for (a,b),v in H.items():rows.setdefault(a,[]).append((b,v))
 for (a,b),v in H.items():
  for c,w in rows.get(b,[]):out[a,c]=out.get((a,c),0)+v*w
 return {k:v for k,v in out.items() if v}
def inc(H,i,j,x):H[i,j]=H.get((i,j),0)+x
phases=[39+52j,25+60j,-39+52j] # denominator65: distinct exact rational unit phases
for row in D['rows']:
 signs={(tuple(v),a):s for (v,a),s in zip(D['cube_edge_order'],row['cube_signs'])}
 def edge(y,a):v=list(y);v[a]=0;return signs[tuple(v),a]
 H={}
 for i,j,e,s in row['terms']:
  a=next((a for a,x in enumerate(e) if x),None)
  phase=65 if a is None else phases[a] if e[a]>0 else phases[a].conjugate()
  inc(H,i,j,s*phase)
 target={}
 for i,r in enumerate(V):
  b=tuple(x//2 for x in r);y=tuple((x%2)^(x//2) for x in r)
  inc(target,i,i,3*65**2)
  for a,c in itertools.product(range(3),repeat=2):
   ya=list(y);ya[a]^=1;yc=ya.copy();yc[c]^=1
   out=tuple(2*b[t]+(yc[t]^b[t]) for t in range(3))
   inc(target,i,ix[out],65**2*edge(y,a)*edge(ya,c))
  for a in range(3):
   yy=list(y);bb=list(b);yy[a]^=1;bb[a]^=1
   out=tuple(2*bb[t]+(yy[t]^bb[t]) for t in range(3))
   ay=edge(y,a)*(-1j if y[a]==0 else 1j)
   gamma=(-1)**sum(b[:a])*((phases[a].real-65)*(-1j if b[a]==0 else 1j)-phases[a].imag)
   inc(target,i,ix[out],65*ay*gamma)
 target={k:v for k,v in target.items() if v};ck(square(H)==target,'mixed rational phase coordinate square')
 # Actual wrong sine sign must fail this same raw matrix.
 bad=target.copy()
 for i,r in enumerate(V):
  b=tuple(x//2 for x in r);y=tuple((x%2)^(x//2) for x in r)
  for a in range(3):
   yy=list(y);bb=list(b);yy[a]^=1;bb[a]^=1;out=tuple(2*bb[t]+(yy[t]^bb[t]) for t in range(3))
   inc(bad,i,ix[out],130*edge(y,a)*(-1j if y[a]==0 else 1j)*(-1)**sum(b[:a])*phases[a].imag)
 ck(square(H)!={k:v for k,v in bad.items() if v},'wrong sine sign adverse')
print(json.dumps({'status':'PASS','predicates':n,'backgrounds':32,'phase_numerators':[[int(z.real),int(z.imag)] for z in phases],'denominator':65,'seconds':time.monotonic()-start,'scope':'independent literal-coordinate exact Gaussian integers; no eigenvalues'}))
