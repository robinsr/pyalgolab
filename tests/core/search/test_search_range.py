import pytest
from core.search.search_range import search_range  # implement this

@pytest.mark.parametrize("nums, target, expected", [
    # example-style
    ([5,7,7,8,8,10], 8, [3,4]),
    ([5,7,7,8,8,10], 6, [-1,-1]),
    ([], 0, [-1,-1]),

    # single element
    ([1], 1, [0,0]),
    ([1], 0, [-1,-1]),

    # all elements same
    ([2,2,2,2], 2, [0,3]),
    ([2,2,2,2], 3, [-1,-1]),

    # target spans interior
    ([1,2,2,2,3,4], 2, [1,3]),
    ([1,1,2,3,3,3,4,5], 3, [3,5]),

    # target at boundaries
    ([1,1,1,2,3], 1, [0,2]),
    ([1,2,3,3,3], 3, [2,4]),

    # target smaller than first / larger than last
    ([10,20,30], 5, [-1,-1]),
    ([10,20,30], 40, [-1,-1]),

    # negatives and mixed
    ([-10,-5,-5,-5,0,1], -5, [1,3]),
    ([-5,-3,-1,0,2,2,2,9], 2, [4,6]),
])
def test_search_range(nums, target, expected):
    # Preconditions from problem statement
    assert nums == sorted(nums)
    assert all(isinstance(x, int) for x in nums)
    assert isinstance(target, int)

    assert search_range(nums, target) == expected