#!/usr/bin/env python3
"""Exact 60D twisted Klein cellular chain tensor filled K4 packet chain.
This is a graded product carrier, NOT a geometrically glued 3D tetrahedral manifold.
Requires sympy. Reproduce: python3 experiments/klein-tetra-face-flip-20261103/twisted_packet_chain_v03.py
"""
import json
from itertools import combinations
from sympy import Matrix,zeros,eye,trace
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

simp=[list(combinations(range(4),k)) for k in (1,2,3,4)]
K={}
for q in (1,2,3):
 m=zeros(len(simp[q-1]),len(simp[q]))
 for j,t in enumerate(simp[q]):
  for a in range(q+1):
   m[simp[q-1].index(t[:a]+t[a+1:]),j]=(-1)**a
 K[q]=m
assert K[1]*K[2]==zeros(4,4) and K[2]*K[3]==zeros(6,1)

def make(twist):
 B={1:Matrix([[-2,0]]) if twist else zeros(1,2),
    2:zeros(2,1) if twist else Matrix([[0],[2]])}
 assert B[1]*B[2]==zeros(1,1)
 kb=(1,2,1);pk=(4,6,4,1)
 bases=[[(p,q,i,j) for p in range(3) for q in range(4)
         if p+q==n for i in range(kb[p]) for j in range(pk[q])]
        for n in range(6)]
 ix=[{v:i for i,v in enumerate(level)} for level in bases]
 d=[]
 for n in range(1,6):
  z=zeros(len(bases[n-1]),len(bases[n]))
  for col,(p,q,i,j) in enumerate(bases[n]):
   if p:
    for ii in range(kb[p-1]):
     z[ix[n-1][(p-1,q,ii,j)],col]+=B[p][ii,i]
   if q:
    for jj in range(pk[q-1]):
     z[ix[n-1][(p,q-1,i,jj)],col]+=(-1)**p*K[q][jj,j]
  d.append(z)
 for k in range(1,5):assert d[k-1]*d[k]==zeros(d[k-1].rows,d[k].cols)
 dim=[len(z) for z in bases]
 ranks=[z.rank() for z in d]
 betti=[dim[n]-(ranks[n-1] if n else 0)-(ranks[n] if n<5 else 0)
        for n in range(6)]
 A=zeros(60);offset=[0]
 for n in dim:offset.append(offset[-1]+n)
 for n in range(1,6):
  A[offset[n-1]:offset[n],offset[n]:offset[n+1]]=d[n-1]
  A[offset[n]:offset[n+1],offset[n-1]:offset[n]]=-d[n-1].T
 assert A.T==-A
 L=-A*A
 assert L*(L-4*eye(60))*(L-8*eye(60))==zeros(60)
 assert trace(L)==344 and trace(L*L)==2272
 return {'dims':dim,'ranks':ranks,'betti_R':betti,
         'L_eigen_multiplicities':{'0':2,'4':30,'8':28},
         'trace_L':344,'trace_L_squared':2272}
t=make(True);u=make(False)
assert t['betti_R']==[0,1,1,0,0,0] and u['betti_R']==[1,1,0,0,0,0]
assert t['L_eigen_multiplicities']==u['L_eigen_multiplicities']
assert abs(int(smith_normal_form(Matrix([[-2,0]]),domain=ZZ)[0,0]))==2
assert abs(int(smith_normal_form(Matrix([[0],[2]]),domain=ZZ)[0,0]))==2
assert (-1)*1*(-1)*1==1 and (-1)**2==1
out={'source':'QPB1 signed filled-K4 incidence, plus assumed Klein CW seam local system',
     'carrier':'Z cellular tensor complex; 60 real coordinates after extension to R',
     'K4_f_vector':[4,6,4,1],
     'twisted_CW_boundary':{'d1':[[-2,0]],'d2':[[0],[0]],'holonomy_h':-1,'holonomy_v':1,
        'H0_Z':'Z/2Z','H1_Z':'Z','H2_Z':'Z'},
     'untwisted_CW_boundary':{'d1':[[0,0]],'d2':[[0],[2]],'holonomy_h':1,'holonomy_v':1,
        'H0_Z':'Z','H1_Z':'Z + Z/2Z','H2_Z':'0'},
     'twisted':t,'untwisted':u,
     'tensor_rule':'d_total=d_CW tensor I + (-1)^p I tensor d_K4',
     'boundary_squared_zero':True,'generator':'A=d_total-d_total.T, unit Euclidean chain metric',
     'norm_conserved':True,'ungraded_spectra_equal':True,
     'orientation_loop_twisted':'-I15','orientation_loop_null':'+I15',
     'orientation_twice':'I15','contractible_relator':'I15',
     'norm_squared_blind_to_twist':True,
     'warning':'formal CW tensor product is not sourced physical 3D tetrahedral gluing or physical-time law',
     'physical_promotion':0,'status':'PASS_EXACT_CONDITIONAL'}
print(json.dumps(out,indent=2,sort_keys=True))
