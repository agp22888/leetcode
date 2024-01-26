class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:
            x = -x
        result = 0
        while True:
            result += x % 10
            x = x // 10
            if x == 0:
                break
            result *= 10
        if result >= 2147483648:
            return 0
        return (-1 if negative else 1) * result


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
