import sympy as s
x,y,L=s.symbols("x y L",real=True)
g=1+L*(x*x-y*y)/(x*x+y*y)
swap=g.xreplace({x:y,y:x})
assert s.simplify(g-swap-2*L*(x*x-y*y)/(x*x+y*y))==0
assert g.subs(y,0)==1+L and g.subs(x,0)==1-L
z=s.Matrix([x,y]);J=s.Matrix([[0,1],[-1,0]])
F=s.simplify(g*J*z)
assert s.simplify(z.dot(F))==0
assert s.simplify(F.subs({x:1,y:0}))==s.Matrix([0,-1-L])
assert s.simplify(F.subs({x:0,y:1}))==s.Matrix([1-L,0])
print("PASS exact directional limits, swap difference and skew conservation")
