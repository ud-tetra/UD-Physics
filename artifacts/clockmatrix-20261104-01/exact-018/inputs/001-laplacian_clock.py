"""Fixed even Laplacian coupling with separately tracked reference lobes."""
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
    reflected = (-np.arange(size)) % size
    backward = forward[np.ix_(reflected, reflected, reflected)]
    assert not np.any((forward != 0) & (backward != 0))

    def channels(spectrum, time, strength):
        phase = 2 + strength * omega**2
        return tuple(np.fft.fftshift(np.fft.ifftn(
            spectrum * np.exp(-1j * (omega + sign * phase) * time)
        )) for sign in (-1, 1))

    def stock(pair):
        return (abs(pair[0])**2 + abs(pair[1])**2) / 2

    def track(pair):
        mass = stock(pair)
        center = [float(np.sum(mass * axis) / np.sum(mass)) for axis in r]
        window = np.exp(-sum((axis - mean)**2 for axis, mean in zip(r, center)) / 72)
        return center, window

    def observe(pair, time, window=1):
        mass = stock(pair)
        count = np.sum(window * mass)
        contrast = np.sum(window * pair[0] * pair[1].conj()) / count
        return (float(np.angle(contrast * np.exp(-4j * time)) / 2),
                float(abs(contrast)), float(count / np.sum(mass)))

    rows = []
    for strength in (0, 1 / 128):
        for time in (0, 4, 8, 12):
            moving = channels(forward, time, strength)
            reverse = channels(backward, time, strength)
            reference = tuple((a + b) / np.sqrt(2) for a, b in zip(moving, reverse))
            center, window = track(moving)
            reverse_center, reverse_window = track(reverse)
            ref_center, center_window = track(reference)
            assert np.linalg.norm(np.array(center) + reverse_center) < 1e-10
            assert np.linalg.norm(ref_center) < 1e-10
            global_moving = observe(moving, time)
            global_ref = observe(reference, time)
            assert np.allclose(global_moving, global_ref, atol=1e-12, rtol=0)
            local_moving = observe(moving, time, window)
            local_reverse = observe(reverse, time, reverse_window)
            assert np.allclose(local_moving, local_reverse, atol=1e-12, rtol=0)
            reference_windows = observe(reference, time, (window + reverse_window) / 2)
            center_readout = observe(reference, time, center_window)
            rows.append({
                "strength": strength, "native_time": time, "moving_centroid": center,
                "global_clock_residual": global_moving[0],
                "global_contrast": global_moving[1],
                "isolated_lobe_residual": local_moving[0],
                "coherent_reference_two_window_residual": reference_windows[0],
                "coherent_reference_window_minus_lobe": reference_windows[0] - local_moving[0],
                "reference_two_window_stock_fraction": reference_windows[2],
                "reference_centroid_window_stock_fraction": center_readout[2],
            })
    return {"grid": size, "rows": rows}


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2))
