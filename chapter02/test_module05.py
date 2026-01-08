"""
Code for Verbosity Control with User Inputs
"""


import unittest
import inspect

def add(x, y):
  print("This is a custom function: {}".format(inspect.stack()[0][3]))
  return x + y

class TestClass03(unittest.TestCase):

  def test_case01(self):

    print("\nRunning Test Method: {}\n".format(inspect.stack()[0][3]))

    print("--- User entering first value ---")
    val1 = input("Enter integer: ")
    
    if val1.isnumeric():
      print("User has entered integer.")
      val1 = int(val1)
    
    print("--- User entering second value ---")
    val2 = input("Enter integer: ")

    if val2.isnumeric():
      print("User has entered integer.")
      val2 = int(val2)
      
    self.assertEqual(add(val1, val2), val1 + val2)


if __name__ == "__main__":
  unittest.main(verbosity = 2)