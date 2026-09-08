from producer import *
signal.alarm(30)
t=time.monotonic();rows=run(128,.01,reps=1,classical=20,burn=80);work=time.monotonic()-t
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if time.monotonic()-start>=30 or not 0<rss<384:raise ValueError('micro resources')
# Conservative: first whole call includes compile/load; multiply this cold cost, never subtract it.
forecast128=1.5*work*16+(t-start);forecast256=1.5*work*32+(t-start)
print(json.dumps(dict(scope='one end-to-end timing replica, not an energy estimate',population=128,xi=.01,classical=20,burn=80,work_seconds=work,seconds=time.monotonic()-start,rss_mib=rss,first_call_includes_compilation_or_cache_load=True,postconditions=all(r['postconditions'] for r in rows),cache_error=max(r['literal_error'] for r in rows),forecast_cell128=forecast128,forecast_cell256=forecast256,forecast_total14=7*(forecast128+forecast256),gate120=max(forecast128,forecast256)<=120,gate500=7*(forecast128+forecast256)<=500,source_sha256=hashlib.sha256((p/'producer.py').read_bytes()).hexdigest()),indent=2))
