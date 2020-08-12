#! /usr/bin/env python
"""Quick sort
"""
from utils import initdata
import time
trg_list = initdata.generate(10)
trg_list = [10, 12, 15, 3, 8, 17, 4, 1]
print("input: ", trg_list)


def quick_sort(lst: list, left, right):
    if right - left <= 1:
        return

    p = int((left+right)/2)
    pivot = lst[p]

    tmp = lst[right-1]
    lst[right-1] = lst[p]
    lst[p] = tmp

    i = left
    for j in range(left, right-1):
        if lst[j] < pivot:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            i += 1
    tmp = lst[i]
    lst[i] = lst[right-1]
    lst[right-1] = tmp

    print(lst, left, right, i, j)
    quick_sort(lst, left, i)
    quick_sort(lst, i+1, right)

    return


start = time.time()
quick_sort(trg_list, 0, len(trg_list))
elapsed = time.time() - start

print("elapsed time: ", elapsed)
print(trg_list)