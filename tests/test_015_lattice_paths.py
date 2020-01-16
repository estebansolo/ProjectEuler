import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname("./src/solutions")))
from solutions._015_lattice_paths import lattice_paths

parameters = [(2, 6), (20, 137846528820)]


@pytest.mark.parametrize("n_input,expected", parameters)
def test_lattice_paths(n_input, expected):
    assert lattice_paths(n_input) == expected, f"Excepted {expected}"
