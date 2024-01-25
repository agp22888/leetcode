import datetime
import time


class Solution:
    def lengthOfLongestSubstring_(self, s: str) -> int:  # two pointers
        s_len = len(s)
        if s_len <= 1:
            return s_len
        max_len = 0
        c_dict = {}
        start, end = 0, 1
        c_dict[s[start]] = 1
        c_dict[s[end]] = c_dict.get(s[end], 0) + 1
        while True:
            if c_dict[s[end]] > 1:
                max_len = max(max_len, end - start)
                while c_dict[s[end]] > 1:
                    c_dict[s[start]] -= 1
                    start += 1
            end += 1
            if end == s_len:
                max_len = max(end - start, max_len)
                break
            c_dict[s[end]] = c_dict.get(s[end], 0) + 1
        return max_len

    # VVVVVVVVVVV
    # not mine
    # very clever, ~ 15% faster
    # VVVVVVVVVVV
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_seen_at = {}
        max_len = 0
        start = 0
        for i, c in enumerate(s):
            if char_seen_at.get(c, -1) >= start:
                start = char_seen_at[c] + 1
            max_len = max(max_len, i - start + 1)
            char_seen_at[c] = i
        return max_len


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("p") == 1
    assert sol.lengthOfLongestSubstring("pw") == 2
    assert sol.lengthOfLongestSubstring("dvdf") == 3
