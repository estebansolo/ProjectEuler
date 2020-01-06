import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._003_largest_prime_factor import largest_prime_factor

parameters = [
    (13195, 29),
    (600851475143, 6857),
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_largest_prime_factor(n_input, expected):
    assert largest_prime_factor(n_input) == expected, f"Expected {expected}"
