#!/usr/bin/env python3
"""Independent symbolic/numerical checks; not independent replication."""
from fractions import Fraction as F
import math
import numpy as np
import sympy as S
from scipy.integrate import quad
from pathlib import Path

# Star-incidence operator on four primary sites, acting on each Cartesian component.
B=S.Matrix([[-1,1,0,0],[-1,0,1,0],[-1,0,0,1]])
assert (B*B.T).eigenvals()=={S.Integer(1):2,S.Integer(4):1}
# Endpoint 2-component coefficient norm squared = (1+cos(t)**2)/2<=1.
c=S.symbols('c',real=True)
assert S.simplify(((1+c)**2+(1-c)**2)/4-(c**2+1)/2)==0
assert S.simplify(1+((1-c)**2)/2-(c**2-2*c+3)/2)==0
# Reference 3x3 cell gram (regular icosahedral star) in Q(sqrt5).
R2=(5+S.sqrt(5))/8
G=S.eye(3)/2+(R2-S.Rational(1,2))*S.ones(3)
eig=G.eigenvals()
assert eig=={S.Rational(1,2):2,(7+3*S.sqrt(5))/8:1}
# Rational energy, primary speed and Gram allowance independently.
E=F(1360051,20000000)
v=F(19,50)
assert 2*E/F(19,20)<v*v
assert 2*(2*v*F(9,10))**2 < F(97,100)**2
# Numerical sine lemma diagnostic only; analytic proof in PROOF.md.
for x in np.linspace(0,80*math.pi,1601):
    n=int(x/math.pi)
    r=x-n*math.pi
    val=2*n+(1-math.cos(r))
    assert val<=.75*x+1e-9,(x,val,.75*x)
# Explicit adaptive integration checks for domain of interest.
for t in [0.05,0.4,0.7,0.8,0.9]:
    I=quad(lambda s: abs(math.sin(10*s)),0,t,epsabs=1e-12,limit=200)[0]
    assert I<=.75*t+2e-10,(t,I)
margin=F(1,2)-F(41,5000)-(F(19,50)+F(47,300))*F(9,10)
assert margin==F(11,1250)
print('PASS independent star singular values, ico Gram, rational margin and sampled sine diagnostics')
