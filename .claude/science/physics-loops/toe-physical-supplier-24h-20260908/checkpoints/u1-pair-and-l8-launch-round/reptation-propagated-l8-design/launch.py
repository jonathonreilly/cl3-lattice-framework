import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import pathlib,json,time,subprocess,sys,argparse
from producer import verify_freeze,config,req,P

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);v=ap.parse_args();out=pathlib.Path(v.out);req(not out.exists(),'fresh study output required');out.mkdir();freeze=verify_freeze();t=time.monotonic();rows=[];prior=json.loads((P/'RESOURCE_LEDGER.json').read_text())['preproduction_seconds']
 for arm in range(3):
  for cid in range(16):
   c=config(arm,cid);total=c['burn']+c['updates']
   for seg in range((total+c['cap']-1)//c['cap']):
    req(14400-prior-(time.monotonic()-t)>=180,'full job reserve');name=f'arm{arm}_chain{cid}_segment{seg}';start=time.monotonic()
    with (out/(name+'.stdout')).open('x') as o,(out/(name+'.stderr')).open('x') as e:
     try:r=subprocess.run([sys.executable,str(P/'producer.py'),'--arm',str(arm),'--chain',str(cid),'--segment',str(seg),'--out',str(out)],stdout=o,stderr=e,timeout=180)
     except subprocess.TimeoutExpired:
      rows.append(dict(name=name,timeout=True));(out/'STATUS.json').write_text(json.dumps(rows,indent=2));raise
    rows.append(dict(name=name,exit=r.returncode,seconds=time.monotonic()-start));(out/'STATUS.json').write_text(json.dumps(rows,indent=2));req(r.returncode==0,'fixed job failed; no replacement')
if __name__=='__main__':main()
