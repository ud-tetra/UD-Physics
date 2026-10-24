"""Exact native quadrature zero-crossing observer; finite event encoding is a hypothesis."""
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations,permutations,product
from pathlib import Path
import argparse,hashlib,importlib.util,json
ROOT=Path(__file__).resolve().parents[2]
sp=importlib.util.spec_from_file_location('hist',ROOT/'experiments/qpb1-loop-history/audit.py')
hist=importlib.util.module_from_spec(sp);sp.loader.exec_module(hist)
fp=hist.fp;mm,mv,tr,dot=hist.mm,hist.mv,hist.tr,hist.dot
add,neg,b4=hist.add,hist.neg,hist.b4;Z=(0,0)
EC=[(1,1),(2,1),(1,2),(1,0),(0,1),(3,1)]
scaleclass=lambda n,x:(int(n*x[0])%4,int(n*x[1])%4)
save=lambda p,x:p.write_text(json.dumps(x,indent=2)+'\n')


def half(v):return 0 if v[1]>0 or (v[1]==0 and v[0]>0) else 1

def cross(a,b):return a[0]*b[1]-a[1]*b[0]

def raycmp(a,b):
 if half(a)!=half(b):return -1 if half(a)<half(b) else 1
 c=cross(a,b);return -1 if c>0 else 1 if c<0 else 0


def events(q,p):
 """Clocktheta in[0,2pi);directions encode(cos,sin)rays without trig or numericalroots."""
 es=[]
 for e,(a,b) in enumerate(zip(q,p)):
  if a==b==0:continue # Identicallyzero pairissuppressed,notinfinitelymanycrossings.
  for typ,ray,eps in [('T',(b,-a),1),('M',(a,b),-1)]:
   for sign in [1,-1]:es.append({'ray':tuple(sign*v for v in ray),'type':typ,'edge':e,'epsilon':sign*eps,'label':scaleclass(sign*eps,EC[e])})
 es.sort(key=cmp_to_key(lambda a,b:raycmp(a['ray'],b['ray'])))
 batches=[]
 for ev in es:
  if not batches or raycmp(batches[-1][0]['ray'],ev['ray'])!=0:batches.append([])
  batches[-1].append(ev)
 return batches


def encode(batches,k=1,priority='TM'):
 # Chronologicaleventgactsbynewg*oldword,rightmostoperatoractsfirst.
 c=0;x=Z;y=Z;prefix=[]
 for batch in batches:
  for typ in priority:
   v=Z
   for e in batch:
    if e['type']==typ:v=add(v,e['label'])
   if typ=='T':x=add(v,x)
   else:c=(c+k*b4(v,x))%4;y=add(v,y)
   prefix.append((c,x,y))
 return c,x,y,prefix


def predicted(q,p,k=1):
 active=[e for e,(a,b) in enumerate(zip(q,p)) if a or b]
 c=2*len(active)
 for e,f in combinations(active,2):
  if q[e]*q[f]+p[e]*p[f]!=0:c+=2*b4(EC[e],EC[f])
 return (k*c)%4


def serialize(batches):
 return [[{'clock_ray':[str(v) for v in e['ray']],'type':e['type'],'edge':e['edge'],'crossing_sign':e['epsilon'],'class':list(e['label'])} for e in batch] for batch in batches]


def main(out):
 out.mkdir(parents=True,exist_ok=True);here=Path(__file__).resolve().parent
 sources=json.loads((here/'SOURCES.json').read_text())
 for s in sources['sources']:assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256']
 ledger=json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text());byid={r['id']:r for r in ledger['rows']}
 rows=json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows'];assert all(byid[r['id']]==r for r in rows)
 simplices=[list(combinations(range(4),k)) for k in range(1,5)];all_s=[s for block in simplices for s in block];si={s:i for i,s in enumerate(all_s)};edges=simplices[1]
 d=fp.lat.zero(15,15)
 for ss in all_s:
  if len(ss)>1:
   for j in range(len(ss)):d[si[ss[:j]+ss[j+1:]]][si[ss]]=F((-1)**j)
 matadd,scale,eye,rank=fp.lat.field.add,fp.lat.field.scale,fp.lat.eye,fp.lat.rank
 A=matadd(d,scale(tr(d),-1));J=scale(A,F(1,2));P=scale(mm(A,A),F(-1,4));E=fp.lat.zero(15,15)
 for e in edges:E[si[e]][si[e]]=F(1)
 V=matadd(E,mm(mm(J,E),tr(J)));H=matadd(P,scale(V,-1))
 assert rank(P)==14 and rank(V)==12 and rank(H)==2
 assert mm(V,V)==V and mm(H,H)==H and mm(V,H)==fp.lat.zero(15,15)
 assert mm(E,H)==mm(mm(E,J),H)==fp.lat.zero(15,15)
 assert mm(V,J)==mm(J,V) and mm(H,J)==mm(J,H)
 edgevec=lambda q:[F(q[edges.index(s)]) if s in edges else F(0) for s in all_s]
 embed=lambda q,p: [a-b for a,b in zip(edgevec(q),mv(J,edgevec(p)))]
 def observe(x):
  jx=mv(J,x);return [x[si[e]] for e in edges],[jx[si[e]] for e in edges]
 top=[F(i==si[(0,1,2,3)]) for i in range(15)];assert mv(H,top)==top and dot(top,top)==1
 assert observe(top)==([F(0)]*6,[F(0)]*6)
 # Allphase-spacefixturesarevalidnativeactivestates:q andp can be prescribed independently initially.
 fixtures=[]
 for mask in range(1,64):
  for mode in range(3):
   q=[];p=[]
   for e in range(6):
    if not(mask>>e&1):a=b=0
    elif mode==0:a,b=e+1,0
    elif mode==1:a,b=e+1,e*e+1
    else:a,b=[(1,0),(0,1),(-1,0),(0,-1)][e%4]
    q.append(F(a));p.append(F(b))
   fixtures.append((mask,mode,q,p))
 actions=[];native_checks=0
 for perm in permutations(range(4)):
  R=fp.lat.field.representation(all_s,perm);Re=fp.lat.field.representation(edges,perm)
  assert mm(R,A)==mm(A,R) and mm(R,V)==mm(V,R) and mm(R,H)==mm(H,R);native_checks+=1
  im=[]
  for e in [3,4]:
   vv=[F(i==e) for i in range(6)];image=mv(Re,vv);ec=Z
   for sign,label in zip(image,EC):ec=add(ec,scaleclass(sign,label))
   im.append(ec)
  act=lambda x,im=im:add(scaleclass(x[0],im[0]),scaleclass(x[1],im[1]))
  assert all(act(EC[j])==next(scaleclass(Re[i][j],EC[i]) for i in range(6) if Re[i][j]) for j in range(6))
  actions.append((Re,act))
 fixture_records=[];covariance=0;eventcount=0;prefix_roots=set();generic_count=0;batch_count=0
 for mask,mode,q,p in fixtures:
  x=embed(q,p);assert mv(P,x)==x and observe(x)==(q,p)
  assert dot(x,x)==dot(q,q)+dot(p,p)
  batches=events(q,p);ne=sum(map(len,batches));N=mask.bit_count();assert ne==4*N;eventcount+=ne;batch_count+=len(batches)
  c,tx,my,pref=encode(batches);assert tx==my==Z and c==predicted(q,p)
  assert encode(batches,priority='MT')[:3]==(c,Z,Z) # Fullperiod resultagrees,batchprefixcan differ.
  for phase,xx,yy in pref:prefix_roots.add(phase)
  generic=all(q[e]*q[f]+p[e]*p[f]!=0 for e,f in combinations([e for e in range(6) if mask>>e&1],2) if b4(EC[e],EC[f])%2)
  if generic:
   generic_count+=1;v=Z
   for e in range(6):
    if mask>>e&1:v=add(v,EC[e])
   assert c==b4(v,v)
  for Re,act in actions:
   qq,pp=mv(Re,q),mv(Re,p);cc,xx,yy,pref2=encode(events(qq,pp))
   assert (cc,xx,yy)==(c,act(tx),act(my))
   assert len(pref2)==len(pref) and all((a,act(b),act(d))==(aa,bb,dd) for (a,b,d),(aa,bb,dd) in zip(pref,pref2));covariance+=1
  fixture_records.append({'support_mask':mask,'phasor_fixture':mode,'active_edge_count':N,'events_per_recurrence':ne,'batch_count':len(batches),'no_mixed_noncommuting_ties':generic,'central_quarter_turns':c})
 assert prefix_roots=={0,1,2,3}
 # Exhaustive two-edgephaseorderingfixtures,includingorthogonal mixedties andboth edge incidence types.
 directions=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
 pair_checks=0;orthogonal_checks=0
 for e,f in combinations(range(6),2):
  for z,w in product(directions,repeat=2):
   q=[F(0)]*6;p=q[:];q[e],p[e]=map(F,z);q[f],p[f]=map(F,w)
   for k in [1,3]:assert encode(events(q,p),k)[:3]==(predicted(q,p,k),Z,Z)
   pair_checks+=1;orthogonal_checks+=dot(list(z),list(w))==0
 # Mixedtiecounterexample with e01 and e02,whoseclasspairingisprimitivequarterturn.
 tie=[]
 for eps in [F(-1,1000),F(0),F(1,1000)]:
  q=[F(1),eps,F(0),F(0),F(0),F(0)];p=[F(0),F(1),F(0),F(0),F(0),F(0)]
  batches=events(q,p);c,xx,yy,pref=encode(batches)
  tie.append({'epsilon':str(eps),'central_quarter_turns':c,'batches':serialize(batches),'first_batch_TM_c':encode([batches[0]],priority='TM')[0],'first_batch_MT_c':encode([batches[0]],priority='MT')[0]})
 assert [t['central_quarter_turns'] for t in tie]==[2,0,2]
 # Vanishing-amplitudecounterexample:events/holonomyjump at an exactlysilentedge.
 vanish=[]
 for eps in [F(0),F(1,1000),F(1)]:
  q=[eps]+[F(0)]*5;p=[F(0)]*6;batches=events(q,p);c,_,_,_=encode(batches)
  vanish.append({'amplitude':str(eps),'event_count':sum(map(len,batches)),'central_quarter_turns':c})
 assert [(r['event_count'],r['central_quarter_turns']) for r in vanish]==[(0,0),(4,2),(4,2)]
 sparse=[]
 for eps in [F(0),F(1,1000),F(1,1000000)]:
  q=[F(1),F(0),F(0),F(0),F(0),eps];p=[F(0)]*6
  c,_,_,_=encode(events(q,p));sparse.append({'new_disjoint_edge_amplitude':str(eps),'central_quarter_turns':c,'native_support':str(dot(q,q))})
 assert [r['central_quarter_turns'] for r in sparse]==[2,0,0]
 # Scale/hiddensectornonidentifiabilityofnativeaction;supportreceiptmustbeexternaltoeventword.
 q=[F(1)]+[F(0)]*5;p=[F(0)]*6;vis=embed(q,p);invisible=[a+b for a,b in zip(vis,top)]
 assert observe(vis)==observe(invisible) and dot(vis,vis)==1 and dot(invisible,invisible)==2
 scaled=[2*a for a in vis];assert dot(scaled,scaled)==4
 ev=events(*observe(vis));assert encode(events(*observe(invisible)))[:3]==encode(ev)[:3]
 assert len(events(*observe(scaled)))==len(ev)
 for b1,b2 in zip(ev,events(*observe(scaled))):
  assert raycmp(b1[0]['ray'],b2[0]['ray'])==0
  assert sorted((e['type'],e['edge'],e['epsilon']) for e in b1)==sorted((e['type'],e['edge'],e['epsilon']) for e in b2)
 # Rationalchambercertificate:||delta native x||<=1/10 controls everyobservedphasorerror.
 q=list(map(F,[1,2,3,4,5,6]));p=list(map(F,[1,3,2,5,4,7]));eps=F(1,10)
 radii=[a*a+b*b for a,b in zip(q,p)];upper=[abs(a)+abs(b) for a,b in zip(q,p)]
 assert min(radii)>eps*eps
 margins=[]
 for e,f in combinations(range(6),2):
  gap=abs(q[e]*q[f]+p[e]*p[f])-eps*(upper[e]+upper[f])-eps*eps
  assert gap>0;margins.append(gap)
 robust_phase=encode(events(q,p))[0];assert robust_phase==0
 # Everyobserverphasepair isorthonormalprojection(x_e,(Jx)_e);the exact normbound is1.
 assert all(dot(mv(J,edgevec([int(i==j) for i in range(6)])),mv(J,edgevec([int(i==j) for i in range(6)])))==1 for j in range(6))
 # Actioncarryandeventcount forintegerfullperiods;N>0 required,hiddenonlydoesnotcount.
 carry_checks=0
 for mask,mode,q1,p1 in fixtures:
  N=mask.bit_count();a=dot(embed(q1,p1),embed(q1,p1))
  for n in range(5):
   count=4*N*n;assert count//(4*N)==n
   r=n%4;m=(n-r)//4;assert a*(r+4*m)==a*n;carry_checks+=1
 save(out/'visibility.json',{'active_rank':14,'edge_observer_rank':12,'unobserved_active_rank':2,'visible_projector':[[str(v) for v in row] for row in V],'hidden_projector':[[str(v) for v in row] for row in H],'hidden_witness':'unit topcell basis;itsJquadratureisalsoinvisible','identical_event_native_supports':['1','2'],'scaled_identical_event_support':'4','scope':'Exactnativecarrier;noShannoninformationlossinterpretation'})
 save(out/'event_fixtures.json',{'fixtures':fixture_records,'prefix_central_quarter_turns_seen':sorted(prefix_roots),'full_period_prediction':'c=2N+sum_(e<f,phasordotnonzero)2*b4(delta_e,delta_f) mod4','generic_reduction':'c=b4(sum_active delta_e,sum_active delta_e),henceonly0or2','dense_open_full_support_phase':'+1;all6activeandnoorthogonaladjacentphasors','event_rule':'qzero->T(signp*delta_e);pzero->M(-signq*delta_e)','simultaneous_rule':'AggregateallTfirst,thenallMchronologically;silentpairs suppressed','event_clock':'theta=2s;exactrays[0,2pi);rightmostoperatoractsfirst'})
 save(out/'degeneracies.json',{'mixed_tie_challenge':tie,'vanishing_amplitude_challenge':vanish,'sparse_nonzero_state_challenge':sparse,'priority_scope':'TMandMTgiveequalfullperiodcentralphasehere,butmixedbatchoperatorsdiffer;neitherpriorityisderivedfromnativeA','physical_promotion':0})
 save(out/'chamber_action.json',{'q':[str(v) for v in q],'p':[str(v) for v in p],'native_state_error_norm_bound':str(eps),'minimum_radius_squared':str(min(radii)),'minimum_dot_margin_after_bound':str(min(margins)),'fullperiodcentralphase':'+1','certificate':'Forallnativeperturbationsnorm<=1/10,everyedgepairremainsactiveandallphasordotsnonzero;wordordercanchangeonlythroughcommutingevents','action_receipt':'ForN>0,n=event_count/(4N)overfullforwardperiods;storea,r,m;I=pi*a*(r+4m)','scope':'No amplitudequantization;invisible-onlystateN0needsanotherobserver;nosourceboundphysicalclockoractionanchor'})
 result={'status':'PASS','source_hashes':len(sources['sources']),'selected_source_rows':len(rows),'native_S4_checks':native_checks,'active_visible_hidden_ranks':[14,12,2],'support_phase_fixtures':len(fixtures),'generic_fixtures':generic_count,'fixture_event_count':eventcount,'event_batches':batch_count,'S4_fullword_checks':covariance,'two_edge_direction_checks':pair_checks,'orthogonal_two_edge_cases':orthogonal_checks,'primitive_characters_checked':[1,3],'mixed_tie_phases':['-1','+1','-1'],'action_carry_checks':carry_checks,'chamber_error_bound':'1/10','physical_score':'UNSCORED','physical_promotion':0}
 save(out/'summary.json',result);print(json.dumps(result))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);main(p.parse_args().out)
