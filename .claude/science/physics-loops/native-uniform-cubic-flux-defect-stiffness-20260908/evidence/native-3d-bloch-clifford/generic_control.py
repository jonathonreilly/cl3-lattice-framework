"""New exact rational-phase and Kramers controls; no eigenvalues."""
from pathlib import Path
import ast,json,time
p=Path(__file__).resolve().parent;tree=ast.parse((p/'check.py').read_text());ns={}
# Reuse only elementary sparse matrix function definitions, no author background loop.
keep=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('add','scale','mul','kron','I','tr')]
exec(compile(ast.Module(body=keep,type_ignores=[]),'<sparse-ops>','exec'),ns)
add,scale,mul,kron,I=[ns[n] for n in ('add','scale','mul','kron','I')]
from itertools import product
D=json.loads((p.parent/'native-3d-chessboard-spectral-design/INPUTS.json').read_text());C=list(product(range(2),repeat=3));idx={x:i for i,x in enumerate(C)};P=[]
for r in D['site_order']:P.append(idx[tuple((0,1,1,0)[x] for x in r)]*8+idx[tuple(x//2 for x in r)])
X={(0,1):1,(1,0):1};Y={(0,1):-1j,(1,0):1j};Z={(0,0):1,(1,1):-1};J=kron(I(8),{(0,1):1,(1,0):-1},2);checks=0
for row in D['rows']:
 signs={(tuple(v),a):s for (v,a),s in zip(D['cube_edge_order'],row['cube_signs'])};cube={};AA=[]
 for a in range(3):
  aa={}
  for y in C:
   z=list(y);z[a]^=1;v=list(y);v[a]=0;s=signs[tuple(v),a];cube[idx[y],idx[tuple(z)]]=s;aa[idx[y],idx[tuple(z)]]=s*(-1j if y[a]==0 else 1j)
  AA.append(aa)
 base=add(mul(cube,cube),scale(I(8),3));h={}
 for i,j,e,s in row['terms']:
  # Common phase(3+4i)/5 on every positive wrapped bond; Hscaled=5h.
  n=sum(e);h[P[i],P[j]]=s*(5 if n==0 else 3+4j*n)
 pred=scale(kron(base,I(8),8),25)
 for a in range(3):
  gamma={}
  for b in C:
   c=list(b);c[a]^=1;gamma[idx[b],idx[tuple(c)]]=(-1)**sum(b[:a])*(-2*(-1j if b[a]==0 else 1j)-4)
  pred=add(pred,scale(kron(AA[a],gamma,8),5))
 if mul(h,h)!=pred:raise ValueError('rational phase full square identity')
 checks+=1
 reduced=kron(base,I(2),2)
 for a,q in enumerate((1,2,3)):reduced=add(reduced,scale(kron(AA[a],(X,Y,Z)[a],2),q))
 transformed=scale(mul(mul(J,{k:complex(v).conjugate() for k,v in reduced.items()}),J),-1)
 if transformed!=reduced or mul(J,J)!=scale(I(16),-1):raise ValueError('Kramers identity')
 checks+=2
print(json.dumps(dict(checks=checks,rational_phase='(3+4i)/5',scope='exact scaled Gaussian integers; Kramers test algebraic q3 allowed, not claimed physical q range')))
