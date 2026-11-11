"""Exact Q169/Q170 full-carrier Hasse current and early-time cut audit."""
import json
from native_compare import CELLS, INDEX, N, boundary, matmul, mv


def flux(d, x):
    """Hasse lower->upper current for A=d-d^T (opposite to d^T-d)."""
    arcs = [(i, j, -2 * d[i][j] * x[i] * x[j])
            for i in range(N) for j in range(N) if d[i][j]]
    divergence = [0] * N
    for i, j, current in arcs:
        divergence[i] -= current
        divergence[j] += current
    return arcs, divergence


def main():
    d = boundary()
    a = [[d[i][j] - d[j][i] for j in range(N)] for i in range(N)]
    x = [0] * N
    x[INDEX[(0,)]] = 1
    x[INDEX[(0, 1)]] = 2
    ax, a2x = mv(a, x), mv(matmul(a, a), x)
    arcs, divergence = flux(d, x)
    stock_dot = [2 * x[i] * ax[i] for i in range(N)]
    assert divergence == stock_dot
    assert sum(divergence) == 0
    assert len(arcs) == 28  # 12 vertex-edge + 12 edge-face + 4 face-top
    active = [(CELLS[i], CELLS[j], q) for i, j, q in arcs if q]
    assert active == [((0,), (0, 1), 4)]
    assert stock_dot[INDEX[(0,)]] == -4
    assert stock_dot[INDEX[(0, 1)]] == 4

    # c(s)=x+s Ax+(s^2/2) A^2 x+O(s^3); rho=c^2.
    taylor = {''.join(map(str, cell)): [x[i] ** 2,
              2 * x[i] * ax[i], ax[i] ** 2 + x[i] * a2x[i]]
              for i, cell in enumerate(CELLS)}
    assert [sum(v[k] for v in taylor.values()) for k in range(3)] == [5, 0, 0]
    assert taylor['0'] == [1, -4, 1]
    assert taylor['01'] == [4, 4, -15]
    assert {k: v[2] for k, v in taylor.items() if k not in ('0','01') and v[2]} == {
        '1': 4, '02': 1, '03': 1, '012': 4, '013': 4}
    # Closed-form vertex amplitude under A^3=-4A, useful for a phase check.
    assert a2x[INDEX[(0,)]] == -3
    # Null: identity/HOLD x(s)=x, every current and stock derivative zero.
    hold_arcs, hold_divergence = [(i,j,0) for i,j,_ in arcs], [0] * N
    assert all(q == 0 for _,_,q in hold_arcs) and sum(hold_divergence) == 0
    print(json.dumps({
        'source_convention':'Q169 A=d-d^T, lower-to-upper Hasse arrow',
        'current_formula':'j_lower_to_upper=-2 B_lower,upper c_lower c_upper',
        'incidence_cut_count':len(arcs),
        'nonzero_initial_arcs':[{'lower':list(i),'upper':list(j),'signed_current':q} for i,j,q in active],
        'initial_vertex_0_stock_derivative':stock_dot[INDEX[(0,)]],
        'initial_edge_01_stock_derivative':stock_dot[INDEX[(0,1)]],
        'stock_taylor_coefficients_constant_linear_quadratic':taylor,
        'vertex_0_amplitude_exact':'1-sin(2s)-3(1-cos(2s))/4',
        'hold_vertex_0_stock_constant':1,
        'hold_vertex_0_stock_derivative':0,
        'candidate_one_tick_vertex_0_stock':4,
        'interpretation':'Native initial S_{v0}=1-4s+s^2+O(s^3); HOLD is 1; candidate tick jumps to 4 on a distinct clock.',
        'sign_note':'Historical HASSE_CURRENT_CURL.md lower-to-upper j=+2 B c_lower c_upper uses A=d^T-d; its sign is opposite to this Q169 convention.',
        'physical_promotion':0
    },indent=2))


if __name__ == '__main__':
    main()
