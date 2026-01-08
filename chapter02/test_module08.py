"""
Code for Test Fixtures with Custom Functions
"""


import unittest
import inspect

def setUpModule():
  """ called once, before anything else in the module """
  print("--- In setUpModule() ---")

def tearDownModule():
  """ called once, after everything else in the module """
  print("--- In tearDownModule() ---")

def multiplication(a, b):
  
  print("Currently in function: {}".format(inspect.stack()[0][3]))
  return a * b

class TestClass06(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    """ called once, before any test """
    print("--- In setUpClass() ---")

  @classmethod
  def tearDownClass(cls):
    """ called once, after all tests, if setUpClass was successful """
    print("--- In tearDownClass() ---")

  def setUp(self):
    """ called multiple times, before every test method """
    print("\n--- In setUp() ---")

  def tearDown(self):
    """ called multiple times, after every test method """
    print("--- In tearDown() ---")

  def test_case01(self):
    print("--- In test_case01() ---")

    val1 = int(input("Enter integer value: "))
    val2 = int(input("Enter integer value: "))
    self.assertEqual(multiplication(val1, val2), val1 * val2)

  def test_case02(self):
    print("--- In test_case02() ---")

    val1 = float(input("Enter float value: "))
    val2 = float(input("Enter float value: "))
    self.assertEqual(multiplication(val1, val2), val1 * val2)

if __name__ == '__main__':
  unittest.main(verbosity=2)