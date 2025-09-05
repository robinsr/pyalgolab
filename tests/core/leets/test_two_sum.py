import pytest
from core.leets.two_sum import add, two_sum

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

@pytest.mark.parametrize("a, b, expected", [
    ([2,3,6,8], 5, (0,1)),
    ([2,3,6,8], 10, (0,3)),
    ([2,3,6,8], 14, (2,3)),
    ([2,3,6,8], 9, (1,2)),
])
def test_add_parametrized(a, b, expected):
    assert two_sum(a, b) == expected