#! /usr/bin/env python
"""Merge sort
"""
from utils import initdata
import time
trg_list = initdata.generate(10000)
print("input: ", trg_list)


def merge_sort(lst: list) -> list:
    length = len(lst)
    if length <= 1:
        return lst
    mid = int(length/2)

    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    sorted_list = []
    while True:
        if left_list[0] < right_list[0]:
            sorted_list.append(left_list.pop(0))
            if len(left_list) <= 0:
                sorted_list.extend(right_list)
                break
        else:
            sorted_list.append(right_list.pop(0))
            if len(right_list) <= 0:
                sorted_list.extend(left_list)
                break
    return sorted_list


start = time.time()
trg_list = merge_sort(trg_list)

elapsed = time.time() - start
print("sorted: ", trg_list)
print("elapsed time: ", elapsed)
