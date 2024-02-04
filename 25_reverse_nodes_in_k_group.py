from util.util import ListNode, list_to_list_node
from util.util import swap_list


class Solution:
    def swap_pair(self, prev_head: ListNode, dist: int) -> tuple[ListNode, bool]:
        prev_h = prev_t = prev_head
        h = t = prev_head.next
        if not t:
            return prev_head, False
        for _ in range(dist - 1):
            t = t.next
            if not t:
                return prev_head, False
            prev_t = prev_t.next
        prev_h.next = t
        tmp = t.next
        if h is not prev_t:
            prev_t.next = h
            t.next = h.next
        else:
            t.next = h
        h.next = tmp
        return prev_h, True

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k <= 1:
            return head
        result = ListNode()
        result.next = head
        h = result
        while True:
            t = h.next
            for i in range(k, 0, -2):
                h, res = self.swap_pair(h, i)
                if not res:
                    break
                h = h.next
            h = t
            if not h or not h.next:
                return result.next


class SolutionFast:
    def length(self, head: ListNode | None) -> int:
        size = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            size += 1
        return size

    def solve(self, head: ListNode | None, k: int, size: int):
        if not head:
            return head
        if k > size:
            return head
        curr = head
        prev = None
        nn = None
        ct = 0
        while curr and ct < k:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
            ct += 1
        head.next = self.solve(nn, k, size - k)
        return prev

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        size = self.length(head)
        return self.solve(head, k, size)


if __name__ == "__main__":
    sol = SolutionFast()
    tasks = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3)
    ]
    for lst, k in tasks:
        orig = list_to_list_node(lst)
        print(orig)
        check = list_to_list_node(swap_list(lst, k))
        print(check)
        res = sol.reverseKGroup(orig, k)
        print(res)
        assert res == check
        print('-------')
