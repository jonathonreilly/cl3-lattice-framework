"""Width ledger only: no integrand center, moments or B outputs."""
from fractions import Fraction as F
import json,time
import ledger,input_loader,caps,recover

def run(out,binding):
 start=time.monotonic();current={'stage':'load'};done=[];count=0
 def save(): (out/'PARTIAL.json').write_text(json.dumps({'current':current,'poles':done,'node_checks':count,'seconds':time.monotonic()-start},default=str)+'\n')
 save()
 try:
  poles,rows,nodes=input_loader.load(binding['physical'])
  current={'stage':'recover_pole0'};save();recovered_total,recovered_separated=recover.load(binding['prior'],out)
  guarded=caps.operand;up=caps.upward
  for n in nodes:
   if not 0<n['t_interval'][0]<n['t_interval'][1]<=8 or n['t_interval'][1]-n['t_interval'][0]>F(1,2**140) or not 0<n['weight_interval'][0]<=n['weight_interval'][1] or n['weight_interval'][1]-n['weight_interval'][0]>F(1,10**38):raise ValueError('geometry input gate')
  if sum(n['weight_interval'][1]for n in nodes)>9:raise ValueError('mapped weight sum')
  for i in range(66):
   s=F(poles[i]['s_midpoint']);ass=tuple(map(F,rows[i]['oracle']['A']));aps=tuple(map(F,rows[i]['oracle']['Aprime']));total=[F(0),F(0)];separated=True;current={'stage':'pole','pole':i};save()
   if i==0:
    total=recovered_total;separated=recovered_separated;count=1742
   else:
    with(out/f'NODES_{i:02d}.ndjson').open('x')as log:
     for n in nodes:
      current={'stage':'node','pole':i,'node':n['id']}
      if n['id']%26==0:save()
      for x in (s,*n['t_interval'],*n['A_interval'],*ass,*aps,*n['weight_interval']):guarded(x)
      try:r,info=ledger.node(s,n['t_interval'],n['A_interval'],ass,aps,n['weight_interval'])
      except ValueError as e:
       if 'denominator does not separate'not in str(e):raise
       separated=False;r=(F(0),F(0));info={'separation_failure':str(e)}
      caps.tree(info);r=tuple(up(x)for x in r);total=[total[k]+r[k]for k in range(2)];count+=1;log.write(json.dumps({'node':n['id'],'panel':n['panel'],'radii':r,'info':info,'cumulative_radii':total},default=str)+'\n')
      if n['id']%26==25:log.flush();save()
   result=caps.tree(ledger.total(s,ass,aps,total));result['separated']=separated;result['pole']=i;result['s']=str(s);result['status']='FEASIBLE_UNDER_DECLARED_ARITHMETIC_RESERVE'if separated and all(result['passes'])else'INDETERMINATE_WIDTH_OR_SEPARATION'
   (out/f'POLE_{i:02d}.json').write_text(json.dumps(result,default=str)+'\n');done.append({'pole':i,'status':result['status'],'separated':separated,'passes':result['passes']});save()
  if count!=114972:raise ValueError('node count')
  result={'status':'COMPLETE_REMAINING65_WIDTH_DIAGNOSTIC','recovered_node_records':1742,'new_node_checks':113230,'all_feasible':all(r['status']=='FEASIBLE_UNDER_DECLARED_ARITHMETIC_RESERVE'for r in done),'poles':done,'node_checks':count,'moments_evaluated':0,'integral_centers_evaluated':0,'oracle_calls':0,'seconds':time.monotonic()-start};(out/'RESULT.json').write_text(json.dumps(result)+'\n');current={'stage':'complete'};save()
 except BaseException as e:save();(out/'FAILURE.json').write_text(json.dumps({'current':current,'completed':done,'node_checks':count,'error':repr(e)})+'\n');raise
