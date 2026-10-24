#!/usr/bin/env python3
"""Exact A5 character calculation for 3D UD symmetric moving-baseline tangent.

Standard-library Q(sqrt(5)); class counts verified independently by
verify_equivariance.py.  No physical interpretation assumed.
"""
import json, argparse
from fractions import Fraction as F
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class Q5:
 a:F=F(0)
 b:F=F(0)
 def __post_init__(self):object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
 def __add__(self,o):
  o=o if isinstance(o,Q5) else Q5(o);return Q5(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return Q5(-self.a,-self.b)
 def __sub__(self,o):return self+-o
 def __rsub__(self,o):return Q5(o)+-self
 def __mul__(self,o):
  o=o if isinstance(o,Q5) else Q5(o);return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __truediv__(self,o):
  o=o if isinstance(o,Q5) else Q5(o)
  n=o.a*o.a-5*o.b*o.b
  assert n!=0
  return self*Q5(o.a/n,-o.b/n)
 def __eq__(self,o):
  o=o if isinstance(o,Q5) else Q5(o);return self.a==o.a and self.b==o.b
 def __repr__(self):return f'({self.a})+({self.b})sqrt5'
 def asdict(self):return {'rational':str(self.a),'sqrt5_coefficient':str(self.b)}
ONE=Q5(1); ZERO=Q5(0);PHI=Q5(F(1,2),F(1,2));PSI=ONE-PHI
CLASSES=['1','2','3','5a','5b'];SIZES=[1,15,20,12,12]
TRACE_R=[Q5(3),Q5(-1),ZERO,PHI,PSI]
FIX_VERT=[12,0,0,2,2];FIX_EDGES=[30,2,0,0,0]
# output Z = (I - P0 - PV)Y, R3 physical Cartesian representation
# tr(P perm) = #(fixed vertices) - tr(P0 perm) - tr(PV perm)
# = fixed_vertices - 1 - traceR.
CHAR_Z=[(Q5(f)-ONE-t)*t for f,t in zip(FIX_VERT,TRACE_R)]
CHAR_H=[Q5(fe)*t for fe,t in zip(FIX_EDGES,TRACE_R)]
CHAR_PHASE=[2*c for c in CHAR_H]
assert CHAR_Z==[Q5(24),ZERO,ZERO,Q5(-1),Q5(-1)]
assert CHAR_H==[Q5(90),Q5(-2),ZERO,ZERO,ZERO]
assert CHAR_PHASE==[Q5(180),Q5(-4),ZERO,ZERO,ZERO]
# Real irreducible characters of rotational icosahedral group A5, over Q(sqrt5).
IRREPS={
 '1':(1,[ONE,ONE,ONE,ONE,ONE]),
 '3':(3,[Q5(3),Q5(-1),ZERO,PHI,PSI]),
 '3prime':(3,[Q5(3),Q5(-1),ZERO,PSI,PHI]),
 '4':(4,[Q5(4),ZERO,ONE,Q5(-1),Q5(-1)]),
 '5':(5,[Q5(5),ONE,Q5(-1),ZERO,ZERO])
}
def inner(c,d):
 v=sum((Q5(n)*x*y for n,x,y in zip(SIZES,c,d)),ZERO)/60
 assert v.b==0 and v.a.denominator==1 and v.a>=0
 return int(v.a)
# Check exact character orthonormality; ensures table has a faithful class decomposition.
for n,(dim,x) in IRREPS.items():
 for m,(_,y) in IRREPS.items():
  assert inner(x,y)==int(n==m),(n,m)
ZMULT={n:inner(CHAR_Z,seq) for n,(_,seq) in IRREPS.items()}
HMULT={n:inner(CHAR_H,seq) for n,(_,seq) in IRREPS.items()}
PHMULT={n:inner(CHAR_PHASE,seq) for n,(_,seq) in IRREPS.items()}
assert ZMULT=={'1':0,'3':1,'3prime':1,'4':2,'5':2}
assert HMULT=={'1':1,'3':5,'3prime':5,'4':6,'5':7}
assert PHMULT=={'1':2,'3':10,'3prime':10,'4':12,'5':14}
assert sum(IRREPS[k][0]*v for k,v in ZMULT.items())==24
assert sum(IRREPS[k][0]*v for k,v in HMULT.items())==90
assert sum(IRREPS[k][0]*v for k,v in PHMULT.items())==180
# The full 180-vector housing input has an invariant Euclidean mass-energy norm
# for uniform beta and housing weights. Thus L L^T is symmetric, nonnegative,
# and belongs to the A5 commutant in the 24-dimensional output representation.
# Its nonzero sectors: scalar k3 I3, k3p I3, B4 tensor I4, B5 tensor I5.
# Second-order symmetry does NOT give a small scalar bound. Sym^2 of phase
# representation has character (chi(g)^2 + chi(g^2))/2.
# g^2 classes: identity->id, order2->id, order3->order3, order5->other 5 class.
CHAR_SYM2=[(c*c+CHAR_PHASE[j])/2 for c,j in zip(CHAR_PHASE,[0,0,2,4,3])]
assert CHAR_SYM2==[Q5(16290),Q5(98),ZERO,ZERO,ZERO]
HESSIAN_EQUIVARIANT_DIM=inner(CHAR_SYM2,CHAR_Z)
assert HESSIAN_EQUIVARIANT_DIM==6516
result={
 'status':'PASS','evidence':'EXACT CONDITIONAL',
 'group':'A5 rotational icosahedral group; 60 proper rotations',
 'ordered_conjugacy_classes':CLASSES,
 'class_sizes':SIZES,'fixed_shell_vertices':FIX_VERT,'fixed_shell_edges':FIX_EDGES,
 'trace_R':[v.asdict() for v in TRACE_R],
 'output_character':[v.asdict() for v in CHAR_Z],
 'housing_coordinate_character':[v.asdict() for v in CHAR_H],
 'housing_phase_character':[v.asdict() for v in CHAR_PHASE],
 'output_multiplicities':ZMULT,'housing_coordinate_multiplicities':HMULT,'housing_phase_multiplicities':PHMULT,
 'output_decomposition':'3 + 3prime + 2*4 + 2*5',
 'housing_phase_decomposition':'2*1 + 10*3 + 10*3prime + 12*4 + 14*5',
 'commuting_gram_normal_form':'k3*I3 + k3prime*I3 + (B4 tensor I4) + (B5 tensor I5), with B4 and B5 symmetric 2x2 PSD',
 'full_phase_gain_exact_reduction':'||L(t)||_2^2 = max(k3,k3prime,lambda_max(B4),lambda_max(B5))',
 'phase_singlet_to_nonaffine_linear_gain':'zero for all t',
 'second_order_character':[v.asdict() for v in CHAR_SYM2],
 'dimension_of_equivariant_symmetric_bilinear_hessian_maps':HESSIAN_EQUIVARIANT_DIM,
 'limitations':['Group decomposition applies to exactly uniform stiffness/mass/gain/housing weights around exactly symmetric moving baseline; scattered coefficients break the symmetry.',
 'Symmetry alone does not bound coefficients k3,k3prime,B4,B5 or the nonlinear Hessian norm.',
 'No u100 continuous-time propagated gain or nonlinear all-phase/phase-ball certification.']
}
def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS exact A5 characters: Z=3+3prime+2*4+2*5; Hphase=2+10*3+10*3prime+12*4+14*5; Hessian dimension 6516')
if __name__=='__main__':main()
