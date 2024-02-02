from functools import reduce

from util.util import ListNode, list_to_list_node


class Solution:
    # the fastest but cheating
    def mergeKLists_(self, lists: list[ListNode | None]) -> ListNode | None:
        storage = []
        for node in lists:
            while node:
                storage.append(node)
                node = node.next
        if storage:
            storage.sort(key=lambda x: x.val)
            for i in range(len(storage) - 1):
                storage[i].next = storage[i + 1]
            return storage[0]
        else:
            return None

    # slowest
    def mergeKLists__(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return
        head = None
        tail = None
        while any(lists):
            if head is None:
                head = min(lists, key=lambda x: x.val if x is not None else 10001)
                tail = head
            inc_list_index = lists.index(tail)
            lists[inc_list_index] = tail.next
            if not any(lists):
                break
            tail.next = min(lists, key=lambda x: x.val if x is not None else 10001)
            tail = tail.next
        return head

    # slightly faster than slowest
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        head = None
        tail = None
        to_delete = []
        while any(lists):
            to_delete.clear()
            min_val = None
            min_ind = -1
            for i in range(len(lists)):
                if not lists[i]:
                    to_delete.append(i)
                    continue
                if min_val is None:
                    min_val = lists[i].val
                    min_ind = i
                    continue
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_ind = i
            if not head:
                head = tail = lists[min_ind]
            else:
                tail.next = lists[min_ind]
                tail = tail.next
            lists[min_ind] = lists[min_ind].next
            for i in to_delete[::-1]:
                lists.pop(i)

        return head


if __name__ == "__main__":
    sol = Solution()
    tasks = [
        [[1, 4, 5], [1, 3, 4], [2, 6]],
        [],
        [[]],
        [[], [-1, 5, 11], [], [6, 10]]
    ]

    for t in tasks:
        orig_node_list = [list_to_list_node(x) for x in t]
        result_node_list = list_to_list_node(sorted(reduce(lambda x, y: x + y, t, [])))
        assert sol.mergeKLists(orig_node_list) == result_node_list
