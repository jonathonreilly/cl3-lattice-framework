"""Strict source identity/extraction. No supplier or native moment arithmetic."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
import interval as I
import history
S=1<<256

def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as stream:
  for chunk in iter(lambda:stream.read(1048576),b''):h.update(chunk)
 return h.hexdigest()
def read(spec):
 need(sha(spec['path'])==spec['sha256'],'input hash');return json.loads(Path(spec['path']).read_text())
def family(spec):
 o={k:read(spec['files'][k])for k in('acceptance','worker','receipt','root_freeze','result')};a,w,r,f=o['acceptance'],o['worker'],o['receipt'],o['root_freeze'];e=spec['expected']
 need(a['status']==e['acceptance']and a['once']is True,'accepted status')
 need(a['result_sha256']==spec['files']['result']['sha256']==w['result_sha256'],'result chain')
 need(a['worker_freeze']==spec['worker_freeze']==w['runtime_sha256']==r['worker_freeze']==f['worker_freeze'],'worker chain')
 need(a['root_freeze']==spec['files']['root_freeze']['sha256'],'root chain')
 need(w['status']==e['worker']and o['result']['status']==e['result'],'completion status')
 need(r['pass']is True and r['failure']is None and type(r['returncode'])is int and r['returncode']==0,'root completion')
 for v,cap in((w['seconds'],e['worker_seconds']),(r['seconds'],e['root_seconds']),(a['external_seconds'],e['external_seconds'])):need(type(v)in(int,float)and math.isfinite(v)and 0<v<cap,'receipt time')
 need(w['seconds']<=r['seconds']<=a['external_seconds'],'time order')
 for v in(w['rss_bytes'],r['sampled_whole_tree_peak'],a['sampled_whole_tree_peak'],a['external_rss_bytes']):need(type(v)is int and 0<v<=384*1048576,'receipt RSS')
 need(r['sampled_whole_tree_peak']==a['sampled_whole_tree_peak'],'tree equality')
 return o['result']
def select(events,stage,mode,kind=None):
 v=[e['data']for e in events if e['stage']==stage and e['choice']==mode and(kind is None or e['data'].get('kind')==kind)]
 need(len(v)==1,'unique '+stage);return v[0]
def grid(box):
 need(type(box)is list and len(box)==2,'complex grid')
 for pair in box:need(type(pair)is list and len(pair)==2 and all(type(x)is int and abs(x).bit_length()<=4096 for x in pair)and pair[0]<=pair[1],'literal grid endpoints')
 need(box[1][0]<=0<=box[1][1],'real moment containment');return F(box[0][0],S),F(box[0][1],S)
def load(b,emit):
 need(b['high']is not None,'NOT_READY: accepted high moments absent')
 emit('before_bound_inputs',{'families':['degree20','posterior20','high']})
 old=family(b['degree20']);post=family(b['posterior20']);high=family(b['high'])
 # The high supplier and posterior must bind the exact original255-event producer.
 hb=read(b['high']['binding']);pb=read(b['posterior20']['binding'])
 need(hb['degree20']['files']['events']==b['degree20']['files']['events']and hb['degree20']['files']['result']==b['degree20']['files']['result'],'high lower source identity')
 need(pb['files']['events']==b['degree20']['files']['events']and pb['files']['result']==b['degree20']['files']['result'],'posterior original identity')
 spec=b['degree20']['files']['events'];need(sha(spec['path'])==spec['sha256'],'event stream hash')
 events=[json.loads(line)for line in Path(spec['path']).read_text().splitlines()]
 need(len(events)==255 and all(type(e['sequence'])is int and e['sequence']==i for i,e in enumerate(events,1)),'original255 sequence')
 need([(e['stage'],e['choice'])for e in events]==history.schedule(),'original full chronology')
 need(type(old['events'])is int and old['events']==255 and type(old['choices'])is int and old['choices']==2,'original result census')
 need(type(post['source_events'])is int and post['source_events']==255 and type(post['choices'])is int and post['choices']==2,'posterior census')
 need(type(high['first_order'])is int and high['first_order']==7 and type(high['native_lower_moments_recomputed'])is int and high['native_lower_moments_recomputed']==0 and type(high['native_oracle_calls'])is int and high['native_oracle_calls']==0,'high scope')
 need([r['kind']for r in high['rows']]==['P','O'],'high class order');hm={r['kind']:r for r in high['rows']};packet={};lows={}
 tables=read(b['high']['tables']);need(tables['units']=='dimensionless_h1'and type(tables['grid_bits'])is int and tables['grid_bits']==256,'same units/grid')
 for kind in('P','O'):
  copies=[]
  for mode in('residual','variational'):
   rows=[e['data']for e in events if e['stage']=='vacuum_moment_raw'and e['choice']==mode and e['data'].get('kind')==kind]
   need(len(rows)==7 and all(type(r['index'])is int and r['index']==j for j,r in enumerate(rows)),'lower order');copies.append(rows)
  need(copies[0]==copies[1],'unchanged lower copies');lows[kind]=[]
  for j,r in enumerate(copies[0]):
   im=I.box(r['imaginary']);need(im[0]<=0<=im[1],'real lower');v=I.box(r['real']);lows[kind].append(v)
   lo=v[0].numerator*S//v[0].denominator;hi=-((-v[1].numerator*S)//v[1].denominator)
   need(tables['classes'][kind]['accepted_m'][str(j)]==[[lo,hi],[0,0]],'high exact lower mapping')
  r=hm[kind];need(r['orders']==[7,8,9,10]and all(type(x)is int for x in r['orders'])and set(r['moments'])==set(map(str,range(7,11))),'high orders')
  lows[kind]+=[grid(r['moments'][str(j)])for j in range(7,11)]
 for index,mode in enumerate(('residual','variational')):
  gate=select(events,'gate_inputs',mode);original=old['rows'][index];prior=post['rows'][index];saved=read(b['posterior20']['mode_inputs'][mode])
  need(original['mode']==prior['mode']==mode and original['nominal']==prior['nominal']==gate['nominal']and saved['gate']==gate,'unchanged same trial nominal/gate')
  rows={}
  for kind in('P','O'):
   p=select(events,'first_polynomial',mode,kind)['coefficients'];raw=select(events,'residual_raw',mode,kind);g=gate['rows'][kind]
   need(p==g['p']and raw['q']==g['q']==saved['q'][kind]and raw['r2']==g['r2']and raw['t2']==g['t2'],'same p/q/residual source')
   need(saved['s0'][kind]==[e['data']['real']for e in events if e['stage']=='source_moment_raw'and e['choice']==mode and e['data'].get('kind')==kind and type(e['data'].get('index'))is int and e['data']['index']==0][0],'source norm identity')
   rho0=I.box(raw['r2']);rows[kind]={'moments':lows[kind],'p':list(map(I.parse,p)),'r2':rho0,'t2':I.box(raw['t2']),'old_first_squared_upper':I.check(rho0[1]*16)}
  packet[mode]={'rows':rows,'nominal':I.box(gate['nominal']),'old_alpha':I.box(prior['alpha_interval']),'trial_a2':I.point(I.parse(prior['a_squared_upper'])),'trial_b2':I.point(I.parse(prior['b_squared_upper']))}
 emit('authenticated_same_trial_inputs',packet);return packet
