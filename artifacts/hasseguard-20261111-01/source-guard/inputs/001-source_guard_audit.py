"""Exact Q201/Q202 receipt versus signed Q169 flux and candidate guard."""
import json
from native_compare import CELLS, INDEX, N, boundary
from native_flux import flux
from replay import tick


PAIR = ((0, 1), (2, 3))


def receipt(x, integrity):
    """Q201, Q202 and Q204 on the fixed opposite-edge pair M_p."""
    hard = int(all(integrity[e] for e in PAIR))
    latent = sum(2 * abs(x[INDEX[e]]) *
                 (abs(x[INDEX[(e[0],)]]) + abs(x[INDEX[(e[1],)]]))
                 for e in PAIR)
    return hard, latent, hard * int(latent > 0)


def state(v0, v1, e01):
    x = [0] * N
    x[INDEX[(0,)]] = v0
    x[INDEX[(1,)]] = v1
    x[INDEX[(0, 1)]] = e01
    return x


def candidate_verdict(x):
    hardmask = (1, 0, 0, 0, 0, 1)  # e01,e23 only; identifying it with T_hard is an added assumption
    return tick((tuple(x[:4]), tuple(x[4:10]), hardmask))[1]


def current_at_01(x):
    arcs, _ = flux(boundary(), x)
    return next(q for i, j, q in arcs if CELLS[i] == (0,) and CELLS[j] == (0, 1))


def main():
    integrity = {e: 1 for e in PAIR}
    plus, minus, tie = state(1, 0, 2), state(1, 0, -2), state(1, 1, 1)
    witnesses = [plus, minus, tie]
    assert [receipt(x, integrity) for x in witnesses] == [(1, 4, 1)] * 3
    assert [current_at_01(x) for x in witnesses] == [4, -4, 2]
    assert [candidate_verdict(x) for x in witnesses] == ['EVENT', 'EVENT', 'HOLD_TIE']
    assert sum(plus[:4]) == sum(minus[:4]) == 1
    assert sum(q*q for q in plus) == sum(q*q for q in minus) == 5

    # General weighted C0<-C1 incidence block: L A_w x = sum_e
    # (w_head,e - w_tail,e) x_e. For a single e01 with x_e=2:
    weighted = [{'tail_weight':tail,'head_weight':head,
                 'vertex_sum_derivative':2*(head-tail)}
                for tail in (0,1) for head in (0,1)]
    assert [r['vertex_sum_derivative'] for r in weighted] == [0,2,-2,0]
    assert all((r['vertex_sum_derivative'] == 0) ==
               (r['tail_weight'] == r['head_weight']) for r in weighted)

    print(json.dumps({
        'source':'recovered ledger v0.85 Q201-Q204/Q205/Q208/Q210; Q169/Q170 sign from full carrier',
        'matching_pair':['01','23'],
        'witnesses':[{'name':name,'nonzero_amplitudes':{'v0':x[0],'v1':x[1],'e01':x[4]},
                      'Q201_Q202_Q204':list(receipt(x, integrity)),
                      'native_signed_current_v0_to_e01':current_at_01(x),
                      'candidate_verdict_under_added_hardmask_map':candidate_verdict(x)}
                     for name,x in zip(('plus','sign_flip','tie'),witnesses)],
        'Q201_Q202_receipts_select_signed_current':False,
        'Q201_Q202_receipts_select_candidate_unique_flag_verdict':False,
        'weighted_incidence_vertex_sum_checks':weighted,
        'exact_invariant_condition':'for each edge e, w_tail,e=w_head,e for L=sum_vertices conservation for all x',
        'source_selected_weight_or_event_guard':False,
        'physical_promotion':0
    },indent=2))


if __name__ == '__main__':
    main()
