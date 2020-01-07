import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._007_10001_prime import search_prime

parameters = [
    (6, 13),
    (10001, 104743)
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_search_prime(n_input, expected):
    assert search_prime(n_input) == expected, f"Excepted {expected}"
