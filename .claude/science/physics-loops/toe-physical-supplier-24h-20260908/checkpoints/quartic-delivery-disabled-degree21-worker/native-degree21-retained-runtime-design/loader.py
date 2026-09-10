"""Authenticated reuse only; no old moment supplier or trial recomputation."""
import json
from pathlib import Path
from fractions import Fraction as F
import accepted as A
import interval as I
import core,arithmetic as C

original_read=A.read
def bounded_read(spec):
 A.need(Path(spec["path"]).stat().st_size<=32*1048576,"bounded input JSON")
 return original_read(spec)
A.read=bounded_read

def stream(spec,count):
 A.need(Path(spec["path"]).stat().st_size<=32*1048576,"bounded input stream")
 A.need(A.sha(spec['path'])==spec['sha256'],'stream hash');ev=[json.loads(x)for x in Path(spec['path']).read_text().splitlines()]
 A.need(len(ev)==count and all(type(x['sequence'])is int and x['sequence']==i for i,x in enumerate(ev,1)),'stream census/order');return ev

def preflight(x):
 if isinstance(x,dict):
  if set(x)=={"path","sha256"}:A.need(Path(x["path"]).stat().st_size<=32*1048576,"input size preflight")
  else:
   for v in x.values():preflight(v)
 elif isinstance(x,list):
  for v in x:preflight(v)

def load(binding,emit):
 preflight(binding)
 qspec=binding['quartic'];qr=A.family(qspec);qb=A.read(qspec['binding']);preflight(qb);packet=A.load(qb,emit);saved=A.read(qspec['inputs']);A.need(I.encode(packet)==saved,'exact quartic input copy');qe=stream(qspec['events'],97)
 A.need(type(qr['events'])is int and qr['events']==97 and type(qr['choices'])is int and qr['choices']==2,'quartic complete')
 he=stream(binding['high_events'],189)
 # High acceptance and exact original lower family were checked by A.load.
 source=[x['data']for x in he if x['stage']=='absolute_moment_source_map'];grids=[x['data']for x in he if x['stage']=='absolute_moment_grid'];A.need(len(source)==len(grids)==1,'unique radial map')
 R=source[0]['rational'];G=grids[0]['moments'];A.need(set(R)==set(G)==set(map(str,range(11))),'radial keys');A.need(type(grids[0]['grid_bits'])is int and grids[0]['grid_bits']==256,'radial grid')
 radial={}
 for n in range(11):
  lo,hi=I.box(R[str(n)]);expected=[[lo.numerator*C.S//lo.denominator,-((-hi.numerator*C.S)//hi.denominator)],[0,0]];A.need(G[str(n)]==expected and all(type(x)is int for row in G[str(n)]for x in row),'exact radial mapping');radial[n]=tuple(tuple(x)for x in expected);core.box(radial[n])
 # Bind the radial stream to the exact high producer referenced by quartic input.
 A.need(Path(binding['high_events']['path']).parent==Path(qb['high']['files']['result']['path']).parent,'same high output directory')
 ev=stream(qb['degree20']['files']['events'],255);out={}
 for index,mode in enumerate(('residual','variational')):
  prior=qr['rows'][index];A.need(prior['mode']==mode,'quartic mode order');p={};oldq={};s={};first={}
  gate=A.select(ev,'gate_inputs',mode)
  for kind in('P','O'):
   row=packet[mode]['rows'][kind];p[kind]=row['p'];oldq[kind]=I.parse(gate['rows'][kind]['q']);raw=[x['data']for x in ev if x['stage']=='source_moment_raw'and x['choice']==mode and x['data'].get('kind')==kind];A.need(len(raw)==3 and all(type(x['index'])is int and x['index']==j for j,x in enumerate(raw)),'source0..2')
   ss=[]
   for x in raw:
    lo,hi=I.box(x['real']);im=I.box(x['imaginary']);A.need(im[0]<=0<=im[1],'real source');ss.append(((lo.numerator*C.S//lo.denominator,-((-hi.numerator*C.S)//hi.denominator)),(0,0)))
   s[kind]=ss;bound=[x['data']for x in qe if x['stage']=='class_residual_bound'and x['choice']==mode and x['data'].get('kind')==kind];A.need(len(bound)==1,'quartic first class');first[kind]=I.parse(bound[0]['first_squared_upper']);A.need(first[kind]>=0,'first nonnegative')
  out[mode]={'p':p,'old_q':oldq,'s0_s2':s,'first_squared':first,'a_squared':packet[mode]['trial_a2'],'old_alpha':I.box(prior['intersection'])}
 emit('authenticated_degree21_inputs',{'radials':radial,'modes':out});return radial,out
