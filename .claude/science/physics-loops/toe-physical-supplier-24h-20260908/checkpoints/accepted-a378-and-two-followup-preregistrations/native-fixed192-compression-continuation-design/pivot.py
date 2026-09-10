"""Fixed192 arithmetic candidate. Caller supplies immutable true physical entries."""
from fractions import Fraction as F
import interval as iv
T=531;MAX_PAIRS=198

def square(x):
 lo,hi=x
 if lo>hi:raise ValueError('interval order')
 return (0 if lo<=0<=hi else min(lo*lo,hi*hi)//iv.S,-((-max(lo*lo,hi*hi))//iv.S))
def intersection(x,y):
 z=max(x[0],y[0]),min(x[1],y[1])
 if z[0]>z[1]:raise ValueError('empty proved intersection')
 return z
def divide(x,r):
 if r[0]<=0:raise ValueError('uncertain positive denominator')
 return iv.div(x,r)
def coordinate(x,r):return divide(x,iv.sqrt(r))
def midpoint_radius(x):
 m=(x[0]+x[1])//2;return m,max(m-x[0],x[1]-m)

def labels(augmented=True):
 lab=[('pole',n,s,eta,2) for n in range(66) for s in range(3) for eta in(-1,1)]
 if augmented:lab.extend(('append',0,s,1,1) for s in range(3))
 return tuple(lab)

def validate(lab,native):
 if not isinstance(lab,tuple) or not lab or len(set(lab))!=len(lab):raise ValueError('immutable unique labels')
 for kind,n,s,eta,weight in lab:
  if kind not in('pole','append') or eta not in(-1,1) or weight!=(2 if kind=='pole' else 1):raise ValueError('label/weight')
  if kind=='append' and eta!=1:raise ValueError('append chirality')
 if native and lab not in(labels(False),labels(True)):raise ValueError('canonical396/399 labels')

def run(entry,lab,persist,*,native=True,max_pairs=12, resume=(), initial_checkpoint=None):
 """entry(i,j) immutable G/J interval pair, symmetric/skew and chiral.
 No native reader/driver exists. persist writes each stage before dependent work.
 """
 validate(lab,native)
 if not 0<=max_pairs<=12:raise ValueError('continuation cumulative cap12')
 if native and (len(resume)!=4 or max_pairs!=12):raise ValueError('fixed four-to-twelve continuation')
 if initial_checkpoint is None:raise ValueError('authenticated final checkpoint required')
 n=len(lab);aug=any(l[0]=='append' for l in lab);bound=1062 if aug else 1058;threshold=F(1,10**6*bound)
 history=[];selected=set()
 # Caller authenticates the history file and its exact source/input identity.
 # Restore saved rows without asking entry() to recompute any completed pivot.
 for saved in resume:
  h=dict(saved);i=h['index']
  if type(i)is not int or not 0<=i<n or i in selected or h['chirality']!=lab[i][3]:raise ValueError('resume labels')
  for key in ('g','j'):
   h[key]=tuple(tuple(x) for x in h[key])
   if len(h[key])!=n or any(len(x)!=2 or any(type(t)is not int for t in x) or x[0]>x[1] for x in h[key]):raise ValueError('resume interval rows')
  h['r']=tuple(h['r'])
  if len(h['r'])!=2 or any(type(t)is not int for t in h['r']) or not 0<h['r'][0]<=h['r'][1]:raise ValueError('resume pivot')
  history.append(h);selected.add(i)
 if len(history)>max_pairs:raise ValueError('resume beyond cap')
 initial_pairs=len(history)
 audit={'intersections':0};current=None
 if initial_checkpoint['pairs']!=initial_pairs:raise ValueError('checkpoint pair count')
 initial_diag=tuple(tuple(x) for x in initial_checkpoint['diagonals'])
 if len(initial_diag)!=n or any(len(x)!=2 or any(type(t)is not int for t in x) or not 0<=x[0]<=x[1]<=T*iv.S for x in initial_diag):raise ValueError('saved diagonal shape')
 if any(initial_diag[i]!=(0,0) for i in selected):raise ValueError('selected diagonal must be exact zero')
 initial_raw=F(sum(lab[i][4]*initial_diag[i][1] for i in range(n)),iv.S)
 initial_dsq=F(initial_checkpoint['coordinate_radius_squared'])
 if initial_dsq<0 or F(initial_checkpoint['raw_residual_upper'])!=initial_raw:raise ValueError('saved checkpoint scalar consistency')
 if initial_checkpoint['residual_pass']!=(initial_raw<=threshold) or initial_checkpoint['coordinate_pass']!=(initial_dsq<=F(1,40000**2)):raise ValueError('saved checkpoint gates')
 def box(x,diagonal=False):
  z=intersection(x,(0,T*iv.S) if diagonal else(-T*iv.S,T*iv.S))
  if z!=x:audit['intersections']+=1
  return z
 def original(i,j):
  g,z=entry(i,j)
  if any(not isinstance(t,int) for pair in(g,z) for t in pair):raise ValueError('integer endpoints')
  g=box(g,i==j);z=box(z)
  # Verify that the original enclosure CONTAINS each mathematically known zero.
  if lab[i][3]!=lab[j][3]:g=intersection(g,iv.ZERO)
  if lab[i][3]==lab[j][3] or i==j:z=intersection(z,iv.ZERO)
  return g,z
 def residual(i,j):
  g,z=original(i,j)
  for h in history:
   gi,gj,ji,jj=h['g'][i],h['g'][j],h['j'][i],h['j'][j];r=h['r']
   numer=iv.add(square(gi),square(ji)) if i==j else iv.add(iv.mul(gi,gj),iv.mul(ji,jj))
   g=iv.sub(g,divide(numer,r));z=iv.sub(z,divide(iv.sub(iv.mul(gi,jj),iv.mul(ji,gj)),r))
  g=box(g,i==j);z=box(z)
  if i in selected or j in selected:g=intersection(g,iv.ZERO);z=intersection(z,iv.ZERO)
  if lab[i][3]!=lab[j][3]:g=intersection(g,iv.ZERO)
  if lab[i][3]==lab[j][3]:z=intersection(z,iv.ZERO)
  return g,z
 def coordinates():
  rows=[];weighted_sq=0
  for h in history:
   out=[]
   for vector in(h['g'],[iv.neg(z) for z in h['j']]):
    coords=[]
    for j,x in enumerate(vector):
     enclosure=coordinate(x,h['r']);m,rad=midpoint_radius(enclosure);weighted_sq+=lab[j][4]*rad*rad;coords.append((m,rad))
    out.append(tuple(coords))
   rows.append(tuple(out))
  # d² exact after reconstructing pole halves; append entries have weight1.
  dsq=F(weighted_sq,iv.S**2)
  return tuple(rows),dsq
 try:
  for step in range(len(history),max_pairs+1):
   if step==initial_pairs:
    # No entry or coordinate call here: restore the accepted terminal state.
    diag=initial_diag;raw=initial_raw;dsq=initial_dsq
    res_ok=initial_checkpoint['residual_pass'];coord_ok=initial_checkpoint['coordinate_pass']
    persist({'stage':'restored_checkpoint','pairs':initial_pairs,'raw_residual_upper':str(raw),'coordinate_radius_squared':str(dsq),'residual_pass':res_ok,'coordinate_pass':coord_ok})
   else:
    current={'stage':'diagonals','step':step};persist(current)
    diag=[]
    for i in range(n):
     current={'stage':'diagonal','step':step,'index':i};persist(current)
     diag.append(residual(i,i)[0])
    persist({'stage':'diagonals_complete','step':step,'diagonals':diag})
    raw=F(sum(lab[i][4]*diag[i][1] for i in range(n)),iv.S)
    coords,dsq=coordinates();res_ok=raw<=threshold;coord_ok=dsq<=F(1,40000**2)
    persist({'stage':'checkpoint','pairs':len(history),'raw_residual_upper':str(raw),'coordinate_radius_squared':str(dsq),'coordinate_intervals':coords,'residual_pass':res_ok,'coordinate_pass':coord_ok,'audit':dict(audit)})
   if res_ok:return {'status':'PASS_BOTH' if coord_ok else 'RESIDUAL_PASS_COORDINATE_FAIL','pairs':len(history),'history':tuple(history),'coordinate_radius_squared':str(dsq)}
   if step==max_pairs:return {'status':'PAIR_CAP','pairs':len(history),'history':tuple(history)}
   candidates=[i for i in range(n) if i not in selected and diag[i][0]>0]
   if not candidates:return {'status':'PRECISION_STALL','pairs':len(history),'history':tuple(history)}
   i=min(candidates,key=lambda j:(-diag[j][0],j));current={'stage':'pivot_row','index':i,'step':step};persist(current)
   row=[]
   for j in range(n):
    current={'stage':'pivot_entry','index':i,'column':j,'step':step};persist(current)
    row.append(residual(i,j))
   persist({'stage':'pivot_row_complete','step':step,'index':i,'row':row})
   r=intersection(diag[i],row[i][0])
   if r[0]<=0:raise ValueError('pivot lost positivity')
   g=tuple(x[0] for x in row);z=tuple(x[1] for x in row);h={'index':i,'chirality':lab[i][3],'r':r,'g':g,'j':z};persist({'stage':'pivot_saved',**h});history.append(h);selected.add(i)
 except BaseException as e:persist({'stage':'FAILED','current':current,'error':repr(e),'pairs':len(history),'audit':dict(audit)});raise
