"""
Code for running unittest without main()
"""


import unittest

class TestClass07(unittest.TestCase):

  def test_case01(self):
    self.assertTrue("PYTHON".isupper())
    print("\n--- In test_case01() ---")