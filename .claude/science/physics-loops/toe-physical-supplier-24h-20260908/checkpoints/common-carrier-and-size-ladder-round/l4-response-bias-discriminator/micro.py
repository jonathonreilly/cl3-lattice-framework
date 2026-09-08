from driver import *
signal.alarm(30)
g=prod.build_geometry(4);cr,ci,modes=prod.transverse_coefficients(4,(1,2));co=source_coefficients(cr,ci,2);t=time.monotonic()
st,ct,ob,ns,xs,ess,drift,div=prepare(initial_ice(4).ravel(),-.05,.02,1.92,2048,2,8,co,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,6199999)
error=float(np.max(abs(ob[:,:6]+1j*ob[:,6:]-prod.evaluate_observables(st,cr[6:],ci[6:]))))
if not np.isfinite(error) or error>1e-10 or not np.all((st==0)|(st==1)):raise ValueError('cache/binary')
for s,n in zip(st,ct):
 if prod.count_flippable(s,g.plaquette_links)!=n or not np.all(vertex_degrees(s.reshape(4,4,4,3))==3) or electric_flux(s.reshape(4,4,4,3))!=(0,0,0):raise ValueError('invariants')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-start
if elapsed>=30 or not 0<rss<384:raise ValueError('resources')
print(json.dumps(dict(scope='memory/timing only, no physics estimate',population=2048,seed=6199999,seconds=elapsed,rss_mib=rss,cache_error=error,postconditions=True,forecast_total=1682.1285463124077+elapsed,forecast_max_cell=101.9471846249944,forecast_pass=1682.1285463124077+elapsed<=2000,driver_sha256=hashlib.sha256((p/'driver.py').read_bytes()).hexdigest()),indent=2))
