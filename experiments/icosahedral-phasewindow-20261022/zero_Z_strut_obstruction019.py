#!/usr/bin/env python3
"""Exact energy-only counterexample to strut positivity even with Z=0.

Not a time-reachable trajectory, not part of symmetric housing initial family.
"""
import argparse,json
from fractions import Fraction as Q
from pathlib import Path
BETA=Q(1,200)
# R²=(5+sqrt5)/8 >9/10; k_h=40 beta/R²
# One housing moved from edge midpoint toward an endpoint by
# displacement (1-epsilon)*(v_i-v_j)/2. One strut length=epsilon/2.
# With shell at exact reference, alpha=z=v=0, only mount energy remains:
# U= k_h*(1-epsilon)²/8 = (1-epsilon)²/(40 R²).
# Because R²>9/10, U< (1-epsilon)² /36 <=1/36 <13/200,
# so it lies in the pulse energy sublevel with Z=0 and arbitrary tiny strut.
assert Q(1,36)<Q(13,200)
assert Q(5) > Q(11,5)**2 and Q(5,8)+Q(1,8)*Q(11,5) == Q(9,10)  # sqrt5>11/5
out={
 'status':'PASS','evidence':'EXACT / CONDITIONAL / NEGATIVE CONTROL',
 'shell_nonaffine_norm':'0',
 'static_family':'X_i=v_i, alpha=z=v=0; one housing H_e=m_e+(1-epsilon)(v_i-m_e); others at midpoints',
 'strut_length':'epsilon/2',
 'mount_energy':'(1-epsilon)^2/(40*R2), R2=(5+sqrt5)/8',
 'strict_energy_upper':'1/36 <13/200',
 'logic':'Even perfect shell-affine readout Z=0 plus energy <=pulse does not ensure any time-uniform strut lower bound. These are static inadmissible-to-reach counterexamples, not reachable pulse trajectories.'
}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path);a=p.parse_args();raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
 if a.out:a.out.write_text(raw)
 print('PASS: exact zero-Z energy-only strut obstruction');print(raw)