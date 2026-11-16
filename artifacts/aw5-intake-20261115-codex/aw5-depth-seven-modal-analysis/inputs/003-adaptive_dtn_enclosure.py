"""Adapt the frequency truncation for AW5 depths six and seven on the fixed time grid."""
from fractions import Fraction as Q
from math import ceil, factorial, floor, pi

import numpy as np

from recursive_dtn import (
    ALPHA, AW5_A, AW5_FACES, AW5_INDEX, EXTERIOR_INDICES, FILLED_PROBE, GAMMA,
    HOLLOW_PROBES, LEAF_A, PERIOD, absolute_entries, af, assemble, common_radius,
    crosscheck, ff, leaf_schur_components, midpoint_weights, response, schur, shifted,
)

DEPTHS = (0,6,7)
CUTOFFS = (4096,8192,16384)
GATE = Q(3,64)
TAIL_TARGET = Q(1,10000)
ACQUISITION = Q(9,2048)+Q(49169,2097152)+Q(1,32)
DAMPING_INTERPOLATION = Q(1,3072)
MICRO = 10**6
OPERATOR_NORMS = (8,56,95)


def truncation_radius(k):
    p = Q(157,50)
    assert max(2*(6+2*(3**7-1)),3*(6+4*(2**7-1)),8) < 94**2
    q = Q(95*PERIOD,2*k)/p
    assert q < 1
    tail = Q(37,5)*Q(81,16)*PERIOD**2/((2*p)**3*k*k*(1-q))
    r = Q(1,8_000_000)
    alias = (2+Q(32,512))*r/(1-r)+Q(PERIOD,512)*r/(1-r)**2
    # Bound the midpoint weighting error and ordinary summation separately.
    arithmetic = Q(3,10**9)*(2*k+1)*33/PERIOD+Q(1,10**6)
    return Q(ceil((tail+alias+arithmetic)*MICRO),MICRO)


def blocks(s, depth):
    if depth == 0:
        M, error = schur(shifted(s,np.asarray(af,dtype=float)),list(range(ff.start,ff.stop)))
        return M, FILLED_PROBE, error
    delta, errors = leaf_schur_components(s,depth)
    whole, rounding = assemble(s,AW5_A,delta,AW5_INDEX,absolute_entries(shifted(s,LEAF_A)))
    M, correction = schur(whole,AW5_FACES)
    # Each terminal leaf contributes its roundoff on faces only.
    # Internal step corrections act on their embedded graded skeleton.
    overlap_bound = 2*errors[0]+sum(3**(depth-j+1)*err for j,err in enumerate(errors[1:],1))
    return M, HOLLOW_PROBES, overlap_bound+rounding+correction


def add_modes(frequency, weights, start, end, means, errors):
    for first in range(start,end,128):
        sl = slice(first,min(first+128,end))
        s = ALPHA+1j*frequency[sl]
        for k,depth in enumerate(DEPTHS):
            M,probes,error = blocks(s,depth)
            width = probes.shape[1]
            for j,gamma in enumerate((0,GAMMA)):
                values,radius = response(s,M,probes,error,EXTERIOR_INDICES,gamma,OPERATOR_NORMS[k])
                smoothed = values-1/s[:,None]+gamma/s[:,None]**2
                means[k,j,:width] += (weights[sl,None]*smoothed).real.sum(axis=0)/PERIOD
                errors[k,j,:width] += (abs(weights[sl,None])*radius).sum(axis=0)/PERIOD


def report(means,errors,cutoff,radius,lower,upper):
    # Include a small outward allowance when reporting the arithmetic radii.
    centers = means+np.array([1,1-16*GAMMA])[None,:,None]
    rad = errors+float(radius)+1e-10
    np.maximum(lower, centers-rad, out=lower)
    np.minimum(upper, centers+rad, out=upper)
    assert np.all(lower<=upper)
    print(f"K={cutoff}: common radius per arm {radius}; "
          f"max numerical resolvent allowance {float(errors.max()):.9f}")
    floors = {}
    for i,depth in enumerate(DEPTHS[1:],1):
        target = min(lower[i,:,0])
        filled = max(upper[0,:,0])
        reference = max(upper[i,:,1])
        loss = float(ACQUISITION+DAMPING_INTERPOLATION)
        values = [Q(floor(MICRO*(target-bound-loss)),MICRO) for bound in (filled,reference)]
        floors[depth] = min(values)
        nominal_upper = Q(ceil(MICRO*(upper[i,0,0]-lower[i,0,1])),MICRO)
        nominal_lower = Q(floor(MICRO*(lower[i,0,0]-upper[i,0,1])),MICRO)
        print(f"  depth {depth}: budgeted floors {float(values[0]):.6f}, {float(values[1]):.6f}; "
              f"undamped fixed-reference gap [{float(nominal_lower):.6f}, {float(nominal_upper):.6f}]; "
              f"{'CERTIFIED PASS' if min(values)>=GATE else 'NO UNIFORM PASS CERTIFICATE'}")
    return floors


def depth_seven_witness(lower,upper):
    # Use legal damping endpoints, collinear drive and sensor gain errors,
    # fully adverse mean offsets, and independent Gaussian sample noise.
    target_hi = Q(ceil(upper[2,1,0]*MICRO),MICRO)
    reference_lo = Q(floor(lower[2,0,1]*MICRO),MICRO)
    eps, beta = Q(1,512), Q(1,256)
    gap_hi = (1-eps)**2*target_hi-(1+eps)**2*reference_lo-2*beta
    margin = gap_hi-GATE
    assert margin > 0 and margin**2 < Q(50,256**2)
    # Mills' lower bound at z=5 exceeds the allowed 2 exp(-16) tail.
    # It suffices to show exp(7/2)>32 and sqrt(2*pi)<13/5.
    assert sum(Q(7,2)**n/factorial(n) for n in range(12)) > 32
    assert 2*Q(22,7) < Q(13,5)**2
    assert Q(5,52)*32/Q(13,5) > 1
    print(f"depth 7 admissible witness: mean gap upper {ceil(gap_hi*MICRO)/MICRO:.6f}; "
          "actual failure probability > 2 exp(-16)")


def main():
    common_radius()  # Validate inherited Machin and exponential bounds.
    crosscheck()
    indices = np.arange(CUTOFFS[-1]+1)
    frequency = 2*pi*indices/PERIOD
    weights = midpoint_weights(indices)
    means = np.zeros((len(DEPTHS),2,2))
    errors = np.zeros_like(means)
    lower, upper = np.full_like(means,-np.inf), np.full_like(means,np.inf)
    start = 0
    for cutoff in CUTOFFS:
        add_modes(frequency,weights,start,cutoff+1,means,errors)
        radius = truncation_radius(cutoff)
        floors = report(means,errors,cutoff,radius,lower,upper)
        if radius <= TAIL_TARGET:
            assert floors[6] > GATE
            depth_seven_witness(lower,upper)
            quieter_floor = floors[7]+Q(1,32)-Q(1,256)
            assert quieter_floor > GATE
            print(f"depth 7 sufficient alternative sigma <= 1/128: "
                  f"floor {floor(MICRO*quieter_floor)/MICRO:.6f}")
            print("PASS: adaptive truncation radius target met on frozen midpoint grid")
            return
        start = cutoff+1
    raise RuntimeError("Cutoff budget exhausted")


if __name__ == "__main__":
    main()
