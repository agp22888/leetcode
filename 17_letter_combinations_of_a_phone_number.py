from util.util import compare_list_ignore_order


class Solution:
    letters = {
        "1": " ",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        return self.get_letters(digits)

    def get_letters(self, _digits: str) -> list[str]:
        if len(_digits) == 1:
            return [x for x in self.letters[_digits[-1]]]
        result = []
        sub_letters = self.get_letters(_digits[1:])
        for c in self.letters[_digits[0]]:
            result.extend([c + x for x in sub_letters])
        return result


if __name__ == "__main__":
    sol = Solution()
    assert compare_list_ignore_order(sol.letterCombinations("23"),
                                     ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    assert compare_list_ignore_order(sol.letterCombinations(""), [])
    assert compare_list_ignore_order(sol.letterCombinations("2"), ["a", "b", "c"])
