# Definition for singly-linked list.
from copy import copy

from util.util import ListNode, list_node_to_list, list_to_list_node


class Solution:
    def removeNthFromEnd__(self, head: ListNode, n: int) -> ListNode | None:
        l = []
        while head is not None:
            l.append(head)
            head = head.next
        if len(l) < 2:
            return None
        if n == len(l):
            return l[1] if len(l) > 1 else None
        l[len(l) - n - 1].next = l[-n + 1] if -n + 1 < 0 else None
        return l[0]

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode | None:
        t = head
        count = 0
        while t:
            t = t.next
            count += 1
        t = head
        if n == count:
            return head.next
        for _ in range(count - n - 1):
            t = t.next
        t.next = t.next.next if t.next else None
        return head


if __name__ == "__main__":
    import random

    sol = Solution()
    assert sol.removeNthFromEnd(list_to_list_node([1, 2, 3, 4, 5]), 2) == list_to_list_node([1, 2, 3, 5])
    assert sol.removeNthFromEnd(list_to_list_node([1]), 1) == list_to_list_node([])
    assert sol.removeNthFromEnd(list_to_list_node([1, 2]), 1) == list_to_list_node([1])

    number_of_tests = 10000
    for _ in range(number_of_tests):
        list_len = random.randint(1, 30)
        pos = random.randint(1, list_len)
        original_vals = [random.randint(0, 100) for _ in range(list_len)]
        result_vals = copy(original_vals)
        result_vals.pop(list_len - pos)
        original_list_node = list_to_list_node(original_vals)
        result_list_node = list_to_list_node(result_vals)
        print(list_len)
        print(pos)
        print(original_list_node)
        print(result_list_node)
        calculated_list_node = sol.removeNthFromEnd(original_list_node, pos)
        print(calculated_list_node)
        assert calculated_list_node == result_list_node
