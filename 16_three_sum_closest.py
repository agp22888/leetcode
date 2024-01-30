class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = 0
        min_dist = 2147483648
        for i in range(len(nums)):
            head = i + 1
            tail = len(nums) - 1
            while head < tail:
                dist = nums[i] + nums[head] + nums[tail] - target
                if abs(dist) < min_dist:
                    min_dist = abs(dist)
                    result = nums[i] + nums[head] + nums[tail]
                if dist < 0:
                    head += 1
                elif dist > 0:
                    tail -= 1
                else:
                    break
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert sol.threeSumClosest([0, 0, 0], 1) == 0
    assert sol.threeSumClosest([1, 1, 1, 0], -100) == 2
    assert sol.threeSumClosest([2, 3, 8, 9, 10], 16) == 15
    assert sol.threeSumClosest([-1000, -5, -5, -5, -5, -5, -5, -1, -1, -1], -14) == -15
