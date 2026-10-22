"""Integer pair graphs and exact Q(sqrt5) differential-strain kernel."""
from pathlib import Path
import argparse,json
from fractions import Fraction as F
import numpy as np
from network import Network,ico


def rank(rows):
    a=[r.copy() for r in rows];p=0;zero=ico.Q5(0)
    for j in range(len(a[0])):
        ix=next((i for i in range(p,len(a)) if a[i][j]!=zero),None)
        if ix is None:continue
        a[p],a[ix]=a[ix],a[p];v=a[p][j];a[p]=[x/v for x in a[p]]
        for i in range(p+1,len(a)):
            v=a[i][j]
            if v!=zero:a[i]=[x-v*y for x,y in zip(a[i],a[p])]
        p+=1
        if p==len(a):break
    return p


def main(out):
    model=Network();Q=ico.Q5;zero=Q(0);one=Q(1);R2=ico.dot(model.vertices[1],model.vertices[1])
    def graph(n,pairs,line=False):
        G=np.zeros((len(pairs),n),dtype=np.int64)
        for row,(i,j) in zip(G,pairs):row[i]=1;row[j]=-1
        # Connected graph incidence has rank n-1; exhibit connectivity directly.
        seen={0}
        while True:
            new=seen|{int(j) for i,j in pairs if i in seen}|{int(i) for i,j in pairs if j in seen}
            if new==seen:break
            seen=new
        assert len(seen)==n
        L=G.T@G;I=np.eye(n,dtype=np.int64);quad=L@L-10*L+20*I
        P=L@(L-6*I)@quad
        if line:P=P@(L-10*I)
        assert not np.any(P)
        eig=[(Q(0),1),(Q(6),5),(Q(5,1),3),(Q(5,-1),3)]
        if line:eig.append((Q(10),18))
        power=I.copy();moments=[]
        for k in range(len(eig)):
            value=sum(mult*lam**k for lam,mult in eig);assert value==Q(int(np.trace(power)))
            moments.append(int(np.trace(power)));power=power@L
        return {'vertices':n,'edges':len(pairs),'incidence_rank':n-1,'degree':sorted(set(np.diag(L).tolist())),
                'laplacian_spectrum':[(str(v),m) for v,m in eig],'exact_moments':moments}
    graphs={'radial':graph(12,model.radial_pairs),'edge_line':graph(30,model.edge_pairs,True)}
    J=[]
    for i in range(1,13):
        r=[zero]*40
        for a in range(3):r[1+3*i+a]=model.vertices[i][a]/R2;r[1+a]=-model.vertices[i][a]/R2
        J.append(r)
    for i,j in model.edges:
        r=[zero]*40;v=ico.sub(model.vertices[i],model.vertices[j])
        for a in range(3):r[1+3*i+a]=v[a];r[1+3*j+a]=-v[a]
        J.append(r)
    D=[[x-y for x,y in zip(J[i],J[j])] for i,j in model.pairs]
    redge=rank(D[30:]);rfull=rank(D);assert redge==29 and rfull==32
    kernel=[[one]+[zero]*39,[zero]+[x for v in model.vertices for x in v]]
    for a in range(3):
        r=[zero]*40
        for i in range(13):r[1+3*i+a]=one
        kernel.append(r)
    for a in range(3):
        unit=[Q(int(i==a)) for i in range(3)];r=[zero]*40
        for i,v in enumerate(model.vertices):
            for j,x in enumerate(ico.cross(unit,v)):r[1+3*i+j]=x
        kernel.append(r)
    assert rank(kernel)==8
    assert all(sum(x*y for x,y in zip(row,v))==zero for row in D for v in kernel)
    # Check derivative assembly against a separately built exact matrix.
    numeric=np.array([[float(x) for x in row] for row in D]);error=float(np.max(abs(numeric-model.rows(model.initial[:40]))))
    assert error<3e-15
    result={'status':'PASS','coefficient_field':'Z graph incidence;Q(sqrt5) strain derivatives','graphs':graphs,
            'edge_only_derivative_rank':redge,'combined_derivative_rank':rfull,'kernel_dimension':8,
            'kernel':'six rigid spatial motions plus internal alpha and uniform radial scale',
            'auxiliary_coordinates':150,'total_configuration_coordinates':190,'phase_coordinates':380,
            'derivative_crosscheck_error':error,
            'linear_stability_proof':'Positive total quadratic energy and gamma>0 force any undamped nonzero-frequency mode to have z=0. Auxiliary equations then give D*x=0. Exact kerD is collective+rigid; symmetric parent K,M preserve that space. Therefore all32shape+150auxiliary modes have strictly negative-real poles,for every positive mu,kappa,gamma;two collective oscillators and sixrigid motions remain.',
            'scope':'default symmetric mechanical properties and ideal reciprocal difference ratios;local equilibrium linearization,not finite-amplitude/global attraction'}
    out.mkdir(parents=True,exist_ok=True);(out/'exact.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);main(p.parse_args().out)
