"""Future authenticated normalized-source replay, NEVER called during preparation."""
import json
from pathlib import Path
from fractions import Fraction as F
import arithmetic as a

def check(source,out,emit):
 """source is supplied only by a future reviewed immutable-source binder."""
 if source.get('status')!='AUTHENTICATED_ACTUAL_CENTER_AND_WIDTH_OUTPUTS':raise ValueError('NOTREADY')
 read=lambda p:json.loads(Path(p).read_text());pair=a.vector
 M=a.moments();pi=a.pi();count=0;results=[]
 if len(source['poles'])!=66 or len(source['nodes'])!=1742:raise ValueError('fixed family')
 for i,p in enumerate(source['poles']):
  emit({'stage':'pole','pole':i});s=a.fraction(p['s']);As=a.interval(p['A']);Ap=a.interval(p['Aprime']);od=Path(source['output'])/f'POLE_{i:02d}'
  total=[F(0),F(0)];panel=[F(0),F(0)];errors=[F(0),F(0)]
  with(od/'CENTERS.ndjson').open()as log,Path(p['radius_file']).open()as radii:
   for j,node in enumerate(source['nodes']):
    emit({'stage':'center','pole':i,'node':j,'checked':count});saved=json.loads(next(log));old=json.loads(next(radii))
    if type(saved['node'])is not int or saved['node']!=j or type(saved['panel'])is not int or saved['panel']!=j//26-64:raise ValueError('saved node order')
    if type(old['node'])is not int or type(old['panel'])is not int or old['node']!=j or old['panel']!=j//26-64:raise ValueError('radius order')
    exact=a.weighted(s,a.interval(node['t']),a.interval(node['A']),As,Ap,a.interval(node['w']))
    emit({'stage':'computed_center','pole':i,'node':j,'computed':list(map(str,exact)),'saved':saved['centers']})
    if pair(saved['centers'])!=exact:raise ValueError('independent center mismatch')
    rr=pair(old['radii'])
    if pair(saved['accepted_radii'])!=rr or min(rr)<0:raise ValueError('inherited radii')
    panel=[panel[k]+exact[k]for k in range(2)];errors=[errors[k]+rr[k]for k in range(2)];count+=1
    if pair(saved['panel_cumulative'])!=tuple(panel):raise ValueError('node cumulative')
    if j%26==25:
     total=[total[k]+panel[k]for k in range(2)];q=read(od/f'PANEL_{j//26:02d}.json')
     if type(q['panel'])is not int or q['panel']!=j//26-64:raise ValueError('panel id')
     if pair(q['centers'])!=tuple(panel)or pair(q['cumulative'])!=tuple(total)or pair(q['accepted_radius_cumulative'])!=tuple(errors):raise ValueError('panel sums')
     panel=[F(0),F(0)]
   if log.readline()or radii.readline():raise ValueError('extra rows')
  low,high=a.tails(s,As,Ap,M);budget=read(od/'TAILS_AND_BUDGET.json');oldbudget=read(p['budget_file'])
  if pair(budget['low_centers'])!=low or pair(budget['high_centers_with_half_remainder'])!=high:raise ValueError('tail center')
  lr=pair(oldbudget['low_radii']);hr=pair(oldbudget['high_input_radii']);rem=F(12**40,81*8**81);quad=F(128,4**52)
  rad=[errors[k]+lr[k]+hr[k]+rem/2+quad+F(1,10**35)for k in range(2)];c=[total[k]+low[k]+high[k]for k in range(2)]
  if pair(oldbudget['widths'])!=tuple(F(200,157)*x+F(1,10**35)for x in rad):raise ValueError('accepted total radius')
  if pair(budget['middle'])!=tuple(total)or pair(budget['node_radii'])!=tuple(errors)or F(budget['positive_remainder'])!=rem or F(budget['quadrature_radius'])!=quad or F(budget['arithmetic_reserve'])!=F(1,10**35):raise ValueError('budget components')
  if pair(budget['total_centers'])!=tuple(c)or pair(budget['total_radii'])!=tuple(rad):raise ValueError('total inputs')
  ans=a.final(c,rad,pi);row=read(od/'RESULT.json');widths=tuple(x[1]-x[0]for x in ans)
  if type(row['pole'])is not int or row['pole']!=i or F(row['s_midpoint'])!=s or pair(row['targets'])!=(F(2,10**28),F(2,10**27)):raise ValueError('row scope')
  if a.interval(row['B'])!=ans[0]or a.interval(row['Bprime'])!=ans[1]or pair(row['widths'])!=widths:raise ValueError('final enclosures')
  flag=widths[0]<=F(2,10**28)and widths[1]<=F(2,10**27)
  if row['status']!=('CERTIFIED_TARGET'if flag else'INDETERMINATE_TARGET'):raise ValueError('target status')
  results.append({'pole':i,'target_met':flag});emit({'stage':'pole_complete','pole':i,'checked':count,'results':results})
 return {'status':'PASS_ALL_SAVED_CENTER_FORMULAS','node_pairs':count,'panels':4422,'tail_terms':40,'poles':results,'inherited_width_radii':True,'oracle_calls':0}
