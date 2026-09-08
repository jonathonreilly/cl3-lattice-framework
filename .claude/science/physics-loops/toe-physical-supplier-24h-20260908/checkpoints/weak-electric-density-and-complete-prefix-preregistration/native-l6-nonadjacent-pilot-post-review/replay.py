"""Independent rank-four inverse-trace replay; no author core import."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt,isfinite
from itertools import product
import json,hashlib,sys,signal,time,resource
BASE=Path(__file__).resolve().parent.parent;SOURCE=BASE/'native-l6-nonadjacent-gap-pilot';OUT=BASE/'native-l6-nonadjacent-pilot-run-97826';ROOT=BASE/'native-l6-nonadjacent-pilot-root-review';PIN='97826f9d7eb4fea4c3357cc7ba12d46c741fa51fbbdc95a25571eb6e94bf92a7'
def ck(x,msg):
 if not x:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def transpose(A):return list(map(list,zip(*A)))
def mat(A,B):
 cols=transpose(B);return [[sum(x*y for x,y in zip(row,col) if x and y) for col in cols] for row in A]
def inv(A):
 n=len(A);M=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for j in range(n):
  k=next(k for k in range(j,n) if M[k][j]);M[j],M[k]=M[k],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for k in range(n):
   if k!=j:q=M[k][j];M[k]=[a-q*b for a,b in zip(M[k],M[j])]
 return [r[n:] for r in M]
def baseline(census):
 V=list(product(range(6),repeat=3));black=[i for i,v in enumerate(V) if sum(v)%2==0];white=[i for i,v in enumerate(V) if sum(v)%2];bi={v:i for i,v in enumerate(black)};wi={v:i for i,v in enumerate(white)};B=[[0]*108 for _ in range(108)]
 for e,(i,j) in enumerate(census['edges']):
  xi=(-1)**sum(V[e//3][:e%3]);sign=-xi
  if i in bi:B[bi[i]][wi[j]]=sign
  else:B[bi[j]][wi[i]]=-sign
 A=mat(B,transpose(B));I=[[int(i==j) for j in range(108)] for i in range(108)];powers=[I,A]
 for k in range(2,4):powers.append(mat(powers[-1],A))
 # Vandermonde interpolation independently solves the four coefficients.
 nodes=(3,6,9,12);VI=inv([[F(x)**k for k in range(4)] for x in nodes]);coef=[sum(v/F(x+F(25,4)) for v,x in zip(row,nodes)) for row in VI];R=[[sum(coef[k]*powers[k][i][j] for k in range(4)) for j in range(108)] for i in range(108)]
 for i in range(108):
  nz=[(k,a) for k,a in enumerate(A[i]) if a]
  for j in range(108):ck(sum(a*R[k][j] for k,a in nz)+F(25,4)*R[i][j]==int(i==j),'baseline inverse')
 return B,R,bi,wi

def gap(mask,center,census,B,R,bi,wi):
 delta=[[0]*108 for _ in range(108)]
 for e,(a,b) in enumerate(census['edges']):
  if mask>>e&1:
   if a not in bi:a,b=b,a
   delta[bi[a]][wi[b]]=-2*B[bi[a]][wi[b]]
 row=delta[bi[0]];column=[delta[i][wi[center]] if i!=bi[0] else 0 for i in range(108)];F0=[[int(i==bi[0]),column[i]] for i in range(108)];G=[[row[j],int(j==wi[center])] for j in range(108)];ck(mat(F0,transpose(G))==delta,'literal rank2')
 BG=mat(B,G);U=[a+b for a,b in zip(F0,BG)];RU=mat(R,U);UtRU=mat(transpose(U),RU);UtR2U=mat(transpose(RU),RU);GG=mat(transpose(G),G)
 # C^-1=[[0,I],[I,-G*G]], avoiding author's I+C*G inverse formula.
 Ci=[[F(0) if i<2 and j<2 else F(int(i==j+2 or j==i+2)) if (i<2)!=(j<2) else -F(GG[i-2][j-2]) for j in range(4)] for i in range(4)]
 S=[[Ci[i][j]+UtRU[i][j] for j in range(4)] for i in range(4)];Si=inv(S);ck(mat(S,Si)==[[F(i==j) for j in range(4)] for i in range(4)],'small inverse');correction=mat(Si,UtR2U);trace=sum(R[i][i] for i in range(108))-sum(correction[i][i] for i in range(4));upper=F(1323,10)+F(5,2)*(108-F(25,4)*trace);canonical=72+40*F(isqrt(3*10**60),10**30)+48*F(isqrt(6*10**60),10**30);return canonical-upper,max(x.denominator.bit_length() for row in mat(Si,Ci) for x in row)

def main():
 start=time.monotonic();signal.alarm(170);ck(sha(SOURCE/'FREEZE.json')==PIN,'freeze');freeze=read(SOURCE/'FREEZE.json')
 for p,h in freeze['files'].items():ck(sha(SOURCE/p)==h,'source')
 for p,h in {**freeze['dependencies'],**freeze['runtime']}.items():ck(sha(p)==h,'dependency/runtime')
 ck(not (OUT/'FAILURE.json').exists(),'failure');result=read(OUT/'RESULT.json');plan=read(SOURCE/'PLAN.json');ck(result['status']=='COMPLETE' and result['freeze']==PIN and len(result['rows'])==len(plan['cases'])==25,'complete25');ck(sorted(p.name for p in OUT.glob('case_*.json'))==[f'case_{i:02d}.json' for i in range(25)],'case files');census=read(SOURCE/'CENSUS.json');B,R,bi,wi=baseline(census);details=[]
 for i,(row,c) in enumerate(zip(result['rows'],plan['cases'])):
  ck(row==read(OUT/f'case_{i:02d}.json'),'percase copy');ck((row['case'],row['name'],row['order'],row['mask'],row['white_center'])==(i,c['name'],c['order'],c['mask'],c['white_center']),'case identity');v,bits=gap(int(c['mask']),c['white_center'],census,B,R,bi,wi);ck(F(row['gap_lower'])==v and row['positive']==(v>0),'exact gap');ck(row['inverse_dimension']==4 and row['max_denominator_bits']==bits,'inverse diagnostics');ck(isfinite(row['seconds']) and row['seconds']>0,'case timing');details.append({'case':i,'gap_lower':str(v),'positive':v>0})
 outer=read(ROOT/'OUTER.json');ck(outer['freeze']==PIN and outer['returncode']==0 and outer['watchdog_failure'] is None and outer['provisional_resource_accept'] is True,'outer');ck(0<outer['seconds']<30 and 0<outer['observed_peak_whole_tree_bytes']<=384*1048576,'resources');ck(0<result['seconds']<29 and 0<result['rss_bytes']<=384*1048576,'innerresources');ck(result['singletons']==plan['singletons'] and F(result['singleton_lower'])==2*F(isqrt(3*10**60),10**30),'singleton')
 lines=(ROOT/'SHELL.stderr').read_text().splitlines();wall=[float(x.split()[1]) for x in lines if x.startswith('real ')];rss=[int(x.split()[0]) for x in lines if 'maximum resident set size' in x];ck(len(wall)==len(rss)==1 and 0<wall[0]<=30 and 0<rss[0]<=384*1048576,'shellreceipt')
 elapsed=time.monotonic()-start;ck(elapsed<170 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=384*1048576,'review cap');return dict(status='PASS',freeze=PIN,cases=25,alternative='inverse(C^-1+U*RU), exact Vandermonde baseline, no author import',rows=details,seconds=elapsed)
if __name__=='__main__':ck(len(sys.argv)==1,'no arguments');print(json.dumps(main(),indent=2))
