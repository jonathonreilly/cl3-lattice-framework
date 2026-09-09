from pathlib import Path
from itertools import combinations
import json,hashlib
P=Path(__file__).parent;source=P.parent/'native-l6-adapted-fock-transports/BLOCKS.json';rows=json.loads(source.read_text());pairs=list(combinations(range(6),2));reps={'P':(0,2),'O':(0,1)}
def image(pair,row):
 T=row['T'];ans=[]
 for v in pair:
  axis,neg=divmod(v,2);i=next(i for i in range(3) if T[i][axis]);sign=T[i][axis]*(-1 if neg else 1);ans.append(2*i+int(sign<0))
 return tuple(sorted(ans))
entries=[]
for pair in pairs:
 cls='O' if pair[0]//2==pair[1]//2 else 'P';indices=[i for i,row in enumerate(rows) if image(reps[cls],row)==pair]
 if not indices:raise ValueError('orbit')
 entries.append({'pair':pair,'class':cls,'transport':indices[0]})
pred={c:[e for e in entries if set(e['pair']).isdisjoint(pair)] for c,pair in reps.items()}
if [(sum(e['class']=='P' for e in pred[c]),sum(e['class']=='O' for e in pred[c])) for c in ('P','O')]!=[(5,1),(4,2)]:raise ValueError('six predecessor classes')
(P/'LEDGER.json').write_text(json.dumps({'source_sha':hashlib.sha256(source.read_bytes()).hexdigest(),'representatives':reps,'entries':entries,'predecessors':pred,'selection':'smallest exact symmetry index before candidate data'},indent=2)+'\n')
