from util.util import ListNode, list_to_list_node


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num = 0
        for ln in (l1, l2):
            dig = 0
            while ln:
                num += ln.val * 10 ** dig
                dig += 1
                ln = ln.next
        if num < 10:
            return ListNode(num)
        result_node = ListNode()
        cur_node = result_node
        while True:
            cur_node.val = num % 10
            num //= 10
            if num == 0:
                break
            cur_node.next = ListNode()
            cur_node = cur_node.next
        return result_node


if __name__ == '__main__':
    s = Solution()
    assert s.addTwoNumbers(list_to_list_node([2, 4, 3]), list_to_list_node([5, 6, 4])) == list_to_list_node([7, 0, 8])
    assert s.addTwoNumbers(list_to_list_node([0]), list_to_list_node([0])) == list_to_list_node([0])
    assert (s.addTwoNumbers(list_to_list_node([9, 9, 9, 9, 9, 9, 9]), list_to_list_node([9, 9, 9, 9])) ==
            list_to_list_node([8, 9, 9, 9, 0, 0, 0, 1]))
