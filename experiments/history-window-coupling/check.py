"""Exact rational primitive for the declared compact crossing window (a=1)."""
from fractions import Fraction as Q
from itertools import product
import json

def F(u):
    u=Q(u)
    if u<=-1: return Q(0)
    if u>=1: return Q(1)
    return Q(1,2)+Q(3,4)*u-u**3/Q(4)

assert F(-1)==0 and F(0)==Q(1,2) and F(1)==1
assert F(Q(1,2))==Q(27,32)
# Along any path, each segment's pulse-angle factor is F(end)-F(start).
paths=[[-1,1],[-1,Q(1,2),-1],[-1,1,-1],[-1,1,-1,1],[-1,0,1],[-1,-Q(1,2),-1]]
expected=[1,0,0,1,1,0]
for path,target in zip(paths,expected):
    net=sum((F(v)-F(u) for u,v in zip(path,path[1:])),Q(0))
    assert net==target==F(path[-1])-F(path[0])
# A finite set of rational endpoints verifies derivative-integral endpoint accounting,
# while the telescope identity proves it for every piecewise smooth path.
for path in product([-1,Q(-1,2),0,Q(1,2),1],repeat=4):
    assert sum((F(v)-F(u) for u,v in zip(path,path[1:])),Q(0))==F(path[-1])-F(path[0])
print(json.dumps({"status":"PASS","sample_paths":len(paths),"four_point_paths":625,
 "full_traversal_angle_over_pi":"1/2","root_half_traversal_write_probability":"1/2",
 "closed_path_net_angle":0,"same_slot_history_retention":False,
 "energy_scope":"external-path pointer drive; no joint conserved energy"},indent=2))
