import ast,json,itertools
from pathlib import Path
p=Path(__file__).parents[1]/"originals/scripts/frontier_cycle947_h0_discharge_2026_07_28.py"
t=ast.parse(p.read_text());ns={"ast":ast}
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef) and n.name=="statement_is_lane_diagonal"],type_ignores=[]),str(p),"exec"),ns)
statement="c[1] ^= c[0]"
assert ns["statement_is_lane_diagonal"](statement)[0]
a=[0,0];b=[1,0]
exec(statement,{},{"c":a});exec(statement,{},{"c":b})
assert a[1]!=b[1] and not ((a[1]^b[1])&~1)
# Counterexample to covariance implying that the FULL automorphism group is only spatial isometries.
# Identity rule is an implication counterexample, NOT a model satisfying every axiom.
identity=lambda x:tuple(x)
local=lambda x:(1-x[0],)+tuple(x[1:])
assert all(identity(local(x))==local(identity(x)) for x in itertools.product((0,1),repeat=3))
print(json.dumps({"lane_diagonal_statement":statement,"actual_whitelist_accepts":True,"wire1_changes_when_wire0_changes_in_one_lane":True,"other_lanes_unchanged":True,"identity_rule_commutes_with_single_site_flip_all_8_states":True,"scope":"counterexamples to implication steps only; no physical model or supplier claimed"}))
