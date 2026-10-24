"""Exact constructor classification on one filled tetrahedron; no physical fit."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd, lcm
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[2]
sp = importlib.util.spec_from_file_location(
    'phase', ROOT/'experiments/qpb1-continuous-phase/audit.py')
phase = importlib.util.module_from_spec(sp)
sp.loader.exec_module(phase)
alg = phase.alg
mm, mv, tr, dot = alg.mm, alg.mv, alg.tr, alg.dot
add, scale, rank = alg.add, alg.scale, alg.rank
save = lambda p, x: p.write_text(json.dumps(x, indent=2)+'\n')


def lincomb(coeffs, matrices):
    z = alg.zero(len(matrices[0]))
    for c, m in zip(coeffs, matrices):
        z = add(z, scale(m, c))
    return z


def rational_gcd(values):
    """Positive additive generator of the subgroup spanned by rational values."""
    den = lcm(*(v.denominator for v in values))
    return F(gcd(*(abs(int(v*den)) for v in values)), den)


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    src = json.loads((here/'SOURCES.json').read_text())
    for s in src['sources']:
        assert hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest() == s['sha256']
    ledger = json.loads((ROOT/'experiments/action-normalization-audit/sources/ledger_v0.85.json').read_text())
    byid = {r['id']: r for r in ledger['rows']}
    rows = json.loads((here/'SOURCE_ROWS.json').read_text())['selected_rows']
    assert all(byid[r['id']] == r for r in rows)
    simp, A, J, P, edge, visible, hidden = phase.carrier()
    n = len(simp)
    z = alg.zero(n)
    D = [alg.zero(n) for _ in range(3)]
    ix = {s: i for i, s in enumerate(simp)}
    for s in simp:
        if len(s) > 1:
            for j in range(len(s)):
                D[len(s)-2][ix[s[:j]+s[j+1:]]][ix[s]] = F((-1)**j)
    K = [add(d, scale(tr(d), -1)) for d in D]
    assert lincomb([F(1)]*3, K) == A
    sector = [scale(mm(k, k), F(-1, 4)) for k in K]
    assert [rank(p) for p in sector] == [6, 6, 2]
    assert add(sector[0], sector[1]) == visible and sector[2] == hidden
    assert lincomb([F(1)]*3, sector) == P
    for k in range(3):
        assert mm(sector[k], sector[k]) == sector[k]
        assert tr(sector[k]) == sector[k]
        assert mm(K[k], J) == mm(J, K[k])
        for j in range(3):
            assert mm(D[k], D[j]) == z
            if k != j:
                assert mm(K[k], K[j]) == z
                assert mm(sector[k], sector[j]) == z
    pairs = list(combinations(range(n), 2))
    loc = {p: i for i, p in enumerate(pairs)}
    vec = lambda a: [a[i][j] for i, j in pairs]
    Kv = [vec(k) for k in K]
    hasse = [sum(v != 0 for v in q) for q in Kv]
    assert hasse == [12, 12, 4]
    reps = [phase.representation(simp, p) for p in permutations(range(4))]
    char_rows = []
    actions = []
    for R in reps:
        assert mm(tr(R), R) == alg.eye(n)
        for k in K:
            assert mm(R, k) == mm(k, R)
        images = []
        for i in range(n):
            j = next(j for j in range(n) if R[j][i])
            images.append((j, R[j][i]))
        actions.append(images)
        chi = sum(R[i][i] for i in range(n))
        R2 = mm(R, R)
        chi2 = sum(R2[i][i] for i in range(n))
        char_rows.append({'trace': int(chi), 'trace_square_action': int(chi2),
                          'endom_character': int(chi*chi),
                          'skew_character': int((chi*chi-chi2)/2)})
    assert F(sum(r['endom_character'] for r in char_rows), 24) == 13
    assert F(sum(r['skew_character'] for r in char_rows), 24) == 3
    # Reynolds projection of every standard skew matrix, using signed actions.
    # Independent character sum verifies the dimension of its image.
    projected = []
    nonzero = 0
    for i, j in pairs:
        row = [F(0)]*len(pairs)
        for im in actions:
            a, sa = im[i]
            b, sb = im[j]
            p, sign = ((a, b), 1) if a < b else ((b, a), -1)
            row[loc[p]] += sa*sb*sign/24
        coeff = [dot(v, row)/dot(v, v) for v in Kv]
        assert row == [sum(c*v[t] for c, v in zip(coeff, Kv)) for t in range(len(pairs))]
        projected.append(row)
        nonzero += any(row)
    assert rank(projected) == rank(Kv) == 3 and nonzero == 28
    # All continuous coefficient triples are covered by the basis proof;
    # these finite fixtures verify the formulas, currents and metric branch.
    triples = list(product([F(1, 2), F(1), F(3, 2)], repeat=3))
    triples += [(F(1), F(1), F(2)), (F(1), F(3, 2), F(2)), (F(2), F(3), F(5))]
    x = mv(P, [F((3*i+2) % 7-3, 5) for i in range(n)])
    receipts = []
    current_checks = metric_checks = 0
    for gains in triples:
        G = lincomb(gains, K)
        d = lincomb(gains, D)
        assert mm(d, d) == z and tr(G) == scale(G, -1)
        assert mm(G, J) == mm(J, G)
        assert mm(G, G) == lincomb([-4*g*g for g in gains], sector)
        Omega = lincomb([2*g for g in gains], sector)
        assert scale(mm(J, G), -1) == Omega
        velocity = mv(G, x)
        support_rate = [2*a*b for a, b in zip(x, velocity)]
        current = [[2*G[i][j]*x[i]*x[j] for j in range(n)] for i in range(n)]
        assert tr(current) == scale(current, -1)
        assert support_rate == [sum(row) for row in current]
        assert sum(support_rate) == 0
        for k in range(3):
            assert dot(mv(sector[k], x), mv(sector[k], velocity)) == 0
        for mask in [list(range(i)) for i in range(1, n+1)]:
            assert sum(support_rate[i] for i in mask) == sum(
                current[i][j] for i in mask for j in range(n) if j not in mask)
            current_checks += 1
        # Unweighted boundary with a separately assumed positive degree metric.
        sqrt_h = [F(1)]
        for g in gains:
            sqrt_h.append(sqrt_h[-1]/g)
        S = [[sqrt_h[len(simp[i])-1] if i == j else F(0) for j in range(n)] for i in range(n)]
        Si = [[1/S[i][i] if i == j else F(0) for j in range(n)] for i in range(n)]
        H = mm(S, S)
        Hi = mm(Si, Si)
        native_d = lincomb([F(1)]*3, D)
        raw = add(native_d, scale(mm(mm(Hi, tr(native_d)), H), -1))
        assert mm(mm(S, raw), Si) == G
        assert add(mm(tr(raw), H), mm(H, raw)) == z
        metric_checks += 1
        if gains[0] != gains[1] or gains[1] != gains[2]:
            q = rational_gcd([g-gains[0] for g in gains])
            T_pi = 1/q
            wind = [(g-gains[0])*T_pi for g in gains]
            assert all(t.denominator == 1 for t in wind)
            weights = [dot(x, mv(p, x))/dot(x, x) for p in sector]
            turns = -sum(w*r for w, r in zip(wind, weights))
            assert gains[0]*T_pi - sum(g*r for g, r in zip(gains, weights))*T_pi == turns
            receipts.append({'gains': list(map(str, gains)), 'ray_period_over_pi': str(T_pi),
                             'relative_windings': list(map(int, wind)),
                             'sector_support_fractions': list(map(str, weights)),
                             'holonomy_turns_mod1': str(turns % 1)})
    # Exact local realization of the previous two-rate family.
    for gv, gh in [(F(1), F(3, 2)), (F(3, 2), F(1)), (F(1), F(2))]:
        G = lincomb([gv, gv, gh], K)
        assert G == mm(J, add(scale(visible, 2*gv), scale(hidden, 2*gh)))
    # Earlier reference has all three invariant sectors populated.
    edge01 = [F(i == ix[(0, 1)]) for i in range(n)]
    top = [F(i == ix[(0, 1, 2, 3)]) for i in range(n)]
    reference = [a+b for a, b in zip(edge01, top)]  # norm2=2; same ray as unit reference.
    weights = [dot(reference, mv(p, reference))/dot(reference, reference) for p in sector]
    assert weights == [F(1, 4), F(1, 4), F(1, 2)]
    challenge = []
    for N in [3, 5, 11, 101, 1001, 1000001]:
        gains = [F(1), F(1)+F(1, N), F(3, 2)]
        q = rational_gcd([g-gains[0] for g in gains])
        assert q == F(1, 2*N)
        T_pi = 1/q
        wind = [(g-gains[0])*T_pi for g in gains]
        assert wind == [0, 2, N]
        turns = -sum(w*r for w, r in zip(wind, weights))
        assert turns.denominator == 1  # Hol=+1, whereas unperturbed Hol=-1.
        challenge.append({'N': N, 'gain_error': str(F(1, N)), 'ray_period_over_pi': str(T_pi),
                          'relative_windings': list(map(int, wind)), 'holonomy': '+1',
                          'unperturbed_holonomy': '-1', 'unperturbed_period_over_pi': '2',
                          'old_window_visible_sector_mismatch_turns': str(F(2, N))})
    save(out/'classification.json', {'field': 'Q matrices; R coefficient span',
         'skew_matrix_basis_size': len(pairs), 'Reynolds_image_rank': rank(projected),
         'nonzero_projected_skew_seeds': nonzero, 'zero_projected_skew_seeds': len(pairs)-nonzero,
         'commutant_dimension': 13, 'skew_commutant_dimension': 3,
         'basis': ['K1=D1-D1^T', 'K2=D2-D2^T', 'K3=D3-D3^T'],
         'incidence_pairs_by_grade': hasse, 'sector_ranks': [6, 6, 2],
         'spectrum': '0^1; (+/-2i*g1)^3,(+/-2i*g2)^3,(+/-2i*g3)^1',
         'character_rows': char_rows,
         'two_rate_identity': 'g1=g2=omega_visible/2;g3=omega_hidden/2',
         'scope': 'Single filled tetrahedron; full signed S4; real linear time-independent Euclidean skew generators'})
    save(out/'metric_and_currents.json', {'positive_gain_triples_checked': len(triples),
         'control_volume_checks': current_checks, 'whitening_checks': metric_checks,
         'gain_metric_map': 'g_k=sqrt(h_(k-1)/h_k); h_k=h0/(g1*...*gk)^2',
         'current': 'j_(i<-j)=2G_ij x_i x_j; local incidence only; antisymmetric',
         'energy': 'H_g=(1/2)<x,(-JG)x>=sum_k g_k ||P_k x||^2',
         'source_selection': 'NONE; unweighted unit-metric source is exactly g1=g2=g3=1'})
    save(out/'recurrence.json', {'three_rate_rational_fixtures': receipts,
         'reference_sector_weights': list(map(str, weights)), 'gain_error_challenge': challenge,
         'all_odd_N_proof': 'gcd(1/N,1/2)=1/(2N); n=(0,2,N);sum(n*r)=(N+1)/2 integer',
         'irrational_counterexample': 'g=(1,2,1+sqrt(2)), all sectors nonzero: relative-gap ratio sqrt(2), no nonzero exact ray return',
         'limitation': 'Exact-return period changes/diverges; does not show failure of a separately specified finite-window open-path readout'})
    result = {'status': 'PASS', 'source_hashes': len(src['sources']), 'selected_rows': len(rows),
              'signed_S4_actions': 24, 'skew_seeds_classified': len(pairs),
              'Reynolds_rank': 3, 'independent_character_skew_dimension': 3,
              'sector_ranks': [6, 6, 2], 'gain_triples': len(triples),
              'control_volume_checks': current_checks, 'metric_whitening_checks': metric_checks,
              'two_rate_local_identities': 3, 'rational_recurrence_receipts': len(receipts),
              'odd_N_challenges': len(challenge), 'physical_score': 'UNSCORED', 'physical_promotion': 0}
    save(out/'summary.json', result)
    print(json.dumps(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, type=Path)
    main(parser.parse_args().out)
