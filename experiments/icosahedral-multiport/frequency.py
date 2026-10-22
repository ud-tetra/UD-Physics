"""Finite auxiliary impedance; no instantaneous-dashpot substitution."""
from pathlib import Path
import argparse,csv,json
import numpy as np
from scipy.linalg import eigvals
from network import Network

def main(out):
    rows=[];records=[]
    for label,mu,k,g in [('A',.2,2.,.5),('B',2.,50.,5.)]:
        for om in np.logspace(-2,2,161):
            Z=(k/10)*(1j*mu*om+g)/(k-mu*om*om+1j*g*om)
            positive=k*k*g/(10*((k-mu*om*om)**2+g*g*om*om))
            assert abs(Z.real-positive)<1e-12 and positive>0
            rows.append({'phase':label,'omega':om,'real_force_over_velocity':Z.real,'imag_force_over_velocity':Z.imag,
                         'internal_stroke_gain':abs(k/(k-mu*om*om+1j*g*om))})
        m=Network(mu=mu,kappa=k,gamma=g);K,C,D=m.normal_matrices();n=len(K)
        poles=eigvals(np.block([[np.zeros_like(K),np.eye(n)],[-K,-C]]))
        records.append({'phase':label,'mu':mu,'kappa':k,'gamma':g,'minimum_full_transverse_decay':float(-max(poles.real))})
    with (out/'frequency.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    result={'status':'PASS','impedance_convention':'Z=force/relative_velocity;Smith2002 uses reciprocal naming',
            'Z_s':'(kappa/10)*(mu*s+gamma)/(mu*s^2+gamma*s+kappa)',
            'Re_Z_iomega':'kappa^2*gamma/[10*((kappa-mu*omega^2)^2+gamma^2*omega^2)]>0',
            'low_frequency':'Z=gamma/10+O(s);finite auxiliary dynamics retained',
            'records':records}
    (out/'frequency.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
