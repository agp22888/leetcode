class Solution:
    int_max = 2147483647
    int_min = -2147483648

    @staticmethod
    def my_int(c: str) -> int | None:
        match c:
            case "0":
                return 0
            case "1":
                return 1
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case "5":
                return 5
            case "6":
                return 6
            case "7":
                return 7
            case "8":
                return 8
            case "9":
                return 9
        return None

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
            if (converted := self.my_int(ch)) is None:
                break
            result = result * 10 + converted
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
