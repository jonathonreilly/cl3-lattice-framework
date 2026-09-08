import ast,pathlib,numpy as np,json,itertools
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/ice-spectral-moments/pilot/pilot.py');tree=ast.parse(p.read_text());names=['coefficients','measurements','numerator_methods'];nodes=[]
for n in tree.body:
 if isinstance(n,ast.FunctionDef) and n.name in names:n.decorator_list=[];nodes.append(n)
def flip(s,f):a,b,c,d=s[f];return a==c and b==d and a!=b
ns={'np':np,'is_flippable':flip};exec(compile(ast.Module(body=nodes,type_ignores=[]),str(p),'exec'),ns)
ck={};rng=np.random.default_rng(66119)
for L in [2,4]:
 roots=list(itertools.product(range(L),repeat=3));links=[(r,a)for r in roots for a in range(3)];idx={l:i for i,l in enumerate(links)};faces=[]
 for a,b in itertools.combinations(range(3),2):
  for r in roots:
   ra=list(r);ra[a]=(ra[a]+1)%L;rb=list(r);rb[b]=(rb[b]+1)%L;faces.append([idx[r,a],idx[tuple(ra),b],idx[tuple(rb),a],idx[r,b]])
 faces=np.array(faces);state=np.array([r[a]%2 for r,a in links],dtype=np.uint8);co,pl,sc,modes=ns['coefficients'](L);snap=[];res=0
 for sample in range(8):
  for _ in range(3*L**3):
   f=faces[rng.integers(len(faces))]
   if flip(state,f):state[f]^=1
  snap.append(state.copy());v,sq,c=ns['measurements'](state,faces,co,pl,sc)
  O=co@(state.astype(float)-.5);lo=np.zeros(len(modes),complex);d=np.zeros(len(modes))
  for f in faces:
   if flip(state,f):
    y=state.copy();y[f]^=1;delta=co@(y.astype(float)-.5)-O;lo-=delta;d+=abs(delta)**2/2
  res=max(res,np.max(abs(v[:,0]+1j*v[:,1]-O)),np.max(abs(sq-abs(lo)**2)),np.max(abs(v[:,3]-d)))
 assert res<1e-10;ck[str(L)]={'samples':8,'max_residual':float(res)}
 snaps=np.array(snap);choices=rng.integers(len(faces),size=8);a=ns['numerator_methods'](snaps,faces,co,pl,sc,choices,0);b=ns['numerator_methods'](snaps,faces,co,pl,sc,choices,2);assert np.max(abs(a-b))<1e-12
print(json.dumps({'actual_AST_functions':names,'controls':ck,'scope':'function implementation checks; no production or mixing test'},indent=2))
