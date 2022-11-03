#!/bin/python3

# ---------- Selection Sort
# Python implementation of the selection sort algorithm
# n^n complexity, so it will start to chug on larger datasets.


# ---------- Imported modules
import inputoutput as io
import csv
import sys


# ---------- Main

# ingress of data
target = sys.argv[1]
numdata = io.ingressCSV(target)

# selection sort algorithm
for i in range(len(numdata)):
    mindex = i
    
    for j in range(i+1, len(numdata)):
        if numdata[mindex] > numdata[j]:
            mindex = j

    # updating values using simultaneous assignments
    numdata[i], numdata[mindex] =  numdata[mindex], numdata[i]

# finishing up, appending identifier to file
target = target[:-4]+"-selection"+target[-4:]
print("Sorting complete, writing to file!")
io.egressCSV(numdata,target)
