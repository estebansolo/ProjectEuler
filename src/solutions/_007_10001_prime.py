"""
By listing the first six prime numbers:

2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from utils import timing, execution


@timing
@execution
def search_prime(num):
    prime, number, count = 2, 3, 1
    while count < num:
        for n in range(2, int(number ** 0.5) + 1):
            if not number % n:
                break
        else:
            count += 1
            prime = number
        
        number += 2
  
    return prime

def main():
    search_prime(6)
    search_prime(10001)