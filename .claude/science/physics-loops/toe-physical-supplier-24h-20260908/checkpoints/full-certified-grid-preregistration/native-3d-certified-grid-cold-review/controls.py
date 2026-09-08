from pathlib import Path
import runpy,json,copy
from fractions import Fraction as F
from independent import *
B=Path(__file__).parent.parent/'native-3d-certified-grid-design';certify=runpy.run_path(str(B/'exact_certificate.py'))['certificate'];count=0
A=[[0j]*16 for _ in range(16)];Q=[[0j]*16 for _ in range(16)]
for i in range(16):A[i][i]=i;Q[i][i]=1
Q[0][0]=1+2**-20;Q[1][1]=1j
for values in (list(range(16)),[i+.25 for i in range(16)]):
 c=certify(A,Q,values,F(1,1<<40));verify(A,Q,values,F(1,1<<40),c);count+=1
 # A changed claimed input radius must fail independent replay.
 bad=copy.deepcopy(c);bad['input_radius']='0'
 try:verify(A,Q,values,F(1,1<<40),bad)
 except ValueError:count+=1
 else:raise ValueError('radius mutant')
 bad=copy.deepcopy(c);bad['root_intervals'][0]=['0','0']
 try:verify(A,Q,values,F(1,1<<40),bad)
 except ValueError:count+=1
 else:raise ValueError('interval mutant')
Q[0][0]=0
try:certify(A,Q,list(range(16)),0)
except ValueError as e:ck('Gram' in str(e),'actual badGram');count+=1
else:raise ValueError('badGram survived')
# Actual core input-radius omission mutant: intentional semantic change, not hash gate.
s=(B/'exact_certificate.py').read_text();s=s.replace('radius=input_radius+2*r+4*L*eta','radius=2*r+4*L*eta');ns={};exec(compile(s,'actual_radius_mutant','exec'),ns);Q[0][0]=1
c=ns['certificate'](A,Q,list(range(16)),F(1,10))
try:verify(A,Q,list(range(16)),F(1,10),c)
except ValueError:count+=1
else:raise ValueError('actual radius omission survived')
print(json.dumps({'controls':count,'scope':'synthetic complex nonorthogonal/zero/incorrect eigenvalue, bad Gram and actual omitted radius; no physical spectra'}))
