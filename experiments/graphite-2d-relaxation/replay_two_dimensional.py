#!/usr/bin/env python3
"""Exact first-star symmetry moments and source-rounded 2D drag contrast."""
import json
from fractions import Fraction


def moments(squared_dots):
    return [sum(d**j for d in squared_dots) for j in (1, 2, 3)]


# Three wavevector axes at 0, 120, 240 degrees. Squared directional
# cosines at phi=0 and phi=30 degrees are exact rational numbers.
axis = [Fraction(1), Fraction(1,4), Fraction(1,4)]
halfway = [Fraction(3,4), Fraction(0), Fraction(3,4)]
tensor_xx = Fraction(1) + Fraction(1,4) + Fraction(1,4)
tensor_yy = Fraction(0) + Fraction(3,4) + Fraction(3,4)
tensor_xy_in_units_sqrt3 = -Fraction(1,4) + Fraction(1,4)
assert (tensor_xx,tensor_yy,tensor_xy_in_units_sqrt3) == (Fraction(3,2),Fraction(3,2),Fraction(0))
assert moments(axis) == [Fraction(3,2),Fraction(9,8),Fraction(33,32)]
assert moments(halfway) == [Fraction(3,2),Fraction(9,8),Fraction(27,32)]


def normalized_power(squared_dots, z):
    # P/(C*g^2*v^2) for z=g*v*tau, C=lambda^2*U1^2*tau/(2*kappa).
    return sum(d/(1+z*z*d) for d in squared_dots)


u7, u13 = Fraction('0.0793'), Fraction('-0.00598') # Table 4 rigid, micro-eV/atom
ratio = (u7/u13)**2 * Fraction(7,13) # g_N^2 proportional to N
assert ratio == Fraction(651175,6877)
at_z_1 = [normalized_power(ds,Fraction(1)) for ds in (axis,halfway)]
assert at_z_1 == [Fraction(9,10),Fraction(6,7)]
print(json.dumps({"status":"PASS_EXACT_2D_FIRST_STAR_RELAXATION",
 "source":"Lebedeva et al. arXiv:2511.01338v1 Eq.(2), Eq.(2) wavevectors, Table 4 rigid U1; source rounded",
 "three_wave_PES":"U1*[cos(g1.r)+cos(g2.r)+cos(g3.r)], equal |gj|=4*pi*sqrt(N)/(sqrt(3)*a)",
 "drag_tensor_low_speed":"Gamma=lambda^2*eta*U1^2/(2*kappa^2)*sum_j(gj tensor gj)=3*lambda^2*eta*U1^2*g^2/(4*kappa^2)*I2",
 "normalized_power_series":"P/(C*g^2*v^2)=3/2-(9/8)z^2+(15/16+3/32*cos(6phi))z^4+O(z^6), z=g*v*tau",
 "unit_wavevector_dyad_xx_yy_xy_over_sqrt3":[str(tensor_xx),str(tensor_yy),str(tensor_xy_in_units_sqrt3)],
 "moments_axis_0":[str(x) for x in moments(axis)],
 "moments_axis_30_degrees":[str(x) for x in moments(halfway)],
 "power_axis_0_at_z_1":str(at_z_1[0]),"power_axis_30_at_z_1":str(at_z_1[1]),
 "rigid_U1_micro_eV_per_atom":{"N7":"0.0793","N13":"-0.00598"},
 "conditional_shared_bath_gamma7_over_gamma13":str(ratio),
 "ratio_decimal_from_rounded_values":round(float(ratio),6),
 "scope":"identical independent Debye modes at each first-star wavevector; same lambda,eta,kappa and participating per-atom transfer across angles; low speed; no force measurement or UD residual"},indent=2))
