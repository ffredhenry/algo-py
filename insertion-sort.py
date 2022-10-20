#!/bin/python3

import inputoutput as io
import csv
import sys


# insertion sort algorithm, as function
def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # left comparison
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        # move key after element smaller than it
        data[j + 1] = key

testarr = [99,77,44,22,11,33]
print(testarr)
insertionSort(testarr)
#FIXME: no return argument needed!

print(testarr)