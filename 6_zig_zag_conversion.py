class Solution:
    def convert(self, string: str, num_rows: int) -> str:
        dim_h = int(len(string))
        dim_v = num_rows
        matrix = [['' for _ in range(dim_h)] for _ in range(dim_v)]
        h, v = 0, 0
        diag = False
        for ch in string:
            matrix[v][h] = ch
            if not diag:
                if v < dim_v - 1:
                    v += 1
                else:
                    if v == 0:
                        h += 1
                        continue
                    v -= 1
                    h += 1
                    diag = True
            else:
                if v == 0:
                    v += 1
                    diag = False
                else:
                    v -= 1
                    h += 1
        return ''.join([''.join(x) for x in matrix])


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
