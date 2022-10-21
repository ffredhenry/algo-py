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

# bubble sort operation
for i in range(len(numdata)):
        for j in range(0,len(numdata)-i-1):
            if numdata[j] > numdata[j+1]:
                numdata[j], numdata[j+1] = numdata[j+1], numdata[j]

# finishing up
print("writing to file")
io.egressCSV(numdata,target)
