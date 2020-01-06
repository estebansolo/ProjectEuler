"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt
from utils import timing, execution

@timing
@execution
def largest_prime_factor(number):
  if number in [2, 3, 5, 7]:
    return number

  value = 3
  primes = [2]
  while value < sqrt(number):
    for prime in primes:
      if value % prime == 0:
        break
    else:
      if number % value == 0:
        primes.append(value)
    
    value += 2

  return primes.pop()

def main():
    largest_prime_factor(13195)
    largest_prime_factor(600851475143)

