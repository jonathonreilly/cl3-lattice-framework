import itertools,json,pathlib,hashlib
p=pathlib.Path(__file__).resolve().parent;base=p.parent
count=0
def req(b):
 global count
 if not b:raise ValueError(count)
 count+=1
src=base/'native-sparse-pivot-action-stretch'
for name,h in json.loads((src/'SOURCE_HASHES.json').read_text()).items():req(hashlib.sha256((base/name).read_bytes()).hexdigest()==h)
for name,h in json.loads((src/'FREEZE.json').read_text()).items():req(hashlib.sha256((src/name).read_bytes()).hexdigest()==h)
# Synthetic index carrier: raw poles6 source pairs +3insertions, then3DATAq.
# Exact support sets; no physical vectors, entries or history.
raw=15
gamma=lambda i:i+raw if i<raw else i-raw
Q={12,15,16,17} # use tuple labels below to avoid artificial index overlap
J=lambda x:(x[0],1-x[1])
Q={(x,g) for x in ('x0','qA','qC','qD') for g in (0,1)}
seeds=[{('p'+str(n)+'-'+str(v),0),('m'+str(n)+'-'+str(v),0)} for n in range(2) for v in range(3)]+[{(x,0)} for x in ('x0','xA','xC')]
def image(x):
 name,g=x
 if name[0] in 'pm':return {x, (('x0','qA','qC')[int(name[-1])],g)}
 return {({'x0':'qD','xA':'qA','xC':'qC'}[name],g)}
for k in range(5):
 for chosen in itertools.combinations(seeds,k):
  S=set().union(*chosen) if chosen else set();R=S|{J(x) for x in S};U=R|Q
  req(len(R)<=4*k);req(len(U)<=4*k+8)
  for x in R:req(image(x)<=U)
  req({('x0',0),('qA',0),('qC',0)}<=U)
req(24*25//2==300)
result={'status':'PASS_SOURCE_PINS_AND_SYNTHETIC_SUPPORT','predicates':count,'native_calls':0}
(p/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
