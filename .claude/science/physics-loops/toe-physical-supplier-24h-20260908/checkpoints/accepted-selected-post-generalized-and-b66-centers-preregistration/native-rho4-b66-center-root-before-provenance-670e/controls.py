"""Fabricated full-shape schema fixture. Native moment evaluator replaced by zero mock.
No native input, center formula or true moment40 evaluation. This tests schema only.
"""
import json,tempfile,hashlib,types
from pathlib import Path
from fractions import Fraction as F
import schema as s

def run():
 original=s.moments;s.moments=lambda:[F(0)]*41
 def write(p,x):p.write_text(json.dumps(x,default=str)+'\n')
 def rowpair(x):return list(map(str,x))
 tests=0
 try:
  with tempfile.TemporaryDirectory()as tmp:
   p=Path(tmp);o=p/'out';o.mkdir();budget=p/'budget.json';write(budget,{'low_radii':['1','1'],'high_input_radii':['1','1']});binding=p/'binding.json';write(binding,{'pole_files':[str(budget)]*66});rf={'binding_path':str(binding),'binding_sha256':'b','worker_freeze':'w'}
   pi=s.pi_bounds();write(o/'PI.json',{'interval':rowpair(pi)});write(o/'MOMENTS.json',{'moment_indices':list(range(41)),'values':['0']*41});write(o/'STARTED.json',{})
   rem=F(12**40,81*8**81);q=F(128,4**52);low=(s.floor(-s.EPS**3*s.A0/6),s.floor(-s.EPS**3*s.A0/3));high=(s.floor(rem/2),)*2;c=tuple(low[k]+high[k]for k in range(2));r=F(2)+rem/2+q+F(1,10**35);ans=[]
   for k in range(2):
    v=[x*y for x in(c[k]-r,c[k]+r)for y in(2/pi[1],2/pi[0])];b=(s.floor(min(v)),-s.floor(-max(v)));ans.append(b if k==0 else(-b[1],-b[0]))
   rows=[]
   for i in range(66):
    od=o/f'POLE_{i:02d}';od.mkdir()
    with(od/'CENTERS.ndjson').open('w')as f:
     for j in range(1742):f.write(json.dumps({'node':j,'panel':j//26-64,'centers':['0','0'],'panel_cumulative':['0','0'],'accepted_radii':['0','0']})+'\n')
    for j in range(67):write(od/f'PANEL_{j:02d}.json',{'panel':j-64,'centers':['0','0'],'cumulative':['0','0'],'accepted_radius_cumulative':['0','0']})
    tail={'s':'1','A':['0','0'],'Aprime':['0','0'],'high_centers_with_half_remainder':rowpair(high),'low_centers':rowpair(low),'middle':['0','0'],'node_radii':['0','0'],'low_radii':['1','1'],'high_input_radii':['1','1'],'positive_remainder':str(rem),'quadrature_radius':str(q),'arithmetic_reserve':'1/100000000000000000000000000000000000','total_centers':rowpair(c),'total_radii':rowpair((r,r))};write(od/'TAILS_AND_BUDGET.json',tail)
    row={'pole':i,'s_midpoint':'1','B':rowpair(ans[0]),'Bprime':rowpair(ans[1]),'widths':[str(b-a)for a,b in ans],'targets':rowpair(s.TARGETS),'status':'INDETERMINATE_TARGET'};rows.append(row);write(od/'RESULT.json',row)
   result={'status':'COMPLETE_NEW_RHO4_B66_CERTIFICATES','rows':rows,'poles':66,'node_center_pairs':114972,'panels_per_pole':67,'tail_terms':40,'moments':41,'oracle_calls':0,'old_protocol_replays':0,'matrix_computed':False,'alpha_computed':False,'all_targets_met':False,'seconds':1.0};write(o/'RESULT.json',result)
   worker={'status':'COMPLETE_NEW_CENTER_CERTIFICATES_ONLY','runtime_sha256':'w','binding_sha256':'b','result_sha256':s.sha(o/'RESULT.json'),'seconds':2.0,'rss_bytes':1000000,'all_targets_met':False};write(o/'WORKER_COMPLETE.json',worker)
   partial={'current':{'stage':'complete'},'rows':rows,'node_centers':114972,'seconds':1.5};write(o/'PARTIAL.json',partial);write(o/'CURRENT.json',{'stage':'complete'})
   answer=s.check(o,rf,3.0);assert answer['all_targets_met']is False;tests+=1
   for file,field,value in [('RESULT.json','node_center_pairs',True),('RESULT.json','oracle_calls',1),('CURRENT.json','stage','node'),('PARTIAL.json','node_centers',114971),('WORKER_COMPLETE.json','rss_bytes',1.0)]:
    old=json.loads((o/file).read_text());changed={**old,field:value};write(o/file,changed)
    if file=='RESULT.json':write(o/'WORKER_COMPLETE.json',{**worker,'result_sha256':s.sha(o/'RESULT.json')})
    try:s.check(o,rf,3.0)
    except (ValueError,KeyError):tests+=1
    else:raise AssertionError('accepted '+field)
    write(o/file,old)
    write(o/'WORKER_COMPLETE.json',worker)
   f=o/'POLE_00/TAILS_AND_BUDGET.json';old=json.loads(f.read_text());write(f,{**old,'high_centers_with_half_remainder':['0','0']})
   try:s.check(o,rf,3.0)
   except ValueError:tests+=1
   else:raise AssertionError('missing half remainder accepted')
  return {'status':'PASS_FULL_SHAPE_FABRICATED_SCHEMA','checks':tests,'synthetic_records':114972,'actual_native_moment_calls':0,'actual_center_calls':0,'override':'moments() replaced by41 synthetic zeros; validates structure/accumulation/tail path, not native moment identity'}
 finally:s.moments=original
if __name__=='__main__':print(json.dumps(run()))
