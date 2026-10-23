"""Exact conditional local reservoir transfer and reset accounting.

Standard-library rational matrices; no physical data or numerical hbar input.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import argparse, importlib.util, json

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('prior', ROOT/'experiments/action-normalization-audit/audit.py')
prior = importlib.util.module_from_spec(spec); spec.loader.exec_module(prior)
eye, zero, tr, add, scale, mm, mv, dot, rank = (getattr(prior, k) for k in ['eye','zero','tr','add','scale','mm','mv','dot','rank'])


def save(p, x):
    p.write_text(json.dumps(x, indent=2)+'\n')


def rotation(c, s):
    assert c*c+s*s == 1
    return [[c, -s], [s, c]]


def cross(x, y):
    return x[0]*y[1]-x[1]*y[0]


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    simplices = [s for k in range(1,5) for s in combinations(range(4),k)]
    ix = {s:i for i,s in enumerate(simplices)}; d = zero(15)
    for s in simplices:
        if len(s)>1:
            for j in range(len(s)):
                d[ix[s[:j]+s[j+1:]]][ix[s]] = F((-1)**j)
    A = add(d, scale(tr(d),-1)); J = scale(A,F(1,2)); P = scale(mm(A,A),F(-1,4))
    e = [F(0)]*15; e[ix[(0,1,2,3)]]=F(1); f = mv(J,e)
    E = [[a,b] for a,b in zip(e,f)]; j2 = [[F(0),F(-1)],[F(1),F(0)]]
    assert mm(tr(E),E)==eye(2) and mm(A,E)==scale(mm(E,j2),2)
    Q = mm(E,tr(E)); assert rank(Q)==2 and rank(add(P,scale(Q,-1)))==12
    sign_projector=zero(15); symmetry_cases=0
    for perm in permutations(range(4)):
        rho=zero(15)
        sign=F((-1)**sum(perm[i]>perm[k] for i in range(4) for k in range(i+1,4)))
        for col,s in enumerate(simplices):
            mapped=tuple(perm[v] for v in s)
            orientation=(-1)**sum(mapped[i]>mapped[k] for i in range(len(s)) for k in range(i+1,len(s)))
            rho[ix[tuple(sorted(mapped))]][col]=F(orientation)
        assert mm(rho,A)==mm(A,rho) and mm(rho,E)==scale(E,sign)
        sign_projector=add(sign_projector,scale(rho,sign/F(24)))
        symmetry_cases+=1
    assert sign_projector==Q
    local_support = [list(s) for s,row in zip(simplices,E) if any(row)]
    assert len(local_support)==5 and all(len(s)>=3 for s in local_support)
    JJ = zero(17); PP = zero(17); QQ = zero(17); readout = zero(17)
    for i in range(15):
        for k in range(15):
            JJ[i][k]=J[i][k]; PP[i][k]=P[i][k]; QQ[i][k]=Q[i][k]; readout[i][k]=Q[i][k]
    for i in range(2):
        for k in range(2):JJ[15+i][15+k]=j2[i][k]
        PP[15+i][15+i]=QQ[15+i][15+i]=F(1)
    assert mm(JJ,JJ)==scale(PP,-1) and rank(PP)==16
    assert mm(JJ,readout)==mm(readout,JJ)
    spectra=[]
    for g in [F(1,3),F(1,2),F(1),F(3,2)]:
        G=zero(17)
        for i in range(15):
            for k in range(15):G[i][k]=A[i][k]
            for k in range(2):G[i][15+k]=g*E[i][k]; G[15+k][i]=-g*E[i][k]
        for i in range(2):
            for k in range(2):G[15+i][15+k]=2*j2[i][k]
        assert tr(G)==scale(G,-1) and mm(JJ,G)==mm(G,JJ)
        K=scale(mm(JJ,G),-1); assert tr(K)==K and rank(K)==16
        C=add(K,scale(PP,-2)); assert mm(C,C)==scale(QQ,g*g)
        for sign in [-1,1]:
            projector=scale(add(QQ,scale(C,F(sign)/g)),F(1,2))
            assert rank(projector)==2 and mm(projector,projector)==projector
            assert mm(K,projector)==scale(projector,2+sign*g)
        rest=add(PP,scale(QQ,-1)); assert rank(rest)==12 and mm(K,rest)==scale(rest,2)
        assert ((1+g/2)-(1-g/2))/((2+g)-(2-g)) == F(1,2)
        assert mm(G,readout)!=mm(readout,G)
        # Rational instantaneous states test support,energy and coupling current.
        for seed in range(1,4):
            x=mv(P,[F((seed*k)%7-3,11) for k in range(1,16)])
            y=[F(seed,5),F(2-seed,7)]; z=x+y; zd=mv(G,z)
            r=mv(tr(E),x); rd=mv(tr(E),zd[:15]); yd=zd[15:]
            N=dot(x,x)+dot(y,y); D=cross(r,y)
            assert dot(z,zd)==0
            assert 2*dot(x,zd[:15])==2*g*dot(r,y)
            assert 2*dot(y,yd)==-2*g*dot(r,y)
            assert cross(rd,y)+cross(r,yd)==0
            assert dot(z,mv(K,z))/2==N+g*D
            assert dot(zd,mv(K,z))==0
        spectra.append({'g':str(g),'joint_real_dimension':17,'active_real_dimension':16,
          'coupled_frequencies':[str(2-g),str(2+g)],'unaddressed_frequency':'2 with6complex modes',
          'harmonic_dimension':1,'energy_lower_factor':str(1-g/2),
          'normalized_energy_gap_over_native_frequency_gap':'1/2',
          'characteristic_polynomial':'lambda*(lambda^2+4)^6*(lambda^2+(2-g)^2)*(lambda^2+(2+g)^2)'})
    save(out/'local_generator.json',{'local_target_simplices':local_support,'E_columns':[[str(v) for v in e],[str(v) for v in f]],
         'generator':'[[A,gE],[-gE^T,2j]]','Hamiltonian':'H=||x||^2+||y||^2+g*cross(E^T*x,y) on active target',
         'general_positive_energy_scope':'0<g<2','spectral_cases':spectra,
         'S4_permutations_verified':symmetry_cases,'S4_sign_projector_equals_target_plane_projector':True,
         'source_symmetry_assumption':'Both source coordinates transform by the S4 sign representation. Equivariance then restricts coupling to this rank2 plane.',
         'remaining_coupling_choices':'Complex-compatible port map E*(alpha*I+beta*j);symmetry doesnot select its magnitude,source phase orincoming support. Audit choosesbeta0,alpha=g.',
         'Born_compatible_target_plane_projector_commutes_with_joint_J':True,
         'scope':'Added resonant reservoir and local port;not derived from original incidence complex or physical apparatus.'})

    phases=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1)),
            (F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(-3,5),F(4,5)),(F(-5,13),F(12,13))]
    inputs=[([F(0),F(0)],[F(3,5),F(4,5)]),([F(2),F(-1)],[F(3,5),F(4,5)]),
            ([F(1,3),F(2,7)],[F(2,5),F(-3,11)])]
    cases=0; swaps=[]
    for c,s in phases:
        R=rotation(c,s)
        for C,S in phases:
            for x0,y0 in inputs:
                x=mv(R,[C*a+S*b for a,b in zip(x0,y0)])
                y=mv(R,[-S*a+C*b for a,b in zip(x0,y0)])
                assert dot(x,x)+dot(y,y)==dot(x0,x0)+dot(y0,y0)
                assert cross(x,y)==cross(x0,y0)
                assert dot(x,x)==C*C*dot(x0,x0)+S*S*dot(y0,y0)+2*C*S*dot(x0,y0)
                if C==0 and S==1:
                    assert x==mv(R,y0) and y==[-v for v in mv(R,x0)]
                    swaps.append({'phase_cos':str(c),'phase_sin':str(s),'old_target':[str(v) for v in x0],
                                  'input_source':[str(v) for v in y0],'prepared_target':[str(v) for v in x],
                                  'outgoing_old_state':[str(v) for v in y]})
                cases+=1
    # A spectator edge stays occupied; only the top-cell/face plane is reset.
    spectator=[F(0)]*15; spectator[ix[(0,1)]]=F(1)
    assert mv(Q,spectator)==[F(0)]*15 and mv(P,spectator)==spectator
    occupied_error_cases=0
    for C,S in phases:
        for R0 in [F(1,2),F(1),F(2)]:
            for sign in [-1,1]:
                support=(C*sign*R0+S)**2
                assert (abs(C)*R0-abs(S))**2 <= support <= (abs(C)*R0+abs(S))**2
                assert abs(support-1) <= C*C*abs(R0*R0-1)+2*abs(C*S)*R0
                occupied_error_cases+=1
    save(out/'transfer_reset.json',{'general_transfer_formula':'r=R(2s)*(cosTheta*r0+sinTheta*y0);y=R(2s)*(-sinTheta*r0+cosTheta*y0)',
          'pulse_area':'Theta=integral g(s)ds','exact_rational_state_cases':cases,'swap_cases':swaps,
          'unit_preparation':'AtTheta=pi/2,an incoming unit source prepares target-plane support1 for arbitrary old addressed state.',
          'outgoing_record':'Outgoing reservoir contains the old addressed state up to a known rotation/sign;no erasure.',
          'spectator_counterexample':'Initial unit edge plus incoming unit source leaves full target support2;whole-carrier reset not claimed.',
          'retention':'Constant coupling returns target support to0 from an empty target byTheta=pi;isolation gate required.',
          'area_error_bound':'For empty addressed target and source supportN,Theta=pi/2+epsilon gives targetN*cos(epsilon)^2;loss<=N*epsilon^2.',
          'occupied_target_error_cases':occupied_error_cases,
          'occupied_target_bound':'For unit incoming source and old addressed normR,abs(a_final-1)<=cos(Theta)^2*abs(R^2-1)+2*abs(cosTheta*sinTheta)*R. Error can be first order near a swap;no uniform bound for unbounded old R.'})

    detuning=[]
    for g in [F(1,2),F(1),F(3,2)]:
        for delta in [F(0),F(1,2),F(1),F(2)]:
            B=zero(4)
            for i in range(2):
                for k in range(2):B[i][k]=-delta*j2[i][k]/2;B[2+i][2+k]=delta*j2[i][k]/2
                B[i][2+i]=g;B[2+i][i]=-g
            k2=g*g+delta*delta/4
            assert mm(B,B)==scale(eye(4),-k2)
            efficiency=g*g/k2;assert 0<efficiency<=1 and (efficiency==1)==(delta==0)
            detuning.append({'g':str(g),'source_frequency_offset_delta':str(delta),'kappa_squared':str(k2),'maximum_support_fraction':str(efficiency)})
    save(out/'detuning.json',{'cases':detuning,
         'formula':'max addressed support/incoming support = g^2/(g^2+delta^2/4)',
         'scope':'Empty target,resonant-plane model with constant g and constant bare-frequency detuning;maximum over time,not a fixed-pulse guarantee or arbitrary-control no-go.'})

    cycles=[]
    for old in [F(0),F(1,4),F(1),F(4)]:
        incoming=F(1);outgoing=old;target_gain=1-old
        assert target_gain==incoming-outgoing
        cycles.append({'old_target_support':str(old),'incoming_source_support':'1','outgoing_source_support':str(outgoing),
                       'prepared_target_support':'1','net_input_energy_over_Eunit':str(target_gain),
                       'source_refresh_energy_change_over_Eunit':str(1-old)})
    save(out/'energy_control.json',{'cycle_cases':cycles,'isolated_unit_energy':'Eunit=A0/tau0 only under declared physical energy map',
        'pulse_work':'H(s)=N+g(s)D;D constant;dH/ds=g_prime(s)*D. Pulse starting/endingg0 has zero net ideal system work.',
        'empty_target':'D=0,so ideal modeled gate work0;controller/timing/reset hardware costs are not determined by this model.',
        'reset_obstruction':'An invertible joint swap cannot erase arbitrary old target states while returning every auxiliary to the same fixed state. Outgoing record or another changed degree of freedom is necessary.',
        'resources':['incoming normalized reservoir preparation','matched reservoir dynamics','coupling envelope and pulse-area clock','outgoing old-state carrier','isolation/retention gate','reservoir refresh and target removal for repeated empty-target cycles'],
        'universal_unit':'Rescaling physical A0 while retaining the native generator/support protocol changes all dimensional energies/actions without changing these native readouts.'})
    # Conditional energy operator is K/2; Schr law would scale native G byeta/2.
    eta_cases=[]
    for eta in [F(1),F(2),F(3),F(6),F(10)]:
        eta_cases.append({'eta':str(eta),'native_generator_multiplier':str(eta/2),'small_pulse_population_curvature_ratio':str(eta*eta/4)})
    aliases=[2+4*n for n in range(6)];assert all((eta-2)%4==0 for eta in aliases)
    save(out/'conditional_readout.json',{'native_target_population':'sin(Theta)^2 for empty target,unit incoming source',
        'readout_map':'Target-plane projector commutes with joint complex structure;coupling mixes source/target populations. This is invariant under overall joint phase.',
        'hypothetical_quantum_energy_map':'M=K/2,physical energyoperator=(A0/tau0)*M;Schrodinger equation with hbar is an extra correspondence.',
        'conditional_Born_population':'sin((eta_A/2)*Theta)^2;eta_A=2 matches the declared native generator',
        'eta_examples':eta_cases,'single_full_transfer_endpoint_positive_eta_aliases':aliases,
        'scope':'No physical source coupling,energy/readout calibration or quantum identity established;classical coherent oscillators share the native transfer curve. Unknown coupling scale remains confounded with eta.'})
    results={'status':'EXACT_CONDITIONAL_SOURCE_RESERVOIR_PASS','joint_real_dimension':17,'active_complex_dimension_under_added_J':8,
       'local_port_target_support':'one topcell anditsfourboundaryfaces','rational_generator_cases':len(spectra),'S4_permutation_cases':symmetry_cases,
       'rational_transfer_cases':cases,'exact_swap_cases':len(swaps),'occupied_target_error_cases':occupied_error_cases,'detuning_cases':len(detuning),'cycle_budgets':len(cycles),
       'main_finding':'Matched reservoir pulse swaps one active target-plane state with the source;old state exits in the reservoir. Isolation and fresh-source/reset accounting remain necessary.',
       'new_observable':'Invariant target-plane population varies under added coupling,unlike the prior isolated scalar phase.',
       'source_unit':'Incoming unit support is assumed/prepared,not derived or physically calibrated.',
       'physical_action_unit':'OPEN','empirical_status':'UNSCORED','independent_review':'NOT_PERFORMED','physical_promotion':0}
    save(out/'results.json',results);print(json.dumps(results,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
