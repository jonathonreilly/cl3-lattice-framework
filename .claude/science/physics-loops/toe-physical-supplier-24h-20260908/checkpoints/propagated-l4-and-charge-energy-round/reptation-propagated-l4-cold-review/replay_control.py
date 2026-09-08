import sys,pathlib,importlib.util,itertools,json
sys.dont_write_bytecode=True
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-propagated-l4/analyze.py');s=importlib.util.spec_from_file_location('a',p);a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
count=0
for n in (2,4,8):
 for tape in itertools.product((False,True),repeat=10):
  for burn in (0,3,7):
   tags=list(range(n+1));d=1;u=lo=hi=0;run=0;runs=[];tagged=0;escape=None;bt=None;rej=0
   for j,ok in enumerate(tape,1):
    if ok:
     tags=tags[1:]+[None] if d==1 else [None]+tags[:-1];u+=d;lo=min(lo,u);hi=max(hi,u);run+=1
    else:runs.append(run);run=0;d=-d
    inside=tags[n//2] is not None
    if not inside and escape is None:escape=j
    if j==burn:bt=sum(x is not None for x in tags)
    if j>burn:tagged+=inside;rej+=not ok
   expected=dict(tagged_measurements=tagged,fraction=tagged/(10-burn),burn_end_tags=bt,final_tags=sum(x is not None for x in tags),first_escape=escape,u=u,lo=lo,hi=hi)
   got,r=a.replay(n,runs,run,burn,10-burn)
   if got!=expected or r!=rej:raise RuntimeError((n,tape,burn,got,expected))
   count+=1
pathlib.Path(__file__).with_name('REPLAY_CONTROL.json').write_text(json.dumps({'literal_histories':count,'PASS':True})+'\n');print(count)
