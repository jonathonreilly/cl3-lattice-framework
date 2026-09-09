import json,time,resource
from pathlib import Path
from kernel import physical_geometry,vacuum_kernel,literal_kernel,require

PAIRS=[((0,1),(2,3)),((0,1),(2,4)),((0,2),(4,5)),((0,2),(1,3)),((0,2),(1,4))]
TIMES=[(0.,0.),(1/128,1/64),(1/64,1/64)]
def run(out):
    out.mkdir(); rows=[]; stage='initial'; start=time.monotonic(); geometry=[]
    def save(name,payload): (out/name).write_text(json.dumps(payload,indent=2)+'\n')
    save('PARTIAL.json',{'stage':stage,'rows':rows})
    try:
        for case,pair in enumerate(PAIRS):
            stage=f'geometry-{case}'; save('PARTIAL.json',{'stage':stage,'rows':rows})
            t0=time.monotonic(); ks,js,v,e0,meta=physical_geometry(pair)
            meta.update(case=case,seconds=time.monotonic()-t0); geometry.append(meta)
            a,c=ks; ja,jc=js
            for ti,(t,s) in enumerate(TIMES):
                fixtures=[('overlap',[(c,t),(a,s)],[]),
                  ('C_insertion',[(c,t/2),(c,t/2),(a,s)],[(0,jc),(1,v)]),
                  ('A_insertion',[(c,t),(a,s/2),(a,s/2)],[(0,v),(1,ja)])]
                for name,segments,ins in fixtures:
                    stage=f'{case}-{ti}-{name}'; save('PARTIAL.json',{'stage':stage,'rows':rows,'geometry':geometry})
                    t0=time.monotonic(); val,diag=vacuum_kernel(segments,ins,e0); gaussian=time.monotonic()-t0
                    t0=time.monotonic(); ref=literal_kernel(segments,ins,e0); literal=time.monotonic()-t0
                    err=abs(val-ref); row={'case':case,'time_index':ti,'name':name,'times':[t,s],
                      'gaussian':[val.real,val.imag],'literal':[ref.real,ref.imag],
                      'absolute_error':err,'gaussian_seconds':gaussian,'literal_seconds':literal,**diag}
                    rows.append(row); save('PARTIAL.json',{'stage':stage,'rows':rows,'geometry':geometry})
                    require(err<=2e-10*(1+abs(ref)),'Gaussian/Fock comparison')
                    require(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=384*1048576,'worker RSS')
        require(len(rows)==45,'fixed coverage')
        save('RESULT.json',{'status':'COMPLETE','purpose':'fixed finite normalization and cost only',
          'rows':rows,'geometry':geometry,'seconds_including_row_io':time.monotonic()-start,
          'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'infinite_node_value_computed':False,'interval_certificate':False})
    except BaseException as exc:
        save('FAILURE.json',{'stage':stage,'error':repr(exc),'rows':rows,'geometry':geometry,'seconds':time.monotonic()-start});raise
