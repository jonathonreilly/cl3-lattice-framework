import ast,json,sys
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parent;sys.path.insert(0,str(p.parent/'detuned-energy-moment'));sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts');import producer_original as prod
src=(p/'kernel.py').read_text();rows=[]
for name,old,new in [('real_only','return np.sum(obs*obs)','return np.sum(obs[:len(obs)//2]*obs[:len(obs)//2])'),('lost_cache_copy','obs[indices].copy()','obs.copy()'),('wrong_signed_delta','(1.-2.*state[i])','(2.*state[i]-1.)')]:
 s=src.replace(old,new);assert s!=src;(p/(name+'.py')).write_text(s)
 tree=ast.parse(s);nodes=[]
 for n in tree.body:
  if isinstance(n,ast.FunctionDef):n.decorator_list=[];nodes.append(n)
 ns={'np':np,'prod':prod};exec(compile(ast.Module(body=nodes,type_ignores=[]),name,'exec'),ns)
 failed=False
 try:
  if name=='real_only':
   o=np.array([1.,2.,3.,4.]);
   if ns['source_norm'](o)!=30:raise AssertionError('full_complex_norm')
  elif name=='lost_cache_copy':
   aa=np.arange(12).reshape(3,4);oo=np.arange(36.).reshape(3,12);z=ns['resample'](aa,np.arange(3),oo,np.arange(3),np.array([-1000.,0.,-1000.]))
   if not np.array_equal(z[2],np.repeat(oo[1:2],3,axis=0)):raise AssertionError('cache_ancestry')
  else:
   g=prod.build_geometry(4);from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
   st=initial_ice(4).ravel();cr,ci,_=prod.transverse_coefficients(4,(1,));co=np.vstack((cr,ci));o=ns['literal_O'](st,co)
   for f,face in enumerate(g.plaquette_links):
    if prod.is_flippable(st,face):
     s2=st.copy();o2=o.copy();ns['flip_cached'](s2,prod.count_flippable(st,g.plaquette_links),o2,f,co,g.plaquette_links,g.affected_plaquettes,g.affected_counts)
     if np.max(abs(o2-ns['literal_O'](s2,co)))>1e-12:raise AssertionError('signed_complex_cache')
 except AssertionError as e:failed=True;reason=str(e)
 if not failed:raise RuntimeError('surviving mutant '+name)
 rows.append({'mutation':name,'failed':failed,'predicate':reason,'scope':'actual changed function executed without JIT decorator'})
(p/'MUTATIONS.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
