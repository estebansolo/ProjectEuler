"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils import timing, execution

@timing
@execution
def summation_primes(num):
  def is_prime(num):
    for n in range(3, int(num ** 0.5) + 1, 2):
      if not num % n:
        return False
    
    return True
    
  primes_total = 2
  for number in range(3, num, 2):
    if not num % 2 and is_prime(number):
      primes_total += number

  return primes_total

def main():
  summation_primes(10)
  summation_primes(2000000)