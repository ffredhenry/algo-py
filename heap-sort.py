#!/bin/python3

# ---------- Heap Sort Algorithm
# 


# ---------- Imported modules
import inputoutput as io
import csv
import sys


# ---------- Main
target = sys.argv[1]

# ingress of data
numdata = io.ingressCSV(target)


# Heap function (set up for algorithm)
def heapMake(data, node, root):
    
    # create root and define left and right tree branches
    maxi = root
    left = 2 * root + 1
    rite = 2 * root + 2

    # check for existence of left child and if so, compare to root
    if left < node and data[maxi] < data[left]:
        maxi = left

    # check for existence of right child and if so, compare to root
    if rite < node and data[maxi] < data[rite]:
        maxi = rite

    # if needed change out root value using a swap assignment
    if maxi != root:
        data[root], data[maxi] = data[maxi], data[root]

        # recursively make root into a heap
        heapMake(data, node, maxi)


# Algorithm
def heapSort(atad):
    span = len(atad)

    # buildup heap
    for i in range(span // 2 - 1, -1, -1):
        heapMake(atad, span, i)

    # extract heap elements single-file
    for i in range(span - 1, 0, -1):
        # swap assignment
        atad[i], atad[0] = atad[0], atad[i]
        heapMake(atad, i, 0)

# using sorting algorithm
heapSort(numdata)

# finishing up
print("Sorting done! Writing to file")
io.egressCSV(numdata,target)
