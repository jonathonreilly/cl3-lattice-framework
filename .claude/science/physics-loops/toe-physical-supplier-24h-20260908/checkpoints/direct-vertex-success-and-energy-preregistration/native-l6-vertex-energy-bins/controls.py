from pathlib import Path
import runpy,json
from fractions import Fraction as F
p=Path(__file__).parent;c=runpy.run_path(str(p/'core.py'));checks=0
# Single occupations in each sector, including omitted top-bit one-particle state.
for bits,expected in [(1,(1,0,0,0)),(1<<6,(0,1,0,0)),(1<<12,(0,0,1,0)),(1<<20,(0,0,0,1)),(7,(3,0,0,0))]:
 if c['counts'](bits&((1<<20)-1))!=expected:raise ValueError('sector')
 checks+=1
# Pure integer-frequency one/three-particle eigenstates give exact spectral targets.
for k in [1,3]:
 bins={(0,0,k,0):c['square'](0.5)};r=c['summarize'](bins,F(0));interval=list(map(F,r['total']['stored_susceptibility_interval']))
 if interval!=[F(1,24*k)]*2:raise ValueError('direct spectral')
 checks+=1
mutations={'wrong_energy':("+6*e",'+3*e'),'wrong_top_parity':('top=1^','top=0^')}
failed=[]
for name,(a,b) in mutations.items():
 s=(p/'core.py').read_text();assert a in s;s=s.replace(a,b);(p/(name+'.py')).write_text(s);ns={};exec(compile(s,name,'exec'),ns)
 try:
  if name=='wrong_energy':
   z=ns['summarize']({(0,0,1,0):ns['square'](0.5)},F(0));assert list(map(F,z['total']['stored_susceptibility_interval']))==[F(1,24)]*2
  else:assert ns['counts'](0)==(0,0,0,1)
 except AssertionError:failed.append(name)
 else:raise ValueError('surviving mutant')
print(json.dumps({'status':'PASS','predicates':checks,'actual_semantic_mutants_failed':failed,'full_scans':0}))
