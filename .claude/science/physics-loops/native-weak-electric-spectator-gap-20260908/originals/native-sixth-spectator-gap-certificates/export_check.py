from pathlib import Path
import json,runpy,hashlib
b=Path(__file__).parent;ns=runpy.run_path(str(b/'check.py'));p=Path('/private/tmp/toe-24h-probes-20260908/native-zero-penalty-sixth-spectator-coefficient/PREFIXES.json');x=json.loads(p.read_text())
if x['coordinates']!=[list(v) for v in ns['vs']] or x['edge_order']!=[list(e) for e in ns['edges']]:raise RuntimeError('coordinate binding')
rows=[]
for row in x['rows']:
 if row['bridge_edge']==ns['bridge']:continue
 q=next(v for v in row['prefixes'] if v['k']==3);r=ns['cert'](int(q['full_toggle_mask']));r['bridge_edge']=row['bridge_edge'];rows.append(r)
(b/'EXPORT_RESULT.json').write_text(json.dumps({'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':rows,'scope':'five prospectively selected external k3 prefixes, no solves'},indent=2)+'\n')
