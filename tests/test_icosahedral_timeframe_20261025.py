"""Read-only final 180-column tangent reprojection of archived 3D pulse checkpoints.
Pure standard library: ZIP/NPY loader and real-symmetric Jacobi eigensolver.
The source archive belongs to integrated icosahedral-pulsetube, never edited.
"""
import array
import ast
import json
import math
import struct
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "artifacts/icosahedral-pulsetube-20261022-a1/pulsetube-001/files/compact_checkpoints.npz"
SOURCE = ARCHIVE.parent

def npy(z, name):
    raw = z.read(name + ".npy")
    assert raw[:6] == b"\x93NUMPY"
    version = raw[6]
    assert version in (1, 2, 3)
    hlen = struct.unpack_from("<H" if version == 1 else "<I", raw, 8)[0]
    offset = 10 if version == 1 else 12
    info = ast.literal_eval(raw[offset:offset + hlen].decode("latin1"))
    assert info["fortran_order"] is False
    assert info["descr"] in ("<f8", "=f8", "|f8")
    values = array.array("d")
    values.frombytes(raw[offset + hlen:])
    assert len(values) == math.prod(info["shape"])
    return values, tuple(info["shape"])

def vec_positions(ref):
    # The source canonical q starts with alpha, then 13x3 primary positions.
    assert len(ref) == 561
    rows = [list(ref[1 + 3*i:1 + 3*i + 3]) for i in range(13)]
    hub, shell = rows[0], rows[1:]
    mu = [sum(r[k] for r in shell) / 12 for k in range(3)]
    return hub, [[r[k] - mu[k] for k in range(3)] for r in shell], mu

def invert_apply(A, b):
    M = [list(A[i]) + [b[i]] for i in range(3)]
    for j in range(3):
        k = max(range(j, 3), key=lambda i: abs(M[i][j]))
        assert abs(M[k][j]) > 1e-12
        M[j], M[k] = M[k], M[j]
        d = M[j][j]
        for h in range(j, 4):
            M[j][h] /= d
        for i in range(3):
            if i == j:
                continue
            f = M[i][j]
            for h in range(j, 4):
                M[i][h] -= f * M[j][h]
    return [M[i][3] for i in range(3)]

def frame_column(Ehub, Eshell, X, href):
    # Infinitesimal least-squares proper rotation about the selected reference.
    mu = [sum(r[k] for r in Eshell) / 12 for k in range(3)]
    Ec = [[r[k] - mu[k] for k in range(3)] for r in Eshell]
    cross = [[sum(X[i][j] * Ec[i][k] for i in range(12))
              for k in range(3)] for j in range(3)]
    S = [[(cross[i][j] - cross[j][i]) / 2 for j in range(3)] for i in range(3)]
    G = [[sum(r[i] * r[j] for r in X) for j in range(3)] for i in range(3)]
    trace = sum(G[i][i] for i in range(3))
    M = [[(trace if i == j else 0.0) - G[i][j] for j in range(3)] for i in range(3)]
    omega = invert_apply(M, [2*S[2][1], 2*S[0][2], 2*S[1][0]])
    Q = [[0.0, -omega[2], omega[1]], [omega[2], 0.0, -omega[0]],
         [-omega[1], omega[0], 0.0]]
    shell = [[Ec[i][k] - sum(X[i][j] * Q[j][k] for j in range(3))
              for k in range(3)] for i in range(12)]
    return [Ehub[k] - mu[k] - sum(href[j] * Q[j][k] for j in range(3)) for k in range(3)] + [v for row in shell for v in row]

def tangent_matrix(arr, dims, X, href=None):
    assert dims == (560, 180)
    result = [[0.0] * 180 for _ in range(39)]
    for j in range(180):
        hub = [arr[(1+k)*180 + j] for k in range(3)]
        shell = [[arr[(4+3*i+k)*180+j] for k in range(3)] for i in range(12)]
        aligned = frame_column(hub, shell, X, href) if X is not None else (
            hub + [v for row in shell for v in row])
        for i, value in enumerate(aligned):
            result[i][j] = float(value)
    return result

def top_singular(A):
    # Symmetric Jacobi diagonalization of 39x39 A A^T; no numpy dependency.
    n = len(A)
    G = [[sum(x*y for x, y in zip(A[i], A[j])) for j in range(n)] for i in range(n)]
    for sweep in range(100):
        max_off = 0.0
        for p in range(n):
            for q in range(p+1, n):
                z = G[p][q]
                max_off = max(max_off, abs(z))
                if abs(z) < 1e-16:
                    continue
                tau = (G[q][q] - G[p][p]) / (2*z)
                t = (1 if tau >= 0 else -1) / (abs(tau) + math.sqrt(1+tau*tau))
                c = 1 / math.sqrt(1+t*t)
                s = t*c
                app, aqq = G[p][p], G[q][q]
                G[p][p] = app - t*z
                G[q][q] = aqq + t*z
                G[p][q] = G[q][p] = 0.0
                for k in range(n):
                    if k in (p, q):
                        continue
                    akp, akq = G[k][p], G[k][q]
                    G[k][p] = G[p][k] = c*akp-s*akq
                    G[k][q] = G[q][k] = s*akp+c*akq
        if max_off < 1e-12 * max(max(abs(G[i][i]) for i in range(n)), 1e-18):
            break
    return math.sqrt(max(0.0, max(G[i][i] for i in range(n))))


def feasible_total_endpoint(raw_matrix, epsilon, reference_start, reference_end):
    """Explicit unit housing-phase directions yield valid *linearized* lower bounds."""
    b = [reference_end[1+k] - reference_start[1+k] for k in range(39)]
    ncols = 180
    ATb = [sum(raw_matrix[i][j]*b[i] for i in range(39)) for j in range(ncols)]
    seeds = [ATb,
             [math.sin(0.371*(j+1))+math.cos(0.763*(j+1)) for j in range(ncols)],
             [math.cos(0.183*(j+1)) for j in range(ncols)]]
    best = math.sqrt(sum(x*x for x in b))
    best_kind = "reference"
    for index, seed in enumerate(seeds):
        v = list(seed)
        norm = math.sqrt(sum(x*x for x in v))
        if norm < 1e-14:
            continue
        v = [x/norm for x in v]
        # For nonzero baseline seed index 0 is matched; for others use
        # power iteration to find high-response raw housing directions.
        if index:
            for _ in range(500):
                y = [sum(x*z for x,z in zip(row,v)) for row in raw_matrix]
                vnew = [sum(raw_matrix[i][j]*y[i] for i in range(39))
                        for j in range(ncols)]
                nv = math.sqrt(sum(x*x for x in vnew))
                if nv < 1e-14:
                    break
                v = [x/nv for x in vnew]
        y = [sum(x*z for x,z in zip(row,v)) for row in raw_matrix]
        for sign in (-1,1):
            value = math.sqrt(sum((b[i]+sign*epsilon*y[i])**2 for i in range(39)))
            if value>best:
                best,best_kind=value,f"probe{index},sign{sign}"
    return {"feasible_linearized_total_primary_radius_lower_bound":best,
            "lower_bound_phase_type":best_kind,
            "exceeds_frame001_0_036_radius_in_linearization":best>0.036}

def calculate():
    assert ARCHIVE.is_file(), str(ARCHIVE)
    records = json.loads((SOURCE / "variational-normal.json").read_text())["records"]
    fine = json.loads((SOURCE / "variational-fine.json").read_text())["records"][0]
    cases = [
        ("worst_fine", fine),
        ("worst_normal", next(r for r in records if "seed10422" in r["id"])),
        ("nominal_normal", next(r for r in records if "uniform" in r["id"])),
    ]
    out = {}
    with zipfile.ZipFile(ARCHIVE) as z:
        names = set(z.namelist())
        for label, rec in cases:
            needed = [label + "_" + q + ".npy" for q in (
                "final_tangent", "reference_initial", "reference_final")]
            assert all(name in names for name in needed), (label, needed, list(names)[:8])
            tangent, dims = npy(z, label + "_final_tangent")
            initial, ds0 = npy(z, label + "_reference_initial")
            final, ds1 = npy(z, label + "_reference_final")
            assert ds0 == ds1 == (561,)
            hub0, X0, center0 = vec_positions(initial)
            hubf, Xf, centerf = vec_positions(final)
            ref_displacement = math.sqrt(sum((a-b)**2 for a,b in zip(initial[1:40],final[1:40])))
            G0 = [[sum(r[i]*r[j] for r in X0) for j in range(3)] for i in range(3)]
            c0 = sum(G0[i][i] for i in range(3))/3
            anisotropy0 = max(abs(G0[i][j]-(c0 if i==j else 0)) for i in range(3) for j in range(3))
            Gf = [[sum(r[i]*r[j] for r in Xf) for j in range(3)] for i in range(3)]
            cf = sum(Gf[i][i] for i in range(3))/3
            anisotropyf = max(abs(Gf[i][j]-(cf if i==j else 0)) for i in range(3) for j in range(3))
            eps = math.sqrt(2*rec["housing_energy"])
            raw_matrix = tangent_matrix(tangent, dims, None)
            lower = feasible_total_endpoint(raw_matrix, eps, initial, final)
            raw = eps*top_singular(raw_matrix)
            fixed = eps*top_singular(tangent_matrix(tangent, dims, X0, [hub0[k]-center0[k] for k in range(3)]))
            moving = eps*top_singular(tangent_matrix(tangent, dims, Xf, [hubf[k]-centerf[k] for k in range(3)]))
            out[label] = {
                "source_id":rec["id"], "epsilon":eps,
                "raw_final_primary_linear_radius":raw,
                "equilibrium_frame_final_primary_linear_radius":fixed,
                "moving_reference_frame_final_primary_linear_radius":moving,
                "reference_final_displacement_from_equilibrium":ref_displacement,
                "initial_shell_gram_anisotropy_max":anisotropy0,
                "moving_shell_gram_anisotropy_max":anisotropyf,
                "reference_hub_relative_to_shell_centroid_norm":math.sqrt(sum((hubf[k]-centerf[k])**2 for k in range(3))),
                "frame001_radius":0.036,
                "frame001_ball_contains_moving_reference_final":ref_displacement<=0.036,
                **lower,
            }
            assert raw >= min(fixed, moving)*0.99999
            assert eps > 0 and all(math.isfinite(x) for x in (raw,fixed,moving,ref_displacement))
    return out

class FrameTangentArchiveTest(unittest.TestCase):
    def test_archived_final_180_column_tangent(self):
        out=calculate()
        print("FRAME_TANGENT_RESULT_JSON:"+json.dumps(out,sort_keys=True),flush=True)
        self.assertEqual(len(out),3)

if __name__ == "__main__":
    unittest.main(verbosity=2)


class RigidTranslationGreenTest(unittest.TestCase):
    """Test exact Galilean translation Green block against the source 560x180 W."""
    def test_cm_translation_all_180_columns(self):
        source_cases=json.loads((ROOT / "artifacts/icosahedral-jointwindow-20261022-a1/jointwindow-001/files/cases.json").read_text())
        cases={c["id"]:c for c in source_cases if c["id"] in ("seed10422-0-boundary2","uniform-b0.05-cf0.0")}
        results=json.loads((SOURCE/"variational-normal.json").read_text())["records"]
        fine=json.loads((SOURCE/"variational-fine.json").read_text())["records"][0]
        Eref={"worst_fine":fine,"worst_normal":next(x for x in results if x["id"]=="seed10422-0-boundary2"),
              "nominal_normal":next(x for x in results if x["id"]=="uniform-b0.05-cf0.0")}
        R2=(5+math.sqrt(5))/8
        horizon=100
        out={}
        with zipfile.ZipFile(ARCHIVE) as z:
            for label,record in Eref.items():
                case=cases[record["id"]]
                masses=[m/R2 for m in case["primary"]["m"]]
                m_h=[0.4*case["beta"]*weight/R2 for weight in case["housing_weights"]]
                Mtot=sum(masses)+sum(m_h)
                Mh=sum(m_h)
                eps=math.sqrt(2*record["housing_energy"])
                Omega=case["omega_h"]
                W,dims=npy(z,label+"_final_tangent")
                assert dims==(560,180) and len(masses)==13 and len(m_h)==30
                cm=[[0.0]*180 for _ in range(3)]
                predicted=[[0.0]*180 for _ in range(3)]
                for axis in range(3):
                    for col in range(180):
                        v=sum(masses[i]*W[(1+3*i+axis)*180+col] for i in range(13))
                        v+=sum(m_h[j]*W[(190+3*j+axis)*180+col] for j in range(30))
                        cm[axis][col]=v/Mtot
                    for j in range(30):
                        predicted[axis][3*j+axis]=math.sqrt(m_h[j])/(Omega*Mtot)
                        predicted[axis][90+3*j+axis]=horizon*math.sqrt(m_h[j])/Mtot
                max_error=max(abs(cm[axis][col]-predicted[axis][col])
                              for axis in range(3) for col in range(180))
                assert max_error<1e-6, (label,max_error)
                analytic_cm=eps*math.sqrt(Mh)/Mtot*math.hypot(horizon,1/Omega)
                analytic_primary=math.sqrt(13)*analytic_cm
                raw=tangent_matrix(W,dims,None)
                residual=[[(raw[3*i+axis][col]-cm[axis][col])
                           for col in range(180)]
                          for i in range(13) for axis in range(3)]
                residual_radius=eps*top_singular(residual)
                raw_radius=eps*top_singular(raw)
                assert raw_radius>=analytic_primary-residual_radius-1e-7
                out[label]={"housing_mass":Mh,"total_mass":Mtot,
                            "house_energy":record["housing_energy"],
                            "analytic_global_cm_position_radius":analytic_cm,
                            "analytic_uniform_primary_translation_radius":analytic_primary,
                            "observed_source_full180_primary_raw_radius":raw_radius,
                            "cm_removed_primary_radius":residual_radius,
                            "max_column_cm_translation_identity_error":max_error}
        print("ICO_RIGID_GREEN_RESULT_JSON:"+json.dumps(out,sort_keys=True),flush=True)
        self.assertEqual(len(out),3)
