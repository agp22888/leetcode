from util.util import ListNode, list_to_list_node, list_node_to_list, swap_list


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return
        if not head.next:
            return head
        left = head
        head = head.next
        prev = None
        while left and left.next:
            right = left.next
            left.next = right.next
            right.next = left
            if prev:
                prev.next = right
            prev = left
            left = left.next
        return head


if __name__ == "__main__":
    sol = Solution()
    tasks = [
        [1, 2, 3, 4, 5],
        [1, 3, 5, 7, 11],
        [1],
        [1, 2, 3, 4],
        [1]
    ]
    for t in tasks:
        assert sol.swapPairs(list_to_list_node(t)) == list_to_list_node(swap_list(t, 2))
