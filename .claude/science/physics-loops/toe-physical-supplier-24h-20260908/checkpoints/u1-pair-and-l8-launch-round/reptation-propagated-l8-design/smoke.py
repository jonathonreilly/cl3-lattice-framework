"""One reduced CLI smoke, not production. Executes all five tiny segments."""
import pathlib,subprocess,sys,time,json
p=pathlib.Path(__file__).parent;t=time.monotonic();out=p/'SMOKE_OUTPUT';rows=[]
for segment in range(5):
 r=subprocess.run([sys.executable,str(p/'producer.py'),'--arm','0','--chain','0','--segment',str(segment),'--out',str(out),'--smoke'],capture_output=True,text=True,timeout=max(.1,30-(time.monotonic()-t)))
 rows.append(dict(segment=segment,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr))
 if r.returncode:break
(p/'SMOKE_RESULT.json').write_text(json.dumps(dict(not_production=True,total_seconds=time.monotonic()-t,rows=rows),indent=2)+'\n')
if any(r['returncode'] for r in rows) or len(rows)!=5:raise RuntimeError('smoke failed')
print('smoke completed',time.monotonic()-t)
