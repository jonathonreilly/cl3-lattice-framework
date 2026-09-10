# Pure conversion and receipt guards only, no source files or scientific values loaded.
import loader as L
from fractions import Fraction as F
import json,copy
n=0
for token in ['1/3','-1/7','1','0']:
 x=L.dyadic([token,token]);v=F(token);assert F(x[0][0],L.S)<=v<=F(x[0][1],L.S);n+=1
expected={'accepted_status':'SYNTHETIC','worker_status':'COMPLETE','worker_seconds':19,'root_seconds':19.5,'external_seconds':20};pins={'result':'r','worker_freeze':'w','root_freeze':'f'};o={'acceptance':{'status':'SYNTHETIC','once':True,'result_sha256':'r','worker_freeze':'w','root_freeze':'f','external_seconds':3,'external_rss_bytes':100,'sampled_whole_tree_peak':200},'worker':{'status':'COMPLETE','result_sha256':'r','runtime_sha256':'w','seconds':1,'rss_bytes':100},'receipt':{'worker_freeze':'w','pass':True,'failure':None,'returncode':0,'seconds':2,'sampled_whole_tree_peak':200},'root_freeze':{'worker_freeze':'w'}};L.receipt_family(o,pins,expected);n+=1
for family,key,value in [('receipt','seconds',True),('worker','rss_bytes',1.0),('acceptance','once',1),('receipt','failure','bad')]:
 q=copy.deepcopy(o);q[family][key]=value
 try:L.receipt_family(q,pins,expected)
 except ValueError:n+=1
 else:raise AssertionError('bad receipt accepted')
print(json.dumps({'checks':n,'native_files_read':0}))
