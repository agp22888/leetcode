class Solution:
    def romanToInt(self, s: str) -> int:
        # MDCLXVI
        map = {"M": 1000,
               "D": 500,
               "C": 100,
               "L": 50,
               "X": 10,
               "V": 5,
               "I": 1
               }
        result = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                result += map[s[i]]
                break
            if map[s[i + 1]] > map[s[i]]:
                result += map[s[i + 1]] - map[s[i]]
                i += 1
            else:
                result += map[s[i]]
            i += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("MCDXLV") == 1445
    assert sol.romanToInt("LXXXV") == 85
    assert sol.romanToInt("MLXXV") == 1075
    assert sol.romanToInt("MCCCLXXV") == 1375
    assert sol.romanToInt("MCM") == 1900
    assert sol.romanToInt("XL") == 40
    assert sol.romanToInt("IX") == 9
