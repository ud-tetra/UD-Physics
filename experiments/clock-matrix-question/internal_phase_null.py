"""Two-channel transported clock null and injected-detuning control."""
import json
import numpy as np

from directional_packet import CUTOFF, WIDTH, dispersion


def replay(size=97):
    k = np.meshgrid(*(np.fft.fftfreq(size) * (2 * np.pi),) * 3,
                    indexing="ij", sparse=True)
    r = np.meshgrid(*(np.arange(size) - size // 2,) * 3,
                    indexing="ij", sparse=True)
    omega, _ = dispersion(k)
    radius = np.sqrt((k[0] - np.pi / 3)**2 + k[1]**2 + k[2]**2)
    taper = np.clip((radius - 0.45) / (CUTOFF - 0.45), 0, 1)
    forward = np.exp(-radius**2 / (2 * WIDTH**2)) * (1 + np.cos(np.pi * taper)) / 2
    opposite_indices = (-np.arange(size)) % size
    backward = forward[np.ix_(opposite_indices, opposite_indices, opposite_indices)]
    assert not np.any((forward != 0) & (backward != 0))
    stationary = (forward + backward) / np.sqrt(2)
    assert np.allclose(np.sum(omega * forward**2), np.sum(omega * stationary**2))
    times = np.arange(25) / 2

    def observations(spectrum, clock_rate):
        rows = []
        for time in times:
            upper = np.fft.fftshift(np.fft.ifftn(spectrum * np.exp(-1j * (omega - clock_rate) * time)))
            lower = np.fft.fftshift(np.fft.ifftn(spectrum * np.exp(-1j * (omega + clock_rate) * time)))
            a, b = (upper + lower) / 2, (upper - lower) / (2j)
            stock = abs(a)**2 + abs(b)**2
            center = [float(np.sum(stock * axis) / np.sum(stock)) for axis in r]
            radius_sq = sum((axis - mean)**2 for axis, mean in zip(r, center))
            window = np.exp(-radius_sq / 72)
            contrast = np.sum(window * (abs(a)**2 - abs(b)**2 + 2j * np.real(a.conj() * b)))
            denominator = np.sum(window * stock)
            rows.append((center, np.angle(contrast), abs(contrast) / denominator,
                         denominator / np.sum(stock)))
        phase = np.unwrap([row[1] for row in rows]) / 2
        return rows, phase

    moving, phase_moving = observations(forward, 2)
    fixed, phase_fixed = observations(stationary, 2)
    injected, phase_injected = observations(forward, 2 + 1/32)
    null_error = max(abs(phase_moving - phase_fixed))
    injection_error = max(abs(phase_injected - phase_fixed - times / 32))
    fixed_motion = max(np.linalg.norm(row[0]) for row in fixed)
    contrast_min = min(row[2] for series in (moving, fixed, injected) for row in series)
    assert null_error < 1e-12 and injection_error < 1e-12
    assert fixed_motion < 1e-12 and contrast_min > 1 - 1e-12
    return {
        "grid_side": size, "samples": len(times), "last_native_time": float(times[-1]),
        "moving_final_centroid": moving[-1][0], "stationary_max_centroid_norm": fixed_motion,
        "max_null_phase_difference_rad": float(null_error),
        "injected_final_phase_difference_rad": float(phase_injected[-1] - phase_fixed[-1]),
        "max_injected_phase_error_rad": float(injection_error),
        "min_normalized_contrast": float(contrast_min),
        "min_window_stock_fraction": float(min(row[3] for series in (moving, fixed, injected)
                                                for row in series)),
    }


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2))
