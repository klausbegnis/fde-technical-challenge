import pytest
from main import sort

valid_examples = [
    (100, 100, 100, 10, "SPECIAL"),
    (100, 100, 100, 20, "REJECTED"),
    (10, 10, 10, 10, "STANDARD"),
    (100, 200, 100, 10, "SPECIAL"),
    (100, 200, 100, 20, "REJECTED"),
]


@pytest.mark.parametrize("width, height, length, mass, expected", valid_examples)
def test_sort_valid_examples(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected


invalid_examples = [
    (0, 100, 100, 10),
    (100, 0, 100, 10),
    (100, 100, 0, 10),
    (100, 100, 100, 0),
]


@pytest.mark.parametrize("width, height, length, mass", invalid_examples)
def test_sort_invalid_examples(width, height, length, mass):
    with pytest.raises(ValueError):
        sort(width, height, length, mass)
