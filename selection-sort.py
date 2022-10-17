#!/bin/python3

# ---------- title



# ---------- Imported modules
import inputoutput as io
import csv
import sys


# ---------- Main
target = sys.argv[1]

# ingress of data
numdata = io.ingressCSV(target)

# selection sort algorithm
for i in range(len(numdata)):
    mindex = i
    
    for j in range(i+1, len(numdata)):
        if numdata[mindex] > numdata[j]:
            mindex = j

    # updating values - trying without simulatenous assignment
    numdata[i], numdata[mindex] =  numdata[mindex], numdata[i]

# finishing up
print("writing to file")
io.egressCSV(numdata,target)
