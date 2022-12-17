#!/usr/bin/python3
import unittest
from helpers import overlaps_with, is_continuous

class TestingIntervals(unittest.TestCase):

    def test_non_overlapping(self):
      # Arrange
      x = [1, 2]
      y = [3, 4]
      # Act 
      actual = overlaps_with(x, y)
      actual2 = overlaps_with(y, x)
      # Assert
      self.assertFalse(actual)
      self.assertFalse(actual2)

    def test_touching(self):
      x = [1, 2]
      y = [2, 3]

      actual = overlaps_with(x, y)
      actual2 = overlaps_with(y, x)

      self.assertTrue(actual)
      self.assertTrue(actual2)
    
    def test_overlapping(self):
      x = [1, 5]
      y = [2, 6]

      actual = overlaps_with(x, y)
      actual2 = overlaps_with(y, x)

      self.assertTrue(actual)
      self.assertTrue(actual2)


    def test_is_continuous(self):
      a = [1, 2]
      b = [3, 4]

      self.assertTrue(is_continuous(a, b))
      self.assertTrue(is_continuous(b, a))




if __name__ == '__main__':
    unittest.main()