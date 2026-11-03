#!/usr/bin/env python3
"""Independent same-runtime reconstruction of frozen witness and derivatives."""
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.optimize._numdiff import approx_derivative
from barrier_audit import VERT,EDGES,FACE,fungrad,det_grad

root=Path(__file__).resolve().parent
obj=json.loads((root/'flat_witness.json').read_text())
v=np.zeros((12,3))
for i,coords in obj['independent_vertex_coordinates_as_rationals'].items():
    v[int(i)]=[float(Fraction(t)) for t in coords]
i,j,k=obj['face_indices'];p=float(Fraction(obj['dependent_vertex']['p']));q=float(Fraction(obj['dependent_vertex']['q']))
v[k]=p*v[i]+q*v[j]
assert abs(np.linalg.det(v[[i,j,k]]))<1e-14
norm=np.linalg.norm(v,axis=1)
R=np.sqrt((5+np.sqrt(5))/8)
s=norm/R-1
L=np.linalg.norm(v[EDGES[:,0]]-v[EDGES[:,1]],axis=1)
a=float(Fraction(obj['alpha']))
E=.5*(a*a+np.sum(s*s)+.95*np.sum((s-a)**2)+.38*np.sum((L-1)**2))
assert E < .125 and abs(E-float(json.loads((root/'witness_result.json').read_text())['energy_upper_float_for_display']))<1e-7
# Derivative check near reference; use arbitrary bounded perturbation away from singularities.
rng=np.random.default_rng(20261022)
point=(VERT+.08*rng.normal(size=(12,3))).ravel()
num=approx_derivative(lambda x:fungrad(x)[0],point,method='3-point',abs_step=1e-6)
assert np.max(abs(num-fungrad(point)[1]))<1e-7
num2=approx_derivative(lambda x:det_grad(x)[0],point,method='3-point',abs_step=1e-6)
assert np.max(abs(num2-det_grad(point)[1]))<1e-7
print('PASS same-runtime independent frozen witness energy, exact-coplanarity float diagnostic, objective/constraint finite-difference gradients')
print('physical spring energy',format(E,'.15g'),'rigorous upper',json.loads((root/'witness_result.json').read_text())['energy_upper_float_for_display'])
