from wider import *
fixed=[numeric_row(i,float(s)) for i,s in schedule if (i,s)!=(2,F(1,2))]
best=[]
for k in range(1,48):
    ts=F(k,32)
    j=jac(float(ts))
    for i,(g,_,r,s,_) in enumerate(cases):
        v=(arr(r)@arr(g)@expm(float(ts)*arr(g))@arr(s))[0,0]
        row=np.r_[j[i],v,float(ts)*v]
        try:q=np.linalg.norm(np.linalg.inv(np.vstack([*fixed,row])),np.inf)
        except np.linalg.LinAlgError:continue
        if q<215:best.append((max(abs(v),max(abs(u[4]) for u in fixed))*q,i,str(ts),q,v))
score,i,ts,estimate,slope=min(best)
assert (i,ts)==(0,'7/32')
print('NUMERICAL screen: 188 choices; selected channel',i+1,'time',ts,'score',float(score),'inverse estimate',float(estimate))
g,ds,r,s,_=cases[i]
ti=F(ts); p=s; d=[[[F(0)] for _ in s] for _ in ds]
row=[F(0)]*6
for m in range(81):
    v=mm(r,mm(g,p))[0][0]
    row=[a+w for a,w in zip(row,[mm(r,u)[0][0] for u in d]+[v,ti*v])]
    d=[[[ti/(m+1)*a[0]] for a in add(mm(g,u),mm(D,p))] for u,D in zip(d,ds)]
    p=[[ti/(m+1)*a[0]] for a in mm(g,p)]
Pnew=P[:4]+[row]+P[5:]
base.n=6
try: pinv=inv(Pnew)
finally: base.n=n
assert ni(pinv)<210 and 210*(err+L*radius)<F(1,2)
newcap=F(96,125)
assert abs(row[4])+tail_time+28*(1+8*t)*radius+64*(F(5,2)*radius+jitter_window)<newcap
worst=max(caps[:4]+[newcap]+caps[5:])
assert worst==F(4,5)
print('EXACT/CONDITIONAL radius',radius,'inverse <=420; replacement slope',newcap,'max slope',worst)
print('Jitter-only allowance',radius/(1680*worst),'improvement factor',F(1733,1000)/worst)
