import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname("./src/solutions")))
from solutions._013_large_sum import get_digits, largest_sum


def test_largest_sum_digits():
    digits = get_digits()

    expected = "5537376230"
    assert largest_sum(digits, 10) == expected, f"Excepted {expected}"
