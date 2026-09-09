from pathlib import Path
import types,json
p=Path(__file__).with_name('schema.py');m=types.ModuleType('schema');exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
rows=list(m.expected());m.req(len(rows)==2010 and sum(len(v) for _,v in rows)==6015,'census');m.req(rows[0][0]==dict(orbit_id=0,type='bare_to_pole',append_index=399,pole_id=0,sigma=-1),'first');m.req(rows[132]==(dict(orbit_id=0,type='bare_to_insertion',append_index=399),[396,397,398]),'insertion');m.req(rows[-1]==(dict(orbit_id=4,type='bare_self',append_index=401),[401]),'last');m.iv([0,1]);n=5
for bad in ([True,1],[2,1],[0],['0',1]):
 try:m.iv(bad)
 except ValueError:n+=1
 else:raise ValueError('bad interval accepted')
print(json.dumps({'status':'PASS','predicates':n,'native_calls':0,'scope':'metadata census and tiny fabricated interval controls, no output fixture'}))
