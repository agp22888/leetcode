class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for h_i in range(len(haystack)-len(needle)+1):
            if haystack[h_i] == needle[0]:
                match = True
                for n_i, n_c in enumerate(needle):
                    if haystack[h_i + n_i] != n_c:
                        match = False
                        break
                if match:
                    return h_i
        return -1


if __name__ == '__main__':
    sol = Solution()
    assert sol.strStr('sadbutsad', 'sad') == 0
    assert sol.strStr('leetcode', 'leeto') == -1
    assert sol.strStr('a', 'a') == 0
    assert sol.strStr('a', 'b') == -1
    assert sol.strStr('abc', 'c') == 2
    assert sol.strStr('saobutsad', 'sad') == 6
    assert sol.strStr('aaa', 'aaaa') == -1
    assert sol.strStr("mississippi", "issipi") == -1
