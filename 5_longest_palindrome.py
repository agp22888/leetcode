class Solution:
    def longestPalindrome(self, s: str) -> str:
        sequences = self.scan_for_sequences(s)
        longest_palindrome = ''
        singles = list(range(len(s)))
        for pos, l in sequences:
            for i in range(pos, pos + l):
                singles.remove(i)
            a, b = pos, pos + l - 1

            palindrome = self.get_longest_palindrome(s, a, b)
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
        for single in singles:
            palindrome = self.get_longest_palindrome(s, single, single)
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
        return longest_palindrome

    def get_longest_palindrome(self, s: str, start: int, end: int) -> str:
        length = end - start + 1
        try:
            while end < len(s) and start >= 0 and s[end] == s[start]:
                end += 1
                start -= 1
                length += 2
        except IndexError:
            pass
        return s[start + 1:end]

    def scan_for_sequences(self, s: str) -> list[tuple[int, int]]:
        result = []
        prev_char = None
        start = None
        pos = 0
        for c in s:
            if c == prev_char:
                if start is None:
                    start = pos - 1
            else:
                if start is not None:
                    result.append((start, pos - start))
                    start = None

            pos += 1
            prev_char = c
        if start is not None:
            result.append((start, pos - start))
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindrome('babad') == 'bab'
    assert sol.longestPalindrome('cbbd') == 'bb'
