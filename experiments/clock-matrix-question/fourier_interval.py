"""Rational verification of the Fourier and Cayley stability margins."""
from fractions import Fraction as F
import json
from pathlib import Path

from certified_interval import matrices, model_matrices
from stabilization_exact import add, definite_pivots, eye, mm, sc, tr


def positive(matrix):
    assert matrix == tr(matrix)
    assert all(pivot > 0 for pivot in definite_pivots(matrix))


def run():
    J, P, T = matrices()
    J = mm(J, P)
    Id = eye(len(J))
    a, b, c = F(19, 256), F(35, 64), F(3, 64)
    T2 = mm(T, T)
    negative = sc(mm(mm(add(T2, sc(P, a)), add(T2, sc(P, c))), P),
                  1 / ((a-b)*(c-b)))
    K = sc(mm(J, T), -1)
    G = add(mm(K, add(P, sc(negative, -2))), Id, sc(P, -1))
    positive(add(G, sc(Id, F(-1,20))))
    positive(add(sc(Id, F(5,4)), sc(G, -1)))
    assert add(mm(tr(T), G), mm(G, T)) == sc(Id, 0)
    assert mm(J, J) == sc(P, -1)
    assert mm(negative, negative) == negative

    _, _, Bc, Bs, Bx = model_matrices()
    constant = add(sc(add(Bc, Bs), F(1,2)), sc(Id,-1))
    cosine = sc(add(Bc, sc(Bs,-1)), F(1,2))
    sine = sc(Bx, F(1,2))

    def harmonics(D):
        D = mm(mm(P, D), P)
        JD, DJ = mm(J,D), mm(D,J)
        return (sc(add(JD,DJ), F(1,2)),
                sc(add(JD,sc(DJ,-1)), F(1,2)),
                sc(add(D,mm(JD,J)), F(1,2)))

    t0, tc, ts = harmonics(constant)
    c0, cc, cs = harmonics(cosine)
    s0, ss_c, ss_s = harmonics(sine)
    assert add(t0,sc(add(cc,ss_s),F(1,2))) == T
    pairs = [(2, add(c0,tc), add(s0,ts)),
             (4, sc(add(cc,sc(ss_s,-1)),F(1,2)),sc(add(ss_c,cs),F(1,2)))]
    caps = [F(3,4), F(7,8), F(49,64), F(9,32), F(9,64)]

    def check_norm(A, cap):
        positive(add(sc(G,cap**2),sc(mm(mm(tr(A),G),A),-1)))

    check_norm(T,caps[0])
    comm = lambda A,B: add(mm(A,B),sc(mm(B,A),-1))
    second = sc(Id,0)
    for i, (k, A, B) in enumerate(pairs):
        check_norm(A,caps[2*i+1])
        check_norm(B,caps[2*i+2])
        second = add(second,sc(add(comm(T,B),sc(comm(A,B),F(-1,2))),F(1,k)))
    check_norm(second,F(1,2))
    assert sum(caps) < 3

    # h = pi*rho. The bounds below are monotone in h and rho.
    mu_max = F(1,64)
    rho_max = mu_max/(2+mu_max)
    h_max = F(22,7)*rho_max
    r2_over_h = 9*h_max/(2*(1-h_max))
    r3_over_h = 27*h_max**2/(6*(1-3*h_max/4))
    x_over_h = caps[0]+r2_over_h
    assert h_max*x_over_h < 1
    error = (rho_max/2+r3_over_h
             +h_max*(2*caps[0]+r2_over_h)*r2_over_h/2
             +h_max**2*x_over_h**3/(4*(1-h_max*x_over_h/2)))
    e = F(1,100)
    assert error < e
    radius = F(1,5)
    assert b>F(7,10)**2 and a<F(3,10)**2 and c<F(3,10)**2
    assert 5*e < 1
    projector_error = 2*e/(radius-e)
    metric_error = 5*e*(1+2*projector_error)+2*projector_error
    assert c>F(1,25) and a>F(1,25) and b>F(1,25)
    assert metric_error < F(1,2)
    assert 5*h_max < F(1,8)
    assert 25*(1+metric_error)/(1-metric_error)*F(8,7)**2 < 64

    # The prior nonlinear readout inequalities still hold at the new endpoint.
    assert 2+mu_max/2 < F(33,16)
    assert 18*F(33,16)/128 < F(1,3)
    phase = F(1,1000)
    assert F(9,32768) < phase-phase**3/6
    assert F(1,128)>2*phase
    return {
        'evidence': 'EXACT_CONDITIONAL',
        'mu_upper_closed': str(mu_max),
        'rho_upper_closed': str(rho_max),
        'fourier_norm_caps': list(map(str,caps)),
        'second_order_norm_cap': '1/2',
        'scaled_cayley_error_cap': str(e),
        'projector_error_cap': str(projector_error),
        'relative_metric_error_cap': str(metric_error),
        'linear_normal_gain_cap': '8',
        'physical_promotion': 0,
    }


if __name__ == '__main__':
    result = json.dumps(run(), indent=2)+'\n'
    Path(__file__).with_name('fourier_interval_results.json').write_text(result)
    print(result, end='')
