import pathlib,json,itertools,hashlib
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-global-charge-exchange');O=pathlib.Path(__file__).parent
r=json.loads((P/'RESULT.json').read_text());vs=list(itertools.product(range(4),repeat=3));ids={v:i for i,v in enumerate(vs)};es=set()
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;es.add(tuple(sorted((ids[v],ids[tuple(w)]))))
es=sorted(es);ix={e:i for i,e in enumerate(es)};inc=[[e for e,(i,j) in enumerate(es) if v in (i,j)] for v in range(64)];eps=[(-1)**sum(v) for v in vs]
if r['vertices']!=[list(v) for v in vs] or r['edges']!=[list(e) for e in es]:raise RuntimeError('geometry')
def state(z):
 deg=[sum(z>>e&1 for e in inc[v]) for v in range(64)]
 return [eps[v]*(deg[v]-3) for v in range(64)],sum((d%2)<<v for v,d in enumerate(deg))
# Quadratic W phase from the source dictionary, independently of author's native tape.
M=[]
for e,(i,j) in enumerate(es):
 mask=0
 for v,other in ((i,j),(j,i)):
  for f in inc[v]:
   nb=es[f][0] if es[f][1]==v else es[f][1]
   if nb<other:mask^=1<<f
 for v in range(i,j):
  for f in inc[v]:mask^=1<<f
 M.append(mask)
if any(((M[e]>>f)&1)!=((M[f]>>e)&1) for e in range(192) for f in range(192)):raise RuntimeError('W quadratic')
def phase(z):return (-z.bit_count()+2*sum((z>>e&1)*((M[e]&z)>> (e+1)).bit_count() for e in range(192)))%4
def fermion(b,v,create):
 if bool(b>>v&1)==create:raise RuntimeError('CAR support')
 return b^(1<<v),(b&((1<<v)-1)).bit_count()%2
seqA=[(0,16),(4,0),(0,1)];seqB=[(0,1),(4,0),(0,16)]
checks=0;summary=[]
for w in r['witnesses']:
 s=w['sign'];start=int(w['initial_bits'],2);ends=[];phases=[]
 for name,seq,z in [('routeA',seqA,start),('routeB',seqB,start),('reverseB',[(b,a) for a,b in reversed(seqB)],int(w['routeA'][-1]['bits'],2))]:
  ph=0
  for step in range(4):
   q,bits=state(z);row=w[name][step]
   if row['bits']!=format(z,'0192b') or row['charges']!=q or row['phase_mod4']!=ph or q.count(1)!=2 or q.count(-1)!=2 or max(map(abs,q))!=1:raise RuntimeError('literal tape')
   checks+=1
   if step==3:break
   target,source=seq[step]
   if q[target]!=0 or q[source]!=s:raise RuntimeError('signed support')
   # Electron target -> source fills old hole and creates new hole.
   bb,a=fermion(bits,target,False);bb,c=fermion(bb,source,True);zz=z^(1<<ix[tuple(sorted((target,source)))])
   if state(zz)[1]!=bb:raise RuntimeError('Gauss CAR')
   ph=(ph+phase(z)-phase(zz)+2*(a+c))%4;z=zz
  ends.append(z);phases.append(ph)
 if ends[0]!=ends[1] or ends[2]!=start or (phases[0]+phases[2])%4!=2:raise RuntimeError('closure')
 summary.append({'sign':s,'phases':phases,'closed_phase':2})
if summary[0]['closed_phase']!=2:raise RuntimeError('negative loop mutant')
out={'PASS':True,'literal_full_states_checked':checks,'summary':summary,'scope':'Delivered bits only; independent CAR+W phases; no maxflow execution or author import.','hashes':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('DERIVATION.md','check.py','RESULT.json')}}
(O/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
