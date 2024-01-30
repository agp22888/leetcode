from util.util import compare_list_of_ints_ignore_order


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        r = set()
        nums_len = len(nums)
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i - 1]:
                continue
            j, k = i + 1, nums_len - 1
            target = 0 - num
            while j < k:
                s = nums[j] + nums[k]
                if target - s < 0:
                    k -= 1
                elif target - s > 0:
                    j += 1
                else:
                    r.add((num, nums[j], nums[k]))
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        result = [list(x) for x in r]
        # print(result)
        return result


if __name__ == '__main__':
    sol = Solution()
    assert compare_list_of_ints_ignore_order(sol.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    assert compare_list_of_ints_ignore_order(sol.threeSum([0, 1, 1]), [])
    assert compare_list_of_ints_ignore_order(sol.threeSum([0, 0, 0]), [[0, 0, 0]])
    assert compare_list_of_ints_ignore_order(sol.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]),
                                             [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3],
                                  [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]])
