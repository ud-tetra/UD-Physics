"""Exact symmetry/coupling checks plus passive radial mechanical realization.

Uses the preserved exact icosahedral-cone constructor. No physical calibration.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import argparse
import csv
import importlib.util
import json
import math
import sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('ico_audit',ROOT/'experiments/icosahedral-cone/analyze.py')
ico=importlib.util.module_from_spec(spec);sys.modules[spec.name]=ico;spec.loader.exec_module(ico)


def symmetry_group(vertices,faces,simplices):
    """All120 exact isometries from images of one ordered boundary face."""
    source=[vertices[i] for i in faces[0]];denom=ico.det(*source)
    coeff=[]
    for v in vertices:
        coeff.append([ico.det(*[v if j==i else source[j] for j in range(3)])/denom for i in range(3)])
    lookup={tuple(v):i for i,v in enumerate(vertices)}
    offsets=np.cumsum([0]+list(map(len,simplices)))
    indices=[{s:offsets[k]+i for i,s in enumerate(level)} for k,level in enumerate(simplices)]
    group=[]
    for face in faces:
        for target in permutations(face):
            rays=[vertices[i] for i in target]
            p=[lookup[tuple(sum(rays[j][k]*co[j] for j in range(3)) for k in range(3))] for co in coeff]
            parity=(ico.det(*rays)/denom).sign()
            assert sorted(p)==list(range(13)) and p[0]==0
            dest=[];sign=[]
            for k,level in enumerate(simplices):
                for s in level:
                    mapped=[p[i] for i in s]
                    odd=sum(mapped[i]>mapped[j] for i in range(len(s)) for j in range(i+1,len(s)))%2
                    dest.append(indices[k][tuple(sorted(mapped))]);sign.append((-1)**odd)
            group.append((p,parity,np.array(dest),np.array(sign)))
    assert len({tuple(p) for p,_,_,_ in group})==120
    assert sum(e==1 for _,e,_,_ in group)==60
    return group


def main(out):
    out.mkdir(parents=True,exist_ok=True)
    vertices,edges,faces,cells,simplices,B=ico.construction()
    f=list(map(len,simplices));offsets=np.cumsum([0]+f);n=sum(f)
    boundary=np.zeros((n,n),dtype=np.int64)
    for k,b in enumerate(B,1):boundary[offsets[k-1]:offsets[k],offsets[k]:offsets[k+1]]=b
    A=boundary.T-boundary
    assert not np.any((A@A)[offsets[2]:,:offsets[1]])
    e=np.zeros(n,dtype=np.int64);e[0]=1
    Z=np.zeros(n,dtype=np.int64);Z[offsets[3]:]=[ico.det(*[vertices[i] for i in c[1:]]).sign() for c in cells]
    S=boundary@Z
    W=np.outer(Z,e)-np.outer(e,Z)
    assert np.array_equal(W.T,-W) and np.count_nonzero(W)==40
    # The added off-grade interaction has support only on incident centre/cell pairs.
    for i,j in zip(*np.nonzero(W)):
        assert (i==0 and j>=offsets[3]) or (j==0 and i>=offsets[3])
    group=symmetry_group(vertices,faces,simplices)
    inversion=None
    for p,parity,dest,sign in group:
        left=np.empty_like(A);left[dest,:]=sign[:,None]*A
        right=A[:,dest]*sign[None,:]
        assert np.array_equal(left,right)
        rz=np.empty_like(Z);rz[dest]=sign*Z
        rs=np.empty_like(S);rs[dest]=sign*S
        assert np.array_equal(rz,parity*Z) and np.array_equal(rs,parity*S)
        conjugated=np.empty_like(W);conjugated[np.ix_(dest,dest)]=sign[:,None]*W*sign[None,:]
        assert np.array_equal(conjugated,parity*W)
        if all(vertices[p[i]]==[-x for x in vertices[i]] for i in range(13)):inversion=(dest,sign)
    assert inversion is not None
    # Exact invariant5D basis [centre, uniform outer vertices, uniform rays,Z,S].
    U=np.zeros(n,dtype=np.int64);U[1:13]=1
    R=np.zeros(n,dtype=np.int64)
    for i,s in enumerate(simplices[1]):
        if 0 in s:R[offsets[1]+i]=1
    V=np.column_stack([e,U,R,Z,S]);metric=V.T@V
    assert np.array_equal(metric,np.diag([1,12,12,20,20]))
    chain_checks=[]
    t=np.linspace(0,100,4001);chain_curves=None
    for g in [F(0),F(1,4),F(1,2),F(1)]:
        M=np.array([[0,0,12,-20*g,0],[0,0,-1,0,0],[-1,1,0,0,0],[g,0,0,0,1],[0,0,0,-1,0]],dtype=object)
        full=A.astype(object)+g*W
        assert np.array_equal(full@V,V@M)
        assert not np.any(M.T@metric+metric@M)
        omega2=13+20*g*g
        assert np.array_equal(M@M@M[:,0],-omega2*M[:,0])
        I=np.eye(5,dtype=object)
        assert not np.any(M@(M@M+I)@(M@M+omega2*I))
        omega=math.sqrt(float(omega2));y=1-np.cos(omega*t)
        traj=np.column_stack([(1+(float(omega2)-1)*np.cos(omega*t))/float(omega2),
                              y/float(omega2),-np.sin(omega*t)/omega,
                              float(g)*np.sin(omega*t)/omega,-float(g)*y/float(omega2)])
        model_energy=np.sum(traj*traj*np.diag(metric),axis=1)
        residual=float(max(abs(model_energy-1)));assert residual<2e-14
        errors=[]
        root_metric=np.sqrt(np.diag(metric))
        normalized=np.array(M,dtype=float)*root_metric[:,None]/root_metric[None,:]
        assert np.max(abs(normalized+normalized.T))<2e-15
        for time in [.1,1.,5.]:
            exact=np.array([(1+(float(omega2)-1)*math.cos(omega*time))/float(omega2),
                            (1-math.cos(omega*time))/float(omega2),-math.sin(omega*time)/omega,
                            float(g)*math.sin(omega*time)/omega,-float(g)*(1-math.cos(omega*time))/float(omega2)])
            errors.append(float(max(abs(expm(normalized*time)[:,0]/root_metric-exact))))
        # Longer-time expm cross-check is floating point, separate from exact
        # invariant-space and Krylov identities above; report its actual error.
        assert max(errors)<1e-12
        maximum=20*g*g/(12+20*g*g)
        chain_checks.append({'g':str(g),'heart_active_squared_frequency':str(omega2),
                             'maximum_cell_plus_surface_model_energy_fraction_exact':str(maximum),
                             'maximum_cell_plus_surface_model_energy_fraction':float(maximum),
                             'model_energy_residual':residual,'expm_check_error':max(errors)})
        if g==F(1,2):chain_curves=traj
    # Separate passive mechanical model:13 strains plus13 velocities.
    # Ordinary edge extension energy uses actual spatial distances.
    pos=np.array([[float(x) for x in v] for v in vertices[1:]])
    edge=np.array(edges)-1;g=1.;k=2/5;a0=.1
    def energy_and_force(x):
        a=x[0];q=x[1:];scaled=(1+q[:,None])*pos
        delta=scaled[edge[:,0]]-scaled[edge[:,1]]
        length=np.linalg.norm(delta,axis=1)
        assert min(length)>1e-9
        extension=length-1
        force=np.r_[a+g*np.sum(a-q),q+g*(q-a)]
        direction=delta/length[:,None]
        for j,(i,l) in enumerate(edge):
            force[1+i]+=k*extension[j]*np.dot(direction[j],pos[i])
            force[1+l]-=k*extension[j]*np.dot(direction[j],pos[l])
        potential=(a*a+np.sum(q*q)+g*np.sum((q-a)**2)+k*np.sum(extension*extension))/2
        return potential,force
    # Exact rational tangent stiffness, including ordinary edge signless Laplacian.
    Q=np.zeros((12,12),dtype=np.int64)
    for i,j in edge:Q[i,i]+=1;Q[j,j]+=1;Q[i,j]+=1;Q[j,i]+=1
    K=np.zeros((13,13),dtype=object);K[0,0]=13
    K[0,1:]=-1;K[1:,0]=-1
    K[1:,1:]=2*np.eye(12,dtype=object)+F(1,10)*Q
    for p,_,_,_ in group:
        assert np.array_equal(K[np.ix_(p,p)],K)
    collective=np.zeros((13,2),dtype=int);collective[0,0]=1;collective[1:,1]=1
    reduced=np.array([[13,-12],[-1,3]],dtype=object)
    assert np.array_equal(K@collective,collective@reduced)
    assert not np.any(reduced@reduced-16*reduced+27*np.eye(2,dtype=object))
    # Exact all-mode tangent certificate in the integer-scaled matrix10K.
    tenK=np.array(10*K,dtype=np.int64).astype(object);eye13=np.eye(13,dtype=object)
    assert not np.any((tenK@tenK-160*tenK+2700*eye13)@(tenK-24*eye13)@(tenK@tenK-50*tenK+620*eye13))
    col=[2,160];contrast=[2,50]
    for j in range(2,5):
        col.append(160*col[-1]-2700*col[-2])
        contrast.append(50*contrast[-1]-620*contrast[-2])
    power=eye13
    for j in range(5):
        assert int(np.trace(power))==col[j]+5*24**j+3*contrast[j]
        power=power@tenK
    # Actual nonlinear forces retain the uniform manifold, verified at several strains.
    manifold_errors=[]
    for a,b in [(.1,.02),(-.05,.04),(.2,-.1)]:
        _,force=energy_and_force(np.r_[a,np.full(12,b)])
        expected=np.r_[13*a-12*b,np.full(12,3*b-a)]
        manifold_errors.append(float(max(abs(force-expected))))
    assert max(manifold_errors)<2e-15
    def ode(time,state):
        _,force=energy_and_force(state[:13]);return np.r_[state[13:],-force]
    initial=np.r_[a0,np.zeros(25)]
    solution=solve_ivp(ode,(0,100),initial,t_eval=t,method='DOP853',rtol=1e-11,atol=1e-13)
    assert solution.success
    x=solution.y[:13].T;vel=solution.y[13:].T
    lamlo=8-math.sqrt(37);lamhi=8+math.sqrt(37)
    b=a0*(np.cos(math.sqrt(lamlo)*t)-np.cos(math.sqrt(lamhi)*t))/(2*math.sqrt(37))
    ah=a0*((3-lamlo)*np.cos(math.sqrt(lamlo)*t)+(lamhi-3)*np.cos(math.sqrt(lamhi)*t))/(2*math.sqrt(37))
    state_error=float(max(np.max(abs(x[:,1:]-b[:,None])),np.max(abs(x[:,0]-ah))))
    assert state_error<3e-10 and np.min(x[:,1:])>-1
    E=np.array([energy_and_force(q)[0] for q in x])+np.sum(vel*vel,axis=1)/2
    energy_error=float(max(abs(E-E[0]))/E[0]);assert energy_error<3e-9
    # Explicit per-cell determinant readout under radial guides.
    volumes=np.column_stack([np.prod(1+x[:,np.array(face)],axis=1) for face in faces])
    volume_error=float(np.max(abs(volumes-(1+b[:,None])**3)));assert volume_error<1e-9
    nonlinear_symmetry=[]
    sample=np.r_[.07,np.linspace(-.03,.04,12)]
    U0,F0=energy_and_force(sample)
    numerical_gradient=[]
    for j in range(13):
        delta=np.zeros(13);delta[j]=1e-6
        numerical_gradient.append((energy_and_force(sample+delta)[0]-energy_and_force(sample-delta)[0])/(2e-6))
    gradient_error=float(max(abs(np.array(numerical_gradient)-F0)))
    assert gradient_error<1e-9
    for p,_,_,_ in group:
        permuted=np.empty(13);permuted[p]=sample
        up,fp=energy_and_force(permuted);expected=np.empty(13);expected[p]=F0
        nonlinear_symmetry.append(max(abs(up-U0),float(max(abs(fp-expected)))))
    assert max(nonlinear_symmetry)<3e-15
    result={'status':'PASS','symmetry':{'exact_isometries':120,'proper':60,'improper':60,
        'centre_parity':1,'oriented_cell_and_surface_parity':-1,
        'obstruction':'Any fixed real linear generator commuting with inversion keeps an even centre seed orthogonal to odd Z/S. Nonlinear inversion-equivariant unique flows have the same invariant-even-state property.',
        'W_transformation':'R W R^T=det(R)*W; simplex-local W has40 directed nonzeros'},
        'chain_coupling':{'definition':'A_g=A+g*(Z e0^T-e0 Z^T)','symmetry':'proper rotations; a nonzero fixed g selects orientation',
                         'invariant_basis_metric':[1,12,12,20,20],'heart_cyclic_dimension':3,
                         'full_reduced_characteristic':'z*(z^2+1)*(z^2+13+20g^2)',
                         'checks':chain_checks},
        'mechanical_model':{'status':'separate assumed scalar-strain realization; not a native chain derivation',
            'parameters':{'g':g,'k_edge':'2/5','Kh':1,'Ks':1,'Ih':1,'mi':1,'a0':a0},
            'collective_squared_frequencies':['8-sqrt(37)','8+sqrt(37)'],
            'contrast_squared_frequencies':[['5/2-sqrt(5)/10',3],['12/5',5],['5/2+sqrt(5)/10',3]],
            'frequency_numeric':[math.sqrt(lamlo),math.sqrt(lamhi)],
            'breathing_bound_abs':a0/math.sqrt(37),
            'volume_readout':'V_C/V_C0=product_(i in outer face)(1+q_i); uniform=(1+b)^3',
            'maximum_observed_fractional_volume_change':float(np.max(volumes)-1),
            'minimum_observed_fractional_volume_change':float(np.min(volumes)-1),
            'initial_model_energy':float(E[0]),'maximum_relative_energy_error':energy_error,
            'full_nonlinear_vs_analytic_state_error':state_error,'volume_readout_error':volume_error,
            'uniform_manifold_force_error':max(manifold_errors),
            'tangent_spectrum_certificate':'PASS exact integer annihilation and5 moments for10K',
            'potential_force_gradient_check_error':gradient_error,
            'nonlinear_full_group_equivariance_error':max(nonlinear_symmetry)},
        'numerics':{'numpy':np.__version__,'scipy':scipy.__version__,'dtype':'float64',
                    'method':'full nonlinear26-state DOP853 vs exact2-coordinate solution; matrix exponential vs chain analytic solution',
                    'rtol':1e-11,'atol':1e-13,'time_window':[0,100],'samples':4001},
        'limitations':['Energy is a declared positive model energy; no physical calibration or native source selection.',
                       'Strict oriented-chain reflection obstruction and scalar mechanical construction use different transformation laws/carriers.',
                       'Radial guides and scalar central actuator are assumed. Angular/shear modes, material/damping and apparatus implementation are OPEN.',
                       'No hypothesis of sustained autonomous breathing: prepared finite-energy motion only.']}
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    with (out/'trajectories.csv').open('w',newline='') as stream:
        writer=csv.writer(stream,lineterminator='\n')
        writer.writerow(['u','chain_g_half_centre','chain_g_half_cell','chain_g_half_surface','mechanical_centre_strain','mechanical_shell_strain','mechanical_total_volume_ratio','mechanical_energy_ratio'])
        for i,time in enumerate(t):writer.writerow([time,chain_curves[i,0],chain_curves[i,3],chain_curves[i,4],x[i,0],x[i,1],float(volumes[i].mean()),E[i]/E[0]])
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    main(parser.parse_args().out)
