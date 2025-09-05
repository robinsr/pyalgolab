import math


def binary_search(nums: [int], target: int) -> int:
  lo = 0
  hi = len(nums) - 1

  while lo <= hi:
    mid = math.floor((lo + hi) / 2)

    if nums[mid] == target:
      return mid
    elif target < nums[mid]:
      # take left
      hi = mid - 1
    else:
      # take right
      lo = mid + 1

  return -1

