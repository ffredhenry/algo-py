#!/bin/python3

# ---------- Quick Sort
# Python implementation of the quick sort algorithm
# performed against a randomly-generated list of numbers


# ---------- Imported modules
import inputoutput as io
import csv
import sys


# ---------- Main
target = sys.argv[1]

# ingress of data
numdata = io.ingressCSV(target)

# quick sort algorithm, defined as a function to enable recursive calling
def quickSort(data):
    if(len(data)>1):
        pivot = int(len(data)/2)
        vcomp = data[pivot]

        leftmost = [i for i in data if i < vcomp]
        middie = [i for i in data if i == vcomp]
        ritemost = [i for i in data if i > vcomp]

        # recursively calling the quickSort function
        recursor = quickSort(leftmost) + middie + quickSort(ritemost)
        return recursor
    else:
        return data

# running quicksort against the ingressed data
numdata = quickSort(numdata)

# finishing up
print("Sort complete, writing to file!")
io.egressCSV(numdata,target)
