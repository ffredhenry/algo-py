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

# arithmetic operation
for i in range(len(numdata)):
    numdata[i] = 3 * numdata[i]

# finishing up
print("writing to file")
io.egressCSV(numdata,target)
