"""Constructor certificate; run with bip.json argument in this directory."""
from REF01_raw_return_certificate import *
import REF01_raw_return_certificate as base
schedule=[(i,t) for i in range(4)]+[(2,F(1,2)),(1,F(5,4))]
def numeric_row(i,sample):
    g,_,r,s,_=cases[i]
    slope=(arr(r)@arr(g)@expm(sample*arr(g))@arr(s))[0,0]
    return np.r_[jac(sample)[i],slope,sample*slope]
prefix=[numeric_row(i,float(ti)) for i,ti in schedule[:5]]
for trial in (F(1,4),F(3,4),F(1),F(5,4),F(2)):
    print('NUMERICAL scan',str(trial),[float(np.linalg.norm(np.linalg.inv(np.vstack([*prefix,numeric_row(i,float(trial))])),np.inf)) for i in range(4)])
P=[]
for i,ti in schedule:
    g,ds,r,s,_=cases[i]
    p=s
    d=[[[F(0)] for _ in s] for _ in ds]
    row=[F(0)]*6
    for m in range(81):
        v=mm(r,mm(g,p))[0][0]
        row=[a+w for a,w in zip(row,[mm(r,u)[0][0] for u in d]+[v,ti*v])]
        d=[[[ti/(m+1)*a[0]] for a in add(mm(g,u),mm(D,p))] for u,D in zip(d,ds)]
        p=[[ti/(m+1)*a[0]] for a in mm(g,p)]
    P.append(row)
base.n=6
try: pinv=inv(P)
finally: base.n=n
tail_time=16*F(12)**81/factorial(81)/(1-F(12,82))
err=tail+F(5,2)*tail_time
assert ni(pinv)<210 and err<F(1,10**29)
T=t+F(5,2)*rho
L=T*4*7*36000+T*T*1624**2+5*1624*(1+8*T)+64*F(25,4)
assert L<8000000 and 210*(err+L*rho)<F(1,2)
print('EXACT/CONDITIONAL inverse Lipschitz <=420; residual allowance',rho/1680)
