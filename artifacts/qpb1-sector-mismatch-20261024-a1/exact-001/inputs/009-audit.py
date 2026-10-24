"""Exact typed history adapters. Graph walks and Weyl words are proposed inputs,not native events."""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
import argparse,hashlib,importlib.util,json
ROOT=Path(__file__).resolve().parents[2]
sp=importlib.util.spec_from_file_location('fp',ROOT/'experiments/qpb1-finite-pairing/audit.py')
fp=importlib.util.module_from_spec(sp);sp.loader.exec_module(fp)
mm,mv,tr,dot=fp.mm,fp.mv,fp.tr,fp.dot
D=fp.GROUP;Z=(0,0);add=fp.plus;neg=fp.neg
b4=lambda x,y:(2*x[0]*y[0]-x[0]*y[1]-x[1]*y[0]+2*x[1]*y[1])%4
parity=lambda x:0 if x[0]%2==x[1]%2==0 else 2
save=lambda p,x:p.write_text(json.dumps(x,indent=2)+'\n')


def main(out):
 out.mkdir(parents=True,exist_ok=True);here=Path(__file__).resolve().parent
 sources=json.loads((here/'SOURCES.json').read_text())
 for s in sources['sources']:assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256']
 ledger=json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())
 byid={r['id']:r for r in ledger['rows']};rows=json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
 assert all(byid[r['id']]==r for r in rows)
 edges=list(combinations(range(4),2));ix={e:i for i,e in enumerate(edges)}
 L=[[F(x) for x in r] for r in [[1,1,0],[-1,0,1],[0,-1,-1],[1,0,0],[0,1,0],[0,0,1]]]
 G=mm(tr(L),L);Gi=fp.inv(G);uv=[[r[i] for r in Gi] for i in range(2)]
 delta={x:tuple((x[0]*a+x[1]*c)%1 for a,c in zip(*uv)) for x in D};back={v:k for k,v in delta.items()}
 basis=[[F(i==j) for i in range(6)] for j in range(6)]
 edge_classes=[back[tuple(v%1 for v in mv(Gi,mv(tr(L),e)))] for e in basis]
 K=[[x[j] for x in edge_classes] for j in range(2)]
 kappa=lambda p:tuple(int(sum(K[j][i]*p[i] for i in range(6)))%4 for j in range(2))
 b1=[[F(int(v==j)-int(v==i)) for i,j in edges] for v in range(4)]
 pl=fp.lat.field.scale(mm(tr(b1),b1),F(1,4));pt=fp.lat.field.add(fp.lat.eye(6),fp.lat.field.scale(pl,-1))
 C=[r[1:] for r in tr(b1)]
 assert all(kappa([r[j] for r in L])==Z and kappa([r[j] for r in C])==Z for j in range(3))
 actions=[];edge_matrices=[];perms=list(permutations(range(4)))
 for perm in perms:
  R=fp.lat.field.representation(edges,perm);RF=mm(mm(Gi,tr(L)),mm(R,L))
  act={x:back[tuple(v%1 for v in mv(RF,list(delta[x])))] for x in D};actions.append(act);edge_matrices.append(R)
  assert all(kappa(mv(R,p))==act[kappa(p)] for p in basis)
 # Native15-register Hodgecarrier:sourceclockn and supporta are S4 scalars.
 simplices=[list(combinations(range(4),k)) for k in range(1,5)]
 all_s=[s for block in simplices for s in block];si={s:i for i,s in enumerate(all_s)}
 boundary=fp.lat.zero(15,15)
 for ss in all_s:
  if len(ss)>1:
   for j in range(len(ss)):boundary[si[ss[:j]+ss[j+1:]]][si[ss]]=F((-1)**j)
 A=fp.lat.field.add(boundary,fp.lat.field.scale(tr(boundary),-1));A2=mm(A,A)
 P=fp.lat.field.scale(A2,F(-1,4));J=fp.lat.field.scale(A,F(1,2))
 assert fp.lat.rank(P)==14 and mm(J,J)==fp.lat.field.scale(P,-1)
 native_symmetries=0
 for perm in perms:
  R=fp.lat.field.representation(all_s,perm)
  assert mm(tr(R),R)==fp.lat.eye(15) and mm(R,A)==mm(A,R)
  native_symmetries+=1
 fixed=[x for x in D if all(act[x]==x for act in actions)];assert fixed==[Z]
 fixed_characters=[t for t in D if all(b4(t,act[x])==b4(t,x) for act in actions for x in D)];assert fixed_characters==[Z]
 # All256 module endomorphisms;commuting with S4 leaves only scalar maps.
 endomorphisms=[]
 for a,b,c,d in product(range(4),repeat=4):
  f=lambda x:((a*x[0]+b*x[1])%4,(c*x[0]+d*x[1])%4)
  if all(f(act[x])==act[f(x)] for act in actions for x in [(1,0),(0,1)]):endomorphisms.append([a,b,c,d])
 assert endomorphisms==[[k,0,0,k] for k in range(4)]
 # Projection is a homomorphism with kernel Gamma+Lambda;kernel proof andindex16 inREADME.
 projections=0;kernel_checks=0
 for p in product(range(2),repeat=6):
  pp=list(map(F,p));projected=mv(pt,pp);coord=mv(Gi,mv(tr(L),pp))
  assert kappa(p)==back[tuple(v%1 for v in coord)]
  in_kernel=all(v.denominator==1 for v in coord);assert (kappa(p)==Z)==in_kernel
  if in_kernel:
   assert all(v.denominator==1 for v in projected)
   assert all((a-b).denominator==1 for a,b in zip(pp,projected));kernel_checks+=1
  projections+=1
 assert {kappa(p) for p in product(range(4),repeat=3) for p in [[0,0,0,*p]]}==set(D)
 directed={}
 for i,j in permutations(range(4),2):
  e=ix[tuple(sorted((i,j)))];sgn=1 if i<j else -1
  directed[i,j]=edge_classes[e] if sgn==1 else neg(edge_classes[e])
 assert len(set(directed.values()))==12
 assert all(4%4==0 and add(x,x)!=Z for x in directed.values())
 # Every graphwalk up tolength6;all endpoints,backtracks andclosed cyclesincluded.
 paths=[];closed=0;range_seen=set();triangle=[]
 for length in range(7):
  for start in range(4):
   def grow(word):
    if len(word)==length+1:yield word;return
    for v in range(4):
     if v!=word[-1]:yield from grow(word+[v])
   for word in grow([start]):
    p=[0]*6
    for i,j in zip(word,word[1:]):p[ix[tuple(sorted((i,j)))]]+=1 if i<j else -1
    x=kappa(p);expected=Z if word[-1]==start else directed[start,word[-1]]
    assert x==expected
    rho=mv(b1,list(map(F,p)));assert rho==[F(int(v==word[-1])-int(v==start)) for v in range(4)]
    # Edgewise signconnection versusendpointquadraticobservable.
    link_turns=(2*length)%4;endpoint_turns=parity(x)
    assert link_turns==(2*sum(p))%4
    if word[-1]==start:closed+=1;assert x==Z
    if word==[0,1,2,0]:
     assert link_turns==2 and endpoint_turns==0;triangle=word
    range_seen.add(x);paths.append({'vertices':word,'chain':p,'class':x,'link_turns':link_turns})
 assert len(paths)==4372 and closed==1096 and len(range_seen)==13 and triangle
 # Endpointparityquadraticcocycle;notacharacter. Three paritylabels areopposite-edgematchings.
 parity_failures=0
 for x,y in product(D,repeat=2):
  assert parity(add(x,y))==(parity(x)+parity(y)+2*b4(x,y))%4
  parity_failures+=parity(add(x,y))!=(parity(x)+parity(y))%4
 assert parity_failures>0
 # Finite Weyl group inexactcentral quarter-turn coordinates:(c,x,y)represents i^c T_x M_y.
 identity=(0,Z,Z)
 def mul(g,h,k):
  c,x,y=g;d,u,v=h
  return ((c+d+k*b4(y,u))%4,add(x,u),add(y,v))
 def inverse(g,k):
  c,x,y=g
  return ((-c+k*b4(y,x))%4,neg(x),neg(y))
 def monomial(g,z,k):
  c,x,y=g;return add(z,x),(c+k*b4(y,z))%4
 def mapped(g,act):return g[0],act[g[1]],act[g[2]]
 commutator_checks=0;word_checks=0;covariance_checks=0;commutator_records=[]
 cocycle_checks=0
 for k in [1,3]:
  for x,y,z in product(D,repeat=3):
   assert k*b4(x,add(y,z))%4==k*(b4(x,y)+b4(x,z))%4;cocycle_checks+=1
  for x,y in product(D,repeat=2):
   M=(0,Z,y);T=(0,x,Z)
   g=mul(mul(mul(M,T,k),inverse(M,k),k),inverse(T,k),k)
   assert g==(k*b4(y,x)%4,Z,Z);commutator_checks+=1
   if x==(1,0) and y==(0,1):commutator_records.append({'k':k,'central_quarter_turns':g[0],'net_translation':list(g[1]),'net_modulation':list(g[2])})
  letters=[(0,(1,0),Z),(0,(0,1),Z),(0,Z,(1,0)),(0,Z,(0,1))]
  letters+= [inverse(g,k) for g in letters]
  for length in range(5):
   for word in product(range(8),repeat=length):
    g=identity
    for j in word:g=mul(g,letters[j],k)
    assert mul(g,inverse(g,k),k)==identity
    # Independentoperatorapplication onall16basisstates,rightmostletteractsfirst.
    for z in D:
     zz=z;phase=0
     for j in reversed(word):
      zz,inc=monomial(letters[j],zz,k);phase=(phase+inc)%4
     assert (zz,phase)==monomial(g,z,k)
    word_checks+=1
    if length<=3:
     for act in actions:
      h=identity
      for j in word:h=mul(h,mapped(letters[j],act),k)
      assert h==mapped(g,act);covariance_checks+=1
 # AnytwoS4-equivariant linearadapters fromonesameDchannelare (a*x,b*x),henceisotropic.
 same_channel_checks=0
 for a,c in product(range(4),repeat=2):
  f=lambda x:((a*x[0]%4,a*x[1]%4),(c*x[0]%4,c*x[1]%4))
  for x,y in product(D,repeat=2):
   tx,my=f(x);ty,mx=f(y)
   assert (b4(my,ty)-b4(mx,tx))%4==0;same_channel_checks+=1
 # Framed windingadapter H_e(n)=n*delta_e:composition,S4covariance andkernel4Z.
 frame_checks=0
 for edge,x in directed.items():
  f=lambda n:(n*x[0]%4,n*x[1]%4)
  assert all((f(n)==Z)==(n%4==0) for n in range(-8,9))
  for n,m in product(range(-4,5),repeat=2):assert f(n+m)==add(f(n),f(m))
  for perm,act in zip(perms,actions):
   for n in range(-4,5):
    z=directed[perm[edge[0]],perm[edge[1]]]
    assert act[f(n)]==(n*z[0]%4,n*z[1]%4);frame_checks+=1
 # Exactunboundedcarryrecordfornativewinding;fixedsupportconcatenationonly.
 receipts=[];carry_checks=0
 for a in [F(1,4),F(1),F(9,4)]:
  for n in range(-8,9):
   r=n%4;m=(n-r)//4;assert n==r+4*m
   assert a*n==a*(r+4*m)
   receipts.append({'support':str(a),'winding':n,'residue':r,'integer_carry':m,'action_over_pi':str(a*n)})
   for n2 in range(-8,9):
    r2=n2%4;m2=(n2-r2)//4;rc=(r+r2)%4;mc=m+m2+(r+r2)//4
    assert n+n2==rc+4*mc and a*(n+n2)==a*n+a*n2;carry_checks+=1
 assert (0%4)==(4%4) and F(0)!=F(4)
 # AllfourcentralcharactersofnativeintegerwindingremainS4invariantchoices;notD-valuedmaps.
 assert all((k*(n+m))%4==((k*n)%4+(k*m)%4)%4 for k in range(4) for n,m in product(range(-4,5),repeat=2))
 save(out/'history_maps.json',{'edge_order':[list(e) for e in edges],'kappa_matrix_mod4':K,'directed_edge_classes':[{'edge':list(e),'class':list(x)} for e,x in directed.items()],'fixed_D_subgroup':[list(x) for x in fixed],'S4_fixed_additive_characters':[list(x) for x in fixed_characters],'equivariant_endomorphisms':endomorphisms,'natural_map_kernel':'Gamma+Lambda;allintegralgraphcycleskilled','native_scalar_winding_D_map':'OnlyzeroifdependssolelyonS4-invariant(a,n)','native_scalar_winding_center_maps':'n->i^(kn),fourchoiceskmod4;notselected','single_graphwalk_image_size':len(range_seen),'frame_adapter_kernel':'4Z','continuous_state_map_scope':'AnycontinuousDvaluedadapterdefinedonallnonzeroactiveR14statesisconstantforeachn;equivarianceforceszero'})
 save(out/'path_parity.json',{'walks_checked':len(paths),'closed_walks':closed,'maximum_length':6,'triangle_witness':{'vertices':triangle,'endpoint_class':[0,0],'endpoint_parity_phase':'+1','edgewise_connection_phase':'-1'},'opposite_edge_parity_classes':[[list(e),[v%2 for v in edge_classes[j]]] for j,e in enumerate(edges)],'quadratic_composition_failures':parity_failures,'edgewise_connection':'Eachorientededgehasphase-1;backtrack+1;everytriangularfacecurvature-1;notflatonthefilledcomplex','four_face_curvature_product':'+1'})
 save(out/'weyl_words.json',{'group_law':'(c,x,y)*(d,u,v)=(c+d+k*4b(y,u),x+u,y+v)mod4','word_convention':'Listedoperatorsmultiplylefttoright;rightmostactsfirstonstate','central_commutators':commutator_records,'operator_words_checked':word_checks,'basis_states_per_word':16,'S4_word_covariance_checks':covariance_checks,'same_channel_isotropic_checks':same_channel_checks,'source_boundary':'TwocontrollableT/Mrecordtypesareadded;nodiscreteeventextractorfromnativeHodgeflowhasbeenderived'})
 save(out/'action_receipts.json',{'records':receipts,'carry_composition_checks':carry_checks,'reconstruction':'I/pi=a*(r+4m);S_native=A0*I','limitations':['Fixedsupportnativeorbitloops;changingcarrier/supportneedsseparateprocessaccounting','Nativeintegercarryisunbounded;finitephasecannotreplaceit','ActionunitA0andphysicalidentificationremainseparate']})
 result={'status':'PASS','source_hashes':len(sources['sources']),'selected_source_rows':len(rows),'S4_actions':24,'native_Hodge_symmetry_checks':native_symmetries,'fixed_D_subgroup_order':1,'endomorphisms_screened':256,'equivariant_endomorphisms':4,'projection_binary_fixtures':projections,'projection_kernel_fixtures':kernel_checks,'directed_edge_frames':12,'graph_walks':len(paths),'closed_walks':closed,'parity_composition_failures':parity_failures,'Weyl_cocycle_checks':cocycle_checks,'Weyl_commutator_checks':commutator_checks,'Weyl_words':word_checks,'Weyl_basis_state_checks':16*word_checks,'S4_word_covariance_checks':covariance_checks,'same_channel_isotropic_checks':same_channel_checks,'framed_covariance_checks':frame_checks,'action_receipts':len(receipts),'carry_composition_checks':carry_checks,'physical_score':'UNSCORED','physical_promotion':0}
 save(out/'summary.json',result);print(json.dumps(result))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
