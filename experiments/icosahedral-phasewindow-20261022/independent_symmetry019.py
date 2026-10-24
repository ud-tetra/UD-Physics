#!/usr/bin/env python3
"""Separate SymPy-based exact icosahedral edge/anchor/face geometry audit."""
import sympy as s
import itertools,json,argparse
from pathlib import Path
Q=s.Rational;phi=(1+s.sqrt(5))/2
vertices=[]
for a,b in itertools.product([-1,1],repeat=2):vertices.append(s.Matrix([0,Q(a,2),phi*b/2]))
for a,b in itertools.product([-1,1],repeat=2):vertices.append(s.Matrix([Q(a,2),phi*b/2,0]))
for a,b in itertools.product([-1,1],repeat=2):vertices.append(s.Matrix([phi*a/2,0,Q(b,2)]))
edges=[(i,j) for i,j in itertools.combinations(range(12),2) if s.simplify((vertices[i]-vertices[j]).dot(vertices[i]-vertices[j]))==1]
E=set(edges)
faces=[f for f in itertools.combinations(range(12),3) if all((i,j) in E for i,j in itertools.combinations(f,2))]
assert len(edges)==30 and len(faces)==20
R2=(5+s.sqrt(5))/8;m2=R2-Q(1,4)
for i,j in edges:
 m=(vertices[i]+vertices[j])/2;w=(vertices[i]-vertices[j])/2
 assert s.simplify(m.dot(w))==0
 assert s.simplify(w.dot(w)-Q(1,4))==0
 assert s.simplify(m.dot(m)-m2)==0
 opp=[next(k for k in f if k not in (i,j)) for f in faces if i in f and j in f]
 assert len(opp)==2
 for k in opp:
  v=vertices[k]
  assert s.simplify(m.dot(v)-(R2-Q(1,2)))==0
  perp=s.simplify(v.dot(v)-m.dot(v)**2/m2)
  assert s.simplify(perp-m2)==0
# independently complete squares for radial energy in b-1,alpha
alpha,t=s.symbols('alpha t',real=True)
U=(alpha**2+24*t**2+12*(t-alpha)**2)/2
assert s.simplify(U- (Q(13,2)*(alpha-Q(12,13)*t)**2+Q(162,13)*t**2))==0
E=Q(13,200)+Q(51,20000000)
assert s.simplify(Q(162,13)*Q(3,40)**2-E)>0
out={'status':'PASS','spokes':12,'edges':len(edges),'faces':len(faces),'anchors_checked':4*len(edges), 'exact_geometry':True,'energy_identity':True,'all_time_strut_bound':'37/80'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path);args=p.parse_args();raw=json.dumps(out,sort_keys=True,indent=2)+'\n'
 if args.out:args.out.write_text(raw)
 print('PASS independent SymPy geometry, energy and 120-anchor checks')
 print(raw)