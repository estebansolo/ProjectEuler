import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._009_special_pythagorean_triplet import special_pythagorean_triplet

parameters = [
    (24, 480),
    (30, 780),
    (48, 3840),
    (1000, 31875000),
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_special_pythagorean_triplet(n_input, expected):
    _, value = special_pythagorean_triplet(n_input)
    assert value == expected, f"Excepted {expected}"


def test_special_pythagorean_triplet_false():
    assert not special_pythagorean_triplet(50), "Expected False"