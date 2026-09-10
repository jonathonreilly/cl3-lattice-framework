"""Independent exact coefficient/event reconciliation; no producer arithmetic imports."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,math

def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def q(x):
 need(type(x)is str and len(x)<=40000 and re.fullmatch(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?',x)is not None,'rational encoding');v=F(x);need(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=50000,'canonical bits');return v
def box(x):
 need(type(x)is list and len(x)==2,'box shape');a,b=map(q,x);need(a<=b,'box order');return a,b
def matrix(x,n):need(type(x)is list and len(x)==n and all(type(r)is list and len(r)==n for r in x),'matrix shape');return [list(map(q,r))for r in x]
def timing(x):need(type(x)in(int,float) and math.isfinite(x)and 0<x<119,'worker timing')
def atan(q0,n):
 s=sum((F((-1)**k,(2*k+1)*q0**(2*k+1))for k in range(n)),F(0));r=F((-1)**n,(2*n+1)*q0**(2*n+1));return min(s,s+r),max(s,s+r)
def pi_box():
 a,b=atan(5,40),atan(239,12);return F(1)/(16*a[1]-4*b[0]),F(1)/(16*a[0]-4*b[1])
def rounded(v):
 z=v*2**84;return F((2*z.numerator+z.denominator)//(2*z.denominator),2**84)
def check(out,root,elapsed,progress):
 out=Path(out);need({x.name for x in out.iterdir()}=={'EVENTS.ndjson','STARTED.json','PARTIAL.json','RESULT.json','WORKER_COMPLETE.json'},'exact outputs')
 bindpath=Path(root['binding_path']);need(sha(bindpath)==root['binding_sha256'],'binding pin');binding=json.loads(bindpath.read_text());identity=binding['identity'];source=Path(binding['output'])
 # All actual source bytes are checked by the monitor against scientific pins.
 nodes=json.loads((source/'NODES.json').read_text())['rows'];need(len(nodes)==378,'source nodes')
 result=json.loads((out/'RESULT.json').read_text());complete=json.loads((out/'WORKER_COMPLETE.json').read_text());partial=json.loads((out/'PARTIAL.json').read_text())
 need(json.loads((out/'STARTED.json').read_text())=={'freeze_sha256':root['worker_freeze'],'output':str(out.resolve()),'once':True},'STARTED authorization')
 seq=0;blocks=0
 with (out/'EVENTS.ndjson').open() as stream:
  def take(stage):
   nonlocal seq
   line=stream.readline();need(bool(line),'missing event');e=json.loads(line);need(type(e['seq'])is int and e['seq']==seq and e['stage']==stage,'event order');seq+=1;return e['payload']
  start=take('start');need(start=={'scope':'NEW_A_ONLY_PHYSICAL_COLUMN_COEFFICIENTS','acquisition_binding':identity},'start binding')
  for i,n in enumerate(nodes):need(take('input_row_before_check')=={'id':i,'node':n},'original input copy')
  loaded=take('accepted_inputs_loaded');need(loaded=={'count':378,'acquisition_result_sha256':sha(source/'RESULT.json')},'accepted inputs')
  pi=take('reciprocal_pi');pb=pi_box();need(box(pi['interval'])==pb and pi['terms']==[40,12],'independent Machin');pm=sum(pb)/2
  ea=rs=rw=et=F(0);totalw=F(0)
  for i,n in enumerate(nodes):
   orig=box(n['weight_interval']);grid=2**192;wl=F((orig[0]*grid).__floor__(),grid);wh=F((orig[1]*grid).__ceil__(),grid)
   rec=take('weight_recentered');need(type(rec['index'])is int and rec['index']==i and box(rec['original'])==orig and box(rec['rounded'])==(wl,wh),'weight recenter')
   need(wl<=orig[0]<=orig[1]<=wh and wl>0,'weight containment');sl,sh=box(n['s_interval']);s=(sl+sh)/2;w=(wl+wh)/2
   raw=json.loads((source/f'RAW_{i:03d}.json').read_text())['raw'];ab=box(raw['A']);need(q(raw['s'])==s,'raw A argument');al,ah=ab
   row=take('node_start');need(type(row['index'])is int and row['index']==i,'node index');row=row['row'];need(type(row['id'])is int and row['id']==i and box(row['root'])==(sl,sh) and box(row['weight'])==orig and box(row['A'])==ab,'node exact source')
   need(F(1,2**32)<=sl<=sh<=16 and ah-al<=F(1,10**30),'input range');A=(max(F(0),al)+min(1/(s*s),ah))/2;need(max(F(0),al)<=min(1/(s*s),ah),'spectral intersection')
   D=(1-s*s*A)/6;a=1-4*D
   ea=max(ea,(ah-al)/2);rs=max(rs,(sh-sl)/2);rw=max(rw,(wh-wl)/2);totalw+=w
   for kind in('P','O'):
    B=A if kind=='P' else D;det=a*a+8*s*s*A*B;need(det>=F(1,9),'positive determinant')
    inp=take('coefficient_inputs');expected={'s':s,'A':A,'D':D,'Bgeo':B,'a':a,'determinant':det};need(inp['kind']==kind and box(inp['A_box'])==ab and all(q(inp[k])==v for k,v in expected.items()),'coefficient input')
    exact=[[-8*s*B/det,2*a/det],[-2*a/det,-4*s*A/det]];approx=[[rounded(v)for v in row]for row in exact];err=2*max(abs(exact[j][k]-approx[j][k])for j in range(2)for k in range(2))
    retained=take('coefficient_exact_and_rounded');need(matrix(retained['Q'],2)==exact and matrix(retained['Qhat'],2)==approx and q(retained['operator_rounding'])==err and err<=F(1,2**80),'exact inverse and rounding');et=max(et,err)
    op=take('node_operator');need(type(op['index'])is int and op['index']==i and op['kind']==kind and op['columns']=='R0(+is)[e0,d], R0(-is)[e0,d]','operator descriptor')
    c=[[F(0)]*4 for _ in range(4)]
    for j in range(2):
     for k in range(2):c[j][k+2]=-w*pm*approx[j][k]/2;c[k+2][j]=-c[j][k+2]
    need(matrix(op['positive_imaginary'],4)==c,'positive coefficient block');blocks+=1
   progress({'stage':'schema_node','completed':i+1})
  ledger=take('ledger_before_gate');analytic={'low':F(2,9)*F(5439,160)/2**48+F(867,192)/2**64,'high':F(1,8)*F(9,64)**15*(1+F(18,64*33)),'quadrature':6139*F(4,25)**21}
  radii={'A':ea,'pole':rs,'weight':rw,'coefficient':et,'reciprocal_pi':(pb[1]-pb[0])/2};factors={'A':2**27,'pole':2**42,'weight':2**13,'coefficient':5,'reciprocal_pi':2**12};terms={k:radii[k]*factors[k]for k in radii};inp=sum(terms.values());total=inp+sum(analytic.values())
  for name,expected in [('analytic',analytic),('input_radii',radii),('input_terms',terms)]:need(set(ledger[name])==set(expected) and all(q(ledger[name][k])==v for k,v in expected.items()),'ledger '+name)
  need(q(ledger['input_error'])==inp and q(ledger['total_error'])==total and total<F(1,10**12) and totalw<=17 and q(ledger['midpoint_weight_sum'])==totalw,'total ledger')
  need(ledger['physical_columns_exact']is True and ledger['gram_or_consumer_certified']is False and ledger['low_columns']=='H0^-1 [e0,d]' and ledger['high_operator']=='sum coefficient*(HA^power-H0^power)','ledger scope')
  need(matrix(ledger['low_imaginary'],2)==[[F(0),-6*pm/2**32],[6*pm/2**32,F(0)]],'low sign');need(len(ledger['high'])==15,'high count')
  for n,h in enumerate(ledger['high']):need(type(h['n'])is int and h['n']==n and type(h['power'])is int and h['power']==2*n+1 and q(h['coefficient'])==pm*F((-1)**n,(2*n+1)*16**(2*n+1)),'high coefficient')
  need(take('complete')==result and not stream.read(),'complete event and EOF')
 need(seq==3407 and blocks==756 and type(result['events'])is int and result['events']==3407,'full census')
 need(result['status']=='CERTIFIED_DESCRIPTOR_OPERATOR_INPUT_BOUND' and result['scope']=='physical-column operator only; no Gram or Gaussian consumer' and result['binding']==identity and result['ledger']==ledger,'result binding')
 need(type(result['nodes'])is int and result['nodes']==378 and result['classes']==['P','O'] and type(result['coefficient_blocks'])is int and result['coefficient_blocks']==756,'result dimensions')
 need(type(result['native_oracle_calls'])is int and result['native_oracle_calls']==0 and result['physical_columns_evaluated']is False and result['gaussian_consumer_certified']is False,'scope flags');timing(result['seconds']);timing(complete['seconds']);timing(partial['seconds']);need(result['seconds']<=partial['seconds']<=complete['seconds'],'time order')
 need(partial['current']=={'stage':'complete','seq':3406} and type(partial['events'])is int and partial['events']==3407 and type(partial['coefficient_blocks'])is int and partial['coefficient_blocks']==756,'final partial')
 need(complete['status']=='COMPLETE' and complete['scope']=='NEW_A_ONLY_DESCRIPTOR_COEFFICIENTS' and complete['freeze_sha256']==root['worker_freeze'] and complete['binding']==identity,'worker binding');need(type(complete['rss_bytes'])is int and 0<complete['rss_bytes']<=384*1048576,'worker RSS')
 for field,name in [('result_sha256','RESULT.json'),('events_sha256','EVENTS.ndjson'),('partial_sha256','PARTIAL.json')]:need(complete[field]==sha(out/name),'completion hash')
 return {'status':'ACCEPTED_DESCRIPTOR_COEFFICIENT_SCHEMA','count':378,'events':3407,'coefficient_blocks':756,'result_sha256':sha(out/'RESULT.json'),'events_sha256':sha(out/'EVENTS.ndjson'),'total_error':str(total),'independent_coefficient_reconciliation':True,'native_oracle_replay':False,'gaussian_consumer_certified':False,'seconds_before_schema':elapsed}
