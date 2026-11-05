"""Exact wider-box and independent-error certificate, inherits affine.py."""
from affine import *
from math import isqrt

def upper(M):
    X=mm(Hi,mm(tr(M),mm(H,M)))
    z=sum(X[i][i] for i in range(n))
    assert z>=0
    return isqrt(z.numerator//z.denominator)+1

radius=F(1,4000000)
kappa=sum(upper(mm(Hi,k)) for k in ks)
d0=max(sum(upper(d) for d in ds) for _,ds,_,_,_ in cases)
assert (kappa,d0)==(58,27)
a=kappa*radius
equiv=(1+a)/(1-a) # upper bound for sqrt of this ratio also
delta=d0*radius/(1-a)
D=equiv*(d0+kappa*delta)/(1-a)
K=equiv*kappa/(1-a)
assert D<28 and K<59
# H-skew operator norm equals spectral radius, bounded by infinity norm.
assert F(77,10)+57*radius/(1-153*radius)<8
T=t+F(5,2)*radius
L=T*2*59*28+T*T*28**2+5*28*(1+8*T)+400
assert L<9200 and 210*(err+L*radius)<F(1,2)
jitter_window=F(1,100000)
caps=[]
for i,ti in schedule:
    g,_,r,s,_=cases[i]
    p=s
    slope=F(0)
    for m in range(81):
        slope+=mm(r,mm(g,p))[0][0]
        p=[[ti*v[0]/(m+1)] for v in mm(g,p)]
    bound=abs(slope)+tail_time+28*(1+8*t)*radius+64*(F(5,2)*radius+jitter_window)
    caps.append(F((1000*bound).numerator//(1000*bound).denominator+1,1000))
assert ni(H)+radius*sum(map(ni,ks))<4
print('radius',radius,'inverse <=420','slope caps',list(map(str,caps)))
print('combined per-return allowance',radius/1680)
