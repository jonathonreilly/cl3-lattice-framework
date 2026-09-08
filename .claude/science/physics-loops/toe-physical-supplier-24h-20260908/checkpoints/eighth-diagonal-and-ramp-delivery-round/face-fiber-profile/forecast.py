"""Fixed-face cost screening, not a production gate or mixing estimate."""
import pathlib,json,math,hashlib,struct

def positive(x):return type(x) in (float,int) and math.isfinite(x) and x>0
def compute(folder):
 folder=pathlib.Path(folder);r=json.loads((folder/'RESULT.json').read_text())
 if r['status']!='complete' or not positive(r['elapsed']) or not positive(r['rss_mib']) or r['rss_mib']>384 or len(r['cases'])!=2:raise ValueError('complete capped result')
 rows=[];accounted=0.
 for i,(row,V) in enumerate(zip(r['cases'],(.95,0.))):
  if (row['case'],row['V'],row['L'],row['n'],row['RK'],row['faces'],row['init_seed'],row['draw_seed'])!=(i,V,8,110592,2048,[0,512,1024],202609320100+i,202609320200+i) or not row['completed']:raise ValueError('fixed case')
  if len(row['blocks'])!=3 or [b['face'] for b in row['blocks']]!=row['faces'] or len(row['measurements'])!=4:raise ValueError('coverage')
  keys=('geometry_seconds','initializer_seconds','measurement_seconds','checkpoint_save_seconds','checkpoint_load_seconds')
  if not all(positive(row[k]) for k in keys) or not all(positive(b['seconds']) for b in row['blocks']):raise ValueError('timing')
  p=folder/('case'+str(i));raw=(p/'meta.json').read_bytes();m=json.loads(raw)
  if hashlib.sha256(raw).hexdigest()!=row['checkpoint_meta_sha'] or m!=row['checkpoint'] or (m['L'],m['n'],m['V'])!=(8,110592,V):raise ValueError('checkpoint receipt')
  for name,h in m['files'].items():
   if name not in ('states.bin','nf.bin','witness.bin') or hashlib.sha256((p/name).read_bytes()).hexdigest()!=h:raise ValueError('checkpoint payload')
  total=sum(z[0] for z in struct.iter_unpack('<H',(p/'nf.bin').read_bytes()))
  if total!=m['total_nf'] or total!=row['measurements'][-1]['total_nf']:raise ValueError('all-time total')
  for v in row['measurements']:
   if len(v['S'])!=2 or not all(math.isfinite(float(z)) for z in [v[k] for k in v if k!='S']+v['S']):raise ValueError('measurement finite')
  accounted+=sum(row[k] for k in keys)+sum(b['seconds'] for b in row['blocks'])
  maximum=max(b['seconds'] for b in row['blocks']);sweep=1536*maximum
  setup=row['geometry_seconds']+row['initializer_seconds']+row['checkpoint_save_seconds']+row['checkpoint_load_seconds']
  measurement_per_snapshot=row['measurement_seconds']/4
  rows.append(dict(V=V,maximum_fixed_face_block_seconds=maximum,nominal_sweep_proxy_seconds=sweep,base_16chain_16sweep_seconds_before_unallocated=16*(setup+16*(sweep+measurement_per_snapshot))))
 return dict(scope='three fixed faces only; pending outer timing, not a final forecast',accounted_case_seconds=accounted,cases=rows)


def price(pending,charged_seconds):
 if not positive(charged_seconds) or not positive(pending['accounted_case_seconds']):raise ValueError('outer accounting')
 if charged_seconds+0.02<pending['accounted_case_seconds']:raise ValueError('outer time below accounted timers')
 overhead=max(0.,charged_seconds-pending['accounted_case_seconds'])
 rows=[]
 for row in pending['cases']:
  rows.append(dict(row,unallocated_seconds_charged_per_hypothetical_chain=overhead,hypothetical_16chain_16sweep_seconds=row['base_16chain_16sweep_seconds_before_unallocated']+16*overhead))
 return dict(scope='fixed-face screening proxy only; no production or mixing claim',charged_outer_seconds=charged_seconds,accounted_case_seconds=pending['accounted_case_seconds'],unallocated_profile_seconds=overhead,formula='16*(setup + 16*(1536*max_fixed_face_block + mean_measurement)) + 16*max(0,outer_total - sum_all_case_timers)',cases=rows)
