from util.util import ListNode
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
    import random
    import time

    k_bound = 5000
    list_len_bound = 5000
    val_bound = 1000
    num_test = 10
    sol = SolutionFast()
    sol.reverseKGroup(ListNode.list_to_list_node([1, 2, 3, 4, 5]), 2)
    exit(0)
    # for tk in range(10):
    #     print(ListNode.listnode_to_list(sol.reverseKGroup(ListNode.list_to_listnode([659, 2997, 4319, 2337, 751, 4367, 3030, 872, 3272, 2540]), tk)))
    #     print(swap_list([659, 2997, 4319, 2337, 751, 4367, 3030, 872, 3272, 2540], tk))
    #     print('____')
    # exit(0)
    l1 = [random.randint(0, val_bound) for x in range(list_len_bound)]

    for _ in range(num_test):
        ln1 = ListNode.list_to_list_node(l1)
        k = random.randint(0, len(l1))
        # print(l1)
        # print(k)
        l1_rev = swap_list(l1, k)
        start = time.time()
        ln1_rev = sol.reverseKGroup(ln1, k)
        # print(ln1_rev)
        # print(l1_rev)
        assert ListNode.list_node_to_list(ln1_rev) == l1_rev
        # print(f'len(lst)={len(l1)}, run_time={time.time() - start}')
    # ln2 = ListNode.list_to_listnode(l2)
    # assert ListNode.listnode_to_list(ln1) == l1
    # assert ListNode.listnode_to_list(ln2) == l2
    # assert ListNode.listnode_to_list(sol.reverseKGroup(ln1, 4)) == [3, 2, 7, 5, 11]
    # assert ListNode.listnode_to_list(sol.reverseKGroup(ln2, 4)) == [1]
