"""Pure per-orbit API. Prospective dispatcher/binding deliberately absent."""
from fractions import Fraction as F
from checker import reconstruct,certificate,require,BoundExceeded

def canonical(x):
 if isinstance(x,dict):return {k:canonical(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [canonical(v)for v in x]
 if isinstance(x,str):return F(x)
 return x

def check(ids,events,t,claimed,persist):
 persist('before_selected_entries',{})
 raw=[e['data']for e in events if e['stage']=='selected_entry']
 c,r,labels,embedding=reconstruct(ids,raw)
 grams=[e['data']for e in events if e['stage']=='selected_gram'];require(len(grams)==1,'one Gram')
 require(canonical(grams[0])==canonical(dict(center=c,radii=r,labels=labels,E=embedding)),'reconstructed paired Gram/embedding')
 persist('selected_reconstruction',dict(entries=300,support=len(labels)))
 if claimed['status']=='INDETERMINATE_LIMIT_OR_CANDIDATE':
  # A retained failure is not promoted to a mathematical certificate.
  require(claimed['failure_kind']in ('Limit','CandidateFailure'),'named failure')
  persist('retained_indeterminate',dict(status=claimed['status']))
  return {'status':'SAVED_INDETERMINATE_ONLY','certificate_replayed':False}
 require(t is not None,'candidate required')
 t=[[F(x)for x in row]for row in t]
 def compare(stage,data):
  persist('before_'+stage,{})
  saved=[e['data']for e in events if e['stage']==stage];require(len(saved)==1,'one '+stage)
  require(canonical(saved[0])==canonical(data),'independent '+stage)
  persist('verified_'+stage,{})
 ans=certificate(c,r,t,embedding,compare)
 require(canonical(ans)==canonical(claimed),'final certificate/flags')
 return {'status':'PASS_SAVED_MATRIX_CERTIFICATE','certificate_replayed':True}
