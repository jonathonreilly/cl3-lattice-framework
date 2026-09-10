from pathlib import Path
import sys,json,copy,importlib.util
from fractions import Fraction as F
P=Path('/private/tmp/toe-24h-probes-20260908/native-coarse-witness-continuation-design');sys.path.insert(0,str(P))
import adapter,prefix,triples
from interval import const
oldpath=P.with_name('native-coarse-occupied-witness-runtime-design')/'adapter.py'
spec=importlib.util.spec_from_file_location('original_adapter',oldpath);oldadapter=importlib.util.module_from_spec(spec);spec.loader.exec_module(oldadapter)
n=0
sources=[[1,0,0,0,0,0,0],[0,1,-1,0,0,0,0],[0,0,0,1,0,-1,0]]
bank=[{'s':F(2),'A':const(F(1,5)),'B':const(F(2,7)),'alpha':const(4)}]*66
for gamma in (0,1):
 for i in range(9):
  label=(i if i<6 else 390+i,gamma)
  a=adapter.raw_local(label,sources,bank,const(3),const(5));b=oldadapter.raw_local(label,sources,bank,const(3),const(5))
  for x,y in zip(a,b):assert max(x[0],y[0])<=min(x[1],y[1]);n+=1
  for sigma in(-1,1):
   x=adapter.new_raw_cross(F(3),sigma,sources[1],label,sources,bank,const(F(1,11)),const(F(2,13)),const(3))
   y=oldadapter.new_raw_cross(F(3),sigma,sources[1],label,sources,bank,const(F(1,11)),const(F(2,13)),const(3))
   assert max(x[0],y[0])<=min(x[1],y[1]);n+=1
# Literal dense exact coefficient identities, separately from interval endpoint overlap.
for sigma in(-1,1):
 C,L=triples.coefficients(F(3),sigma,const(F(1,11)),const(F(2,13)))
 M,N=oldadapter.pole(F(3),sigma,const(F(1,11)),const(F(2,13)))
 for x in sources:
  for y in sources:
   for coef,mat in((C,M),(L,N)):
    a=triples.contract(coef,triples.dots(tuple(x),tuple(y)));b=oldadapter.dot(x,mat,y)
    assert max(a[0],b[0])<=min(a[1],b[1]);n+=1
z=lambda a,b:[[['0','0']for _ in range(b)]for _ in range(a)]
events=[];plan={'files':{'T_'+str(i):{'sha256':str(i)*64}for i in range(5)}}
def put(stage,case,data):events.append({'current':{'stage':stage,'case':case},'data':data})
for i in range(5):put('mapped_T',0,{'orbit':i,'source_sha256':str(i)*64,'mapped':z(48,48),'operator_squared_upper':'1'})
cases=[]
for ci in range(4):
 put('factorization',ci,{'local':z(7,48),'projector_columns':z(48,7)})
 for k in range(21,379 if ci<3 else 211,21):put('witness_panel',ci,{'completed':k,'direct':z(7,7),'mixed':z(7,7)})
 if ci<3:
  put('witness_block',ci,{'block':z(7,7)});cases.append({'squared_block_lower':'0','excludes_tau_1e9':False,'status':'INDETERMINATE_COARSE_WITNESS','stored_operator':'minus_i_times_positive_projector_difference','metric_and_tail_charged':True,'orbit':ci//2,'impurity':ci%2+1})
a=prefix.grammar(events,cases,plan,lambda *_:None);assert len(a[0])==5 and len(events)==76;n+=1
for mutation in range(6):
 e=copy.deepcopy(events);c=copy.deepcopy(cases)
 if mutation==0:e.pop()
 if mutation==1:e[-1]['data']['completed']=209
 if mutation==2:e[0]['data']['orbit']=False
 if mutation==3:c[0]['excludes_tau_1e9']=0
 if mutation==4:e[-1]['data']['direct'][0][0]=['1','0']
 if mutation==5:e[0]['data']['source_sha256']='f'*64
 try:prefix.grammar(e,c,plan,lambda *_:None)
 except ValueError:n+=1
 else:raise AssertionError('adverse accepted '+str(mutation))
print(json.dumps({'status':'PASS','predicates':n,'actual_saved_prefix_reads':0,'native_nodes':0,'scope':'synthetic algebra interval-overlap and full76-event grammar; no native truth by these tests'}))
