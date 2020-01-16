import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname("./src/solutions")))
from solutions._012_highly_divisible_triangular_number import highly_triangular_number


parameters = [
    (5, (7, 28)),
    (500, (12375, 76576500))
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_highly_triangular_number(n_input, expected):
    assert highly_triangular_number(n_input) == expected, f"Excepted {expected}"
