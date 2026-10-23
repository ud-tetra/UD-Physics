"""Exact source, units, filled-tetrahedron Hodge and phase-normalization audit.

Imported source verifier is reviewed and rerun with explicit input/output paths.
All new finite-matrix arithmetic uses Fraction; no fitted physical constants.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse,hashlib,importlib.util,json

HERE=Path(__file__).resolve().parent
SRC=HERE/'sources'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def zero(n):return [[F(0) for j in range(n)] for i in range(n)]
def tr(a):return [list(r) for r in zip(*a)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r] for r in a]
def mm(a,b):return [[sum((x*y for x,y in zip(r,c)),F(0)) for c in zip(*b)] for r in a]
def mv(a,x):return [sum((v*w for v,w in zip(r,x)),F(0)) for r in a]
def dot(x,y):return sum((v*w for v,w in zip(x,y)),F(0))
def rank(a):
    a=[r[:] for r in a];k=0
    for j in range(len(a[0])):
        p=next((p for p in range(k,len(a)) if a[p][j]),None)
        if p is None:continue
        a[k],a[p]=a[p],a[k];c=a[k][j];a[k]=[x/c for x in a[k]]
        for i in range(len(a)):
            if i!=k:
                c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k
def dump(p,v):p.write_text(json.dumps(v,indent=2)+'\n')

def main(out):
    out.mkdir(parents=True,exist_ok=True)
    sources=json.loads((HERE/'SOURCES.json').read_text())
    for r in sources['sources']:
        p=SRC/r['name'];assert sha(p)==r['sha256'] and p.stat().st_size==r['size_bytes']
        raw=p.read_bytes();g=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert g==r['source_git_blob']
    ledger=json.loads((SRC/'ledger_v0.85.json').read_text());rows=ledger['rows'];by={r['id']:r for r in rows}
    assert len(rows)==ledger['typed_objects']==len(by)==723
    assert sha(SRC/'ledger_v0.85.json')=='8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec'
    assert by['G06']['claim_bin']=='SOURCE_STRATUM'
    assert all(by[f'O{i:02}']['claim_bin']=='NOT_A_COEFFICIENT' for i in range(9,16))
    assert all(by[q]['claim_bin']=='QUARANTINED_CANDIDATE' for q in ['Q287','Q288'])
    overlay=json.loads((SRC/'O13_CORRECTION_OVERLAY.json').read_text())
    assert overlay['original_exact_form']==by['O13']['exact_form']
    assert overlay['operation']=='APPEND_ONLY_CORRECTION_PROPOSAL'

    # Exact reproduction of the existing scoped type/anchor audit, not an
    # independent review. Only this reviewed imported module is executed.
    spec=importlib.util.spec_from_file_location('source_action_verifier',SRC/'verify_action_original.py')
    legacy=importlib.util.module_from_spec(spec);spec.loader.exec_module(legacy)
    legacy.SOURCE=SRC/'ledger_v0.85.json';legacy.HERE=out/'reproduced';legacy.HERE.mkdir(exist_ok=True)
    legacy.main()
    same=sha(legacy.HERE/'ACTION_UNIT_CONTRACT.json')==sha(SRC/'ACTION_UNIT_CONTRACT_original.json')
    assert same
    verified=json.loads((legacy.HERE/'VERIFICATION.json').read_text())

    # C_k(Delta3;Q), ascending oriented simplices and H=I. d is boundary;
    # A=d-d^T sets the positive phase orientation used below.
    cells=[list(combinations(range(4),k+1)) for k in range(4)]
    simp=[s for group in cells for s in group];ix={s:i for i,s in enumerate(simp)}
    n=len(simp);I=eye(n);Z=zero(n);d=zero(n)
    for group in cells[1:]:
        for s in group:
            for j in range(len(s)):d[ix[s[:j]+s[j+1:]]][ix[s]]=F((-1)**j)
    assert mm(d,d)==Z
    A=add(d,scale(tr(d),-1));A2=mm(A,A)
    assert tr(A)==scale(A,-1) and mm(A2,A)==scale(A,-4)
    P=scale(A2,F(-1,4));P0=add(I,scale(P,-1));J=scale(A,F(1,2));Omega=scale(P,2)
    assert mm(P,P)==P and tr(P)==P and rank(P)==14 and rank(P0)==1
    assert mm(J,J)==scale(P,-1) and mm(tr(J),J)==P
    assert mm(Omega,Omega)==scale(A2,-1)
    expected=zero(15)
    for i in range(4):
        for j in range(4):expected[i][j]=F(1,4)
    assert P0==expected
    x=[F(0)]*n;x[ix[(0,1)]]=F(1);y=mv(J,x)
    assert mv(P,x)==x and dot(x,x)==dot(y,y)==1 and dot(x,y)==0
    assert mv(A,x)==[2*v for v in y] and mv(A,y)==[-2*v for v in x]
    assert dot(x,mv(Omega,x))/2==1
    assert sum(P[i][i] for i in range(n))==14 and sum(J[i][i] for i in range(n))==0
    winds=[]
    for amplitude in [F(1,2),F(1),F(3,2)]:
        X=[amplitude*v for v in x];a=dot(X,X)
        assert dot(X,mv(Omega,X))/2==a
        # theta=1/2<JX,dX>, X'=AX. The action rate is a and
        # phase rate2, giving dI/dphi=a/2 exactly.
        assert dot(mv(J,X),mv(A,X))/2==a
        assert dot(mv(J,X),mv(A,X))/2-dot(X,mv(Omega,X))/2==0
        for winding in [-2,-1,0,1,2]:
            phase_over_pi=2*winding;action_over_pi=a*winding
            assert phase_over_pi%2==0
            if winding:assert action_over_pi/(a*phase_over_pi)==F(1,2)
            winds.append({'support':str(a),'winding':winding,'phase_over_pi':phase_over_pi,
              'phase_mod_2pi':'0','action_over_pi':str(action_over_pi),'endpoint_operator':'I15'})
    assert winds[6]['endpoint_operator']==winds[8]['endpoint_operator'] and winds[6]['action_over_pi']!=winds[8]['action_over_pi']
    # Nonidentifiability examples preserve native matrices and dimensionless
    # action but change dimensional action through the unspecified mass anchor.
    anchors=[]
    for mass_factor in [F(1,3),F(1),F(5,2)]:
        anchors.append({'B0_scale':str(mass_factor),'A0_scale':str(mass_factor),
          'dimensionless_A_J_I':'unchanged','eta_A_scale_at_fixed_external_hbar':str(mass_factor)})
    result={'status':'EXACT_SCOPED_SOURCE_AND_ACTION_AUDIT_PASS',
      'source_ledger':{'archive_label':'v0.85','sha256':sha(SRC/'ledger_v0.85.json'),'rows':len(rows),
         'unique_ids':len(by),'inherited_scientific_revision_field':ledger['scientific_revision'],
         'source_baseline_field':ledger['source_baseline'],'warning':'Preserve inherited metadata; archive label does not mean every field was rewritten.'},
      'source_bytes_verified':len(sources['sources']),
      'source_verifier_reproduction':{'typed_equalities':verified['typed_equalities_passed'],
         'source_rows_bound':verified['source_rows_bound'],'rational_anchor_banks':verified['anchor_banks_checked'],
         'unit_contract_bytes_equal_original':same,'review_relationship':'same constructor reexecution, not independent review'},
      'O13':{'literal_source_chain':'DIMENSIONALLY_INVALID','existing_overlay':'CONSTRUCTOR_CHECKED_PROPOSAL; NON_CONSTRUCTOR_REVIEW_PENDING',
         'correct_equalities':overlay['replacement_equalities'],'mainline_registry_edited':False},
      'exact_carrier':{'f_vector':[len(g) for g in cells],'chain_dimension':n,'boundary_squared_zero':True,
         'active_rank':14,'harmonic_rank':1,'identities':['A^T=-A','A^3=-4A','P=-A^2/4','P^2=P','J=A/2','J^2=-P','Omega=2P']},
      'action_normalization':{'support':'a=||x||^2>0','chosen_one_form':'theta=1/2<Jx,dx>',
         'lifted_action':'I=a*Delta_phi_lift/2','specific_dimensional_scale':'S_native/(a*Delta_phi_lift)=A0/2',
         'energy_frequency_check':'E_native/(a*omega)=A0/2 if E_native=A0*a/tau0 and omega=2/tau0',
         'scope':'Single filled tetrahedron,unit chain metric,Hodge loop action convention; not generic glued carrier or complete master dynamical action'},
      'winding_cases':winds,
      'endpoint_trace_no_go':{'trace_formula':'Tr U(phi)=1+14 cos(phi)',
         'witness':'phi=0 and2pi give identical U=I15 and trace15 but I=0 andpi*a',
         'conclusion':'No endpoint-operator or endpoint-trace-only function recovers this lifted loop action for unrestricted windings.'},
      'distinct_action_check':{'loop_one_form_rate':'theta(X_prime)=a',
         'spectral_Hamiltonian':'H=a','first_order_functional_rate':'theta(X_prime)-H=0 on this unforced orbit',
         'conclusion':'The nonzero integrated loop one-form and the first-order theta-minus-H functional are different typed actions. Specify which action enters a proposed physical phase map.'},
      'phase_map_conditions':{'assumption':'physical phase chi=S_native/hbar and same-carrier phase map are an additional bridge',
         'coefficient_of_I':'chi=eta_A*I',
         'coefficient_of_Hodge_phi':'chi=(eta_A*a/2)*phi_lift; unit ray gives eta_A/2',
         'unit_ray_phase_identification':'chi=phi_lift implies eta_A=2 under this postulate, matching quarantined Q287/Q288',
         'xi_act_identity':'xi_act=eta_A only if xi_act multiplies I under the independently justified physical phase map; coefficient of raw phi is different'},
      'scale_ambiguity_examples':anchors,
      'physical_status':'No native-to-SI anchor,primitive quantum-holonomy reconstruction or empirical score; QPB1 candidate remains quarantined; promotion0',
      'limitations':['18 typed equalities from17 source rows; not global typing of723objects',
        'Hodge trace counterexample is not reconstruction of an unspecified primitive quantum-holonomy operator',
        'Action one-form and lift convention explicitly imported/declared; no physical action or phase correspondence derived']}
    dump(out/'audit_results.json',result)
    print(json.dumps({k:result[k] for k in ['status','source_verifier_reproduction','exact_carrier','physical_status']}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
