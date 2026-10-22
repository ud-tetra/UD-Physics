"""Exact QPB1 projective-readout and classical-anchor countermodels.

Standard-library rational arithmetic; no physical data or real hbar value.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import argparse,copy,importlib.util,json
from intake import inspect
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('prior_action',ROOT/'experiments/action-normalization-audit/audit.py')
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
mm,add,scale,tr,mv,dot,eye,zero=prior.mm,prior.add,prior.scale,prior.tr,prior.mv,prior.dot,prior.eye,prior.zero

def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def density(z):
    norm=sum((a*a+b*b for a,b in z),F(0));assert norm>0
    return [[tuple(v/norm for v in cmul(a,conj(b))) for b in z] for a in z]
def dump(p,d):p.write_text(json.dumps(d,indent=2)+'\n')

def main(out):
    out.mkdir(parents=True,exist_ok=True)
    simplices=[s for k in range(1,5) for s in combinations(range(4),k)];ix={s:i for i,s in enumerate(simplices)};d=zero(15)
    for s in simplices:
        if len(s)>1:
            for j in range(len(s)):d[ix[s[:j]+s[j+1:]]][ix[s]]=F((-1)**j)
    A=add(d,scale(tr(d),-1));J=scale(A,F(1,2));P=scale(mm(A,A),F(-1,4));P0=add(eye(15),scale(P,-1))
    assert mm(J,J)==scale(P,-1) and prior.rank(P)==14
    x=[F(0)]*15;x[ix[(0,1)]]=F(1);y=mv(J,x)
    assert dot(x,x)==dot(y,y)==1 and dot(x,y)==0
    # Raw normalized edge-coordinate observable changes under the common phase.
    assert x[ix[(0,1)]]**2==1 and y[ix[(0,1)]]**2==0
    B=[[a*b for b in x] for a in x]
    assert mm(B,J)!=mm(J,B)
    Bavg=scale(add(B,mm(mm(tr(J),B),J)),F(1,2))
    assert mm(Bavg,J)==mm(J,Bavg) and dot(x,mv(Bavg,x))==dot(y,mv(Bavg,y))==F(1,2)
    phases=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
    phases += [((1-t*t)/(1+t*t),2*t/(1+t*t)) for t in [F(1,3),F(1,2),F(2),F(3)]]
    state_checks=0
    for seed in range(1,5):
        z=[(F((seed*j)%5-2,7),F((seed+j)%7-3,11)) for j in range(1,8)];rho=density(z)
        for c,s in phases:
            assert c*c+s*s==1
            rotated=[cmul((c,-s),v) for v in z]
            assert density(rotated)==rho;state_checks+=1
    # One extra real coordinate pairs the harmonic line into a complex plane.
    h=[F(1,2)]*4+[F(0)]*11;assert mv(P0,h)==h and dot(h,h)==1
    K=zero(16);G=zero(16)
    for i in range(15):
        for j in range(15):K[i][j]=J[i][j];G[i][j]=A[i][j]
        K[i][15]=-h[i];K[15][i]=h[i]
    assert tr(K)==scale(K,-1) and mm(K,K)==scale(eye(16),-1) and mm(K,G)==mm(G,K)
    interference=[]
    for c,s in phases:
        p=((1+c)**2+s*s)/4
        assert p==(1+c)/2 and 0<=p<=1
        interference.append({'cos_phase':str(c),'sin_phase':str(s),'p_plus':str(p)})
    # Exact classical harmonic oscillator map q=L*Q,p=-m*omega*L*P.
    oscillators=[]
    for m,L,w in [(F(1),F(1),F(2)),(F(3,2),F(2,3),F(5,4)),(F(7,5),F(11,9),F(13,7))]:
        A0=m*w*L*L;tau=2/w;B0=2*m
        assert A0==B0*L*L/tau
        T=[[L,F(0)],[F(0),-m*w*L]]
        native=[[F(0),-w],[w,F(0)]];physical=[[F(0),1/m],[-m*w*w,F(0)]]
        assert mm(physical,T)==mm(T,native)
        E=m*w*w*L*L/2;assert E==A0/tau and 2*E/w==A0
        for Q,Pv,dQ,dP in [(F(1),F(0),F(0),F(1)),(F(2,3),F(4,5),F(5,7),F(6,11))]:
            q,p=L*Q,-m*w*L*Pv;dq,dp=L*dQ,-m*w*L*dP
            assert (p*dq-q*dp)/2==A0*(Q*dP-Pv*dQ)/2
        assert m*w*(2*L)**2==4*A0
        oscillators.append({'mass':str(m),'unit_amplitude_L':str(L),'angular_frequency':str(w),
          'B0':str(B0),'tau0':str(tau),'A0':str(A0),'unit_state_energy':str(E),
          'loop_action_over_pi':'A0','changing_L_to_2L_changes_A0_by':'4'})
    # Synthetic provenance/interval fixtures: not apparatus data.
    nodes=[{'id':k,'parents':[],'uses_candidate_relation':False,'uses_hbar_in_anchor_formula':False,
            'h_traceability':'SI_definition' if k=='m' else 'none_claimed','provenance_receipt':'SYNTHETIC/'+k} for k in ['m','L','w']]
    r={'data_status':'SYNTHETIC_FIXTURE','independence_mode':'target_independent_disclosed_SI',
       'unit_preparation_selected_using_candidate':False,'calibration_nodes':nodes,
       **{k:'SYNTHETIC/'+k for k in ['carrier_map_receipt','unit_preparation_receipt','action_pullback_receipt','clock_map_receipt']},
       'anchors':{'mass':{'unit':'kg','interval':['99/100','101/100'],'calibration_node':'m'},
                  'length':{'unit':'m','interval':['999/1000','1001/1000'],'calibration_node':'L'},
                  'omega':{'unit':'rad/s','interval':['199/100','201/100'],'calibration_node':'w'}}}
    fixtures={};ok=inspect(r);assert ok['status']=='SYNTHETIC_OR_PROSPECTIVE_ONLY' and ok['empirical_score']=='UNSCORED';fixtures['valid_synthetic']=ok
    changes={
      'strict_h_free':lambda z:z.update(independence_mode='strict_h_free_full_chain'),
      'missing_unit_preparation':lambda z:z.update(unit_preparation_receipt=None),
      'amplitude_backsolved':lambda z:z.update(unit_preparation_selected_using_candidate=True),
      'unknown_traceability':lambda z:z['calibration_nodes'][0].update(h_traceability='unknown'),
      'cycles_not_angular':lambda z:z['anchors']['omega'].update(unit='Hz'),
      'negative_mass':lambda z:z['anchors']['mass'].update(interval=['-1','1']),
      'dangling_parent':lambda z:z['calibration_nodes'][0].update(parents=['missing']),
      'cycle':lambda z:z['calibration_nodes'][0].update(parents=['m']),
      'invalid_parent_container':lambda z:z['calibration_nodes'][0].update(parents=7),
      'invalid_parent_type':lambda z:z['calibration_nodes'][0].update(parents=[7]),
      'hidden_target_ancestor':lambda z:z['calibration_nodes'].append({'id':'hidden','parents':[],
          'uses_candidate_relation':True,'uses_hbar_in_anchor_formula':False,'h_traceability':'none_claimed','provenance_receipt':'SYNTHETIC/target'})}
    for name,change in changes.items():
        z=copy.deepcopy(r);change(z)
        if name=='hidden_target_ancestor':z['calibration_nodes'][0]['parents']=['hidden']
        result=inspect(z);assert result['status']=='BLOCKED',(name,result);fixtures[name]=result
    # A disconnected final comparison node does not enter anchor arithmetic.
    z=copy.deepcopy(r);z['calibration_nodes'].append({'id':'comparison_only','parents':[],
       'uses_candidate_relation':True,'uses_hbar_in_anchor_formula':True,'h_traceability':'SI_definition','provenance_receipt':'SYNTHETIC/comparison'})
    separate=inspect(z);assert separate['conditional_A0_interval_J_s']==ok['conditional_A0_interval_J_s']
    fixtures['disconnected_comparison']=separate
    blank=json.loads((Path(__file__).parent/'MEASUREMENT_TEMPLATE.json').read_text());blocked=inspect(blank);assert blocked['status']=='BLOCKED'
    fixtures['real_blank_template']=blocked
    dump(out/'synthetic_intake_fixtures.json',fixtures)
    dump(out/'classical_oscillator_maps.json',oscillators)
    result={'status':'EXACT_CONDITIONAL_QPB1_CARRIER_ANCHOR_AUDIT_PASS',
      'original_carrier_real_dimension':15,'active_real_dimension':14,'active_complex_dimension':7,
      'free_active_complex_flow':'U=exp(-i*2t/tau0)*I7 with i=-J',
      'projective_readout_no_go':'rho(t)=rho(0) for scalar unitary phase; all fixed Born readouts independent of rate and eta',
      'native_observable_witness':{'edge_coordinate_squared_at_x':'1','at_Jx':'0','same_complex_projective_ray':True,'J_averaged_readout_at_both':'1/2'},
      'exact_density_invariance_cases':state_checks,
      'full_real_carrier_complex_structure':'Impossible on15real dimensions:det(K)^2=det(-I15)=-1',
      'minimal_reference_extension':{'real_dimension':16,'complex_dimension':8,'K_squared_minus_identity':True,
         'commutes_with_extended_native_flow':True,'phase_interference_cases':interference,
         'scope':'Added real coordinate and reference/coherent-readout assumptions;not a physical implementation or strict original-carrier closure'},
      'classical_null':'m,L,omega oscillator family preserves one native active plane and pulled-back loop action;A0=m*omega*L^2=2E/omega,B0=2m,tau0=2/omega',
      'amplitude_ambiguity':'L->cL leaves normalized native trajectory unchanged butA0->c^2A0;unit-ray normalization alone does not fixphysical action',
      'intake_cases':len(fixtures),'real_template_status':blocked['status'],'empirical_score':'UNSCORED',
      'next_discriminant':'Source a target-independent physical unit-preparation/amplitude map and action readout with calibration provenance;choose J-invariant observables or specify a physical relative-phase reference.',
      'scope':'Single filled tetrahedron,unit metric anddeclared projective Born readout;doesnot obstruct other metric/generator/readout/extension branches.'}
    dump(out/'carrier_anchor_results.json',result);print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
