import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))

from solutions._005_smallest_multiple import smallest_multiple

parameters = [
    (10, 2520),
    (20, 232792560)
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_smallest_multiple(n_input, expected):
    assert smallest_multiple(n_input) == expected, f"Excepted {expected}"