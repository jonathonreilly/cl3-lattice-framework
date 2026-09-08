"""Execute only actual geometry class/functions extracted by AST; no producer job."""
import ast,pathlib,hashlib,json
from dataclasses import dataclass
import numpy as np
from geometry_reference import Geometry
p=pathlib.Path('/private/tmp/toe-physical-supplier-24h-20260908/scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py')
s=p.read_text();tree=ast.parse(s);nodes=[]
for n in tree.body:
 if isinstance(n,(ast.ClassDef,ast.FunctionDef)) and n.name in ('Geometry','link_index','build_geometry'):nodes.append(n)
 if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ORIENTATIONS' for t in n.targets):nodes.append(n)
if len(nodes)!=4:raise ValueError('source extraction menu')
ns=dict(np=np,dataclass=dataclass);exec(compile(ast.Module(body=nodes,type_ignores=[]),str(p),'exec'),ns)
rows=[]
for L in (2,4):
 actual=ns['build_geometry'](L);g=Geometry(L);faces=actual.plaquette_links.tolist()
 if faces!=[list(f) for f in g.faces]:raise ValueError('actual source geometry differs')
 masks=[sum(1<<int(e) for e in f) for f in faces]
 if len(set(masks))!=3*L**3:raise ValueError('unexpected native aliases')
 rows.append(dict(L=L,geometric_labels=len(faces),distinct_masks=len(set(masks)),maximum_mask_multiplicity=max(masks.count(m) for m in set(masks)),all_ordered_faces_match=True))
print(json.dumps(dict(source=str(p),source_sha=hashlib.sha256(p.read_bytes()).hexdigest(),extracted_AST_sha=hashlib.sha256(ast.dump(ast.Module(body=nodes,type_ignores=[]),include_attributes=False).encode()).hexdigest(),rows=rows,scope='actual source geometry only, no stochastic or producer execution'),indent=2))
