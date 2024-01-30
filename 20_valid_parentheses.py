class Solution:
    def isValid(self, s: str) -> bool:
        open = {"[", "{", "("}
        close = {"]": "[", "}": "{", ")": "("}
        par_list = []
        if s[0] not in open:
            return False
        for c in s:
            if len(par_list) == 0:
                if c in open:
                    par_list.append([c, 1])
                else:
                    return False
                continue
            if c in open:
                if par_list[-1][0] != c:
                    par_list.append([c, 1])
                else:
                    par_list[-1][1] += 1
            elif c in close:
                if par_list[-1][0] != close[c] or par_list[-1][1] == 0:
                    return False
                else:
                    par_list[-1][1] -= 1
            if par_list[-1][1] == 0:
                par_list.pop(-1)
        return len(par_list) == 0


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()")
    assert s.isValid("[](){}")
    assert not s.isValid("[}")
    assert s.isValid("([{}])")
    assert not s.isValid("([{]})")
    assert not s.isValid(")[")
    assert not s.isValid("(){}}{")
