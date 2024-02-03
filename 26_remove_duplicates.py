class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    sol = Solution()
    tasks = [
        [[1, 1, 2], [1, 2, 2], 2],
    ]
    for t, r_lst, r_len in tasks:
        k = sol.removeDuplicates(t)
        assert k == r_len
        for i in range(k):
            assert t[i] == r_lst[i]
