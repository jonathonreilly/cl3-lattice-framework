import ast,itertools,json
from pathlib import Path
p=Path(__file__).parents[1]/"current/scripts/frontier_cycle891_complement_mechanism_2026_07_28.py"
t=ast.parse(p.read_text()); keep={"law_longest_good_run"}; ns={}
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef) and n.name in keep],type_ignores=[]),str(p),"exec"),ns)
count=0
for N in range(1,9):
 for bits in itertools.product((0,1),repeat=N):
  W={i for i,b in enumerate(bits) if b}
  for P in range(N):
   truth=0
   for start in range(N):
    length=0
    for k in range(N):
     if bits[(start+k)%N]!=bits[(start+k+P)%N]:break
     length+=1
    truth=max(truth,length)
   got=ns["law_longest_good_run"](N,W,P)
   assert got==truth,(N,bits,P,got,truth)
   count+=1
print(json.dumps({"exhaustive_cells":count,"mismatches":0,"domain":"all binary cyclic words N=1..8, P=0..N-1; run capped at N"}))
