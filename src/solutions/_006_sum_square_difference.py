"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

from utils import timing, execution


@timing
@execution
def sum_square_difference(n_max):
  _range = list(range(n_max + 1))

  squares_nums = 0
  for n in _range:
    squares_nums += n ** 2

  return (sum(_range) ** 2) - squares_nums

def main():
  sum_square_difference(10)
  sum_square_difference(100)
