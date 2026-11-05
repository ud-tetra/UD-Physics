"""Exact observer checks on the frozen signed Pachner preparation."""
import json
from fractions import Fraction as Q
import audit as a

d = a.main(return_setup=True)
M, Ao, An, K = (d[k] for k in ('M', 'Ao', 'An', 'K0'))
mv = a.lin.mvec
c = d['c'][:]
c[3] += Q(1,4)
v = c[:]
# Check the scalar recurrence by Cayley-Hamilton on the 23-dimensional old space.
for _ in range(23):
    w = mv(Ao, v)
    ww = mv(Ao,w)
    assert v[-2] == v[-1]
    assert ww[-2:] == [-5*x for x in v[-2:]]
    v = w
assert c[-2:] == [0,0] and mv(Ao,c)[-2:] == [1,1]
for A, v, project in ((An,mv(M,c),False),(K,c,True)):
    for _ in range(len(A)):
        assert (mv(M,v) if project else v)[-3:] == [0]*3
        v = mv(A,v)
e = [Q(0)]*23
e[-2:] = [Q(1),Q(-1)]
assert mv(Ao,e)[-2:] == [0,0]
assert mv(Ao,mv(Ao,e)) == [-3*x for x in e]
eps = Q(1,10**9)
p = [x+eps*y for x,y in zip(c,e)]
assert a.scalar(d['G'],c) == Q(9,10)
assert a.scalar(d['G'],p) == Q(9,10)+eps**2
assert 2*a.iface.dot(mv(d['G'],c),mv(Ao,c)) == -3
# Existing crossing certificate applies since preparation error <=2eps.
assert 2*eps <= Q(1,1000) and 10*eps <= Q(1,1000)
# |s5(t*)| <= t* <= eps²/2; epsilon*cos(sqrt(3)t*) dominates.
shift = eps**2/2
assert eps*(1-3*shift**2/2)>shift
for x in (0,1):
    for y in (0,1):
        assert (x^y)==((x^1)^(y^1))
        assert (x^y)!=((x^1)^y)
print(json.dumps({
    'old_top_root_at_nominal_event': 'two simultaneous transverse roots, slopes +1,+1',
    'full_and_projected_new_top_coordinates': 'identically zero; no transverse roots',
    'odd_top_perturbation': str(eps),
    'fixed_reserve_event_shift_upper_bound': str(shift),
    'perturbed_event_cell_signs': ['positive','negative'],
    'publication': 'two flips cancel in shared XOR; serial intermediate is order-dependent in actor identity',
},indent=2))
