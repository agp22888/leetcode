import random


# runtime 88.06% memory 51.2%

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s_nums = sorted(zip(nums, range(len(nums))), key=lambda x: x[0])
        start, stop = 0, len(nums) - 1
        while start < stop:
            if (two_sum := s_nums[start][0] + s_nums[stop][0]) > target:
                stop -= 1
            elif two_sum < target:
                start += 1
            else:
                result = [s_nums[start][1], s_nums[stop][1]]
                return result


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
