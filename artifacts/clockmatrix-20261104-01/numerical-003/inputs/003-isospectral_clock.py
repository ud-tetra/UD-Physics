"""Equal spectral loading and distinct packet speeds on the scalar dispersion."""
from fractions import Fraction as F
import json
import numpy as np

from directional_packet import dispersion


def center_speeds_squared():
    frequency_squared = F(1744, 125)
    axis = 4 * (1 - F(93, 125)**2) / frequency_squared
    diagonal = F(3, 8) * F(384, 125)**2 / frequency_squared
    assert axis == F(16, 125)
    assert diagonal == F(3456, 13625)
    return [str(axis), str(diagonal)]


def replay(order, probe=None):
    points, weights = np.polynomial.legendre.leggauss(order)
    weights *= (1 - points**2)**4
    weights /= weights.sum()
    p, y, z = np.meshgrid(points, points / 100, points / 100, indexing="ij")
    probability = weights[:, None, None] * weights[None, :, None] * weights[None, None, :]
    target = 1744 / 125 + p / 20

    def chart(diagonal):
        center = np.arccos(3 / 5 if diagonal else -93 / 125)

        def coordinates(x):
            return (x, x + y, x + z) if diagonal else (x, y, z)

        lo, hi = np.full_like(target, center - 1 / 20), np.full_like(target, center + 1 / 20)
        assert np.all(dispersion(coordinates(lo))[0]**2 < target)
        assert np.all(dispersion(coordinates(hi))[0]**2 > target)
        for _ in range(48):
            mid = (lo + hi) / 2
            below = dispersion(coordinates(mid))[0]**2 < target
            lo, hi = np.where(below, mid, lo), np.where(below, hi, mid)
        wavevector = coordinates((lo + hi) / 2)
        omega, velocity = dispersion(wavevector)
        mean = np.array([np.sum(probability * v) for v in velocity])
        speed = np.sqrt(np.dot(mean, mean) / 2 - mean.sum()**2 / 8)
        contrast = np.sum(probability * np.exp(2j * (omega**2 / 128) * 12))
        result = {
            "centroid_velocity": mean.tolist(),
            "centroid_speed": float(speed),
            "phase_residual_at_12_rad": float(np.angle(contrast) / 2),
            "contrast_at_12": float(abs(contrast)),
            "max_squared_frequency_error": float(np.max(abs(omega**2 - target))),
        }

        if probe is not None:
            result["probe"] = probe(wavevector, probability)
        return result

    axis, diagonal = chart(False), chart(True)
    assert diagonal["centroid_speed"] - axis["centroid_speed"] > 0.14
    assert max(row["max_squared_frequency_error"] for row in (axis, diagonal)) < 1e-12
    assert abs(axis["phase_residual_at_12_rad"] - diagonal["phase_residual_at_12_rad"]) < 1e-12
    return {"order": order, "axis": axis, "diagonal": diagonal}


if __name__ == "__main__":
    print(json.dumps({"center_speeds_squared": center_speeds_squared(),
                      "quadrature": [replay(8), replay(16)]}, indent=2))
