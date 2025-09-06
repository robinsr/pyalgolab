import pytest
from core.search.search_range import search_range


def _assert_search_range(nums, target, expected):
    # Preconditions from problem statement (uncomment if adding new test cases)
    # assert nums == sorted(nums)
    # assert all(isinstance(x, int) for x in nums)
    # assert isinstance(target, int)
    got = search_range(nums, target)

    assert got == expected, f"nums={nums}, target={target}: got {got}, expected {expected}"




# --- example-style ---
@pytest.mark.parametrize("nums, target, expected", [
    ([5,7,7,8,8,10], 8, [3,4]),
    ([5,7,7,8,8,10], 6, [-1,-1]),
    ([], 0, [-1,-1]),
])
def test_search_range_examples(nums, target, expected):
    _assert_search_range(nums, target, expected)


# --- single element ---
@pytest.mark.parametrize("nums, target, expected", [
    ([1], 1, [0,0]),
    ([1], 0, [-1,-1]),
])
def test_search_range_single_elem_array(nums, target, expected):
    _assert_search_range(nums, target, expected)


# --- all elements same ---
@pytest.mark.parametrize("nums, target, expected", [
    ([2,2,2,2], 2, [0,3]),
    ([2,2,2,2], 3, [-1,-1]),
])
def test_search_range_all_elems_same(nums, target, expected):
    _assert_search_range(nums, target, expected)


# --- target spans interior ---
@pytest.mark.parametrize("nums, target, expected", [
    ([1,2,2,2,3,4], 2, [1,3]),
    ([1,1,2,3,3,3,4,5], 3, [3,5]),
])
def test_search_range_interior_span(nums, target, expected):
    _assert_search_range(nums, target, expected)


# --- target at boundaries ---
@pytest.mark.parametrize("nums, target, expected", [
    ([1,1,1,2,3], 1, [0,2]),
    ([1,2,3,3,3], 3, [2,4]),
])
def test_search_range_at_boundaries(nums, target, expected):
    _assert_search_range(nums, target, expected)


# --- target smaller than first / larger than last ---
@pytest.mark.parametrize("nums, target, expected", [
    ([10,20,30], 5, [-1,-1]),
    ([10,20,30], 40, [-1,-1]),
])
def test_search_range_target_out_of_range(nums, target, expected):
    _assert_search_range(nums, target, expected)


# --- negatives and mixed ---
@pytest.mark.parametrize("nums, target, expected", [
    ([-10,-5,-5,-5,0,1], -5, [1,3]),
    ([-5,-3,-1,0,2,2,2,9], 2, [4,6]),
])
def test_search_range_negatives_and_mixed(nums, target, expected):
    _assert_search_range(nums, target, expected)