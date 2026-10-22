"""Negative result: conservative midpoint mounts add54undamped hidden modes."""
from itertools import permutations
from pathlib import Path
import argparse,json,csv
import numpy as np
from scipy.integrate import solve_ivp
from hardware import Hardware


def main(out):
    m=Hardware();lookup={tuple(e):i for i,e in enumerate(m.edges)};edge_set=set(lookup)
    cycle=next(p for p in permutations(range(1,13),4) if all(tuple(sorted((p[i],p[(i+1)%4]))) in edge_set for i in range(4)))
    N=np.zeros((12,30),dtype=int)
    for j,(a,b) in enumerate(m.edges):N[a-1,j]=N[b-1,j]=1
    q=np.zeros(30,dtype=int)
    for i in range(4):q[lookup[tuple(sorted((cycle[i],cycle[(i+1)%4])))]]=(-1)**i
    assert not np.any(N@q)
    # Connected+odd cycle forces ker(N^T)=0 exactly: v_i+v_j=0 on each edge,
    # an odd triangle implies v=0 there,and connectivity propagates zero.
    seen={1}
    while True:
        new=seen|{int(b) for a,b in m.edges if a in seen}|{int(a) for a,b in m.edges if b in seen}
        if new==seen:break
        seen=new
    assert len(seen)==12 and len(m.faces)>0
    amplitude=1e-4;direction=np.zeros((30,3));direction[:,0]=q
    initial=m.initial_augmented(0.);reference=initial.copy();initial[190:m.n]+=amplitude*direction.ravel()
    t=np.linspace(0,10,1001)
    sol=solve_ivp(m.ode,(0,10),initial,t_eval=t,method='DOP853',rtol=2e-12,atol=1e-15);assert sol.success
    Y=sol.y.T;prediction=reference[None,190:m.n]+amplitude*np.cos(m.omega_h*t)[:,None]*direction.ravel()[None,:]
    primary_error=float(np.max(abs(Y[:,:190]-reference[None,:190])));housing_error=float(np.max(abs(Y[:,190:m.n]-prediction)))
    E=np.array([m.energy(y) for y in Y]);relative=float(np.max(abs(E-E[0]))/E[0]);loss=float(max(Y[:,-1])/E[0])
    assert primary_error<1e-11 and housing_error<1e-11 and relative<1e-7 and loss<1e-14
    result={'status':'COUNTEREXAMPLE_VERIFIED','unsigned_incidence_rank':12,'housing_force_nullity_per_axis':18,'undamped_housing_modes':54,
            'exact_proof':'N is unsigned12x30 edgeincidence. Connectedgraphcontainsoddtriangles,so rankN12. UniformOmega andpositivehousingmasses give pure H-mode space ker((N*diag(m_h)) tensor I3),dimension3*(30-12)=54. Their point reactions cancel and Hddot=-Omega²H. Device/input losses cannot damp them when primarypoints remainstill.',
            'cycle_vertices':list(map(int,cycle)),'integer_edge_amplitudes':q.tolist(),'probe_amplitude':amplitude,'alpha_initial':0,'window':[0,10],
            'primary_plus_relative_coordinate_error':primary_error,'housing_vs_harmonic_error':housing_error,
            'relative_energy_variation':relative,'dissipated_energy_fraction_upper':loss,
            'conclusion':'Full housing-extended model is not asymptotically attracting in all transverse coordinates,even with positive device and input losses. The20jointcoherenceprobes startthesehousingmodesat zero anddo not test their decay.',
            'scope':'defined conservative midpoint-mount model withcommonOmega;one exact counterexample invalidates an unqualified all-mode decay extension. Prior190-coordinate theorem remains unchanged.'}
    out.mkdir(parents=True,exist_ok=True)
    with (out/'mount-mode-curve.csv').open('w',newline='') as f:
        writer=csv.writer(f,lineterminator='\n');writer.writerow(['u','measured_housing_mode','analytic_housing_mode','energy_ratio','dissipated_energy_ratio'])
        edge=int(np.flatnonzero(q)[0]);coef=int(q[edge])
        for i,time in enumerate(t):writer.writerow([time,(Y[i,190+3*edge]-reference[190+3*edge])/coef,amplitude*np.cos(m.omega_h*time),E[i]/E[0],Y[i,-1]/E[0]])
    (out/'mount-modes.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
