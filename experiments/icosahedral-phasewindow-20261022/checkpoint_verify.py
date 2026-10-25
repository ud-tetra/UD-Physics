#!/usr/bin/env python3
"""Verify archived SHA-256 capture; replay exact gate and optional numerical smoke/full."""
import argparse,hashlib,json,tempfile,subprocess,os,sys,shutil
from pathlib import Path

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--smoke',action='store_true');ap.add_argument('--full',action='store_true');a=ap.parse_args()
 root=a.root.resolve();man=json.loads((root/'manifest.json').read_text());assert man['schema_version']==2
 for x in man['inputs']+man['files']:
  p=root/x['path'];b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['size_bytes'],p
 print('PASS SHA-256',len(man['inputs']),'inputs',len(man['files']),'outputs')
 with tempfile.TemporaryDirectory() as td:
  work=Path(td)
  for x in man['inputs']:shutil.copyfile(root/x['path'],work/x['name'])
  env=dict(os.environ,OPENBLAS_NUM_THREADS='1')
  def cmd(c):
   p=subprocess.run([sys.executable]+c,cwd=work,env=env,capture_output=True,text=True,check=True)
   print(p.stdout[-1200:])
  cmd(['exact_gain_gate.py','--csv',str(root/'files'/'sampled_operator_gains_4001.csv'),'--out',str(work/'gate.json')])
  assert (work/'gate.json').read_bytes()==(root/'files'/'exact_conditional_gate_result.json').read_bytes()
  print('PASS exact gate byte replay')
  if a.smoke or a.full:
   T=100 if a.full else 6
   cmd(['forward_fundamental.py','--T',str(T),'--h','.025' if a.full else '.05', '--rtol','1e-11' if a.full else '1e-9', '--sample','.025' if a.full else '.05','--out',str(work/'numerical.json')])
   got=json.loads((work/'numerical.json').read_text());expect=json.loads((root/'files'/'numerical_summary_024.json').read_text())
   if a.full:
    for key in ('g','v','w'):
     err=abs(got['peak_'+key][0]-expect['peaks'][key][0]);assert err<2e-9, (key,err)
   else:
    assert len(got['nodes'])==121
    assert got['peak_g'][0]<1e-4 and got['peak_v'][0]<.00065
   print('PASS', 'full' if a.full else 'smoke', 'replay')
if __name__=='__main__':main()
