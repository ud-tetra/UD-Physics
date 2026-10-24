"""Exact discriminant phases; no physical action normalization or quantum dynamics inferred."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import argparse, hashlib, importlib.util, json
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('lat',ROOT/'experiments/qpb1-integral-duality/audit.py')
lat=importlib.util.module_from_spec(spec);spec.loader.exec_module(lat)
mm,mv,tr,dot,inv=lat.mm,lat.mv,lat.tr,lat.dot,lat.inv
GROUP=list(product(range(4),repeat=2));ZERO=(0,0)
plus=lambda x,y:tuple((a+b)%4 for a,b in zip(x,y))
neg=lambda x:tuple((-a)%4 for a in x)
# Turns modulo1, not radians; Z4 is a ring, not a field.
b=lambda x,y:F(2*x[0]*y[0]-x[0]*y[1]-x[1]*y[0]+2*x[1]*y[1],4)%1
qbase=lambda x:F(x[0]**2+x[1]**2-x[0]*x[1],4)%1
save=lambda p,x:p.write_text(json.dumps(x,indent=2)+'\n')


def main(out):
 out.mkdir(parents=True,exist_ok=True);here=Path(__file__).resolve().parent
 sources=json.loads((here/'SOURCES.json').read_text())
 for s in sources['sources']:assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256']
 ledger=json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())
 rows=json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows'];byid={r['id']:r for r in ledger['rows']}
 assert all(byid[r['id']]==r for r in rows)
 L=[[F(x) for x in row] for row in [[1,1,0],[-1,0,1],[0,-1,-1],[1,0,0],[0,1,0],[0,0,1]]]
 G=mm(tr(L),L);Gi=inv(G)
 uv=[[row[i] for row in Gi] for i in range(2)]
 delta={x:tuple((x[0]*a+x[1]*c)%1 for a,c in zip(*uv)) for x in GROUP}
 back={v:k for k,v in delta.items()};assert len(back)==16
 for x,y in product(GROUP,repeat=2):
  assert b(x,y)==dot(list(delta[x]),mv(G,list(delta[y])))%1
  assert delta[plus(x,y)]==tuple((a+c)%1 for a,c in zip(delta[x],delta[y]))
 assert (2*2-(-1)*(-1))%4==3  # determinant a unit, hence perfect pairing over Z4.
 radicals=[]
 for k in range(4):
  radical=[x for x in GROUP if all((k*b(x,y))%1==0 for y in GROUP)]
  radicals.append({'k':k,'radical_size':len(radical),'radical':[list(x) for x in radical]})
 assert [r['radical_size'] for r in radicals]==[16,1,4,1]
 edges=list(combinations(range(4),2));faces=list(combinations(range(4),3));actions=[];face_actions=[]
 for perm in permutations(range(4)):
  R=lat.field.representation(edges,perm);RF=mm(mm(Gi,tr(L)),mm(R,L))
  act={x:back[tuple(v%1 for v in mv(RF,list(delta[x])))] for x in GROUP};actions.append(act)
  face_actions.append([faces.index(tuple(sorted(perm[v] for v in f))) for f in faces])
  assert all(b(act[x],act[y])==b(x,y) for x,y in product(GROUP,repeat=2))
 # Exhaustive symmetric bilinear forms on Z4^2:64 matrices,check on module generators.
 invariant=[];gens=[(1,0),(0,1)]
 for a,c,d in product(range(4),repeat=3):
  form=lambda x,y:(a*x[0]*y[0]+c*(x[0]*y[1]+x[1]*y[0])+d*x[1]*y[1])%4
  if all(form(act[x],act[y])==form(x,y) for act in actions for x,y in product(gens,repeat=2)):
   invariant.append([a,c,d])
 assert sorted(invariant)==sorted([[(2*k)%4,(-k)%4,(2*k)%4] for k in range(4)])
 # Half squared norm on the odd lattice fails descent:0 and Le1 are the same class.
 assert G[0][0]/2%1==F(1,2)
 qmaps={t:{x:(qbase(x)+b(t,x))%1 for x in GROUP} for t in GROUP}
 for q in qmaps.values():
  assert q[ZERO]==0
  assert all((q[plus(x,y)]-q[x]-q[y])%1==b(x,y) for x,y in product(GROUP,repeat=2))
 # Completeness:two refinements differ by a character;nondegenerate b lists all16characters.
 assert len({tuple(q[x] for x in GROUP) for q in qmaps.values()})==16
 homogeneous=[t for t,q in qmaps.items() if all(q[neg(x)]==q[x] for x in GROUP)]
 fixed=[t for t,q in qmaps.items() if all(q[act[x]]==q[x] for act in actions for x in GROUP)]
 assert len(homogeneous)==4 and not fixed
 keys={tuple(q[x] for x in GROUP):t for t,q in qmaps.items()};remaining=set(GROUP);orbits=[]
 while remaining:
  t=min(remaining);q=qmaps[t];orbit={keys[tuple(q[act[x]] for x in GROUP)] for act in actions}
  orbits.append({'size':len(orbit),'homogeneous_count':sum(z in homogeneous for z in orbit),'labels':[list(z) for z in sorted(orbit)]});remaining-=orbit
 assert sorted(o['size'] for o in orbits)==[4,6,6]
 # Characteristic triangular boundaries give all4 homogeneous refinements.
 char_vectors=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)],[F(1),F(-1),F(1)]]
 qfaces=[];face_labels=[]
 for ci,c in enumerate(char_vectors):
  assert all((v-1)%2==0 for v in mv(G,c))
  q={x:((dot(list(delta[x]),mv(G,list(delta[x])))-dot(list(delta[x]),mv(G,c)))/2)%1 for x in GROUP}
  label=keys[tuple(q[x] for x in GROUP)];assert label in homogeneous;face_labels.append(label);qfaces.append(q)
  # Representative shift check forall16classes and27neighboringlattice shifts.
  for x,n in product(GROUP,product(range(-1,2),repeat=3)):
   dx=[a+c0 for a,c0 in zip(delta[x],n)]
   assert ((dot(dx,mv(G,dx))-dot(dx,mv(G,c)))/2)%1==q[x]
 assert len(set(face_labels))==4
 for act,fa in zip(actions,face_actions):
  for f in range(4):assert all(qfaces[fa[f]][act[x]]==qfaces[f][x] for x in GROUP)
 # No scalar invariant choice;the face-indexed family is equivariant. Its product phase is trivial.
 assert all(sum((q[x] for q in qfaces),F(0))%1==0 for x in GROUP)
 # Squaring any homogeneous refinement removes the face choice, but degenerates the pairing.
 parity={x:(2*qfaces[0][x])%1 for x in GROUP}
 assert all((2*q[x])%1==parity[x] for q in qfaces for x in GROUP)
 assert all(parity[act[x]]==parity[x] for act in actions for x in GROUP)
 assert all(parity[x]==(F(0) if all(a%2==0 for a in x) else F(1,2)) for x in GROUP)
 assert all(parity[plus(x,y)]==parity[x] for x in GROUP for y in GROUP if all(a%2==0 for a in y))
 # Short independent obstruction:invariantq constanton12order4classes;u,v,u+v,u-v allorder4.
 # Polarization would force-a=-1/4 and-a=+1/4 simultaneously.
 assert b((1,0),(0,1))!=b((1,0),(0,3))
 # Exact finite Weyl operators on C[D],represented as basis permutations +phase turns.
 # T_x|z>=|z+x>;M_y|z>=exp(2pi i k b(y,z))|z>.
 # M_y T_x = phase(k b(y,x)) T_x M_y;verifyeveryx,y,z forbothfaithfulcharacters.
 weyl_checks=0;traces=[]
 for k in [1,3]:
  for x,y,z in product(GROUP,repeat=3):
   assert (k*b(y,plus(z,x))-k*b(y,z))%1==(k*b(y,x))%1;weyl_checks+=1
  for x,y in product(GROUP,repeat=2):
   # Trace is zero for nontrivialshift;otherwise count roots of unityexactly.
   counts=[0]*4
   if x==ZERO:
    for z in GROUP:counts[int(4*((k*b(y,z))%1))]+=1
   real,imag=counts[0]-counts[2],counts[1]-counts[3]
   assert (real,imag)==((16,0) if x==y==ZERO else (0,0))
  traces.append({'k':k,'dimension':16,'normalized_trace_identity':1,'other_Weyl_basis_traces':0})
 # A primitivefourth-root endpoint remembersnmod4,not unrestrictedactionpi*a*n.
 winding=[]
 for a in [F(1,4),F(1),F(9,4)]:
  for n in range(-4,5):
   assert F(n,4)%1==F(n+4,4)%1
   assert a*(n+4)-a*n==4*a
   winding.append({'support':str(a),'n':n,'n_plus4':n+4,'native_action_over_pi':[str(a*n),str(a*(n+4))],'phase_turns':str(F(n,4)%1)})
 # Optionaltestdictionary:normalizednativewindingactionpi*n maps toexp(i*pi*eta*n).
 # Equalitywithi^(k*n) fixeseta=k/2mod2,not anabsolutevalue. Sourceeta2 isnot adopted.
 aliases=[]
 for k in [1,3]:
  vals=[F(k,2)+2*m for m in range(3)]
  for eta in vals:
   for n in range(-4,5):assert (eta*n/2)%1==F(k*n,4)%1
  aliases.append({'k':k,'conditional_eta_congruence':str(F(k,2))+' mod2','positive_examples':[str(x) for x in vals]})
 assert F(2,2)%1==0 and F(1,4)%1!=0 and F(3,4)%1!=0
 save(out/'pairing_characters.json',{'group':'Z4xZ4','generator_pairing_matrix_over4':[[2,-1],[-1,2]],'pairing_table_turns':[[str(b(x,y)) for y in GROUP] for x in GROUP],'class_order':[list(x) for x in GROUP],'central_character_radicals':radicals,'S4_invariant_symmetric_forms_coefficients':invariant,'note':'Faithfulk1and3;integerphasesmod4;no physicalcharge oractionunit.'})
 save(out/'quadratic_refinements.json',{'base_q':'(m^2+n^2-m*n)/4 mod1','refinements':[{'character_label':list(t),'homogeneous':t in homogeneous,'phase_turns':[str(q[x]) for x in GROUP]} for t,q in qmaps.items()],'S4_orbits':orbits,'S4_fixed_refinements':[],'face_labels':[{'face':list(f),'character_label':list(t)} for f,t in zip(faces,face_labels)],'odd_lattice_descent_failure':{'same_class_representatives':['0','first triangular boundary'],'half_norm_turns':['0','1/2']},'four_face_product_phase':'identity','common_squared_refinement_turns':[str(parity[x]) for x in GROUP],'parity_quotient':'D/2D=Z2xZ2;phase+1at0,-1at3nonzeroclasses;polarization2bhasradical2Dofsize4'})
 save(out/'weyl_winding.json',{'finite_Weyl_dimension':16,'commutation_checks':weyl_checks,'trace_checks':traces,'winding_aliases':winding,'optional_Hodge_winding_dictionary':aliases,'eta2_status':'Incompatibleonlywiththeaddedprimitivefourth-root-per-Hodge-windingdictionary;notarefutationofsourceQPB1','missing_inputs':['Native loop-history-to-discriminant map','Primitive physical phase/central character rule','Typed physical action map and independent unit anchor']})
 result={'status':'PASS','source_hashes':len(sources['sources']),'selected_source_rows':len(rows),'pairing_classes':16,'pairing_pairs':256,'symmetric_forms_screened':64,'S4_actions':24,'invariant_bilinear_forms':4,'faithful_characters':[1,3],'quadratic_refinements':16,'homogeneous_refinements':4,'S4_invariant_refinements':0,'refinement_orbits':[4,6,6],'squared_refinement_quotient_classes':4,'characteristic_shift_checks':1728,'weyl_commutation_checks':weyl_checks,'Weyl_trace_checks':512,'winding_alias_checks':27,'conditional_eta_families':2,'physical_score':'UNSCORED','physical_promotion':0}
 save(out/'summary.json',result);print(json.dumps(result))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
