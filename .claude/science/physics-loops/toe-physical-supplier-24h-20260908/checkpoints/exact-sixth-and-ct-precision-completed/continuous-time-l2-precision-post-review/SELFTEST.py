from pathlib import Path
import runpy,json,hashlib,tempfile
B=Path(__file__).parent;m=runpy.run_path(str(B/'review.py'));n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
rows=[[float(i+j+1) for j in range(12)] for i in range(64)]
s=m['summarize'](rows);ck(s['mean'][0]==32.5);ck(abs(s['covariance'][0][1]-65/12)<1e-13);ck(len(s['joint'])==17);ck(m['derived']([0.]*12) is None)
ck(len(m['seed'])==24 and m['nf'](m['seed'])==12)
# Deterministic literal path replay, no RNG or author imports.
p=next(p for p in range(24) if m['legal'](m['seed'],p));packed=sum(x<<i for i,x in enumerate(m['seed']))
with tempfile.TemporaryDirectory(dir=B) as d:
 f=Path(d)/'p.json';z=dict(initial=hex(packed),events=[[(.25).hex(),p]],T=(.5).hex(),witness=[]);f.write_text(json.dumps(z));T,v=m['path_values'](f);ck(T==.5 and len(v)==12 and v[8]==1)
 z['events'][0][0]=(0.).hex();f.write_text(json.dumps(z))
 try:m['path_values'](f)
 except RuntimeError:ck(True)
 else:raise ValueError('time zero survived')
text=(B/'review.py').read_text();ck('for shard in range(16)' in text);ck('len(rows)==256' in text);ck('range(0,256,16)' in text);ck('mean(x[:128]),mean(x[128:])' in text);ck('[(0,1),(2,3)]' in text);ck('for i in [0,1,2,3]' in text)
result=dict(selftests=n,data_read=False,source_freeze=m['FREEZE'],predecessor_review_sha256='82a2ab2c5570fbac92cd128629ca8ac0fca455b883a008c91455f4469ba78539',files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [B/'review.py',B/'SELFTEST.py',B/'prepare.py']},status='frozen before study data; no production replay yet')
(B/'HARNESS_FREEZE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
