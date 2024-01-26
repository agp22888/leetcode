# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def intToRoman(self, num: int) -> str:
        parts = "MDCLXVI"
        result = ""
        thousands = num // 1000
        result += thousands * 'M'
        for i in range(3):
            result += self.convert((num // 10 ** (2 - i)) % 10, parts[i * 2: i * 2 + 3])
        return result

    def convert(self, digit: int, mask: str) -> str:
        if digit < 4:
            return mask[-1] * digit
        elif digit == 4:
            return mask[-1] + mask[-2]
        elif digit < 9:
            return mask[1] + (digit - 5) * mask[-1]
        else:
            return mask[-1] + mask[0]


if __name__ == "__main__":
    s = Solution()
    assert s.intToRoman(1988) == "MCMLXXXVIII"
    assert s.intToRoman(1475) == "MCDLXXV"
    assert s.intToRoman(2023) == "MMXXIII"
    assert s.intToRoman(2234) == "MMCCXXXIV"
    assert s.intToRoman(45) == "XLV"
