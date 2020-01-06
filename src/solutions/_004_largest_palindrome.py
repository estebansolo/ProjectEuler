"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import timing, execution


def is_palindrome(num):
  return num == num[::-1]

@timing
@execution
def largest_palindrome_product(digits):
    """ multiply strings to get the start and the end """
    start, end = int("9" * digits), int("1" * digits)

    result = 0
    reverse_range = range(start, end, -1)

    for first in reverse_range:
        for second in reverse_range:
            product = first * second
            if product < result:
                break

            if is_palindrome(str(product)):
                result = product

    return result

def main():
    largest_palindrome_product(2)
    largest_palindrome_product(3)