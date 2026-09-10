"""Prepare final input binding only after BOTH root acceptances exist. No contraction."""
import json,hashlib,argparse
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('catalog_directory');ap.add_argument('catalog_acceptance');ap.add_argument('output');args=ap.parse_args()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1<<20),b''):h.update(x)
 return h.hexdigest()
def make(directory,acceptance):
 p=Path(directory).resolve();a=Path(acceptance).resolve();v=json.loads(a.read_text())
 if not v['status'].startswith('ACCEPTED_') or sha(p/'RESULT.json')!=v['result_sha256']:raise ValueError('acceptance absent/inconsistent')
 return {'directory':str(p),'acceptance_path':str(a),'acceptance_sha256':sha(a),'result_sha256':sha(p/'RESULT.json'),'worker_complete_sha256':sha(p/'WORKER_COMPLETE.json'),'source_freeze_sha256':v['worker_freeze']}
p=Path('/private/tmp/toe-24h-probes-20260908');po=p/'native-stationary-pole-scalar-batch-design/POLES.json';geo=p/'native-highprecision-b-catalog-design/CATALOG_GEOMETRY.json'
b={'a66':make(p/'native-stationary-pole-scalar-run-9845c',p/'native-stationary-pole-scalar-root-review/ROOT_ACCEPTANCE.json'),'catalog':make(args.catalog_directory,args.catalog_acceptance),'poles_path':str(po),'poles_sha256':sha(po),'catalog_geometry_path':str(geo),'catalog_geometry_sha256':sha(geo),'shards':[list(range(6*i,6*i+6)) for i in range(11)]}
out=Path(args.output)
if out.exists():raise ValueError('fresh binding output')
out.write_text(json.dumps(b,indent=2)+'\n');print(sha(out))
