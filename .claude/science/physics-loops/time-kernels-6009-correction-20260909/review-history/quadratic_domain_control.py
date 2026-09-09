import ast,json
from fractions import Fraction
from pathlib import Path
p=Path(__file__).parents[1]/'originals/6009/scripts/frontier_cycle884_gbs2_kernel_window_2026_07_28.py'
t=ast.parse(p.read_text());ns={'Fraction':Fraction,'NEIGHBOURS':((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))}
names={'ptrim','padd','pneg','psub','pmul','pscale','pdeg','pmonic','pmod','pgcd','pdivexact','squarefree_split','site_meanvalue_residual'}
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),str(p),'exec'),ns)
rows=[];polys=[]
for n in (1,2):
 U,V,W,D0=ns['site_meanvalue_residual']((n,0,0));h=ns['pgcd'](U,V)
 Ur,Vr=ns['pdivexact'](U,h),ns['pdivexact'](V,h)
 norm=ns['psub'](ns['pmul'](Ur,Ur),ns['pscale'](ns['pmul'](Vr,Vr),Fraction(D0)))
 polys.append(norm)
 rows.append({'axis':n,'D':D0,'h_coefficients':[str(x) for x in h],'h_divides_rationalized_denominator':not ns['pmod'](W,h),'reduced_norm_degree':len(norm)-1})
print(json.dumps({'rows':rows,'reduced_norm_gcd':[str(x) for x in ns['pgcd'](*polys)],'scope':'actual quadratic functions; domain of removed factors still requires original denominators'},indent=2))
