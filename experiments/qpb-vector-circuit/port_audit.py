#!/usr/bin/env python3
"""Exact K4 source-ported charge/LC model; source energy law is hypothetical."""
import argparse,json,math
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
E=list(combinations(range(4),2)); T=list(combinations(range(4),3))
def z(m,n):return [[F(0) for _ in range(n)] for _ in range(m)]
def tr(a):return [list(r) for r in zip(*a)]
def mv(a,b):return [sum((x*y for x,y in zip(r,b)),F(0)) for r in a]
def mm(a,b):return [mv(tr(b),r) for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(a,k):return [[k*x for x in r] for r in a]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
B=z(4,6);C=z(6,4)
for k,(i,j) in enumerate(E):B[i][k]=-1;B[j][k]=1
for k,f in enumerate(T):
 for i in range(3):C[E.index(f[:i]+f[i+1:])][k]=F((-1)**i)
D=mm(C,tr(C)); PL=sc(mm(tr(B),B),F(1,4)); PT=sc(D,F(1,4));I=z(6,6)
for i in range(6):I[i][i]=1
assert mm(B,C)==z(4,4) and add(PL,PT)==I
assert mm(PL,PT)==z(6,6) and mm(PL,PL)==PL and mm(PT,PT)==PT
w=[F(1,2),0,F(-1,2),F(1,2),0,F(1,2)];j=[1,-1,0,0]
fL=[x/4 for x in mv(tr(B),j)]
assert mv(B,fL)==j and mv(PT,fL)==[0]*6
assert mv(B,w)==[0]*4 and dot(w,w)==1 and mv(D,w)==[4*x for x in w]
checks=0
for uL,uT,v in [(F(1),F(1),F(1)),(F(3),F(2),F(1,2)),(F(1,3),F(4,3),F(3,4))]:
 U=add(sc(PL,uL),sc(PT,uT))
 for k in range(8):
  a=[F((2*i+k)%7-3,5) for i in range(6)]
  p=[F((3*i+k)%9-4,7) for i in range(6)]
  psi=[F(k+i-2,11) for i in range(4)]
  f=[F(k+1,6)*x+F(k+2,10)*y for x,y in zip(fL,w)]
  ap=[x+y for x,y in zip(mv(U,p),mv(tr(B),psi))]
  pp=[-v*x+y for x,y in zip(mv(D,a),f)]
  assert mv(B,pp)==mv(B,f)
  Hd=dot(mv(U,p),pp)+v*dot(mv(D,a),ap)
  assert Hd==dot(mv(U,p),f)
  A0=F(5,3);q0=F(2,3);tau=F(7,4)
  VE=[A0/(tau*q0)*x for x in mv(U,p)]
  IE=[q0/tau*x for x in f]
  assert A0/(tau*tau)*Hd==dot(VE,IE)
  for h in (F(1,2),F(2),F(3)):
   UU=sc(U,h);vv=v/h;aa=[h*x for x in a];AA=A0/h
   assert sc(U,A0/(tau*q0*q0))==sc(UU,AA/(tau*q0*q0))
   assert sc(D,v*q0*q0/(A0*tau))==sc(D,vv*q0*q0/(AA*tau))
   assert [A0/q0*x for x in a]==[AA/q0*x for x in aa]
   assert [h*x for x in ap]==[x+y for x,y in zip(mv(UU,p),mv(tr(B),[h*t for t in psi]))]
   assert pp==[-vv*x+y for x,y in zip(mv(D,aa),f)]
  checks+=1
for ul in (F(1,2),F(1),F(3)):
 for r,rp in [(F(0),F(1)),(F(1,2),F(1,3)),(F(2),F(-1,4))]:
  p=[r*x for x in fL];pd=[rp*x for x in fL]
  assert ul*dot(p,p)/2==ul*r*r/4
  assert ul*dot(p,pd)==ul*r*rp/2
result={'status':'PASS','evidence':['EXACT','CONDITIONAL','NUMERICAL','HYPOTHESIS','FAILED','OPEN'],
 'case_count':checks,'PL_PT_ranks':[3,3],'B1B2_zero':True,
 'driven_system':'a_dot=U p+B1^T psi; p_dot=-v B2B2^T a+f; rho_dot=B1 f',
 'source_split':'fL=B1^T j/4 gives charged dipole; fT=w F gives neutral oscillatory cycle',
 'power':'Hdot=(Up)^T f and physical dE/dt=Vedge^T Iedge',
 'physical_map':'Phi=(A0/q0)a, Q=q0p, E=A0 H/tau, Cinv=A0 U/(tau q0^2), Linv=v q0^2 B2 B2^T/(A0 tau)',
 'dipole':'rho=(r,-r,0,0); H_C=uL r^2/4; Cdip=2 tau q0^2/(A0 uL)',
 'neutral':'omega_native=2sqrt(uT v), H_after=uT F^2 sinc^2(sqrt(uT v) T)/2',
 'pulse_energy_fraction':{'instant_limit':1.0,'half_period':4/math.pi**2,'full_period':0.0},
 'scale_family':'(U,v,a,A0,psi)->(hU,v/h,h a,A0/h,h psi), Q,Phi and all physical Cinv/Linv unchanged',
 'scale_fixtures':['1/2','2','3'],
 'gauge_source':'Source continuity rho_ref_dot=B1 f required for gauge-action boundary term; it is added, not native autonomous current',
 'conventional_null':'ordinary positive reciprocal coupled LC multiport with same Cinv and Linv',
 'source_physical_selection':'OPEN q0,A0,tau,uL,uT,v and current transducer; no measured physical device',
 'separate_native_space':'edge a,p real12 is not the original rank14 tetrahedral active carrier'}
if __name__=='__main__':
 q=argparse.ArgumentParser();q.add_argument('--out',type=Path,required=True);a=q.parse_args()
 a.out.parent.mkdir(parents=True,exist_ok=True)
 a.out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'status':'PASS','cases':checks},sort_keys=True))
