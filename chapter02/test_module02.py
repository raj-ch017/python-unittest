import unittest

class TestClass01(unittest.TestCase):
  
  def test_case01(self):

    my_str = "Pac-man"
    my_int = 420

    self.assertTrue(isinstance(my_str, str))
    self.assertTrue(isinstance(my_int, int))

  def test_case02(self):

    my_pi = 3.14
    self.assertFalse(isinstance(my_pi, int))

  def test_case03(self):

    my_int = 10
    self.assertTrue(my_int > 0)

if __name__ == '__main__':

  unittest.main(verbosity=1)
