"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""

from utils import timing, execution


@timing
@execution
def smallest_multiple(n_max):
    value = n_max
    while True:
        for factor in range(n_max, 2, -1):
            if value % factor:
                value += n_max
                break
        else:
            return value

def main():
    smallest_multiple(10)
    smallest_multiple(20)
