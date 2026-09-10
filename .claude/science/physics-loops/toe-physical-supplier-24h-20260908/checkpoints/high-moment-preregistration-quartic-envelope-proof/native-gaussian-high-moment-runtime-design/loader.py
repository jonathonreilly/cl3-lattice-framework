"""Disabled binding schema and pure exact conversion/extraction helpers."""
from fractions import Fraction as F
import json,hashlib,math
from pathlib import Path
S=1<<256
class Refused(ValueError):pass
def need(x,m):
 if not x:raise Refused(m)
def rational(x):
 need(type(x)is str and len(x)<=20000,'rational token');v=F(x);need(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=32768,'canonical32768bits');return v
def interval(x):
 need(type(x)is list and len(x)==2,'interval');a,b=map(rational,x);need(a<=b,'interval order');return a,b
def dyadic(x):
 a,b=interval(x);lo=a.numerator*S//a.denominator;hi=-((-b.numerator*S)//b.denominator);need(max(abs(lo).bit_length(),abs(hi).bit_length())<=4096,'stored grid cap');return [[lo,hi],[0,0]]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def timing(x,cap):need(type(x)in(int,float)and math.isfinite(x)and 0<x<cap,'finite capped time')
def memory(x):need(type(x)is int and 0<x<=384*1048576,'literal RSS')
def receipt_family(objects,pins,expected):
 a,w,r,rf=objects['acceptance'],objects['worker'],objects['receipt'],objects['root_freeze']
 need(a['status']==expected['accepted_status']and a['once']is True,'accepted status');need(a['result_sha256']==pins['result']==w['result_sha256'],'result identity');need(a['worker_freeze']==pins['worker_freeze']==w['runtime_sha256']==r['worker_freeze']==rf['worker_freeze'],'worker identity');need(a['root_freeze']==pins['root_freeze'],'root identity');need(w['status']==expected['worker_status'],'worker complete');need(r['pass']is True and r['failure']is None and type(r['returncode'])is int and r['returncode']==0,'receipt completion')
 for x,cap in [(w['seconds'],expected['worker_seconds']),(r['seconds'],expected['root_seconds']),(a['external_seconds'],expected['external_seconds'])]:timing(x,cap)
 need(w['seconds']<=r['seconds']<=a['external_seconds'],'time ordering')
 for x in [w['rss_bytes'],r['sampled_whole_tree_peak'],a['sampled_whole_tree_peak'],a['external_rss_bytes']]:memory(x)
 need(r['sampled_whole_tree_peak']==a['sampled_whole_tree_peak'],'tree receipt relation')
def lower_moments(events):
 need(type(events)is list and len(events)==255,'fixed original event count')
 for i,e in enumerate(events,1):need(type(e['sequence'])is int and e['sequence']==i,'original sequence')
 out={}
 for kind in ['P','O']:
  modes=[];originals=[]
  for mode in ['residual','variational']:
   rows=[e['data']for e in events if e['stage']=='vacuum_moment_raw'and e['choice']==mode and e['data'].get('kind')==kind];need(len(rows)==7,'seven originals');m={};originals.append(rows)
   for j,row in enumerate(rows):
    need(type(row['index'])is int and row['index']==j,'moment index');im=interval(row['imaginary']);need(im[0]<=0<=im[1],'real moment');m[str(j)]=dyadic(row['real'])
   need(interval(rows[0]['real'])==(F(1),F(1))and m['0']==[[S,S],[0,0]],'m0 exact1');modes.append(m)
  need(originals[0]==originals[1]and modes[0]==modes[1],'same original vacuum moments');out[kind]=modes[0]
 return out
def load(binding_path):
 # No path is read until the entire future binding has been independently completed.
 raise Refused('NOT_READY: accepted omega79 receipt and full transitive source binding absent')

def load_packet(binding,emit):
 import adapter
 def read(role,which):
  spec=binding[which]['files'][role];emit('before_input',{'family':which,'role':role});need(sha(spec['path'])==spec['sha256'],'bound input hash');return json.loads(Path(spec['path']).read_text())
 families={}
 for which in ['degree20','omega79']:
  spec=binding[which];o={k:read(k,which)for k in ['acceptance','worker','receipt','root_freeze','result']};receipt_family(o,{'result':spec['files']['result']['sha256'],'worker_freeze':spec['worker_freeze'],'root_freeze':spec['files']['root_freeze']['sha256']},spec['expected']);need(o['result']['status']==spec['expected']['result_status'],'result status');families[which]=o
 spec=binding['degree20']['files']['events'];emit('before_input',{'family':'degree20','role':'events'});need(sha(spec['path'])==spec['sha256'],'original events hash');ev=[json.loads(line)for line in Path(spec['path']).read_text().splitlines()]
 # Exact original255-event chronology without original moment arithmetic.
 from itertools import combinations
 labels=list(combinations(range(6),2));kind=lambda a:'O'if a[0]//2==a[1]//2 else'P'
 local=['vacuum_inputs']+['vacuum_moment_raw']*7+['first_polynomial','source_inputs']+['source_moment_raw']*3+['residual_raw'];stages=local*2;seen=set()
 for C in labels:
  for A in labels:
   if set(C)&set(A):continue
   kc,ka=kind(C),kind(A);ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag='PP'+str(ell)if kc==ka=='P'else kc+ka
   if tag not in seen:stages.append('cross_wick_raw');seen.add(tag)
   stages.append('ordered_word')
 stages.append('gate_inputs');schedule=[('binding',None),('scalar_inputs',None)]
 for mode in ['residual','variational']:schedule += [('choice_start',mode)]+[(x,mode)for x in stages]+[('choice_complete',mode)]
 schedule.append(('complete',None));need([(e['stage'],e['choice'])for e in ev]==schedule,'original exact chronology');low=lower_moments(ev)
 scalars=[e['data']for e in ev if e['stage']=='scalar_inputs'and e['choice']is None];need(len(scalars)==1,'unique scalar source');scalars=scalars[0]
 omega=families['omega79']['result'];need(type(omega['rows'])is list and len(omega['rows'])==2,'two omega rows');odd={}
 for name,row,target in zip(['omega7','omega9'],omega['rows'],['1/10000000000000000000000','1/100000000000000000000']):
  need(rational(row['target'])==F(target),'original target identity');need(row['observable']==name and row['status']=='CERTIFIED_TARGET'and row['middle_width_gate']is True and row['weighted_power_gate']is True,'accepted omega target');a,b=interval(row['interval']);need(rational(row['width'])==b-a and b-a<=F(target),'exact omega width');odd[name]=row['interval']
 reused=read('reused','omega79');need(set(reused)==set(map(str,range(44))),'reused moment keys');M={'0':['1','1'],'2':['6','6'],'4':['42','42']}
 for absolute,dispersion in [(6,3),(8,4),(10,5)]:
  v=rational(reused[str(dispersion)]);need(v.denominator==1 and v>0,'inherited even integer');M[str(absolute)]=[str(v),str(v)]
 a,b=interval(scalars['c']);M['1']=[str(3*a),str(3*b)];M['3']=scalars['nu'];M['5']=scalars['omega5'];M['7']=odd['omega7'];M['9']=odd['omega9'];emit('absolute_moment_source_map',{'rational':M,'old_even_indices':{'6':3,'8':4,'10':5}})
 absolute={k:dyadic(v)for k,v in M.items()};emit('absolute_moment_grid',{'grid_bits':256,'moments':absolute})
 packet={'first_order':7,'grid_bits':256,'units':'dimensionless_h1','classes':{}}
 for k in ['P','O']:
  D,B=adapter.tables(absolute,k);packet['classes'][k]={'D':D,'B':B,'accepted_m':low[k]};emit('native_table',{'kind':k,'D':D,'B':B,'accepted_m':low[k]})
 return packet
