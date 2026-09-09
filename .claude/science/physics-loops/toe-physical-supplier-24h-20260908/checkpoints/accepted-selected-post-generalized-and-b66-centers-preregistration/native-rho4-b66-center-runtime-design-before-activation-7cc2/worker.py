"""New fixed66 center certificates, using accepted error radii without recomputing them."""
import json,os,time
from pathlib import Path
from fractions import Fraction as F
import core,binder
from interval_base import pi_bounds

def save(path,data):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,default=str,separators=(',',':'))+'\n');os.replace(tmp,path)
def run(out,b):
 start=time.monotonic();rows=[];count=0;current={'stage':'bind'};out=Path(out)
 def partial():save(out/'PARTIAL.json',{'current':current,'rows':rows,'node_centers':count,'seconds':time.monotonic()-start})
 partial()
 try:
  poles,scalars,nodes=binder.load(b);current={'stage':'new_exact_moments'};partial()
  M=core.moments(40);save(out/'MOMENTS.json',{'moment_indices':list(range(41)),'values':list(map(str,M))});pl,pu=pi_bounds();save(out/'PI.json',{'interval':[str(pl),str(pu)]})
  for i in range(66):
   current={'stage':'pole','pole':i};partial();od=out/f'POLE_{i:02d}';od.mkdir();s=F(poles[i]['s_midpoint']);raw=scalars[i]['oracle'];ass=tuple(map(F,raw['A']));aps=tuple(map(F,raw['Aprime']))
   if F(raw['s'])!=s or max(abs(s.numerator).bit_length(),s.denominator.bit_length())>256:raise ValueError('exact fixed pole')
   for x in(*ass,*aps):
    if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>512:raise ValueError('pole scalar512')
   sums=[F(0),F(0)];errors=[F(0),F(0)];panel=[F(0),F(0)];node_count=0
   with Path(b['node_files'][i]).open()as old,(od/'CENTERS.ndjson').open('x')as log:
    for n in nodes:
     current={'stage':'node','pole':i,'node':n['id']};save(out/'CURRENT.json',current);d=json.loads(next(old));j=n['id']
     if type(d['node'])is not int or d['node']!=j or type(d['panel'])is not int or d['panel']!=n['panel']:raise ValueError('saved radius ordering')
     rr=tuple(map(F,d['radii']))
     if len(rr)!=2 or any(x<0 or (x*core.S).denominator!=1 for x in rr)or 'separation_failure'in d['info']or F(d['info']['denominator_lower_abs'])<=0:raise ValueError('saved separated radii')
     errors=[core.guard(errors[k]+rr[k])for k in range(2)]
     if tuple(map(F,d['cumulative_radii']))!=tuple(errors):raise ValueError('saved radius cumulative')
     vals=core.center(s,n['t_interval'],n['A_interval'],ass,aps,n['weight_interval'])
     panel=[core.guard(panel[k]+vals[k])for k in range(2)];node_count+=1;count+=1
     log.write(json.dumps({'node':j,'panel':n['panel'],'centers':vals,'panel_cumulative':panel,'accepted_radii':rr},default=str)+'\n');log.flush()
     if j%26==25:
      log.flush();sums=[core.guard(sums[k]+panel[k])for k in range(2)];save(od/f'PANEL_{j//26:02d}.json',{'panel':n['panel'],'centers':panel,'cumulative':sums,'accepted_radius_cumulative':errors});panel=[F(0),F(0)];partial()
    if old.readline():raise ValueError('extra saved node radius')
   if node_count!=1742:raise ValueError('1742 centers')
   current={'stage':'tails','pole':i};partial();high=core.tail_centers(s,ass,aps,M);low=core.low_centers(s,ass,aps)
   accepted=json.loads(Path(b['pole_files'][i]).read_text())
   if type(accepted['pole'])is not int or accepted['pole']!=i or F(accepted['s'])!=s or accepted['separated']is not True or accepted['passes']!=[True,True]or any(type(v)is not bool for v in accepted['passes'])or accepted['status']!='FEASIBLE_UNDER_DECLARED_ARITHMETIC_RESERVE':raise ValueError('accepted pole budget')
   low_r=list(map(F,accepted['low_radii']));high_r=list(map(F,accepted['high_input_radii']))
   if len(low_r)!=2 or len(high_r)!=2 or any(x<0 for x in low_r+high_r):raise ValueError('two nonnegative budget components')
   rem=F(12**40,81*8**81);quad=F(128,4**52);radii=[core.guard(errors[k]+low_r[k]+high_r[k]+rem/2+quad+core.RESERVE)for k in range(2)]
   if tuple(map(F,accepted['widths']))!=tuple(F(200,157)*r+F(1,10**35)for r in radii):raise ValueError('same certified radius ledger')
   centers=[core.guard(sums[k]+low[k]+high[k])for k in range(2)]
   save(od/'TAILS_AND_BUDGET.json',{'s':str(s),'A':list(map(str,ass)),'Aprime':list(map(str,aps)),'middle':sums,'low_centers':low,'high_centers_with_half_remainder':high,'node_radii':errors,'low_radii':low_r,'high_input_radii':high_r,'positive_remainder':rem,'quadrature_radius':quad,'arithmetic_reserve':core.RESERVE,'total_centers':centers,'total_radii':radii})
   ans=core.finalize(centers,radii,(pl,pu));widths=[v[1]-v[0]for v in ans];row={'pole':i,'s_midpoint':str(s),'B':list(map(str,ans[0])),'Bprime':list(map(str,ans[1])),'widths':list(map(str,widths)),'targets':[str(F(2,10**28)),str(F(2,10**27))],'status':'PENDING'}
   save(od/'RESULT.json',row);rows.append(row);partial()
   row['status']='CERTIFIED_TARGET'if widths[0]<=F(2,10**28)and widths[1]<=F(2,10**27)else'INDETERMINATE_TARGET';save(od/'RESULT.json',row);partial()
  if count!=114972:raise ValueError('fixed count')
  result={'status':'COMPLETE_NEW_RHO4_B66_CERTIFICATES','rows':rows,'all_targets_met':all(r['status']=='CERTIFIED_TARGET'for r in rows),'node_center_pairs':count,'poles':66,'panels_per_pole':67,'tail_terms':40,'moments':41,'oracle_calls':0,'old_protocol_replays':0,'matrix_computed':False,'alpha_computed':False,'seconds':time.monotonic()-start}
  save(out/'RESULT.json',result);current={'stage':'complete'};save(out/'CURRENT.json',current);partial();return result
 except BaseException as exc:
  try:partial();save(out/'FAILURE.json',{'current':current,'completed_rows':rows,'node_center_pairs':count,'error':repr(exc)})
  except BaseException as failure:exc.add_note('retention '+repr(failure))
  raise
