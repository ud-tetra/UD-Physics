"""Exact K4 contact/register stock and switching-work identities."""

import itertools
import json
from fractions import Fraction as Q

edges=list(itertools.combinations(range(4),2))
B=[[(-1 if i==a else 1 if i==b else 0) for a,b in edges] for i in range(4)]
L=[[sum(B[i][e]*B[j][e] for e in range(6)) for j in range(4)] for i in range(4)]
assert L==[[4*(i==j)-1 for j in range(4)] for i in range(4)]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def energy(x,y,r):
    return (dot([a-b for a,b in zip(x,r)],[a-b for a,b in zip(x,r)])+dot(y,y))/2


def state_derivative(x,y,r,gamma):
    xd=[-sum(B[i][e]*y[e] for e in range(6)) for i in range(4)]
    yd=[sum(B[i][e]*(x[i]-r[i]) for i in range(4))-gamma*y[e] for e in range(6)]
    return xd,yd


def main():
    u=[Q(1,4)]*4
    r=[Q(1),Q(0),Q(0),Q(0)]
    y0=[Q(0)]*6
    assert state_derivative(r,y0,r,Q(1))==(y0[:4],y0)
    assert sum(u)==sum(r)==1
    # A contact picked at a symmetric state breaks S4 externally.
    initial_native=dot(u,u)
    final_native=dot(r,r)
    initial_shifted=energy(u,y0,r)
    final_shifted=energy(r,y0,r)
    assert (initial_native,final_native,initial_shifted,final_shifted)==(Q(1,4),Q(1),Q(3,8),Q(0))
    # Fixed r, gamma>0: heat integral follows from E'= -gamma ||y||².
    heat=initial_shifted-final_shifted
    native_contact_work=2*dot(r,[b-a for a,b in zip(u,r)])
    assert native_contact_work==Q(3,2)
    assert final_native-initial_native==native_contact_work-2*heat==Q(3,4)
    # Instantaneous local power checks for rational states.
    x=[Q(1,2),Q(1,4),Q(1,8),Q(1,8)]
    y=[Q(e-3,10) for e in range(6)]
    gamma=Q(2,3)
    xd,yd=state_derivative(x,y,r,gamma)
    e_dot=dot([a-b for a,b in zip(x,r)],xd)+dot(y,yd)
    s_dot=2*dot(x,xd)+2*dot(y,yd)
    assert e_dot==-gamma*dot(y,y)
    assert s_dot==2*dot(r,xd)-2*gamma*dot(y,y)
    # One-hot register switch at fixed x,y: Delta E=-x.Delta r.
    r1=[Q(0),Q(1),Q(0),Q(0)]
    assert energy(u,y0,r1)-energy(u,y0,r)==0
    assert energy(r,y0,r1)-energy(r,y0,r)==1
    assert energy(u,y0,r)-energy(u,y0,[Q(0)]*4)==Q(1,4)
    print(json.dumps({'fixed_root_equilibrium':'x=r, y=0','symmetric_initial_native_stock':str(initial_native),
                      'root_final_native_stock':str(final_native),'initial_contact_energy':str(initial_shifted),
                      'conditional_integrated_heat_gamma_positive':str(heat),
                      'contact_work_in_native_stock_units':str(native_contact_work),
                      'native_stock_gain':str(final_native-initial_native),
                      'switch_cost_at_symmetric_state':'0',
                      'zero_to_one_hot_register_energy_jump_at_symmetric_state':'1/4',
                      'switch_cost_from_exact_root_to_another_root':'1',
                      'root_contrast_from_symmetric_seed':'1-f_gamma(s), with f_gamma(0)=1; f_gamma<1 for s>0 if gamma>0'},
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
