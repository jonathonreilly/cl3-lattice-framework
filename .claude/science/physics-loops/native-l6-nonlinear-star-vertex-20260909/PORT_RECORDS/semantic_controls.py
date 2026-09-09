from pathlib import Path
import json,hashlib,tempfile,types,time
W=Path('/private/tmp/toe-native-l6-nonlinear-star-vertex-20260909');I=W/'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs';P=W/'.claude/science/physics-loops/native-l6-nonlinear-star-vertex-20260909/PORT_RECORDS';start=time.monotonic();rows=[]
def module(path,source=None):
 m=types.ModuleType('tested');m.__file__=str(path);exec(compile(path.read_bytes() if source is None else source,str(path),'exec'),m.__dict__);return m
primary=W/'scripts/native_l6_nonlinear_star_vertex_2026_09_09.py';m=module(primary);r=json.loads((I/'accepted/INDEPENDENT_REVIEW.json').read_text());m.claims(r)
for factor in (64,1/64):
 try:m.claims(r,factor);raise RuntimeError('mutant survived')
 except ValueError:rows.append({'mutation':'vertex scale changed by8, squared weight factor '+str(factor),'rejected':True})
g=W/'scripts/native_l6_nonlinear_vertex_geometry_2026_09_09.py';src=g.read_text()
for old,new in [('z=-2*(-1)**sum(v[:a])','z=2*(-1)**sum(v[:a])'),('for v in [0]+neighbors:','for v in [2]+neighbors:')]:
 if old not in src:raise RuntimeError('missing mutation target')
 try:module(g,src.replace(old,new)).check(I);raise RuntimeError('mutant survived')
 except ValueError as e:rows.append({'mutation':old+' -> '+new,'rejected':True,'reason':str(e)})
# Exact orthogonal decomposition: omitted three-particle bucket changes the true distance.
from fractions import Fraction as F
x=[F(3,2),F(1,3),F(1,5),F(1,7)];one=x[0]*x[0];higher=sum(v*v for v in x[1:]);full=sum(v*v for v in x)
if full-one!=higher or sum(v*v for v in x[2:])==higher:raise RuntimeError('projection control')
rows.append({'control':'exact orthogonal projection and omitted-three-sector adverse','passed':True})
(P/'SEMANTIC_CONTROLS.json').write_text(json.dumps({'status':'PASS','source_sha256':hashlib.sha256(primary.read_bytes()).hexdigest(),'geometry_sha256':hashlib.sha256(g.read_bytes()).hexdigest(),'controls':rows,'seconds':time.monotonic()-start,'physical_replay':False},indent=2)+'\n')
print(rows)
