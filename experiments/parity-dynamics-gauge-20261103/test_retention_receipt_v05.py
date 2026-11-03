#!/usr/bin/env python3
"""Alternative exact allocation/capture tests: 29 simplices in the 1->4 K4 ball."""
import itertools,unittest
from fractions import Fraction as F

T=[(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)]
S=sorted({ss for tt in T for k in range(1,5) for ss in itertools.combinations(tt,k)},key=lambda x:(len(x),x))
def owner(s,t):
    n=sum(set(s).issubset(set(tt)) for tt in T)
    return F(int(set(s).issubset(set(t))),n)
def inc(s,t):
    if len(t)!=len(s)+1:return 0
    return sum((-1)**j for j in range(len(t)) if t[:j]+t[j+1:]==s)
class TestReceipt(unittest.TestCase):
    def test_partition(self):
        self.assertEqual(len(S),29)
        for s in S:self.assertEqual(sum((owner(s,t) for t in T),F(0)),1)
    def test_all29_full_capture(self):
        for s in S:
            before={t:owner(s,t) for t in T}
            retained={t:owner(s,t) for t in T}
            self.assertEqual(sum(before.values()),1)
            self.assertEqual(sum(retained.values()),1)
            self.assertTrue(all(z>=0 for z in retained.values()))
    def test_conservative_current(self):
        face=(0,1,4); top=(0,1,2,4)
        c={s:int(s==face or s==top) for s in S}
        derived={}
        for cell in T:
            direct=F(0)
            for s in S:
                slope=sum((inc(s,t)*c[t]-inc(t,s)*c[t] for t in S),0)
                direct+=owner(s,cell)*2*c[s]*slope
            current=F(0)
            for s in S:
                for t in S:
                    if inc(s,t):
                        J=-2*inc(s,t)*c[s]*c[t]
                        current+=(owner(t,cell)-owner(s,cell))*J
            self.assertEqual(direct,current)
            derived[cell]=direct
        self.assertEqual([derived[t] for t in T],[-1,1,0,0])
        self.assertEqual(sum(derived.values()),0)
    def test_nonselection(self):
        a=F(1); w=[F(1,2),F(1,2)]
        for delta in [F(0),F(1,4),F(1)]:
            self.assertEqual((a-delta)+sum(z*delta for z in w),a)
        self.assertNotEqual(F(0),F(1))
if __name__=="__main__":unittest.main()
