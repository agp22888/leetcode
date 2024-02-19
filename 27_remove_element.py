class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums_l = len(nums)
        if nums_l == 0:
            return 0
        start = 0
        while nums[start] != val:
            start += 1
            if start == nums_l:
                return start
        end = start + 1
        while True:
            try:
                if nums[end] == val:
                    end += 1
                    continue
            except IndexError:
                break
            nums[start] = nums[end]
            start += 1
            end += 1
        return start


if __name__ == "__main__":
    sol = Solution()
    tasks = (
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3]),
        ([], 2, []),
        ([1], 1, []),
        ([1, 2, 3], 4, [1, 2, 3])
    )
    for n, v, expected_nums in tasks:
        k = sol.removeElement(n, v)
        assert k == len(expected_nums);
        sorted_result = sorted(n[:k])
        expected_nums.sort()
        for i in range(len(expected_nums)):
            assert sorted_result[i] == expected_nums[i]
