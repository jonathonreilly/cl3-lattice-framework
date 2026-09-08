from fractions import Fraction as F
from pathlib import Path
import hashlib,json,itertools
P=Path(__file__).parent;S=P.parent/'native-l4-third-vertex';freeze=S/'FREEZE.json'
if hashlib.sha256(freeze.read_bytes()).hexdigest()!='1085e0ac7288428d50d3a2b9505b6b8615784149b46ca414067e7bd36acde536':raise ValueError('freeze')
f=json.loads(freeze.read_text());count=0
for group,base in [('files',S),('runtime',None),('dependencies',None)]:
 for path,h in f[group].items():
  q=base/path if base else Path(path)
  if hashlib.sha256(q.read_bytes()).hexdigest()!=h:raise ValueError(path)
  count+=1
# Independent rational toy: square metric values permit literal diagonal similarity.
d=[F(4),F(9),F(25)];sqrt=[F(2),F(3),F(5)];N=8
s=[__import__('functools').reduce(lambda a,i:a*sqrt[i],(i for i in range(3) if b>>i&1),F(1)) for b in range(N)]
checks=0;wrong=0
for b in range(N):
 for i in range(3):
  a=b^(1<<i);sign=(-1)**((b&((1<<i)-1)).bit_count());rv=F(i+1,7)
  direct=sign*rv/sqrt[i]*s[b]/s[a]
  formula=sign*rv*(1 if b>>i&1 else 1/d[i])
  if direct!=formula:raise ValueError('gamma similarity')
  checks+=1
  wrong+=direct!=sign*rv/d[i]
# Every ordered pair of disjoint pairs determines exactly one middle pair.
pairs=list(itertools.combinations(range(6),2));words=[]
for a in pairs:
 for c in pairs:
  if set(a).isdisjoint(c):words.append((a,tuple(sorted(set(range(6))-set(a)-set(c))),c))
if len(words)!=90 or len(set(words))!=90:raise ValueError('word grouping')
if F(1,8)*F(1,6)!=F(1,48):raise ValueError('resolvent factor')
if wrong==0:raise ValueError('nondiscriminating mutant')
out={'source_pins_verified':count,'gamma_similarity_cases':checks,'wrong_vacuum_annihilation_factor_mismatches':wrong,'ordered_words':len(words),'normalization':'1/48','physical_core_imported':False,'physical_solves':0}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
