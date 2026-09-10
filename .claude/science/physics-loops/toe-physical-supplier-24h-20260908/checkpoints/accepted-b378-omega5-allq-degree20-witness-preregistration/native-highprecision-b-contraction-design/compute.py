"""Arithmetic body only. No CLI; accepted-input dispatcher is not yet supplied."""
import json,time
from fractions import Fraction as F
from interval import add,mul,neg,const
from interval_base import pi_bounds
from core import integrands,high_tail,moment

def run(out,poles,a66,catalog,selected_ids):
 # All inputs must be source/hash/acceptance verified by a future dispatcher.
 if selected_ids!=sorted(set(selected_ids)) or not selected_ids or any(i not in range(66) for i in selected_ids):raise ValueError('fixed pole ids')
 if len(poles)!=66 or len(a66)!=66 or len(catalog)!=1742:raise ValueError('input census')
 out.mkdir();(out/'PANELS').mkdir();(out/'POLES').mkdir();start=time.monotonic();stage='initial';current=None;rows=[];panels=[]
 def save(name,x):(out/name).write_text(json.dumps(x,indent=2)+'\n')
 def partial():save('PARTIAL.json',{'stage':stage,'current':current,'completed_panels':panels,'rows':rows,'seconds':time.monotonic()-start})
 partial()
 try:
  stage='moments';moments=[moment(n) for n in range(27)]
  sums={i:[const(0),const(0)] for i in selected_ids};fixed={}
  for i in selected_ids:
   raw=a66[i]['oracle'];s=F(poles[i]['s_midpoint'])
   if F(raw['s'])!=s:raise ValueError('A66 midpoint identity')
   fixed[i]=(const(s),tuple(map(F,raw['A'])),tuple(map(F,raw['Aprime'])))
  for j in range(-64,3):
   panel={i:[const(0),const(0)] for i in selected_ids};nodes=[v for v in catalog if v['panel']==j]
   if len(nodes)!=26:raise ValueError('panel census')
   for node in nodes:
    stage='contract';current={'panel':j,'node':node['id']}
    t=node['t_interval'];at=node['A_interval'];w=node['weight_interval']
    for i in selected_ids:
     current['pole']=i;s,a,da=fixed[i];g,h=integrands(s,t,a,da,at)
     panel[i]=[add(panel[i][0],mul(w,g)),add(panel[i][1],mul(w,h))]
   for i in selected_ids:sums[i]=[add(sums[i][k],panel[i][k]) for k in (0,1)]
   stage='panel_saved';name=f'PANELS/{j+64:02d}.json'
   save(name,{'panel':j,'values':{str(i):[[str(x) for x in v] for v in panel[i]] for i in selected_ids},'cumulative':{str(i):[[str(x) for x in v] for v in sums[i]] for i in selected_ids}})
   panels.append({'panel':j,'path':name});partial()
  radius=F(400,27)*F(4,25)**26;low=F(1,3*2**64);pl,pu=pi_bounds();factor=(2/pu,2/pl)
  for i in selected_ids:
   stage='finish';current={'pole':i};s,a,da=fixed[i];tail=high_tail(s,a,da,moments);answers=[]
   for k in (0,1):
    v=mul(add(add(sums[i][k],tail[k]),(-radius,radius+low)),factor)
    answers.append(neg(v) if k else v)
   widths=[v[1]-v[0] for v in answers]
   row={'id':i,'s_midpoint':str(s[0]),'B':[str(x) for x in answers[0]],'Bprime':[str(x) for x in answers[1]],'widths':[str(x) for x in widths],'target':'1/5000000000000000000','status':'PENDING'}
   rows.append(row);save(f'POLES/{i:02d}.json',row);partial()
   row['status']='CERTIFIED_TARGET' if max(widths)<=F(2,10**19) else 'INDETERMINATE'
   save(f'POLES/{i:02d}.json',row);partial()
  save('RESULT.json',{'status':'COMPLETE_FIXED_CASES','rows':rows,'selected_ids':selected_ids,'pairs':1742*len(selected_ids),'all_targets_met':all(r['status']=='CERTIFIED_TARGET' for r in rows),'seconds':time.monotonic()-start,'exact_gauss_root_values':False,'midpoint_displacement_requires_separate_ledger':True,'matrix_computed':False,'alpha_computed':False})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'current':current,'panels':panels,'rows':rows,'error':repr(e)});raise
