"""Inverse-designed positive local penalty search using this task's own Floquet code."""
import json
from pathlib import Path
from itertools import combinations
import numpy as np
from transverse_stability import setup,monodromy

def run():
    jn,bs,N,J,hessian=setup()
    cells=[s for k in range(1,5) for s in combinations(range(4),k)]
    inactive=[0,3]+[i for i,s in enumerate(cells) if len(s)==3]
    D=np.zeros((15,15));D[inactive,inactive]=1
    DN=N.T@D@N
    reports=[]
    for eta in (0.,.25,.5,1.,2.,4.,8.,16.,32.,64.):
        bb=[bs[0],bs[1]+eta*DN,bs[2]]
        row=[]
        for mu in (1/16,1.,4.):
            U=monodromy(mu/(2+mu),1024,jn,bb)
            row.append(float(np.max(np.abs(np.linalg.eigvals(U)))))
        reports.append({'eta':eta,'max_moduli_mu_1over16_1_4':row})
        print(reports[-1],flush=True)
    refined=[]
    eta=1.
    bb=[bs[0],bs[1]+eta*DN,bs[2]]
    for mu in (0.,1/64,1/16,1/4,1.,2.,4.,8.,16.,64.):
        rho=mu/(2+mu)
        U=monodromy(rho,2048,jn,bb);Uf=monodromy(rho,4096,jn,bb)
        eig,V=np.linalg.eig(Uf)
        refined.append({'mu':mu,'eta':eta,'max_multiplier_modulus':float(np.max(np.abs(eig))),
                        'min_multiplier_modulus':float(np.min(np.abs(eig))),
                        'step_doubling_matrix_error':float(np.linalg.norm(U-Uf,ord=2)),
                        'symplectic_residual':float(np.linalg.norm(Uf.T@jn@Uf-jn,ord=2)),
                        'eigenvector_condition':float(np.linalg.cond(V)),
                        'multipliers':[[float(z.real),float(z.imag)] for z in sorted(eig,key=lambda z:(z.real,z.imag))]})
    out={'numpy_version':np.__version__,'refined_eta1':refined,'evidence' :'NUMERICAL','family':'positive inactive-register incidence penalties, Bs->Bs+eta D6','grid':reports,'physical_promotion':0}
    Path(__file__).with_name('local_stabilization_results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':run()
