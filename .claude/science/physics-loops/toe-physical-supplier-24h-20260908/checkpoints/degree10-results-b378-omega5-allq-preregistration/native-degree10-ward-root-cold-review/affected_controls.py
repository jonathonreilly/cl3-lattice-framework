from pathlib import Path
from fractions import Fraction as F
import types,sys,json,hashlib,tempfile
P=Path(__file__).resolve().parent;src=P.parent/'native-low-degree-ward-runtime-design'
for name in ['interval','compute','worker']:
 m=types.ModuleType(name);m.__file__=str(src/(name+'.py'));exec(compile((src/(name+'.py')).read_bytes(),m.__file__,'exec'),m.__dict__);sys.modules[name]=m
I=sys.modules['interval'];worker=sys.modules['worker'];worker.load=lambda b:(I.point(F(4,5)),I.point(F(15)))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v)+'\n')
with tempfile.TemporaryDirectory(dir=P)as tmp:
 t=Path(tmp);out=t/'out';out.mkdir();wp=t/'wp';wp.mkdir();rs=t/'source';save(rs,{'rows':[{}, {'interval':['12/5','12/5']},{'interval':['15','15']}]});save(wp/'BINDING.json',{'files':{'result':str(rs)}});bh=sha(wp/'BINDING.json');save(t/'WORKER_AUTHORIZATION.json',{});save(out/'STARTED.json',{});worker.run({'_binding_file_sha256':bh},out)
 save(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_NEW_DEGREE10_ONLY','runtime_sha256':'fake','result_sha256':sha(out/'RESULT.json'),'rss_bytes':100,'seconds':1,'binding_sha256':bh})
 s=types.ModuleType('schema');s.__file__=str(t/'schema.py');path=P.parent/'native-degree10-ward-root-review/schema.py';exec(compile(path.read_bytes(),str(path),'exec'),s.__dict__);rf={'worker_path':str(wp),'worker_freeze':'fake'}
 part=json.loads((out/'PARTIAL.json').read_text());part['seconds']='not-a-time';save(out/'PARTIAL.json',part)
 try:s.check(out,rf,2,lambda x:None);v='ACCEPTED_BAD_PARTIAL_TIME'
 except ValueError:v='REJECTED_BAD_PARTIAL_TIME'
 save(P/'AFFECTED_CONTROLS.json',{'full_synthetic_205':'PRIOR_PASS_NOT_REPEATED','adverse':v,'accepted_scalar_loads':0});print(v)
