class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = j = 0
        nums_sorted = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        while True:
            if i >= nums1_len and j < nums2_len:
                nums_sorted.extend(nums2[j:])
                break
            elif j >= nums2_len and i < nums1_len:
                nums_sorted.extend(nums1[i:])
                break
            elif j < nums2_len and i < nums1_len:
                if nums1[i] < nums2[j]:
                    nums_sorted.append(nums1[i])
                    i += 1
                else:
                    nums_sorted.append(nums2[j])
                    j += 1
            else:
                break
        mid = len(nums_sorted) // 2
        if len(nums_sorted) % 2 == 0:
            result = (nums_sorted[mid] + nums_sorted[mid - 1]) / 2
        else:
            result = nums_sorted[mid]
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
