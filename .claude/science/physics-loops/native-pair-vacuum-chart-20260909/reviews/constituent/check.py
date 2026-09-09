from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,hashlib
P=Path('/private/tmp/toe-24h-probes-20260908/native-pair-vacuum-transversality-stretch');O=Path(__file__).resolve().parent
checks=0
def need(x,m):
 global checks
 checks+=1
 if not x:raise ValueError(m)
p=F(0)
for n in range(33):
 term=comb(2*n,n)**2;c=term
 for j in range(n):
  l=n-j;term,rem=divmod(term*l**4,(j+1)**2*2*l*(2*l-1));need(rem==0,'axis allocation');c+=term
 p+=F(c,36**n)*F(comb(4*n,2*n),16**n)
d=json.loads((P/'RESULT.json').read_text());need(p==F(d['partial']),'partial')
upper=p*F(1000,2449)+F(1,192);need(upper==F(d['C0_h_upper'])<F(7,15),'upper')
need(F(2449,1000)**2<6,'sqrt6');need(F(99,70)**2>2,'sqrt2')
g=F(33,25);c=F(1,150)/(1+g)
need(c==F(1,348),'angle');need((1-c)/(1+c)==F(347,349),'chart');need(F(87,4)/(1+c)==F(7569,349),'overlap')
reads={}
for name,v in json.loads((P/'FREEZE.json').read_text()).items():
 q=P/name;h=hashlib.sha256(q.read_bytes()).hexdigest();need(h==v,name);reads[str(q)]=h
for name,v in json.loads((P/'IMPORT_HASHES.json').read_text()).items():
 h=hashlib.sha256(Path(name).read_bytes()).hexdigest();need(h==v,name);reads[name]=h
(O/'READ_HASHES.json').write_text(json.dumps(reads,indent=2)+'\n');(O/'RESULT.json').write_text(json.dumps({'status':'PASS','predicates':checks,'C0_h_upper':str(upper),'terms_including_n0':33,'physical_matrix_integral_calls':0},indent=2)+'\n');print(checks)
