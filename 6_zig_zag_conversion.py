class Solution:
    def convert(self, string: str, num_rows: int) -> str:
        if num_rows < 2:
            return string
        if len(string) < num_rows:
            return string
        levels = num_rows * 2 - 2
        result = []
        steps = [levels, 0]
        for i in range(num_rows):
            self._var_step(string, result, i, steps)
            steps[0] -= 2
            steps[1] += 2
        return ''.join(result)

    @staticmethod
    def _var_step(string: str,
                  result: list[str],
                  start: int,
                  steps: list[int]):
        index = 0
        while start < len(string):
            step = steps[index]
            if step != 0:
                result.append(string[start])
            start += step
            index = (index + 1) & 1


if __name__ == '__main__':
    sol = Solution()
    tasks = [('PAYPALISHIRING', 3, "PAHNAPLSIIGYIR"),
             ('PAYPALISHIRING', 4, "PINALSIGYAHRPI"),
             ('A', 1, "A"),
             ('ABC', 1, "ABC"),
             ('A', 2, "A"), ]
    for s, n, a in tasks:
        res = sol.convert(s, n)
        # print(res)
        assert res == a
