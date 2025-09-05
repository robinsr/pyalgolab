import pytest
from core.search.search_insert import search_insert

@pytest.mark.parametrize("nums, target, expected", [
    # exact hits
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 1, 0),
    ([1,3,5,6], 6, 3),

    # insert before first
    ([10,20,30], 0, 0),
    ([-5,-2,7], -10, 0),

    # insert in middle
    ([1,3,5,6], 2, 1),
    ([1,3,5,6], 4, 2),
    ([-3,-1,2,4], 3, 3),

    # insert after last
    ([1,3,5,6], 7, 4),
    ([-2,-1,0], 5, 3),

    # single-element arrays (len >= 1, still distinct)
    ([42], 42, 0),
    ([42], 41, 0),
    ([42], 43, 1),

    # boundary values within constraints
    ([-10_000, 0, 10_000], -10_000, 0),
    ([-10_000, 0, 10_000], 10_000, 2),
])
def test_search_insert_distinct(nums, target, expected):
    # Sanity: enforce LeetCode 35 preconditions (sorted, distinct, len >= 1)
    assert nums == sorted(nums)
    assert len(nums) >= 1
    assert len(nums) == len(set(nums))

    assert search_insert(nums, target) == expected