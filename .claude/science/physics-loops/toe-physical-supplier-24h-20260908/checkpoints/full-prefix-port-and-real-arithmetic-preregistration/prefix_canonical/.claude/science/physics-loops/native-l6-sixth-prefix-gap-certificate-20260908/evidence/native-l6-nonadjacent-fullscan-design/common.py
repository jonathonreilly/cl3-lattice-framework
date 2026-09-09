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
 ck(sys.flags.isolated and sys.dont_write_bytecode,'requires -I -B')
 f=read(P/'FREEZE.json')
 actual=sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p.suffix in ('.py','.pyc','.so','.dylib'))
 ck(actual==f['executable_membership'],'local executable membership')
 for p,h in f['files'].items():ck(sha(P/p)==h,'source '+p)
 old=read(P/'PILOT_FREEZE.json')
 ck(str(Path(sys.executable).resolve())==old['interpreter'],'interpreter')
 for p,h in {**old['dependencies'],**old['runtime']}.items():ck(sha(p)==h,'runtime/dependency')
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):ck(os.environ.get(k)=='1','threads')
 a=read(P/'PILOT_OUTER.json');b=read(P/'PILOT_POST.json');c=read(P/'PILOT_RESULT.json')
 ck(a['returncode']==0 and a['watchdog_failure'] is None and b['status']=='PASS','accepted cost')
 for x in (a['seconds'],b['seconds'],c['seconds'],a['observed_peak_whole_tree_bytes']):ck(math.isfinite(x) and x>0,'finite positive cost')
 validate_cost(a,b,c,read(P/'PILOT_ACCEPTANCE.json'),(P/'PILOT_SHELL.stderr').read_text(),read(P/'FORECAST.json'))
 ck(sha(P/'PILOT_RESULT.json')==read(P/'PILOT_ACCEPTANCE.json')['result_sha'],'accepted result')
 return sha(P/'FREEZE.json')
def rowscheck(rows,indices,plan):
 ck(len(rows)==len(indices),'row count')
 for r,i in zip(rows,indices):
  c=plan['cases'][i];ck(r['index']==i and r['case']==c,'case binding');v=Fraction(r['gap_lower']);ck(type(r['positive']) is bool and r['positive']==(v>0),'signed result')

def loaded_numpy():
 old=read(P/'PILOT_FREEZE.json');import numpy as np
 ck(str(Path(np.__file__).resolve())==old['numpy_origin'] and np.__version__==old['numpy_version'],'numpy origin/version')
 for module in tuple(sys.modules.values()):
  name=getattr(module,'__file__',None)
  if name and str(Path(name).resolve()).startswith(old['numpy_root']):
   name=str(Path(name).resolve());ck(name in old['runtime'] and sha(name)==old['runtime'][name],'loaded numpy closure')
def validate_cost(a,b,c,accept,shell,f):
 pin='97826f9d7eb4fea4c3357cc7ba12d46c741fa51fbbdc95a25571eb6e94bf92a7'
 ck(a['freeze']==c['freeze']==accept['freeze']==pin and accept['status']=='PASS','cost ancestry')
 for x,cap in [(a['seconds'],30),(c['seconds'],29),(b['seconds'],170),(a['observed_peak_whole_tree_bytes'],384*1048576),(c['rss_bytes'],384*1048576),(accept['external_seconds'],30),(accept['external_peak_bytes'],384*1048576),(accept['observed_tree_peak_bytes'],384*1048576)]:ck(math.isfinite(x) and 0<x<=cap,'cost cap')
 lines=shell.splitlines();wall=[float(x.split()[1]) for x in lines if x.startswith('real ')];rss=[int(x.split()[0]) for x in lines if 'maximum resident set size' in x]
 ck(wall==[accept['external_seconds']] and rss==[accept['external_peak_bytes']],'shell agreement')
 ck(a['observed_peak_whole_tree_bytes']==accept['observed_tree_peak_bytes'],'tree agreement')
 for key in ('production_seconds_per_shard','independent_replay_seconds_per_shard','finalization_reserve_seconds','aggregate_forecast_seconds'):
  ck(math.isfinite(f[key]) and f[key]>0,'forecast finite positive')
 ck(f['shards']==52 and f['unique_masks']==4986 and f['proper_keys']==5110 and f['maximum_masks_per_shard']==96,'forecast coverage')
 ck(accept['external_seconds']<=2.11 and b['seconds']<=.60,'priced costs')
 ck(abs(f['production_seconds_per_shard']-2*(2.11*96/25+2.11))<1e-10 and abs(f['independent_replay_seconds_per_shard']-2*(.60*96/25+.60))<1e-10,'fixed forecast formula')
 ck(f['finalization_reserve_seconds']==60 and abs(f['aggregate_forecast_seconds']-(52*(f['production_seconds_per_shard']+f['independent_replay_seconds_per_shard'])+60))<1e-9 and f['aggregate_forecast_seconds']<1440,'aggregate forecast')
