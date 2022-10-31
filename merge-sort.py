#!/bin/python3

# ---------- Merge Sort Algorithm



# ---------- Imported modules
import inputoutput as io
import csv
import sys


# ---------- Main
target = sys.argv[1]

# ingress of data
numdata = io.ingressCSV(target)

# merge sorting
def mergeSort(data):
    if len(data) > 1:
        # perition out list
        middie = len(data) // 2
        leftmost = data[:middie]
        ritemost = data[middie:]

        # sorting left and right recursively
        mergeSort(leftmost)
        mergeSort(ritemost)

        # iterator initializations
        i = j = k = 0

        # populating temporary arrays with data
        while i < len(leftmost) and j < len(ritemost):
            if leftmost[i] <= ritemost[j]:
                data[k] = leftmost[i]
                i += 1
            else:
                data[k] = ritemost[j]
                j += 1

            k += 1

        # cleanup for any elements left behind
        while i < len(leftmost):
            data[k] = leftmost[i]
            i += 1
            k += 1

        while j < len(ritemost):
            data[k] = ritemost[j]
            j += 1
            k += 1

# calling the function
mergeSort(numdata)

# finishing up and appending "-mergesorted" to CSV
target = target[:-4]+"-mergesorted"+target[-4:]
print("Sorting done, writing to file!")
io.egressCSV(numdata,target)
