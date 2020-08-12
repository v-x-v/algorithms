#! /usr/bin/env python
"""Insertion sort
"""
from utils import initdata
import time
trg_list = initdata.generate(10)
print("input: ", trg_list)

start = time.time()
for i, item in enumerate(trg_list[1:], 1):
    for j in reversed(range(i)):
        if item < trg_list[j]:
            trg_list[j+1] = trg_list[j]
        else:
            j += 1
            break
    trg_list[j] = item

elapsed = time.time() - start
print("sorted: ", trg_list)
print("elapsed time: ", elapsed)
