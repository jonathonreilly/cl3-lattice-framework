from pathlib import Path
from fractions import Fraction as F
import runpy,itertools,json,tempfile,hashlib,time
P=Path(__file__).parent;c=runpy.run_path(str(P/'core.py'));b=runpy.run_path(str(P/'binding.py'));count=0
for x in [F(0),F(1,3),F(-1,7),F(10**5000,3)]:
 if not c['down'](x)<=x<=c['up'](x) or c['up'](x)-c['down'](x)>F(1,c['D']):raise ValueError('directed rounding')
 count+=1
bins={t:1 for t in itertools.product(range(7),range(7),range(7),range(4)) if sum(t)%2};start=time.monotonic();z=c['summarize'](bins,0);json.dumps(z);count+=1
for k in [1,3]:
 z=c['summarize']({(0,0,k,0):c['square'](.5)},0);lo,hi=map(F,z['total']['stored_susceptibility_interval'])
 if not lo<=F(1,24*k)<=hi:raise ValueError('spectral enclosure')
 count+=1
# Binding fixtures are tiny synthetic metadata, not production acceptance.
with tempfile.TemporaryDirectory() as td:
 d=Path(td);prod={'algorithm':'direct_gaussian_once','passes_Echi':True,'physical_global_phase':'i','Echi':'0','vector_manifest':[{'file':'chi_real.npy','raw':{'phase':'i','sha256':'a'*64}}]}
 def write(name,obj):
  p=d/name;p.write_text(json.dumps(obj));return {'path':str(p),'sha256':b['sha'](p)}
 pr=write('prod',prod);co=write('complete',{'status':'PRODUCTION_ONLY_COMPLETE','result_sha256':pr['sha256'],'source_freeze':'s','contract_sha256':'c'});rep={'status':'PASS','scientific_pass':True,'input_result_sha256':pr['sha256'],'worker_complete_sha256':co['sha256'],'source_freeze':'r','Echi':'0'};rr=write('replay',rep);aa=write('acceptance',{'accepted':True,'production_result_sha256':pr['sha256'],'independent_replay_sha256':rr['sha256']});binding={'receipts':{'production':pr,'completion':co,'replay':rr,'acceptance':aa},'production_source_freeze':'s','production_contract_sha256':'c','replay_source_freeze':'r','raw_sha256':'a'*64};bp=d/'binding';bp.write_text(json.dumps(binding));b['validate'](bp);count+=1
 rep['scientific_pass']=False;binding['receipts']['replay']=write('replay',rep);bp.write_text(json.dumps(binding))
 try:b['validate'](bp)
 except ValueError:count+=1
 else:raise ValueError('false scientific pass')
(P/'CONTROL_RESULT.json').write_text(json.dumps({'status':'PASS','predicates':count,'synthetic_bins':686,'seconds':time.monotonic()-start,'full_scans':0},indent=2)+'\n');print(count)
