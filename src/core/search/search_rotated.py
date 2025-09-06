"""
Search in Rotated Sorted Array

You are given an integer array nums that was originally sorted in strictly increasing order and then rotated at an unknown pivot index k (0 <= k < nums.length). For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

Given an integer target, return the index of target if it is in nums. Otherwise, return -1.

You must write an algorithm with O(log n) time complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:
    •   1 <= nums.length <= 10^4
    •   -10^4 <= nums[i], target <= 10^4
    •   All values of nums are distinct.
    •   nums is a rotated version of a strictly increasing array.
"""

def _bin_search(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) >> 1

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            # T is greater, take right
            lo = mid + 1
        else:
            hi = mid - 1

    return -1

def search_rotated(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    lo = 0
    hi = len(nums) - 1
    pivot = 0

    while lo <= hi:
        mid = (lo + hi) >> 1

        # which side is sorted?
        if nums[lo] <= nums[mid]:
            # low should be lower than the higher mid index, so left is sorted
            left = _bin_search(nums[lo:mid], target)

            if left != -1:
                return left

        else:
            right = _bin_search(nums[mid:hi], target)

            if right != -1:
                return right

        # no what?

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            # T is greater, take right
            lo = mid + 1
        else:
            hi = mid - 1

    return -1