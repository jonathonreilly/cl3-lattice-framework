from pathlib import Path
import sys,json
b=Path('/private/tmp/toe-24h-probes-20260908');sys.path.insert(0,str(b/'native-coordinate-free-root-review'));import retention
s=(b/'native-coordinate-free-runtime-cold-review/retention_controls.py').read_text();s=s[:s.index('with tempfile.TemporaryDirectory()')];d={};exec(compile(s,'synthetic-definitions','exec'),d)
e,a=d['make'](0);new=[];skip=False
for st,v in e:
 if st=='action_columns':skip=False
 if st=='frame_residual':
  v['data']['e']='1';new.append((st,v));skip=True
 elif not skip:new.append((st,v))
a['results']=[{'status':'INDETERMINATE_FRAME','e':'1','terms':0}for _ in range(2)]
new=[(st,json.loads(json.dumps(v)))for st,v in new]
def req(x,m):
 if not x:raise ValueError(m)
retention.validate(new,a,0,req);n=1
# Missing second impurity action cannot be accepted as complete.
bad=[x for x in new if not(x[0]=='action_columns'and x[1]['impurity']==400)]
try:retention.validate(bad,a,0,req)
except ValueError:n+=1
else:raise AssertionError('missing branch accepted')
print(json.dumps({'synthetic_frame_branch_checks':n,'native_calls':0}))
