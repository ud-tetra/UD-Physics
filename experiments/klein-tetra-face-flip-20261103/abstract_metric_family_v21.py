#!/usr/bin/env python3
"""Independent exact direct-sum proof control for continuous metric nonuniqueness.
Not another K4 empirical test; demonstrates the algebraic mechanism without K4 data.
"""
import sympy as s
D0=s.Matrix([[0,1],[0,0]])
D1=s.diag(D0,D0)
F=s.Matrix([[1,0],[0,1],[0,0],[0,0]])
P=F.T
Q=s.eye(4)-F*P
t=s.symbols('t',real=True,positive=True)
H=P.T*P+t*Q.T*Q
A0=D0-D0.T
At=s.simplify(D1-H.inv()*D1.T*H)
assert D1*F==F*D0 and P*D1==D0*P
assert F.T*H*F==s.eye(2)
assert At==s.diag(A0,A0) and not At.has(t)
assert At.T*H+H*At==s.zeros(4)
assert At*F==F*A0
print('PASS_EXACT: for all t>0, H=diag(1,1,t,t) isometric and At independent of t; not a physical source law')
