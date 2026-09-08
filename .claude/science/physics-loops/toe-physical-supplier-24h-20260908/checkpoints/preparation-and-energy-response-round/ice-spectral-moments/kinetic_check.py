import contextlib,io,runpy,json
from pathlib import Path
p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p/'check.py'))
import numpy as np
from scipy import sparse
from scipy.linalg import eigh
r=np.array(d['rows']);c=np.array(d['cols']);f=np.array(d['faceids']);m=f<8
Axy=sparse.coo_matrix((np.ones(sum(m)),(r[m],c[m])),shape=(864,864)).toarray();psi=d['psi'];kin=float(psi@Axy@psi);S=d['Zd']/32
mu=.25*kin/S;h=1e-4;H=d['H'];energy=lambda z:float(eigh(z,subset_by_index=[0,0],eigvals_only=True)[0]);fd=(energy(H-h*Axy)-energy(H+h*Axy))/(2*h)
assert abs(mu-d['correct1'])<1e-12
assert abs(fd+kin)<1e-6
print(json.dumps({'kinetic_plane_expectation':kin,'moment_from_kinetic':mu,'finite_difference':fd,'Hellmann_Feynman_residual':abs(fd+kin),'h':h,'checks':2},indent=2))
