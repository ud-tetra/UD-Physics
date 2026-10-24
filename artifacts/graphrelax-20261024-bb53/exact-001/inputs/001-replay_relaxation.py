#!/usr/bin/env python3
"""Exact rational passive first-harmonic null and source-rounded shear ratio."""
import json
from fractions import Fraction


def harmonic_balance(z, amplitude=Fraction(1)):
    """tau*qdot+q=amplitude*cos(omega*t), z=omega*tau."""
    c = amplitude / (1 + z*z)
    s = amplitude*z / (1 + z*z)
    assert c + z*s == amplitude
    assert s - z*c == 0
    # kappa=eta=lambda=k=1 implies tau=1, omega=v=z and A=amplitude.
    mean_force = -amplitude*s/2
    dissipated_power = z*z*(c*c+s*s)/2
    assert -mean_force*z == dissipated_power
    return {"z":str(z),"cos_coefficient":str(c),"sin_coefficient":str(s),
            "mean_force":str(mean_force),"dissipated_power":str(dissipated_power)}


shear_21, shear_31 = Fraction(13900), Fraction(6680)  # source-rounded Pa
static_ratio = shear_21/shear_31
drag_ratio = static_ratio*static_ratio
assert static_ratio == Fraction(695,334)
assert drag_ratio == Fraction(483025,111556)
rows = [harmonic_balance(z) for z in (Fraction(0),Fraction(1,2),Fraction(1),Fraction(2))]
print(json.dumps({"status":"PASS_EXACT_PASSIVE_RELAXATION_NULL",
    "model":"E=U0(x)+kappa*q^2/2-lambda*A*q*cos(k*x); eta*qdot=-partial_q E; tau=eta/kappa; x=v*t",
    "drag_law":"<F>=-lambda^2*A^2*k^2*tau*v/[2*kappa*(1+(k*v*tau)^2)]",
    "low_velocity_gamma":"lambda^2*eta*(A*k)^2/(2*kappa^2)",
    "load_log_slope":"2lambda'/lambda+eta'/eta+2G'/G-2kappa'/kappa; G=A*k, nonzero factors",
    "source_rounded_rigid_static_shear_Pa":{"(2,1)":"13900","(3,1)":"6680"},
    "conditional_shared_bath_drag_ratio_7_over_13":str(drag_ratio),
    "ratio_decimal_from_rounded_values":round(float(drag_ratio),6),
    "ratio_scope":"only if same effective area-per-atom conversion and lambda,eta,kappa at both angles, same low-speed regime, G proportional to Table 6 rigid ideal shear; neither measured friction nor UD-specific",
    "harmonic_balance_unit_parameters":rows},indent=2))
