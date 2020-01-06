"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from utils import timing, execution


@timing
@execution
def multiples(number):
  """
  The range function returns a sequence of integers, I use list comprehension
  to create a list just after valite the numbers
  """
  
  numbers = [
    num for num in range(number)
    if not num % 3 or not num % 5
  ]
  
  """
  The sum function takes an iterable and returns the sum of the items.
  """
  return sum(numbers)


def main():
  multiples(1000)
