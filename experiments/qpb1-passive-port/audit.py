"""Exact ideal passive LC port and action-reference identifiability.

Synthetic rational parameters; no apparatus data or numerical hbar input.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, importlib.util, json

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('prior',ROOT/'experiments/action-normalization-audit/audit.py')
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
eye,zero,tr,add,scale,mm,mv,dot=(getattr(prior,k) for k in ['eye','zero','tr','add','scale','mm','mv','dot'])
j=[[F(0),F(-1)],[F(1),F(0)]]


def inv2(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det>0
    return scale([[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]],1/det)


def physical(Ci,Li):
    G=zero(4);H=zero(4)
    for a in range(2):
        for b in range(2):
            G[a][2+b]=Ci[a][b];G[2+a][b]=-Li[a][b]
            H[a][b]=Li[a][b];H[2+a][2+b]=Ci[a][b]
    return G,H


def native(g):
    G=zero(4)
    for a in range(2):
        for b in range(2):G[a][b]=G[2+a][2+b]=2*j[a][b]
        G[a][2+a]=g;G[2+a][a]=-g
    return G


def transform(Phi,Z):
    # Physical ordering(Phi1,Phi2,Q1,Q2);native(r1,r2,y1,y2),y=j*t.
    T=zero(4);T[0][0]=Phi;T[1][3]=Phi;T[2][1]=-Phi/Z;T[3][2]=Phi/Z
    return T


def save(path,x):path.write_text(json.dumps(x,indent=2)+'\n')


def main(out):
    out.mkdir(parents=True,exist_ok=True)
    cases=[];preps=[];gates=[];scales=[]
    tuples=[(F(1),F(1,2),F(1),F(1)),(F(3,2),F(1,3),F(5,4),F(2,3)),
       (F(7,5),F(2,7),F(11,9),F(13,7)),(F(2,3),F(3,5),F(4,3),F(5,6)),
       (F(5,4),F(7,8),F(2,5),F(3,2)),(F(9,7),F(1,9),F(7,3),F(4,5))]
    for C0,Cc,Z,Phi in tuples:
        C=[[C0+Cc,-Cc],[-Cc,C0+Cc]];L=scale(C,Z*Z);Ci,Li=inv2(C),inv2(L)
        assert Li==scale(Ci,1/(Z*Z)) and C0>0 and Cc>0
        w0=Ci[0][0]/Z;kappa=Ci[0][1]/Z;g=2*kappa/w0;tau=2/w0
        assert 0<g<2 and abs(L[0][1])<L[0][0]
        assert g==2*Cc/(C0+Cc)
        fast=1/(Z*C0);slow=1/(Z*(C0+2*Cc))
        assert fast==w0+kappa and slow==w0-kappa
        for v,w in [([F(1),F(1)],fast),([F(1),F(-1)],slow)]:
            assert mv(scale(Ci,1/Z),v)==[w*a for a in v]
        Gp,Hp=physical(Ci,Li);Gn=native(g);T=transform(Phi,Z)
        assert mm(Gp,T)==scale(mm(T,Gn),1/tau)
        J4=zero(4)
        for a in range(2):
            for b in range(2):J4[a][b]=J4[2+a][2+b]=j[a][b]
        K=scale(mm(J4,Gn),-1);Aref=Phi*Phi/Z;Eref=Aref/tau
        assert mm(mm(tr(T),Hp),T)==scale(K,Eref)
        theta=zero(4)
        for a in range(2):theta[a][2+a]=-1;theta[2+a][a]=1
        assert mm(mm(tr(T),theta),T)==scale(J4,-Aref)
        # Exact physical preparation:zero flux,Q1=0,Q2=Phi_ref/Z.
        Qin=[F(0),Phi/Z];Vin=mv(Ci,Qin)
        assert Vin==[kappa*Phi,w0*Phi] and Vin[0]/Vin[1]==g/2
        assert dot(Qin,Vin)/2==Eref
        prepared=mv(T,[F(0),F(0),F(1),F(0)])
        assert prepared==[F(0),F(0),F(0),Phi/Z]
        # Naive one-node voltage preparation is not empty at the addressed port.
        naiveQ=mv(C,[F(0),Vin[1]])
        assert naiveQ[0]!=0
        naive_pop=naiveQ[0]**2/dot(naiveQ,naiveQ)
        assert naive_pop==Cc*Cc/(Cc*Cc+(C0+Cc)**2)>0
        preps.append({'C0':str(C0),'Cc':str(Cc),'Z':str(Z),'Phi_ref':str(Phi),
             'required_voltages':[str(v) for v in Vin],'required_Q':[str(v) for v in Qin],
             'required_voltage_ratio':str(g/2),'naive_V1_zero_target_population':str(naive_pop)})
        # Fixed physical reference map retains amplitude support;new reference changes Aref.
        controls=[]
        for c in [F(1,2),F(1),F(2),F(3)]:
            q=[c*a for a in Qin];E=dot(q,mv(Ci,q))/2
            assert E==c*c*Eref and 2*E/w0==c*c*Aref
            assert E/(c*c)==Eref
            controls.append({'actual_voltage_ratio':str(c),'fixed_map_support':str(c*c),
              'physical_energy_ratio':str(c*c),'raw_twoE_over_w0':str(2*E/w0),
              'support_divided_action_reference':str(2*E/(w0*c*c)),
              'Aref_if_cPhi_is_chosen_as_new_unit_reference':str(c*c*Aref)})
        scales.append({'reference_Amap':str(Aref),'controls':controls})
        # Normalized normalmode energy gap andfrequency gap atcommon unit support.
        Efast=Aref*fast/2;Eslow=Aref*slow/2
        assert (Efast-Eslow)/(fast-slow)==Aref/2
        for mode,w in [([F(1),F(1)],fast),([F(1),F(-1)],slow)]:
            state=[Phi*mode[0],Phi*mode[1],F(0),F(0)]
            assert dot(state,mv(Hp,state))/(2*dot(mode,mode))==Aref*w/2
        # Changing only the capacitor coupler does not close the matched port.
        Coff=scale(eye(2),C0);Gbad,_=physical(inv2(Coff),Li)
        assert mm(Gbad,T)!=scale(mm(T,native(F(0))),1/tau)
        cases.append({'C_matrix':[[str(a) for a in row] for row in C],
          'L_matrix':[[str(a) for a in row] for row in L],
          'signed_mutual_inductance':str(L[0][1]),'magnetic_coupling_magnitude_ratio':str(abs(L[0][1])/L[0][0]),
          'omega_bar':str(w0),'kappa':str(kappa),'g_native':str(g),'tau0':str(tau),
          'frequencies':[str(fast),str(slow)],'Amap':str(Aref),'E_reference':str(Eref),
          'equal_unit_normalmode_energy_gap_over_frequency_gap':str(Aref/2),
          'physical_state_map':'Phi1=Phi_ref*r1,Phi2=Phi_ref*y2,Q1=-Phi_ref*r2/Z,Q2=Phi_ref*y1/Z'})

    # Family that preservesbarfrequency/impedance while changing native g.
    Z=F(5,3);w0=F(7,4);Phi=F(11,9);T=transform(Phi,Z)
    for g in [F(0),F(1,3),F(1),F(3,2)]:
        k=g*w0/2;C0=1/(Z*(w0+k));Cc=k/(Z*(w0*w0-k*k))
        C=[[C0+Cc,-Cc],[-Cc,C0+Cc]];L=scale(C,Z*Z)
        Gp,_=physical(inv2(C),inv2(L))
        assert mm(Gp,T)==scale(mm(T,native(g)),w0/2)
        gates.append({'g':str(g),'C0':str(C0),'Cc':str(Cc),
                      'coil_self_L':str(L[0][0]),'signed_M':str(L[0][1]),
                      'omega_bar':str(w0),'Z':str(Z)})
    # Restricted simple edge-inductor topology has the wrong off-diagonal sign
    # for thisfixed local impedance/quadrature dictionary (notallcanonicalmaps).
    C0,Cc,L0,Lc=F(1),F(1,2),F(2),F(3)
    C=[[C0+Cc,-Cc],[-Cc,C0+Cc]];Ci=inv2(C)
    edge_Linv=[[1/L0+1/Lc,-1/Lc],[-1/Lc,1/L0+1/Lc]]
    assert Ci[0][1]>0 and edge_Linv[0][1]<0

    # Dimensions in M,L,T,I. With no amplitude/charge/flux/energy primitive,
    # passive C,L,R,time all obey M+I/2=0;an action has M+I/2=1.
    dims={'capacitance':(-1,-2,4,2),'inductance':(1,2,-2,-2),
          'resistance':(1,2,-3,-2),'time':(0,0,1,0),
          'impedance':(1,2,-3,-2),'flux':(1,2,-2,-1),'action':(1,2,-1,0)}
    assert all(F(dims[k][0])+F(dims[k][3],2)==0 for k in ['capacitance','inductance','resistance','time'])
    assert F(dims['action'][0])+F(dims['action'][3],2)==1
    assert tuple(2*dims['flux'][i]-dims['impedance'][i] for i in range(4))==dims['action']
    # Conditional positive interval estimate fromindependent absolute energy/frequency.
    Elo,Ehi=F(99,100),F(101,100);wlo,whi=F(199,100),F(201,100)
    Alo,Ahi=2*Elo/whi,2*Ehi/wlo
    assert Alo<=1<=Ahi
    for E in [Elo,Ehi]:
        for w in [wlo,whi]:assert Alo<=2*E/w<=Ahi
    save(out/'passive_realizations.json',{'cases':cases,'scope':'Ideal positive lumped C,L matrices withsignedmutual orientation;no built apparatus or tolerance validation;exact one-addressed-plane realization,notfulltargetchain.'})
    save(out/'preparation_readout.json',{'cases':preps,
         'canonical_reconstruction':'Q=C*V,Phi=L*I;targetpop=(Phi1^2+Z^2Q1^2)/(Phi^T Phi+Z^2Q^T Q)',
         'scope':'Node voltage/current and canonical modal support aredifferenttypedreadouts. Prepared input requiresbothnodevoltages,notjustV1=0.'})
    save(out/'action_scale_controls.json',{'families':scales,
         'scaling_proof':'Forfixedlinearcomponents,Phi,Q ->c(Phi,Q) leavesfrequencies andnormalizedpopulations unchanged;physicalenergy andloopactionmultiplybyc^2.',
         'conditional_energy_estimator':'Amap=2E_ref/omega_bar forafrozenunit-referencepreparation;physicalsourceA0identity remains separate.',
         'synthetic_interval_Amap':[str(Alo),str(Ahi)],'interval_corner_checks':4,
         'conclusion':'Absolute energy calibration identifies a chosen preparation scale;itdoesnotselectwhichreferenceis thefundamentalUDunit.'})
    save(out/'gate_matching.json',{'coordinated_family':gates,
         'counterexample':'OpeningcouplingcapacitoralonewhileholdingLmatrixfixeddoesnotgiveg0inthefixedmap.',
         'simple_edge_inductor_obstruction':'Cinv_offdiag>0 andLinv_edge_offdiag<0 cannotobeyLinv=Cinv/Z^2 forpositiveZ. Scopedtofixedlocalquadraturemap;othertransforms/approximationsexcludedfromthisclaim.',
         'scope':'Static parameterfamily only;noactuator,clock,work/loss orautomaticretentionimplementationderived.'})
    save(out/'dimensional_gate.json',{'dimension_order':['M','L','T','I'],'dimensions':dims,
         'annihilator':'mass exponent +current exponent/2',
         'result':'No dimensionallyhomogeneousmonomialofC,L,R,time yieldsanactionwithoutanadditionalamplitude/charge/flux/energyprimitive.',
         'scope':'Declaredpassivelinearparameterfamily;doesnotexcludeotherphysicalprimitivesornonlinear/quantizedsources.'})
    result={'status':'EXACT_CONDITIONAL_PASSIVE_PORT_PASS','passive_family_cases':len(cases),'preparation_cases':len(preps),
       'amplitude_intervention_cases':sum(len(x['controls']) for x in scales),'coordinated_gate_cases':len(gates),
       'main_finding':'L=Z^2C gives anexactidealpassive realizationof thepreviouslocalreservoirport underanexplicitquarter-rotatedsourcedictionary.',
       'calibration_result':'Amap=Phi_ref^2/Z=2E_ref/omega_bar isidentifiableforafrozenphysicalpreparation,buttheuniversalnativeunitreferenceisunselected.',
       'unit_bridge_decision':'PARK classical linear passive circuit asanabsolute universal-unit derivation;retainasconditionalanalogue. Reopenwithanindependentunit-preparationlaw oradditionalphysicalprimitive.',
       'hardware_status':'NOT_EXECUTED','empirical_status':'UNSCORED','physical_promotion':0,'independent_review':'NOT_PERFORMED'}
    save(out/'results.json',result);print(json.dumps(result,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
