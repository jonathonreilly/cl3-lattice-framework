"""Five abstract orthogonal real seeds; four restored, one NEW pair only."""
import pivot,interval as iv,json,copy
lab=tuple(('pole',i,0,1,2) for i in range(5));one=iv.ONE;zero=iv.ZERO
history=[{'index':i,'chirality':1,'r':one,'g':[one if i==j else zero for j in range(5)],'j':[zero]*5} for i in range(4)]
original=copy.deepcopy(history)
cp={'pairs':4,'diagonals':[zero]*4+[one],'raw_residual_upper':'2','coordinate_radius_squared':'0','residual_pass':False,'coordinate_pass':True}
requests=[];events=[];coordinates=[]
def entry(i,j):requests.append((i,j));return (one if i==j else zero),zero
old=pivot.coordinate
def coord(x,r):coordinates.append((x,r));return old(x,r)
pivot.coordinate=coord
r=pivot.run(entry,lab,events.append,native=False,max_pairs=5,resume=history,initial_checkpoint=cp)
checks=0
def req(x):
 global checks
 if not x:raise ValueError('check '+str(checks))
 checks+=1
req(r['status']=='PASS_BOTH' and r['pairs']==5)
req(requests==[(4,j) for j in range(5)]+[(i,i) for i in range(5)])
req(len(coordinates)==50) # only terminal5-pair coordinates, not initial4 pass
req(history==original)
req([e['step'] for e in events if e['stage']=='diagonals']==[5])
req([e['index'] for e in events if e['stage']=='pivot_saved']==[4])
for field,value in [('pairs',3),('raw_residual_upper','3'),('residual_pass',True)]:
 bad=dict(cp);bad[field]=value;before=len(requests)
 try:pivot.run(entry,lab,events.append,native=False,max_pairs=5,resume=history,initial_checkpoint=bad)
 except ValueError:req(len(requests)==before)
 else:req(False)
print(json.dumps({'status':'PASS_TINY_CONTINUATION','checks':checks,'new_entry_requests':requests,'coordinate_calls':len(coordinates),'native_calls':0,'actual_history_loaded':False}))
