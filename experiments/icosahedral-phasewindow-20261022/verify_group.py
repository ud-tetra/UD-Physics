#!/usr/bin/env python3
"""Independent 60-element combinatorial rotational action + full 560-state
nonlinear force-covariance check. Numerical constructor check, not formal proof.
"""
from pathlib import Path
import argparse, json, sys
import numpy as np
import networkx as nx
sys.path.insert(0,str(Path(__file__).resolve().parent))
from nonaffine_audit import Mechanical,X,V,R2,EDGES,pairs,PROJ
from itertools import combinations

def build_actions():
 G=nx.Graph();G.add_nodes_from(range(12));G.add_edges_from((i-1,j-1) for i,j in EDGES)
 els=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
 assert len(els)==120
 base_edges={tuple(e):i for i,e in enumerate(map(tuple,EDGES))}
 pair_lookup={tuple(sorted(map(int,p))):i for i,p in enumerate(pairs)}
 out=[]
 for d in els:
  p=np.array([d[i] for i in range(12)],dtype=int)
  rt=np.linalg.lstsq(X,X[p],rcond=None)[0]
  if np.linalg.det(rt)<0:continue
  assert np.max(np.abs(X@rt-X[p]))<1e-14
  assert np.max(np.abs(rt@rt.T-np.eye(3)))<1e-14
  node=np.r_[0,p+1]
  edge=np.array([base_edges[tuple(sorted([int(node[i]),int(node[j])]))] for i,j in EDGES])
  strain=np.r_[p,edge+12]
  auxidx=[];auxsign=[]
  for a,b in pairs:
   aa,bb=int(strain[a]),int(strain[b]);k=pair_lookup[tuple(sorted((aa,bb)))]
   a2,b2=map(int,pairs[k]);sgn=1 if (aa,bb)==(a2,b2) else -1
   assert (aa,bb)==(a2,b2) or (aa,bb)==(b2,a2)
   auxidx.append(k);auxsign.append(sgn)
  assert len(set(auxidx))==150 and len(set(edge))==30
  order=1;c=np.arange(12)
  while True:
   c=p[c]
   if np.all(c==np.arange(12)):break
   order+=1;assert order<=5
  tr=np.trace(rt)
  cls=('1' if order==1 else '2' if order==2 else '3' if order==3 else ('5a' if tr>0 else '5b'))
  fixed_v=int(np.sum(p==np.arange(12)));fixed_e=int(np.sum(edge==np.arange(30)))
  out.append(dict(p=p,rt=rt,node=node,edge=edge,strain=strain,auxidx=np.array(auxidx),auxsign=np.array(auxsign),order=order,cls=cls,fixed_v=fixed_v,fixed_e=fixed_e,trR=float(tr)))
 assert len(out)==60
 return out

def transform_state(a,s):
 t=s.copy()
 for sl in [slice(0,280),slice(280,560)]:
  start=sl.start
  q=s[sl];z=np.zeros(280)
  z[0]=q[0]
  xx=q[1:40].reshape(13,3);yy=np.zeros_like(xx);yy[a['node']]=xx@a['rt'];z[1:40]=yy.ravel()
  z[a['auxidx']+40]=q[40:190]*a['auxsign']
  hh=q[190:280].reshape(30,3);hnew=np.zeros_like(hh);hnew[a['edge']]=hh@a['rt'];z[190:280]=hnew.ravel()
  t[sl]=z
 return t

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
 actions=build_actions()
 cls={}
 for a in actions:
  key=a['cls'];cls.setdefault(key,[]).append(a)
 for name,n,fv,fe,tr in [('1',1,12,30,3),('2',15,0,2,-1),('3',20,0,0,0),('5a',12,2,0,(1+np.sqrt(5))/2),('5b',12,2,0,(1-np.sqrt(5))/2)]:
  x=cls.get(name,[]);assert len(x)==n
  assert all(a['fixed_v']==fv and a['fixed_e']==fe and abs(a['trR']-tr)<1e-13 for a in x)
 rng=np.random.default_rng(20261024)
 mech=Mechanical(nu=.05,beta=.005,cf=.0005)
 y,_=mech.initial(phase='none');q=y[:280];v=y[280:560]
 q[0]=0.071;q[1:40]+=rng.normal(size=39)*.012
 q[40:190]+=rng.normal(size=150)*.008
 q[190:280]+=rng.normal(size=90)*.013
 v[:280]+=rng.normal(size=280)*.017
 assert np.min(mech.geometry(q)[-1])>.42
 state=np.r_[q,v,0.]
 rhs=mech.rhs(0,state)
 _,heat,E,_,_,_=mech.forces(q,v,energy=True)
 errors={'rhs_covariance':0.,'projected_output_covariance':0.,'energy_invariance':0.,'heat_power_invariance':0.,'isometry_of_initial_housing_phase':0.}
 for a in actions:
  y2=transform_state(a,state)
  dy2=mech.rhs(0,y2)
  dyt=transform_state(a,rhs)
  errors['rhs_covariance']=max(errors['rhs_covariance'],float(np.linalg.norm(dyt-dy2,np.inf)))
  _,heat2,E2,_,_,_=mech.forces(y2[:280],y2[280:560],energy=True)
  errors['energy_invariance']=max(errors['energy_invariance'],float(abs(E2-E)))
  errors['heat_power_invariance']=max(errors['heat_power_invariance'],float(abs(heat2-heat)))
  xx=q[1:40].reshape(13,3)[1:];xx2=y2[1:40].reshape(13,3)[1:]
  zout=PROJ@xx;znew=PROJ@xx2
  predicted=np.zeros_like(znew);predicted[a['p']]=zout@a['rt']
  errors['projected_output_covariance']=max(errors['projected_output_covariance'],float(np.max(abs(znew-predicted))))
  hu=rng.normal(size=(30,3));hv=rng.normal(size=(30,3));hh=np.zeros_like(hu);vv=np.zeros_like(hv)
  hh[a['edge']]=hu@a['rt'];vv[a['edge']]=hv@a['rt']
  errors['isometry_of_initial_housing_phase']=max(errors['isometry_of_initial_housing_phase'],float(abs(np.linalg.norm(np.r_[hh.ravel(),vv.ravel()])-np.linalg.norm(np.r_[hu.ravel(),hv.ravel()]))))
 assert max(errors.values())<5e-12,errors
 result={'status':'PASS','evidence':'NUMERICAL_CONSTRUCTOR','group_size':len(actions),'class_multiplicities':{name:len(vals) for name,vals in cls.items()},'fixed_vertex_counts':{k:int(v[0]['fixed_v']) for k,v in cls.items()},'fixed_edge_counts':{k:int(v[0]['fixed_e']) for k,v in cls.items()},'trace_R':{k:float(v[0]['trR']) for k,v in cls.items()},'max_absolute_errors':errors,'full_state_dimension':560,'output_dimension':24,'input_housing_phase_dimension':180,'auxiliary_signed_permutation':'verified 150 axes for each of 60 group elements','nu':mech.nu,'beta':mech.beta,'cf':mech.cf,'rng_seed':20261024,'interpretation':'Independent all-group numerical covariance check of complete nonlinear mechanical force including signed auxiliary transmissions. Does not prove or numerically compute full-time Green gain.'}
 args.out.parent.mkdir(exist_ok=True,parents=True);args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print('PASS all 60 A5 rotations; full560 nonlinear force equivariance, power/energy invariance, nonaffine readout covariance; error',max(errors.values()))
if __name__=='__main__':main()
