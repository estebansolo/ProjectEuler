import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname("./src/solutions")))
from solutions._014_longest_collatz_sequence import collatz, longest_collatz


def test_collatz():
    expected = 10
    assert collatz(13) == expected, f"Excepted {expected}"


def test_longest_collatz():
    expected = (837799, 525)
    assert longest_collatz(1000000) == expected, f"Excepted {expected}"
