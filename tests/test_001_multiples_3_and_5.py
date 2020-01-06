import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname('./src/solutions')))
from solutions._001_multiples_3_and_5 import multiples


parameters = [
    (1000, 233168),
    (49, 543),
    (19564, 89301183),
    (8456, 16687353)
]

@pytest.mark.parametrize("n_input,expected", parameters)
def test_multiples_3_and_5(n_input, expected):
    assert multiples(n_input) == expected, f"Excepted {expected}"
    