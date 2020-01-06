import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._006_sum_square_difference import sum_square_difference

parameters = [
    (10, 2640),
    (100, 25164150)
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_sum_square_difference(n_input, expected):
    assert sum_square_difference(n_input) == expected, f"Excepted {expected}"
