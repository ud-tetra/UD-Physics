"""Separate same-runtime symbolic audit of original pulse Duhamel safety."""
import sympy as s
T=s.symbols('T',positive=True,real=True)
tau=s.symbols('tau',nonnegative=True,real=True)
w=s.Rational(10)
cut=s.Rational(1,10)
VP=s.Rational(2,5)
FD=s.Rational(94,45)
# Independent exact integration of min(10*tau,1) for T>=.1.
A=s.simplify(w*VP*(s.integrate(w*tau*(T-tau),(tau,0,cut))+s.integrate(T-tau,(tau,cut,T))))
D=s.simplify(FD/w*(s.integrate(w*tau,(tau,0,cut))+s.integrate(1,(tau,cut,T))))
assert s.simplify(A-(2*T*T-T/s.Integer(5)+s.Rational(1,150)))==0
assert s.simplify(D-s.Rational(47,225)*(T-s.Rational(1,20)))==0
# Direct unreduced sum of all losses including uniform point motion.
loss=s.Rational(1,180)+s.Rational(3,500)+A+D+s.Rational(2,5)*T
assert s.simplify(loss-(s.Rational(7,900)+s.Rational(92,225)*T+2*T*T))==0
margin=s.simplify(s.Rational(1,2)-loss)
assert margin.subs(T,s.Rational(2,5))==s.Rational(13,1500)
assert s.simplify(s.diff(margin,T))<0
r2=(5+s.sqrt(5))/8
G=s.eye(3)/2+(r2-s.Rational(1,2))*s.ones(3)
eig=G.eigenvals()
assert eig[s.Rational(1,2)]==2
assert s.simplify(G.det())>0
# Physical-to-volume shape inequality t<=2/5 => 0.2<sigma_min proxy .7.
assert (1-2*s.Rational(2,5))**3==s.Rational(1,125)
assert (1+2*s.Rational(2,5))**3==s.Rational(729,125)
print("PASS independent SymPy kernel integrals, universal margin, and reference Gram eigenvalues")
print("A-drive-bound",A)
print("damping-bound",D)
print("strut-margin-at-T",margin.subs(T,s.Rational(2,5)))
