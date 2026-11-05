"""Exact constructor checks for historical transport/Q136 and G06 anchor gates."""
from fractions import Fraction as Q
import json
from pathlib import Path


def rank(rows):
    a = [[Q(v) for v in row] for row in rows]
    pivot = 0
    for j in range(len(a[0])):
        k = next((i for i in range(pivot, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        t = a[pivot][j]
        a[pivot] = [v / t for v in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                t = a[i][j]
                a[i] = [v - t * w for v, w in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def main():
    seed = Q(1, 2) * Q(7, 16) * Q(1, 6)
    assert seed == Q(7, 192)
    # Formal logarithm certificate: when r_k=exp(-sum sigma_k),
    # -log(product r_k)=sum sum sigma_k. Rational exponents are exact.
    steps = [(Q(1, 2), Q(1, 3), Q(1, 6)),
             (Q(2, 3), Q(1, 4), Q(1, 12))]
    costs = [sum(s) for s in steps]
    assert costs == [Q(1), Q(1)] and sum(costs) == Q(2)
    # If each transport ratio is identical for an oriented path and its
    # reversal, L is even; O09 is odd for any nonzero lifted winding.
    a, winding = Q(3, 2), 1
    forward_i_over_pi = a * winding
    reverse_i_over_pi = -a * winding
    forward_step_sigmas = steps[0]
    reverse_step_sigmas = forward_step_sigmas  # declared reciprocal-attenuation branch
    reverse_cost = sum(reverse_step_sigmas)
    assert forward_i_over_pi == -reverse_i_over_pi
    assert costs[0] == reverse_cost and forward_i_over_pi != reverse_i_over_pi
    # Unknown log variables (A0,tau0,a): E=A0*a/tau0, T=pi*tau0.
    e, t, support, target = (1, -1, 1), (0, 1, 0), (0, 0, 1), (1, 0, 0)
    assert rank([e, t]) == 2 and rank([e, t, target]) == 3
    assert rank([e, t, support]) == rank([e, t, support, target]) == 3
    null = (1, 0, -1)
    assert sum(x*y for x, y in zip(e, null)) == 0
    assert sum(x*y for x, y in zip(t, null)) == 0
    assert sum(x*y for x, y in zip(target, null)) == 1
    # Direct amplitude scaling with fixed measured energy and period.
    A0, tau0, norm, c = Q(5), Q(2), Q(3), Q(2)
    E = A0 * norm / tau0
    A0_new, norm_new = A0 / c**2, c**2 * norm
    assert A0_new * norm_new / tau0 == E and A0_new != A0
    # Signed linear readout x1=cos(2s) has period pi;
    # nonconstant quadratic x1^2=(1+cos(4s))/2 has period pi/2.
    result = {
        "historical_transport_seed": str(seed),
        "obstruction_step_costs": [str(x) for x in costs],
        "product_transport_log_cost": str(sum(costs)),
        "reverse_even_cost": str(reverse_cost),
        "forward_reverse_O09_over_pi": [str(forward_i_over_pi), str(reverse_i_over_pi)],
        "g06_energy_time_rows": [list(e), list(t)],
        "g06_rank_before_after_support": [rank([e,t]), rank([e,t,support])],
        "g06_action_target_rank_without_support": rank([e,t,target]),
        "g06_null_witness": list(null),
        "g06_rescale_example": {"E":str(E), "A0_before":str(A0), "A0_after":str(A0_new), "a_before":str(norm), "a_after":str(norm_new)},
        "signed_readout_period_in_s": "pi",
        "nonconstant_quadratic_readout_period_in_s": "pi/2",
        "transport_to_Hodge_map": "OPEN",
        "independent_physical_anchor_admitted": False,
        "physical_promotion": 0,
    }
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
