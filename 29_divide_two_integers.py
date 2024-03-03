class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend = -dividend
        if divisor < 0:
            sign *= -1
            divisor = -divisor
        if dividend == 0 or dividend < divisor:
            return 0
        if dividend == divisor:
            return 1 * sign
        if divisor == 1:
            return self.trunc(dividend * sign)

        dividend_bl = self.get_bit_len(dividend)
        divisor_bl = self.get_bit_len(divisor)
        temp = dividend >> (dividend_bl - divisor_bl)
        result = 0
        mask_pos = dividend_bl - divisor_bl - 1
        while mask_pos >= 0:
            if temp < divisor:
                result <<= 1
            else:
                result = (result << 1) + 1
                temp -= divisor
            temp <<= 1
            temp += (dividend & (1 << mask_pos)) >> mask_pos
            mask_pos -= 1
        result = (result << 1) + (1 if temp >= divisor else 0)
        return self.trunc(result * sign)

    def trunc(self, num):
        min_result = -2 ** 31
        max_result = 2 ** 31 - 1
        if num < min_result:
            return min_result
        elif num > max_result:
            return max_result
        else:
            return num

    def get_bit_len(self, num):
        bit_len = 0
        while num != 0:
            num >>= 1
            bit_len += 1
        return bit_len


if __name__ == "__main__":
    sol = Solution()
    tasks = (
        (1, -1),
        (10, 10),
        (3, 10),
        (10, 3),
        (7, -3),
        (-7, -3),
        (0, 1),
        (1000000000, 1),
        (-32, 2),
        (-2147483648, 2),
        (-231, 3),
    )
    for dividend, divisor in tasks:
        assert sol.divide(dividend, divisor) == int(dividend / divisor)
