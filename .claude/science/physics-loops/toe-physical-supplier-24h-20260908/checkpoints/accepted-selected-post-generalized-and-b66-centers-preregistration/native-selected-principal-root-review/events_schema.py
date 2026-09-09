from fractions import Fraction as F

def expected():
 x=[('selected_entry',{'a':a,'b':b})for a in range(24)for b in range(a,24)]+[('selected_gram',{})]
 for i in range(48):
  x += [('candidate_pivot',{'i':i,'j':j})for j in range(i+1)];x.append(('candidate_factor_row',{'row':i}))
 x += [('candidate_inverse_entry',{'i':i,'j':j})for j in range(48)for i in range(j,-1,-1)]
 return x+[(s,{})for s in ('dyadic_inputs','H_integer','error','coefficient_box')]
def validate(events,a,candidate,orbit,req):
 ex=expected();req(len(ex)==2705 and len(events)<=len(ex),'finite event count')
 for j,e in enumerate(events):
  stage,keys=ex[j];req(type(e['sequence'])is int and e['sequence']==j and e['stage']==stage and isinstance(e['data'],dict),'event order')
  d=e['data']
  for k,v in keys.items():req(type(d[k])is int and d[k]==v,'event coordinate')
  def walk(x):
   if type(x)is int:req(x.bit_length()<=32768,'integer bits')
   elif isinstance(x,list):
    for y in x:walk(y)
   elif isinstance(x,dict):
    for y in x.values():walk(y)
   elif isinstance(x,str):
    q=F(x);req(q.numerator.bit_length()<=32768 and q.denominator.bit_length()<=32768,'rational bits')
   else:raise ValueError('event numeric type')
  walk(d)
  def matrix(x,n,m):req(isinstance(x,list)and len(x)==n and all(isinstance(r,list)and len(r)==m for r in x),'matrix shape')
  if stage=='selected_entry':req(len(d['g'])==len(d['j'])==2 and d['g'][0]<=d['g'][1]and d['j'][0]<=d['j'][1],'entry intervals')
  elif stage=='selected_gram':
   matrix(d['center'],48,48);matrix(d['radii'],48,48);req(0<len(d['labels'])<=96,'support count');matrix(d['E'],len(d['labels']),48)
  elif stage=='candidate_factor_row':req(len(d['values'])==48,'factor row')
  elif stage=='dyadic_inputs':
   matrix(d['Gcenter'],48,48);matrix(d['radius'],48,48);matrix(d['T'],48,48);req(0<len(d['E'])<=96 and d['scale']==1<<256,'dyadic shape/scale');matrix(d['E'],len(d['E']),48)
  elif stage=='H_integer':matrix(d['H'],48,48);req(d['denominator']==1<<768,'H scale')
  elif stage=='coefficient_box':req(0<len(d['center'])<=96,'coefficient support');matrix(d['center'],len(d['center']),48)
 status=a['status']
 if status=='CERTIFIED_ENCLOSURE':
  req(len(events)==2705,'full certificate stages');req(events[-1]['data']['center']==a['center']and F(events[-1]['data']['radius'])==F(a['radius'])and F(events[-2]['data']['e'])==F(a['e']),'retained certificate equality')
 elif status=='INDETERMINATE_RESIDUAL':req(len(events)==2704 and F(a['e'])>=1 and F(events[-1]['data']['e'])==F(a['e']),'residual failure evidence')
 else:
  req(status=='INDETERMINATE_LIMIT_OR_CANDIDATE'and 301<=len(events)<=2705 and a['failure_kind']in('Limit','CandidateFailure')and type(a['error'])is str and a['error'].startswith(a['failure_kind']+'('),'limit prefix')
  req(a['current']=={'stage':events[-1]['stage'],'orbit':orbit},'failure last stage')
 inv=[e['data']for e in events if e['stage']=='candidate_inverse_entry']
 if candidate is not None:
  req(len(inv)==1176 and len(candidate)==48 and all(len(r)==48 for r in candidate),'complete candidate shape')
  for d in inv:req(F(candidate[d['i']][d['j']])==F(d['value'],1<<256),'candidate delta equality')
  req(all(F(candidate[i][i])>0 and all(F(candidate[i][j])==0 for j in range(i))for i in range(48)),'candidate positive upper')
 elif status!='INDETERMINATE_LIMIT_OR_CANDIDATE':req(False,'missing complete candidate')
