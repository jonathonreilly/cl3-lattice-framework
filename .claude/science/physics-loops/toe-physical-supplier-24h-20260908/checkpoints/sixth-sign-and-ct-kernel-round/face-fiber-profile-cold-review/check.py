from pathlib import Path
import json,hashlib,sys,cmath,math
B=Path('/private/tmp/toe-24h-probes-20260908/face-fiber-profile');O=Path(__file__).parent
sys.path.insert(0,str(B))
import factory,checkpoint,measure,forecast
checks=[]
def req(c,s):
 if not c:raise RuntimeError(s)
 checks.append(s)
freeze=json.loads((B/'FINAL_FREEZE.json').read_text())
req(hashlib.sha256((B/'FINAL_FREEZE.json').read_bytes()).hexdigest()=='f7b24558fbe7ef70850448fe7943c13570dbba03530bba269b14be6d5cfa5250','freeze')
for n,h in freeze['files'].items():req(hashlib.sha256((B/n).read_bytes()).hexdigest()==h,'file '+n)
for n,h in json.loads((B/'RUNTIME.json').read_text())['files'].items():req(hashlib.sha256(Path(n).read_bytes()).hexdigest()==h,'runtime '+n)
for folder in sorted((B/'CONTROL_FILES').iterdir()):
 if not folder.name.isdigit():continue
 m=json.loads((folder/'meta.json').read_text());g=factory.Geometry(m['L']);a=checkpoint.load(g,folder,(m['L'],m['n'],m['V']))
 req(all(g.nf(x)==k for x,k in zip(a.states,a.nf)),'literal counts '+folder.name)
 req(all(g.flux(x)==g.flux(g.seed) for x in a.states),'flux '+folder.name)
 r=measure.measure(a);x=a.states[m['n']//2];S=[]
 for h in ([1] if g.L==2 else [1,2]):
  value=0
  for axis in range(3):
   for linkdir in range(3):
    if axis==linkdir:continue
    re=im=0
    for e,(v,d) in enumerate(g.links):
     if d!=linkdir:continue
     amp=(1 if sum(v)%2==0 else -1)*(2*((x>>e)&1)-1)/(2*math.sqrt(g.L**3));angle=2*math.pi*h*v[axis]/g.L
     re+=amp*math.cos(angle);im+=amp*math.sin(angle)
    value+=re*re+im*im
  S.append(value)
 req(max(abs(x-y) for x,y in zip(S,r['S']))<1e-12,'literal S '+folder.name)
 u=[.31]*len(a.states); before=set(a.g.flux(z) for z in a.states);factory.draw(a,0,u)
 req(set(a.g.flux(z) for z in a.states)==before,'fixed draw flux '+folder.name)
 # witness reconstruction validates changed free endpoint, not an old fixed endpoint.
 b=factory.reconstruct(g,a.states,a.nf,a.V,list(a.witness),sum(a.nf));req(b.states==a.states,'witness '+folder.name)
p={'accounted_case_seconds':8,'cases':[{'base_16chain_16sweep_seconds_before_unallocated':100}]}
req(forecast.price(p,10)['cases'][0]['hypothetical_16chain_16sweep_seconds']==132,'all overhead per chain')
(O/'RESULT.json').write_text(json.dumps({'checks':len(checks),'predicates':checks,'no_sampling':True},indent=2)+'\n')
(O/'READ_HASHES.json').write_text(json.dumps({str(B/n):hashlib.sha256((B/n).read_bytes()).hexdigest() for n in freeze['files'] if n.endswith(('.py','.md','.sh','.json')) and '/' not in n},indent=2)+'\n')
print(len(checks))
