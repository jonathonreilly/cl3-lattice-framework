import time
START=time.monotonic()
import sys,pathlib,json,hashlib,types,signal,resource
P=pathlib.Path(__file__).resolve().parent
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('29second synthetic cap')));signal.setitimer(signal.ITIMER_REAL,max(.001,29-(time.monotonic()-START)))
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('strict flags')
f=json.loads((P/'FREEZE.json').read_text())
for n,h in f['files'].items():
 if hashlib.sha256((P/n).read_bytes()).hexdigest()!=h:raise ValueError('source pin')
for name in ['core','worker']:
 p=P/(name+'.py');m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
out=P.parent/'native-jet-synthetic-profile-output'
with(P.parent/'native-jet-synthetic-profile.ATTEMPT').open('x')as z:z.write('synthetic once\n')
try:
 r=sys.modules['worker'].execute_authenticated(json.loads((P/'FIXTURE.json').read_text()),out)
 C=sys.modules['core'];from fractions import Fraction as F
 widths=[]
 for row,d in zip(r['rows'],[1,2]):
  for n,x in row['moments'].items():
   exact=(-d)**n
   if not x[0][0]<=exact*C.S<=x[0][1]:raise ValueError('independent exact finite moment mismatch')
   widths.append(str(F(x[0][1]-x[0][0],C.S)))
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss>384*1048576:raise MemoryError('synthetic RSS')
 (out/'PROFILE.json').write_text(json.dumps({'status':'PASS_NONNATIVE_PROFILE','seconds':time.monotonic()-START,'rss_bytes':rss,'widths':widths,'native_values':0},indent=2)+'\n')
except BaseException as e:
 if out.exists():(out/'PROFILE_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START})+'\n')
 raise
