"""Pure saved-event verifier API; durable caller/actual binding not yet supplied."""
from fractions import Fraction as F
import stages as s
import action

def normalize(x):
 if type(x)is bool:return ("BOOLEAN",x)
 if isinstance(x,dict):return {k:normalize(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [normalize(v)for v in x]
 if type(x)is str:
  try:return F(x)
  except ValueError:return x
 return x

def verify(ids,t_integer,poles,alpha,events,claimed,persist):
 # Scope: raw saved intervals are authenticated truths, never queried anew.
 if not events or events[0][0]!='selected_candidate':raise ValueError('candidate event')
 record=events[0][1]
 if record.get('indices')!=ids or record.get('T')!=t_integer or type(record.get('pairs'))is not int or record['pairs']!=24 or type(record.get('candidate_bits'))is not int or record['candidate_bits']!=256:raise ValueError('candidate binding')
 r,u,e=action.seeds(ids);raw=sorted({a for a,g in u});cursor=1;count=0;table={}
 def consume(stage,data):
  nonlocal cursor
  persist('independent_'+stage,data)
  if cursor>=len(events)or events[cursor][0]!=stage or normalize(events[cursor][1])!=normalize(data):raise ValueError('saved stage mismatch '+stage)
  cursor+=1
 for j,a in enumerate(raw):
  for b in raw[j:]:
   consume('acquisition_current',dict(raw_i=a,raw_j=b,completed=count))
   if cursor>=len(events)or events[cursor][0]!='acquired_raw':raise ValueError('missing inherited entry')
   d=events[cursor][1]
   if any(type(d[k])is not int for k in ('i','j','count')):raise ValueError('typed acquisition')
   g,z=s.pair(d['G']),s.pair(d['J'])
   if a==b and z!=(0,0):raise ValueError('exact diagonal J')
   count+=1
   consume('acquired_raw',dict(i=a,j=b,G=g,J=z,count=count));table[a,b]=(g,z)
 m=[]
 for a,g in u:
  row=[]
  for b,h in u:
   x,j=table[min(a,b),max(a,b)]
   if a>b:j=s.neg(j)
   row.append(x if g==h else(s.neg(j)if g else j))
  m.append(row)
 consume('physical_principal',dict(U=u,M=m,raw_pairs=count))
 if len(t_integer)!=48 or any(len(row)!=48 for row in t_integer):raise ValueError('T shape')
 t=[[s.pair((x,x))for x in row]for row in t_integer]
 def enclose(v):v=F(v)*s.S;return s.pair((s.down(v),s.up(v)))
 pp=[enclose(v)for v in poles];aa=[enclose(v)for v in alpha]
 try:ans=action.run(ids,t,m,pp,aa,consume)
 except s.Incomplete as exc:
  persist('checker_incomplete',{'error':repr(exc),'consumed':cursor})
  return {'status':'INCOMPLETE_INDEPENDENT_CHECK','certificate_pass':False,'consumed':cursor}
 if claimed['status']=='INDETERMINATE_CERTIFICATE':
  return {'status':'PRODUCER_REFUSAL_NOT_REPLAYED','certificate_pass':False}
 if cursor!=len(events)or normalize(ans)!=normalize(claimed):raise ValueError('final result/stage count')
 return {'status':'PASS_INDEPENDENT_STAGE_ARITHMETIC','certificate_pass':True,'entry_truth_inherited':True,'stages':cursor}
