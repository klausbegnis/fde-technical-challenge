import pytest
from main import sort

examples = [
    (100, 100, 100, 10, "SPECIAL"),
    (100, 100, 100, 20, "REJECTED"),
    (10, 10, 10, 10, "STANDARD"),
    (100, 200, 100, 10, "SPECIAL"),
    (100, 200, 100, 20, "REJECTED"),
]

@pytest.mark.parametrize("width, height, length, mass, expected", examples)
def test_sort(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected