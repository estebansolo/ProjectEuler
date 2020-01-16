import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname("./src/solutions")))
from solutions._016_power_digit_sum import power_digit_sum

parameters = [(15, 26), (1000, 1366)]


@pytest.mark.parametrize("n_input,expected", parameters)
def test_power_digit_sum(n_input, expected):
    assert power_digit_sum(n_input) == expected, f"Excepted {expected}"
