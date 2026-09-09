from fractions import Fraction as F

def validate(events,ans,oi,req):
 def box(x):req(isinstance(x,list)and len(x)==2 and all(type(v)is int and abs(v).bit_length()<=4096 for v in x)and x[0]<=x[1],'typed interval')
 def mat(a,n,m,interval=True):
  req(isinstance(a,list)and len(a)==n and all(isinstance(row,list)and len(row)==m for row in a),'matrix shape')
  for row in a:
   for x in row:
    if interval:box(x)
    else:
     q=F(x);req(max(abs(q.numerator).bit_length(),q.denominator.bit_length())<=65536,'scalar bits')
 ids=events[0][1]['indices'];R=set()
 for i in ids:
  if i>=396:R.update((i,g)for g in(0,1))
  else:
   n,t=divmod(i,6);a=t//2;R.update((6*n+a+off,g)for off in(0,3)for g in(0,1))
 R=sorted(R);U=sorted(set(R)|{(r,g)for r in(396,399,400,401)for g in(0,1)});raw=sorted({r for r,g in U});u=len(U);nr=len(R)
 schedule=[];terms=0
 def add(s,fn=lambda d:None):schedule.append((s,fn))
 def equality(d,expected):req(d==expected,'stage metadata')
 add('selected_candidate')
 count=0
 for j,r in enumerate(raw):
  for s in raw[j:]:
   add('acquisition_current',lambda d,r=r,s=s,c=count:equality(d,dict(raw_i=r,raw_j=s,completed=c)))
   count+=1
   def acquired(d,r=r,s=s,c=count):
    req(d['i']==r and d['j']==s and type(d['i'])is int and type(d['j'])is int and type(d['count'])is int and d['count']==c,'raw pair order');box(d['G']);box(d['J'])
   add('acquired_raw',acquired)
 req(count<=1378,'raw cap')
 def principal(d):req(d['U']==[list(x)for x in U]and type(d['raw_pairs'])is int and d['raw_pairs']==count,'principal census');mat(d['M'],u,u)
 add('physical_principal',principal)
 def product(n,k,m):
  nonlocal terms
  old=terms;terms+=n*k*m;new=terms
  add('matrix_product_start',lambda d:equality(d,dict(rows=n,inner=k,columns=m,completed_terms=old)))
  def finish(d):req(type(d['completed_terms'])is int and d['completed_terms']==new,'term count');mat(d['matrix'],n,m)
  add('matrix_product_raw',finish)
 product(nr,48,48) # E has nr rows,48 columns.
 def emb(d):
  req(d['R']==[list(x)for x in R]and d['U']==[list(x)for x in U],'support');mat(d['E'],nr,48);mat(d['C_U'],u,48)
 add('embedding',emb);product(u,u,48);product(48,u,48);add('H_raw',lambda d:mat(d,48,48))
 for imp in(399,400):
  def ac(d,imp=imp):req(type(d['impurity'])is int and d['impurity']==imp,'impurity');mat(d['B_U'],u,48)
  add('action_columns',ac);product(u,u,48);product(48,u,48);product(48,u,48)
  def az(d,imp=imp):req(d['impurity']==imp and type(d['impurity'])is int,'impurity');mat(d['A'],48,48);mat(d['Z'],48,48)
  add('A_Z_raw',az);product(48,48,48);product(48,48,48)
  def inv(d,imp=imp):req(d['impurity']==imp and type(d['impurity'])is int and type(d['terms'])is int and d['terms']==4,'inverse candidate');mat(d['X'],48,48)
  add('inverse_candidate',inv)
  def wrapped(fn,imp=imp):
   def run(d):req(type(d['impurity'])is int and d['impurity']==imp,'impurity');fn(d['data'])
   return run
  add('frame_residual',wrapped(lambda d:req(F(d['e'])>=0,'frame e')))
  # Select only the branch actually reported for this impurity. Refused prefixes
  # use the complete branch as a permitted prefix until the failure point.
  frames=[d['data'] for st,d in events if st=='frame_residual' and d.get('impurity')==imp]
  if frames and F(frames[0]['e'])>=1:continue
  add('inverse_residual',wrapped(lambda d:req(all(F(d[k])>=0 for k in('r','epsilon','A_norm'))and F(d['a'])>0,'inverse scalars')))
  for stage in('AXA','N_raw'):add(stage,wrapped(lambda d:mat(d,48,48)))
  def schur(d):mat(d['N0'],48,48,False);req(F(d['N_radius'])>=0,'N radius')
  add('Schur_center',wrapped(schur));add('Schur_center',wrapped(schur))
  def result(d):req(0<=F(d['e'])<1 and d['entrywise_C_claim']is False,'certificate scope')
  add('result',wrapped(result))
 refused=ans['status']=='INDETERMINATE_CERTIFICATE'
 data=events[:-1]if refused else events
 req(len(data)<=len(schedule)if refused else len(data)==len(schedule),'complete stage count')
 for (stage,d),(expected,fn)in zip(data,schedule):req(stage==expected,'stage order');fn(d)
 if refused:
  req(events[-1]==('indeterminate',ans)and ans['error'].startswith('Refused(')and len(data)>0,'honest refusal')
  req(ans['current']==dict(orbit=oi,stage=data[-1][0],serial=len(data)-1),'failure current')
 return count
