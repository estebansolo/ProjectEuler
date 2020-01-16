"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.png

How many such routes are there through a 20×20 grid?
"""

from utils import timing, execution


@timing
@execution
def lattice_paths(num):
    ranges = range(num + 1)
    matrix = create_matrix(num)

    for row in ranges:
        for col in ranges:
            if not row and not col:
                matrix[row][col] = 1
                continue

            prev_row = 0 if (row - 1) < 0 else (row - 1)
            prev_col = 0 if (col - 1) < 0 else (col - 1)

            matrix[row][col] = matrix[prev_row][col] + matrix[row][prev_col]

    return matrix[num][num]


def create_matrix(number):
    number += 1
    return [[0] * number for num in range(number)]


def main():
    lattice_paths(2)
    lattice_paths(20)

