"""
Code for Multiple Test Classes within Same File
"""

import unittest
import inspect

class TestClass04(unittest.TestCase):

  def test_case01(self):
    print("\nClassname: {}".format(self.__class__.__name__))
    print("Running Test Method: {}".format(inspect.stack()[0][3]))

class TestClass05(unittest.TestCase):

  def test_case01(self):
    print("\nClassname: {}".format(self.__class__.__name__))
    print("Running Test Method: {}".format(inspect.stack()[0][3]))

if __name__ == "__main__":
  unittest.main(verbosity = 2)