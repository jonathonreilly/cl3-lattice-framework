"""Authenticate saved scalar interval certificates; never evaluate a Green oracle."""
import argparse,json,hashlib,signal
from fractions import Fraction as F
from pathlib import Path

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args();signal.alarm(30);root=Path(__file__).resolve().parents[1];folder=root/'outputs/native_certified_local_green_scalars_2026_09_09_inputs';pins=json.loads((folder/'MANIFEST.json').read_text());checks=0
 def req(x,label):
  nonlocal checks
  if not x:raise ValueError(label)
  checks+=1
 def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
 for rel,h in pins.items():req(digest(root/rel)==h,'source '+rel)
 results={}
 for kind in ('return','elliptic','B'):
  path=folder/(kind+'_RESULT.json');d=json.loads(path.read_text());a=json.loads((folder/(kind+'_ROOT_ACCEPTANCE.json')).read_text());w=json.loads((folder/(kind+'_WORKER_COMPLETE.json')).read_text());h=digest(path)
  req(a['result_sha256']==w['result_sha256']==h,'receipt binding');req(w['status']=='COMPLETE' and a['status'].startswith('ACCEPTED_'),'accepted execution');results[kind]=d
  keys=('B','Bprime') if kind=='B' else ('A','Aprime')
  expected=['1','2'] if kind=='B' else ['0','1/1000000000','1/2','1','2'] if kind=='elliptic' else ['1','1','2','2','1/2','1/2']
  req([r['s'] for r in d['rows']]==expected,'fixed rows')
  for row in d['rows']:
   req(row['status']=='CERTIFIED_TARGET','target status')
   target=F(row['target'])
   for key,width in zip(keys,row['widths']):
    lo,hi=map(F,row[key]);req(lo<=hi and hi-lo==F(width)<=target,'exact width');req(lo>0 if key in ('A','B') else hi<0,'known sign')
 for s in ('1/2','1','2'):
  a=next(r for r in results['elliptic']['rows'] if r['s']==s);b=next(r for r in results['return']['rows'] if r['s']==s and r['target']=='1/1000000000000')
  for key in ('A','Aprime'):
   x,y=map(F,a[key]);u,v=map(F,b[key]);req(max(x,u)<=min(y,v),'independent overlap')
 print(json.dumps({'status':'PASS_SAVED_CERTIFICATE_CHECKS','checks':checks,'physical_calls':0,'oracle_calls':0,'actual_current_surface_status':'conditional-support','input_hashes':pins,'scope':'receipt and exact interval consistency; containment also depends on reviewed source methods'},indent=2))
if __name__=='__main__':main()
