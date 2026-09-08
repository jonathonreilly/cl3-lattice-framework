from pathlib import Path
import runpy,contextlib,io,json,hashlib
p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p/'check_design.py'))
rows=[]
for e in d['bridges']:
 sets=d['pairings'](sorted(list(d['cut'])+[e,e]));keys={}
 for pairs in sets:
  for sub in range(64):
   usage={};k=sub.bit_count()
   for j,(a,b) in enumerate(pairs):
    if sub>>j&1:
     usage[a]=usage.get(a,0)+1;usage[b]=usage.get(b,0)+1
   mask=sum(1<<a for a,n in usage.items() if n%2);boundary=sum(1<<a for a,n in usage.items() if a!=e and n)
   key=(boundary,usage.get(e,0));keys[key]={'k':k,'boundary_used_mask':str(boundary),'bridge_count':usage.get(e,0),'full_toggle_mask':str(mask)}
 rows.append({'bridge_edge':e,'bridge_endpoints':d['edges'][e],'unordered_pair_sets':len(sets),'prefixes':sorted(keys.values(),key=lambda x:(x['k'],int(x['boundary_used_mask']),x['bridge_count']))})
out={'edge_order':d['edges'],'coordinates':d['vs'],'centers':[d['v'],d['w']],'boundary_edges':sorted(d['cut']),'rows':rows,'scope':'All completable multidegrees from exact six-pair incidence matchings; k0 and6 included but need no resolvent','design_source_sha256':hashlib.sha256((p/'check_design.py').read_bytes()).hexdigest()}
(p/'PREFIXES.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'counts':[{'bridge':r['bridge_edge'],'keys':len(r['prefixes']),'proper':sum(0<x['k']<6 for x in r['prefixes'])} for r in rows],'distinct_proper_masks':len({x['full_toggle_mask'] for r in rows for x in r['prefixes'] if 0<x['k']<6}),'sha256':hashlib.sha256((p/'PREFIXES.json').read_bytes()).hexdigest()},indent=2))
