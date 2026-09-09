import subprocess,os,time,signal,pathlib,json
O=pathlib.Path(__file__).parent;t=time.monotonic();maximum=0;reason=None
with (O/'decoder_control.json').open('w') as out,(O/'decoder_control.stderr').open('w') as err:
 p=subprocess.Popen(['python3',str(O/'decoder_control.py')],stdout=out,stderr=err,start_new_session=True)
 while p.poll() is None:
  rows=subprocess.check_output(['ps','-axo','pgid=,rss='],text=True).splitlines();rss=sum(int(r.split()[1]) for r in rows if r.split() and int(r.split()[0])==p.pid);maximum=max(maximum,rss)
  if time.monotonic()-t>30 or rss>2*1024**2:reason='time or RSS limit';os.killpg(p.pid,signal.SIGKILL);break
  time.sleep(.05)
 rc=p.wait()
(O/'decoder_guard_receipt.json').write_text(json.dumps({'elapsed':time.monotonic()-t,'max_group_rss_kib':maximum,'returncode':rc,'termination':reason},indent=2))
print(rc)
