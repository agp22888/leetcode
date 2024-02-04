import time
from functools import wraps


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return f'[{self.val}]'

    def __str__(self):
        return f'[{self.val}] {str(self.next)}'

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


def list_node_to_list(head: ListNode) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def list_to_list_node(lst: list[int]) -> ListNode | None:
    if not lst:
        return
    head = ListNode(lst[0])
    tail = head
    for val in lst[1:]:
        tail.next = ListNode(val)
        tail = tail.next
    return head


def swap_list(lst: list[int], k: int) -> list[int]:
    if 2 <= k <= len(lst):
        for i in range(0, len(lst), k):
            if len(lst) - i < k:
                break
            stop = -len(lst) - 1 + i
            start = -len(lst) - 1 + i + k
            step = -1
            new_lst = lst[start:stop:step]
            lst[i:i + k] = new_lst
            # print(new_lst)
    # print(lst)
    return lst


def compare_list_of_ints_ignore_order(lst1: list[list[int]], lst2: list[list[int]]) -> bool:
    for l in lst1:
        l.sort()
    for l in lst2:
        l.sort()
    lst1.sort()
    lst2.sort()
    return lst1 == lst2


def compare_list_ignore_order(lst1: list, lst2: list) -> bool:
    lst1.sort()
    lst2.sort()
    return lst1 == lst2


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} - {total_time}')
        return result

    return inner


if __name__ == "__main__":
    assert swap_list([1, 2, 3, 4, 5], 2) == [2, 1, 4, 3, 5]
    assert swap_list([1, 2, 3, 4, 5], 3) == [3, 2, 1, 4, 5]
    assert swap_list([1, 2, 3, 4, 5], 4) == [4, 3, 2, 1, 5]
    assert swap_list([1, 2, 3, 4, 5, 6], 2) == [2, 1, 4, 3, 6, 5]
    assert swap_list([1, 2, 3, 4, 5, 6], 3) == [3, 2, 1, 6, 5, 4]
    assert swap_list([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
    assert swap_list([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6]
    assert swap_list([1, 2, 3, 4, 5, 6], 6) == [6, 5, 4, 3, 2, 1]
    assert swap_list([1, 2], 3) == [1, 2]
    assert swap_list([], 1) == []

    assert list_to_list_node([1, 2, 3]) == list_to_list_node([1, 2, 3])
    assert list_to_list_node([1, 2, 3]) != list_to_list_node([1, 2])
    assert list_to_list_node([1, 2, 3]) != list_to_list_node([])
    assert list_to_list_node([1, 2, 3]) != [1, 2, 3]
