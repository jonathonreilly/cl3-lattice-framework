"""Disabled binding schema and pure exact conversion/extraction helpers."""
from fractions import Fraction as F
import json,hashlib,math
from pathlib import Path
S=1<<256
class Refused(ValueError):pass
def need(x,m):
 if not x:raise Refused(m)
def rational(x):
 need(type(x)is str and len(x)<=20000,'rational token');v=F(x);need(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=32768,'canonical32768bits');return v
def interval(x):
 need(type(x)is list and len(x)==2,'interval');a,b=map(rational,x);need(a<=b,'interval order');return a,b
def dyadic(x):
 a,b=interval(x);lo=a.numerator*S//a.denominator;hi=-((-b.numerator*S)//b.denominator);need(max(abs(lo).bit_length(),abs(hi).bit_length())<=4096,'stored grid cap');return [[lo,hi],[0,0]]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def timing(x,cap):need(type(x)in(int,float)and math.isfinite(x)and 0<x<cap,'finite capped time')
def memory(x):need(type(x)is int and 0<x<=384*1048576,'literal RSS')
def receipt_family(objects,pins,expected):
 a,w,r,rf=objects['acceptance'],objects['worker'],objects['receipt'],objects['root_freeze']
 need(a['status']==expected['accepted_status']and a['once']is True,'accepted status');need(a['result_sha256']==pins['result']==w['result_sha256'],'result identity');need(a['worker_freeze']==pins['worker_freeze']==w['runtime_sha256']==r['worker_freeze']==rf['worker_freeze'],'worker identity');need(a['root_freeze']==pins['root_freeze'],'root identity');need(w['status']==expected['worker_status'],'worker complete');need(r['pass']is True and r['failure']is None and type(r['returncode'])is int and r['returncode']==0,'receipt completion')
 for x,cap in [(w['seconds'],expected['worker_seconds']),(r['seconds'],expected['root_seconds']),(a['external_seconds'],expected['external_seconds'])]:timing(x,cap)
 need(w['seconds']<=r['seconds']<=a['external_seconds'],'time ordering')
 for x in [w['rss_bytes'],r['sampled_whole_tree_peak'],a['sampled_whole_tree_peak'],a['external_rss_bytes']]:memory(x)
 need(r['sampled_whole_tree_peak']==a['sampled_whole_tree_peak'],'tree receipt relation')
def lower_moments(events):
 need(type(events)is list and len(events)==255,'fixed original event count')
 for i,e in enumerate(events,1):need(type(e['sequence'])is int and e['sequence']==i,'original sequence')
 out={}
 for kind in ['P','O']:
  modes=[];originals=[]
  for mode in ['residual','variational']:
   rows=[e['data']for e in events if e['stage']=='vacuum_moment_raw'and e['choice']==mode and e['data'].get('kind')==kind];need(len(rows)==7,'seven originals');m={};originals.append(rows)
   for j,row in enumerate(rows):
    need(type(row['index'])is int and row['index']==j,'moment index');im=interval(row['imaginary']);need(im[0]<=0<=im[1],'real moment');m[str(j)]=dyadic(row['real'])
   need(interval(rows[0]['real'])==(F(1),F(1))and m['0']==[[S,S],[0,0]],'m0 exact1');modes.append(m)
  need(originals[0]==originals[1]and modes[0]==modes[1],'same original vacuum moments');out[kind]=modes[0]
 return out
def load(binding_path):
 # No path is read until the entire future binding has been independently completed.
 raise Refused('NOT_READY: accepted omega79 receipt and full transitive source binding absent')
