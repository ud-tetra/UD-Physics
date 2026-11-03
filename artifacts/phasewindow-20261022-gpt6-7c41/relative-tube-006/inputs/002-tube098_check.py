"""Same-runtime independent implementation of main inequalities and reference geometry.
No independent scientific replication implied.
"""
from fractions import Fraction as F
import sympy as s
from scipy.integrate import quad
import numpy as np
r2=(5+s.sqrt(5))/8
G=s.eye(3)/2+(r2-s.Rational(1,2))*s.ones(3)
assert G.eigenvals()=={s.Rational(1,2):2,(7+3*s.sqrt(5))/8:1}
E=F(1360051,20000000)
assert 2*E*F(181,200)/F(19,20) < F(9,25)**2
assert 2*E/F(9,5000)<F(35,4)**2
assert 2*F(51,20000000)/F(9,50)<F(1,180)**2
T=F(49,50)
act=quad(lambda t:abs(np.sin(10*t)),0,float(T),epsabs=1e-12,limit=100)[0]
assert act< float(F(79,125))
# Check star-incidence operator norm2 in Cartesian basis.
B=s.Matrix([[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
assert (B*B.T).eigenvals()=={s.Integer(1):2,s.Integer(4):1}
acc=F(1,18)*4*(F(35,4)+F(9,25))
L=F(1,2)-F(1,180)-F(9,25)*T-acc/F(10)*F(79,125)
assert L==F(3853,281250)>0
C=F(8)*F(9,25)**2*T*T
assert C<F(499,500)**2
print('PASS: independent SymPy geometry / scalar quadrature / rational inequalities')
