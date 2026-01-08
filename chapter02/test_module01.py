"""
Code for using unittest
"""


import unittest

# creation of test class
# test class is inherited from TestCase class
class TestClass01(unittest.TestCase):

  # test function 1
  def test_case01(self):

    my_str = "Pac-man"
    my_int = 420

    # assert statement used to assert instance of variable
    self.assertTrue(isinstance(my_str, str))
    self.assertTrue(isinstance(my_int, int))

  # test function 2
  def test_case02(self):

    my_pi = 3.14
    self.assertFalse(isinstance(my_pi, int))

if __name__ == '__main__':
  unittest.main()