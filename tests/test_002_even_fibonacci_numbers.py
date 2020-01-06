import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._002_even_fibonacci_numbers import even_fibonacci

parameters = [
    (89, 44),
    (4000000, 4613732)
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_even_fibonacci(n_input, expected):
    assert even_fibonacci(n_input) == expected, f"Excepted {expected}"