"""Exact K4 integral flow/cut pairing and conditional field-preparation audit.

Lattices are kinematic hypotheses, not an inferred quantum dynamics.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('field',ROOT/'experiments/qpb1-charge-field/audit.py')
field=importlib.util.module_from_spec(spec);spec.loader.exec_module(field)
zero,eye,tr,add,scale,mm,mv,dot,rank=(getattr(field,k) for k in ['zero','eye','tr','add','scale','mm','mv','dot','rank'])


def det(a):
    n=len(a);value=F(0)
    for p in permutations(range(n)):
        x=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):x*=a[i][p[i]]
        value+=x
    return value


def inv(a):
    n=len(a);x=[row[:]+ident for row,ident in zip(a,eye(n))]
    for k in range(n):
        pivot=next(j for j in range(k,n) if x[j][k])
        x[k],x[pivot]=x[pivot],x[k];v=x[k][k];x[k]=[c/v for c in x[k]]
        for j in range(n):
            if j!=k:
                v=x[j][k];x[j]=[c-v*d for c,d in zip(x[j],x[k])]
    return [row[n:] for row in x]


def snf3(a):
    divisors=[]
    for size in range(1,4):
        g=0
        for rows in combinations(range(3),size):
            for cols in combinations(range(3),size):
                d=det([[a[i][j] for j in cols] for i in rows]);assert d.denominator==1
                g=gcd(g,abs(d.numerator))
        divisors.append(g)
    return [divisors[0],divisors[1]//divisors[0],divisors[2]//divisors[1]]


def integral(a):
    return all(v.denominator==1 for row in a for v in row)


def vector_integral(x):
    return all(v.denominator==1 for v in x)


def strings(a):return [[str(v) for v in row] for row in a]
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')


def main(out):
    out.mkdir(parents=True,exist_ok=True);here=Path(__file__).resolve().parent
    sources=json.loads((here/'SOURCES.json').read_text())
    for s in sources['sources']:
        assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256']
    simplices=[list(combinations(range(4),k)) for k in range(1,5)]
    bs=[]
    for low,high in zip(simplices,simplices[1:]):
        ix={s:i for i,s in enumerate(low)};b=zero(len(low),len(high))
        for col,s in enumerate(high):
            for j in range(len(s)):b[ix[s[:j]+s[j+1:]]][col]=F((-1)**j)
        bs.append(b)
    b1,b2,b3=bs
    assert mm(b1,b2)==zero(4,4) and mm(b2,b3)==zero(6,1)
    cycle=[row[:3] for row in b2]
    cut=[row[1:] for row in tr(b1)]
    assert cycle[3:]==eye(3) and cut[:3]==eye(3)
    assert mm(b1,cycle)==zero(4,3) and mm(tr(cut),cycle)==zero(3,3)
    # The fourth oriented face is integral in the first three; graph cycles bound in the filled complex.
    assert [b2[i][3] for i in range(6)]==mv(cycle,[F(1),F(-1),F(1)])
    g=mm(tr(cycle),cycle);gc=mm(tr(cut),cut);gi=inv(g)
    dual=mm(cycle,gi);pl=scale(mm(tr(b1),b1),F(1,4));pt=scale(mm(b2,tr(b2)),F(1,4))
    assert mm(tr(cycle),dual)==eye(3) and mm(dual,tr(cycle))==pt
    assert mm(mm(cut,inv(gc)),tr(cut))==pl
    assert det(g)==det(gc)==16 and snf3(g)==snf3(gc)==[1,4,4]
    assert abs(det([c+f for c,f in zip(cut,cycle)]))==16
    sign=[F(1),F(-1),F(1)];outer=[[a*b for b in sign] for a in sign]
    assert g==add(scale(eye(3),4),scale(outer,-1))
    assert gi==scale(add(eye(3),outer),F(1,4))
    # Exact minimum-vector enumeration with proved bounds documented in README.
    cycle_short=[];dual_short=[]
    for z0 in product(range(-1,2),repeat=3):
        z=list(map(F,z0));n=dot(z,mv(g,z));nd=dot(z,mv(gi,z))
        if n==3:cycle_short.append(z0)
        if nd==F(1,2):dual_short.append(z0)
        if any(z):assert n>=3 and nd>=F(1,2)
    assert len(cycle_short)==8 and len(dual_short)==12
    # A homothety/similarity would require both sigma^6=1/256 and sigma^2=1/6.
    assert F(1,6)**3!=F(1,256)
    # Canonical graph projection classes, all represented by chord inputs modulo4.
    classes={}
    for z in product(range(4),repeat=3):
        delta=tuple(v%1 for v in mv(gi,list(map(F,z))))
        classes.setdefault(delta,z)
    assert len(classes)==16
    minima={};records=[]
    for delta,z0 in sorted(classes.items()):
        best=None;best_ns=[]
        # G>=I, G<=4I and a centered representative gives energy<=3.
        # Therefore outside[-2,1]^3 any coordinate has magnitude>=2 and cannot minimize.
        for ns in product(range(-2,2),repeat=3):
            x=[a+b for a,b in zip(delta,ns)];n=dot(x,mv(g,x))
            if best is None or n<best:best=n;best_ns=[ns]
            elif n==best:best_ns.append(ns)
        order=next(n for n in [1,2,4] if all((n*d).denominator==1 for d in delta))
        assert best=={1:F(0),2:F(1),4:F(1,2)}[order]
        p0=[F(0)]*3+list(map(F,z0));rho=mv(b1,p0);p_long=mv(pl,p0)
        p_trans=mv(cycle,[a+b for a,b in zip(delta,best_ns[0])])
        p_min=[a+b for a,b in zip(p_long,p_trans)]
        assert vector_integral(p_min) and mv(b1,p_min)==rho
        assert dot(p_trans,p_trans)==best and dot(p_long,p_trans)==0
        assert dot(p_long,p_long)==dot(rho,rho)/4
        for ul,ut in [(F(1),F(1)),(F(2),F(3)),(F(3),F(1)),(F(1,2),F(7,5))]:
            h=ul*dot(p_long,p_long)/2+ut*dot(p_trans,p_trans)/2
            assert h==ul*dot(rho,rho)/8+ut*best/2
        minima[delta]=(best,order)
        records.append({'cycle_coordinates_mod_Z':[str(x) for x in delta],'order':order,
            'minimum_transverse_norm_squared':str(best),'minimum_multiplicity':len(best_ns),
            'representative_vertex_charge':[str(x) for x in rho],
            'one_integral_minimizing_edge_flux':[str(x) for x in p_min]})
    assert sum(o==1 for _,o in minima.values())==1
    assert sum(o==2 for _,o in minima.values())==3
    assert sum(o==4 for _,o in minima.values())==12
    # Edge-complement star is an isometry between cut and cycle lattices, not Euclidean lattice duality.
    edges=simplices[1];edge_ix={e:i for i,e in enumerate(edges)};star=zero(6,6)
    for col,e in enumerate(edges):
        complement=tuple(i for i in range(4) if i not in e);p=e+complement
        sign_p=F((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)))
        star[edge_ix[complement]][col]=sign_p
    assert mm(star,star)==eye(6) and mm(tr(star),star)==eye(6)
    assert mm(mm(star,pt),star)==pl
    star_coords=mm(mm(inv(gc),tr(cut)),mm(star,cycle))
    assert integral(star_coords) and abs(det(star_coords))==1
    orbits=[];characters=F(0)
    representations=[]
    for perm in permutations(range(4)):
        r=field.representation(edges,perm)
        rf=mm(mm(gi,tr(cycle)),mm(r,cycle))
        rd=mm(tr(cycle),mm(r,dual))
        assert integral(rf) and abs(det(rf))==1 and integral(rd) and abs(det(rd))==1
        assert mm(mm(tr(rf),g),rf)==g and rd==tr(inv(rf))
        chi=sum((rf[i][i] for i in range(3)),F(0));characters+=chi*chi/F(24)
        parity=F((-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4)))
        assert mm(star,r)==scale(mm(r,star),parity)
        for delta in classes:
            image=tuple(v%1 for v in mv(rf,list(delta)))
            assert minima[image]==minima[delta]
        representations.append(rf)
    assert characters==1  # Full real cycle commutant is scalar.
    remaining=set(classes)
    while remaining:
        seed=next(iter(remaining));orb={tuple(v%1 for v in mv(r,list(seed))) for r in representations}
        orbits.append(len(orb));remaining-=orb
    assert sorted(orbits)==[1,3,12]
    # Charged preparation: only integral rho versus the stronger integral p constraint.
    rho=list(map(F,[1,-1,0,0]));p_long=[v/4 for v in mv(tr(b1),rho)]
    p_integer=list(map(F,[-1,0,0,0,0,0]));p_trans=mv(pt,p_integer)
    assert mv(b1,p_integer)==rho and not vector_integral(p_long)
    assert dot(p_long,p_long)==dot(p_trans,p_trans)==F(1,2)
    dipoles=[]
    for ul,ut in [(F(1),F(1)),(F(2),F(3)),(F(3),F(1)),(F(1,2),F(7,5))]:
        real_min=ul/4;integer_min=(ul+ut)/4;face_energy=3*ut/2
        assert integer_min-real_min==ut/4
        # A nonzero integer edge vector has norm²>=1, achieved by this unit-edge dipole.
        candidates=[]
        for x in product(range(-1,2),repeat=6):
            xx=list(map(F,x))
            if mv(b1,xx)==rho:
                l,t=mv(pl,xx),mv(pt,xx);candidates.append(ul*dot(l,l)/2+ut*dot(t,t)/2)
        assert min(candidates)==integer_min
        dipoles.append({'u_L':str(ul),'u_T':str(ut),'real_minimum':str(real_min),
            'integer_edge_minimum':str(integer_min),'real_to_face_ratio':str(real_min/face_energy),
            'integer_to_face_ratio':str(integer_min/face_energy),'extra_radiative_energy':str(ut/4)})
    assert dipoles[0]['real_to_face_ratio']=='1/6' and dipoles[0]['integer_to_face_ratio']=='1/3'
    # Relative lattice rescaling preserves canonical pairing while changing the selected exchange scale.
    scaled=[]
    for r in [F(1,2),F(1),F(3,2),F(2),F(3)]:
        sigma=r*r;u,v=2*sigma,1/(2*sigma)
        assert u*v==1 and u/(4*v)==sigma*sigma
        # a in r*Lambda,p in Lambda/r; D_sigma sends both integer coefficient blocks bijectively.
        assert sigma/r==r and r/sigma==1/r
        assert r*(1/r)==1
        scaled.append({'configuration_lattice_scale':str(r),'momentum_lattice_scale':str(1/r),
            'canonical_pair_scale':'1','exchange_sigma_and_matched_lambda':str(sigma),
            'u_T':str(u),'v':str(v)})
    # In canonical integer coordinates a=Dq,p=Ln, (q,n)->(n,-q) is integral/symplectic,
    # but energy invariance would require u_T*G=4*v*G^-1, impossible as G^2 is nonscalar.
    g2=mm(g,g)
    assert any(g2[i][j] for i in range(3) for j in range(3) if i!=j)
    # Whole-grid phase pi always gives -I. At phase pi/2, natural coordinates
    # have blocks lambda*G and -G^-1/lambda. At lambda1 the latter is not integral.
    assert integral(g) and not integral(gi)
    assert integral(scale(eye(3),-1))
    # Natural grid quarter-turn witness at lambda1: a in Lambda*,p0 maps to p not in Lambda.
    a0=[row[0] for row in dual]
    assert not vector_integral(a0) and mv(b1,a0)==[F(0)]*4
    save(out/'lattice_matrices.json',{'edge_order':[list(e) for e in edges],'B1':strings(b1),
        'cycle_basis':strings(cycle),'cut_basis':strings(cut),'cycle_Gram':strings(g),'cut_Gram':strings(gc),
        'cycle_dual_basis':strings(dual),'cycle_dual_Gram':strings(gi),'cycle_smith':snf3(g),
        'cut_smith':snf3(gc),'integer_split_index':16,'edge_complement_star':strings(star),
        'star_cycle_to_cut_basis_map':strings(star_coords),'cycle_short_vector_count':len(cycle_short),
        'dual_short_vector_count':len(dual_short),'cycle_full_commutant_dimension':str(characters)})
    save(out/'discriminant_classes.json',{'classes':records,'S4_orbit_sizes':sorted(orbits),
        'minimum_norm_distribution':{'identity':'0','12_order4':'1/2','3_order2':'1'},
        'bounded_search':'16 classes,64 shifts each; G eigenvalues1,4,4 prove sufficiency.'})
    save(out/'preparation_duality.json',{'dipole_cases':dipoles,'scaled_lattice_families':scaled,
        'natural_grid_quarter_turn_momentum_witness':[str(-x) for x in a0],
        'canonical_integer_coordinate_exchange':'Exists, but fails isotropic energy invariance because G squared is nonscalar',
        'stroboscopic_whole_grid_groups':{'natural_dual_pair':'Z2 at phase pi multiples',
          'equal_scaled_cycle_pair_with_matched_lambda':'Z4 at phase pi/2 multiples'},
        'continuous_lattice_status':'Nontrivial continuous oscillator flow does not preserve a discrete phase grid at all times.'})
    result={'status':'PASS','evidence':'EXACT / CONDITIONAL','cycle_cut_ranks':[3,3],
        'Gram_determinants':[16,16],'Smith_invariants':[1,4,4],'discriminant_classes':16,
        'class_minimizations':16,'bounded_shifts_per_class':64,'class_energy_checks':64,
        'S4_permutations':24,'dipole_parameter_cases':4,'scaled_pair_families':5,
        'natural_scalar_exchange':'OBSTRUCTED','integer_edge_dipole_to_face_ratio':'1/3 under equal edge electric weights',
        'physical_score':'UNSCORED','physical_promotion':0}
    save(out/'summary.json',result);print(json.dumps(result))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
