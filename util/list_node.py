from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return f'[{self.val}] {self.next}'

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        nodes = [self, other]
        while any(nodes):
            if any(nodes) and not all(nodes):
                return False
            if nodes[0].val != nodes[1].val:
                return False
            nodes[0] = nodes[0].next
            nodes[1] = nodes[1].next
        return True

    @staticmethod
    def list_node_to_list(head: ListNode) -> list[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    @staticmethod
    def list_to_list_node(lst: list[int]) -> ListNode | None:
        if not lst:
            return
        head = ListNode(lst[0])
        tail = head
        for val in lst[1:]:
            tail.next = ListNode(val)
            tail = tail.next
        return head


if __name__ == "__main__":
    assert ListNode.list_to_list_node([1, 2, 3]) == ListNode.list_to_list_node([1, 2, 3])
    assert ListNode.list_to_list_node([1, 2, 3]) != ListNode.list_to_list_node([1, 2])
    assert ListNode.list_to_list_node([1, 2, 3]) != ListNode.list_to_list_node([])
    assert ListNode.list_to_list_node([1, 2, 3]) != [1,2,3]
