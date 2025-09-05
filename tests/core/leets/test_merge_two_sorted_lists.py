import pytest
from core.leets.merge_two_sorted_lists import merge_two_sorted_lists
from helpers.list_node import build_list, to_list


@pytest.mark.parametrize("a, b, expected", [
    ([], [], []),
    ([], [0], [0]),
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([2,5,7], [3,11], [2,3,5,7,11]),
    ([1,1,1], [1,1,1], [1,1,1,1,1,1]),
    ([1,3,5], [2,4,6], [1,2,3,4,5,6]),
    ([5,6,7], [], [5,6,7]),
    ([], [5,6,7], [5,6,7]),
    ([1,2,3], [4,5,6], [1,2,3,4,5,6]),
    ([4,8,15], [16,23,42], [4,8,15,16,23,42]),
])
def test_merge_two_lists(a, b, expected):
    l1 = build_list(a)
    l2 = build_list(b)

    assert merge_two_sorted_lists(l1, l2)  == expected