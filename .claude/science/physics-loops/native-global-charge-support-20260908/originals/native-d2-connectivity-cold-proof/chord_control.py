import pathlib,json
checks=0
for n in range(4,22,2):
 C={(i,(i+1)%n) for i in range(n)}
 for u in range(n):
  for gap in range(3,n-1,2):
   v=(u+gap)%n
   for forward in (True,False):
    a,b=(u,v) if forward else (v,u);arcs=[]
    for x,y in ((a,b),(b,a)):
     arc=[];j=x
     while j!=y:arc.append((j,(j+1)%n));j=(j+1)%n
     arcs.append(arc)
    P,Q=arcs;state=C|{(a,b)}
    for cycle in ([(a,b)]+Q,P+[(b,a)]):
     if len(cycle)>=n or not all(e in state for e in cycle):raise RuntimeError('directed shorter')
     for x,y in cycle:state.remove((x,y));state.add((y,x))
    if state!={(y,x) for x,y in C}|{(a,b)}:raise RuntimeError('net chord identity')
    checks+=1
pathlib.Path(__file__).with_name('CHORD_RESULT.json').write_text(json.dumps({'directed_chord_cases':checks,'PASS':True,'scope':'Exact abstract chord orientation/net-edge identity; not a physical configuration census.'})+'\n');print(checks)
