from pathlib import Path
from fractions import Fraction as F
import json,hashlib,subprocess
B=Path('/private/tmp/toe-24h-probes-20260908');S=B/'native-l6-allprefix-gap';D=B/'native-l6-allprefix-production-25eb6691';O=Path(__file__).parent;R=B/'native-l6-allprefix-root-review';repo='/Users/jonBridger/Documents/New Axioms Lets Go';commit='0116a1211e8553d319035e5ebd950dd7edca03b2'
def ck(x):
 if not x:raise ValueError('postreview predicate')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((S/'FREEZE.json').read_text());plan=json.loads((S/'PLAN.json').read_text());done=json.loads((D/'COMPLETE.json').read_text());ledger=json.loads((D/'LEDGER.json').read_text());ck(not (D/'FAILED.json').exists());ck(done['freeze']==sha(S/'FREEZE.json'))
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',commit],cwd=repo,text=True).splitlines()
for name,h in f['files'].items():
 ck(sha(S/name)==h);matches=[p for p in paths if p.endswith('/native-l6-allprefix-gap/'+name)];ck(len(matches)==1);raw=subprocess.check_output(['git','show',commit+':'+matches[0]],cwd=repo);ck(hashlib.sha256(raw).hexdigest()==h)
allrows=[]
for s in range(16):
 p=D/f's{s}.json';z=json.loads(p.read_text());rec=ledger[s];ck(rec['shard']==s and rec['sha']==sha(p) and 0<rec['seconds']<=180 and 0<rec['rss_bytes']<=384*1048576);ck(z['freeze']==done['freeze'] and z['shard']==s);ck([x['mask'] for x in z['rows']]==plan['shards'][s]['masks'])
 for row in z['rows']:
  ck(row['positive']==(F(row['gap_lower'])>0));ck(row['method']==('singleton initial-parity gap' if row['mask'] in plan['singletons'] else 'fixed c=5/2 Newton/Woodbury'))
 allrows+=z['rows']
ck(allrows==done['rows'] and len(allrows)==len({x['mask'] for x in allrows})==1534);minimum=min(F(x['gap_lower']) for x in allrows);ck(minimum>F('0.3449'));outer=json.loads((R/'OUTER.json').read_text());ck(outer['returncode']==0 and outer['complete'] and outer['watchdog_failure'] is None and outer['charged_seconds']<1200)
(O/'RESULT.json').write_text(json.dumps(dict(rows=1534,all_positive=True,minimum=str(minimum),commit=commit,archived_sources_match=True,scope='complete coverage/hash/sign/receipt replay; prior independent pilot arithmetic reused'),indent=2)+'\n');print(float(minimum))
