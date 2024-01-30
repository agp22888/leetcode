from collections import Counter


def swap_list(lst: list[int], k: int) -> list[int]:
    if k >= 2 and k <= len(lst):
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
