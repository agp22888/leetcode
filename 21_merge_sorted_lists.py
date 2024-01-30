from util.util import ListNode, list_to_list_node


class Solution:
    def min_node(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        return min(list1, list2, key=lambda x: x.val)

    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = None
        tail = None
        while list1 and list2:
            if head is None:
                head = self.min_node(list1, list2)
                tail = head
            if tail is list1:
                list1 = list1.next
            elif tail is list2:
                list2 = list2.next
            tail.next = self.min_node(list1, list2)
            tail = tail.next
        if not tail:
            return list1 if list1 else list2
        if list1 is not None:
            tail.next = list1.next
        elif list2 is not None:
            tail.next = list2.next
        return head


if __name__ == "__main__":
    s = Solution()

    assert s.mergeTwoLists(list_to_list_node([1, 2, 4]), list_to_list_node([1, 3, 4])) == list_to_list_node(
        [1, 1, 2, 3, 4, 4])
    assert s.mergeTwoLists(list_to_list_node([]), list_to_list_node([])) == list_to_list_node([])
    assert s.mergeTwoLists(list_to_list_node([]), list_to_list_node([0])) == list_to_list_node([0])
