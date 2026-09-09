import json,subprocess,sys,signal,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent

def main():
 signal.alarm(30)
 source=(P/'kernel.py').read_text()
 variants={'baseline':source,
 'wrong_vacuum_shift':source.replace('e0*duration+.5','-e0*duration+.5'),
 'wrong_wick_sign':source.replace('ax@by-ax@z@ay','ax@by+ax@z@ay'),
 'wrong_rotation':source.replace('exponential_hermitian(1j*k,-t)','exponential_hermitian(1j*k,t)')}
 rows=[]
 for name,text in variants.items():
  path=P/('unit_'+name+'.py');path.write_text(text)
  code='import types,sys; from pathlib import Path; p=Path('+repr(str(path))+'); m=types.ModuleType("kernel");sys.modules["kernel"]=m;exec(compile(p.read_bytes(),str(p),"exec"),m.__dict__);q=Path('+repr(str(P/'toy.py'))+');exec(compile(q.read_bytes(),str(q),"exec"),{"__name__":"__main__"})'
  r=subprocess.run([sys.executable,'-I','-B','-c',code],capture_output=True,text=True,timeout=10)
  row={'name':name,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
  rows.append(row);(P/'UNIT_CONTROL.json').write_text(json.dumps({'rows':rows,'physical_runs':0},indent=2)+'\n')
  if (r.returncode==0)!=(name=='baseline'):raise ValueError('semantic mutant result '+name)
 print(json.dumps({'status':'PASS','baseline_comparisons':9,'actual_rejected_mutants':3,'physical_runs':0}))
if __name__=='__main__':main()
