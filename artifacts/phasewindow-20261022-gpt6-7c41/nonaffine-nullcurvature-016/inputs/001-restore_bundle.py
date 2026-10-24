#!/usr/bin/env python3
"""Restore exact UD016 39-file ZIP from its versioned GitHub base64 archive parts."""
import argparse,base64,hashlib,zipfile
from pathlib import Path
EXPECTED='e58aa2f25d9295c2fe16bc9cdb50b87a170673551321e0382a7646b9d2c4dcee'
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--parts',type=Path,default=Path('.'))
 p.add_argument('--out',type=Path,default=Path('UD_3D_Nonaffine_NullCurvature_016.zip'))
 a=p.parse_args()
 files=sorted(a.parts.glob('part-*.b64'))
 assert len(files)>=2,('missing archive parts',files)
 s=''.join(f.read_text(encoding='ascii').strip() for f in files)
 data=base64.b64decode(s,validate=True)
 assert hashlib.sha256(data).hexdigest()==EXPECTED,'Original ZIP SHA256 mismatch'
 a.out.write_bytes(data)
 with zipfile.ZipFile(a.out) as z:
  assert z.testzip() is None,'ZIP member checksum failure'
  print(f'PASS archive restored: {a.out}, {len(z.namelist())} members, {len(data)} bytes, SHA256 {EXPECTED}')
