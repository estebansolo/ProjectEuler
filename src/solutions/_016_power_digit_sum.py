"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2̣̣^1000?
"""

from utils import timing, execution


@timing
@execution
def power_digit_sum(number):
    total = 2 ** number
    return sum([int(num) for num in str(total)])


def main():
    power_digit_sum(15)
    power_digit_sum(1000)

