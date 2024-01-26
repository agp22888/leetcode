import re
import string


class Solution:
    int_max = 2147483647
    int_min = -2147483648
    char_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,

    }

    def myAtoi_(self, s: str) -> int:
        match = re.search(r'^ *([+|-]?[0123456789]+)', s)
        if not match:
            return 0
        result = int(match.group())
        if result > 0:
            result = min(result, self.int_max)
        else:
            result = max(result, self.int_min)
        return result

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        start = 0
        positive = True
        if s[0] in ('+', '-'):
            start = 1
            positive = s[0] == '+'
        result = 0
        for ch in s[start:]:
            try:
                result = result * 10 + self.char_dict[ch]
            except KeyError:
                break
        result = (1 if positive else -1) * result
        if positive:
            result = min(result, self.int_max)
        else:
            result = max(result, self.int_min)
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.myAtoi(' ') == 0
    assert sol.myAtoi('42') == 42
    assert sol.myAtoi('+42') == 42
    assert sol.myAtoi('    42') == 42
    assert sol.myAtoi('-42') == -42
    assert sol.myAtoi('     -42') == -42
    assert sol.myAtoi('42    ') == 42
    assert sol.myAtoi('42da') == 42
    assert sol.myAtoi('42        d') == 42
    assert sol.myAtoi("words and 987") == 0
    assert sol.myAtoi("-91283472332") == -2147483648
