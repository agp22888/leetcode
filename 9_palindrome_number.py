class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        parts = self.split(x)
        head = 0
        tail = len(parts) - 1
        while True:
            if parts[head] != parts[tail]:
                return False
            if tail <= head:
                break
            head += 1
            tail -= 1
        return True

    def split(self, x: int) -> list[int]:
        l = []
        for i in range(10):
            l.append(x % 10)
            x //= 10
            if x == 0:
                break
        return l


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121)
    assert s.isPalindrome(1)
    assert not s.isPalindrome(12)
    assert s.isPalindrome(0)
    assert not s.isPalindrome(-121)
