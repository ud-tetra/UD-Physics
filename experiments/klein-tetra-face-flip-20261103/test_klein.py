#!/usr/bin/env python3
"""Separate exact matrix/topology checks for the Klein seam audit."""
import unittest
from math import gcd
from functools import reduce
from itertools import combinations

class KleinControls(unittest.TestCase):
 def test_euler_and_torsion(self):
  B=((1,-1),(-1,-1),(-1,1))
  m=[B[i][0]*B[j][1]-B[i][1]*B[j][0] for i,j in combinations(range(3),2)]
  self.assertEqual(m,[-2,0,-2])
  self.assertEqual(reduce(gcd,map(abs,m)),2)
  self.assertEqual(1-3+2,0)
  self.assertEqual(4-6+4,2)
 def test_orientation_character(self):
  B=((1,-1),(-1,-1),(-1,1))
  w=(1,0,1)
  self.assertEqual(tuple(sum(B[i][j]*w[i] for i in range(3))%2 for j in range(2)),(0,0))
  self.assertEqual(tuple(B[i][0]+B[i][1] for i in range(3)),(0,-2,0))
 def test_torus_control(self):
  B=((1,-1),(1,-1),(-1,1))
  self.assertEqual(tuple(B[i][0]+B[i][1] for i in range(3)),(0,0,0))
 def test_twist_rotation_relation(self):
  def mm(A,B):
   return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
  F=((1,0),(0,-1));R=((0,-1),(1,0));I=((1,0),(0,1))
  self.assertEqual(mm(F,F),I)
  self.assertEqual(mm(mm(mm(F,R),F),R),I)

if __name__=="__main__":unittest.main()
