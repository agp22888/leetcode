class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = 201
        for s in strs:
            min_len = min(min_len, len(s))
            if min_len == 0:
                return ""
        prefix = ""
        for i in range(min_len):
            for s in strs:
                if len(prefix) <= i:
                    prefix += s[i]
                    continue
                if s[i] != prefix[-1]:
                    return prefix[:-1]
        return prefix


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert sol.longestCommonPrefix(["", "racecar", "car"]) == ""
