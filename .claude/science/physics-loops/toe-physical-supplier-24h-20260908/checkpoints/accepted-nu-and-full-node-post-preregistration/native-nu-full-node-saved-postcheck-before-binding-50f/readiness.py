from pathlib import Path
import ast,json
p=Path(__file__).resolve().parent
ast.parse((p/'check.py').read_text())
assert json.loads((p/'BINDING.json').read_text())['status']=='NOT_READY'
print(json.dumps({'status':'PASS_SOURCE_AST_ONLY','saved_calls':0,'oracle_calls':0}))
