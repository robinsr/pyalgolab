import pytest
from core.search.search_rotated import search_rotated

# --- basic examples (from prompt-like cases) ---
# @pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
])
def test_search_rotated_basic(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- no rotation (k = 0) ---
# @pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([1,2,3,4,5,6,7], 1, 0),
    ([1,2,3,4,5,6,7], 7, 6),
    ([1,2,3,4,5,6,7], 8, -1),
])
def test_search_rotated_no_rotation(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- rotated mid ---
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([6,7,0,1,2,3,4,5], 0, 2),
    ([6,7,0,1,2,3,4,5], 6, 0),
    ([6,7,0,1,2,3,4,5], 5, 7),
    ([6,7,0,1,2,3,4,5], 9, -1),
])
def test_search_rotated_mid(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- rotated by 1 (pivot near end) ---
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([7,1,2,3,4,5,6], 7, 0),
    ([7,1,2,3,4,5,6], 6, 6),
    ([7,1,2,3,4,5,6], 4, 4),
])
def test_search_rotated_by_one(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- rotated by len-1 (pivot near start) ---
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([2,3,4,5,6,7,1], 1, 6),
    ([2,3,4,5,6,7,1], 2, 0),
    ([2,3,4,5,6,7,1], 7, 5),
])
def test_search_rotated_by_negative_one(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- small arrays ---
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([2,3], 2, 0),
    ([2,3], 3, 1),
    ([2,3], 1, -1),

    ([3,1,2], 1, 1),
    ([3,1,2], 2, 2),
    ([3,1,2], 3, 0),
    ([3,1,2], 4, -1),
])
def test_search_rotated_sm_array(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- single element ---
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([5], 5, 0),
    ([5], -5, -1),
])
def test_search_rotated_single_elem(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- larger rotation patterns ---
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([15,16,17,18,19,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], 0, 5),
    ([15,16,17,18,19,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], 19, 4),
    ([15,16,17,18,19,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], 11, 16),
])
def test_search_rotated_lg_array(nums, target, expected):
    assert search_rotated(nums, target) == expected



# --- targets outside range ---
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("nums, target, expected", [
    ([9,10,11,12,13,1,2,3,4,5,6,7,8], -10, -1),
    ([9,10,11,12,13,1,2,3,4,5,6,7,8], 100, -1),
])
def test_search_rotated_out_of_range(nums, target, expected):
    assert search_rotated(nums, target) == expected