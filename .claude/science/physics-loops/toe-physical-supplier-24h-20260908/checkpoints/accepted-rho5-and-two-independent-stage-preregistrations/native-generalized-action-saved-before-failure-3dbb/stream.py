"""Orbitwise file-stage stream. No implicit discovery, loader, or execution CLI."""
from pathlib import Path
import json,hashlib
from fractions import Fraction as F
import stages as s
import action
from replay import normalize

def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()

class SavedStages:
 def __init__(self,files,pins,persist):
  self.files=[Path(x)for x in files];self.pins=pins;self.persist=persist;self.cursor=0
  if not 0<len(files)<=4096:raise ValueError('file count')
 def read(self):
  if self.cursor>=len(self.files):raise ValueError('missing stage')
  p=self.files[self.cursor];self.persist('before_saved_parse',dict(index=self.cursor,path=str(p)))
  if not p.name.startswith(f'{self.cursor:05d}_')or p.suffix!='.json' or p.stat().st_size>32*1048576:raise ValueError('stage name/size')
  if sha(p)!=self.pins[str(p)]:raise ValueError('stage hash')
  stage=p.stem.split('_',1)[1];data=json.loads(p.read_text());self.cursor+=1
  return stage,data
 def compare(self,stage,data):
  self.persist('independent_'+stage,data)
  got,value=self.read()
  if got!=stage or normalize(value)!=normalize(data):raise ValueError('stage mismatch '+stage)
 def end(self):
  if self.cursor!=len(self.files):raise ValueError('unconsumed stages')
  for p in self.files:
   if sha(p)!=self.pins[str(p)]:raise ValueError('final stage hash')

def verify(record,poles,alpha,claimed,stream):
 if type(record.get('pairs'))is not int or record['pairs']!=24 or type(record.get('candidate_bits'))is not int or record['candidate_bits']!=256:raise ValueError('typed24/256')
 ids=record['indices'];t_int=record['T'];r,u,e=action.seeds(ids)
 stream.compare('selected_candidate',record)
 raw=sorted({a for a,g in u});table={};count=0
 for j,a in enumerate(raw):
  for b in raw[j:]:
   stream.compare('acquisition_current',dict(raw_i=a,raw_j=b,completed=count))
   st,d=stream.read()
   if st!='acquired_raw' or any(type(d[k])is not int for k in('i','j','count')):raise ValueError('inherited raw record')
   count+=1
   if (d['i'],d['j'],d['count'])!=(a,b,count):raise ValueError('acquisition census')
   g,z=s.pair(d['G']),s.pair(d['J'])
   if a==b and z!=(0,0):raise ValueError('J diagonal')
   table[a,b]=(g,z);stream.persist('authenticated_inherited_raw',dict(i=a,j=b,count=count))
 m=[]
 for a,g in u:
  row=[]
  for b,h in u:
   x,j=table[min(a,b),max(a,b)]
   if a>b:j=s.neg(j)
   row.append(x if g==h else(s.neg(j)if g else j))
  m.append(row)
 stream.compare('physical_principal',dict(U=u,M=m,raw_pairs=count))
 if len(t_int)!=48 or any(len(row)!=48 for row in t_int):raise ValueError('T shape')
 t=[[s.pair((x,x))for x in row]for row in t_int]
 def outward(x):x=F(x)*s.S;return s.pair((s.down(x),s.up(x)))
 ans=action.run(ids,t,m,[outward(x)for x in poles],[outward(x)for x in alpha],stream.compare)
 stream.persist('independent_final',ans)
 if normalize(ans)!=normalize(claimed):raise ValueError('final result')
 stream.end();return dict(status='PASS_INDEPENDENT_STREAMED_STAGES',inherited_entry_truth=True,stages=stream.cursor)
