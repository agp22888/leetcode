class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:
            x = -x
        digits = []
        while x > 0:
            # int1 = int(10 ** i)
            digits.append(x % 10)
            x = x // 10
        count = 0
        result = 0
        for d in digits:
            result += d * 10 ** (len(digits) - count - 1)
            count += 1
        if result >= 2147483648:
            return 0
        return (-1 if negative else 1) * result


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
