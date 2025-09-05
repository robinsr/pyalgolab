def add(a: int, b: int) -> int:
    return a + b


def two_sum(nums: [int], target: int) -> (int, int):
    seen = {}

    for x in range(len(nums)):
        num = nums[x]
        counterpart = target - num

        if counterpart in seen:
            return (seen[counterpart], x)
        else:
            seen[num] = x

    return (0,0)
