import time
START=time.monotonic()
import pathlib,json,sys,hashlib,subprocess,argparse
B=pathlib.Path(__file__).resolve().parent
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args();out=pathlib.Path(a.out)
 if out.exists():raise ValueError('fresh output')
 freeze=json.loads((B/'FINAL_FREEZE.json').read_text())
 for name,h in freeze['files'].items():
  if hashlib.sha256((B/name).read_bytes()).hexdigest()!=h:raise ValueError('freeze '+name)
 for name,h in json.loads((B/'RUNTIME.json').read_text())['files'].items():
  if hashlib.sha256(pathlib.Path(name).read_bytes()).hexdigest()!=h:raise ValueError('runtime '+name)
 try:
  remaining=30-(time.monotonic()-START)
  if remaining<=0:raise TimeoutError('freeze cost')
  r=subprocess.run([sys.executable,'-OO',str(B/'profile.py'),'--out',str(out)],capture_output=True,text=True,timeout=remaining);code=r.returncode;stdout=r.stdout;stderr=r.stderr
 except (subprocess.TimeoutExpired,TimeoutError) as e:
  code=124;stdout=getattr(e,'stdout',None) or '';stderr=getattr(e,'stderr',None) or str(e)
  if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
  if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
 out.mkdir(exist_ok=True)
 if code==0:
  try:
   from forecast import compute
   (out/'FORECAST.json').write_text(json.dumps(compute(out),indent=2))
   if time.monotonic()-START>30:raise RuntimeError('post-dispatch accounting exceeded30s')
  except Exception as e:
   code=1;stderr+='\nForecast/integrity failure: '+repr(e)
 (out/'stdout').write_text(stdout);(out/'stderr').write_text(stderr)
 receipt=dict(exit=code,external_seconds=time.monotonic()-START,freeze=hashlib.sha256((B/'FINAL_FREEZE.json').read_bytes()).hexdigest(),scope='single cost fixture; no retries')
 (out/'DISPATCH.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt));sys.exit(code)
