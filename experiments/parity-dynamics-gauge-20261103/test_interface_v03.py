#!/usr/bin/env python3
"""Second construction for exact QPB1 incidence/observability checks."""
import itertools
import unittest
import sympy as S

class InterfaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        faces=[list(itertools.combinations(range(4),k)) for k in (1,2,3,4)]
        ix={t:i for i,t in enumerate(sum(faces,[]))}
        D=S.zeros(15)
        for k in range(1,4):
            for t in faces[k]:
                for j in range(len(t)):
                    u=t[:j]+t[j+1:]
                    D[ix[u],ix[t]]=(-1)**j
        cls.D=D
        cls.A=D-D.T
        cls.E=S.zeros(6,15)
        for k in range(6):
            cls.E[k,4+k]=1

    def test_observable_rank(self):
        O=self.E.col_join(self.E*self.A)
        self.assertEqual(O.rank(),12)
        self.assertEqual((O.col_join(self.E*self.A**2)).rank(),12)

    def test_quadrature_closure(self):
        self.assertEqual(self.E*self.A**2,-4*self.E)
        self.assertEqual(self.A**3,-4*self.A)

    def test_independent_sector_rank(self):
        D1=self.D[:4,4:10]
        D2=self.D[4:10,10:14]
        self.assertEqual(D1*D2,S.zeros(4,4))
        self.assertEqual(D1.rank(),3)
        self.assertEqual(D2.rank(),3)
        self.assertEqual((self.E*self.A).rank(),6)
        self.assertEqual(self.E*self.A*self.E.T,S.zeros(6))

    def test_halfstep(self):
        M=S.eye(15)+self.A**2/2
        self.assertEqual(M.T*M,S.eye(15))
        self.assertEqual(M*M,S.eye(15))
        self.assertNotEqual(M*S.eye(15)[:,0],S.eye(15)[:,0])

if __name__=="__main__":
    unittest.main()
