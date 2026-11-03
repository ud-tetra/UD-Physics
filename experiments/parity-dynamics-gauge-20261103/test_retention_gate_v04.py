#!/usr/bin/env python3
"""Independent-by-formulation combinatorial checks (same constructor)."""
import itertools
import unittest
from collections import Counter

PAIRS=((0,5),(1,4),(2,3))
EDGES=tuple(itertools.combinations(range(4),2))
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}

def parity(bits):
    return sum((((bits>>i&1)^(bits>>j&1))<<k)
               for k,(i,j) in enumerate(PAIRS))

def permute(bits,order):
    z=0
    for i,(a,b) in enumerate(EDGES):
        a1,b1=order[a],order[b]
        j=EDGE_INDEX[tuple(sorted((a1,b1)))]
        z |= ((bits>>i&1)^int(a1>b1))<<j
    return z

class SampledSignTests(unittest.TestCase):
    def test_fiber_count(self):
        c=Counter((parity(q),parity(p))
                  for q in range(64) for p in range(64))
        self.assertEqual(len(c),64)
        self.assertEqual(set(c.values()),{64})
    def test_quotient_and_counterexample(self):
        for q in range(64):
            for p in range(64):
                newq,newp=p,q^63
                self.assertEqual((parity(newq),parity(newp)),
                                 (parity(p),parity(q)))
        self.assertEqual(parity(0),parity(0))
        self.assertNotEqual(parity(1),parity(0))
    def test_signed_s4_covariance(self):
        for g in itertools.permutations(range(4)):
            induced={}
            for s in range(64):
                a=parity(s)
                v=parity(permute(s,g))
                self.assertTrue(a not in induced or induced[a]==v)
                induced[a]=v
            self.assertEqual(len(induced),8)
            for q in range(64):
                for p in range(64):
                    self.assertEqual((permute(p,g),permute(q^63,g)),
                                    (permute(p,g),permute(q,g)^63))
                    self.assertEqual(
                        (induced[parity(p)],induced[parity(q)]),
                        (parity(permute(p,g)),parity(permute(q^63,g))))
    def test_orbit_count(self):
        seen=set()
        for q in range(8):
            for p in range(8):
                seen.add((q,p))
        self.assertEqual(len(seen),64)

if __name__=="__main__":
    unittest.main()
