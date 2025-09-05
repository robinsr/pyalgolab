"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
  • 0 <= nums.length <= 10^5
  • -10^9 <= nums[i] <= 10^9
  • nums is a non-decreasing array.
  • -10^9 <= target <= 10^9
"""


def lower_bound(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    lo = 0
    hi = len(nums) - 1
    ans = -1

    while lo <= hi:
        mid = (lo + hi) >> 1

        if target == nums[mid]:
            ans = mid

        if target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return ans

def upper_bound(nums: list[int], target: int) -> int:
    if not nums:
        return -1

    lo = 0
    hi = len(nums) - 1
    ans = -1

    while lo <= hi:
        mid = (lo + hi) >> 1

        if target == nums[mid]:
            ans = mid

        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return ans


def search_range(nums: list[int], target: int) -> list[int]:
    return [lower_bound(nums, target), upper_bound(nums, target)]