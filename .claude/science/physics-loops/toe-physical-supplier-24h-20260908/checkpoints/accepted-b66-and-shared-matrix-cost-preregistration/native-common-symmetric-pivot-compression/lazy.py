"""Exact rational reference algorithm for synthetic controls; no native entrypoint."""
from fractions import Fraction as F

def paired_steps(diagonal,row_provider,chirality,max_pairs):
 d=list(diagonal);history=[];n=len(d)
 if len(chirality)!=n or any(x not in(-1,1) for x in chirality):raise ValueError('chiral labels')
 for _ in range(max_pairs):
  if any(x<0 for x in d):raise ValueError('negative exact diagonal')
  if not any(d):break
  i=max(range(n),key=lambda k:(d[k],-k));r=d[i]
  if r<=0:raise ValueError('positive scalar required')
  g,j=[list(x) for x in row_provider(i)]
  for h in history:
   gi,ji=h['g'][i],h['j'][i];old=h['r']
   g=[x-(gi*a+ji*b)/old for x,a,b in zip(g,h['g'],h['j'])]
   j=[x-(gi*b-ji*a)/old for x,a,b in zip(j,h['g'],h['j'])]
  if g[i]!=r or j[i]!=0:raise ValueError('residual diagonal consistency')
  for k in range(n):
   if (chirality[k]!=chirality[i] and g[k]) or (chirality[k]==chirality[i] and j[k]):raise ValueError('symmetry consistency')
  h={'i':i,'eta':chirality[i],'r':r,'g':g,'j':j};history.append(h)
  d=[x-(a*a+b*b)/r for x,a,b in zip(d,g,j)]
  h['diagonal_after']=d[:];h['trace_after']=sum(d,F(0))
 return history,d

def run_native(*args,**kwargs):
 raise RuntimeError('Disabled: no native interval Gram, pivot contract, runtime or resource binding')
