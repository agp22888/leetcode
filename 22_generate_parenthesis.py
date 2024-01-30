class Solution:
    _cache = {1: {"()"}}

    def generateParenthesis(self, n: int) -> list[str]:
        return list(self.recurse_parenthesis(n))

    def recurse_parenthesis(self, n: int) -> set[str]:
        if n in self._cache:
            return self._cache[n]
        result = set()
        for i in range(1, n):
            for start in self.recurse_parenthesis(i):
                for end in self.recurse_parenthesis(n - i):
                    result.add(f'{start}{end}')
        result.update({f'({x})' for x in self.recurse_parenthesis(n - 1)})
        self._cache[n] = result
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.generateParenthesis(1) == ["()"]
    assert sol.generateParenthesis(3).sort() == ["((()))", "(()())", "(())()", "()(())", "()()()"].sort()
