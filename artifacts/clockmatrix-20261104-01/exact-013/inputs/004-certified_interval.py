"""Exact rational margins for an explicit normal-stability interval."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from stabilization_exact import mm,tr,sc,add,eye,definite_pivots

def model_matrices():
    cells=[s for k in range(1,5) for s in combinations(range(4),k)];ix={s:i for i,s in enumerate(cells)};n=15
    d=[[F(0)]*n for _ in range(n)]
    for s in cells:
        if len(s)>1:
            for k in range(len(s)):d[ix[s[:k]+s[k+1:]]][ix[s]]=F((-1)**k)
    J=[[(d[i][j]-d[j][i])/2 for j in range(n)] for i in range(n)]
    v=[F(int(i==1)-int(i==2)) for i in range(n)];h=[r[1]-r[2] for r in J];z=[F(1,2)]*4+[F(0)]*11
    P=[[F(i==j)-z[i]*z[j]-(v[i]*v[j]+h[i]*h[j])/2 for j in range(n)] for i in range(n)]
    def Hess(q,p):
        B=[[F(0)]*n for _ in range(n)]
        for i in (1,2):B[i][i]=3*q*q+p*p
        for e in ((0,1),(0,2),(1,2),(1,3),(2,3)):B[ix[e]][ix[e]]=q*q+3*p*p
        for i,e,s in ((1,(0,1),-1),(1,(1,2),1),(1,(1,3),1),(2,(0,2),-1),(2,(1,2),-1),(2,(2,3),1)):B[i][ix[e]]=B[ix[e]][i]=s*q*p
        return B
    Bc=Hess(F(1),F(0));Bs=Hess(F(0),F(1));Bx=add(Hess(F(1),F(1)),sc(Bc,-1),sc(Bs,-1))
    for i in (0,3,10,11,12,13):Bs[i][i]+=1
    return J,P,Bc,Bs,Bx

def matrices():
    J,P,Bc,Bs,Bx=model_matrices()
    T=mm(mm(P,add(sc(add(mm(J,add(sc(Bc,3),Bs)),mm(add(Bc,sc(Bs,3)),J),mm(mm(J,Bx),J),Bx),F(1,8)),sc(J,-1))),P)
    return J,P,T

def run():
    J,P,T=matrices();Id=eye(15);T2=mm(T,T);a,b,c=F(19,256),F(35,64),F(3,64)
    # Real negative-signature spectral projector, excluding the three ambient zero modes.
    Pminus=sc(mm(mm(add(T2,sc(P,a)),add(T2,sc(P,c))),P),1/((a-b)*(c-b)))
    assert mm(Pminus,Pminus)==Pminus
    assert mm(T,Pminus)==mm(Pminus,T)
    K=sc(mm(J,T),-1);R=add(P,sc(Pminus,-2))
    G=add(mm(K,R),add(Id,sc(P,-1)))
    assert G==tr(G) and add(mm(tr(T),G),mm(G,T))==[[0]*15 for _ in range(15)]
    lo,hi=F(1,64),F(4)
    p1=definite_pivots(add(G,sc(Id,-lo)));p2=definite_pivots(add(sc(Id,hi),sc(G,-1)))
    assert all(x>0 for x in p1+p2)
    knorm=max(sum(abs(x) for x in row) for row in K);assert knorm<F(2)
    # Exact scalar margins in the contour/logarithm proof. pi<22/7 suffices.
    mu_max=F(1,2**30);rho_max=mu_max/2
    error=400*rho_max;deltaP=8192*error;deltaG=33000*error
    assert 5*F(22,7)*rho_max<F(1,8)
    assert 128*error<F(1,2) and deltaP<1
    assert deltaG<F(1,128)
    assert F(4)+F(1,128)<5 and 5*128<32**2
    # Frequency centers separated enough for radius1/8 contours around +-nu_b.
    assert b>F(7,10)**2 and b<F(3,4)**2
    assert a<F(3,10)**2 and c<F(1,4)**2
    assert F(7,10)-F(3,10)>F(1,4)
    # Nonlinear finite-readout gate: I1,lambda=mu, energies<=33/16.
    exponent=18*F(33,16)/128
    assert exponent==F(297,1024) and exponent<F(1,3)
    assert F(1)/(1-F(1,3))==F(3,2)
    phase=F(1,1000)
    assert F(9,32768)<phase-phase**3/6
    assert F(1,128)>2*phase
    assert 2+mu_max/2<F(33,16)
    return {'evidence':'EXACT_CONDITIONAL','mu_interval':{'lower_open':'0','upper_closed':str(mu_max)},
            'rho_upper':str(rho_max),'averaged_metric_bounds':[str(lo),str(hi)],
            'return_log_generator_error_bound':'400rho','projector_error_bound':'8192*(400rho)',
            'invariant_metric_error_bound':'33000*(400rho)',
            'worst_interval_metric_error':str(deltaG),'allowed_metric_error':'1/128',
            'actual_metric_bounds':['1/128','5'],'all_time_linear_normal_gain_bound':'64',
            'nonlinear_hessian_bound':'18||x||^2',
            'nonlinear_readout_gate':{'reference_I':'1','lambda':'mu in certified interval','reference_initial':'q1,p0',
                                     'initial_state_error_max':'1/4096','initial_both_energy_max':'33/16',
                                     'observation_horizon':'1/(128mu) native parameter units',
                                     'state_error_bound':'<3/8192','phase_error_bound':'<1/1000 rad',
                                     'phase_difference_from_lambda0_null':'1/128 rad'},
            'metric_margin_LDL_lower':list(map(str,p1)),'metric_margin_LDL_upper':list(map(str,p2)),
            'native_coefficient_selection':'OPEN','nonlinear_all_time_orbital_stability':'OPEN','physical_promotion':0}

if __name__=='__main__':
    r=run();Path(__file__).with_name('certified_interval_results.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps(r,indent=2,sort_keys=True))
