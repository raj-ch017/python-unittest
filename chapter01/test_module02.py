"""
Sample doctest test module - test_module02
"""

def mul(a, b):
  """
  >>> mul(2, 3)
  6

  >>> mul('a', 2)
  'aa'
  """

  return a * b


def add(a, b):
  """
  >>> add(2, 3)
  5

  >>> add('a', 'b')
  'ab'
  """

  return a + b


# this part of the code incorperates doctest directly 
# there is no need to use '-m doctest' in the python command
# testmod is used when the .py file is being directly run
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)


"""
import doctest 
doctest.testfile('test_module03.txt')
"""
