import sys,json,tempfile,time,hashlib
from pathlib import Path
from fractions import Fraction as F
P=Path('/private/tmp/toe-24h-probes-20260908/native-quartic-spectral-estimator-design');sys.path.insert(0,str(P))
import worker,loader,history,interval as I
checks=0

def fixture(root,mutation=None):
 def write(name,value):
  p=root/name;p.write_text(json.dumps(I.encode(value)));return {'path':str(p),'sha256':loader.sha(p)}
 atoms=[(F(1,2),F(1,5)),(F(2),F(3,10)),(F(7),F(1,2))];p=[F(2,3),F(-1,7),F(1,49)];m=[sum(w*x**j for x,w in atoms)for j in range(11)];r2=sum(w*(1-x*sum(v*x**i for i,v in enumerate(p)))**2 for x,w in atoms);row={'p':p,'q':F(0),'r2':(r2,r2),'t2':(F(1),F(1))};gate={'rows':{'P':row,'O':row},'nominal':(F(0),F(0))};events=[];counts={};sourcecount={};kind='P'
 for seq,(stage,mode)in enumerate(history.schedule(),1):
  data={}
  if stage=='vacuum_inputs':kind='P'if counts.get(mode,0)==0 else'O'
  if stage=='vacuum_moment_raw':
   j=counts.get((mode,kind),0);data={'kind':kind,'index':j,'real':(m[j],m[j]),'imaginary':(F(0),F(0))};counts[mode,kind]=j+1;counts[mode]=counts.get(mode,0)+1
  if stage=='first_polynomial':data={'kind':kind,'coefficients':p}
  if stage=='source_moment_raw':
   j=sourcecount.get((mode,kind),0);sourcecount[mode,kind]=j+1;data={'kind':kind,'index':j,'real':(F(1),F(1))}
  if stage=='residual_raw':data=dict(row,kind=kind)
  if stage=='gate_inputs':data=gate
  events.append({'sequence':seq,'stage':stage,'choice':mode,'data':I.encode(data)})
 if mutation=='float_index':next(e['data']for e in events if e['stage']=='vacuum_moment_raw')['index']=0.0
 if mutation=='wrong_trial':next(e['data']for e in events if e['stage']=='first_polynomial')['coefficients']=['0','0','0']
 ep=root/'original.ndjson';ep.write_text(''.join(json.dumps(e)+'\n'for e in events));es={'path':str(ep),'sha256':loader.sha(ep)}
 def fam(name,result):
  status='accepted_'+name;ws='worker_'+name;rh=write(name+'_root',{'worker_freeze':'0'*64});rs=write(name+'_result',result);w=write(name+'_worker',{'status':ws,'seconds':1,'rss_bytes':1000,'runtime_sha256':'0'*64,'result_sha256':rs['sha256']});rr=write(name+'_receipt',{'pass':True,'failure':None,'returncode':0,'seconds':1.1,'sampled_whole_tree_peak':2000,'worker_freeze':'0'*64});a=write(name+'_accept',{'status':status,'once':True,'result_sha256':rs['sha256'],'worker_freeze':'0'*64,'root_freeze':rh['sha256'],'external_seconds':1.2,'external_rss_bytes':2000,'sampled_whole_tree_peak':2000})
  return {'files':{'acceptance':a,'root_freeze':rh,'worker':w,'receipt':rr,'result':rs},'worker_freeze':'0'*64,'expected':{'acceptance':status,'worker':ws,'result':result['status'],'worker_seconds':19,'root_seconds':19.5,'external_seconds':20}}
 old=fam('old',{'status':'old','events':255,'choices':2,'rows':[{'mode':v,'nominal':gate['nominal']}for v in('residual','variational')]});old['files']['events']=es
 post=fam('post',{'status':'post','source_events':255,'choices':2,'rows':[{'mode':v,'nominal':gate['nominal'],'alpha_interval':(-F(1000000),F(1000000)),'a_squared_upper':F(3),'b_squared_upper':F(2)}for v in('residual','variational')]})
 post['binding']=write('post_binding',{'files':old['files']});post['mode_inputs']={v:write(v+'_input',{'gate':gate,'q':{'P':F(0),'O':F(0)},'s0':{'P':(F(1),F(1)),'O':(F(1),F(1))}})for v in('residual','variational')}
 def grid(v):return [[v.numerator*loader.S//v.denominator,-((-v.numerator*loader.S)//v.denominator)],[0,0]]
 hrows=[{'kind':k,'orders':[7,8,9,10],'moments':{str(j):grid(m[j])for j in range(7,11)}}for k in('P','O')]
 if mutation=='bool_endpoint':hrows[0]['moments']['7'][0][0]=True
 high=fam('high',{'status':'high','first_order':7,'native_lower_moments_recomputed':0,'native_oracle_calls':0,'rows':hrows});high['binding']=write('high_binding',{'degree20':old});high['tables']=write('tables',{'units':'dimensionless_h1','grid_bits':256,'classes':{k:{'accepted_m':{str(j):grid(m[j])for j in range(7)}}for k in('P','O')}})
 return {'degree20':old,'posterior20':post,'high':high}
started=time.monotonic()
for mutation in(None,'float_index','wrong_trial','bool_endpoint'):
 with tempfile.TemporaryDirectory()as d:
  root=Path(d);b=fixture(root,mutation);out=root/'out';out.mkdir()
  try:worker.run(b,out)
  except ValueError:
   assert mutation is not None and(out/'FAILURE.json').exists();checks+=1
  else:
   assert mutation is None;result=json.loads((out/'RESULT.json').read_text());assert result['events']==97 and len(result['rows'])==2;checks+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','controls':checks,'full_original_events':255,'new_events':97,'seconds':time.monotonic()-started,'native_values':0},indent=2))
