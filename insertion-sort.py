#!/bin/python3

# --------- Insertion Sort Algorithm
# Implementation of algorithm in python

# --------- Imported modules
import inputoutput as io
import csv
import sys


# ingressing
target = sys.argv[1]
numdata = io.ingressCSV(target)

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

# sorting call
insertionSort(numdata)

# wrapping up and appending "-insertionsorted" to CSV
target = target[:-4]+"-insertion"+target[-4:]
print("Sorting done! Writing to file.")
io.egressCSV(numdata,target)
