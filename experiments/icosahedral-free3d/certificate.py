"""Exact all-phase transverse stiffness comparison for A0<=1/10.

This certifies positive instantaneous shape stiffness, not parametric stability.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from model import Model,ico


def main(out):
    model=Model();Q=ico.Q5;zero=Q(0);one=Q(1);R2=ico.dot(model.vertices[1],model.vertices[1])
    def matrix():return [[zero for _ in range(40)] for _ in range(40)]
    K=matrix();Tr=matrix();Te=matrix()
    def outer_add(M,v,w=one):
        nonzero=[i for i,x in enumerate(v) if x!=zero]
        for i in nonzero:
            for j in nonzero:M[i][j]+=w*v[i]*v[j]
    def pair_add(M,i,j,block):
        for a in range(3):
            for b in range(3):
                ix=1+3*i+a;iy=1+3*i+b;jx=1+3*j+a;jy=1+3*j+b
                M[ix][iy]+=block[a][b];M[jx][jy]+=block[a][b]
                M[ix][jy]-=block[a][b];M[jx][iy]-=block[a][b]
    K[0][0]=one
    for i in range(1,13):
        r=model.vertices[i];v=[zero]*40
        for j in range(3):v[1+3*i+j]=r[j]/R2;v[1+j]=-r[j]/R2
        outer_add(K,v);v[0]=-one;outer_add(K,v)
        block=[[(Q(int(a==b))-r[a]*r[b]/R2)/R2 for b in range(3)] for a in range(3)]
        pair_add(Tr,i,0,block)
    for i,j in model.edges:
        delta=ico.sub(model.vertices[i],model.vertices[j]);v=[zero]*40
        for a in range(3):v[1+3*i+a]=delta[a];v[1+3*j+a]=-delta[a]
        outer_add(K,v,Q(F(2,5)))
        block=[[Q(F(2,5))*(Q(int(a==b))-delta[a]*delta[b]) for b in range(3)] for a in range(3)]
        pair_add(Te,i,j,block)
    mass=[one]+[one/R2]*39
    # Lift only six rigid directions with the exact mass-orthogonal projector.
    penalty=matrix()
    translations=[];rotations=[]
    for axis in range(3):
        translation=[zero]*40
        for i in range(13):translation[1+3*i+axis]=one
        translations.append(translation)
        outer_add(penalty,[m*v for m,v in zip(mass,translation)],R2/13)
        unit=[Q(int(j==axis)) for j in range(3)];rotation=[zero]*40
        for i,r in enumerate(model.vertices):
            v=ico.cross(unit,r)
            for j in range(3):rotation[1+3*i+j]=v[j]
        rotations.append(rotation)
        outer_add(penalty,[m*v for m,v in zip(mass,rotation)],Q(F(1,8)))
    def mv(A,v):return [sum(a*x for a,x in zip(row,v)) for row in A]
    for v in translations:
        assert mv(K,v)==[zero]*40 and mv(Tr,v)==[zero]*40 and mv(Te,v)==[zero]*40
    for v in rotations:
        assert mv(K,v)==[zero]*40
        assert mv(Tr,v)==[m*x for m,x in zip(mass,v)]==mv(Te,v)
    for i,a in enumerate(translations+rotations):
        for j,b in enumerate(translations+rotations):
            expected=(Q(13)/R2 if i<3 else Q(8)) if i==j else zero
            assert sum(m*x*y for m,x,y in zip(mass,a,b))==expected
    comparison=[[K[i][j]-Q(F(8,59))*Tr[i][j]-Q(F(1,59))*Te[i][j]+penalty[i][j]
                 -(mass[i]/10 if i==j else zero) for j in range(40)] for i in range(40)]
    L=matrix();pivots=[]
    for j in range(40):
        pivot=comparison[j][j]-sum(L[j][k]*L[j][k]*pivots[k] for k in range(j))
        assert pivot.sign()>0
        pivots.append(pivot);L[j][j]=one
        for i in range(j+1,40):
            L[i][j]=(comparison[i][j]-sum(L[i][k]*L[j][k]*pivots[k] for k in range(j)))/pivot
    # Matrix equality reconstructed exactly, not just a positive-pivot report.
    for i in range(40):
        for j in range(40):
            assert sum(L[i][k]*pivots[k]*L[j][k] for k in range(min(i,j)+1))==comparison[i][j]
    encoded=[{'rational':str(p.p),'sqrt5_coefficient':str(p.q)} for p in pivots]
    # Independent force differentiation checks the finite-amplitude Hessian formula.
    rng=np.random.default_rng(801);d=rng.normal(size=40);d/=np.linalg.norm(d);errors=[]
    for t in [0.,.7,3.,10.]:
        alpha,b=model.collective(t);x=np.r_[alpha,(model.ref*np.r_[1,np.full(12,1+b)][:,None]).ravel()]
        eps=1e-6
        fp=model.energy_force(x+eps*d)[1];fm=model.energy_force(x-eps*d)[1]
        H=model.H0+(2*b-alpha)/(1+b)*model.Tr+b/(1+b)*model.Te
        Knum=H*model.rootmass[:,None]*model.rootmass[None,:]
        errors.append(float(max(abs((fp-fm)/(2*eps)-Knum@d))))
    assert max(errors)<3e-9
    result={'status':'PASS','coefficient_field':'Q(sqrt(5))','amplitude_scope':'|A0|<=1/10;g=1,k=2/5,unit inertias/pins',
            'bounds':{'abs_b':'1/60','abs_alpha':'1/10','radial_prestress_coefficient_min':'-8/59','edge_prestress_coefficient_min':'-1/59'},
            'matrix':'K0-(8/59)Tr-(1/59)Te+M P_rigid-(1/10)M',
            'positive_exact_LDL_pivots':40,'pivots':encoded,'minimum_pivot_numeric':min(map(float,pivots)),
            'pivot_sha256':hashlib.sha256(json.dumps(encoded,sort_keys=True).encode()).hexdigest(),
            'conclusion':'On mass-orthogonal nonrigid perturbations, instantaneous quadratic stiffness>=1/10 times the mass norm throughout the symmetric breathing family.',
            'finite_amplitude_force_hessian_check_error':max(errors),
            'limitation':'Uniform positive instantaneous stiffness does not prove bounded evolution for a time-dependent parametric system.'}
    out.mkdir(parents=True,exist_ok=True);(out/'stiffness-certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='pivots'},indent=2),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
