from util.util import compare_list_of_ints_ignore_order


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        if not nums:
            return []
        nums.sort()
        ave_val = target // 4
        if nums[0] > ave_val or nums[-1] < ave_val:
            return []
        result = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                head = j + 1
                tail = len(nums) - 1
                while head < tail:
                    s = nums[i] + nums[j] + nums[head] + nums[tail]
                    if s > target:
                        tail -= 1
                    elif s == target:
                        result.append([nums[i], nums[j], nums[head], nums[tail]])
                        tail -= 1
                        while tail > head and nums[tail + 1] == nums[tail]:
                            tail -= 1
                    else:
                        head += 1
                j += 1
                while 0 < j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while 0 < i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    tasks = (
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([9, 1, 2, -5, -8, -3, 9, 6, -5, 2], 5, [[-8, -5, 9, 9], [-5, 2, 2, 6], [-8, 2, 2, 9], [-5, -5, 6, 9]]),
        ([-1, 0, 1, 2, -1, -4], -1, [[-4, 0, 1, 2], [-1, -1, 0, 1]]),
        ([-3, -2, -1, 0, 0, 1, 2, 3], 0,
         [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2],
          [-1, 0, 0, 1]])
    )
    for lst, tgt, res in tasks:
        four_sum = sol.fourSum(lst, tgt)
        print(four_sum)
        print(res)
        assert compare_list_of_ints_ignore_order(four_sum, res)
