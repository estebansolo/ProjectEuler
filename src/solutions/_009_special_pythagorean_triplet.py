"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

from utils import timing, execution


@timing
@execution
def special_pythagorean_triplet(num):
    rng = range(1, num + 1)
    for a in rng:
        for b in rng:
            c = num - a - b
            if (a ** 2 + b ** 2) == c ** 2:
                return (a, b, c), a * b * c

    return False

def main():
    special_pythagorean_triplet(1000)