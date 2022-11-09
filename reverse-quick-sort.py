#!/bin/python3

# ---------- Quick Sort
# Python implementation of the quick sort algorithm
# performed against a randomly-generated list of numbers
# Uses return arguments in the recursively called quickSort()
# function


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

        leftmost = [i for i in data if i > vcomp]#FIXME: swapping comparator from < to >
        middie = [i for i in data if i == vcomp]
        ritemost = [i for i in data if i < vcomp]#FIXME: swapping comparator from > to <

        # recursively calling the quickSort function
        recursor = quickSort(leftmost) + middie + quickSort(ritemost)
        return recursor
    else:
        return data

# running quicksort against the ingressed data
numdata = quickSort(numdata)

# finishing up and appending "-quicksorted" to CSV
target = target[:-4]+"-reverse-quick"+target[-4:]
print("Sort complete, writing to file!")
io.egressCSV(numdata,target)
