from pathlib import Path
import json
P=Path(__file__).parent;S=P.parent/'native-l6-allprefix-gap';C=P.parent/'native-l6-nonadjacent-prefix-census'
s=(S/'core.py').read_text();(P/'ORIGINAL_ADJACENT_CORE.txt').write_text(s)
s=s.replace('def certify(mask,controls=False):','def certify(mask,white_center,controls=False):')
s=s.replace('wi[36]','wi[white_center]')
a=s.index(' rem=D-np.outer');b=s.index(' if controls:',a)
s=s[:a]+''' rem=D-np.outer(ev,z)-np.outer(u,ew)
 if np.any(rem):raise ValueError('rank2 defect')
 FF=np.column_stack((ev,u));GG=np.column_stack((z,ew));U=np.column_stack((FF,B@GG));GGram=GG.T@GG
 C=[[F(int(GGram[i,j])) if i<2 and j<2 else F(i==j+2 or j==i+2) for j in range(4)] for i in range(4)]
'''+s[b:]
s=s.replace('range(6)','range(4)') if False else s
# Only reduced-update dimensions change; literal lattice stays6.
s=s.replace('for j in range(6)] for i in range(6)', 'for j in range(4)] for i in range(4)').replace('for i in range(6));upper','for i in range(4));upper')
s=s.replace("return dict(mask=str(mask),gap_lower", "return dict(mask=str(mask),white_center=white_center,inverse_dimension=4,max_denominator_bits=max(x.denominator.bit_length() for row in Mi for x in row),gap_lower")
(P/'core.py').write_text(s)
c=json.loads((C/'CENSUS.json').read_text());(P/'CENSUS.json').write_bytes((C/'CENSUS.json').read_bytes());cases=[]
for row in c['rows']:
 for order in range(1,6):
  candidates=[x for x in row['proper_keys'] if x['order']==order and x['mask'] not in row['singleton_masks']]
  x=min(candidates,key=lambda x:x['used']);cases.append(dict(name=row['name'],white_center=row['centers'][1],order=order,mask=x['mask'],used=x['used']))
(P/'PLAN.json').write_text(json.dumps(dict(status='UNLAUNCHED',cases=cases,singletons={m:v for r in c['rows'] for m,v in r['singleton_masks'].items()},full_distinct=4986,full_proper_keys=5110,proposed_full_shards=52),indent=2)+'\n')
