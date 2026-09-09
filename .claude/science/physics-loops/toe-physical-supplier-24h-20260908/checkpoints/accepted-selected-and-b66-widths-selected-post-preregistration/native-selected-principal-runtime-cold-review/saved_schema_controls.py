from pathlib import Path
import tempfile,json,hashlib,sys
sys.path.insert(0,'/private/tmp/toe-24h-probes-20260908/native-selected-principal-saved-root-review')
import schema
outcomes=[]
with tempfile.TemporaryDirectory()as temp:
 p=Path(temp);o=p/'out';o.mkdir();acc=p/'a.json';rf={'authorization':{},'worker_freeze':'dummy','acceptance':str(acc)}
 def put(n,x): (o/n).write_text(json.dumps(x))
 row=lambda i:dict(orbit=i,status='PASS_SAVED_MATRIX_CERTIFICATE',certificate_replayed=True,e='0',radius='0',width_pass=True,l1_pass=True)
 a={'orbits':[row(i)for i in range(5)]};acc.write_text(json.dumps(a))
 z=[[0]*48 for _ in range(48)]
 def setup():
  for f in o.iterdir():f.unlink()
  rows=[row(i)for i in range(5)]
  r=dict(status='PASS_INDEPENDENT_SELECTED_SAVED',entry_truth_inherited=True,seconds=.5,rows=rows)
  put('RESULT.json',r);put('PARTIAL.json',dict(current=dict(stage='complete',orbit=5),rows=rows));put('STARTED.json',{})
  put('WORKER_COMPLETE.json',dict(status='COMPLETE_SELECTED_SAVED',runtime_sha256='dummy',binding_sha256='x',result_sha256=hashlib.sha256((o/'RESULT.json').read_bytes()).hexdigest(),seconds=1,rss_bytes=100))
  rf['authorization']={'binding_sha256':'x'};put('STARTED.json',rf['authorization'])
  events=[]
  def e(s,i,d={}):events.append(dict(current=dict(stage=s,orbit=i),data=d))
  e('initial_pins',0)
  for i in range(5):
   for s in ('before_orbit_parse','before_selected_entries','selected_reconstruction'):e(s,i)
   ds={'dyadic_inputs':dict(Gcenter=z,radius=z,T=z,E=z,scale=2**256),'H_integer':dict(H=z,denominator=2**768),'error':dict(e='0'),'coefficient_box':dict(center=z,radius='0')}
   for s,d in ds.items():e('independent_'+s,i,d);e('verified_'+s,i)
   e('orbit_complete',i+1)
  e('final_pins',5);e('complete',5)
  (o/'INDEPENDENT.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in events))
 def test(name,fn=None,yes=False):
  setup()
  if fn:fn()
  try:schema.check(o,rf,2);ok=True
  except Exception:ok=False
  assert ok==yes,name
  outcomes.append({'case':name,'accepted':ok})
 test('full five orbit actual schema',yes=True)
 test('failure extra',lambda:put('FAILURE.json',{}))
 test('empty intermediates',lambda:(o/'INDEPENDENT.ndjson').write_text(''))
 def change(name,key,value):
  x=json.loads((o/name).read_text());x[key]=value;put(name,x)
 test('wrong timing',lambda:change('WORKER_COMPLETE.json','seconds',False))
 test('wrong digest',lambda:change('WORKER_COMPLETE.json','result_sha256','bad'))
 test('stale partial',lambda:put('PARTIAL.json',{}))
print(json.dumps({'status':'PASS','scope':'fabricated shapes only, no matrix arithmetic or native data','cases':outcomes},indent=2))
