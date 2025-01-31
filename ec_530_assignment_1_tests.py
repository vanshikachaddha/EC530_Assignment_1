# -*- coding: utf-8 -*-
"""EC 530 - Assignment 1 Tests.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eQAy3ZVDlTCQb1IG7wNhzfDr4LXu2zXj
"""

import unittest
import math
from ec_530_assignment_1 import check_DMS, convert_dms, convert_radians, distance, shortest_match

class testfunctions(unittest.TestCase):

  def test_check_DMS(self):
    self.assertTrue(check_DMS("40 42.8"))
    self.assertFalse(check_DMS(40.7133))

  def test_convert_DMS(self):
    self.assertAlmostEqual(convert_dms("40 42.8"), 40.7133, places=4)
    self.assertAlmostEqual(convert_dms("74 00.6"), 74.01, places=4)

  def test_distance(self):
    lat1, lon1 = math.radians(40.7133), math.radians(-74.01)
    lat2, lon2 = math.radians(34.0522), math.radians(-118.2437)
    self.assertAlmostEqual(distance(lon1, lon2, lat1, lat2), 2000)

  def test_shortest_match(self):
    array1 = [(42.3601, -71.0589)]
    array2 = [(40.7128, -74.0060), (36.7783, -119.4179), (41.8781, -87.6298)]
    result = shortest_match(array1, array2)
    self.assertEqual(result[0][1], (40.7128, -74.0060))

if __name__ == '__main__':
    unittest.main()