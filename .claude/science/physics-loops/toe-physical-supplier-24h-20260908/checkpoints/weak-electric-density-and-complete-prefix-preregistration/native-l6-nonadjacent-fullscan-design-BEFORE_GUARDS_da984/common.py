from pathlib import Path
from fractions import Fraction
import json,hashlib,importlib.util,sys,os,math
P=Path(__file__).resolve().parent
def ck(x,m):
 if not x:raise ValueError(m)
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def verify():
 f=read(P/'FREEZE.json')
 for p,h in f['files'].items():ck(sha(P/p)==h,'source '+p)
 old=read(P/'PILOT_FREEZE.json')
 ck(str(Path(sys.executable).resolve())==old['interpreter'],'interpreter')
 for p,h in old['runtime'].items():ck(sha(p)==h,'runtime')
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):ck(os.environ.get(k)=='1','threads')
 a=read(P/'PILOT_OUTER.json');b=read(P/'PILOT_POST.json');c=read(P/'PILOT_RESULT.json')
 ck(a['returncode']==0 and a['watchdog_failure'] is None and b['status']=='PASS','accepted cost')
 for x in (a['seconds'],b['seconds'],c['seconds'],a['observed_peak_whole_tree_bytes']):ck(math.isfinite(x) and x>0,'finite positive cost')
 return sha(P/'FREEZE.json')
def rowscheck(rows,indices,plan):
 ck(len(rows)==len(indices),'row count')
 for r,i in zip(rows,indices):
  c=plan['cases'][i];ck(r['index']==i and r['case']==c,'case binding');v=Fraction(r['gap_lower']);ck(type(r['positive']) is bool and r['positive']==(v>0),'signed result')
