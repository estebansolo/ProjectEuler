import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._010_summation_of_primes import summation_primes

parameters = [
    (10, 17),
    (2000000, 142913828922),
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_summation_primes(n_input, expected):
    assert summation_primes(n_input) == expected, f"Excepted {expected}"
