import pytest
from core.search.binary_search import binary_search


@pytest.mark.parametrize("a, b, expected", [
    ([2,3,6,8], 2, 0),
    ([2,3,6,8], 3, 1),
    ([2,3,6,8], 6, 2),
    ([2,3,6,8], 8, 3),
    ([2,3,6,8], 7, -1),
])
def test_binary_search(a, b, expected):
    assert binary_search(a, b) == expected