"""Source mapping for future execution; no module-level input reads.
Reviewed prior root extraction is reused explicitly; no producer loader import.
"""
import json,math
from pathlib import Path
from fractions import Fraction as F
import prior as P
import independent as I

def read(s):
 P.need(P.sha(s['path'])==s['sha256'],'bound bytes');return json.loads(Path(s['path']).read_text())
def events(s,count):
 P.need(P.sha(s['path'])==s['sha256'],'event bytes');r=[json.loads(x)for x in Path(s['path']).read_text().splitlines()];P.need(len(r)==count,'event count')
 for i,x in enumerate(r,1):P.need(type(x['sequence'])is int and x['sequence']==i,'sequence')
 return r
def family(s):
 f={k:read(s['files'][k])for k in ['result','acceptance','worker','receipt','root_freeze']};a,w,r=f['acceptance'],f['worker'],f['receipt'];e=s['expected']
 P.need(a['status']==e['acceptance']and w['status']==e['worker']and f['result']['status']==e['result'],'family status');P.need(a['once']is True and r['pass']is True and r['failure']is None and type(r['returncode'])is int and r['returncode']==0,'family completion');P.need(a['result_sha256']==w['result_sha256']==s['files']['result']['sha256'],'family result');P.need(a['worker_freeze']==w['runtime_sha256']==r['worker_freeze']==s['worker_freeze']==f['root_freeze']['worker_freeze'],'family worker');P.need(a['root_freeze']==s['files']['root_freeze']['sha256'],'family root')
 for x,cap in [(w['seconds'],e['worker_seconds']),(r['seconds'],e['root_seconds']),(a['external_seconds'],e['external_seconds'])]:P.need(type(x)in(int,float)and math.isfinite(x)and 0<x<cap,'time')
 for x in [w['rss_bytes'],r['sampled_whole_tree_peak'],a['sampled_whole_tree_peak'],a['external_rss_bytes']]:P.need(type(x)is int and 0<x<=384*1048576,'RSS')
 P.need(w['seconds']<=r['seconds']<=a['external_seconds']and r['sampled_whole_tree_peak']==a['sampled_whole_tree_peak'],'resource chain');return f

def load(binding):
 q=family(binding['quartic']);qb=read(binding['quartic']['binding'])
 for name in ['degree20','posterior20','high']:family(qb[name])
 hb=read(qb['high']['binding']);pb=read(qb['posterior20']['binding'])
 for k in ['events','result']:P.eq(hb['degree20']['files'][k],qb['degree20']['files'][k],'high original');P.eq(pb['files'][k],qb['degree20']['files'][k],'posterior original')
 same=P.source_packet(qb);P.eq(read(binding['quartic']['inputs']),same,'quartic original packet');qe=events(binding['quartic']['events'],97);he=events(binding['high_events'],189)
 ha=read(qb['high']['files']['acceptance']);P.need(ha['output_hashes']['EVENTS.ndjson']==binding['high_events']['sha256'],'accepted high event identity')
 sources=[x['data']for x in he if x['stage']=='absolute_moment_source_map'];grids=[x['data']for x in he if x['stage']=='absolute_moment_grid'];P.need(len(sources)==len(grids)==1,'source grids');R={}
 for n in range(11):
  lo,hi=P.box(sources[0]['rational'][str(n)]);z=((lo.numerator*I.GRID//lo.denominator,I.ceildiv(hi.numerator*I.GRID,hi.denominator)),(0,0));P.eq(grids[0]['moments'][str(n)],z,'radial outward');R[n]=I.checked(z)
 ev=events(qb['degree20']['files']['events'],255);out={}
 for index,mode in enumerate(['residual','variational']):
  old=q['result']['rows'][index];P.need(old['mode']==mode,'mode');row=same[mode];p={};s={};oq={};first={}
  gate=[x['data']for x in ev if x['stage']=='gate_inputs'and x['choice']==mode];P.need(len(gate)==1,'gate')
  for kind in ['P','O']:
   p[kind]=row['rows'][kind]['p'];oq[kind]=P.rat(gate[0]['rows'][kind]['q']);raw=[x['data']for x in ev if x['stage']=='source_moment_raw'and x['choice']==mode and x['data'].get('kind')==kind];P.need(len(raw)==3,'old source moments');s[kind]=[]
   for j,x in enumerate(raw):
    P.need(type(x['index'])is int and x['index']==j,'source order');lo,hi=P.box(x['real']);im=P.box(x['imaginary']);P.need(im[0]<=0<=im[1],'source real');s[kind].append(((lo.numerator*I.GRID//lo.denominator,I.ceildiv(hi.numerator*I.GRID,hi.denominator)),(0,0)))
   bound=[x['data']for x in qe if x['stage']=='class_residual_bound'and x['choice']==mode and x['data'].get('kind')==kind];P.need(len(bound)==1,'first bound');first[kind]=P.rat(bound[0]['first_squared_upper']);P.need(first[kind]>=0,'first norm')
  out[mode]={'p':p,'old_q':oq,'s0_s2':s,'first_squared':first,'a_squared':row['trial_a2'],'old_alpha':P.box(old['intersection'])}
 return R,out
