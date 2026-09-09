"""Execute actual driver preflight and scanner import only, never fixture/scan."""
from pathlib import Path
import runpy,json
P=Path(__file__).resolve().parent
source=(P/'run.py').read_text().split('out=Path(sys.argv[1]).resolve()',1)[0]
ns={'__file__':str(P/'run.py'),'__name__':'readiness_actual_prefix'}
exec(compile(source,str(P/'run.py'),'exec'),ns)
scanner=runpy.run_path(str(P/'scanner.py'))
ns['loaded_guard']()
print(json.dumps({'status':'PASS','actual_preflight_executed':True,'scanner_imported':True,'fixture_created':False,'full_scans':0}))
