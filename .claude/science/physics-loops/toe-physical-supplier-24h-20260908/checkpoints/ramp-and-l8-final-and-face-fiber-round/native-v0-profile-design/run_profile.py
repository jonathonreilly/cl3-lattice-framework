"""One profile dispatch only; execution requires the separate root authorization."""
import time
START=time.monotonic()
import pathlib,subprocess,sys,json,hashlib,argparse
P=pathlib.Path(__file__).parent
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args();out=pathlib.Path(args.out)
 if out.exists():raise ValueError('fresh output only')
 freeze=json.loads((P/'FINAL_FREEZE.json').read_text())
 for n,h in freeze.items():
  if hashlib.sha256((P/n).read_bytes()).hexdigest()!=h:raise ValueError('freeze '+n)
 remaining=30-(time.monotonic()-START)
 if remaining<=0:raise RuntimeError('profile budget before dispatch')
 try:r=subprocess.run([sys.executable,'-OO',str(P/'profile.py'),'--out',str(out)],capture_output=True,text=True,timeout=remaining);code=r.returncode;stdout=r.stdout;stderr=r.stderr
 except subprocess.TimeoutExpired as e:code=124;stdout=(e.stdout or b'').decode() if isinstance(e.stdout,bytes) else e.stdout or '';stderr=(e.stderr or b'').decode() if isinstance(e.stderr,bytes) else e.stderr or ''
 elapsed=time.monotonic()-START;out.mkdir(exist_ok=True);(out/'stdout').write_text(stdout);(out/'stderr').write_text(stderr);receipt=dict(exit=code,external_seconds=elapsed,freeze=hashlib.sha256((P/'FINAL_FREEZE.json').read_bytes()).hexdigest(),scope='one capped cost profile, no replacements')
 (out/'DISPATCH.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt));sys.exit(code)
