#!/bin/python3

# ---------- Tripler
# Serves as a proof-of-concept for CSV importation
# and manipulation of its elements in a created list.


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
