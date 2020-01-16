"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from utils import timing, execution


@timing
@execution
def longest_collatz(start_number):
  number, final = 0, 0
  for num in range(start_number, int(start_number // 2), -1):
    iterations = collatz(num)
    if iterations > final:
      final = iterations
      number = num

  return number, final

def collatz(number):
  iterations = 1
  while number > 1:
    iterations += 1
    if number % 2:
      number = (3 * number) + 1
    else:
      number /= 2
  
  return iterations


def main():
  print(collatz(13))
  longest_collatz(1000000)
  