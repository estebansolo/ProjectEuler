"""
Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

from utils import timing, execution


@timing
@execution
def even_fibonacci(limit):
  a, b, even_sum = 1, 1, 0
  while b < limit:
    a, b = b, a + b
    if not a % 2:
      even_sum += a

  return even_sum

def main():
  even_fibonacci(89)
  even_fibonacci(4000000)