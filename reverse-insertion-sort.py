#!/bin/python3

# --------- REVERSE Insertion Sort Algorithm
# Implementation of algorithm in python

# --------- Imported modules
import inputoutput as io
import csv
import sys


# ingressing data through cli arguments and imported modules
target = sys.argv[1]
numdata = io.ingressCSV(target)

# insertion sort algorithm, as function
def insertionSort(data):
    for i in range(1, len(data)):
        # setting the key to the current entry in row
        key = data[i]
        # 
        j = i - 1

        # left comparison FIXME: flipped key < data[j]
        while j >= 0 and key > data[j]:
            data[j + 1] = data[j]
            j = j - 1

        # move key after element smaller than it
        data[j + 1] = key

# sorting call
insertionSort(numdata)

# wrapping up and appending "-insertionsorted" to CSV
target = target[:-4]+"-REV-insertionsorted"+target[-4:]
print("Sorting done! Writing to file.")
io.egressCSV(numdata,target)
