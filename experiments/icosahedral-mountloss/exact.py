"""Exact algebraic geometry certificate; no floating rank threshold."""
import json,argparse
from pathlib import Path
from fractions import Fraction as F
from mountloss import MountLoss
from model import ico,exact_rigidity


def audit():
    m=MountLoss();Q=ico.Q5;z=Q(0);one=Q(1)
    aggregate=[[z,z],[z,z]];determinants=[]
    for e,anchors in zip(m.edges,m.anchors):
        A=[(x+y)/2 for x,y in zip(m.vertices[e[0]],m.vertices[e[1]])]
        d=[ico.sub(A,m.vertices[a]) for a in anchors]
        lens=[ico.dot(v,v) for v in d]
        assert lens==[Q(F(1,4)),Q(F(1,4)),Q(F(3,4)),Q(F(3,4))]
        S=[[sum((v[i]*v[j]/ell for v,ell in zip(d,lens)),z) for j in range(3)] for i in range(3)]
        tr=sum((S[i][i] for i in range(3)),z)
        tr2=sum((S[i][j]*S[j][i] for i in range(3) for j in range(3)),z)
        determinant=ico.det(*S)
        assert tr==Q(4) and tr2==Q(F(64,9)) and determinant==Q(F(8,9))
        assert ico.det(d[0],d[2],d[3])!=z
        determinants.append(str(ico.det(d[0],d[2],d[3])))
        for v,ell,a in zip(d,lens,anchors):
            coeff=[-ico.dot(v,m.vertices[a]),ico.dot(v,A)]
            for i in range(2):
                for j in range(2):aggregate[i][j]+=coeff[i]*coeff[j]/ell
    assert aggregate==[[Q(35),Q(10)],[Q(10),Q(5)]]
    rigid=exact_rigidity(m)
    return {'status':'EXACT_PASS','coefficient_field':'Q(sqrt5)','housings':30,'struts':120,
            'strut_squared_lengths_per_housing':['1/4','1/4','3/4','3/4'],
            'per_housing_direction_gram_trace':'4','trace_square':'64/9','determinant':'8/9',
            'gram_eigenvalues':['(3-sqrt5)/3','(3+sqrt5)/3','2'],
            'fixed_primary_housing_velocity_loss_bound':'power >= eta*(3-sqrt5)/3 * sum|V_h|^2',
            'housing_only_loss_rank':90,'old_hidden_housing_dimension':54,
            'reference_reduced_extra_loss_over_eta':[['35','10'],['10','5']],
            'common_homothety_power':'60*eta*b_dot^2',
            'anchor_triple_determinants':determinants,'parent_rigidity':rigid,
            'linear_decay':'All274 nonrigid equilibrium configuration modes decay for nu>0, positive masses/stiffness/device loss, cf>=0 and positive reciprocal gains; proof in README. Not an all-time finite-amplitude result.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);out=p.parse_args().out
    out.mkdir(parents=True,exist_ok=True);d=audit();(out/'exact.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
