"""Synthetic final aggregation fixture; no eigensolver or physical raw data."""
from pathlib import Path
import tempfile,json,hashlib,copy
from fractions import Fraction as F
from replay import aggregate,REPS,SOURCE,ck,sha,read
count=0
with tempfile.TemporaryDirectory() as d:
 root=Path(d);out=root/'production';out.mkdir();reps=root/'replays';reps.mkdir();freeze='synthetic';(out/'COMPLETE.json').write_text(json.dumps({'freeze':freeze}));dens={r:(F(-2)+F(r,100),F(-2)+F(r,100)+F(1,10000)) for r in REPS}
 for j in range(24):
  p=out/f'job{j:02d}';p.mkdir();(p/'NODES.jsonl').write_text('synthetic\n');(p/'RESULT.json').write_text('{}');e=out/f'job{j:02d}.receipt.json';e.write_text('{}');v=dict(job=j,rep=REPS[j//4],nodes=1024,freeze=freeze,status='PASS',seconds=1.,peak_bytes=1000,node_sha=sha(p/'NODES.jsonl'),producer_receipt_sha=sha(p/'RESULT.json'),external_receipt_sha=sha(e),line_hashes=['synthetic']*1024,density_sum=[str(x*1024) for x in dens[REPS[j//4]]]);(reps/f'job{j:02d}.json').write_text(json.dumps(v))
 trig=read(SOURCE/'TRIG_INPUTS.json');cubes=read(SOURCE/'CUBE_INPUTS.json');error=F(3,8192)*F(trig['pi_upper_numerator'],trig['pi_denominator'])**2;costs=[]
 for r in REPS[:-1]:
  m=cubes['rows'][r]['defects'];lo=dens[r][0]-dens[15][1]-error;hi=dens[r][1]-dens[15][0]+error;costs.append(dict(rep=r,defects=m,density_lower=str(lo),density_upper=str(hi),limiting_delta_lower=str(8*lo/m),limiting_delta_upper=str(8*hi/m),auxiliary_defect_coefficient_lower=str(2*lo/m),native_half_objective_defect_coefficient_lower=str(lo/m),strictly_positive=lo>0))
 report=dict(freeze=freeze,grid_n=32,folded_n=16,multiplicity=8,node_count=24576,original_node_count=196608,quadrature_difference_radius=str(error),grid_density_intervals={r:list(map(str,ab)) for r,ab in dens.items()},costs=costs,all_five_positive=False,common_density_lower=str(min(F(c['density_lower']) for c in costs)));target=out/'ANALYSIS.json';target.write_text(json.dumps(report));v=aggregate(out,reps,freeze);ck(v['all_five_positive'] is False,'negative preservation');count+=1
 for key,value in [('all_five_positive',True),('folded_n',32),('common_density_lower','0'),('quadrature_difference_radius','0')]:
  bad=copy.deepcopy(report);bad[key]=value;target.write_text(json.dumps(bad))
  try:aggregate(out,reps,freeze)
  except ValueError:count+=1
  else:raise ValueError('mutant survived '+key)
 target.write_text(json.dumps(report));saved=reps/'job23.json';saved.rename(reps/'wrong.json')
 try:aggregate(out,reps,freeze)
 except ValueError:count+=1
 else:raise ValueError('missing replay survived')
print(json.dumps({'controls':count,'scope':'synthetic24job aggregation, failed signs, exact error/folding and missing membership; not certificate data'}))
