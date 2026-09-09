"""Saved-row author verification only; no NumPy or physical computation."""
from pathlib import Path
import hashlib,json,math,re,signal
signal.alarm(30)
B=Path(__file__).resolve().parent.parent;P=B/'native-star-gaussian-kernel-pilot';R=B/'native-star-gaussian-kernel-root-review';O=B/'native-star-gaussian-kernel-run-49f78';HERE=Path(__file__).resolve().parent
reads={};checks=0
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):
 reads[str(p)]=sha(p);return json.loads(p.read_text())
def req(ok,msg):
 global checks
 if not ok:raise ValueError(msg)
 checks+=1
f=read(P/'FREEZE.json');req(sha(P/'FREEZE.json')=='49f78f7f1ea1e1fb17724e5b01d236536e0d6b64068eb3ec722c553f55274212','freeze')
for p,h in f['inputs'].items():req(sha(Path(p))==h,'pin '+p)
rf=read(R/'ROOT_FREEZE.json')
for p,h in rf['files'].items():req(sha(R/p)==h,'root pin')
res=read(O/'RESULT.json');done=read(O/'WORKER_COMPLETE.json');partial=read(O/'PARTIAL.json');receipt=read(R/'RECEIPT.json');accept=read(R/'ROOT_ACCEPTANCE.json');peak=read(R/'PEAK.json')
req(done['result_sha256']==sha(O/'RESULT.json') and done['freeze']==sha(P/'FREEZE.json'),'worker binding')
for p,h in accept['files'].items():req(sha(B/p)==h,'acceptance binding')
req(receipt['pass'] and receipt['returncode']==0 and receipt['failure'] is None,'root pass')
req(accept['attempts']==1 and accept['status']=='PASS_ROOT_ACCEPTED_FINITE_NORMALIZATION_ONLY','one attempt')
rows=res['rows'];names=['overlap','C_insertion','A_insertion'];times=[(0.,0.),(1/128,1/64),(1/64,1/64)]
req([(r['case'],r['time_index'],r['name']) for r in rows]==[(c,t,n) for c in range(5) for t in range(3) for n in names],'exact ordered45')
req(partial['rows']==rows and len(res['geometry'])==5,'partial complete')
errors=[]
for r in rows:
 a=complex(*r['gaussian']);b=complex(*r['literal']);err=abs(a-b);errors.append(err)
 req(tuple(r['times'])==times[r['time_index']],'fixed times')
 req(all(math.isfinite(x) for x in [a.real,a.imag,b.real,b.imag,r['chart_distance'],r['thouless_skew']]),'finite')
 req(err==r['absolute_error'] and err<=2e-10*(1+abs(b)),'stored discrepancy')
 req(r['chart_distance']<.75 and r['thouless_skew']<1e-10,'chart/skew')
 req(r['gaussian_seconds']>=0 and r['literal_seconds']>=0,'timings')
for i,g in enumerate(res['geometry']):req(g['case']==i and g['real_dimension']==10 and g['literal_K_square'] is True,'geometry metadata')
gs=sum(r['gaussian_seconds'] for r in rows);ls=sum(r['literal_seconds'] for r in rows)
req(gs==accept['gaussian_seconds_total'] and ls==accept['literal_seconds_total'],'cost sums')
req(max(errors)==accept['max_absolute_difference'],'max error')
shell=(R/'ROOT.stderr').read_text();reads[str(R/'ROOT.stderr')]=sha(R/'ROOT.stderr')
wall=float(re.search(r'^real ([0-9.]+)$',shell,re.M)[1]);rss=int(re.search(r'(\d+)  maximum resident set size',shell)[1])
req(wall==accept['external_seconds'] and rss==accept['external_max_rss'],'external shell')
req(peak['rss_bytes']==receipt['sampled_whole_tree_peak']==accept['sampled_whole_tree_peak'],'tree receipt')
req(wall<60 and peak['rss_bytes']<384*1048576 and done['rss_bytes']<384*1048576,'caps')
req(res['interval_certificate'] is False and res['infinite_node_value_computed'] is False,'scope')
out={'status':'PASS_AUTHOR_POST_VERIFICATION','checks':checks,'physical_reruns':0,'rows':len(rows),'max_error':max(errors),'max_chart':max(r['chart_distance'] for r in rows),'gaussian_seconds':gs,'literal_seconds':ls,'external_seconds':wall,'external_max_rss_bytes':rss,'sampled_whole_tree_peak_bytes':peak['rss_bytes'],'read_hashes':reads}
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='read_hashes'}))
