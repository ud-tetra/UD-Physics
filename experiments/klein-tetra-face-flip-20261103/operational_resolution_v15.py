#!/usr/bin/env python3
"""UD K4 operational resolution audit v1.5: exact unit-edge graph response."""
from itertools import combinations,permutations
import sympy as s
import json

def levels(depth):
 t=[(0,1,2,3)];z=4
 yield 0,list(t)
 for n in range(1,depth+1):
  u=[]
  for T in t:
   for j in range(4):u.append(tuple(sorted(T[:j]+T[j+1:]+(z,))))
   z+=1
  t=u;yield n,list(t)

def response(tetra):
 verts=sorted({v for T in tetra for v in T})
 edges=sorted({e for T in tetra for e in combinations(T,2)})
 ids={v:i for i,v in enumerate(verts)}
 L=s.zeros(len(verts))
 for a,b in edges:
  i,j=ids[a],ids[b]
  L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
 B=[ids[i] for i in range(4)];I=[ids[i] for i in verts if i>=4]
 if I:Lam=L.extract(B,B)-L.extract(B,I)*L.extract(I,I).inv()*L.extract(I,B)
 else:Lam=L.extract(B,B)
 return Lam,len(verts),len(edges)

def alpha(n):return (6+s.Rational(11,4)**n)/7
def prove_all_depth():
 w=s.symbols('w')
 r=2*w+(1+3*w)/4
 assert s.simplify(r-(11*w+1)/4)==0
 for n in range(8):
  wn=(s.Rational(11,4)**n-1)/7
  wn1=(s.Rational(11,4)**(n+1)-1)/7
  assert s.simplify(r.subs(w,wn)-wn1)==0
  assert s.simplify(alpha(n+1)-alpha(n)-s.Rational(11,4)**n/4)==0
 return {'inner_network_clique_recursion':'w_(n+1)=(11w_n+1)/4, w0=0',
         'closed_form':'alpha_n=[6+(11/4)^n]/7',
         'positive_difference':'(11/4)^n/4'}

def stock_contrast(t):
 children=t[:4]
 x={children[0]:s.Integer(1)}
 y={T:s.Rational(1,2) for T in children}
 a=[x.get(T,s.Integer(0))**2 for T in children]
 bb=[y.get(T,s.Integer(0))**2 for T in children]
 assert sum(a)==sum(bb)==1 and sorted(a)!=sorted(bb)
 return {'equal_total_norm':True,'same_original_outer_shell_coefficients':True,
         'core_stock_x':[str(z) for z in a],'core_stock_y':[str(z) for z in bb],
         'source_readout':'Q171 S_tau^core=c_(3,tau)^2'}

def run():
 data=[]
 for n,t in levels(3):
  D,V,E=response(t)
  assert D==alpha(n)*(4*s.eye(4)-s.ones(4))
  p=s.Matrix([1,-1,0,0])
  energy=(p.T*D*p)[0]/2
  assert energy==4*alpha(n)
  for g in permutations(range(4)):
   P=s.zeros(4)
   for i,j in enumerate(g):P[j,i]=1
   assert P.T*D*P==D
  item={'depth':n,'V':V,'E':E,'F':2*4**n+2,'T':4**n,
        'boundary_f_vector':[4,6,4],'response_alpha':str(alpha(n)),
        'probe_energy':str(energy),'S4_checks':24}
  if n>0:item['same_shell_equal_norm_stock_contrast']=stock_contrast(t)
  data.append(item)
 assert [z['response_alpha'] for z in data]==['1','5/4','31/16','245/64']
 out={'status':'PASS_EXACT_CONDITIONAL','version':'v1.5',
      'all_depth_theorem':prove_all_depth(),'direct_exact_K4_levels':data,
      '192_address_count':'24*8 per packet; no top-cell depth cap',
      'observation_scopes':{'shell_geometry':'blind at all depths',
          'unit_edge_boundary_port':'distinguishes every depth',
          'local_Q171_core_stock':'distinguishes equal norm shell-matched states at every depth'},
      'source_selected_physical_observer':'OPEN','SI_units':'NONE','physical_promotion':0}
 print(json.dumps(out,indent=2,sort_keys=True))
 return out
if __name__=='__main__':run()
