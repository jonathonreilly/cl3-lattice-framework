import json,copy
from literal import *
z={'L':4,'V':'19/20','T':(.5).hex(),'initial':hex(SEED),'events':[],'witness':[]}
a=measure(z);require(a['mid_NF']==96,'seed nf');require(a['time_average_NF']==96,'integral');require(a['endpoint_overlap']==1,'overlap');require(a['physical_event_count']==0,'count')
# One legal event: independent closed-form average/endpoints.
p=next(p for p in range(192) if legal(SEED,p));w=copy.deepcopy(z);w['events']=[[(.125).hex(),p]];b=measure(w);end=SEED^MASK[p]
require(abs(b['time_average_NF']-(nf(SEED)/4+3*nf(end)/4))<1e-12,'one event integral');require(b['endpoint_overlap']==1-8/192,'four edge overlap')
count=6
for key,value in [('initial','0x0'),('V','1'),('T',(0.).hex()),('events',[[(0.).hex(),p]]),('events',[[(.1).hex(),p],[(.1).hex(),p]])]:
 t=copy.deepcopy(z);t[key]=value
 try:measure(t)
 except ValueError:count+=1
 else:raise ValueError('malformed survived')
print(json.dumps({'predicates':count,'sampling':False}))
