from pathlib import Path
import runpy,json,hashlib
p=Path(__file__).with_name('review.py');m=runpy.run_path(str(p))
rows=[[float(i+j+1) for j in range(12)] for i in range(16)]
s=m['summarize'](rows)
if s['mean'][0]!=8.5 or abs(s['covariance'][0][1]-17/12)>1e-14:raise RuntimeError('known covariance')
if len(s['joint'])!=17 or m['derived']([0.]*12) is not None:raise RuntimeError('shape/domain')
x=m['seed']
if len(x)!=24 or m['nf'](x)!=12:raise RuntimeError('literal seed')
Path(__file__).with_name('HARNESS_FREEZE.json').write_text(json.dumps({'review_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'selftests':4,'data_read':False,'status':'prepared; not executed on production'},indent=2)+'\n')
