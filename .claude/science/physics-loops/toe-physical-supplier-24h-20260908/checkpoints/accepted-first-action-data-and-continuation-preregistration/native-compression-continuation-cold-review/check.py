import pathlib,types,sys,copy,json,hashlib
p=pathlib.Path(__file__).resolve().parent;s=p.parent/'native-fixed192-compression-continuation-design'
for name in ('interval','pivot'):
 m=types.ModuleType(name);exec(compile((s/(name+'.py')).read_bytes(),str(s/(name+'.py')),'exec'),m.__dict__);sys.modules[name]=m
iv=sys.modules['interval'];pv=sys.modules['pivot'];S=iv.S
seeds=[[int(i==j) for j in range(6)] for i in range(4)]+[[1,0,0,0,2,0],[0,1,0,0,1,3]]
dot=lambda x,y:sum(a*b for a,b in zip(x,y));lab=tuple(('pole',i,0,1,2) for i in range(6))
h=[{'index':i,'chirality':1,'r':[S,S],'g':[[dot(seeds[i],v)*S]*2 for v in seeds],'j':[[0,0] for _ in seeds]} for i in range(4)]
cp={'pairs':4,'diagonals':[[0,0]]*4+[[4*S,4*S],[10*S,10*S]],'raw_residual_upper':'28','coordinate_radius_squared':'0','residual_pass':False,'coordinate_pass':True}
queries=[];events=[];coords=[]
def entry(i,j):queries.append((i,j));v=dot(seeds[i],seeds[j])*S;return(v,v),(0,0)
old=pv.coordinate
pv.coordinate=lambda x,r:(coords.append(1) or old(x,r))
res=pv.run(entry,lab,events.append,native=False,max_pairs=6,resume=h,initial_checkpoint=cp)
checks=0
def req(x):
 global checks
 if not x:raise ValueError(checks)
 checks+=1
req(res['status']=='PASS_BOTH');req([x['index'] for x in events if x['stage']=='pivot_saved']==[5,4]);req(queries==[(5,j) for j in range(6)]+[(i,i) for i in range(6)]+[(4,j) for j in range(6)]+[(i,i) for i in range(6)]);req(len(coords)==132);req(events[0]['stage']=='restored_checkpoint');req([e['step'] for e in events if e['stage']=='diagonals']==[5,6])
for badtype in range(5):
 hh=copy.deepcopy(h);cc=copy.deepcopy(cp)
 if badtype==0:hh[0]['r']=[0,S]
 elif badtype==1:hh[0]['g'].pop()
 elif badtype==2:cc['diagonals'][0]=[S,S]
 elif badtype==3:cc['raw_residual_upper']='29'
 else:cc['coordinate_pass']=False
 before=len(queries)
 try:pv.run(entry,lab,events.append,native=False,max_pairs=6,resume=hh,initial_checkpoint=cc)
 except ValueError:req(len(queries)==before)
 else:raise ValueError('malformed accepted')
req(5*399*16==31920);req(399*5*(sum(range(4,12))+sum(range(5,13)))==255360);req(5*399*2*sum(range(5,13))==271320);req(31920+6*40+5==32165)
(p/'RESULT.json').write_text(json.dumps({'status':'PASS_TINY_NONORTHOGONAL_CONTINUATION','predicates':checks,'entry_calls':len(queries),'coordinate_calls':len(coords),'native_history_loads':0},indent=2)+'\n');print(checks)
