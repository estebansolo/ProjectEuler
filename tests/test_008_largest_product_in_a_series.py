import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._008_largest_product_in_a_series import largest_product_serie

parameters = [
    (4, 5832),
    (13, 23514624000)
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_largest_product_serie(n_input, expected):
    value, seq = largest_product_serie(n_input)
    assert value == expected, f"Excepted {expected}"
