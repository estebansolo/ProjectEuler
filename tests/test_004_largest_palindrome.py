import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._004_largest_palindrome import largest_palindrome_product

parameters = [
    (2, 9009),
    (3, 906609)
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_largest_palindrome_product(n_input, expected):
    assert largest_palindrome_product(n_input) == expected, f"Excepted {expected}"