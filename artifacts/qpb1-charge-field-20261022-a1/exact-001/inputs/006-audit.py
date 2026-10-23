"""Exact finite tetrahedral gauge-field candidate, not the native 15-register law."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('prior', ROOT/'experiments/action-normalization-audit/audit.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
eye, tr, add, scale, mm, mv, dot, rank = (
    getattr(prior,k) for k in ['eye','tr','add','scale','mm','mv','dot','rank'])


def zero(m,n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def save(path, value):
    path.write_text(json.dumps(value,indent=2)+'\n')


def strings(a):
    return [[str(v) for v in row] for row in a]


def representation(simplices, perm):
    index = {s:i for i,s in enumerate(simplices)}
    r = zero(len(simplices),len(simplices))
    for i,s in enumerate(simplices):
        mapped = tuple(perm[v] for v in s)
        inversions = sum(mapped[a]>mapped[b] for a in range(len(s)) for b in range(a+1,len(s)))
        r[index[tuple(sorted(mapped))]][i] = F((-1)**inversions)
    return r


def main(out):
    out.mkdir(parents=True,exist_ok=True)
    here=Path(__file__).resolve().parent
    sources=json.loads((here/'SOURCES.json').read_text())
    for source in sources['sources']:
        assert hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest()==source['sha256']
    ledger=json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())
    byid={r['id']:r for r in ledger['rows']}
    selected=json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    assert len(selected)==18 and all(r==byid[r['id']] for r in selected)
    simplices = [list(combinations(range(4),k)) for k in range(1,5)]
    boundary = []
    for low,high in zip(simplices,simplices[1:]):
        ix = {s:i for i,s in enumerate(low)}
        b = zero(len(low),len(high))
        for col,s in enumerate(high):
            for j in range(len(s)):
                b[ix[s[:j]+s[j+1:]]][col] = F((-1)**j)
        boundary.append(b)
    b1,b2,b3 = boundary
    assert mm(b1,b2)==zero(4,4) and mm(b2,b3)==zero(6,1)
    assert [rank(b) for b in boundary] == [3,3,1]
    grad_lap, curl_lap = mm(tr(b1),b1), mm(b2,tr(b2))
    pl,pt = scale(grad_lap,F(1,4)),scale(curl_lap,F(1,4))
    assert add(pl,pt)==eye(6)
    assert mm(pl,pl)==pl and mm(pt,pt)==pt and mm(pl,pt)==zero(6,6)
    assert rank(pl)==rank(pt)==3
    assert mm(b1,pt)==zero(4,6) and mm(curl_lap,pl)==zero(6,6)
    d_full=zero(15,15)
    offsets=[0,4,10,14]
    for degree,b in enumerate(boundary):
        for i,row in enumerate(b):
            for j,value in enumerate(row):d_full[offsets[degree]+i][offsets[degree+1]+j]=value
    native_a=add(d_full,scale(tr(d_full),-1))
    assert rank(native_a)==14
    group=[]
    full_character_norm=F(0)
    for perm in permutations(range(4)):
        reps=[representation(c,perm) for c in simplices]
        for k,b in enumerate(boundary):
            assert mm(reps[k],b)==mm(b,reps[k+1])
        r=reps[1]
        character=sum((rep[i][i] for rep in reps for i in range(len(rep))),F(0))
        full_character_norm+=character*character/F(24)
        assert mm(r,pl)==mm(pl,r) and mm(r,pt)==mm(pt,r)
        group.append(r)
    assert full_character_norm==13
    # Reynolds projection of every symmetric matrix basis spans all invariant symmetric forms.
    reynolds=[]
    for i in range(6):
        for j in range(i,6):
            e=zero(6,6);e[i][j]=F(1);e[j][i]=F(1)
            avg=zero(6,6)
            for r in group:
                avg=add(avg,scale(mm(mm(tr(r),e),r),F(1,24)))
            reynolds.append([x for row in avg for x in row])
    assert rank(reynolds)==2
    assert rank([[x for row in pl for x in row],[x for row in pt for x in row]])==2
    w=[F(1,2),F(0),F(-1,2),F(1,2),F(0),F(1,2)]
    assert dot(w,w)==1 and mv(b1,w)==[F(0)]*4 and mv(pt,w)==w
    face=[row[0] for row in b2]
    assert dot(face,face)==3 and mv(b1,face)==[F(0)]*4
    rho=[F(1),F(-1),F(0),F(0)]
    p_long=[x/4 for x in mv(tr(b1),rho)]
    assert mv(b1,p_long)==rho and dot(p_long,p_long)==F(1,2)
    cases=[]
    tuples=[(s,s,1/s) for s in [F(1,2),F(1),F(2),F(3),F(4),F(7,3)]]
    tuples += [(F(3,2),F(2,3),F(5,7)),(F(2,5),F(7,4),F(3,2)),(F(5),F(1,3),F(2))]
    tuples += [(F(3),F(1),F(1))]  # Same frequency and impedance, different longitudinal energy.
    for ul,ut,v in tuples:
        u=add(scale(pl,ul),scale(pt,ut));k=scale(curl_lap,v)
        assert mm(u,pl)==scale(pl,ul) and mm(u,pt)==scale(pt,ut)
        assert tr(u)==u and tr(k)==k
        g=zero(12,12);h=zero(12,12);omega2=4*ut*v
        for i in range(6):
            for j in range(6):
                g[i][6+j]=u[i][j];g[6+i][j]=-k[i][j]
                h[i][j]=k[i][j];h[6+i][6+j]=u[i][j]
        assert add(mm(tr(g),h),mm(h,g))==zero(12,12)
        transverse=zero(12,12)
        for i in range(6):
            for j in range(6):transverse[i][j]=transverse[6+i][6+j]=pt[i][j]
        assert mm(mm(g,g),transverse)==scale(transverse,-omega2)
        # Retain the constrained/gauge sector rather than pretending the full Hessian is positive definite.
        assert rank(h)==9 and rank(transverse)==6
        # Current G is S4-covariant; 24-by-9 checks.
        for r in group:
            rr=zero(12,12)
            for i in range(6):
                for j in range(6):rr[i][j]=rr[6+i][6+j]=r[i][j]
            assert mm(rr,g)==mm(g,rr)
        for seed in range(1,4):
            a=[F((i+2*seed)%7-3,5) for i in range(6)]
            p=[F((2*i+seed)%9-4,7) for i in range(6)]
            da,dp=mv(u,p),mv(k,a);dp=[-x for x in dp]
            assert mv(b1,dp)==[F(0)]*4
            chi=[F(seed),F(1,3),F(-1,2),F(0)]
            shifted=[x+y for x,y in zip(a,mv(tr(b1),chi))]
            assert mv(tr(b2),shifted)==mv(tr(b2),a)
            assert dot(da,mv(k,a))+dot(dp,mv(u,p))==0
            da_gauge=[x+y for x,y in zip(da,mv(tr(b1),chi))]
            assert dot(da_gauge,mv(k,a))+dot(dp,mv(u,p))==0
            assert mv(tr(b3),mv(tr(b2),a))==[F(0)]
        ec=dot(p_long,mv(u,p_long))/2
        er=dot(face,mv(u,face))/2
        assert ec==ul/4 and er==3*ut/2 and ec/er==ul/(6*ut)
        lam2=ut/(4*v)
        action_unit,charge_unit,time_unit=F(3,2),F(2,5),F(7,3)
        c_eff=time_unit*charge_unit**2/(action_unit*ut)
        l_eff=action_unit*time_unit/(4*v*charge_unit**2)
        alpha,beta=F(2,3),F(-3,5)
        flux=action_unit*alpha/charge_unit;charge_mode=charge_unit*beta
        physical_energy=charge_mode**2/(2*c_eff)+flux**2/(2*l_eff)
        assert physical_energy==action_unit/time_unit*(ut*beta**2/2+2*v*alpha**2)
        assert 1/(c_eff*l_eff)==omega2/time_unit**2
        assert l_eff/c_eff==(action_unit/charge_unit**2)**2*lam2
        item={'u_L':str(ul),'u_T':str(ut),'v':str(v),'frequency_squared':str(omega2),
              'lambda_squared':str(lam2),'E_static_dipole':str(ec),'E_face_cycle':str(er),
              'static_to_cycle_energy_ratio':str(ec/er),'full_Hessian_rank':rank(h),
              'S4_checks':24,'finite_state_checks':3}
        if ut*v==1:
            lam=ut/2
            assert lam*lam==lam2
            if ul==ut:assert ec/er==F(1,6)
            # q0=1,A0=1 are coefficient fixtures only, not a physical calibration.
            c_eff, l_eff=1/ut,1/(4*v)
            assert l_eff/c_eff==lam*lam and l_eff*c_eff==F(1,4)
            assert ut/2==lam  # p_mode1,a_mode0 has native H/support lambda, not automatically1
            for alpha,beta in [(F(0),F(1)),(F(2,3),F(-3,5)),(F(1),F(2))]:
                support=alpha*alpha/lam+lam*beta*beta
                assert ut*beta*beta/2+2*v*alpha*alpha==support
            item.update(frequency='2',lambda_coefficient=str(lam),unit_mode_charge_support=str(lam))
        cases.append(item)
    assert cases[-1]['static_to_cycle_energy_ratio']=='1/2'
    # Canonical electric/magnetic exchange is a family D_sigma, not a selected scale.
    dualities=[]
    symp=[[F(0),F(1)],[F(-1),F(0)]]
    for sigma in [F(1,4),F(1,2),F(1),F(3,2),F(2)]:
        ut,v=2*sigma,1/(2*sigma)
        h=[[4*v,F(0)],[F(0),ut]]
        d=[[F(0),sigma],[-1/sigma,F(0)]]
        assert mm(mm(tr(d),symp),d)==symp
        assert mm(mm(tr(d),h),d)==h
        assert ut*v==1 and ut/(4*v)==sigma*sigma
        dualities.append({'sigma':str(sigma),'u_T':str(ut),'v':str(v),'lambda':str(sigma)})
    save(out/'matrices.json',{'vertices':[list(s) for s in simplices[0]],'edges':[list(s) for s in simplices[1]],
         'faces':[list(s) for s in simplices[2]],'B1':strings(b1),'B2':strings(b2),'B3':strings(b3),
         'P_L':strings(pl),'P_T':strings(pt),'addressed_cycle_w':[str(a) for a in w],
         'symmetric_edge_commutant_dimension':2,'signed_S4_permutations':24,
         'distinct_native_full_chain_commutant_dimension':str(full_character_norm),
         'distinct_native_chain_active_rank':rank(native_a)})
    save(out/'coefficient_families.json',{'cases':cases,'canonical_duality_cases':dualities})
    result={'status':'PASS','evidence':'EXACT / CONDITIONAL','boundary_ranks':[3,3,1],
         'source_bindings_checked':len(sources['sources']),'source_rows_checked':len(selected),
         'S4_permutations':24,'symmetric_edge_invariant_dimension':2,'Hamiltonian_fixtures':len(cases),
         'fixed_frequency_impedance_cases':6,'longitudinal_counterexamples':1,
         'physical_dictionary_checks':len(cases),
         'state_checks':3*len(cases),'duality_cases':len(dualities),
         'physical_score':'UNSCORED','physical_promotion':0,
         'finding':'Gauge symmetry, S4, positivity and frequency2 leave impedance coefficient free; diagonal electric locality gives a conditional energy ratio1/6.'}
    save(out/'summary.json',result)
    print(json.dumps(result))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path)
    main(p.parse_args().out)
